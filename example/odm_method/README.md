## ODM 定义
```python
class ODM(Meta.CdiscODMEntity):
    """
    https://wiki.cdisc.org/display/ODM2/ODM
    """
    FileType = Model.Attribute()
    Granularity = Model.Attribute()
    Context = Model.Attribute()
    FileOID = Model.Attribute()
    CreationDateTime = Model.Attribute()
    PriorFileOID = Model.Attribute()
    AsOfDateTime = Model.Attribute()
    ODMVersion = Model.Attribute()
    Originator = Model.Attribute()
    SourceSystem = Model.Attribute()
    SourceSystemVersion = Model.Attribute()
    Description = Model.ManyElements()
    Study = Model.ManyElements()
    AdminData = Model.ManyElements()
    ReferenceData = Model.ManyElements()
    ClinicalData = Model.ManyElements()
    Association = Model.ManyElements()
```
## SubjectData定义
```python
class SubjectData(Meta.CdiscODMEntity):
    """
    https://wiki.cdisc.org/display/ODM2/SubjectData+Element
    """
    SubjectKey = Model.Attribute()
    TransactionType = Model.Attribute()
    InvestigatorRef = Model.OneElement()
    SiteRef = Model.OneElement()
    StudyEventData = Model.ManyElements()
    Query = Model.ManyElements()
    AuditRecord = Model.OneElement()
    Signature = Model.OneElement()
    Annotation = Model.ManyElements()
```
## ItemGroupData 定义
```python
class ItemGroupData(Meta.CdiscODMEntity):
    """
    https://wiki.cdisc.org/display/ODM2/ItemGroupData+Element
    """
    ItemGroupOID = Model.Attribute()
    ItemGroupRepeatKey = Model.Attribute()
    TransactionType = Model.Attribute()
    ItemGroupDataSeq = Model.Attribute()
    Query = Model.ManyElements()
    ItemGroupData = Model.ManyElements()
    ItemData = Model.ManyElements()
    AuditRecord = Model.OneElement()
    Signature = Model.OneElement()
    Annotation = Model.ManyElements()
```
## ItemData 定义
```python
class ItemData(Meta.CdiscODMEntity):
    """
    https://wiki.cdisc.org/display/ODM2/ItemData+Element
    """
    
    ItemOID = Model.Attribute()
    TransactionType = Model.Attribute()
    IsNull = Model.Attribute()
    Value = Model.ManyElements()
    Query = Model.ManyElements()
    AuditRecord = Model.ManyElements()
```