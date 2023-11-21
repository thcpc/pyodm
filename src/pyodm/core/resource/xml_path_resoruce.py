from pyodm.core.support.abstract_path_resource import AbstractPathResource

from lxml import etree


class XmlPathResource(AbstractPathResource):
    def load(self):
        return etree.parse(self.file)
