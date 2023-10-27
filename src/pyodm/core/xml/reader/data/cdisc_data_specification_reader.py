import importlib

from pyodm.core.xml.reader.abstract_xml_data_reader import AbstractXMLDataReader


class CdiscDataSpecificationReader(AbstractXMLDataReader):
    """
    根据 Specifincation的方式，读取XML数据， 实例化 ODM 对象
    """
    def _new_cdisc_node(self, cdisc_name):
        clazz_info = self.registry.get(cdisc_name)
        module = importlib.import_module(clazz_info.get("modulePath"))
        new_obj = getattr(module, clazz_info.get("clazz"))()
        return new_obj
