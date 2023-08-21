---
title: Existing data
contributors: [Rob Hooft, Flora D'Anna, Pinar Alper, Yvonne Kallberg, Karel Berka, Marko Vidak, Olivier Collin, Ulrike Wittig]
page_id: existing_data
related_pages:
    tool_assembly: []
description: How to find and reuse existing data.
dsw:
- name: Is there any pre-existing data?
  uuid: efc80cc8-8318-4f8c-acb7-dc1c60e491c1
faircookbook:
- name: Licensing
  url: https://w3id.org/faircookbook/FCB032
---

## How can you find existing data?

### Description
Many datasets could exist that you can reuse for your project. Even if you know the literature very well, you can not assume that you know everything that is available. Datasets that you should be looking for can either be collected for the same purpose in another earlier project, but it could also have been collected for a completely different purpose and still serve your goals.

### Considerations
* Creation of scientific data can be a costly process. For a research project to receive funding one needs to justify, in the project’s data management plan, the need for data creation and why reuse is not possible. Therefore it is advised to always check first if there exists suitable data to reuse for your project.

* When the outputs of a project are to be published, the methodology of selecting a source dataset will be subjected to peer review. Following community best practice for data discovery and documenting your method will help you later in reviews.

* List the characteristics of the datasets you are looking for, e.g. format, availability, coverage, etc. This enables you to formulate the search terms. Please see [Gregory K. et al. Eleven quick tips for finding research data. PLoS Comput Biol 14(4): e1006038 (2018)](https://doi.org/10.1371/journal.pcbi.1006038) for more information.


### Solutions
* Locate the repositories relevant for your field.
    * Check the bibliography on relevant publications, and check where the authors of those papers have stored their data. Note those repositories. If papers don’t provide data, contact the authors.
    * Data papers provide peer-reviewed descriptions of publicly available datasets or databases and link to the data source in repositories. Data papers can be published in dedicated journals, such as [Scientific Data](https://www.nature.com/sdata/), or be a specific article type in conventional journals.
    * Search for research communities in the field, and find out whether they have policies for data submission that mention data repositories. For instance, [ELIXIR communities in Life Sciences](https://elixir-europe.org/communities).

* Locate the primary journals in the field, and find out what data repositories they endorse.
    * Journal websites will have a “Submitter Guide”, where you’ll find lists of recommended deposition databases per discipline, or generalist repositories. For instance, {% tool "scientific-data-s-recommended-repositories" %}.
    * You can also find the databases supported by a journal through the policy interface of {% tool "fairsharing" %}.

* Search registries for suitable data repositories.
    * {% tool "fairsharing" %} is an ELIXIR resource listing repositories.
    * {% tool "re3data" %} lists repositories from all fields of science.
    * {% tool "google-dataset-search" %} or {% tool "datacite" %} for localization of datasets.
    * The {% tool "omicsdi" %} provides a knowledge discovery framework across heterogeneous omics data (genomics, proteomics, transcriptomics and metabolomics).
    * The {% tool "elixir-core-data-resources" %} list of knowledge resources recommended by ELIXIR.
    * {% tool "openaire-explore" %} provides linked open research datasets.

* Search through all repositories you found to identify what you could use. Give priority to curated repositories.


## How can you reuse existing data?

### Description
When you find data of interest, you should first check if the quality is good and if you are allowed to use the data for your purpose. This process might be difficult, so you can find guidelines and tools below.

### Considerations
* Before reusing the data, make sure to check if a licence is attached and that it allows your intended use of the data.

* Check if metadata or documentation are provided with the data. Metadata and documentation should provide enough information for a correct interpretation and reuse of the data. The use of standard metadata schemas and ontologies increase reusability of the data.

* Quality of the data is of utmost importance. You should check whether there is a data curation process on the repository (automatic, manual, community). This information should be available on the repository’s website. Check if the repository provides a quality status of each dataset (e.g. star rating system or quality indicators).

* The data you choose to reuse may be versioned. Before you start to reuse it you should decide which version of the dataset you will use.

### Solutions
* Verify that the data is suitable for reuse.
    * Check the [licences](licensing) or repository policy for data usage.
    * Data from publications can generally be used but make sure that you cite the publication as reference.
    * If you cannot find the licence of the data, contact the authors. No licence means no reuse allowed.
    * If you are reusing personal (identifiable) or even sensitive data, some extra care needs to be taken (see [Human data](human_data) and [Sensitive data](sensitive_data) pages):
        * Make sure you select a data repository that has a clear, published data access/use policy. You do not want to be liable for improper reuse of personal information. For instance, if you’re downloading human data from some lab’s website make sure there is a statement/confirmation that the data was collected with ethical and legal considerations in place.  
        * Sensitive data is often shared under restrictions. Check in the description of the access conditions whether these match with your project (i.e. whether you would be able to successfully ask to get access to the data). For instance, certain datasets can only be accessed by projects with Ethics/Institutional Review Board approval or some can only be used within a specific research field.

* Verify the quality of the data. Some repositories have quality indicators, such as:
    * Star system indicating level of curation, e.g. for manually curated/non-curated entries.
    * {% tool "evidence-and-conclusion-ontology" %}.
    * Detailed quality assessment methods. For instance, PDB has several [structure quality assessment metrics](https://validate.wwpdb.org/).

* If metadata is available, check the quality of metadata. For instance, information about experimental setup, sample preparation, data analysis/processing can be necessary to reuse the data and reproduce the experiments.

* Decide which version (if present) of the data you will use.
    * You can decide to  always use the version that is available at the start of the project. You would do this if switching to the new versions would not be very beneficial to the project or it would require major changes. In this case, you need to make sure that you and others, who want to reproduce your results, can access the old version at a later stage too.
    * You can update to the latest versions if new ones come out during your project. You would do this if the new version does not require major changes in your project workflow, and/or if the updates could improve your project. In this case, consider that you may need to re-do all your calculations based on a new version of the dataset and make sure that everything stays consistent.
