

from pyodmv2.xml_defintion.odm.enums.odm_v2_enum import OdmV2Enum
from pyodmv2.xml_defintion.odm.tags.Element import Element


class StudyEventData(Element):
    def support_attribute(self) -> list[OdmV2Enum]:
        return [OdmV2Enum.StudyEventOID, OdmV2Enum.StudyEventRepeatKey, OdmV2Enum.TransactionType]

    def support_children(self) -> list[OdmV2Enum]:
        return [OdmV2Enum.ItemGroupData, OdmV2Enum.AuditRecord, OdmV2Enum.Signature, OdmV2Enum.Annotation, OdmV2Enum.Query]

    def element_name(self) -> OdmV2Enum:
        return OdmV2Enum.StudyEventData
