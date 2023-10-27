from pyodm.core.xml.writer.cdisc_xml_writer import CdiscXmlWriter


def assert_case1(cdisc):
    cw = CdiscXmlWriter(cdisc.odm)
    cw.write()


def assert_case2(cdisc):
    x = cdisc.odm.ClinicalData.first().SubjectData.first().StudyEventData.first().ItemGroupData.first().ItemData.first().Value
    assert x.first().value == '2200-10-01'
    query = cdisc.odm.ClinicalData.first().SubjectData.first().StudyEventData.first().ItemGroupData.first().ItemData.find(
        ItemOID="VISDT").Query.find(OID='A529A2F2-F896-4AF7-AD4D-11B7110727BC')
    assert query.Value.value == 'Value 2200-10-01 is in the future, please correct'
    assert query.AuditRecord.first().DateTimeStamp.value == '2021-03-10T13:36:51.668-00:00'
    cw = CdiscXmlWriter(cdisc.odm)
    cw.write()


def assert_case3(cdisc):
    x = cdisc.odm.ClinicalData
    assert x.first().StudyOID.value == '11'
    assert x.index(1).StudyOID.value == "EX001"
    cw = CdiscXmlWriter(cdisc.odm)
    cw.write()


def assert_case4(cdisc):
    subject = cdisc.odm.ClinicalData.first().SubjectData.first()
    assert subject.SubjectKey.value == '1001'
    query = subject.StudyEventData.find(StudyEventOID="Visit1").ItemGroupData.first().ItemData.first().Query.array
    assert query[0].Value.value == "Value is in the future, please correct"
    for i in query[0].AuditRecord.array:
        print(i.ReasonForChange.value)
    cw = CdiscXmlWriter(cdisc.odm)
    cw.write()


def assert_case5(cdisc):
    cdisc.odm.ClinicalData.usage(lambda x: print(x.first().StudyOID.value))


def assert_case6(cdisc):
    subject = cdisc.odm.ClinicalData.first().SubjectData.first()
    item_group_data = subject.StudyEventData.first().ItemGroupData.find(ItemGroupOID="IG.HEMATOLOGY")
    item_group_data1 = item_group_data.ItemGroupData.index(0)
    assert item_group_data1.ItemGroupOID.value == "IG.WBC"
    item_data = item_group_data1.ItemData.find(ItemOID="IT.WBC")
    assert item_data.Value.first().value == '5.2'
    item_data = item_group_data1.ItemData.index(1)
    assert item_data.Value.first().value == '10*3/uL'
    item_group_data2 = item_group_data.ItemGroupData.find(ItemGroupOID="IT.RBC")
    assert item_group_data2.ItemGroupOID.value == "IT.RBC"
    item_data = item_group_data2.ItemData.first()
    assert item_data.IsNull.value == "Yes"
    cw = CdiscXmlWriter(cdisc.odm)
    cw.write()
