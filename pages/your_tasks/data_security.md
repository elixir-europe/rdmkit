---
title: Data security
contributors: [Pinar Alper, Yvonne Kallberg, Vilem Ded, Eva Csosz, Niclas Jareborg]
description: How do you ensure that your data is handled securely.
page_id: data_security
redirect_from: data_protection
related_pages: 
  tool_assembly: [tsd, transmed]
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=data+protection#materials
dsw:
- name: Will you collect any data connected to a person, "personal data"?
  uuid: 49c009cb-a38c-4836-9780-8a8b3dd1cbac
- name: Do you need a Data Protection Impact Assessment?
  uuid: 8915bd25-db22-4ed6-bcc8-b1bbdc52989e
- name: What technical and procedural safeguards have been established for processing
    the data?
  uuid: a30f5047-33c1-45a7-8b3f-b1b90c364fc9
faircookbook:
- name: Downloading data with Aspera
  url: https://w3id.org/faircookbook/FCB015
- name: Transferring data with SFTP
  url: https://w3id.org/faircookbook/FCB014
- name: How to create checksum files
  url: https://w3id.org/faircookbook/FCB052
- name: How to check file integrity by validating checksums
  url: https://w3id.org/faircookbook/FCB053
---

## How do you ensure that your data is handled securely?

### Description

To protect your research data, code, and other information assets you should establish adequate Information security measures. Information security relies on combinations of technical and procedural measures that work together to ensure protection of the data at a suitable level. To note is that failure by humans to follow the procedural measures often poses a higher vulnerability to security risks than shortcomings of the technical measures. 

### Considerations

* Information security is usually described as containing three main aspects - **Confidentiality**, **Integrity**, and **Availability**.
  * Confidentiality is about measures to ensure that data is kept confidential from those that do not have rights to access the data.
  * Integrity is about measures to ensure that data is not corrupted or destroyed during storage or transmission.
  * Availability is about measures that ensure access to the data is possible at the time of need or access does not require an inordinate amount of time.
* What information security measures that need to be established should be defined at the planning stage (e.g. when doing a risk assessment for a GDPR Data Protection Impact Assessment). This should identify information security risks, and define measures to mitigate those risks. 
* Balance the cost and effort for protecting your data at an appropriate level. For this, it is useful to classify the impact of failure for the three different CIA aspects to guide your choices. You should not spend more resources than necessary if the impact of failure is low enough that you can easily cope with it. Nor should you spend too few resources on protective measures for aspects where the impact is high. For example, the Availability aspect will probably differ a lot if your data is used in a clinical versus a research setting, where protecting against a system failure in the research setting can be a lot less resource demanding than in the clinical setting.
* Ensure that everyone that works with the data knows what is expected of them, how the Information Security measures are to be implemented, and who is responsible for ensuring that they are followed and performed as agreed.
* Be sure to contact the IT or Information security office at your institution to get guidance and support to address these issues. They should be able to provide you with suitable solutions for your needs.

### Solution

* Below is a non-exhaustive list of good practices that might be relevant depending on the level of protection required. Note that some of these might be quite costly, such as investing in hardware or hiring highly specialized staff to ensure high levels of security. More on costs for RDM is available on the [Costs of data management](/costs_data_management) page.
* Confidentiality
  * Use password protection on all computers
  * Use two-factor authentication, i.e. using two ways of identification in order to obtain access to the (remote) data
  * Set file and folder permissions, e.g. use read-only access for data that should never be changed, and limit access to only those who needs it
  * Apply a “Lock screen policy” to prevent unauthorised access of systems from those who do not have access rights and permissions.
  * Use encrypted data transfers to avoid eavesdropping
  * Consider implementing systems monitoring measures in order to ensure that hacking attempts are detected
  * Decide on procedures on how systems can be physically accessed. Should data be allowed to reside on personal laptops, or only on designated stationery systems? Should stationary systems be physically protected in locked compartments only accessible to a limited number of individuals?
* Integrity
  * Generate checksums for all files as soon as possible, preferably upon file creation.
  * Keep the number of copies to a minimum to facilitate its management.
  * Adopt a data release workflow which ensures the data are versioned and preserved. Each version shall be protected against any change by users, e.g. by setting permissions to read-only.    
  * Perform quality checks both upon data collection to ensure accuracy and on a regular basis to discover potential integrity errors.
  * Define, document and adopt a back-up strategy for your data.
  * Utilise available tools for data management (data warehouses) ensuring data integrity by default.
* Availability
  * Set up disaster recovery procedures with instructions on *what* data, *how*, and by *who*, recovery of data should be done in case an incident of system failure or data loss happens.
  * If high availability is a must, consider designing a redundant computing and storage strategy where there are physically separated compute and storage resources, that ensures that the data is available at all times even in the event of system failure.
* Organisational Measures
  * The procedures on how the technical protection measures are to be used, and who is responsible for what, must be understood by all personnel that work with the data, code, and other information assets. The procedures should be documented, and staff should have access to relevant training to follow the procedures. This is often the most vulnerable part in an Information Security strategy.
  * Policies are an important component of data management and they are essential for information security. Organisations use policies to announce to their staff and third parties the expectations, roles and responsibilities in data handling. Policies typically cover data classification, storage/backup, transfer, retention/archival, deletion/destruction, acceptable use of IT platforms and the reporting of security incidents and data breaches. In some cases research data requirements would be addressed in dedicated policies. Therefore, at the planning phase, it is important to understand institutional data policies applicable to the project’s data. If the data is considered sensitive as per the institutional data classification, this will have an impact on the IT platforms that can be used to store and transmit the data as well as the specific procedures to be followed.
  * Information inventories and documentation is another requirement for projects dealing with sensitive data. At the planning phase you should identify the various categories of data that will be processed in the project e.g. personal health and biomedical data, sensitive habitat data, IP restricted data from the industry. You should document which platforms will be used to process the data and the applicable security measures in case certain measures are applied to restricted classes of data. See the next section for GDPR-specific documentation requirements. See the [Data Sensitivity](/data_sensitivity) page for more information on sensitive data.
  * [ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001) is an international information security standard adopted by data processing centres worldwide. Some universities and research institutes also acquire an ISO 27001 certification for their IT environments. Such certifications allow institutions to consistently and thoroughly identify information security risks and put in place best practice information security controls. These controls would include all above mentioned technical and organisational safeguards and more.


## How do you protect research data under GDPR?

### Description

Where scientific research involves the processing of data concerning people in the European Union (EU), it is subject to the {% tool "eu-general-data-protection-regulation" %} (GDPR). The GDPR applies a ["special regime"](https://edps.europa.eu/sites/edp/files/publication/20-01-06_opinion_research_en.pdf) to research, providing
derogations from some obligations given appropriate criteria are met and safeguards are in place. The criteria is to follow standards in research method and ethics, as well as to aim societal benefit rather than serving private interests in research.
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
     * The GDPR lists certain data e.g. race, ethnicity, health, genetic, biometric data as [special category](https://ec.europa.eu/info/law/law-topic/data-protection/reform/rights-citizens/how-my-personal-data-protected/how-data-my-religious-beliefs-sexual-orientation-health-political-views-protected_en), requiring it's heightened protection. Your research will be considered high risk processing if it involves special category data or if it includes some specified types of processing.
     * A DPIA is often a pre-requisite for ethics applications. Your DPO or local ethics advisory board can help determine whether your project requires a DPIA.  
     * Performing the DPIA while writing the DMP will allow you to reuse information and save time.
     * An outcome of the DPIA will be a listing of risks and corresponding mitigations. Mitigations identify the data protection measures you'll adopt, both technical organisational.       

Apply technical and organisational measures for data protection. These include:
  * institutional policies and codes of conduct;
  * staff training;
  * user authentication, authorisation, data level access control;
  * data privacy measures such as pseudonymisation, anonymisation and encryption,
  * arrangements that will enable data subjects to exercise their rights.

Record your data processing. To meet  GDPR's accountability requirement you should maintain records on the following:
  * project stakeholders and their GDPR roles (controller, processor);
  * purpose of your data processing;
  * description of data subjects and the data;
  * description of data recipients, particularly those outside the EU;
  * logs of data transfers to recipients and the safeguards put in place for transfers, such as data sharing agreements;
  * time limits for keeping different categories of personal data;
  * description of organizational and technical data protection measures.

### Solution

  * [European Data Protection Supervisor's "Preliminary opinion on Data Protection and Scientific Research"](https://edps.europa.eu/sites/edp/files/publication/20-01-06_opinion_research_en.pdf)
  * {% tool "bbmri-eric-s-elsi-knowledge-base" %} contains a glossary, agreement templates and guidance.
  * {% tool "daisy" %} and {% tool "erpa" %} are software tools from ELIXIR that allows the record keeping of data processing activities in research projects.
  * {% tool "dawid" %} is a software tool from ELIXIR that allows generation of tailor-made data sharing agreements
  * {% tool "dpia-knowledge-model" %} is designed to leverage {% tool "data-stewardship-wizard" %} to perform DPIA.
  * {% tool "tryggve-elsi-checklist" %} is a list of Ethical, Legal, and Societal Implications (ELSI) to consider for research projects on human subjects.

