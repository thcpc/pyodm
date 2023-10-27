import pathlib

from pyodm.core.xml.reader.abstract_xml_data_reader import AbstractXMLDataReader
from pyodm.core.xml.reader.configuration.cdisc_configuration_xsd_reader import CdiscConfigurationXsdReader
from pyodm.core.xml.reader.data.cdisc_data_xsd_reader import CdiscDataXsdReader
from pyodm.factory.abstract_cdisc_xml_factory import AbstractCdiscXMLFactory


class CdiscXsdFactory(AbstractCdiscXMLFactory):

    def data_reader(self) -> AbstractXMLDataReader:
        return CdiscDataXsdReader(self)

    def __init__(self, data_file: pathlib.Path, xsd_files: list):
        super().__init__(data_file)
        self._xsd_files = xsd_files

    def clazz_reader(self):
        CdiscConfigurationXsdReader().load_cdisc_definition(self, self._xsd_files)



