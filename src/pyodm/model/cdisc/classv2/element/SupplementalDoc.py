
import pyodm.model.meta.cdisc_odm_entity as Meta


from pyodm.model.cdisc.classv2.element.DocumentRef import DocumentRef


from pyodm.model.definition import ManyElements



class SupplementalDoc(ManyElements,Meta.CdiscODMEntity):
    """
    https://wiki.cdisc.org/display/ODM2/SupplementalDoc
    """

    def __init__(self):
        super().__init__()
        self.set_name("SupplementalDoc")
        
        self._DocumentRef = None
        

    
    @property
    def DocumentRef(self):
        """
        ManyElements
        """
        if self._DocumentRef is None:
            self._DocumentRef = DocumentRef()
        return self._DocumentRef
    