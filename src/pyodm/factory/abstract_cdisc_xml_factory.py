import abc
import pathlib

from pyodm.core.xml.reader.data.xml_data_reader import XMLDataReader
from pyodm.factory.abstract_cdisc_factory import AbstractCdiscFactory


class AbstractCdiscXMLFactory(AbstractCdiscFactory):
    """
    通过 XML 生成ODM的工程对象的类型，定义了生成模板
        1. 获取 Class 类型 class_reader
        2. 读取 XML 文件转化为ODM 对象 data_reader
    """
    def __init__(self, data_file: pathlib.Path):
        super().__init__()
        self._data_file = data_file

    @abc.abstractmethod
    def clazz_reader(self): ...

    @abc.abstractmethod
    def data_reader(self) -> XMLDataReader: ...

    # Override
    def _odm_process(self):
        if self._cdisc_odm is None:
            self.clazz_reader()
            self._cdisc_odm = self.data_reader().read(self._data_file)
        return self._cdisc_odm
