from pyodm.model.definition import Attribute


class TelecomType(Attribute):
    def __init__(self):
        super().__init__()
        self.set_name("TelecomType")