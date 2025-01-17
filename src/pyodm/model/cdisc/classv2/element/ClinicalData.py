
import pyodm.model.meta.cdisc_odm_entity as Meta

from pyodm.model.cdisc.classv2.attribute.StudyOID import StudyOID

from pyodm.model.cdisc.classv2.attribute.MetaDataVersionOID import MetaDataVersionOID


from pyodm.model.cdisc.classv2.element.SubjectData import SubjectData

from pyodm.model.cdisc.classv2.element.ItemGroupData import ItemGroupData

from pyodm.model.cdisc.classv2.element.Query import Query

from pyodm.model.cdisc.classv2.element.AuditRecord import AuditRecord

from pyodm.model.cdisc.classv2.element.Signature import Signature

from pyodm.model.cdisc.classv2.element.Annotation import Annotation


from pyodm.model.definition import ManyElements



class ClinicalData(ManyElements,Meta.CdiscODMEntity):
    """
    https://wiki.cdisc.org/display/ODM2/ClinicalData
    """

    def __init__(self):
        super().__init__()
        self.set_name("ClinicalData")
        
        self._SubjectData = None
        
        self._ItemGroupData = None
        
        self._Query = None
        
        self._AuditRecord = None
        
        self._Signature = None
        
        self._Annotation = None
        
        self._StudyOID = None
        
        self._MetaDataVersionOID = None
        

    
    @property
    def SubjectData(self):
        """
        ManyElements
        """
        if self._SubjectData is None:
            self._SubjectData = SubjectData()
        return self._SubjectData
    
    @property
    def ItemGroupData(self):
        """
        ManyElements
        """
        if self._ItemGroupData is None:
            self._ItemGroupData = ItemGroupData()
        return self._ItemGroupData
    
    @property
    def Query(self):
        """
        ManyElements
        """
        if self._Query is None:
            self._Query = Query()
        return self._Query
    
    @property
    def AuditRecord(self):
        """
        ManyElements
        """
        if self._AuditRecord is None:
            self._AuditRecord = AuditRecord()
        return self._AuditRecord
    
    @property
    def Signature(self):
        """
        OneElement
        """
        if self._Signature is None:
            self._Signature = Signature()
        return self._Signature
    
    @property
    def Annotation(self):
        """
        ManyElements
        """
        if self._Annotation is None:
            self._Annotation = Annotation()
        return self._Annotation
    
    @property
    def StudyOID(self):
        """
        Attribute
        """
        if self._StudyOID is None:
            self._StudyOID = StudyOID()
        return self._StudyOID
    
    @property
    def MetaDataVersionOID(self):
        """
        Attribute
        """
        if self._MetaDataVersionOID is None:
            self._MetaDataVersionOID = MetaDataVersionOID()
        return self._MetaDataVersionOID
    