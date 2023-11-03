import pathlib

from pyodm.core.xml.reader.data.xml_data_reader import XMLDataReader
from pyodm.core.xml.reader.configuration.cdisc_configuration_xsd_reader import CdiscConfigurationXsdReader
from pyodm.factory.abstract_cdisc_xml_factory import AbstractCdiscXMLFactory


class CdiscXsdFactory(AbstractCdiscXMLFactory):
    """
    Class 类型的定义在XSD文件中
    """
    def data_reader(self) -> XMLDataReader:
        return XMLDataReader(self)

    def __init__(self, data_file: pathlib.Path, xsd_files: list):
        super().__init__(data_file)
        self._xsd_files = xsd_files

    def clazz_reader(self):
        CdiscConfigurationXsdReader().load_cdisc_definition(self, self._xsd_files)



