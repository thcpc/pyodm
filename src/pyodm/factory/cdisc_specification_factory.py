import importlib
import pathlib

from pyodm.core.xml.reader.abstract_configuration_reader import AbstractConfigurationReader
from pyodm.core.xml.reader.abstract_xml_data_reader import AbstractXMLDataReader
from pyodm.core.xml.reader.configuration.cdisc_configuration_specification_reader import \
    CdiscConfigurationSpecificationReader
from pyodm.core.xml.reader.data.cdisc_data_specification_reader import CdiscDataSpecificationReader
from pyodm.factory.abstract_cdisc_xml_factory import AbstractCdiscXMLFactory


class CdiscSpecificationFactory(AbstractCdiscXMLFactory):
    def __init__(self, data_file: pathlib.Path, specification_files: list):
        super().__init__(data_file)
        self._specification_files = specification_files

    def clazz_reader(self):
        CdiscConfigurationSpecificationReader().load_cdisc_definition(self, self._specification_files)

    def data_reader(self) -> AbstractXMLDataReader:
        return CdiscDataSpecificationReader(self)

