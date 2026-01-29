---
title: Cancer data
description: Data management solutions for human cancer data
contributors: [Fátima Al-Shahrour, Erika Schirghuber, Robin Navest, Eva Budinska, Gonzalo Gómez, María González, Fotis Psomopoulos, Sarah Morgan, Sophie Huiskes Berends]
page_id: cancer_data
related_pages: 
  Your_tasks: [sensitive, gdpr_compliance,data_security]
training:
- name: Training in TeSS
  registry: TeSS
  url: https://tess.elixir-europe.org/collections/rdmbites-redcap-collection
- name: OMOP Common Data Model and the OHDSI analytics for observational analytics of real world healthcare data courses in EHDEN academy
  url: https://academy.ehden.eu/
fairsharing:
- name: Cancer data collection
  url: https://fairsharing.org/7486
---
## Introduction

Cancer is a heterogeneous disease that affects almost everyone: as a patient, survivor, relative or friend. This page focuses on the key data management challenges, considerations and solutions that are relevant across all stages of the patient’s journey from cancer prevention, diagnosis and treatment to assessment of patient outcomes and monitoring those at follow-up visits. 

Each stage of the patient journey has different associated data types,  a number of  technical, ethical, legal and organisational challenges. In this page we focus on the management of human health data generated from patients diagnosed with both solid and liquid tumors (oncology or hematology). Data might be collected by a number of different means, e.g. from clinical trials and non-interventional studies (NIS) or real-world data (RWD) from observational studies (e.g. registries) or captured in electronic health record (EHR) hospital systems during primary care. 

Efficient data management and interoperability are essential for ensuring timely and accurate diagnoses and treatment while maintaining compliance with ethical and regulatory standards. In the following sections we will address data management best practices, considerations and possible solutions for effective management of data in each stage (Figure1)  of the individual patient's journey.

{% include image.html file="cancer_dm_stages.png" caption="Figure 1. Cancer data management challenges at different stages of patient journey." %}


## Cancer prevention
 
### Description

#### Primary prevention data

Primary prevention in cancer care refers to strategies aimed at reducing the risk of developing cancer. Data from cancer registries (which includes spatial patterns of cancer incidence, as well as stage, survival and mortality) in combination with genetic predisposition and/or exposome data (including exposure to environmental factors and socio-economic characteristics) can be used to identify risk factors for developing cancer. These cancer registries are information systems designed for the collection, storage, and management of data on persons with cancer and play a critical role in cancer research, surveillance, cancer prevention and control interventions. Key challenges include heterogeneity in data collection and integrating diverse datasets from different sources, e.g. linkage of exposome data to the health data from cancer registries. 

#### Secondary prevention data

Secondary prevention in cancer care focuses on early detection and intervention to identify cancer at an early stage when it is more treatable and potentially curable. Survival rate improvement in most major tumour types depends on early detection, which has prompted screening programs in many European countries. These programs produce highly relevant data sets for further (data-driven) research on early cancer diagnostics. This data typically consists of health and bioimaging data, such as mammograms, colonoscopies, or blood tests. Most of this data contains personal health information and must be managed in compliance with privacy regulations such as GDPR.

Key challenges include integrating diverse datasets and ensuring data accuracy since the screening programs could be organised on national or regional level. Additionally, the risks and benefits of screening programs must be balanced.


### Considerations 

#### Primary prevention data

* Consider local cancer registries in the different European countries as they can be organised locally, regionally or nationally.
* Think about the health data access procedures which could be different for each cancer registry.
* Bear in mind the interoperability of variables from the exposome data could be suboptimal due to heterogeneous data collection between different sources.
* Linkage between different data types, e.g. exposome and health data, could be non-trivial. Think about the following:
  * Does the geographical grid match?
  * Does the timestamp of the data correlate?
* Exposome data is considered non-personal data, but once linked to personal data the linked dataset becomes personal data and privacy has to be ensured in compliance with applicable legislation (e.g. GDPR).

#### Secondary prevention data

* The data access procedure could be different for different data sources. Be mindful to contact the relevant data creators and managers for the relevant access rights.
* Interoperability of data originating from multiple screening programs is not guaranteed.
* For general health data considerations, see [Health data page](health_data).
* For general bioimaging data considerations, see [BioImaging data page](bioimaging_data).


### Solutions

#### Primary prevention data

* For data management considerations and solutions of Patient-generated health data and Electronic Health Record (EHR) data see the [Health data page](human_data).
* Cancer registry data common rules and definitions used within Europe defined by the [European Network of Cancer Registries (ENCR)](https://www.encr.eu/ENCR-Recommendations).
* Exposome data management recommendations under development by [Environmental Exposure Assessment Research Infrastructure (EIRENE-RI)](https://eirene.eu/).
* Exposome (meta)data definitions used within Europe defined by Eurostat, [Euro SDMX Registry](https://webgate.ec.europa.eu/fusionregistry/).

#### Secondary prevention data

As there are no commonly accepted data collection standards currently, [EOSC4Cancer](https://eosc4cancer.eu/the-project/) developed a harmonised codebook for colorectal cancer screening (based on Dutch, Catalan, Italian and Czech screening codebooks), which could be used as a common basis to be extended to other cancer types.


## Cancer diagnosis

### Description

A cancer patient's journey starts with a confirmed diagnosis, which involves clinical evaluation, imaging, laboratory tests, and testing of molecular biomarkers by different methods (e.g. immunohistochemistry, next-generation sequencing, in situ hybridisation) in biopsies (e.g. tissue or liquid biopsies) to confirm malignancy and assess tumour characteristics. 

Cancer diagnosis is a multi-step process that begins with a patient's clinical presentation, such as symptoms or incidental findings during routine check-ups or specialized screening programs (e.g. mammography for breast cancer, FIT tests and consequent colonoscopy for colorectal cancer, Pap smears and HPV PCR for cervical cancer). If cancer is suspected, the diagnostic journey typically involves a combination of medical imaging (CT, MRI, PET scans, ultrasound), laboratory tests, and biopsy procedures to confirm malignancy, each step producing a different data type. Integrating diverse data sources, including clinical history, imaging, pathology, and genomic data, allows for a more comprehensive understanding of the disease and personalized treatment strategies. 

Cancer diagnosis relies on data from multiple sources that are also often used at other stages of the cancer patient's journey (prevention, treatment, follow-up):

* **Imaging** (MRI, CT, PET scans) provides tumor size, location, and spread
* **Pathology** (biopsy analysis) confirms tumor type and molecular characteristics
* **Genetic/Genomic** profiling can identify tumor genomic alterations relevant for molecularly matched therapies, pharmacogenomic biomarkers relevant for drug metabolism, germline alterations
* **Clinical data** (patient history, symptoms, lab tests) provide context on overall health and treatment history

Managing cancer data for diagnosing and determining the best treatment for localized tumors presents several challenges, as it requires working with a wide range of [sensitive patient data](sensitive), coming from different departments/sources, including [clinical records](health_data), [radiological images](bioimaging_data) (radiology), histopathological evaluation (pathology) and genomic profiles (pathology or other specialized laboratory). This makes interoperability and data integration essential to enable a holistic approach to cancer care. Consequently,  data management must be precise to ensure that healthcare professionals have accurate and comprehensive information for tumour identification and treatment decisions. Data security and compliance with ethical guidelines (such as [GDPR](gdpr_compliance)) are critical to protecting patient privacy when dealing with personal health records and sensitive tumour data. Furthermore, the need for data to be accessible across different healthcare providers and research institutions adds complexity to the management process.

### Considerations

* Are all clinically relevant variables collected using standard vocabularies across data domains including socio-demographics, risk factors, and tumor-specific metadata (e.g. Tumour- Nodes-Metastases (TNM) stage, histology, genomic alterations)?
* Are diagnostic data and images stored in standardized formats (e.g. {% tool "dicom" %} for imaging, {% tool "vcf" %} for genomics) to allow long-term usability and reanalysis?
* Is there a data management system in place to ensure interoperability between different data types (e.g. imaging, molecular, and health records)?
* Are there AI-based tools or decision-support systems integrated into the workflow to assist oncologists in making diagnostic decisions?

### Solutions

* Utilize structured clinical data models and interoperability frameworks (e.g. {% tool "hl7-fhir" %}, {% tool "omop-cdm" %}, {% tool "dicom" %} and {% tool "xnat" %} for imaging) to facilitate the integration of multi-modal diagnostic data such as clinical, imaging, and molecular data.
* Implement version-controlled patient records using [EHR](health_data) systems that support updates based on evolving classification standards and cancer-specific coding dictionaries for diagnosis (e.g. {% tool "icd-o-3" %} or {% tool "snomed-ct" %} for cancer diagnosis and topography, {% tool "uicc-tnm" %} staging system, {% tool "who-tc" %}).
* Utilize secure repositories and specialized cancer clinical data management systems (e.g. {% tool "redcap" %}, {% tool "i2b2" %}, {% tool "cbioportal" %}) that comply with GDPR, [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html), and other regulatory frameworks.
* Implement standardized consent forms and patient data governance frameworks, such as GA4GH's {% tool "data-use-ontology" %}, to allow data sharing while maintaining privacy.
* Store raw sequencing and imaging data in cloud-based or institutional repositories (e.g. {% tool "the-european-genome-phenome-archive" %}, {% tool "dbgap" %}, {% tool "sequence-read-archive" %}, {% tool "tcia" %} for imaging) to allow reanalysis when new prognostic markers emerge.
* Adopt federated learning approaches (e.g. {% tool "fega" %}, Federated EHR Learning Models) to enable collaborative research without transferring sensitive patient data.
* Integrate AI-based imaging tools (e.g. {% tool "path-ai" %}, {% tool "qure-ai" %}, {% tool "paige-ai" %}) for radiology and pathology analysis to assist in detecting subtle cancer features and ensure adherence to standards (e.g. {% tool "dome" %}, {% tool "tripod" %}), avoiding biases in cancer diagnosis.


## Cancer treatment

### Description
Cancer treatment varies depending on the type and stage of cancer (e.g. locally advanced, metastatic disease), as well as the overall health and preferences of the patient. The use of advanced diagnostic techniques such as PET-CT/MRI, molecular profiling (e.g. next-generation sequencing, comprehensive genomic profiling (CGP), whole genome sequencing (WGS) and liquid biopsies (e.g. ctDNA) has tremendously increased the data density and complexity to be dealt with at this stage of disease.

Cancer treatment employs a wide range of data types, such as patients' therapeutic regimens, including surgery techniques, stem cell transplantation, radiotherapy, systemic therapies (e.g. hormone, chemotherapy, immunotherapy and targeted therapies) as well as  imaging data, biomarker assessments, responses to therapies data, clinical trial outcomes, drug efficacy, and adverse reactions. Cancer treatment data is commonly associated with further clinical data and patients' information. Due to their sensitive nature, the data must be managed following ethical guidelines, data protection laws, and FAIR (Findable, Accessible, Interoperable, and Reusable) principles.

Although cancer treatment data is crucial for developing personalized medicine approaches, improving patient outcomes and advancing research, comprehensive documentation of cancer treatment data remains limited in cancer registries and public datasets. This challenge is often due to data privacy regulations, ethical concerns, and varying reporting standards, which highlight disparities arising from resource limitations, national database structures, and language barriers. In addition, while cancer treatment data publication has increased, it remains inconsistent due to the lack of data standardization along with sparse ontologies. The increasing use of electronic health records across western countries, along with standardized cancer classification systems (e.g. WHO, ICD, CAP), staging systems (e.g. {% tool "uicc-tnm" %} ), and pioneering drug (e.g. DRON PDRO) and side effects (e.g. OAE) ontologies, facilitates data collection. However, clear guidelines for cancer treatment data collection and tools for unified analysis still need to be developed.

### Considerations 

* Do you use human data? You can find more information on the [Human data page](human_data).
* Are the required clinical variables related to the treatment available?
* How will clinical variables be integrated with molecular or imaging data?
* Which resources are available for downloading and analysing cancer treatment data?
* Where can you access standard-of-care cancer clinical guidelines?
* How to access cancer treatment data from clinical trials or side effect registries?
* How to propose cancer treatments based on cancer multi-omics data?

### Solutions

In order to obtain information about oncological clinical practice guidelines several medical societies provide guidance:

* [European Society of Medical Oncology (ESMO)](https://www.esmo.org/guidelines)
* American Society of Clinical Oncology (ASCO)
  * [General treatment types](https://www.cancer.org/cancer/managing-cancer/treatment-types.html)
  * [Clinical guidelines](https://ascopubs.org/guidelines)
* [National Comprehensive Cancer Network (NCCN)](https://www.nccn.org/guidelines/category_1)

A more unified approach to cancer treatment data collection is crucial for improving outcome analysis and supporting all stakeholders. To support this aim, several consortia and institutions provide annotated reference datasets with cancer treatment data:

#### Reference databases and platforms:

* {% tool "the-european-genome-phenome-archive" %} : Service for permanent archiving and sharing of personally identifiable genetic, phenotypic, and clinical data.
* {% tool "cbioportal" %}: Multidimensional genomics data with treatment annotations.
* {% tool "icgc-argo" %}: Comprehensive clinical and genomic data for >100,000 patients.
* {% tool "aacr-genie" %}: Cancer genomic dataset.
* {% tool "msk-chord" %}: Molecular and clinical data for cancer treatment analysis.
* {% tool "hmf" %}: Multi-omic data for >7000 patients.
* {% tool "wayfind-r" %}: Real-world clinical/genomic data from patients diagnosed with solid tumours across geographies.
* {% tool "eucaim" %}: Federated platform for Cancer image data.
* {% tool "all-of-us" %}: US-based patient health data.
* {% tool "uk-biobank" %}: UK-based longitudinal study of 500,000 UK individuals; multi-level data across a range of diseases.
* {% tool "tcia" %}: Imaging data with metadata.
* {% tool "gdsc" %}): Drug sensitivity data from 1000 cancer cell lines.
* {% tool "ctrp" %}: Genetic and drug sensitivity relationships.

#### Drug and trial public repositories:

* {% tool "nci-drug-database" %}
* {% tool "ema-medicine-finder" %}
* {% tool "clinicaltrials-gov" %}
* {% tool "drugbank" %}
* {% tool "dgidb" %}
* {% tool "drugmap" %}
* {% tool "ttd" %} 
* {% tool "pharmgkb-cancer-pgx" %}
* {% tool "oncokb" %}
* {% tool "sider" %}

#### Genomics & multi-omics resources:

* {% tool "mtb-portal" %}: provides a general framework to interpret the functional and predictive relevance of a given list of gene variants in interactive reports.
* {% tool "pandrugs" %}: a platform to prioritize cancer drug treatments according to individual multi-omics data (SNVs, CNVs and gene expression).
* {% tool "cancer-genome-interpreter" %}: flags genomic biomarkers of drug response with clinical relevance.
* {% tool "civic" %}: a free resource to identify the best cancer treatment options based on DNA alterations.
* [Topograph](https://topograph.info/): Therapy-Oriented Precision Oncology Guidelines for Recommending Anti-cancer Pharmaceuticals.

## Monitoring of outcomes during follow-up visits

### Description

The follow-up phase in cancer care is a critical component of comprehensive patient management, ensuring long-term monitoring and well-being of cancer survivors. This stage focuses on assessing treatment outcomes, detecting potential recurrences, managing long-term side effects, and enhancing the overall quality of life. Effective follow-up strategies integrate not only systematic clinical evaluations, which include routine medical visits, imaging exams (e.g. MRI, CT, PET), and biomarker testing (e.g. CEA, PSA, ctDNA), but also patient-reported outcomes (PROs).

In this context, the increasing adoption of digital health technologies, including wearable devices and mobile health applications, as well as Artificial Intelligence and predictive analytics, has transformed post-treatment monitoring. On one hand, it has enabled real-time remote tracking of health metrics (e.g. physical activity, heart rate, sleep patterns etc), facilitating early detection of potential complications and on the other hand help anticipate complications and tailor follow-up schedules to individual patients' needs. Both scenarios lead to generation of diverse data types. Additionally, cancer registries (CRs) and clinical trial databases play a fundamental role in storing longitudinal data on disease progression, survival rates, and treatment efficacy, allowing researchers to analyze trends, identify recurrence risk factors, and refine personalized follow-up guidelines. 

However, due to the wide heterogeneity of data types, sources, and healthcare systems achieving seamless interoperability and standardisation of follow-up data, to support individualized patient management and optimize data reuse in cancer research remains a major challenge. In addition, data collection and management at this stage presents other challenges, including: (i) the sensitive nature of the data, requiring strict adherence to regulatory and ethical frameworks, (ii) the lack of consistency and/or quality of patient follow-up information, and (iii) the lack of standardization and inherent subjectivity in survivorship quality-of-life data, influenced by patient perception, reporting methods, and assessment tools. 

### Considerations 

Different considerations should be taken into account depending on the type of data being managed:

* Use specific standards and methods to extract and transform data included in the Electronic Health Record (clinical data, diagnoses, demographics, procedures, medications, vital signs, laboratory results). For Considerations towards improved reuse of EHR refer to the section in the [Health data page](health_data).
* Considerations for managing  imaging data (and histopathological data), binary files,as well as the associated metadata can be found in the [Bioimaging data page](bioimaging_data).
* For human genomic data, established research ethical guidelines and legislations must be followed as described in the [Human data page](human_data).
* Since health data falls under the "special category of data" as defined by the GDPR, strict guidelines and considerations must be followed when handling this information covered in the [GDPR compliance](gdpr_compliance) and [Data Sensitivity](sensitive) pages of the RDMkit.
* For PROs, to collect data directly from cancer patients and/or survivors, follow the considerations listed on the health data page. Additionally, since these PROs focus on quality-of-life and are inherently subjective, additional considerations must be addressed:

  * Are questionnaires designed to minimize ambiguity and ensure that all patients interpret questions in a similar way?
  * Are there methods in place to differentiate between true changes in quality of life and variations due to individual perception or recall bias?
  * Have statistical or methodological approaches been considered to adjust for subjectivity in self-reported data?
  * How is the potential discrepancy between patient-reported outcomes and clinician assessments addressed?
 
* For data collected from wearable devices and mobile applications, the follow considerations should be taken into account:
  
  * Are the wearable devices and mobile applications validated to provide accurate real-time measurements?
  * How is the data quality ensured, considering potential sensor calibration issues, environmental factors, or user error?
  * Are there mechanisms in place to handle missing or incomplete data, such as when the device is not worn or battery levels are low?
  * How are transient fluctuations in health metrics differentiated from clinically significant changes?
  * Are patient-specific factors incorporated into the analysis to improve data interpretation?
  * Is there a system for aggregating data from multiple devices or platforms to create a comprehensive view of the patient’s health metrics over time?
 
* To address the potential lack of consistency and/or quality in patient follow-up information, particularly over the long term, the following considerations should be taken into account:

  * How will data consistency be maintained if patients change healthcare providers, devices, or platforms over time?
  * Are there standardized processes in place to ensure that follow-up data from different sources can be seamlessly integrated and compared?
  * Is there a plan to handle potential gaps in data, such as missed follow-up appointments or missing reports?
  * What strategies are in place to encourage continuous patient engagement and adherence to follow-up protocols?
  * Are there periodic checks or audits in place to validate data quality and identify potential discrepancies or inconsistencies?

### Solutions

* To address the challenges associated with the monitoring of outcomes during follow-up visits, the following solutions are proposed:
* Adopt common data models and standards to ensure consistency and interoperability of clinical data across institutions.
    * Regarding data included in the EHR, for standards that are likely to be present as part of such systems, common data models that can facilitate data sharing, and tools for data integration, refer to the section in the [Health data page](health_data). 
    * Regarding imaging data, for standard (meta)data formats, management platforms, ontologies resources, and image repositories, refer to the [Bioimaging page](bioimaging_data).
* Use cancer-specific standard terminologies, ontologies, and reference databases for coding diagnosis related data (e.g. {% tool "icd-o-3" %}, {% tool "who-tc" %}, {% tool "uicc-tnm" %}), treatment related data (e.g. {% tool "ctrp" %}, {% tool "civic" %}, {% tool "ttd" %}) and follow-up related data (e.g. {% tool "meddra" %}, {% tool "ecog" %}, {% tool "percist" %}).
* Utilise GDPR compliant EDC systems that support capture of PROs (refer to the [Health data page](health_data) and structured formats (e.g. [FHIR QuestionnaireResponse](https://build.fhir.org/questionnaireresponse.html)).
* Employ validated and standardised instruments for quality-of-life assessment (e.g. {% tool "eortc-qlq" %}, {% tool "promis" %}) to reduce variability in interpretation and improve comparability. 
* Use certified, clinically validated devices and apps to ensure data reliability and regulatory compliance (e.g. CE-marked, {% tool "fda-approved-tools" %}). Employ data aggregation platforms (e.g. {% tool "apple-health-kit" %}, {% tool "google-fit" %}, {% tool "open-mhealth" %}) that support cross-device integration and longitudinal monitoring.
* Define clear data governance policies for longitudinal data capture and ensure data traceability.
* Establish patient engagement protocols to support consistent reporting and minimise data loss over time. Define standardised follow-up templates to optimise data completeness.

