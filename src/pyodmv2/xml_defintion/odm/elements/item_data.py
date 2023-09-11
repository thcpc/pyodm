from edc.common.xml_defintion.odm.tags.Element import Element
from edc.common.xml_defintion.odm_v2 import OdmV2


class ItemData(Element):
    
    def support_attribute(self) -> list[OdmV2]:
        return [OdmV2.ItemOID, OdmV2.TransactionType, OdmV2.IsNull]

    def support_children(self) -> list[OdmV2]:
        return [OdmV2.Value, OdmV2.AuditRecord, OdmV2.Signature, OdmV2.Annotation, OdmV2.Query]

    def element_name(self) -> OdmV2:
        return OdmV2.ItemData
