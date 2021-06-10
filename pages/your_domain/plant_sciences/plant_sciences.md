---
title: Plant sciences
contributors: [Anne-Françoise Adam-Blondon,Daniel Faria]
tags: [metadata]
---

## Introduction
The plant science domain includes studying the adaptation of plants to their environment, with applications ranging from improving crop yield or resistance to environmental conditions, to managing forest ecosystems.

Data integration and reuse are facilitators for understanding the play between genotype and environment to produce a phenotype, which requires integrating phenotyping experiments and genomic assays made on the same plant material, with geo-climatic data. Moreover, cross-species comparisons are often necessary to understand the mechanisms behind phenotypic traits, especially at the genotypic level, due to the gap in genomic knowledge between well-studied plant species (namely *Arabidopsis*) and newly sequenced ones.

The challenges to data integration stem from the multiple levels of heterogeneity in this domain. It encompasses a variety of species, ranging from model organisms, to crop species, to wild plants such as forest trees. These often need to be detailed at infra-specific levels (e.g. subspecies, variety), but naming at these levels sometimes lacks consensus. Studies can take place in a diversity of settings including indoor (e.g. growth chamber, greenhouse) and outdoor settings (e.g. cultivated field, forest) which differ fundamentally on the requirements and manner of characterizing the environment. Phenotypic data can be collected manually or automatically (by sensors and drones), and be very diverse in nature, spanning physical measurements, the results of biochemical assays, and images. Some omics data can be considered as well as molecular phenotypes (e.g. transcriptome, metabolomes, ...). Thus the extension and depth of metadata required to describe a plant experiment in a FAIR-compliant way is very demanding for researchers.

Another particularity of this domain is the absence of central deposition databases for certain important data types, in particular data deriving from plant phenotyping experiments. Whereas datasets from plant omics experiments are typically deposited in global deposition databases for that type of experiment, those from phenotyping experiments remain in institutional or at best national repositories. This makes it difficult to find, access and interconnect plant phenotyping data.


## Plant phenotyping metadata management
 
### Description
It is recommended that metadata collection is contemplated from the start of the experiment and that the working environment facilitates (meta)data collection, storage, and validation throughout the project.

Detailed metadata needs to be captured on a number of aspects. One of the most critical is the description of the biological materials used in the study—the plant varieties and, when applicable, the seed lots or the parent plants—as they are the key to integrating omics and phenotyping datasets. Particularly in field studies, it is equally critical to record the geographical coordinates and time of the experiment, for linkage with geo-climatic data. In growth chamber or greenhouse studies, the environmental conditions that were fixed should be described in detail.

### Considerations

* Is your plant material provided by a genebank or derived from material provided by a genebank?
* Have you documented your phenotyping assays (trait, method, units) both for direct measures (data collection) and computed data (after data processing or analysis)?
  * Is there an existing [Crop Ontology](https://www.cropontology.org) for the species you experiment and does it describe your assay?
* Do you have your own system to collect data and is it compliant with the [MIAPPE](https://www.miappe.org/) standard?

### Solutions
* The metadata standard applicable to plant phenotyping experiments is [MIAPPE](https://www.miappe.org/).
  * It contains a section dedicated to the identification of plant biological materials that follows the general standard for the identification of plant genetic resources, [The Multi-Crop Passport Descriptors](https://www.bioversityinternational.org/e-library/publications/detail/faobioversity-multi-crop-passport-descriptors-v21-mcpd-v21/) (MCPD).
  * It is also possible to describe samples that were collected from the plants chosen for specific phenotyping assays.
  * For woody plants, particularly those in forest settings, it is common to use GPS coordinates as a unique identifier for plant material.
  * There is a section to describe the phenotyping assays based on the [Crop Ontology](https://www.cropontology.org) recommendations.
  * There is section describing the type of experiment (greenhouse, field, etc...) and it is advisable to collect the location (geographical coordinates) and time where it was performed for linkage with geo-climatic data.

* Tools and resources for data collection and management:
  * The [ISA-Tools](https://isa-tools.org/) also include a configuration for MIAPPE and can be used both for filling-in metadata and for validating.
  * [SEEK](https://seek4science.org/) and [Dataverse](https://dataverse.org/) are free data management platforms for which MIAPPE templates are in development.
  * [COPO](https://copo-project.org/) is a data management platform specific for the plant sciences.
  * [FAIRsharing](https://fairsharing.org) is a manually curated registry of reporting guidelines, vocabularies, identifier scheme, models, formats, repositories, knowledgebases, and data policies that includes many resources relevant for managing plant phenotyping data.
  
* Validation of MIAPPE compliance can be done via [ISA-Tools](https://isa-tools.org/) or upon data deposition in a BrAPI-compliant repository ([Breeding API, BrAPI](https://brapi.org/).


## Plant phenotyping data sharing and deposition
 
### Description
Archiving, sharing, and publication of plant phenotyping data can be challenging, given that there is no global centralized archive for this type of data.
Research projects often involve multiple partners, some of which collate data into their own (institutional) data management platforms, whereas others collate data into Excel spreadsheets. For researchers, it would be highly desirable that the datasets collected in different media by the partners in a research project (or across different collaborative projects) can be shared in a way that enables their integration, for collective analysis and for facilitating deposition into a dedicated repository. 
For managers of plant phenotyping data repositories that support a project or institution, it is essential to ensure that the uptake of data is easy and includes a step of metadata validation upon intake.

### Considerations
* Are you exchanging data with individual researchers?
  * In what media are data being collected?
  * Are the data described in a [MIAPPE](https://www.miappe.org/)-compliant manner?
* Are you exchanging data across different data management platforms?
  * Do these platforms implement [BrAPI](https://brapi.org/)?
  * If not, are they MIAPPE-compliant and do they enable automated data exchange? 

### Solutions
* If you or your partners collect data manually, it is critical to adopt a spreadsheet template that is compatible with the structure of the database that will be used for data deposition. 
  * This template should make use of tools for handling ontology annotations in a spreadsheet, such as [OntoMaton](https://github.com/ISA-tools/OntoMaton) 
  * If the database is MIAPPE compliant, you can use the [MIAPPE-compliant spreadsheet template](https://github.com/MIAPPE/MIAPPE/raw/master/MIAPPE_Checklist-Data-Model-v1.1/MIAPPE_templates/MIAPPEv1.1_training_spreadsheet.xlsx)
* If you or your partners collect data into data management platforms:
  * If it implements BrAPI, you can exchange data using BrAPI calls.
  * If it doesn’t implement BrAPI, the simplest solution would be to export data into the MIAPPE spreadsheet template, or another formally defined data template.
* For data deposition, it is highly recommended that you opt for one of the many [repositories that implement BrAPI](https://www.brapi.org/servers), as they enhance findability through the ELIXIR plant data discovery service, [FAIDARE](https://urgi.versailles.inrae.fr/faidare/) and machine actionable access to MIAPPE compliant data.
 
## Integrating plant phenotypic and molecular data
 
### Description 
Genomic-based prediction of plant phenotypes requires the integration of genomic and phenotypic data of the plants with data about their environment. While phenotypic and environmental data are typically stored together in phenotyping databases, genomic and other types of molecular data are typically deposited in international deposition databases, for example, those of the [INSDC global consortium](http://www.insdc.org/). It can be challenging to integrate phenotypic and molecular data even within a single project, particularly if the project involves studying a panel of genetic resources in different conditions. It is paramount to maintain the link between the plant material in the field, the samples extracted from them (e.g. at different development stages), and the results of omics experiments (e.g. transcriptomics, metabolomics) performed on those samples, across all datasets that will be generated and published.

Integrating phenotyping and molecular data, both within and between studies, hinges entirely on precise identification of the plant material under study (down to the variety, or even the seed lot), as well as of the samples that are collected from these plants.

### Considerations
* Are you working with established plant varieties, namely of crop plants?
  * Can you trace their provenance to a genebank and/or are they identified in a germplasm database? 
* Are working with crosses of established plant varieties?
  * Can you trace the geneology of the crosses to plant varieties from a genebank or identified in a germplasm database?
  
### Solutions
* The identification and description of plant materials should comply with the standard for the identification of plant genetic resources, [The Multi-Crop Passport Descriptors](https://www.bioversityinternational.org/e-library/publications/detail/faobioversity-multi-crop-passport-descriptors-v21-mcpd-v21/) (MCPD).
  * If your plant materials that cannot be traced to an existing genebank or germplasm database, you should be describe them in accordance with the MCPD in as much detail as possible.
  * If your plant materials can be traced to an existing genebank or germplasm database, you need only complement the MCPD information already published in the genebank or germplasm database.
  * For wild trees, or plant materials derived from them, precise identification often requires the GPS coordinates of the tree.
* For identifying your plant material in a genebank or germplasm database, you can consult the [European Cooperative Programme for Plant Genetic Resources](https://www.ecpgr.cgiar.org/) (ECPGR), which includes a [central germplasm database](https://www.ecpgr.cgiar.org/resources/germplasm-databases/ecpgr-central-crop-databases) and a catalogue of relevant [external databases](https://www.ecpgr.cgiar.org/resources/germplasm-databases/international-multicrop-databases).
* Another key database for identifying plant material is the [European Search Catalogue for Plant Genetic Resources](https://eurisco.ipk-gatersleben.de/) (EURISCO), which provides information about more than 2 million accessions of crop plants and their wild relatives, from hundreds of institutes in 43 member countries.
* For identifying samples from which molecular data was produced, the [Biosamples](https://www.ebi.ac.uk/biosamples/) database is recommanded as a provider of international unique identifiers.
  * When detailing your sample in Biosamples, it is critical that you provide either a global identifier to your plant materials in a genebank or germplasm database, or a precise description of the plant materials in accordance with the MCPD. 
* It is also recommended that you provide permanent access to a description of the project or study, that contains links to all the data, molecular or phenotypic. The [Biostudies](https://www.ebi.ac.uk/biostudies/) database is recommended for this purpose.

## Relevant tools and resources

{% include toollist.html tag="plants" %}


## Training materials on plant data management
<!-- Link to Tess query -->

{% include tess.html search="plant data management" %}
