# django-dicom



A django app to manage [DICOM][1] files.

This app creates the basic models for DICOM data abstraction: Study, Patient, Series, and Image.  
The models are complemented with some utility methods to facilitate data access.



Quick start
-----------

1. Add "django_dicom" to your INSTALLED_APPS setting:

<pre>
    INSTALLED_APPS = [  
        ...  
        'django_dicom',  
    ]  
</pre>

2. Include the dicom URLconf in your project urls.py:

<pre>
    path('dicom/', include('django_dicom.urls')),
</pre>

3. Run `python manage.py migrate` to create the dicom models.

4. Start the development server and visit http://127.0.0.1:8000/admin/.

5. Visit http://127.0.0.1:8000/dicom/.




[1]: https://www.dicomstandard.org/
