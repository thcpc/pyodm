from eclinical import Environment

from edc.common.edc_subject_crf.bo.study_hierarchies import StudyHierarchies
from edc.common.xml_defintion.odm.elements.builder import Builder
from edc.common.xml_defintion.odm.elements.clinical_data import ClinicalData
from edc.common.xml_defintion.odm.elements.item_data import ItemData
from edc.common.xml_defintion.odm.elements.item_group_data import ItemGroupData
from edc.common.xml_defintion.odm.elements.study_event_data import StudyEventData
from edc.common.xml_defintion.odm.elements.subject_data import SubjectData
from edc.common.xml_defintion.odm.elements.value import Value
from edc.common.xml_defintion.odm.tags.Attribute import Attribute
from lxml import etree

from edc.common.xml_defintion.odm_v2 import OdmV2


def test_odm():
    clinical_data = ClinicalData()

    for subject_name in ["D001001", "D002002", "D003003"]:
        subject = SubjectData()
        subject.add_attribute(Attribute(OdmV2.SubjectKey, value=subject_name))
        for visit in ["Screening", "Main Period (M1)"]:
            study_event = StudyEventData()
            study_event.add_attribute(Attribute(OdmV2.StudyEventOID, value=visit))
            subject.add_child(study_event)
        clinical_data.add_child(subject)
    tree = etree.ElementTree(element=clinical_data.xml())
    tree.write("output.xml", pretty_print=True, encoding="utf-8")


def test_odm_builder():
    study_event_data = []
    for visit in ["Screening", "Main Period (M1)"]:
        study_event = StudyEventData()
        study_event.add_attribute(Attribute(OdmV2.StudyEventOID, value=visit))
        study_event_data.append(Builder()
                                .attributes([Attribute(OdmV2.StudyEventOID, value=visit)])
                                .build(StudyEventData))

    subject_data = []
    for subject_name in ["D001001", "D002002", "D003003"]:
        subject_data.append(Builder()
                            .attributes([Attribute(OdmV2.SubjectKey, value=subject_name)])
                            .children(study_event_data).build(SubjectData))

    clinical_data = Builder().children(subject_data).build(ClinicalData)
    tree = etree.ElementTree(element=clinical_data.xml())
    tree.write("output.xml", pretty_print=True, encoding="utf-8")


def test_odm_from_database():
    hierarchies = StudyHierarchies.create(Environment.loader("EDC_PERFORMANCE_ONC"), subjects=['204-001', '101-023'])
    clinical_data = ClinicalData()
    for subject in hierarchies.subjects():
        subject_data = SubjectData()
        subject_data.add_attribute(Attribute(OdmV2.SubjectKey, value=subject.get("subject_name")))
        for visit in subject.children():
            study_event_data = StudyEventData()
            study_event_data.add_attribute(Attribute(OdmV2.StudyEventOID, value=visit.get("visit_name")))
            for form in visit.children():
                for item_group in form.children():
                    item_group_data = ItemGroupData()
                    item_group_data.add_attribute(Attribute(OdmV2.ItemGroupOID, value=form.get("form_name")))
                    item_group_data.add_attribute(Attribute(OdmV2.ItemGroupDataSeq, value=str(item_group.get("sn"))))
                    for item in item_group.children():
                        item_data = ItemData()
                        item_data.add_attribute(Attribute(OdmV2.ItemOID,
                                                          value=f"{item.get('question')}.{item.get('variable_name')}"))

                        value = Value()
                        value.text = item.get("before_val")
                        value.add_attribute(Attribute(OdmV2.SeqNum, value="0"))
                        item_data.add_child(value)
                        item_group_data.add_child(item_data)
                        value = Value()
                        value.text = item.get("current_val")
                        value.add_attribute(Attribute(OdmV2.SeqNum, value="1"))
                        item_data.add_child(value)
                        item_group_data.add_child(item_data)
                    study_event_data.add_child(item_group_data)
            subject_data.add_child(study_event_data)
        clinical_data.add_child(subject_data)
    tree = etree.ElementTree(element=clinical_data.xml())
    tree.write("output.xml", pretty_print=True, encoding="utf-8")
