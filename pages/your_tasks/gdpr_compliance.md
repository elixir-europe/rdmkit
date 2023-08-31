---
title: GDPR compliance
contributors: [Pinar Alper, Yvonne Kallberg, Vilem Ded, Eva Csosz, Niclas Jareborg]
description: How to protect your research data, and how to make research data compliant to GDPR.
page_id: gdpr_compliance
related_pages: 
  tool_assembly: [tsd, transmed]
  your_tasks: [data_security]
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=data+protection#materials
dsw:
- name: Will you collect any data connected to a person, "personal data"?
  uuid: 49c009cb-a38c-4836-9780-8a8b3dd1cbac
- name: Do you need a Data Protection Impact Assessment?
  uuid: 8915bd25-db22-4ed6-bcc8-b1bbdc52989e
faircookbook:
- name: Licensing Data
  url: https://w3id.org/faircookbook/FCB034
- name: Declaring data permitted uses
  url: https://w3id.org/faircookbook/FCB035
- name: Data Protection Impact Assessment and Data Privacy
  url: https://w3id.org/faircookbook/FCB074
---

## How do you protect research data under GDPR?

### Description

Where scientific research involves the processing of data concerning identifiable people in the European Union (EU), it is subject to the General Data Protection Regulation (GDPR). The GDPR applies a ["special regime"](https://edps.europa.eu/sites/edp/files/publication/20-01-06_opinion_research_en.pdf) to research, providing derogations from some obligations given appropriate criteria are met and safeguards are in place. The criteria are to follow standards in research method and ethics, as well as to aim for societal benefit rather than serving private interests in research.

The safeguards are a multitude and include:
  * data collection with informed consent under ethical oversight and accountability;
  * ensuring lawful processing and exchange of human-subject information;
  * putting in place organisational and technical data protection measures such as encryption and pseudonymisation.

The practical impact of the GDPR on research is, then, establishing these safeguards within projects.

### Considerations

Seek expert help for the interpretation of GDPR legal requirements to practicable measures.
  * Research institutes appoint Data Protection Officers (DPO). Before starting a project you should contact your DPO to be informed of GDPR compliance requirements for your institution.
  * Each EU country has its own national implementation of the GDPR. If your project involves a multi-national consortium, the requirements of all participating countries need to be met and you should inform the project coordinator of any country-specific requirements.
  * Legal offices in research institutes provide model agreements, which cater for various research scenarios and consortia setups. You should inform your local legal office of your project's setup and identify the necessary agreements to be signed.

Assess your project under the GDPR.
  * Determine your GDPR role. Are you a data controller, who determines the purposes and means of the processing, or, are you a data processor, who acts under instructions from the controller?
  * If you are a controller, you need to check whether your processing poses high privacy risks for data subjects, and if so, perform a  Data Protection Impact Assessment (DPIA).
     * The GDPR lists certain data e.g. race, ethnicity, health, genetic, biometric data as [special category](https://ec.europa.eu/info/law/law-topic/data-protection/reform/rights-citizens/how-my-personal-data-protected/how-data-my-religious-beliefs-sexual-orientation-health-political-views-protected_en), requiring heightened protection. Your research will be considered high-risk processing if it involves special category data or if it includes some specified types of processing.
     * A DPIA is often a prerequisite for ethics applications. Your DPO or local ethics advisory board can help determine whether your project requires a DPIA.  
     * Performing the DPIA while writing the DMP will allow you to reuse information and save time.
     * An outcome of the DPIA will be a listing of risks and corresponding mitigations. Mitigations identify the data protection measures you will adopt, both technical and organisational.

Apply technical and organisational measures for data protection. These include:
  * institutional policies and codes of conduct;
  * staff training;
  * user authentication, authorisation, data level access control;
  * data privacy measures such as pseudonymisation, anonymisation and encryption;
  * arrangements that will enable data subjects to exercise their rights.

Record your data processing. To meet GDPR's accountability requirement you should maintain records on the following:
  * project stakeholders and their GDPR roles (controller, processor);
  * purpose of your data processing;
  * description of data subjects and the data;
  * description of data recipients, particularly those outside the EU;
  * logs of data transfers to recipients and the safeguards put in place for transfers, such as data sharing agreements;
  * time limits for keeping different categories of personal data;
  * description of organisational and technical data protection measures.

### Solution

  * [European Data Protection Supervisor's "Preliminary opinion on Data Protection and Scientific Research"](https://edps.europa.eu/sites/edp/files/publication/20-01-06_opinion_research_en.pdf)
  * {% tool "bbmri-eric-s-elsi-knowledge-base" %} contains a glossary, agreement templates and guidance.
  * {% tool "daisy" %} and {% tool "erpa" %} are software tools from ELIXIR that allow the record-keeping of data processing activities in research projects.
  * {% tool "dawid" %} is a software tool from ELIXIR that allows the generation of tailor-made data-sharing agreements
  * {% tool "dpia-knowledge-model" %} is designed to leverage {% tool "data-stewardship-wizard" %} to perform DPIA.
  * {% tool "tryggve-elsi-checklist" %} is a list of Ethical, Legal, and Societal Implications (ELSI) to consider for research projects on human subjects.
