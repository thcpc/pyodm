from lxml import etree


class EtreeUtils:
    @staticmethod
    def localname(element): return etree.QName(element.tag).localname
