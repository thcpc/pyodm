from pyodm.model.definition.cdisc_model import CdiscModel


class Attribute(CdiscModel):
    def __init__(self):
        super().__init__()
        self._value = ""

    @property
    def name(self): return self._name

    @name.setter
    def name(self, name): self._name = name

    @property
    def value(self): return self._value

    @value.setter
    def value(self, value): self._value = value