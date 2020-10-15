---
title: "Plants"
summary: How to publish re-usable plant data
---
## General scope
You will find here the guidelines and resources specific to the publication of Findable Accessible Interoperable and Reusable (FAIR) data on plants: models species like Arabidopsis, crops or forest trees. The typical types of data to be handled would be data from phenotyping experiments and genomic data (RNA or DNAseq, genome sequences, gentypes, ...).


## Producing FAIR plant phenotyping data
 
### Description

You plan to collect plant phenotypic data and you want to ensure that this data will be FAIR from their birth. The first key point is to describe the plant varieties and seed lots in proper way using the proper metadata standards and identifiers. You would also like to have a working environment that facilitates data and metadata collection and storage along the project before publication, and some ways of validating your metadata against the standards. Finally you need to identify where to can deposit and publish the plant phenotyping data, given that there is no global centralized archives for that type of data.

### Solutions
* The metadata standard applicable to plant phenotyping experiments is [MIAPPE](https://www.miappe.org/).
  * It contains a section dedicated to the identification of plant biological materials and samples that has been made compatible with the general standard for the identification of plant genetic resources, [The Multi-Crop Passport Descriptors](https://www.bioversityinternational.org/e-library/publications/detail/faobioversity-multi-crop-passport-descriptors-v21-mcpd-v21/).
  * For woody plants, particularly those in forest settings, it is common to use GPS coordinates as a unique identifier.

* Tools for data collection and management (internal link to a generic solution)
  * In addition to generic solutions that can work for plant phenotyping, [COPO](https://copo-project.org/) is a data management platform specific for the plant sciences.
  * The ISA-Tools also include a configuration for MIAPPE and can be used both for filling in metadata and for validating.
  
* Validation of MIAPPE compliance can be done via ISA-Tools (link to ISA-Validator to be added) or upon data deposition in a BrAPI-compliant repository ([Breeding API, BrAPI](https://brapi.org/).

* Data should be deposited into one of the many repositories that implement BrAPI, as this enables both validation and findability, through the [FAIDARE plant data discovery service](https://urgi.versailles.inrae.fr/faidare/).


## Collecting and depositing plant phenotyping data in a dedicated repository
 
### Description 
You are managing your own repository of plant phenotyping data and you feed it from datasets produced in different collaborative projects. Some partners of these projects use their own data management platforms, while others collect data manually into excel spreadsheets. You want to ensure that the uptake of the data from your partners and its import in your repository is easy and includes a step of validation of the metadata upon intake.

### Solutions
* For collaborators that collect data manually, you should define a spreadsheet template that is compatible with your database structure 
  * Your template should make use of tools for handling ontology annotations in a spreadsheet (internal link to appropriate page) 
  * If your database is MIAPPE compliant, you can use the [MIAPPE-compliant spreadsheet template](https://github.com/MIAPPE/MIAPPE/raw/master/MIAPPE_Checklist-Data-Model-v1.1/MIAPPE_templates/MIAPPEv1.1_training_spreadsheet.xlsx)
* For collaborators that collect data in their own data management platforms:
  * If it implements [BrAPI](https://brapi.org/), you can ingest data using BrAPI calls
  * If it doesn’t implement BrAPI, they should export their data into the spreadsheet template you define for manual collection
* Data validation can be done via BrAPI

 



