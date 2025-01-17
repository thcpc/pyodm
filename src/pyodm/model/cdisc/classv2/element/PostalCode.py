
import pyodm.model.meta.cdisc_odm_entity as Meta



from pyodm.model.definition import OneElement



class PostalCode(OneElement,Meta.CdiscODMEntity):
    """
    https://wiki.cdisc.org/display/ODM2/PostalCode
    """

    def __init__(self):
        super().__init__()
        self.set_name("PostalCode")
        

    