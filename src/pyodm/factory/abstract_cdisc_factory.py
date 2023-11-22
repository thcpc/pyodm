import abc

from pyodm.core.support.abstract_data_reader import AbstractDataReader
from pyodm.core.support.abstract_data_loader import AbstractDataLoader
from pyodm.factory.cdisc_registry import CdiscRegistry
from pyodm.model import odm_xsd_description


class AbstractCdiscFactory(abc.ABC, CdiscRegistry):
    """
    生成ODM的抽象工程类型

    """

    def __init__(self):
        super().__init__()
        self._cdisc_odm = None
        self._data_loader = None

    def default_description_files(self) -> list:
        return odm_xsd_description()

    @abc.abstractmethod
    def clazz_reader(self): ...

    @abc.abstractmethod
    def data_reader(self) -> AbstractDataReader: ...

    @property
    def data_loader(self):
        return self._data_loader

    @data_loader.setter
    def data_loader(self, data_loader: AbstractDataLoader):
        self._data_loader = data_loader

    def _odm_process(self, refresh: bool = False):
        __new = True if self._cdisc_odm is None else refresh
        if __new:
            self.clazz_reader()
            self._cdisc_odm = self.data_reader().read(self.data_loader)
        return self._cdisc_odm

    def odm(self, refresh: bool = False):
        return self._odm_process(refresh)
