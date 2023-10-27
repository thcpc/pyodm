from pyodm.core.xml.reader.abstract_xml_data_reader import AbstractXMLDataReader


class CdiscDataXsdReader(AbstractXMLDataReader):
    def _new_cdisc_node(self, cdisc_name):
        new_obj = self.registry.get(cdisc_name)()
        return new_obj
