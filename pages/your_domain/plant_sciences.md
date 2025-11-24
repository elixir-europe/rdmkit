---
title: Plant sciences
description: Data management solutions for plant sciences data.
contributors: [Anne-Françoise Adam-Blondon, Sebastian Beier, Cyril Pommier, Erwan Le Floch, Daniel Faria, Timothé Cezard, Daniel Arend, Matthijs Brouwer, Manuel Feser]
page_id: plants
related_pages: 
  Your_tasks: [metadata]
  Tool_assembly: [plant_geno_assembly, plant_pheno_assembly, fairtracks]
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=plant%20data%20management
faircookbook:
- name: Improving dataset maturity - MIAPPE-compliant submission to EMBL-EBI databases
  url: https://w3id.org/faircookbook/FCB061
- name: Publishing plant phenotypic data
  url: https://w3id.org/faircookbook/FCB083
---

## Introduction

### Data management challenges in plant sciences
The plant science domain includes studying the adaptation of plants to their environment, with applications ranging from improving crop yield or resistance to environmental conditions to managing forest ecosystems. Data integration and reuse are facilitators for understanding the play between genotype and environment to produce a phenotype, which requires integrating phenotyping experiments and genomic assays made on the same plant material with geo-climatic data. Moreover, cross-species comparisons are often necessary to understand the mechanisms behind phenotypic traits, especially at the genotypic level, due to the gap in genomic knowledge between well-studied plant species and newly sequenced ones.

The challenges to data integration stem from the multiple levels of heterogeneity in this domain. It encompasses a variety of species, ranging from model organisms to crop species and wild plants such as forest trees. These often need to be detailed at infra-specific levels (e.g. subspecies, variety, Genebank material), but naming at these levels sometimes lacks consensus. Studies can take place in a diversity of settings, including indoor (e.g. growth chamber, greenhouse) and outdoor settings (e.g. cultivated field, forest), which differ fundamentally on the requirements and manner of characterizing the environment. Phenotypic data can be collected manually or automatically (e.g. by sensors and drones), and be very diverse in nature, spanning physical measurements, the results of biochemical assays, and images. Some omics data can be considered as well as molecular phenotypes (e.g. transcriptome, metabolomes). Thus, the extension and depth of metadata required to describe a plant experiment in a FAIR-compliant way is very demanding for researchers.

Another particularity of this domain is the absence of central deposition databases for certain important data types, in particular data deriving from plant phenotyping experiments. Whereas datasets from plant omics experiments are typically deposited in global deposition databases for that type of experiment (i.e. EBI, NCBI, DDBJ), those from phenotyping experiments remain in institutional, national(e.g. [Dataverse FR](https://entrepot.recherche.data.gouv.fr/dataverse/inrae), [e!Dal](https://edal-pgp.ipk-gatersleben.de)) or possibly european repositories (i.e. [Zenodo](https://zenodo.org)). This makes it difficult to find, access and interconnect plant phenotyping data to prepare meta analysis.

## Data management planning

### Description 
The general principles for data management planning are described in the [Planning](planning) page of the Data life cycle section, while generic but more practical aspects of writing a DMP can be found on the [Data Management Plan](data_management_plan) page.

### Considerations 

* Important general considerations about data management planning can be found on the [Planning](planning#what-should-be-considered-for-data-management-planning) page.
* Phenotyping data must be described following the {% tool "miappe" %} data standard.
* Omics data should include the Biological Material section of MIAPPE to ensure interoperability with phenotyping data.
* Make sure to identify and describe the biological material and the observation variables in your dataset description and metadata.

### Solutions
The knowledge model of the data management planning application {% tool "data-stewardship-wizard" %} was reviewed for compliance with the needs of the Plant Sciences community.

#### Machine-actionable DMP
* The DSW Plant Sciences project template, available on [ELIXIR's DSW instance for researchers](https://researchers.dsw.elixir-europe.org) can be used for any plant sciences project. When creating the DMP Project, choose the option "[From Project Template](https://researchers.dsw.elixir-europe.org/projects/create/from-template)" and search for the "Plant Sciences" template.

#### DMP as a text document
* {% tool "dataplan" %} is a Data Management Plan generator for plant science. It supports DMPs for Horizon 2020, Horizon Europe and the German BMBF and DFG. The main focus during development was to be able to be used with German funding agencies but was also extended to include other European funders.
* Depending on the country, there might also be other tools to take into consideration: for example, [DMP OPIDoR](https://dmp.opidor.fr) in France or {% tool "dmponline" %} for the UK. Visit the RDMkit [national resources](national_resources) section for details.

## Plant biological materials: (meta)data collection and sharing

### Description
Plant genetic studies, such as GWAS or Genomic Selection, require the integration of genomic and phenotypic data with environmental data. While phenotypic and environmental data are typically stored together in phenotyping databases, genomic and other types of molecular data are typically deposited in international deposition databases, for example, those of the {% tool "international-nucleotide-sequence-database-collaboration" %}.

It can be challenging to integrate phenotypic and molecular data even within a single project, particularly if the project involves studying a panel of genetic resources in different conditions. It is paramount to maintain the link between the plant material in the field, the samples extracted from them (e.g. at different development stages), and the results of omics experiments (e.g. transcriptomics, metabolomics) performed on those samples, across all datasets that will be generated and published.

Integrating phenotyping and molecular data, both within and between studies, hinges entirely on precise identification of the plant material under study (down to the variety or even the seed lot), as well as of the samples that are collected from these plants.

### Considerations
* Are you working with established plant varieties, namely crop plants?
  * Can you trace their provenance to a genebank accession or a plant variety registered in a [national catalog](https://ec.europa.eu/food/plant-variety-portal/)?
  * Are they identified in a germplasm database with an accession number?
* Are you working with crosses of established plant varieties?
  * Can you trace the genealogy of the crosses to plant varieties from a genebank or identified in a germplasm database?
* Are you working with experimental material?
  * Can you trace a genealogy to other material?
  * How do you unambiguously identify your material?

### Solutions

#### Identification of plant biological materials
* Detailed metadata needs to be captured on the biological materials used in the study—the accession in the genebank or the experimental identification and, when applicable, the seed lots or the parent plants as well as the possible samples taken from the plant—as they are the key to integrating omics and phenotyping datasets. 

#### Checklists and metadata standard
* The identification and description of plant materials should comply with the standard for the identification of plant genetic resources, the {% tool "multi-crop-passport-descriptor" %}. 
  * The minimal fields from MCPD are listed in the Biological Material section of the Minimum Information About Plant Phenotyping Experiments (MIAPPE) metadata standard.
  * If you are studying experimental plant materials that cannot be traced to an existing genebank or germplasm database, you should describe them in accordance with the MCPD/MIAPPE Biological Material in as much detail as possible.
  * If your plant materials can be traced to an existing genebank or germplasm database, you need only to cross reference to the MCPD information already published in the genebank or germplasm database.
  * For wild plants and accessions from tree collections, precise identification often requires the GPS coordinates of the tree. MIAPPE provides the necessary fields.

#### Tools for (meta)data collection
* For identifying your plant material in a plant genetic resource repository (genebank or germplasm database), you can consult the European Cooperative Programme for Plant Genetic Resources {% tool "ecpgr" %}, which includes a {% tool "ecpgr-central-crop-databases" %} and a catalogue of relevant {% tool "international-multicrop-databases" %}.
* Other key databases for identifying plant material are 
  * the European Search Catalogue for Plant Genetic Resources {% tool "eurisco" %}, which provides information about more than 2 million accessions of crop plants and their wild relatives from hundreds of European institutes in 43 member countries. 
  * {% tool "genesys" %}, an online platform with a search engine for Plant Genetic Resources for Food and Agriculture (PGRFA) conserved in genebanks worldwide.
* The “Biological Material” section of the {% tool "miappe-checklist-data-model" %} checklist deals with sample description.

#### (Meta)Data sharing
* For identifying samples from which molecular data was produced, the {% tool "biosamples" %} database is recommended as a provider of international unique identifiers. 
  * The {% tool "plant-miappe-json" %} model provided by BioSamples is aligned with all recommendations provided above for plant identification and is therefore recommended for your sample submission.
* It is also recommended that you provide permanent access to a description of the project or study, that contains links to all the data, molecular or phenotypic (see [Data Publication](#Data-Publication))

## Phenotyping: (meta)data collection and sharing

### Description
Archiving, sharing, and publication of plant phenotyping data can be challenging, given that there is no global centralized archive for this type of data. Research projects often involve multiple partners, some of which collate data into their own (institutional) data management platforms, whereas others collate data into Excel spreadsheets.

For researchers, it is highly desirable that the datasets collected in different media by the partners in a research project (or across different collaborative projects) can be shared in a way that enables their integration for collective analysis and for facilitating deposition into a dedicated repository. For managers of plant phenotyping data repositories that support a project or institution, it is essential to ensure that the uptake of data is easy and includes a step of metadata validation upon intake.

It is recommended that metadata collection is contemplated from the start of the experiment and that the working environment facilitates (meta)data collection, storage, and validation throughout the project. In field studies, it is critical to record the geographical coordinates and time of the experiment for linkage with geo-climatic data. For all study types (fields, growth chamber or greenhouse), the environmental conditions that were measured should be described in detail.

### Considerations
* Did you collect the metadata for the identification of your plant material according to the recommendation provided in the [above section](#plant-biological-materials-metadata-collection-and-sharing)?
* Have you documented your phenotyping and environment assays (i.e. measurement or computation methodology based on the trait, method, scale triplet) both for direct measures (data collection) and computed data (after data processing or analysis)?
  * Is there an existing {% tool "crop-ontology" %} for the species you experiment and does it describe your assay? If not, have you described your data following the trait, method, and scale triplet? 
* Do you have your own system to collect data? Is it compliant with the {% tool "miappe" %} standard?
* Are you exchanging data with individual researchers?
  * In what media is data being collected?
  * Is the data described in a {% tool "miappe" %}-compliant manner?
* Are you exchanging data across different data management platforms?
  * Do these platforms implement the Breeding API {% tool "brapi" %} specification?
  * If not, are they MIAPPE-compliant? Do they enable automated data exchange?

### Solutions

#### Data exchange standards and ontologies
* The metadata standard applicable to plant phenotyping experiments is {% tool "miappe" %}.
  * The Plant biological materials section follows {% tool "multi-crop-passport-descriptor" %} described [above](#plant-biological-materials-metadata-collection-and-sharing).
  * The trait and phenotypes, including methods and protocols, are based on the {% tool "crop-ontology" %} recommendations.
  * Experiment type (e.g. greenhouse, field), location (geographical coordinates) and time enable linkage with geo-climatic data. 
  * Other sections include a description of investigations/dataset, studies, people involved, data files, environmental parameters, experimental factors, events.
  * It is implemented as an Excel template, as an ISA profile, in several databases and in the Breeding API ({% tool "brapi" %}).
  
* Tools and resources for data collection and management:
  * A simple [MIAPPE Excel template](https://github.com/MIAPPE/MIAPPE/tree/master/Templates) enables pragmatic and basic data exchange. See also {% tool "miappe-compliant-spreadsheet-template" %} to potentially enhance customised templates with ontology tools such as {% tool "rightfield" %} or {% tool "onotomaton" %}.
  * Submission using {% tool "miappe-compliant-spreadsheet-template" %} to databases such as {% tool "dataverse" %}, {% tool "zenodo" %} and {% tool "e-dal" %} is described in [Plant Phenomics](plant_pheno_assembly), which includes a detailled [step by step procedure](https://w3id.org/faircookbook/FCB083).
  * {% tool "fairdom-seek" %} is a free data management platform for which MIAPPE templates are available.
  * {% tool "dataverse" %} is a free data sharing platform where full datasets can be deposited with MIAPPE templates for complete description. It is used in several repositories such as {% tool "recherche-data-gouv" %}.
  * {% tool "e-dal" %} is a free data management platform for which MIAPPE templates are in development.
  * {% tool "isa-tools" %} also include a configuration for MIAPPE and can be used both for filling in metadata and for validating MIAPPE in ISA-Tab and ISA-JSON format.
  * Collaborative Open Plant Omics {% tool "copo" %} is a data management platform specific to the plant sciences.
  * {% tool "fairsharing" %} is a manually curated registry of reporting guidelines, vocabularies, identifier schemes, models, formats, repositories, knowledge bases, and data policies that includes many resources relevant for managing plant phenotyping data.
  * {% tool "isa-wizard" %} is a configurable web application providing a questionnaire-based form resulting in ISA output.


* For validation of MIAPPE datasets, see the [validation section](#validation-of-plant-phenotypic-and-genotypic-data).


* If you or your partners collect data into data management platforms:
  * If it implements BrAPI, you can exchange data using BrAPI calls.
  * If it doesn’t implement BrAPI, the simplest solution would be to export data into the MIAPPE spreadsheet template, or another formally defined data template.

* It is also recommended that you provide permanent access to a description of the project or study, that contains links to all the data, molecular or phenotypic (see [Data Publication](#Data-Publication))


## Genotyping: (meta)data collection and sharing

### Description
Here are described the mandatory, recommended and optional metadata fields for data interoperability and re-use, as well as for data deposition in {% tool "eva" %} (European Variation Archive), the EMBL-EBI's open-access genetic variation archive connected to {% tool "biosamples" %}, described [above](#plant-biological-materials-metadata-collection-and-sharing). In addition to sample and experiment metadata, the use of stable variant identifiers (RSids) issued by EVA is strongly recommended. RSids (Reference SNP cluster IDs) provide a persistent and globally recognised reference for each variable loci, ensuring long-term traceability and interoperability across datasets.

### Considerations
* Did you collect the metadata for the identification of your plant samples according to the recommendations provided in the [above section](#plant-biological-materials-metadata-collection-and-sharing)?
* Is the reference genome assembly available in an {% tool "international-nucleotide-sequence-database-collaboration" %} archive and has a Genome Collections Accession number, either GCA or GCF?
* Is the analytic approach used for creating the {% tool "vcf" %} file available in a publication and has a Digital Object Identifier (DOI)? 
* How do you plan to refer to the variants you will submit to the {% tool "eva" %} ?

### Solutions

#### Checklists, ontologies, file formats
Sharing plant genotyping data files involves the use of the Variant Call Format (VCF) standard. Findability and reusability of {% tool "vcf" %} files depend on the supplied metadata and, in particular, with MIAPPE-compliant biological material description: the [plant genomic and genetic variation data submission recipe](https://w3id.org/faircookbook/FCB061) helps you on that topic. While metadata standards like MIAPPE and MCPD are described in the phenotyping and biological materials sections, respectively, genomic data relies on a range of standardized file formats to ensure interoperability. Depending on your research, you will encounter several other common formats:
* **FASTA**: The most fundamental format for representing nucleotide or protein sequences. Each sequence entry begins with a single-line description starting with a `>` character, followed by lines of sequence data.
* {% tool "gff3" %}: A tab-delimited text file used to describe the functional features of a genome, such as genes, exons, and regulatory elements. It allows researchers to annotate a reference genome. GFF3 is a popular and more structured version of the format.
* {% tool "bed" %}: A concise and flexible format for defining genomic regions. It is commonly used to provide annotation tracks for display in genome browsers and is simpler than GFF, requiring only the chromosome, start position, and end position for each feature.
* {% tool "agp" %}: A file format used in genome assembly projects. It describes how larger sequences, like chromosomes, are constructed by ordering and orienting smaller sequence fragments (contigs or scaffolds).
* {% tool "hapmap" %}: A specific text-based format for storing genotypes from a population. It typically arranges single nucleotide polymorphisms (SNPs) in rows and individual samples in columns, making it well-suited for population genetics and genome-wide association studies (GWAS).


#### Data sharing
* Once the VCF file is ready with all necessary metadata, it can be submitted to {% tool "european-variation-archive" %}. You will find all necessary information on the submission steps on the [EVA submission page](https://www.ebi.ac.uk/eva/?Submit-Data).

#### Permanent identifers
* {% tool "eva" %} will issue a permanant identifier for each study (BioProject Accession, e.g. PRJEB...) and analysis (Analysis Accession, e.g. ERZ...) included in the submission. This permanant identifer can be used in publication to refer to the dataset.
* Each variant submitted to the EVA will receive RSids for consistent referencing and interoperability. RSids are unique, stable identifiers assigned by the European Variation Archive (EVA) that cluster identical genetic variants found at the same genomic location across multiple independent submissions. These can be used in publication or other database to higlight specific variant of interest.

* It is also recommended that you provide permanent access to a description of the project or study, that contains links to all the data, molecular or phenotypic (see [Data Publication](#Data-Publication))


## Validation of Plant Phenotypic and Genotypic Data

### Description
To ensure the integrity, quality, and interoperability of datasets in plant phenotyping and genotyping, implementing data and metadata standards is required. These standards provide a structured framework for consistent data collection, storage, and sharing. They not only define the expected format and structure of the data but also necessitate validation to confirm compliance with these specifications. Validation can be broadly categorised into two types: semantic and syntactic. Both types are essential for ensuring that data and metadata meet the necessary standards for effective use and integration.

### Considerations


* **Syntactic Validation**: This type of validation focuses on the structure and format of the data. It checks whether the data adheres to predefined rules regarding:
    * **Data Types**: Ensuring that fields contain the correct types of data (e.g. numerical, textual).
    * **Field Completeness**: Verifying that all mandatory fields are filled and that optional fields are populated appropriately.
    * **Consistency**: Checking for uniformity in data entries, such as consistent naming conventions and units of measurement.

    Syntactic validation is often automated and can be performed using software tools that analyse the data against the defined schema, making it efficient and reliable.
    
* **Semantic Validation**: This assesses the meaning and context of the data. It ensures that the data is meaningful within the context of the research and is used in accordance with its intended purpose. Key aspects include:
    * **Logical Consistency**: Verifying that relationships between different data elements are logical and coherent.
    * **Domain Constraints**: Ensuring that data values fall within acceptable ranges or categories relevant to the study.
    * **Contextual Relevance**: Assessing whether the metadata accurately describes the dataset and provides sufficient context for future users.

    Semantic validation often requires human supervision and domain expertise, as it involves interpreting the meaning and relevance of the data.


### Solutions
To improve data and metadata validation in plant phenotyping and genotyping, several effective solutions can be implemented:
* **Adoption of Standardised Protocols**: Utilising established data and metadata standards, such as the Minimum Information About a Plant Phenotyping Experiment {% tool "miappe" %}, can streamline the validation process.
* **Automated Validation Tools**: Implementing software tools designed for both syntactic and semantic validation can significantly improve the efficiency and accuracy of the validation process. These tools can automatically check data against predefined schemas, flagging errors and inconsistencies, which reduces the likelihood of manual errors.
* **Training and Capacity Building**: Providing training for researchers and data managers on the importance of data validation and the use of (meta)data standards is needed. Workshops, online courses, and resources can equip personnel with the necessary skills to effectively implement validation practices, fostering a culture of quality in data management. MIAPPE proposes several [training materials](https://www.miappe.org/trainings/) and recorded webinar that can be freely reused.


## Packaging and contextualizing data for reuse
Beyond collecting metadata, it is important to package your data, code, and experimental descriptions together in a standardised way. This ensures that others can easily understand and reuse your work. Key concepts for this are the {% tool "isa-tools" %}, {% tool "research-object-crate" %}, and {% tool "arc" %}.

* **The ISA Model**: The Investigation, Study, and Assay (ISA) model is a hierarchical framework for structuring and describing the metadata of a scientific experiment. It organises your project into three levels:
    * **Investigation**: The overall project or research goal.
    * **Study**: A specific experiment within the investigation (e.g. a greenhouse trial). It describes the biological material, experimental factors, and protocols used.
    * **Assay**: A specific analysis performed on the material from a study (e.g. mass spectrometry, phenotyping measurements, or a sequencing run).
    * The {% tool "isa-tools" %} are built to help you create metadata that follows this model, and it is the structural backbone for platforms like {% tool "fairdom-seek" %}.
* **Research Object Crate (RO-Crate)**: {% tool "research-object-crate" %} is a community standard for packaging all your research outputs into a single, FAIR-compliant bundle. Think of it as a "zip file for science" that contains not just your data, but also rich, machine-readable metadata describing the contents, contributors, methods, and publications. An RO-Crate can contain an ARC/ISA structure, making your entire research project easier to share, publish, and understand. Platforms like {% tool "fairdom-seek" %} can export projects as RO-Crates, simplifying the process of archiving a complete, reproducible research package.
* **Annotated Research Context (ARC)**: An {% tool "arc" %} is a practical implementation and extension of the ISA model. It is a container that bundles all the ISA metadata files together with the associated data files, protocols, and other relevant documents. The ARC provides a complete and self-contained "map" of your experiment, making it clear how all components are connected. It introduces two further layers to the ISA model namely:
    * **Workflows**: Workflows cover all computational steps of a study and contain application code, scripts, or any other executable description of an analysis ensuring highest flexibility for the scientists. To ensure persistence and reproducibility, these workflows comprise their own containerized running environment. 
    * **Runs**: The resulting data (runs) is linked to the workflows by a minimal Common Workflow Language (CWL) file specifying the input and output of the process.

## Research Data Publication

Beside sharing standardized data using established repositories such as [EVA](https://www.ebi.ac.uk/eva) or [BioSamples](https://www.ebi.ac.uk/biosamples/), it is highly recommended to provide persistent access to the project or study description, that contains links to all the data, molecular or phenotypic. Several generic databases handling plant research data are recommended for this purpose, including:
  * {% tool "recherche-data-gouv" %}
  * {% tool "e-dal" %}
  * {% tool "zenodo" %}
  * {% tool "biostudies" %}
  * {% tool "fairdomhub" %}

Especially for data deposition of phenotypic data, it is highly recommended that you opt for one of the repositories that either support MIAPPE Templates deposition ({% tool "dataverse" %}, {% tool "zenodo" %}, {% tool "e-dal" %}) or that implement {% tool "brapi-compatible-server" %}, as they enhance findability through the ELIXIR plant data discovery service, FAIR Data-finder for Agronomic Research ({% tool "faidare" %}), enable machine actionable access to MIAPPE compliant data and validation of that compliance.

The [Plant Phenomics Assembly](https://rdmkit.elixir-europe.org/plant_phenomics_assembly) provide a more detailed overview as well as further information about the requirement and different submission procedures for the mentioned databases and repositories.
