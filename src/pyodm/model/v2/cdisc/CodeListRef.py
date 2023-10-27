import pyodm.model.definition as Model
import pyodm.model.meta.cdisc_odm_entity as Meta


class CodeListRef(Meta.CdiscODMEntity):
    """
    https://wiki.cdisc.org/display/ODM2/CodeListRef
    """
    
    CodeListOID = Model.Attribute()
    
    
