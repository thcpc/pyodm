import abc

from pyodm.factory.cdisc_registry import CdiscRegistry


class AbstractCdiscFactory(abc.ABC, CdiscRegistry):
    """
    生成ODM的抽象工程类型

    """
    def __init__(self):
        super().__init__()
        self._cdisc_odm = None

    @abc.abstractmethod
    def _odm_process(self): ...
    @property
    def odm(self): return self._odm_process()
