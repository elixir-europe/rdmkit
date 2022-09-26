---
title: Plant sciences
description: Data management solutions for plant sciences data
contributors: [Anne-Françoise Adam-Blondon, Sebastian Beier, Cyril Pommier, Erwan Le Floch, Daniel Faria]
related_pages: 
page_id: plants
related_pages: 
  your_tasks: [metadata]
  tool_assembly: [plant geno assembly, plant pheno assembly]
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=plant%20data%20management
faircookbook:
- name: Plant genomic and genetic variation data submission to EMBL-EBI databases
  url: https://w3id.org/faircookbook/FCB061
---

## Introduction

### Data management challenges in plant sciences
The plant science domain includes studying the adaptation of plants to their environment, with applications ranging from improving crop yield or resistance to environmental conditions, to managing forest ecosystems. Data integration and reuse are facilitators for understanding the play between genotype and environment to produce a phenotype, which requires integrating phenotyping experiments and genomic assays made on the same plant material, with geo-climatic data. Moreover, cross-species comparisons are often necessary to understand the mechanisms behind phenotypic traits, especially at the genotypic level, due to the gap in genomic knowledge between well-studied plant species (namely Arabidopsis) and newly sequenced ones.

The challenges to data integration stem from the multiple levels of heterogeneity in this domain. It encompasses a variety of species, ranging from model organisms, to crop species, to wild plants such as forest trees. These often need to be detailed at infra-specific levels (e.g. subspecies, variety), but naming at these levels sometimes lacks consensus. Studies can take place in a diversity of settings including indoor (e.g. growth chamber, greenhouse) and outdoor settings (e.g. cultivated field, forest) which differ fundamentally on the requirements and manner of characterizing the environment. Phenotypic data can be collected manually or automatically (by sensors and drones), and be very diverse in nature, spanning physical measurements, the results of biochemical assays, and images. Some omics data can be considered as well as molecular phenotypes (e.g. transcriptome, metabolomes, …). Thus the extension and depth of metadata required to describe a plant experiment in a FAIR-compliant way is very demanding for researchers.

Another particularity of this domain is the absence of central deposition databases for certain important data types, in particular data deriving from plant phenotyping experiments. Whereas datasets from plant omics experiments are typically deposited in global deposition databases for that type of experiment, those from phenotyping experiments remain in institutional or at best national repositories. This makes it difficult to find, access and interconnect plant phenotyping data.

## Plant biological materials: (meta)data collection and sharing

### Description
Plant genetic studies such as genomic-based prediction of phenotypes requires the integration of genomic and phenotypic data with data about their environment. While phenotypic and environmental data are typically stored together in phenotyping databases, genomic and other types of molecular data are typically deposited in international deposition databases, for example, those of the [INSDC global consortium](http://www.insdc.org/).

It can be challenging to integrate phenotypic and molecular data even within a single project, particularly if the project involves studying a panel of genetic resources in different conditions. It is paramount to maintain the link between the plant material in the field, the samples extracted from them (e.g. at different development stages), and the results of omics experiments (e.g. transcriptomics, metabolomics) performed on those samples, across all datasets that will be generated and published.

Integrating phenotyping and molecular data, both within and between studies, hinges entirely on precise identification of the plant material under study (down to the variety, or even the seed lot), as well as of the samples that are collected from these plants.

### Considerations
* Are you working with established plant varieties, namely crop plants?
  * Can you trace their provenance to a genebank accession ?
  * Are they identified in a germplasm database with an accession number ?
* Are you working with crosses of established plant varieties?
  * Can you trace the genealogy of the crosses to plant varieties from a genebank or identified in a germplasm database?
* Are you working with experimental material ?
  * Can you trace a genealogy to other material ?
  * How do you unambiguously identify your material ?

### Solutions

#### Identification of plant biological materials
* Detailed metadata needs to be captured on the biological materials used in the study—the accession in the genebank or the experimental identification and, when applicable, the seed lots or the parent plants as well as the possible samples taken from the plant—as they are the key to integrating omics and phenotyping datasets. 

#### Checklists and metadata standard
* The identification and description of plant materials should comply with the standard for the identification of plant genetic resources, The [Multi-Crop Passport Descriptors](https://www.bioversityinternational.org/e-library/publications/detail/faobioversity-multi-crop-passport-descriptors-v21-mcpd-v21/)(MCPD).
  * If you are studying experimental plant materials that cannot be traced to an existing genebank or germplasm database, you should describe them in accordance with the MCPD in as much detail as possible.
  * If your plant materials can be traced to an existing genebank or germplasm database, you need only to cross reference to the MCPD information already published in the genebank or germplasm database. 
  * The minimal fields from MCPD are listed in the Biological Material section of the MIAPPE metadata standard.
  * For wild plants and accessions from tree collections, precise identification often requires the GPS coordinates of the tree. MIAPPE provides the necessary fields.

#### Tools for (meta)data collection
* For identifying your plant material in a plant genetic resource repository (genebank or germplasm database), you can consult the [European Cooperative Programme for Plant Genetic Resources](https://www.ecpgr.cgiar.org/) (ECPGR), which includes a [central germplasm database](https://www.ecpgr.cgiar.org/resources/germplasm-databases/ecpgr-central-crop-databases) and a catalogue of relevant [external databases](https://www.ecpgr.cgiar.org/resources/germplasm-databases/international-multicrop-databases).
* Other key databases for identifying plant material are 
  * the [European Search Catalogue for Plant Genetic Resources](https://eurisco.ipk-gatersleben.de/) (EURISCO), which provides information about more than 2 million accessions of crop plants and their wild relatives, from hundreds of European institutes in 43 member countries 
  * [Genesys](https://www.genesys-pgr.org/), an online platform with a search engine for Plant Genetic Resources for Food and Agriculture (PGRFA) conserved in genebanks worldwide.
* The “Biological Material” section of the [MIAPPE](https://github.com/MIAPPE/MIAPPE/tree/master/MIAPPE_Checklist-Data-Model-v1.1) checklist deals with sample description.

#### (Meta)Data sharing and publication
* For identifying samples from which molecular data was produced, the [BioSamples](https://www.ebi.ac.uk/biosamples/) database is recommended as a provider of international unique identifiers. 
  * The [Plant-miappe.JSon](https://www.ebi.ac.uk/biosamples/schemas/certification/plant-miappe.json) model provided by BioSample is aligned with all recommendations provided above for plant identification and is therefore recommended for your sample submission.
* It is also recommended that you provide permanent access to a description of the project or study, that contains links to all the data, molecular or phenotypic. Several databases are recommended for this purpose including:
  * [Data INRAE](https://data.inrae.fr/)
  * [e!DAL](https://edal.ipk-gatersleben.de/)
  * [Zenodo](https://zenodo.org/)
  * [Biostudies](https://www.ebi.ac.uk/biostudies/)
  * [Fairdomhub](https://fairdomhub.org/)

## Phenotyping: (meta)data collection and publication

### Description
Archiving, sharing, and publication of plant phenotyping data can be challenging, given that there is no global centralized archive for this type of data. Research projects often involve multiple partners, some of which collate data into their own (institutional) data management platforms, whereas others collate data into Excel spreadsheets.

For researchers, it is highly desirable that the datasets collected in different media by the partners in a research project (or across different collaborative projects) can be shared in a way that enables their integration, for collective analysis and for facilitating deposition into a dedicated repository. For managers of plant phenotyping data repositories that support a project or institution, it is essential to ensure that the uptake of data is easy and includes a step of metadata validation upon intake.

It is recommended that metadata collection is contemplated from the start of the experiment and that the working environment facilitates (meta)data collection, storage, and validation throughout the project. In field studies, it is critical to record the geographical coordinates and time of the experiment, for linkage with geo-climatic data. For all study types (fields, growth chamber or greenhouse), the environmental conditions that were measured should be described in detail.

### Considerations
* Did you collect the metadata for the identification of your plant material according to the recommendation provided in the [above section](#plant-biological-materials-metadata-collection-and-sharing) ?
* Have you documented your phenotyping and environment assays (i.e. measurement or computation methodology based on the trait, method, scale triplet) both for direct measures (data collection) and computed data (after data processing or analysis)?
  * Is there an existing [Crop Ontology](https://www.cropontology.org) for the species you experiment and does it describe your assay? If not, have you described your data following the trait, method, scale triplet ? 
* Do you have your own system to collect data and is it compliant with the [MIAPPE](https://www.miappe.org/) standard?
* Are you exchanging data with individual researchers?
  * In what media is data being collected?
  * Is the data described in a [MIAPPE](https://www.miappe.org/)-compliant manner?
* Are you exchanging data across different data management platforms?
  * Do these platforms implement [BrAPI](https://brapi.org/)?
  * If not, are they MIAPPE-compliant and do they enable automated data exchange?

### Solutions

#### Checklists and ontologies
* The metadata standard applicable to plant phenotyping experiments is [MIAPPE](https://www.miappe.org/).
  * There is a section dedicated to the identification of plant biological materials that follows [The Multi-Crop Passport Descriptors](https://www.bioversityinternational.org/e-library/publications/detail/faobioversity-multi-crop-passport-descriptors-v21-mcpd-v21/) (MCPD) described [above](#plant-biological-materials-metadata-collection-and-sharing).
  * There is a section to describe the phenotyping assays based on the [Crop Ontology](https://www.cropontology.org) recommendations.
  * There is a section describing the type of experiment (greenhouse, field, etc…) and it is advisable to collect the location (geographical coordinates) and time where it was performed for linkage with geo-climatic data. 
  * Other sections include description of investigations, studies, people involved, data files, environmental parameters, experimental factors, events, observed variables.
* Tools and resources for data collection and management:
  * [Fairdom-SEEK](https://seek4science.org/) is a free data management platform for which MIAPPE templates are in development.
  * [Dataverse](https://dataverse.org/) is a free data management platform for which MIAPPE templates are in development. It is used in several repositories such as [Data INRAE](https://data.inrae.fr/).
  * [e!DAL](https://edal.ipk-gatersleben.de/) is a free data management platform for which MIAPPE templates are in development.
  * The [ISA-Tools](https://isa-tools.org/) also include a configuration for MIAPPE and can be used both for filling-in metadata and for validating.
  * [COPO](https://copo-project.org/) is a data management platform specific for the plant sciences.
  * [FAIRsharing](https://fairsharing.org) is a manually curated registry of reporting guidelines, vocabularies, identifier scheme, models, formats, repositories, knowledge bases, and data policies that includes many resources relevant for managing plant phenotyping data.
* Validation of MIAPPE compliance can be done via [ISA-Tools](https://isa-tools.org/) or upon data deposition in a [Breeding API](https://brapi.org/) (BrAPI) [compliant repository](https://www.brapi.org/servers).
* If you or your partners collect data manually, it is critical to adopt a spreadsheet template that is compatible with the structure of the database that will be used for data deposition.
  * If the database is MIAPPE compliant, you can use the [MIAPPE-compliant spreadsheet template](https://github.com/MIAPPE/MIAPPE/raw/master/MIAPPE_Checklist-Data-Model-v1.1/MIAPPE_templates/MIAPPEv1.1_training_spreadsheet.xlsx).
  * This template could make use of tools for handling ontology annotations in a spreadsheet, such as [Rightfield](https://rightfield.org.uk/) or [OntoMaton](https://github.com/ISA-tools/OntoMaton).   
* If you or your partners collect data into data management platforms:
  * If it implements BrAPI, you can exchange data using BrAPI calls.
  * If it doesn’t implement BrAPI, the simplest solution would be to export data into the MIAPPE spreadsheet template, or another formally defined data template.
* For data deposition, it is highly recommended that you opt for one of the many [repositories that implement BrAPI](https://www.brapi.org/servers), as they enhance findability through the ELIXIR plant data discovery service, [FAIDARE](https://urgi.versailles.inrae.fr/faidare/), enable machine actionable access to MIAPPE compliant data and validation of that compliance.

## Genotyping: (meta)data collection and publication

### Description
Here are described the mandatory, recommended and optional metadata fields for data interoperability and re-use, as well as for data deposition in EVA (European Variation Archive), the EMBL-EBI's open-access genetic variation archive connected to [BioSamples](https://www.ebi.ac.uk/biosamples/), described [above](#plant-biological-materials-metadata-collection-and-sharing).

### Considerations
* Did you collect the metadata for the identification of your plant samples according to the recommendations provided in the [above section](#plant-biological-materials-metadata-collection-and-sharing) ?
* Is the reference genome assembly available in an [INSDC](https://www.insdc.org/) archive and has GCF / GCA accession number ?
* Is the analytic approach used for creating the VCF file available in a publication and has a DOI ?

### Solutions

#### Checklists, ontologies and file formats
* Sharing plant genotyping data files involves the use of the Variant Call Format (VCF) standard.  
* Findability and reusability of VCF files depends on the supplied metadata and in particular with MIAPPE compliant biological material description: the [plant genomic and genetic variation data submission recipe](https://w3id.org/faircookbook/FCB061) helps you on that topic.

#### Data sharing and publication
* Once the VCF file is ready with all necessary metadata, it can be submitted to the European Variation Archive (EVA). You will find all necessary information on the submission steps on the [EVA submission page](https://www.ebi.ac.uk/eva/?Submit-Data).
