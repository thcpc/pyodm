import abc
import pathlib

from pyodm.factory.cdisc_registry import CdiscRegistry


class AbstractDataReader(abc.ABC):
    def __init__(self, registry: CdiscRegistry):
        self._registry = registry

    @property
    def registry(self): return self._registry

    @abc.abstractmethod
    def read(self, file:  pathlib.Path): ...
