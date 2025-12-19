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

Depositing (meta)data from multi-omics studies (e.g., genomics, transcriptomics, proteomics, metabolomics, imaging and complementary data types) while preserving cross-links is not straightforward but is essential. Data interlinking ensures that datasets placed in their appropriate technology- or domain-specific repositories remain connected and can be reused together. Here we provide brief recommendations to help make these links and improve the findability of related datasets across {% tool "elixir-deposition-databases-for-biomolecular-data" %}.

### Considerations

Before starting submitting (meta)data, consider the following.

* The interlinking process is not yet fully streamlined. It varies a lot depending on the data types and repositories. You must check the repository manual for detailed information.
* {% tool "biostudies" %} is used to register biological studies and link them to related datasets stored in other EMBL-EBI databases or external repositories. It can also hold data that does not fit into any of the structured EMBL-EBI archives. For more information, see the BioStudies manual.
* {% tool "biosamples" %} is the repository to register the biological entities and their specimens, and to describe their hierarchical relations and metadata. Begin by identifying the starting biological entity used in the study—such as each animal, individual, organism, or cohort—and clearly defining the relationships and hierarchy between the source or cohort and any derived specimens (e.g., blood draws, biopsies) or individuals used for specific assays. Examples:
  * ReCoDID: [Linked pathogen and host data across archives - a multi-omics, SARS-CoV-2 cohort case study, infectious diseases toolkit page](https://www.infectious-diseases-toolkit.org/showcase/linked-cohort-data#sharing-the-linked-emc-pilot-cohort-dataset)
  * HoloFood: doi: [10.1093/database/baae112](https://academic.oup.com/database/article/doi/10.1093/database/baae112/7951611)

  See BioSamples manual for details.
* Use the “External Reference” field to cross-link study or project entries across repositories by copying the project or study accession numbers between them. As best practice, use also {% tool "orcid" %}, Publication ID, {% tool "ror" %} for institutes etc.
* Note that the order in which you create entries in the different repositories may vary depending on how each repository handles sample information. Some repositories automatically generate BioSamples entries for you. In those cases, it can be easier to start your submission process with those repositories. The following repositories will create BioSamples ID automatically:
  * {% tool "european-nucleotide-archive" %}
  * {% tool "the-european-genome-phenome-archive" %}
  * {% tool "european-variation-archive" %}
  * {% tool "arrayexpress" %}
* To achieve maximum granularity in sample interlinking, use sample accession numbers across repositories whenever possible. However, note that sample-level linking varies, may require manual steps, and not all repositories assign accession numbers to every sample, leaving sample names as the only option for referencing.
  * If technology-specific repositories do not explicitly support BioSamples accession numbers or identifiers, simply include them as a metadata attribute. See [example of HoloFood in MetaboLights](https://www.ebi.ac.uk/metabolights/editor/MTBLS4382/samples), or the [example in the BioImage Archive](https://www.ebi.ac.uk/biostudies/BioImages/studies/S-BIAD2258) where the BioSamples IDs are added in the Data Files table.

Check documentation of the specific repository for more details.


### Solutions

Here we provide recommended steps for creating links and references to help users gain an overview of which samples were used across the various modalities and analyses.
* Start by creating {% tool "biosamples" %} entries, if the technology-specific repositories don't do it for you: register parent samples and sub-samples (e.g. cohort-individual, individual-specimens, etc).
  * To make your samples findable in BioSamples using your project name, add your project title as an attribute to all your samples (at least the parent samples). Name the attribute “**Project**”. [See sample from the HoloFood project](https://www.ebi.ac.uk/biosamples/samples/SAMEA112369763).
* A way to group all samples from your study under an overarching entry is to create a {% tool "biostudies" %} entry describing your multi-omics study.
  * Link BioSamples entries (e.g. parent samples) through the Linked Information (Link) section. [See the BioStudies example](https://www.ebi.ac.uk/biostudies/studies/S-SUBS5).
  * Provide the required details about your project, funding, and any associated publications. Make sure to use the exact same project name as in BioSamples to ensure consistency.
  * Submit your BioStudies entry to get the accession number.
* If feasible, add your BioStudies accession number as an external reference in the relevant BioSamples entries. This enables you and others to navigate from an entry in BioSamples to all related samples and study information in BioStudies.
* Submit technology-specific datasets to the appropriate technology-specific repositories.
  * Include BioSamples accessions either as the Sample Name or as an additional attribute called "**BioSamples accession**" as shown in the HoloFood example.
  * Use the same project title consistently across BioStudies, BioSamples, and the repository metadata.
  * If applicable, add your BioStudies accession number as an external reference in the technology-specific repository.
  * Finally, in each technology-specific repository entry, add the study or project accession numbers from all the other technology-specific submissions as external references, so the datasets are cross-linked.
* After completing submissions to other repositories, and if feasible, add the study or project accession numbers from each technology-specific repository as external references in the corresponding BioSamples child entries. This shows **exactly which data types and omics technologies are linked to each sample**.
* If applicable, once you have gathered all study or project accession numbers, return to your BioStudies entry and add them under Linked Information. This informs BioStudies users that **some samples in the dataset were processed with multiple omics, although it doesn't specify which**.
* Optionally, after all submissions are complete, you can improve human readability by updating your BioStudies entry with a README file describing how the data are interlinked, along with any supplementary files.

{% include image.html file="data_interlinking_figure.svg" alt="Overview of cross-modal sample linking in ELIXIR Deposition Databases." caption="**Figure 1: Overview of cross-modal sample linking in ELIXIR Deposition Databases.** 

This figure illustrates which links and references can be made across ELIXIR Deposition Databases to help researchers understand which samples were used across different omics modalities. (1) BioSamples accession numbers should be included as metadata in technology-specific datasets. (2) BioStudies can serve as an overarching entry point for a multi-omics study by listing BioSamples accession numbers and referencing other repositories. (3) Repository-specific study or project accession numbers should be cross-referenced between repositories." %}


## How do you search for multi-omics datasets across repositories?
 
### Description
Finding multi-omics datasets across repositories can be tricky unless starting from publications or reports that describe all links.

### Considerations

{% tool "omicsdi" %} aggregates datasets from multiple omics archives and can be used as a starting point to identify and connect paired multi-omics datasets across resources.
* OmicsDI provides a central entry point, but combining datasets may still require some extra effort.
* OmicsDI provides provenance-based grouping links datasets at the publication level, not individual samples.
* The multi-omics facet may miss links because not all repositories expose their datasets to OmicsDI.

### Solutions

For {% tool "omicsdi" %}
* Use OmicsDI to locate datasets and check repository metadata.
* Verify sample-level connections in the original repositories for precise integration.
