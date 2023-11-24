import abc

from pyodm.core.support.abstract_data_reader import AbstractDataReader
from pyodm.core.support.abstract_data_loader import AbstractDataLoader
from pyodm.factory.cdisc_registry import CdiscRegistry
from pyodm.model import odm_xsd_description


class AbstractCdiscFactory(abc.ABC, CdiscRegistry):
    """
    生成 ODM 的抽象工厂,定义类生成ODM实例的模板方法

    """

    def __init__(self):
        super().__init__()
        self._cdisc_odm = None
        self._data_loader = None

    def default_description_files(self) -> list:
        """
        默认的 XSD 文件路径 , 如果没有指定
        clazz_reader,默认采取的是XSD 的方式解析 ODM Class
        :return:
        :rtype:
        """
        return odm_xsd_description()

    @abc.abstractmethod
    def clazz_reader(self):
        """
        指定 生成 ODM Class 的方式
        :return:
        :rtype:
        """
        ...

    @abc.abstractmethod
    def data_reader(self) -> AbstractDataReader:
        """
        指定 解析 ODM Data 的方式
        :return:
        :rtype:
        """
        ...

    @property
    def data_loader(self):
        """
        读取 ODM 数据
        :return:
        :rtype:
        """
        return self._data_loader

    @data_loader.setter
    def data_loader(self, data_loader: AbstractDataLoader):
        self._data_loader = data_loader

    def _odm_process(self, refresh: bool = False):
        """
        解析 ODM Data 模板方法
        :param refresh: 是否重新读取 True Y, False N
        :type refresh:
        :return:
        :rtype:
        """
        __new = True if self._cdisc_odm is None else refresh
        if __new:
            self.clazz_reader()
            self._cdisc_odm = self.data_reader().read(self.data_loader)
        return self._cdisc_odm

    def odm(self, refresh: bool = False):
        """
        返回 ODM 对象
        :param refresh:
        :type refresh:
        :return:
        :rtype:
        """
        return self._odm_process(refresh)
