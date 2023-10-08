import pytest
import xmlschema

from pyodm.odm_validator import ODMValidator

def test_xml_xsd_valid():
    # ODMValidator.odm("resources/un_odm_xml.xml")
    # ODMValidator.xml("resources/odm_template.xml")
    assert ODMValidator.odm("resources/odm_template.xml") == True


def test_xml_xsd_unvalid():
    with pytest.raises(xmlschema.XMLSchemaException):
        ODMValidator.odm("resources/un_odm_xml.xml")
