import importlib

from pyodm.core.xml.reader.abstract_xml_data_reader import AbstractXMLDataReader


class CdiscDataSpecificationReader(AbstractXMLDataReader):
    def _new_cdisc_node(self, cdisc_name):
        clazz_info = self.registry.get(cdisc_name)
        module = importlib.import_module(clazz_info.get("modulePath"))
        new_obj = getattr(module, clazz_info.get("clazz"))()
        return new_obj
