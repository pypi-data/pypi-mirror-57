import os
import pydicom
import shutil
import zipfile

from datetime import datetime
from django_dicom.models.patient import Patient
from django_dicom.models.series import Series
from django_dicom.models.study import Study
from django_dicom.models.validators import digits_and_dots_only
from django.db.utils import IntegrityError
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import models
from django.urls import reverse


class InstanceManager(models.Manager):
    def from_dcm(self, file):
        dest_name = default_storage.save('tmp.dcm', ContentFile(file.read()))
        instance = Instance()
        instance.file = dest_name
        try:
            instance.save()
        except IntegrityError:
            dest_path = os.path.join(settings.MEDIA_ROOT, dest_name)
            uid = pydicom.dcmread(dest_path).SOPInstanceUID
            os.remove(dest_path)
            return Instance.objects.filter(instance_uid=uid).first()
        return instance

    def from_zip(self, file):
        dest_name = default_storage.save('tmp.zip', ContentFile(file.read()))
        dest_path = os.path.join(settings.MEDIA_ROOT, dest_name)
        with zipfile.ZipFile(dest_path, 'r') as archive:
            for file_name in archive.namelist():
                if file_name.endswith('.dcm'):
                    with archive.open(file_name) as dcm_file:
                        self.from_dcm(dcm_file)
        os.remove(dest_path)

    def from_local_directory(self, path: str):
        for directory, sub_directory, file_list in os.walk(path):
            for file_name in file_list:
                if file_name.endswith('.dcm'):
                    full_path = os.path.join(directory, file_name)
                    with open(full_path, 'rb') as f:
                        self.from_dcm(f)


class Instance(models.Model):
    _headers = None
    SEX_DICT = {'M': 'MALE', 'F': 'FEMALE', 'O': 'OTHER'}

    instance_uid = models.CharField(
        max_length=64,
        unique=True,
        blank=False,
        null=False,
        validators=[digits_and_dots_only],
        verbose_name='Instance UID',
    )

    file = models.FileField(upload_to='dicom', blank=True)
    number = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Instance Number',
    )
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    series = models.ForeignKey(
        Series, blank=True, null=True, on_delete=models.PROTECT)
    study = models.ForeignKey(
        Study, blank=True, null=True, on_delete=models.PROTECT)
    patient = models.ForeignKey(
        Patient, blank=True, null=True, on_delete=models.PROTECT)

    objects = InstanceManager()

    def __str__(self):
        return self.instance_uid

    def get_absolute_url(self):
        return reverse('dicom:instance_detail', args=[str(self.id)])

    def read_data(self) -> pydicom.dataset.FileDataset:
        return pydicom.dcmread(self.file.path)

    def read_headers(self) -> pydicom.dataset.FileDataset:
        return pydicom.dcmread(self.file.path, stop_before_pixels=True)

    def parse_date_element(self, value: str) -> datetime.date:
        """
        Parses DA elements to date objects.

        :param value: DA element value.
        :type value: str
        :return: Date.
        :rtype: datetime.date
        """
        return datetime.strptime(value, '%Y%m%d').date()

    def parse_time_element(self, value: str) -> datetime.time:
        """
        Parses TM elements to time objects.

        :param value: TM element value.
        :type value: str
        :return: Time.
        :rtype: datetime.time
        """
        return datetime.strptime(value, '%H%M%S.%f').time()

    def get_series_attributes(self) -> dict:
        return {
            'series_uid': self.headers.SeriesInstanceUID,
            'number': int(self.headers.SeriesNumber),
            'date': self.parse_date_element(self.headers.SeriesDate),
            'time': self.parse_time_element(self.headers.SeriesTime),
            'description': self.headers.SeriesDescription,
            'study': self.get_study(),
            'patient': self.get_patient(),
        }

    def create_series(self) -> Series:
        return Series.objects.create(**self.get_series_attributes())

    def get_series(self) -> Series:
        series_uid = self.headers.SeriesInstanceUID
        series = Series.objects.filter(series_uid=series_uid).first()
        if not series:
            series = self.create_series()
        return series

    def get_study_attributes(self) -> dict:
        return {
            'study_uid': self.headers.StudyInstanceUID,
            'date': self.parse_date_element(self.headers.StudyDate),
            'time': self.parse_time_element(self.headers.StudyTime),
            'description': self.headers.StudyDescription,
        }

    def create_study(self) -> Study:
        return Study.objects.create(**self.get_study_attributes())

    def get_study(self) -> Study:
        study_uid = self.headers.StudyInstanceUID
        study = Study.objects.filter(study_uid=study_uid).first()
        if not study:
            study = self.create_study()
        return study

    def get_patient_attributes(self) -> dict:
        return {
            'patient_id':
            self.headers.PatientID,
            'given_name':
            self.headers.PatientName.given_name,
            'family_name':
            self.headers.PatientName.family_name,
            'middle_name':
            self.headers.PatientName.middle_name,
            'name_prefix':
            self.headers.PatientName.name_prefix,
            'name_suffix':
            self.headers.PatientName.name_suffix,
            'date_of_birth':
            self.parse_date_element(self.headers.PatientBirthDate),
            'sex':
            self.SEX_DICT[self.headers.PatientSex],
        }

    def create_patient(self) -> Patient:
        return Patient.objects.create(**self.get_patient_attributes())

    def get_patient(self) -> Patient:
        patient_id = self.headers.PatientID
        patient = Patient.objects.filter(patient_id=patient_id).first()
        if not patient:
            patient = self.create_patient()
        return patient

    def get_attributes_from_file(self) -> dict:
        return {
            'instance_uid': self.headers.SOPInstanceUID,
            'number': int(self.headers.InstanceNumber),
            'date': self.parse_date_element(self.headers.InstanceCreationDate),
            'time': self.parse_time_element(self.headers.InstanceCreationTime),
            'series': self.get_series(),
            'study': self.get_study(),
            'patient': self.get_patient(),
        }

    def update_attributes_from_file(self) -> None:
        attributes = self.get_attributes_from_file()
        for key, value in attributes.items():
            setattr(self, key, value)

    def get_default_file_name(self) -> str:
        return os.path.join(
            'MRI', 
            self.headers.PatientID,
            self.headers.SeriesInstanceUID,
            'DICOM',
            f'{self.number}.dcm',
        )

    def move_file(self, new_name: str = None) -> None:
        """
        Move the 'file' FileField attribute from its current location to
        another location relative to MEDIA_ROOT.

        :param new_name: New relative path, defaults to None (default path)
        :param new_name: str, optional
        :return:
        :rtype: None
        """
        new_name = new_name or self.get_default_file_name()
        initial_path = self.file.path
        self.file.name = new_name
        new_path = os.path.join(settings.MEDIA_ROOT, self.file.name)
        os.makedirs(os.path.dirname(new_path), exist_ok=True)
        os.rename(initial_path, new_path)

    def create_backup(self, dest: str):
        shutil.copyfile(self.file.path, dest)
        self.has_raw_backup = True
        self.save()

    @property
    def headers(self):
        if self._headers is None:
            self._headers = self.read_headers()
        return self._headers
