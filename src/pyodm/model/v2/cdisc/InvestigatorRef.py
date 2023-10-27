import pyodm.model.definition as Model
import pyodm.model.meta.cdisc_odm_entity as Meta


class InvestigatorRef(Meta.CdiscODMEntity):
    """
    https://wiki.cdisc.org/display/ODM2/InvestigatorRef+Element
    """
    
    UserOID = Model.Attribute()
    
    
