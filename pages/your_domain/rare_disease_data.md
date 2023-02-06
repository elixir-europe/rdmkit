---
title: Rare disease data
description: Data management solutions for rare disease data.
contributors: [Philip van Damme, Nirupama Benis, César Bernabé, Shuxin Zhang, Alberto Camara Ballesteros, Bruna Dos Santos Vieira, Munazah Andrabi]
page_id: rare_disease
related_pages: 
  your_domain: [human_data]
  your_tasks: [dmp, data_publication, machine_actionability]
---

## Introduction
The rare disease (RD) domain brings some unique challenges when it comes to data management. Rare disease research is often scarce and scattered among many institutions in different countries – due to the, per definition, low prevalence of RDs. This makes rare diseases a prime example of a research area that can strongly profit from coordination on an international scale, including data management. RD research should be improved to overcome fragmentation, leading to efficacious use of data and resources, faster scientific progress and competitiveness, and most importantly to decrease unnecessary hardship and prolonged suffering of RD patients. Considering the introduction of omics into care practice and the structuration of RD care centers in [European Reference Networks](https://ec.europa.eu/health/european-reference-networks_en) (ERNs), data management is key to ensure data reuse and interpretation. The go-to guidelines for efficient data management are the FAIR Principles for research data management and stewardship. These principles provide guidance for making (meta)data more Findable, Accessible, Interoperable, and Reusable.
Research data on RDs can be found in patient registries, biobanks, genomics & multi-omics repositories, knowledge bases, resources (such as animal models and cell lines libraries), omics deposition & analysis platforms, and translational & clinical research supporting materials and services. This page provides an overview of what steps one should take to make data from those sources FAIR, with an emphasis on patient registries. It is written by people affiliated with the [European Joint Programme on Rare Diseases](https://www.ejprarediseases.org/) (EJP RD) and, therefore, reflects the vision of this project. Information is grouped into six topics: administrative aspects of rare disease data, creating and collecting data, processing data, interpreting data, describing data, and giving access to data.

## Teams for managing rare disease data
### Description
Data management is done by people; it pays off to spend some time building a team with the right people and expertise before embarking on data management activities. 

### Considerations
First, data managers and/or policy makers should define why they want to improve their data management activities (or lack thereof). Data management goals should be captured in a data management plan. 
The [European Rare Disease Registry Infrastructure](https://eu-rd-platform.jrc.ec.europa.eu/erdri-description_en) (ERDRI) provides components to ensure that rare disease registries are searchable, findable, and interoperable. It does so with the European Directory of Registries (ERDRI.dor); and the Central Metadata Repository (ERDRI.mdr). ERDRI.dor provides an overview of registries that have been registered by their owners and includes their main characteristics and description. ERDRI.mdr stores all metadata of the included registries, which eases the integration of data from different rare disease registries. Registry owners should add the relevant information of their registry to ERDRI.dor and ERDRI.mdr. 

When going through the process of making a rare disease registry more FAIR, and building a team of people to do so, it is considered good practice to follow the so called ‘three-party collaboration’ setup for interdisciplinary teams. 

Essential roles include:

* FAIRification steward (embedded in a group that has experience with making data FAIR and semantic data modelling). Note: this role relates to the [Data Steward: infrastructure](data_steward_infrastructure) role. 
*	Local steward (expert of local data management). Note: this role relates to the [Data Steward: research](data_steward_research) role. 
*	Software engineer responsible for the software that manages the data (it is recommended to avoid vendor lock-in as much as possible).

Recommended additional roles:
*	Project manager (highly recommended organizer role).
*	Part-time advisors for expertise on (i) the domain (e.g., a medical doctor), (ii) international FAIR standards (e.g., a senior FAIR expert), and (iii) implementation of FAIR software.
*	Data scientist dedicated to exploiting the added value of FAIR, machine readable data.

### Solutions
* [European Rare Disease Registry Infrastructure](https://eu-rd-platform.jrc.ec.europa.eu/erdri-description_en) (ERDRI) 


## Creating and collecting rare disease data
### Description
This section covers ways of creating and collecting data in a FAIR way focusing on how to use your electronic data capture system to make you data FAIR as you collect it.  

### Considerations
Data collection for clinical research is often done through (electronic) Case Report Forms (CRFs) using an Electronic Data Capture (EDC) system. When collecting rare disease data, one should ensure that they collect the minimal set of data elements for rare disease registration. The Common Data Elements (CDEs) are a list of core data elements to be collected by rare disease registries, especially the ERN registries, to ensure a certain level of interoperability. The full list of CDEs for rare disease registries can be found [here](https://eu-rd-platform.jrc.ec.europa.eu/set-of-common-data-elements_en). 

When choosing an EDC system, it is important to check if the system is open to and supports an implementation of FAIR. Two aspects to take into consideration are, for example: 

*	Does the EDC system support the implementation of a [FAIR Data Point](https://www.fairdatapoint.org/)?
    *	A FAIR Data Point stores the metadata of the data that has been collected. It makes metadata findable and reusable for others on the internet and offers a uniform way for accessing the data for those who are authorized. 
*	Does the EDC system support semantic data models?
    *	Mapping the eCRFs to the elements of a semantic data model helps making the data being collected interoperable and reusable. The EJP RD developed and published a [semantic data model based on the CDEs for rare disease registries](https://github.com/ejp-rd-vp/CDE-semantic-model).

### Solutions
* [Common Data Elements for rare disease registries](https://eu-rd-platform.jrc.ec.europa.eu/set-of-common-data-elements_en)
* [Semantic data model EJP RD](https://github.com/ejp-rd-vp/CDE-semantic-model)


## Processing rare disease data
### Description
 This section covers the processing of data as it is being collected. It covers the different pseudonymisation tools that could be used for registry data.

### Considerations
For data pseudonymization, it is recommended to use the [pseudonymization tool](https://eu-rd-platform.jrc.ec.europa.eu/erdri/pseudonymisation-tool_en) offered by the European Platform on Rare Disease Registration.
When making data FAIR retrospectively, it is recommended to follow the [retrospective FAIRification workflow](https://doi.org/10.1162/dint_a_00028). On the other hand, when registry data must be FAIR right from when it is being collected by an EDC system, it is recommended to read two papers ([here](https://ojrd.biomedcentral.com/articles/10.1186/s13023-021-02004-y) and [here](https://pubmed.ncbi.nlm.nih.gov/34454078/)), to learn more about the denovo FAIRification process.

### Solutions
* [Pseudonymization tool EU RD platform](https://eu-rd-platform.jrc.ec.europa.eu/erdri/pseudonymisation-tool_en)


## Interpreting rare disease data
### Description
This section deals with the modeling of your data, so it can be annotated with unambiguous terms and the different ways it can be queried.

### Considerations
EJP RD’s CDE semantic model comes with a data transformation tool called ‘CDE in a box’, which transforms data in CSV format to linked data according to the model. The '[CDE in a box](https://github.com/ejp-rd-vp/cde-in-box)' tool works independently from any EDC system. Additionally, the EJP RD will provide mappings to other data models such as the Observational Health Data Sciences and Informatics (OMOP) Common Data Model, the Clinical Data Interchange Standards Consortium (CDISC) Operational Data Model, and Health Level 7’s Fast Healthcare Interoperability Resources (FHIR). 
To enable data discovery and querying, the EJP RD is developing a Virtual Platform for rare disease resources. This Virtual Platform is a federated ecosystem in which resources are enhanced to be amenable for rare disease research. Data stays at its source but can be queried remotely through an EJP RD query endpoint. As an ecosystem, multiple query endpoints will be present, allowing for sending interrogations from one resource to another. Thus, federated discovery, querying, and analysis are made possible. All while preserving patient privacy and respecting the access conditions of individual resources. 

### Solutions
* [CDE in a box](https://github.com/ejp-rd-vp/cde-in-box)
* [EJP RD Virtual Platform](https://vp.ejprarediseases.org/)

## Describing rare disease data
### Description
This section deals with the information needed to properly describe your data, so users can reuse it. It covers the use of FAIR Data Points and database technologies to store data.

### Considerations
When describing rare disease data (i.e., describing the metadata), one could make use of the FAIR Data Point specification as mentioned earlier. This specification offers an extended metadata model based on the [Data Catalog Vocabulary (DCAT) version 2](https://www.w3.org/TR/vocab-dcat-2/), a [World Wide Web Consortium (W3C)](https://www.w3.org/) recommendation. Once the FAIR Data Point has been set up properly it should be visible in the list of active [FAIR Data Points](https://home.fairdatapoint.org/). Note: make sure that the registry’s Data Access Policy allows for sharing of metadata. 

### Solutions
* [EJP RD metadata model](https://github.com/ejp-rd-vp/resource-metadata-schema)
* [FAIR Data Point](https://www.fairdatapoint.org/)


## Giving access to rare disease data
### Description
This section deals with the information needed by people who will re-use your data, and with the access conditions they will need to follow.  

### Considerations
Two main topics can be addressed when dealing with data access. First, the collection of informed consent through an informed consent form. Second, specifying who is allowed access to which data using an Authentication and Authorization Infrastructure (AAI). The informed consent form should use existing standards for informed consent. The EJP RD has developed a generic informed consent form for ERN registries that can be found [here](https://www.ejprarediseases.org/ern-registries-generic-icf/).

### Solutions
* [EJP RD metadata model](https://github.com/ejp-rd-vp/resource-metadata-schema)
* [Informed consent form for ERN registries](https://www.ejprarediseases.org/ern-registries-generic-icf/)
