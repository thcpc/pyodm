import abc
from abc import ABC

from pyodmv2.odm_source import ODMSource
from pyodmv2.utils.forest import Forest


class ODM(ABC):

    def __init__(self):
        self._odm = None

    @property
    def odm(self) -> Forest: return self._odm

    @odm.setter
    def odm(self, source: ODMSource):
        self._odm = Forest.transform(source.data())

    @abc.abstractmethod
    def v2(self):
        """
        非标准数据转为ODM V2 标准数据
        :return:
        :rtype:
        """
        ...


def odm_factory(odm_clazz: ODM.__class__, source: ODMSource) -> ODM:
    obj = odm_clazz()
    obj.odm = source
    return obj
