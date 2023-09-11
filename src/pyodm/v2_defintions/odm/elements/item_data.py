# from edc.common.v2_defintions.odm.tags.Element import Element
# from edc.common.v2_defintions.odm_v2 import OdmV2
from pyodmv2.xml_defintion.odm.enums.odm_v2_enum import OdmV2Enum
from pyodmv2.xml_defintion.odm.tags.Element import Element


class ItemData(Element):
    
    def support_attribute(self) -> list[OdmV2Enum]:
        return [OdmV2Enum.ItemOID, OdmV2Enum.TransactionType, OdmV2Enum.IsNull]

    def support_children(self) -> list[OdmV2Enum]:
        return [OdmV2Enum.Value, OdmV2Enum.AuditRecord, OdmV2Enum.Signature, OdmV2Enum.Annotation, OdmV2Enum.Query]

    def element_name(self) -> OdmV2Enum:
        return OdmV2Enum.ItemData
