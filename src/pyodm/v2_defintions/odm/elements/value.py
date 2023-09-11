from edc.common.xml_defintion.odm.tags.Element import Element
from edc.common.xml_defintion.odm_v2 import OdmV2


class Value(Element):
    def support_attribute(self) -> list[OdmV2]:
        return [OdmV2.SeqNum]

    def support_children(self) -> list[OdmV2]:
        return []

    def element_name(self) -> OdmV2:
        return OdmV2.Value
