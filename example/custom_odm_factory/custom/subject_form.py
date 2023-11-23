import pyodm.model.definition as Model
import pyodm.model.meta.cdisc_odm_entity as Meta


class SubjectForm(Meta.CdiscODMEntity):
    Name = Model.Attribute()
    SubjectItem = Model.ManyElements()
