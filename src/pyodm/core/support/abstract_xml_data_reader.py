import abc
from pyodm.core.support.abstract_data_loader import AbstractDataLoader
from pyodm.core.support.abstract_data_reader import AbstractDataReader
from pyodm.factory.cdisc_registry import CdiscRegistry
from pyodm.utils.etree_utils import EtreeUtils


class AbstractXMLDataReader(AbstractDataReader):
    """
    读取 XML 文件的实现
    """

    def __init__(self, registry: CdiscRegistry):
        super().__init__(registry)

    def _new_cdisc_node(self, cdisc_name):
        new_obj = self.registry.get(cdisc_name)()
        return new_obj

    def _set_attribute(self, element, cdisc_node):
        for key, val in element.attrib.items():
            attr = getattr(cdisc_node, key)
            attr.set_name(key)
            attr.set_value(val)

    def _sub_cdisc_node(self, cdisc_node, sub_cdisc_name):
        return getattr(cdisc_node, sub_cdisc_name)

    def _set_text(self, element, cdisc_node):
        if element.text and not element.text.isspace() and element.text.strip():
            cdisc_node.set_value(element.text)

    @abc.abstractmethod
    def _parse(self, element, cdisc_name):
        ...

    def read(self, loader: AbstractDataLoader):
        tree = loader.load()
        return self._parse(tree.getroot(), EtreeUtils.localname(tree.getroot()))
