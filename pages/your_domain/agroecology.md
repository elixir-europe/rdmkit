---
title: Agroecology
description: Data management solutions for agroecology life science research
contributors: [Niels Geudens, Flora D'Anna, Breza Witmond, Rafael Abbeloos]
editors: [Bert Droesbeke, Federico Bianchini]
page_id: agroecology
related_pages: 
  Your_tasks: [ metadata, data_quality, data_provenance, data_organisation, sensitive, gdpr_compliance, ethics ]
  Tool_assembly: []

fairsharing:
- name: AgroServ collection
  url: https://fairsharing.org/FAIRsharing.f397c2
tess: 
- name: Visualize Climate data with Panoply netCDF viewer
  url: https://tess.elixir-europe.org/materials/hands-on-for-visualize-climate-data-with-panoply-netcdf-viewer-tutorial
---

## Introduction

Agroecology is a transdisciplinary field that integrates principles from agriculture, ecology, and environmental sciences to study and promote sustainable farming systems. It focuses on the interactions between plants, soil, water, biodiversity, and climate, aiming to optimise agricultural productivity while enhancing ecosystem resilience and biodiversity conservation. In the context of modern challenges such as climate change, soil degradation, and biodiversity loss, agroecology aims to research solutions that prioritise ecological balance and resource efficiency.

Agroecological research generates diverse and complex datasets, spanning field observations, soil and plant analysis, remote sensing, genomic studies, and environmental monitoring. Effective Research Data Management (RDM) is essential to ensure that these datasets remain accessible, interoperable, and reusable, facilitating collaboration across disciplines and institutions.

This page focuses on RDM best practices for the life science aspects of agroecology and supports alignment with the FAIR principles (Findable, Accessible, Interoperable, Reusable). Given the breadth of agroecology, readers may also find relevant RDM guidance in existing RDMkit domain pages, in particular [Your Domain - Biodiversity](biodiversity) and [Your Domain - Plant Sciences](plants), which cover overlapping data types, standards, and workflows commonly encountered in agroecological research. Topics related to social and economic sciences are outside the scope of this page but are acknowledged as complementary aspects of agroecology research.

## Data collection
 
### Description

Agroecology studies often combine field observations, sensor measurements, remote sensing, laboratory analyses, and management records across multiple spatial and temporal scales (plot, farm, landscape; days, seasons, years). This leads to datasets that are heterogeneous, context-dependent, and sensitive to local conditions (soil, climate, practices). Robust data collection workflows are therefore essential to ensure that datasets remain comparable, reusable, and suitable for integration with external sources.

### Considerations 

- What do you need to define to ensure measurements are comparable across sites and time?
- Which information is essential to interpret observations in their local context?
- How will you represent spatial and temporal variability consistently?
- What quality assurance steps do you need to prevent or detect errors and inconsistencies during data capture?
- Are any data sensitive, and if so, what restrictions do you need to enable responsible reuse?

### Solutions
The following practices help you ensure agroecology data remain comparable across sites and reusable:
- Use standardised protocols and templates to harmonise sampling and field observations across teams and sites (e.g. by maintaining shared, versioned methods in protocols.io, or aligning practices with long-term monitoring initiatives such as [LTER protocols](https://lter.kbs.msu.edu/protocols)).
- Capture a minimum set of contextual information during collection so measurements remain interpretable later (e.g. where/when/how the observation was made).
- Maintain a simple field-level data dictionary (variables, units, and codes) to avoid inconsistencies between teams and seasons.
- Apply lightweight QA/QC during collection, for example calibration checks, validation rules, and clear missing-value conventions. More information is available at [Your task - Data Quality](data_quality).
- Keep traceability from raw to derived data, documenting transformations and any scripts or tools used.  More information is available at [Your task - Data Provenance](data_provenance).
- Use consistent naming and structures from the start to support later integration and reuse. More information is available at [Your task - Data Organisation](data_organisation).
- Handle sensitive information responsibly, separating identifying information where needed and documenting access conditions (e.g. precise farm locations or rare species occurrence locations).

## Metadata and data interoperability
### Description

In agroecological research, documenting data and ensuring data interoperability are essential for making data FAIR. However, achieving consistent and comprehensive documentation poses several challenges:
1.	Agroecological research involves a wide range of data types, including genomic sequences, phenotypic traits, geospatial data, and environmental observations. This diversity makes it difficult to apply a one-size-fits-all approach to metadata and data interoperability.
2.	Agroecology integrates data from life sciences, environmental science, and agronomy. The absence of standardised terminology and metadata practices across these disciplines can lead to inconsistencies.
3.	Inadequate metadata or inconsistent documentation can hinder the long-term usability of datasets, reducing their value for future research and reproducibility.

### Considerations

* What metadata standards are most relevant for the type of agroecological data you collect (e.g. genomic, environmental, geospatial)?
* How can you ensured consistent data documentation across multidisciplinary research teams?
* What controlled vocabularies and ontologies should you use to enhance data interoperability?
* Which data formats best support long-term preservation and reusability?

### Solutions

The following practices help improve interoperability and reuse of agro-ecology datasets across disciplines and infrastructures:
* Adopt community metadata standards where possible, selecting those that best match your data types and community expectations. For example, guidance on recommended standards and how they map to common agroecology data types is collected via the {% tool "agroserv" %}, which links out to discipline- and technology-specific best practices.
* Use controlled vocabularies and ontologies to standardise terminology, especially for describing environments, experimental conditions, traits, organisms, and management variables. This improves consistency within a project and makes it easier to integrate datasets across studies and infrastructures. Useful resources include:
  * {% tool "agroportal" %}: a curated portal for agronomy and related domains (e.g., plant sciences, nutrition, biodiversity), supporting ontology search, browsing, and semantic annotation.
  * {% tool "the-environment-ontology" %}: a widely used ontology for environmental and habitat descriptors, often used to harmonise site and environmental context.
  * {% tool "crop-ontology" %}: provides standardised trait and variable descriptions for crops, commonly used in plant breeding and phenotyping contexts.
  * {% tool "ontology-lookup-service" %}: a general-purpose service for searching and resolving terms across many biomedical and life science ontologies, useful when projects span multiple domains.
  * {% tool "agroserv" %}: the AgroServ FAIRsharing collection complements the ontology resources above by pointing to recommended community standards, and project-relevant guidance across life sciences and beyond.
* Keep identifiers consistent across datasets for sites, plots, samples, and observations, so that data from different sources can be reliably linked and integrated.
   * See also: [Your task - Identifiers](identifiers)
* Choose formats that support long-term reuse and integration, and document format choices early in the project (including version and conventions used).
   * {% tool "csv" %}: A simple, human-readable format for tabular data.
   * {% tool "netcdf" %}: A format suited for climate and environmental datasets, supporting multi-dimensional data structures. 
   * Use {% tool "isa-tab" %} format to describe complex field experiments and keep sample - measurement - datafile relationships clear across many sites, seasons, and analytical methods (soil chemistry, crop traits, biodiversity surveys, omics, remote sensing, etc.).
   * For a more detailed overview of appropriate formats, see [Your task - Data organisation](data_organisation).
* Make transformations and harmonisation steps explicit, especially when integrating multi-source data (field, lab, sensors, remote sensing), to support reproducibility and cross-study reuse. More information on this can be found in [Your task - Data Provenance](data_provenance).


## Data sharing and publishing
### Description

Agroecology datasets are often valuable beyond the original study, for example for meta-analyses, modelling, long-term monitoring, and synthesis across sites. However, publishing agroecology data can be challenging because datasets are heterogeneous, collected across multiple partners, and may include sensitive elements. Sharing data with appropriate documentation, licensing, and access conditions helps maximise reuse while supporting responsible data handling.

### Considerations
* What can you share openly, and what requires controlled access, aggregation, or other safeguards?
* Which repository or platform best fits the data type and community practices?
* What documentation doe you need so others can interpret your data outside its original context?
* How will you make datasets citable, with stable identifiers and clear attribution?
* Which licence and reuse conditions are appropriate for your intended audiences and stakeholders?

### Solutions
The following practices help agroecology datasets become discoverable, citable, and reusable:
* Publish data in a suitable repository or platform, prioritising disciplinary services where possible, and ensuring long-term availability. The following repositories and data networks provide open-access platforms that support collaboration, standardization, and FAIR data practices across multiple scientific domains:
   * {% tool "gbif" %}: GBIF is a biodiversity data repository, providing open access to species occurrence records, ecological datasets, and conservation-relevant information. By publishing and integrating biodiversity data in GBIF, researchers contribute to global biodiversity assessments and ecological research.
   * {% tool "agrodatacube" %}: This platform aggregates spatial agricultural datasets, combining open and derived data to support precision agriculture and agri-food applications. Researchers can use AgroDataCube to analyze spatial patterns in farming, climate interactions, and land use.
   * {% tool "agcros" %}: AgCROS fosters data collaboration in agriculture, allowing researchers to share, compare, and integrate datasets to enhance agricultural productivity, sustainability, and resilience. The platform supports open-access data integration across different agroecological domains.
   * {% tool "e-dal-pgp" %} (PGP): PGP provides specialised data hosting for plant genomics and phenomics research, ensuring that datasets on crop adaptation, resilience, and functional traits are findable and accessible for agricultural and environmental studies.
   * {% tool "crop-nutrient-data" %}: Crop Nutrient Data is a comprehensive database of field trial measurements on soil and crop nutrient concentrations. It enables researchers to explore, compare, and reuse standardized nutrient datasets across locations and crops, supporting improved nutrient management strategies and more sustainable agriculture practices.
   * [International Soil Data Network (ISRIC)](https://ismn.earth/en/): ISRIC provides global soil datasets, tools, and resources for soil information management and mapping. By using ISRIC’s data, researchers can study soil properties, fertility, and sustainability at a regional and global scale. 
   * {% tool "tape" %}: Developed by the Food and Agriculture Organization (FAO), TAPE is a structured framework to assess the multidimensional performance of agroecological systems. It is designed for researchers, practitioners, and policymakers to facilitate the adoption and scaling up of agroecological practices.
   * {% tool "faidare" %}: Developed by INRA-URGI, FAIDARE is a data portal that enables and increases dataset findability and accessibility in open international federations of information systems for research on plants. It uses BrAPI to access the individual repositories which is an implementation of MIAPPE. 
* Provide sufficient documentation for reuse, including methodology, context, variable definitions, and known limitations. More information is available at [Your Task - Documentation and metadata](metadata).
* Ensure datasets are citable, for example by assigning a persistent identifier (e.g. DOI) and providing a recommended citation. More information is available at [Your Task - Identifiers](identifiers).
* Choose a clear licence to remove ambiguity for reusers and to support responsible reuse. More information is available at [Your Task - Licensing](licensing).
* Manage sensitive data responsibly, especially where sharing could expose precise farm locations or commercially sensitive management records. More information is available at [Your Task - Data sentivity](sensitive), [Your Task - Ethical Aspects](ethics), [Your Task - GDPR compliance](gdpr_compliance) and [Your Task - Data Security](security).


