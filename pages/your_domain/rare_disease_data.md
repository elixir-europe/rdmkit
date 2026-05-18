---
title: Rare disease data
description: Data management solutions for rare disease data.
contributors: [Philip van Damme, Nirupama Benis, César Bernabé, Shuxin Zhang, Alberto Camara Ballesteros, Bruna Dos Santos Vieira, Munazah Andrabi]
page_id: rare_disease
related_pages: 
  Your_domain: [human_data]
  Tool_assembly: [fairtracks]
  Your_tasks: [dmp, data_publication, machine_actionability]
fairsharing:
- name: Rare disease data collection
  url: https://fairsharing.org/7475
---

## Introduction
The rare disease (RD) domain brings some unique challenges when it comes to data management. Rare disease research is often scarce and scattered among many institutions in different countries – due to the, per definition, low prevalence of RDs. This makes rare diseases a prime example of a research area that can strongly profit from coordination on an international scale, including data management. RD research should be improved to overcome fragmentation, leading to efficacious use of data and resources, faster scientific progress and competitiveness, and most importantly to decrease unnecessary hardship and prolonged suffering of RD patients. Considering the introduction of omics into care practice and the structuration of RD care centers in {% tool "european-reference-networks" %}, data management is key to ensure data reuse and interpretation. The go-to guidelines for efficient data management are the FAIR Principles for research data management and stewardship. These principles provide guidance for making (meta)data more Findable, Accessible, Interoperable, and Reusable.
Research data on RDs can be found in patient registries, biobanks, genomics & multi-omics repositories, knowledge bases, resources (such as animal models and cell lines libraries), omics deposition & analysis platforms, and translational & clinical research supporting materials and services. This page provides an overview of what steps one should take to make data from those sources FAIR, with an emphasis on patient registries. It is written by people affiliated with the {% tool "european-joint-programme-on-rare-diseases" %} and, therefore, reflects the vision of this project. Information is grouped into six topics: administrative aspects of rare disease data, creating and collecting data, processing data, interpreting data, describing data, and giving access to data.

## Teams for managing rare disease data
### Description
Data management is done by people; it pays off to spend some time building a team with the right people and expertise before embarking on data management activities. 

### Considerations
First, data managers and/or policy makers should define why they want to improve their data management activities (or lack thereof). Data management goals should be captured in a data management plan. 
The [European Rare Disease Registry Infrastructure](https://eu-rd-platform.jrc.ec.europa.eu/erdri-description_en) (ERDRI) provides components to ensure that rare disease registries are searchable, findable, and interoperable. It does so with the {% tool "european-rare-disease-registry-infrastructure-directory-of-registries" %}; and the {% tool "european-rare-disease-registry-infrastructure-metadata-repository" %}. ERDRI.dor provides an overview of registries that have been registered by their owners and includes their main characteristics and description. ERDRI.mdr stores all metadata of the included registries, which eases the integration of data from different rare disease registries. Registry owners should add the relevant information of their registry to ERDRI.dor and ERDRI.mdr.

When going through the process of making a rare disease registry more FAIR, and building a team of people to do so, it is considered good practice to follow the so called ‘three-party collaboration’ setup for interdisciplinary teams. 

Essential roles include:

* FAIRification steward (embedded in a group that has experience with making data FAIR and semantic data modelling). Note: this role relates to the [Research Software Engineer (RSE)](research_software_engineer) role. 
*	Local steward (expert of local data management). Note: this role relates to the [data steward](data_steward) role. 
*	Software engineer responsible for the software that manages the data (it is recommended to avoid vendor lock-in as much as possible).

Recommended additional roles:
*	Project manager (highly recommended organiser role).
*	Part-time advisors for expertise on (i) the domain (e.g., a medical doctor), (ii) international FAIR standards (e.g., a senior FAIR expert), and (iii) implementation of FAIR software.
*	Data scientist dedicated to exploiting the added value of FAIR, machine readable data.

### Solutions
* [European Rare Disease Registry Infrastructure](https://eu-rd-platform.jrc.ec.europa.eu/erdri-description_en) (ERDRI) 


## Creating and collecting rare disease data
### Description
This section covers ways of creating and collecting data in a FAIR way focusing on how to use your electronic data capture system to make you data FAIR as you collect it.  

### Considerations
Data collection for clinical research is often done through (electronic) Case Report Forms (CRFs) using an Electronic Data Capture (EDC) system. When collecting rare disease data, one should ensure that they collect the minimal set of data elements for rare disease registration. The Common Data Elements (CDEs) are a list of core data elements to be collected by rare disease registries, especially the ERN registries, to ensure a certain level of interoperability. The full list of CDEs for rare disease registries can be found in the {% tool "set-of-common-data-elements-for-rare-diseases-registration" %}. 

When choosing an EDC system, it is important to check if the system is open to and supports an implementation of FAIR. Two aspects to take into consideration are, for example: 

*	Does the EDC system support the implementation of a {% tool "fair-data-point" %}?
    *	A FAIR Data Point stores the metadata of the data that has been collected. It makes metadata findable and reusable for others on the internet and offers a uniform way for accessing the data for those who are authorised. 
*	Does the EDC system support semantic data models?
    *	Mapping the eCRFs to the elements of a semantic data model helps making the data being collected interoperable and reusable. The EJP RD developed and published a {% tool "semantic-data-model-of-the-set-of-common-data-elements-for-rare-diseases-registration" %}.

### Solutions
* {% tool "set-of-common-data-elements-for-rare-diseases-registration" %}
* {% tool "semantic-data-model-of-the-set-of-common-data-elements-for-rare-diseases-registration" %}


## Processing rare disease data
### Description
 This section covers the processing of data as it is being collected. It covers the different pseudonymisation tools that could be used for registry data.

### Considerations
For data pseudonymisation, it is recommended to use the {% tool "spider-pseudonymisation-tool" %} offered by the European Platform on Rare Disease Registration.
When making data FAIR retrospectively, it is recommended to follow the [retrospective FAIRification workflow](https://doi.org/10.1162/dint_a_00028). On the other hand, when registry data must be FAIR right from when it is being collected by an EDC system, it is recommended to read two papers ([here](https://ojrd.biomedcentral.com/articles/10.1186/s13023-021-02004-y) and [here](https://pubmed.ncbi.nlm.nih.gov/34454078/)), to learn more about the denovo FAIRification process.

### Solutions
* {% tool "spider-pseudonymisation-tool" %}


## Interpreting rare disease data
### Description
This section deals with the modelling of your data, so it can be annotated with unambiguous terms and the different ways it can be queried.

### Considerations
EJP RD’s CDE semantic model comes with a data transformation tool called ‘CDE in a box’, which transforms data in CSV format to linked data according to the model. The {% tool "common-data-elements-in-a-box" %} tool works independently from any EDC system. Additionally, the EJP RD will provide mappings to other data models such as the Observational Health Data Sciences and Informatics (OMOP) Common Data Model, the Clinical Data Interchange Standards Consortium (CDISC) Operational Data Model, and Health Level 7’s Fast Healthcare Interoperability Resources (FHIR). 
To enable data discovery and querying, the EJP RD is developing a Virtual Platform for rare disease resources. This Virtual Platform is a federated ecosystem in which resources are enhanced to be amenable for rare disease research. Data stays at its source but can be queried remotely through an EJP RD query endpoint. As an ecosystem, multiple query endpoints will be present, allowing for sending interrogations from one resource to another. Thus, federated discovery, querying, and analysis are made possible. All while preserving patient privacy and respecting the access conditions of individual resources. 

### Solutions
* {% tool "common-data-elements-in-a-box" %}
* {% tool "european-joint-programme-on-rare-diseases-virtual-platform" %}

## Describing rare disease data
### Description
This section deals with the information needed to properly describe your data, so users can reuse it. It covers the use of FAIR Data Points and database technologies to store data.

### Considerations
When describing rare disease data (i.e., describing the metadata), one could make use of the FAIR Data Point specification as mentioned earlier. This specification offers an extended metadata model based on the {% tool "data-catalog-vocabulary" %}, a [World Wide Web Consortium (W3C)](https://www.w3.org/) recommendation. Once the FAIR Data Point has been set up properly it should be visible in the list of active {% tool "fair-data-points" %}. Note: make sure that the registry’s Data Access Policy allows for sharing of metadata. 

### Solutions
* {% tool "european-joint-programme-on-rare-diseases-metadata-model" %}
* {% tool "fair-data-points" %}


## Giving access to rare disease data
### Description
This section deals with the information needed by people who will re-use your data, and with the access conditions they will need to follow.  

### Considerations
Two main topics can be addressed when dealing with data access. First, the collection of informed consent through an informed consent form. Second, specifying who is allowed access to which data using an Authentication and Authorization Infrastructure (AAI). The informed consent form should use existing standards for informed consent. The EJP RD has developed a {% tool "ern-registries-generic-informed-consent-forms" %}.

### Solutions
* {% tool "european-joint-programme-on-rare-diseases-metadata-model" %}
* {% tool "ern-registries-generic-informed-consent-forms" %}
