---
title: "Plant Sciences"
summary: How to publish reusable plant data
---
## General scope
You will find here the guidelines and resources specific to the publication of Findable Accessible Interoperable and Reusable (FAIR) data on plants. Studied plants can be model species like Arabidopsis, crops, wild species among which forest trees... The typical types of data handled by researchers would be data from phenotyping experiments, genomic assays (RNAseq or DNAseq, genome sequences, genotypes, ...). The main objective is to be able to integrate different types of experiments made on the same plant material (e.g. phenotyping experiments and OMICs experiments) to get knowledge on plant biology. The study of the adaptation of plants to their environment necessitate to integrate experimental data on plant material with geo-climatic data.


## Producing FAIR plant phenotyping data
 
### Description

You plan to collect plant phenotypic data and you want to ensure that this data will be FAIR from their birth. The first key point is to describe the plant varieties and seed lots in proper way using the proper metadata standards and identifiers. You would also like to have a working environment that facilitates data and metadata collection and storage along the project before publication, and some ways of validating your metadata against the standards. Finally you need to identify where to can deposit and publish the plant phenotyping data, given that there is no global centralized archives for that type of data.

### Considerations

* Is your plant material provided by a Genebank or derived from a material provided by a Genebank?
* Have you documented your phenotyping assays (trait, method, units) both for direct measures and computed data?
  * Is there an existing [Crop Ontology](https://www.cropontology.org) for the species you experiment and does it describe your assay?
* Do you have your own system to collect data and is it compliant with the [MIAPPE](https://www.miappe.org/) standard?

### Solutions
* The metadata standard applicable to plant phenotyping experiments is [MIAPPE](https://www.miappe.org/).
  * It contains a section dedicated to the identification of plant biological materials that has been made compatible with the general standard for the identification of plant genetic resources, [The Multi-Crop Passport Descriptors](https://www.bioversityinternational.org/e-library/publications/detail/faobioversity-multi-crop-passport-descriptors-v21-mcpd-v21/).
  * It is also possible to describe samples that were collected from the experimented plants for specific phenotyping assays
  * For woody plants, particularly those in forest settings, it is common to use GPS coordinates as a unique identifier for plant material.
  * There is a section to describe the phenotyping assays based on the [Crop Ontology](https://www.cropontology.org) recommendations
  * There is section describing the experiment itself (greenhouse, field, etc...) and it is advisable to collect its geographical coordinates and time of experiment for linkage with geo-climatic data.

* Tools for data collection and management:
  * The [ISA-Tools](https://isa-tools.org/) also include a configuration for MIAPPE and can be used both for filling in metadata and for validating.
  * [SEEK](https://seek4science.org/) and [Dataverse](https://dataverse.org/) are free softwares that can be used for data management
  * [COPO](https://copo-project.org/) is a data management platform specific for the plant sciences
  * [FAIRsharing](https://fairsharing.org) is a manually curated metadata registry of reporting guidelines, vocabularies, identifier scheme, models, formats, repositories, knowledgebases and data policies in the plant sciences and across domain.
  
* Validation of MIAPPE compliance can be done via [ISA-Tools](https://isa-tools.org/) or upon data deposition in a BrAPI-compliant repository ([Breeding API, BrAPI](https://brapi.org/).

* Data should be deposited into one of the many repositories that implement BrAPI, as this enables both validation and findability, through the [FAIDARE plant data discovery service](https://urgi.versailles.inrae.fr/faidare/).


## Collecting and depositing plant phenotyping data in a dedicated repository
 
### Description 
You are managing your own repository of plant phenotyping data and you feed it from datasets produced in different collaborative projects. Some partners of these projects use their own data management platforms, while others collect data manually into excel spreadsheets. You want to ensure that the uptake of the data from your partners and its import in your repository is easy and includes a step of validation of the metadata upon intake.

### Considerations
* Are the data sets and databases MIAPPE compliant?
* With whom (individual researchers and/or data management platforms) and how (manual and/or automated) will you exchange data?

### Solutions
* For collaborators that collect data manually, you should define a spreadsheet template that is compatible with your database structure 
  * Your template should make use of tools for handling ontology annotations in a spreadsheet like for example [OntoMaton](https://github.com/ISA-tools/OntoMaton) 
  * If your database is MIAPPE compliant, you can use the [MIAPPE-compliant spreadsheet template](https://github.com/MIAPPE/MIAPPE/raw/master/MIAPPE_Checklist-Data-Model-v1.1/MIAPPE_templates/MIAPPEv1.1_training_spreadsheet.xlsx)
* For collaborators that collect data in their own data management platforms:
  * If it implements [BrAPI](https://brapi.org/), you can ingest data using BrAPI calls
  * If it doesn’t implement BrAPI, they should export their data into the spreadsheet template you define for manual collection
* Data validation can be done via BrAPI

 
## Keep the connection between phenotyping and genomic data
 
### Description 
You have set up an experiment in which you are studying a panel of genetic resources in different conditions. You take various phenotyping measurements on the plants themselves and you collect samples at different development stages to perform transcriptomic and metabolomic analysis. You want to ensure that you keep the link between the plant material in the field, their phenotypes and the results obtained in transcriptomics and metabolomics in the data sets that will be generated and when possible published in international archives (transcriptome and metabolome data).

### Considerations
* The key informations for integrating phenotyping and genomic experiments are the identifiers of the different varieties/accessions that constitute the panel of genetic resources that are phenotyped and the identifiers of the samples that are collected from these varieties/accessions for transcriptome and metabolome analysis. these identifiers are generated by distinct groups of people: 
  * laboratories, genebanks or a governed regional network of genebanks like ECPGR or EUFGEN for accessions/varieties
  * international archives dedicated to the description of the samples associated to the genomic data deposited in the archives of the INSDC global consortium  
* Another handy feature is to give a permanent access to a project description that links to all the data and that makes is findable
  
### Solutions
* For phenotyping data, proceed as described in ## Producing FAIR plant phenotyping data
* For transcriptomic data


## Relevant tools and resources

{% include toollist.html tag="plants" %}