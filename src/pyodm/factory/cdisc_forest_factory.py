from pyodm.core.forest.reader.forest_data_reader import ForestDataReader

from pyodm.core.xml.reader.configuration.cdisc_configuration_xsd_reader import CdiscConfigurationXsdReader
from pyodm.factory.abstract_cdisc_factory import AbstractCdiscFactory


class CdiscForestFactory(AbstractCdiscFactory):

    def __init__(self, configuration_files: list):
        super().__init__()
        self._configuration_files = configuration_files
        self._reader_class = CdiscConfigurationXsdReader

    @property
    def reader_class(self): return self._reader_class

    @reader_class.setter
    def reader_class(self, clazz): self._reader_class = clazz

    def clazz_reader(self):
        self._reader_class().load_cdisc_definition(self, self._configuration_files)

    def data_reader(self) -> ForestDataReader:
        return ForestDataReader(self)
