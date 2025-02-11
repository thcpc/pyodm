import importlib

from pyodm.core.support.abstract_configuration_reader import AbstractConfigurationReader
from pyodm.exceptions import CdiscDefineRequiredException

import lxml.etree as Etree

from pyodm.factory.xpath.xpath_node import XpathNode
from pyodm.model.definition import OneElement, ManyElements


class CdiscConfigurationSpecificationReader(AbstractConfigurationReader):
    """
    读取 Specifincation 配置文件
    """

    def load_cdisc_definition(self, registry, spec_file: str):

        xml_tree = Etree.parse(spec_file)
        root = xml_tree.getroot()
        cdisc = self._find_cdisc(root)
        if cdisc is None: raise CdiscDefineRequiredException(f"{spec_file} 没有定义 CDISC 节点")
        for name, clazz_info in self._cdisc_loader(cdisc).items():
            module = importlib.import_module(clazz_info.get("modulePath"))
            clazz = getattr(module, clazz_info.get("clazz"))
            elements = []
            for attr_name, attr in vars(clazz).items():
                if isinstance(attr, OneElement) or isinstance(attr, ManyElements):
                    elements.append(XpathNode(attr_name))
            registry.definition_tree.add(XpathNode(name), elements)

            registry.registry_cdisc(name, clazz)

    def data_reader(self, spec_file: str):
        xml_tree = Etree.parse(spec_file)
        root = xml_tree.getroot()
        data_reader_class = root.attrib.get("dataReader")
        if data_reader_class is None:
            raise Exception(f"{spec_file} is not define dataReader on root")
        pkg, clazz_name = ".".join(data_reader_class.split(".")[0:-1]), data_reader_class.split(".")[-1]
        module = importlib.import_module(pkg)
        clazz = getattr(module, clazz_name)
        return clazz
    def _find_cdisc(self, element):
        if element.tag.lower() == "CDISC".lower():
            return element
        else:
            for sub_element in element:
                x = self._find_cdisc(sub_element)
                if x: return x

    def _cdisc_loader(self, cdisc):
        # result = {"root": cdisc.attrib.get("cdiscRoot")}
        result = {}
        for sub_element in cdisc:
            result[sub_element.tag] = {
                "clazz": sub_element.attrib.get("clazz"),
                "modulePath": sub_element.attrib.get("modulePath")
            }
        return result
