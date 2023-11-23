SELECT es.name as SubjectKey,
       ess.code as LocationOID, esv.visit_name as StudyEventOID,
       esf.form_name as ItemGroupOID, e.sn as ItemGroupRepeatKey,
       esi.variable_name as ItemOID,
       esr.id as SeqNum, esr.current_val as Text
FROM eclinical_subject es
         join eclinical_study_site ess on es.study_site_id = ess.id
         join eclinical_subject_crfversion esc on es.id = esc.subject_id and esc.is_lastest = true
         join eclinical_subject_visit esv on esc.id = esv.subject_version_id
         join eclinical_subject_visit_status esvs on esv.id = esvs.subject_visit_id and esvs.complete = true
         join eclinical_subject_form esf on esv.id = esf.subject_visit_id and esv.subject_version_id = esc.id
         join eclinical_subject_ig e on esc.id = e.subject_version_id and e.subject_form_id = esf.id
         join eclinical_subject_item esi on esc.id = esi.subject_version_id and esi.subject_ig_id = e.id
         join eclinical_subject_record_history esr on esi.id = esr.subject_item_id and esc.id = esi.subject_version_id;