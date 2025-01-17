
import pyodm.model.meta.cdisc_odm_entity as Meta





class Code(Meta.CdiscODMEntity):
    """
    https://wiki.cdisc.org/display/ODM2/Code
    """

    def __init__(self):
        super().__init__()
        self.set_name("Code")
        

    