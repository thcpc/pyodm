from pyodm.core.xml.reader.abstract_xml_data_reader import AbstractXMLDataReader


class CdiscDataXsdReader(AbstractXMLDataReader):
    """
    根据 XSD 的方式，读取XML数据， 实例化 ODM 对象
    """
    def _new_cdisc_node(self, cdisc_name):
        new_obj = self.registry.get(cdisc_name)()
        return new_obj
