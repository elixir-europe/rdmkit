---
title: Human health data
description: Data management solutions for human health data.
contributors: [Marcus Buchwald, Tim Beck, Saskia Lawson-Tovey, Gerhard Mayer, Soumyabrata Ghosh, Philip Quinlan, Venkata Satagopam, Jan Willem Boiten, Patrick Ruch, Hindrik Kerstens, Carlos Luís Parra Calderón, Salvador Capella-Gutierrez, Magda Chegkazi, Arshiya Merchant and the ELIXIR Health Data Focus Group]
page_id: health_data
related_pages: 
  your_tasks: [sensitive, gdpr_compliance]
  your_domain: [human data]
  
---
## Introduction

Human ‘health data’ is a broad concept encapsulating diverse data types and modalities, including omics and clinical data. Clinical data (routinely collected or originating from clinical studies) includes but is not limited to images, healthcare administrative data (e.g., demographics), free text and patient-generated data from questionnaires or real-world wearables/mobile devices. This page describes data management considerations and solutions for two widely collected data types used in health data research studies - data about the patient from questionnaires and electronic health records (EHRs) generated from interactions with the healthcare system. Future versions of this page will include additional health data types.

All scientific research involving data processing concerning identifiable people in the European Union is subject to the General Data Protection Regulation (GDPR) and may require ethics approval. This page will not repeat the GDPR, ethics and data anonymization information given elsewhere in RDMkit, namely on the [GDPR compliance](gdpr_compliance), [Ethical aspects](ethics), [Data sensitivity](data_sensitivity) and [Human data pages](human_data), which should be familiar to scientists working with health data. The content on this page is also distinct from the [Rare disease data page](rare-disease), which considers collecting and processing data specific to rare diseases. Country-specific RDM resources, including existing national solutions or RDM advice specific to national policies/funders/infrastructures are on the [National Resources pages](https://rdmkit.elixir-europe.org/website_overview#national-resources). The information presented on this page is disease and country-agnostic.


## Patient-generated health data from questionnaires 
 
### Description
Participants’ health data which can be collected via surveys, interviews, and monitoring, are called Clinical Outcome Measures (COMs). In surveys, the questionnaire is either completed by the participants or their representative (e.g., family member or caregiver). In interviews, a healthcare professional asks/explains the questionnaire to the participants and records their responses. Monitoring includes measuring a participant’s behaviour or activity in both a clinical and non-clinical setup. Based on this, COMs can be classified into four broad categories:
Patient Reported Outcome Measure (PROM) is a measurement that comes directly from the patient (i.e., study participant) about the status of a patient’s health condition without amendment or interpretation of the patient’s response by a clinician or anyone else.
Observer-Reported Outcome Measure (ObsROM) is a measurement based on a report of observable signs, events or behaviours related to a patient’s health condition by someone (e.g., family member or caregiver) other than the patient or a health professional.
Clinician-Reported Outcome Measure (ClinROM) is a measurement based on a report from a trained healthcare professional after observing a patient’s health condition.
Performance Outcome Measure (PefOM) is a measurement based on standardised task(s) actively undertaken by a patient according to a set of instructions and administered by trained professionals or completed by the patient independently.
 
Usually, COMs are inherently time-point specific, necessitating the inclusion of corresponding date-time information alongside the measured values. When COMs from a participant are gathered across multiple time points, the study is categorised as a longitudinal study. Within the clinical study/trial domain, these time points are referred to as Events, and a cohesive set of COM questions presented in a singular questionnaire is denoted as an Instrument or Battery.


### Considerations 
To collect health data directly from participants, an efficient data collection strategy will consider the following components:
* Consider the impact of the digital divide when digital collection methods are utilised. 
* Define key scientific objectives with patients and stakeholders from clinical, social-sciences and data analysis domains.
* In the case of a longitudinal study, define time points for the data collection (consult doctors on typical visit schedules to minimise the burden on participants and a calendar for holidays and other events).
* Any personally identifiable information (PII), including communication details like name, address, email, or telephone number, needs to be separated from data and stored in a separate system with additional security measures like Two-Factor Authentication and encryption at rest. 
* Design the privacy policy for the survey according to relevant local guidelines with the information governance/data protection officer and IT team
* Design the questionnaires with consideration given to interoperability (e.g., mapping questions/answers to concepts in clinical terminologies) and avoiding ambiguity in the questions.

  * Guidelines: 
     - [EC Guidelines for the development and criteria for the adoption of Health Survey instruments] (https://ec.europa.eu/health/ph_information/dissemination/reporting/healthsurveys_en.pdf)
     - [EC Selection of a Coherent Set of Health Indicators for the European Union Phase II](https://ec.europa.eu/health/ph_projects/2000/monitoring/fp_monitoring_2000_frep_03_en.pdf)
  * Check the readability and accessibility of the questionnaires.
  * Use validated, standardised questionnaires where possible, for example REDCap has a [library of data collection instruments](https://redcap.vanderbilt.edu/consortium/library/search.php)
  * Use a collaborative editing platform with versioning 
  * Finalise the questionnaires in the required template (if any) for ethical approval

* Development of the machine readable data dictionary for all languages   
   * Use a table format file such as CSV or TSV for the data dictionary
   * REDCap has an example [data dictionary template](https://github.com/sglcsb/health/wiki/REDCap-EDC-Data-Dictionary-template)
   * It is highly recommended to use standard ontology terms as field names and value options where applicable
   * Map the data dictionary to applicable standards in your disease/research area to improve interoperability in future data use

* Once the data collection workflow is finalised, design a diagram of the workflow with tools like draw.io or Miro. This will help to understand the bottlenecks of the flow better. Keep the workflow diagram updated if there are any changes to the workflow.
* Use or deploy GDPR-compliant Electronic Data Capture (EDC) systems (see Solutions section)
* Import/build the questionnaire/data dictionary into the chosen EDC systems to generate the collection instrument(s) or forms
* Design the survey frontend (user interface) of the collection instrument(s) considering the participant’s perspective. Responsive design and co-development with patient partners are highly recommended.
* Test and retest the data collection forms and UI
* If patients/parents/public are involved in any part of the project, including data system development, make sure their time/expenses are costed into the grant.


### Solutions
GDPR compliant EDC systems that support the capture of COMs:
* {% tool "redcap" %} - Academic licence
    - Check the licence terms carefully, as some uses in commercial research may not be allowed.
    - REDCap – [online training videos](https://tess.elixir-europe.org/materials?tools=REDCap)
* {% tool "redcapcloud" } - Commercial licence
    - A fully managed REDCap system based in the cloud, provided by nPhase.
* {% tool "castor" %} - Academic/commercial licence
* {% tool "eusurvey" %} - SaaS provided by EU commission
* {% tool "limesurvey" %} Open source, 
* {% tool "alchemer" %} – Commercial
* {% tool "jotform"} – Commercial 
* [Data Integration System](https://www.bitcare.de) – Commercial

PII separation and storage systems:
* {% tool "smasch" %} - Open source
* [Mosaic Project](https://www.ths-greifswald.de/en/projekte/mosaic-project/) - Open source 

Improving the FAIRness of health data:
{% tool "fairsharing" %}
{% tool "fair-cookbook" %}


## Electronic Health Record (EHR) data

### Description
Electronic Health Record (EHR) data includes patient identifiers, diagnoses, demographics, procedures, medications, vital signs, laboratory results, and utilisation events as well as financial records or administrative information. Converting these different data types to a usable structured format is critical to improving EHR-originated data management.

### Considerations
The structure of EHRs varies widely within and between countries. Even within a single care provider, there may be multiple EHRs. National and international efforts are underway to drive EHR standardisation and interoperability. It is useful to keep in mind that EHRs are healthcare-oriented electronic tools with a data model design and functionalities intended for critical healthcare operations and not for research.  Therefore, specific standards and methods to extract and transform this information are required to allow such use ethically and legally. This section presents some of the transnational projects working towards improved reuse of EHR data, and the next section introduces key technical standards for storing, integrating, and exchanging EHR and clinical data.

For member states within the EU, the European Commission published a proposed regulation for establishing the [European Health Data Space (or “EHDS”)](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space_en). The proposed regulation establishes a common space for health data where:
  * Individuals are empowered through increased digital access to and control of their electronic personal health data
  * Researchers, innovators and policymakers can request access to these electronic health data in a trusted and secure way that preserves the individual’s personal data
The EHDS will also regulate the interoperability of EHRs to a certain extent, in particular to facilitate the exchange of the patient summary data.

EHDS places a significant emphasis on promoting the secondary use of health data, to serve research, innovation, policy making and regulatory purposes. To achieve this, several European initiatives have been launched to establish its foundation and define guiding principles. Among these endeavors, two signification projects stand out:
- [TEHDAS]( https://tehdas.eu/), the joint action Towards the European Health Data Space, helped develop and promote concepts for the secondary use of health data to benefit public health and health research and innovation in Europe. TEHDAS produced [a set of recommendations]( https://tehdas.eu/results/) for the European Commission and member states to enable secondary use of health data.
- [HealthData@EU Pilot](https://ehds2pilot.eu/) is a project designed to build a pilot version of the EHDS infrastructure for the secondary use of health data “HealthData@EU”. The project establishes connections between data platforms within a network infrastructure and develops services that facilitate the user journey for research projects using health data. It also offers guidelines for data standards, data quality, data security and data transfer to support this cross-border infrastructure.

The EU published an overview of the [national laws on electronic health records](https://health.ec.europa.eu/other-pages/basic-page/overview-national-laws-electronic-health-records-eu-member-states-2016_en) in 2016. Under US law, EHR data is classified as protected health information (PHI) and must comply with security laws and encrypt data properly when sending or retrieving such information. Examples of protected health data include patient names, phone numbers, addresses, dates of birth, social security numbers, and insurance information.
  * Regulations: [Health Insurance Portability and Accountability Act (HIPAA) and Health Information Technology for Economic and Clinical Health (HITECH)](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html)

The [International Patient Summary (IPS)](https://international-patient-summary.net/) is a standardised set of basic patient-related physiological and clinical data that includes the most important health and care related facts required to ensure safe and secure healthcare. It comprises data about medications, allergies/intolerances, problems, immunizations, results and procedures for a specified patient. It is a joint standard of five standard development organisations (CEN, HL7, IHE, ISO and SNOMED) and is actively supported by the Global Digital Health Partnership and the World Health Organisation.

### Solutions

It is likely that the use of one of the following standards will not be a choice, but something imposed by the software providers of the EHR systems.These interchange formats are the standards that are likely to be present as part of the EHR, and include:
* {% tool "hl7fhir" %} is a standard used for health care data exchange and/or storage of semantically annotated clinical or administrative health data that is useful for data integration and data interoperability. Within the FHIR ecosystem there are specific implementation guides for its use in research:
    * Real World Data for Clinical Research ({% tool "vulcan" %}) defines a minimal set of clinical research FHIR resources and elements in an EHR that can be utilised in an interoperable and consistent manner for clinical research
    * {% tool "fhir4fair" %} provides guidance on how FHIR can be used for supporting FAIR health data
* {% tool "iso13606" %} is a standard designed by the European Committee for Standardization to define a rigorous and stable information architecture for communicating part or all of the EHR of a single patient between EHR systems or between EHR systems and a centralised EHR data repository. It may also be used for EHR communication between an EHR system and clinical applications or middleware components, or for representing EHR data within a federated record system
* The {% tool "eehrxf" %} is recommended by the European Commission to be used for the exchange of EHR data for cross-border healthcare
* The ISO/DIS 141997 standard Biomedical Research Integrated Domain Group ([BRIDG](https://bridgmodel.nci.nih.gov/)) Model is a domain model for data interchange that enables semantic interoperability and intends to integrate biomedical, clinical research and routine healthcare data
* {% tool "openehr" %} - a non‑profit organisation that publishes technical standards for an EHR platform along with domain‑developed clinical models to define content. It is an open health interoperability standard and an alternative to FHIR. The data are patient-centric, i.e., all health data for a person are stored in a lifetime, vendor-independent EHR for that patient

These common data models are less likely to be directly supported by the EHR, but can facilitate sharing and analysis of data, however, EHR data are likely to require curation to these standards:
* {% tool "cdisc" %} is a consortium, which defines several open standards for regulatory approval and case report forms in particular in the context of clinical trials meant for submission to FDA and EMA, e.g.
      * {% tool "adam" %} Analysis Data Model for data and metadata of clinical trial statistical analysis
      * [CTR-XML](https://www.cdisc.org/standards/data-exchange/ctr-xml) Clinical Trial Registry-XML
      * [ODM-XML](https://www.cdisc.org/standards/data-exchange/odm) Operational Data Model-XML
      * [SDTM](https://www.cdisc.org/standards/foundational/sdtm)	Study Data Tabulation Model for clinical study data in a tabular format
* The OMOP Common Data Model [(CDM] (https://ohdsi.github.io/CommonDataModel/) is an open community standard for observational health care data obtained from health records. It uses the OHDSI (Observational Health Data Sciences and Informatics) standard vocabularies. It has quickly gained traction over recent years, amongst others, through the support received from several large EU projects.
* Federated Health Information Model [(VA-FHIM)](https://fhim.org/fhim-model) is a UML-based logical health information model defined by the Open Group, intended to achieve interoperability between multiple healthcare standards and protocols
* Detailed clinical model (DCM) is the [ISO 13972:2022](https://www.iso.org/standard/79498.html) standard. It defines data elements, the relationships between such data elements and terminologies for detailed small, reusable clinical models
Additionally, [FAIRSharing](https://fairsharing.org/) can be used to search for more domain/disease-specific standards (if applicable).


**Data integration tooling**, from EHR to a common data model:
* REDCap has an existing feature, CDIS (Clinical Data Interoperability Services), which allows a REDCap project to interact with an EHR system and pull EHR data into REDCap
* Tools to map datasets to the OMOP CDM
    * [OHDSI software](https://www.ohdsi.org/software-tools/)
    * [CaRROT-Mapper](https://github.com/HDRUK/CaRROT-Mapper)

Comprehensive lists of clinical terminologies are available from the [EBI OLS](https://www.ebi.ac.uk/ols4/ontologies) and [NCBO BioPortal](https://bioportal.bioontology.org/ontologies) ontology catalogues. Ontologies for use with the OMOP CDM are available from [OHDSI Athena](https://athena.ohdsi.org/search-terms/start). Some examples of widely used clinical terminologies in health data research include:
* International Classification of Diseases ([ICD-10](https://icd.who.int/browse10/2019/en), [ICD-11](https://icd.who.int/en))
* Logical Observation Identifiers Names and Codes ([LOINC](https://loinc.org/)) for reporting laboratory test results
* Systematized Nomenclature of Medicine – Clinical Terms ([SNOMED-CT](https://www.snomed.org/))
* Human Phenotype Ontology ([HPO](https://hpo.jax.org/))
* Normalised names for clinical drugs ([RxNorm](https://www.nlm.nih.gov/research/umls/rxnorm/index.html))
