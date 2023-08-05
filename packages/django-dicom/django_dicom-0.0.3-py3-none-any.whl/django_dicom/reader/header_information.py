from django_dicom.reader.parser import DicomParser
from pydicom.dataelem import DataElement
from pydicom.dataset import FileDataset


class HeaderInformation:
    """
    Facilitates access to DICOM_ header information from pydicom_'s FileDataset_.

    .. _DICOM: https://www.dicomstandard.org/
    .. _pydicom: https://github.com/pydicom/pydicom
    .. _FileDataset: https://github.com/pydicom/pydicom/blob/master/pydicom/dataset.py

    """

    def __init__(self, raw: FileDataset, parser: type = DicomParser):
        """
        HeaderInformation is meant to be initialized with a pydicom_ FileDataset_
        representing a single image's header.
        
        Parameters
        ----------
        header : pydicom.dataset.FileDataset
            DICOM_ image header information.
        parser : type
            An object with a public `parse()` method that may be used to parse
            data elements.
        
        .. _pydicom: https://github.com/pydicom/pydicom
        .. _FileDataset: https://github.com/pydicom/pydicom/blob/master/pydicom/dataset.py
        .. _DICOM: https://www.dicomstandard.org/

        """

        self.raw = raw
        self.parser = parser()

    def get_element_by_keyword(self, keyword: str) -> DataElement:
        """
        Returns a pydicom_ DataElement_ from the header (FileDataset_ isntance)
        by keyword.

        .. _pydicom: https://github.com/pydicom/pydicom
        .. _DataElement: https://github.com/pydicom/pydicom/blob/master/pydicom/dataelem.py
        .. _FileDataset: https://github.com/pydicom/pydicom/blob/master/pydicom/dataset.py
        
        Parameters
        ----------
        keyword : str
            The keyword representing the DICOM data element in pydicom.
        
        Returns
        -------
        DataElement
            The requested data element.
        """

        try:
            return self.raw.data_element(keyword)
        except KeyError:
            return None

    def get_element_by_tag(self, tag: tuple) -> DataElement:
        """
        Returns a pydicom_ DataElement_ from the header (FileDataset_ isntance)
        by tag.

        .. _pydicom: https://github.com/pydicom/pydicom
        .. _DataElement: https://github.com/pydicom/pydicom/blob/master/pydicom/dataelem.py
        .. _FileDataset: https://github.com/pydicom/pydicom/blob/master/pydicom/dataset.py
        
        Parameters
        ----------
        tag : tuple
            The DICOM tag of the desired data element.
        
        Returns
        -------
        DataElement
            The requested data element..
        """
        return self.raw.get(tag)

    def get_element(self, tag_or_keyword) -> DataElement:
        """
        Returns a pydicom_ DataElement_ from the associated FileDataset_ either by 
        tag (passed as a tuple) or a keyword (passed as a string). If none found
        or the tag or keyword are invalid, returns None.
        
        .. _pydicom: https://github.com/pydicom/pydicom
        .. _DataElement: https://github.com/pydicom/pydicom/blob/master/pydicom/dataelem.py
        .. _FileDataset: https://github.com/pydicom/pydicom/blob/master/pydicom/dataset.py

        Parameters
        ----------
        tag_or_keyword : tuple or str
            Tag or keyword representing the requested data element.
        
        Returns
        -------
        DataElement
            The requested data element.
        """

        # By keyword:
        if type(tag_or_keyword) is str:
            return self.get_element_by_keyword(tag_or_keyword)

        # By tag:
        elif type(tag_or_keyword) is tuple:
            return self.get_element_by_tag(tag_or_keyword)

        # else:
        return None

    def get_raw_value(self, tag_or_keyword):
        """
        Returns the raw value for the requested data element, as returned by
        pydicom_. If none is found will return None.

        .. _pydicom: https://github.com/pydicom/pydicom
        
        Parameters
        ----------
        tag_or_keyword : tuple or str
            Tag or keyword representing the requested data element.
        
        Returns
        -------
        type
            The raw value of the data element.
        """

        element = self.get_element(tag_or_keyword)
        try:
            return element.value
        except AttributeError:
            return None

    def get_parsed_value(self, tag_or_keyword):
        """
        Returns the parsed value of pydicom_ data element using the this class's
        parser attribute. The data element may be represented by tag or by its 
        pydicom_ keyword. If none is found will return None.
        
        .. _pydicom: https://github.com/pydicom/pydicom

        Parameters
        ----------
        tag_or_keyword : tuple or str
            Tag or keyword representing the requested data element.
        
        Returns
        -------
        type
            Parsed data element value.
        """

        element = self.get_element(tag_or_keyword)
        if element:
            return self.parser.parse(element)
        return None

    def get_value(self, tag_or_keyword, parsed: bool = True):
        """
        Returns the value of a pydicom data element, selected by tag (`tuple`) or 
        keyword (`str`). 
        
        Parameters
        ----------
        tag_or_keyword : tuple or str
            Tag or keyword representing the requested data element.
        parsed : bool, optional
            Whether to return a parsed or raw value (the default is True, which will return the parsed value).
        
        Returns
        -------
        type
            The requested data element value.
        """

        if parsed:
            return self.get_parsed_value(tag_or_keyword)
        return self.get_raw_value(tag_or_keyword)

