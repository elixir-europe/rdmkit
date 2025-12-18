---
title: Data interlinking
search_exclude: true
no_robots: true
sitemap: false
description: Best practices to interlink datasets from a multi-omics study deposited in technology-specific repositories.
contributors: [Flora D'Anna, Wolmar Nyberg Åkerström, Monique Zahn, Nadim Rahman, Vilem Ded, Marcos Casado Barbero, Ulrike Wittig, Teresa Zulueta-Coarasa, Christos Ouzounis, Silvia Rodríguez Mejías, Luana Licata, Espen Åberg, Niclas Jareborg, Yvonne Kallberg, Stephan Nylinder]
page_id: data_interlinking 
training:
  - name: EMBL-EBI Training
    url: https://www.ebi.ac.uk/training/search-results?query=data%20submission&domain=ebiweb_training&page=1&facets=
---

## How do you interlink data for multi-omics studies across ELIXIR deposition databases?
 
### Description

Depositing (meta)data from multi-omics studies (e.g., genomics, transcriptomics, proteomics, metabolomics, imaging and complementary data types) while preserving cross-links is not straightforward but is essential. Data interlinking ensures that datasets placed in their appropriate technology- or domain-specific repositories remain connected and can be reused together. Here we provide brief recommendations to help make these links and improve the findability of related datasets across ELIXIR Deposition Databases.

### Considerations

Before starting submitting (meta)data, consider the following.

* The interlinking process is not yet fully streamlined. It varies a lot depending on the data types and repositories. You must check the repository manual for detailed information.
* BioStudies is used to register biological studies and link them to related datasets stored in other EMBL-EBI databases or external repositories. It can also hold data that does not fit into any of the structured EMBL-EBI archives. For more information, see the BioStudies manual.
* BioSamples is the repository to register the biological entities and their specimens, and to describe their hierarchical relations and metadata. Begin by identifying the starting biological entity used in the study—such as each animal, individual, organism, or cohort—and clearly defining the relationships and hierarchy between the source or cohort and any derived specimens (e.g., blood draws, biopsies) or individuals used for specific assays. Examples:
  * ReCoDID: https://www.infectious-diseases-toolkit.org/showcase/linked-cohort-data#sharing-the-linked-emc-pilot-cohort-dataset.
  * HoloFood: doi: 10.1093/database/baae112.

  See BioSamples manual for details.
* Use the “External Reference” field to cross-link study or project entries across repositories by copying the project or study accession numbers between them. As best practice, use also ORCID ID, Publication ID, ROR for institutes etc.
* Note that the order in which you create entries in the different repositories may vary depending on how each repository handles sample information. Some repositories automatically generate BioSamples entries for you. In those cases, it can be easier to start your submission process with those repositories. The following repositories will create BioSamples ID automatically:
  * European Nucleotide Archive (ENA)
  * European Genome-phenome Archive (EGA)
  * European Variation Archive (EVA)
  * ArrayExpress
* To achieve maximum granularity in sample interlinking, use sample accession numbers across repositories whenever possible. However, note that sample-level linking varies, may require manual steps, and not all repositories assign accession numbers to every sample, leaving sample names as the only option for referencing.
  * If technology-specific repositories do not explicitly support BioSamples accession numbers or identifiers, simply include them as a metadata attribute. See example of HoloFood in MetaboLights https://www.ebi.ac.uk/metabolights/editor/MTBLS4382/samples, or this example in the BioImage Archive where the BioSamples IDs are added in the Data Files table: https://www.ebi.ac.uk/biostudies/BioImages/studies/S-BIAD2258.

Check documentation of the specific repository for more details.


### Solutions

By using [bullet point style](style_guide#text) as much as possible, try to describe when, why and for what is best to use a specific tool or resource. 
Avoid making long list of links to tools and resources.
Make sure to add the tools and resources mentioned in the text in the main "tools and resources" table.

* Bullet point solution 1
  * Sub-point
* Bullet point solution 2


## Concrete problem 2, formulated as a question <!-- example: where to find ontologies?-->
 
### Description <!-- do not delete this heading and write your text below it -->
Same as above

### Considerations <!-- do not delete this heading and write your text below it -->
Same as above

### Solutions <!-- do not delete this heading and write your text below it -->
Same as above
