from pyodm.model.meta.entity_meta import EntityMeta
import pyodm.model.definition as Model


class CdiscODMEntity(metaclass=EntityMeta):
    def __init__(self):
        self._name = ""
        self.value = None
        for name, instance in vars(self.__class__).items():
            if isinstance(instance, Model.Attribute) \
                    or isinstance(instance, Model.OneElement) \
                    or isinstance(instance, Model.ManyElements):
                setattr(self, name, instance.__class__())

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def is_blank(self) -> bool: return self.value is None
