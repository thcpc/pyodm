import pyodm.model.definition as Model
import pyodm.model.meta.cdisc_odm_entity as Meta


class SubjectItem(Meta.CdiscODMEntity):
    Id = Model.Attribute()
    Name = Model.Attribute()
