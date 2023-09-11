from dataclasses import dataclass

from edc.common.xml_defintion.odm_v2 import OdmV2


@dataclass
class Attribute:
    name: OdmV2
    value: str
