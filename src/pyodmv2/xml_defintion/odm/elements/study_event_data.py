from edc.common.xml_defintion.odm.tags.Element import Element
from edc.common.xml_defintion.odm_v2 import OdmV2


class StudyEventData(Element):
    def support_attribute(self) -> list[OdmV2]:
        return [OdmV2.StudyEventOID, OdmV2.StudyEventRepeatKey, OdmV2.TransactionType]

    def support_children(self) -> list[OdmV2]:
        return [OdmV2.ItemGroupData, OdmV2.AuditRecord, OdmV2.Signature, OdmV2.Annotation, OdmV2.Query]

    def element_name(self) -> OdmV2:
        return OdmV2.StudyEventData
