import abc

from pyodm.core.support.abstract_data_reader import AbstractDataReader
from pyodm.core.support.abstract_resource import AbstractResource
from pyodm.factory.cdisc_registry import CdiscRegistry


class AbstractCdiscFactory(abc.ABC, CdiscRegistry):
    """
    生成ODM的抽象工程类型

    """

    def __init__(self):
        super().__init__()
        self._cdisc_odm = None
        self._data_resource = None

    @abc.abstractmethod
    def clazz_reader(self): ...

    @abc.abstractmethod
    def data_reader(self) -> AbstractDataReader: ...

    @property
    def data_resource(self):
        return self._data_resource

    @data_resource.setter
    def data_resource(self, resource: AbstractResource):
        self._data_resource = resource

    def _odm_process(self, refresh: bool = False):
        __new = True if self._cdisc_odm is None else refresh
        if __new:
            self.clazz_reader()
            self._cdisc_odm = self.data_reader().read(self.data_resource)
        return self._cdisc_odm

    def odm(self, refresh: bool = False):
        return self._odm_process(refresh)
