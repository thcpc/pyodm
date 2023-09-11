from edc.common.xml_defintion.odm.tags.Element import Element
from edc.common.xml_defintion.odm_v2 import OdmV2


class ItemGroupData(Element):
    def support_attribute(self) -> list[OdmV2]:
        return [OdmV2.ItemGroupOID, OdmV2.ItemGroupRepeatKey, OdmV2.TransactionType, OdmV2.ItemGroupDataSeq]

    def support_children(self) -> list[OdmV2]:
        return [OdmV2.ItemGroupData, OdmV2.ItemData, OdmV2.AuditRecord, OdmV2.Signature, OdmV2.Annotation, OdmV2.Query]

    def element_name(self) -> OdmV2:
        return OdmV2.ItemGroupData
