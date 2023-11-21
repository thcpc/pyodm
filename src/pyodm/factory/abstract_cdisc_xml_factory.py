import pathlib
from abc import ABC

from pyodm.core.resource.xml_path_resoruce import XmlPathResource
from pyodm.core.xml.reader.data.xml_data_reader import XMLDataReader
from pyodm.factory.abstract_cdisc_factory import AbstractCdiscFactory


class AbstractCdiscXMLFactory(AbstractCdiscFactory, ABC):
    """
    通过 XML 生成ODM的工程对象的类型，定义了生成模板
        1. 获取 Class 类型 class_reader
        2. 读取 XML 文件转化为ODM 对象 data_reader
    """

    def __init__(self, data_file: pathlib.Path):
        super().__init__()
        self._data_file = data_file
        self.data_resource = XmlPathResource(self._data_file)

    def data_reader(self) -> XMLDataReader: return XMLDataReader(self)


