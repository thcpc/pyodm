import abc
import pathlib

from pyodm.core.xml.reader.abstract_xml_data_reader import AbstractXMLDataReader
from pyodm.factory.abstract_cdisc_factory import AbstractCdiscFactory


class AbstractCdiscXMLFactory(AbstractCdiscFactory):
    def __init__(self, data_file: pathlib.Path):
        super().__init__()
        self._data_file = data_file

    @abc.abstractmethod
    def clazz_reader(self): ...

    @abc.abstractmethod
    def data_reader(self) -> AbstractXMLDataReader: ...

    # Override
    def _odm_process(self):
        if self._cdisc_odm is None:
            self.clazz_reader()
            self._cdisc_odm = self.data_reader().read(self._data_file)
        return self._cdisc_odm
