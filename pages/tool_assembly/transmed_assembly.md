---
title: TransMed
contributors: [Wei Gu, Soumyabrata Ghosh, Muhammad Shoaib, Irina Balaur, Xinhui Wang, Carlos Vega, Pinar Alper, Venkata Satagopam]
description: TransMed tool assembly from ELIXIR Luxembourg supports projects in clinical and translational biomedicine.
page_id: transmed
affiliations: [ELIXIR Europe, LU]
related_pages: 
  your_tasks: [compliance, storage, metadata, data_organisation, data_analysis, sensitive, GDPR_compliance, dmp]
  your_domain: [human_data]
---

## What is the TransMed data and computing tool assembly?
The TransMed data and computing tool assembly is an infrastructure provided by [ELIXIR Luxembourg](https://elixir-luxembourg.org) for clinical and translational projects. TransMed assembly provides the tools for managing ongoing projects that often require the management of cohort recruitment, and processing of samples, data and metadata. This entails GDPR-compliant and secure data collection, storage, curation, standardisation integration and analysis of clinical data and associated molecular, imaging and sensor/mobile data and metadata.

TransMed tool assembly is also a blueprint showing how a collection of tools can be combined to support data lifecycle management in clinical and translational projects.


## Who can use the TransMed data and computing tool assembly?
All researchers can use tools in the TransMed assembly individually or in combination depending on their project needs. Most of the tools in the TransMed assembly are open-source and can be re-used. ELIXIR Luxembourg provides know-how transfer and training on the tool assembly upon request from researchers and data steward organisations. To make a request please contact [info@elixir-luxembourg.org](mailto:info@elixir-luxembourg.org).

Additionally, ELIXIR Luxembourg provides hosting of the TransMed assembly. Hosting of tools and data is free of charge for national users. For international users hosting of data (up to 10TB) is free on the basis that the data is shared with the wider research community with an appropriate access model such as controlled access. For international users, charges for the hosting tools and hosting of large datasets are evaluated on a case-by-case, please contact [info@elixir-luxembourg.org](mailto:info@elixir-luxembourg.org) for details.


## For what purpose can the TransMed assembly be used?

{% include image.html file="TransMed_assembly.svg" caption="Figure 1. TransMed data and computing tool assembly" alt="TransMed tool assembly" %}


### Data management planning
Translational Biomedicine projects often deal with sensitive data from human subjects. Therefore, data management planning of this type of projects needs to take data protection and GDPR compliance into account .

Typically a TransMed project involves  multiple (clinical) study sites and can contain several cohorts. During the planning phase the dataflow for the project and data/metadata collected prospectively or retrospectively needs to be documented. Projects can use the [Data Information Sheet DISH](http://doi.org/10.5281/zenodo.5127940) to map the project dataflow and collect metadata necessary for GDPR-compliant processing. In addition, a data protection impact assessment needs to be performed taking into account partner roles, responsibilities and the data information collected via the DISH. For this purpose TransMed assembly uses the Data Information System - {% tool "daisy" %}, which indexes all information collected by DISH and provides a repository to accumulate GDPR-required project documentation  such as ethics approvals and consent templates and subject information sheets and ultimately the project data management plan.  TransMed assembly includes the risk management tool {% tool "monarc" %}, which can be used to perform Data Protection Impact Assessments (DPIA). DPIAs are a requirement of the GDPR for projects dealing with sensitive human data.

### Data collection, transfer and storage
For projects involving patient recruitment the TransMed assembly provides the Smart Scheduling System, {% tool "smasch" %}, tracking availability of resources in clinics and manages patient visits. Pseudonymised clinical data and patient surveys are then collected by the state of the art electronic data capture (EDC) system {% tool "redcap" %} through a battery of electronic case report forms (eCRFs). Imaging data from the clinics are deposited into a dedicated imaging platform {% tool "xnat" %}. Omics data, both in raw and derived form can be deposited to the data provenance system {% tool "irods" %}.
The transfer of data files can be done via various encrypted communication options as outlined in the [Data transfer](data_transfer) section of the RDMkit. The TransMed assembly most typically utilises (S)FTP, Aspera FASP and ownCloud. Data is also encrypted at rest with hard-ware and also with file-level encryption using either open-source utilities such as gpg or commercial options such as Aspera FASP.

### Data curation and harmonisation
To facilitate cross-cohort/cross-study interoperability of data, upon collection, the data needs to be curated and harmonised. For this purpose the TransMed assembly uses a variety of open standards and tools. For data quality and cleansing the assembly uses {% tool "openrefine" %}, which provides an intuitive interface to generate facets of data that support the research to identify quality issues and outliner. It also enables traceable and yet easy data correction. For data Extraction, Transformation and Loading (ETL) the assembly uses {% tool "talend" %} Open Studio (for complex and reusable ETLs) as well as R and Python (for ad-hoc and simple transformation). To evaluate and improve FAIRness of datasets, the assembly follows the recipes in the {% tool "fair-cookbook" %} developed by the FAIRplus consortium. Related to standard data models and ontologies the assembly follows the recommendations in the  FAIR Cookbook recipe for selecting terminologies and ontologies.

### Data integration and analysis
TransMed projects usually require different data types from different cohorts to be integrated into one data platform for the exploring, sub-setting and integrated analysis for hypothesis generation. The TransMed assembly consists of several such tools: {% tool "ada-discovery-analytics" %} is a web-based tool to provide a performant and highly configurable system for secured integration, visualization, and collaborative analysis of heterogeneous data sets, primarily targeting clinical and experimental sources. The assembly also includes other tools for specific data types, such as {% tool "atlas" %} that integrate features from various {% tool "ohdsi" %} applications for Electronic Health Record data in {% tool "omop-cdm" %} format into a single cohesive experience. {% tool "transmart" %} is a tool that provides easy integration between phenotypic/clinical data and molecular data and a “drag-and-drop” fashion data exploration interface.

### Data stewardship

To facilitate the findability of data the TransMed assembly provides a {% tool "data-catalog" %} tool that supports the indexing search and discovery of studies, data sets and samples accumulated in the context of projects from different sites and cohorts. The catalog implements a controlled-access model by integration with {% tool "rems" %}. Audit trailing of data access is achieved by integration of the {% tool "daisy" %} in the access process. The catalog tool can be integrated with various identity management systems such as {% tool "keycloak" %}, {% tool "life-science-login" %} or {% tool "free-ipa" %}. 

