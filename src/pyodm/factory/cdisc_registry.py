from pyodm.exceptions import CdiscFactoryException


class CdiscRegistry:
    """
    注册 ODM 元素的 Class 类型
    """
    def __init__(self):
        self._registry_classes = dict()

    def get(self, name: str):
        if self._registry_classes.get(name) is None:
            raise CdiscFactoryException(f"{name} No Registry Class")
        return self._registry_classes.get(name)

    def registry_cdisc(self, name, cdisc_class):
        self._registry_classes[name] = cdisc_class
