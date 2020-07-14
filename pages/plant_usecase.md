---
title: "Plant phenotyping"
keywords: 
sidebar: main
permalink: plant_usecase.html
summary: How to produce and publish plant phenotype data
---


## Producing FAIR plant phenotyping data
 
### Description

Michael is coordinating a project that will be collecting plant phenotypic data and he wants to ensure that this data will be FAIR from their birth. He needs to know how to describe the plant varieties and seed lots his project is using and what metadata standards he should comply with. He would like to have a tool or working environment that facilitates data collection and (meta)data storage along the project’s lifecycle, and some way of validating compliance with the metadata standards. Finally he needs to know where he can deposit his plant phenotyping data.

### Solutions
* Identifying plant biological materials and samples follows general practices in other domains (internal link to a generic solution)
  * [The Multi-Crop Passport Descriptors](https://www.bioversityinternational.org/e-library/publications/detail/faobioversity-multi-crop-passport-descriptors-v21-mcpd-v21/) list the fields recommended for describing plant biological materials.
  * For woody plants, particularly those in forest settings, it is common to use GPS coordinates as a unique identifier.
* The metadata standard applicable to plant phenotyping experiments is [MIAPPE](https://www.miappe.org/)
* Tools for data collection and management (internal link to a generic solution)
  * In addition to generic solutions that can work for plant phenotyping, [COPO](https://copo-project.org/) is a data management platform specific for the plant sciences.
  * The ISA-Tools also include a configuration for MIAPPE and can be used both for filling in metadata and for validating.
* Validation of MIAPPE compliance can be done via ISA-Tools or upon data deposition in a BrAPI-compliant repository.
* Data should be deposited into one of the many repositories that implement BrAPI, as this enables both validation and findability, through the [FAIDARE plant data discovery service](https://urgi.versailles.inrae.fr/faidare/).

## Collecting and depositing plant phenotyping data in a dedicated repository
 
### Description 
Peter manages his own repository of plant phenotyping data that is fed by several research projects of his collaborators. Some collaborators use their own data management platforms, while others collect data manually into excel spreadsheets. He wants to ensure that his collaborators can export data in a way that can be easily fed into his repository, or to incorporate into his repository a solution for ingesting data. He also needs to be able to validate the data upon intake.

### Solutions
* For collaborators that collect data manually, you should define a spreadsheet template that is compatible with the database structure 
 * Your template should make use of tools for handling ontology annotations in a spreadsheet (internal link to appropriate page) 
 * If your database is MIAPPE compliant, you have a [MIAPPE-compliant spreadsheet template](https://github.com/MIAPPE/MIAPPE/raw/master/MIAPPE_Checklist-Data-Model-v1.1/MIAPPE_templates/MIAPPEv1.1_training_spreadsheet.xlsx)
* For collaborators that collect data in their own data management platforms:
 * If it implements BrAPI, you can ingest data using BrAPI calls
 * If it doesn’t implement BrAPI, they should export their data into the spreadsheet template you define for manual collection
* Data validation can be done via BrAPI

 



