from edc.common.xml_defintion.odm.tags.Element import Element
from edc.common.xml_defintion.odm_v2 import OdmV2


class SubjectData(Element):

    def support_attribute(self) -> list[OdmV2]:
        return [OdmV2.SubjectKey, OdmV2.TransactionType]

    def support_children(self) -> list[OdmV2]:
        return [OdmV2.InvestigatorRef, OdmV2.SiteRef, OdmV2.StudyEventData, OdmV2.AuditRecord,
                OdmV2.Signature, OdmV2.Annotation, OdmV2.Query]

    def element_name(self) -> OdmV2:
        return OdmV2.SubjectData
