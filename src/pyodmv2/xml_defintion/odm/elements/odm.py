from edc.common.xml_defintion.odm.tags.Element import Element
from edc.common.xml_defintion.odm_v2 import OdmV2


class ODM(Element):
    def support_attribute(self) -> list[OdmV2]:
        return [OdmV2.FileType, OdmV2.Granularity, OdmV2.Context, OdmV2.FileOID, OdmV2.CreationDateTime,
                OdmV2.PriorFileOID, OdmV2.AsOfDateTime, OdmV2.ODMVersion, OdmV2.Originator,
                OdmV2.SourceSystem, OdmV2.SourceSystemVersion]

    def support_children(self) -> list[OdmV2]:
        return [OdmV2.Description, OdmV2.Study, OdmV2.AdminData,
                OdmV2.ReferenceData, OdmV2.ClinicalData, OdmV2.Association]

    def element_name(self) -> OdmV2:
        return OdmV2.ODM
