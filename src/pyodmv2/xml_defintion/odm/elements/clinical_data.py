from abc import ABC
from typing import List

from edc.common.xml_defintion.odm.tags.Element import Element
from edc.common.xml_defintion.odm_v2 import OdmV2


class ClinicalData(Element):
    # def required_children(self) -> list[OdmV2]:
    #     return [OdmV2.SubjectData, OdmV2.ItemGroupData,]

    def support_attribute(self) -> list[OdmV2]:
        return [OdmV2.StudyOID, OdmV2.MetaDataVersionOID]

    def support_children(self) -> list[OdmV2]:
        return [OdmV2.SubjectData, OdmV2.ItemGroupData, OdmV2.AuditRecord, OdmV2.Signature, OdmV2.Annotation, OdmV2.Query]

    def element_name(self) -> OdmV2:
        return OdmV2.ClinicalData
