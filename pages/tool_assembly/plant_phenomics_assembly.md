---
title: Plant Phenomics
contributors: [Anne-Françoise Adam-Blondon, Cyril Pommier, Bert Droesbeke, Matthias Lange, Daniel Arend, Daniel Faria, Isabelle Alic, Philippe Rocca-Serra, Sebastian Beier, Erwan Le Floch]
description: Tool assembly for managing plant phenomic data.
page_id: plant_pheno_assembly
affiliations:
related_pages: 
  your_tasks: [metadata, data_publication]
  your_domain: [plants]
  tool_assembly: [plant_geno_assembly]
training:
  - name: MIAPPE training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=miappe
  - name: MIAPPE templates on GitHub
    registry: GitHub
    url: https://github.com/MIAPPE/MIAPPE/tree/master/MIAPPE_Checklist-Data-Model-v1.1/MIAPPE_templates
  - name: PHIS user documentation
    registry:
    url: https://opensilex.github.io/phis-docs-community/
  - name: PHIS developer documentation
    registry:
    url: https://opensilex.github.io/docs-community-dev/
faircookbook:
- name: Publishing plant phenotypic data
  url: https://w3id.org/faircookbook/FCB083PRE
---

## What is the plant phenomics tool assembly and who can use it?

The plant phenomics tool assembly covers the whole [life cycle](data_life_cycle) of experimental plant phenotyping data. It uses the concepts of the {% tool "miappe" %} (Minimum Information About a Plant Phenotyping Experiment) standard: (i) experiments description including organisation, objectives and location, (ii) biological material description and identification and (iii) traits (phenotypic and environmental) description including measurement methodology. A more [detailed overview](https://www.miappe.org/overview/) of the MIAPPE standard is available, as well as the full [specifications](https://www.miappe.org/support/#miappe-spec).

The plant phenomics tool assembly helps [everyone](your_role) in charge of plant phenotyping data management to enable:
* the integration of phenotyping data with other omics data: see the general principles on the [Plant Sciences domain page](plant_sciences);
* the findability of their data in plant specific (e.g. {% tool "faidare" %}) or generic search portal (e.g. Google Data Search);
* the long term reusability of their data.

## How can you access the plant phenomics tool assembly?

All the components of the plant phenomics tool assembly are publicly available and listed below, but many of them require registration.

{% include image.html file="plant_phenomics.svg" caption="Figure 1. The plant phenomics tool assembly." alt="Tools and resources used in managing plant phenomics and phenotyping data." %}

### Data management planning

The general principles to be considered are described in the [Plant Sciences domain page](plant_sciences).

* {% tool "data-stewardship-wizard" %} is a human-friendly tool for machine-actionable DMP collaborative editing. The DSW Plant Sciences project template, available on [ELIXIR's DSW instance for researchers](https://researchers.ds-wizard.org) can be used for any plant sciences project. When creating the DMP Project, choose the option "[From Project Template](https://researchers.ds-wizard.org/projects/create/from-template)" and search for the "Plant Sciences" template.

### File based data collection

The metadata and description of your experiments should be filled using a [MIAPPE template](https://github.com/MIAPPE/MIAPPE/tree/master/MIAPPE_Checklist-Data-Model-v1.1/MIAPPE_templates). Note that there is a readme that fully describes each field as well as their type and their optional or mandatory status. All fields should be present in the file you are using, even if you leave the optional ones empty. This will allow standard processing and validation using dedicated tools.

### Experimental data gathering and management 

#### Systems for file based data collection

* {% tool "fairdom-seek" %} is an open source web-based data sharing platform used as a repository or a catalog. It is being deployed as several instances ranging from confidential project data sharing platforms ([INRAE/AGENT](https://urgi.versailles.inrae.fr/fairdom), VIB) to public repositories like {% tool "fairdomhub" %}. It is MIAPPE compliant through the integration of MIAPPE metadata at the investigation, study and assay levels. It can be used for project based early data sharing, in preparation for long term data storage, but also as a preservation tool for raw data.
* {% tool "pisa-tree" %} is a data management solution developed to contribute to the reproducibility of research and analyses. Hierarchical set of batch files is used to create standardized nested directory tree and associated files for research projects.
* {% tool "copo" %} is a data management platform specific to plant sciences.

#### High throughput dedicated systems

* {% tool "phis" %} the open-source Phenotyping Hybrid Information System (PHIS), based on [OpenSILEX](https://github.com/OpenSILEX/), manages and collects data from Phenotyping and High Throughput Phenotyping experiments on a day to day basis. It can store, organize and manage highly heterogeneous (e.g. images, spectra, growth curves) and multi-spatial and temporal scale data (leaf to canopy level) originating from multiple sources (field, greenhouse). 
It unambiguously identifies all objects and traits in an experiment and establishes their relations via ontologies and semantics that apply to both field and controlled conditions. Its ontology-driven architecture is a powerful tool for integrating and managing data from multiple experiments and platforms, for creating relationships between objects and enriching datasets with knowledge and metadata. It is MIAPPE and BrAPI compliant, and naming conventions are recommended for users to declare their resources. Several experimental platforms use PHIS to manage their data, and PHIS instances dedicated to sharing resources (projects, genetic resources, variables) also exist to allow the sharing of studied concepts.
* [PIPPA](https://pippa.psb.ugent.be/) is the PSB Interface for Plant Phenotype Analysis, is the central web interface and database that provides the tools for the management of the plant imaging robots on the one hand, and the analysis of images and data on the other hand. The database supports all MIAPPE fields which are accessible through the BrAPI endpoints. Experiment pages are marked up with Bioschemas to improve findability on google. 

### Data processing and analysis 

It is important to keep in mind the difference between data processing and analysing.

* [Processing](processing) provides the tools and procedures to transform primary data, such as imaging or observational data, to appropriate quality and processability. 
* [Analysing](analysing), on the other hand, is concerned with extracting information from the processed data for the purpose of supporting knowledge acquisition. 
Some analysis tools dedicated to plant phenotyping experiments are registered in bio.tools, for example: {% tool "plant3d" %},{% tool "leafnet" %}, {% tool "plantcv" %}, {% tool "phenomenal-3d" %}

### Data sharing

The data collected and annotated can be [shared](sharing) in trustworthy repositories under clear conditions of access to the data. As no global central repository exists for phenotyping data, the Plant Science research community combines the use of scattered trustworthy repositories and of centralized search tools. 

#### Metadata management

* {% tool "isa4j" %} is a software library which can help you to programmatically generate ISA-Tab formatted metadata for your experiments. This will make your metadata machine-(and human-)readable and thereby improve the reusability of your work. It was especially designed for large datasets and/or to be included in applications which export data regularly, but of course it can also be used for smaller, individual datasets (although you will need to know how to code). Since version 1.1 it also supports specific term completion and validation for MIAPPE, see the [isa4j documentation](https://ipk-bit.github.io/isa4j/miappe-validation.html).

#### Repositories

* {% tool "dataverse" %} is an open source research data repository software used by several research institute over the globe to publicly share heterogenous dataset. In Europe, it is being used among others by the portuguese [DMPortal](https://dmportal.biodata.pt/), the german [Julich data portal](https://data.fz-juelich.de/), and the french [Recherche Data Gouv](https://entrepot.recherche.data.gouv.fr/) (previously Data.INRAE) research communities. Its main strength is its flexibility, as the mandatory metadata are focused on publication information such as title, abstract, authors and keywords. It can therefore host any datatype, which is both a strength and a weakness, as shared good practices are necessary to ensure the reusability and findability of published phenomic data.

* {% tool "e-dal-pgp" %} is a comprehensive research data repository, which is hosted at the [Leibniz Institute of Plant Genetics and Crop Plant Research (IPK) Gatersleben](https://www.ipk-gatersleben.de/en/) and is mainly focused on sharing high valuable and large genomics and phenomics datasets. It is the first productive instance, which is based on the open source {% tool "e-dal" %} infrastructure software and is furthermore a part of the de.NBI/ELIXIR Germany services. All provided datasets are FAIR compliant and citable via a persistent DOI. By using the widely established LifeScience AAI (formerly known as ELIXIR AAI) the submission procedure is open for all ELIXIR associated users. The key feature of e!DAL-PGP is its user-friendly, simple and FAIR-compliant data submission and internal review procedure. The repository has no general limit to any type of size of datasets. A comprehensive documentation including, guidelines, code snippets for technical integration and videos is available on the [project website](https://edal-pgp.ipk-gatersleben.de/).

* {% tool "gnpis" %} is a multispecies integrative information system dedicated to plants. It allows researchers to access genetic, MIAPPE compliant phenotypic data as well as genomic data. It is used by both large international projects and the French National Research Institute for Agriculture, Food and Environment.

* {% tool "zenodo" %} is a powerful data publication service, which is supported by the European commission and focused on research data, including supplemental material like software, tables, figures or slides. Therefore the publication is usually associated with the publication of a research paper, book chapters or presentations. The Zenodo data submission form allows to describe every data file with a set of technical metadata based on the DataCite metadata schema, which is necessary and assign a persistent DOI to every dataset. The Zenodo infrastructure is hosted at the CERN and can publish dataset up to a size of 50 GB for free. For larger datasets a specific support request is necessary. A further valuable feature of Zenodo is the connection to GitHub and the provided opportunity to assign a DOI to a concrete version or rather commit of a hosted software repository which allows to persist software scripts, which improves the reproducibility of research workflows and results, which is often a challenge especially for older research publications.

#### Machine actionable data sharing

* {% tool "brapi" %}(the Breeding API) is a MIAPPE compliant web service specification available on several [deposition databases](https://www.brapi.org/servers). Those endpoints can be validated using the BrAPI validator {% tool "brava" %} BrAPI hosts several documentation and training material to support its usage.

### Data reuse

Plant phenotyping data reuse relies on rich metadata following the MIAPPE specifications annotated with proper ontologies. Most of the important ontologies are registered on FAIRSHARING: use this [search example](https://fairsharing.org/search?fairsharingRegistry=Standard&q=plant&isMaintained=true).

* {% tool "agroportal" %} is a vocabulary and ontology repository for agronomy and related domains.
* {% tool "faidare" %}(FAIR Data-finder for Agronomic Research) is a portal facilitating discoverability of public data on plant biology from a federation of established data repositories.
