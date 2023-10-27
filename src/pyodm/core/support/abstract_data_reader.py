import abc
import pathlib

from pyodm.factory.cdisc_registry import CdiscRegistry


class AbstractDataReader(abc.ABC):

    """
    读去数据的抽象方法,定义抽象方法 read()
    """
    def __init__(self, registry: CdiscRegistry):
        self._registry = registry

    @property
    def registry(self): return self._registry

    @abc.abstractmethod
    def read(self, file:  pathlib.Path): ...