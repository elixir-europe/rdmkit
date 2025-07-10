---
title: Documentation and metadata
contributors: [Flora D'Anna, Marco Carraro, Yvonne Kallberg, Markus Englund, Marco Roos, Korbinian Bösl, Rob Hooft, Elin Kronander, Marina Popleteeva, Gil Poiares-Oliveira]
description: How to document and describe your data.
page_id: metadata
related_pages:
  tool_assembly: [nels, transmed, plant_geno_assembly, marine_assembly]
dsw:
- name: Will the metadata be available even when the data no longer exists?
  uuid: 3b3fbcc6-c405-4151-8dce-e11dbd46b1bd
- name: How will you be collecting and keeping your metadata?
  uuid: 8c962e6f-17ee-4b22-8ebb-9f06f779e3b3
faircookbook:
- name: Introducing terminologies and ontologies
  url: https://w3id.org/faircookbook/FCB019
- name: Creating a data/variable dictionary
  url: https://w3id.org/faircookbook/FCB025
- name: Creating a metadata profile
  url: https://w3id.org/faircookbook/FCB026
- name: Introducing Search Engine Optimization (SEO)
  url: https://w3id.org/faircookbook/FCB010
- name: Selecting terminologies and ontologies
  url: https://w3id.org/faircookbook/FCB020
- name: Requesting new terms from terminologies and ontologies
  url: https://w3id.org/faircookbook/FCB021
- name: Introducing ontology-related tools and services
  url: https://w3id.org/faircookbook/FCB022
---

## How can you document data during the project?

### Description
Data documentation could be defined as the clear description of everything that a new “data user” or “your future-self” would need to know in order to find, understand, reproduce and reuse your data, independently. Data documentation should clearly describe how you generated or used the data, why, and where to find the related files. It could be used also as onboarding documentation for new colleagues, even if the responsible researcher leaves the project.

Due to the large variety of experiments, techniques and collaborative studies that usually occur within the same project, it is challenging to keep good documentation. However, lack of good data documentation often leads to data loss, not reproducible results and therefore, waste of money and time for scientists. Here we provide best practices and guidelines to help you properly document your data.

### Considerations
* Write the documentation in such a way that someone else who is known to the field cannot misinterpret any of the data.

* It is best practice to use one appropriate tool or an integration of multiple tools (also called tool assembly or ecosystem) for data documentation during a project. Suitable tools for data documentation are Electronic Lab Notebooks (ELNs), Electronic Data Capture (EDC) systems, Laboratory Information Management Systems (LIMS). Moreover, online platforms for collaborative research and file sharing services (such as {% tool "openscienceframework" %}) could also be used as ELN or data management systems. Check with your institute or other relevant infrastructures to know what is offered.

* Independently of the tools you will use, data documentation is needed at two levels: documentation about the entire study or project and documentation about individual records, observations or data points.
  * Study-level documentation describes the project title and summary, study aims, authors, institutions involved, funds, methods, licence and identifier for each dataset, folders structure, file naming conventions, versioning system, relation between files or tables and other general information.
  * Data-level documentation provides information about individual records or data point, such as the meaning of each variable name, label, ID or type (numeric, string, regular expression, date, etc.), units (i.e., cm, kg…), experimental factors, categories, controlled vocabulary or ontology terms accepted as values for each variable, missing values code and so on. An example could be a data file that contains a "sex" field: someone known to the field could try to misinterpret that from "external sex organs present at birth" to "chromosomal XX or XY" or "high or low testosterone level" or "social gender" or other. In order to avoid this, the way the assignment is made must be part of the documentation or of the data itself (controlled vocabulary).

* Both the study- and data-level documentation must be generated as early as possible in the research process and also maintained, in order to be accurate and complete

* Documentation is also required when publishing your data. General-purpose repositories usually require only study-level documentation, while discipline-specific repositories generally require both study-level and data-level documentation. Importantly, repositories often accept data and documentation in a very strict format: they can require a predefined set of attributes or fields (metadata checklists) to be filled, ontology terms to be used, specific (meta)data schemas (e.g., ISA model, MAGE-TAB) to be adopted. We recommend familiarising yourself with  the requirements of the repositories that could be appropriate for publishing your data already at the beginning of the project, so that you can start documenting and formatting your data accordingly as early as possible.

* Make sure the documentation is kept close to the data, so that nobody will be exposed to the data without being able to find the documentation.

### Solutions
* There are many appropriate tools for data documentation during the project. Check with your institute to know what is offered.
  * Electronic Lab Notebooks (ELNs) are usually better for more disparate and unstructured information that requires flexibility. Researchers can use an ELN (such as {% tool "elabftw" %}) in a personalised way and adapt it to document their everyday work.

  * Laboratory Information Management Systems (LIMS) typically follow pre-defined and highly structured experimental workflow. LIMS are used to document and track biological samples through the experimental processes and can support direct import of data from sources such as instruments.

  * Electronic Data Capture (EDC) systems are usually designated for collection of clinical trial data.

  * Online platforms for collaborative research and file sharing services, which integrate with several data management tools, could also be used for data documentation during the project. For instance, {% tool "openscienceframework" %} has integrations with Mendeley, {% tool "dropbox" %}, {% tool "github" %}, {% tool "figshare" %}, etc.

  * There is a major area of overlap between the aforementioned tools for data documentation, so it is better to choose the tool(s) that best address your specific need. Some tools can be used at the same time to address different needs and they can be complementary. Comparative lists and tools can help with the choice:
    * {% tool "harvard-medical-school-electronic-lab-notebooks" %}
    * {% tool "university-of-cambridge-electronic-research-notebook-products" %}
    * {% tool "publisso" %} - Documenting research data: Electronic Lab(oratory) Notebooks
    * {% tool "eln-finder" %}

* Independently of the tools, you should agree on and establish a [data organisation](data_organisation) system for files (or tables in a database) together with your team or [Data Management Working Group](data_quality#how-do-you-ensure-the-quality-of-research-data):
  * Folder structure
  * File naming convention
  * Versioning system

* The established data organisation system has to be described in detail in the documentation, preferably in open and machine-readable formats (i.e., XML, JSON, CSV, RDF, HTML). The description of the data organisation system has to be placed in the folder at the highest level (e.g. “Project” folder).

* [Study-level](https://ukdataservice.ac.uk/learning-hub/research-data-management/document-your-data/study-level-documentation/) and [data-level](https://ukdataservice.ac.uk/learning-hub/research-data-management/document-your-data/data-level/) documentation can be provided as
  * README file
  * {% tool "create-a-codebook" %}
<<<<<<< metadata-link
  * Data dictionary
=======
  * Data dictionary ([see an example](https://webdav.lcsb.uni.lu/public/elixir/templates/Data_dictionary_example.xlsx))
>>>>>>> master
  * Data list

  Each of these files can be made in several formats depending on the features available in your data documentation tool, your needs or skills. Machine-readable or -actionable formats (such as .xml, .json, .csv, .rdf) are preferred to non-machine-readable ones (.txt, .xls, .pdf).  README.txt is an exception since its main purpose is to be human-readable, i.e. not intended to be machine-readable or -actionable.
  Also non-proprietary formats are preferred over proprietary ones.

* Highly structured data documentation is called **metadata**. Generating metadata in a machine-readable or -actionable format makes your data more FAIR . Metadata provides structured and searchable information so that a user can find existing data, evaluate its reusability and cite it.

* It is good practice to use international standard metadata schemas to organise and store your (meta)data in a structured way. A metadata schema describes the relations, such as hierarchy, of the elements that belong to the structure. It is also good practice to use international standard metadata checklists to describe the content your (meta)data. A (meta)data checklist is a fixed set of attributes about the data that needs to be provided. Some attributes are mandatory, some are only recommended or optional. International standard metadata schemas and checklists are developed by and accepted as standards by communities. There are many standard metadata schemas and checklists, some generic, while others discipline-specific. See the paragraph about [how to find standard metadata.](metadata_management#how-do-you-find-appropriate-standard-metadata-for-datasets-or-samples)

* You can use the attributes of metadata schemas and checklists in a format that is not machine-readable or -actionable (e.g., by copying the metadata fields in a Codebook.xls). However, using standard metadata in a machine-readable or -actionable format will increase the findability of your data.

* Metadata schemas and checklists usually rely on ontologies and controlled vocabularies, which make your data more reusable and interoperable. See the paragraph about [how to find ontologies and controlled vocabularies.](metadata_management#how-do-you-find-appropriate-vocabularies-or-ontologies)

* We recommend familiarising yourself with the requirements of the repositories that could be appropriate for publishing your data already at the beginning of the project, so that you can start documenting and formatting your data according to their requirements as early as possible.

* Platforms for management of metadata and data used by some scientific communities: {% tool "cedar" %}, {% tool "semares" %}, {% tool "fairdom-seek" %}, {% tool "fairdomhub" %}, {% tool "copo" %}.




## How do you find appropriate standard metadata for datasets or samples?

### Description

There are multiple standards for different types of data, ranging from generic dataset descriptions (e.g. DCAT, Dublin core, (bio)schema.org) to specific data types (e.g. MIABIS for biosamples). Therefore, *how to find standard metadata*, and *how to find an appropriate repository for depositing your data* are relevant questions.


### Considerations

* Decide at the beginning of the project what are the {% tool "elixir-deposition-databases-for-biomolecular-data" %} for your data types.
  * Note that you can use several repositories if you have different data types.
  * Distinguish between generic (e.g. Zenodo) and data type (technique) specific repositories (e.g. EBI repositories).


### Solutions

* If you have a repository in mind:
  * Go to the repository website and check the “help”, "guide" or “how to submit” tab to find information about required metadata.
  * On the repository website, go through the submission process (try to submit some dummy data) to identify metadata requirements. For instance, if you consider publishing your transcriptomic data in ArrayExpress, you can make your metadata spreadsheet by using [Annotare 2.0 submission tool](https://www.ebi.ac.uk/fg/annotare/), at the beginning of the project.
  * Be aware that data type specific repositories usually have check-lists for metadata. For example, the European Nucleotide Archive provides [sample checklists](https://www.ebi.ac.uk/ena/browser/checklists) that can also be downloaded as a spreadsheet after log in.

* If you do not know yet what repository you will use, look for what is the recommended minimal information (i.e. “Minimum Information about your topic”, e.g. {%tool "miame" %}, {%tool "minseqe" %}, or {% tool "miappe" %}) required for your type of data in your community, or other metadata, at the following resources:
  * {% tool "min-info-standards" %}
  * {% tool "rda-standards" %}
  * {% tool "fairsharing" %} at “Standards” and “Collections”
  * {% tool "data-curation-centre-metadata-list" %}


## How do you find appropriate vocabularies or ontologies?

### Description

Vocabularies and ontologies are describe concepts and relationships within a knowledge domain. Used wisely, they can enable both humans and computers to understand your data. There is no clear-cut division between the terms "vocabulary" and "ontology", but the latter is more commonly used when dealing with complex (and perhaps more formal) collections of terms and relationships. Ontologies typically provide an identifier.

There are many vocabularies and ontologies available on the web. Finding a suitable one can be difficult and time-consuming.


### Considerations

* Check whether you really need to find a suitable ontology or vocabulary yourself. Perhaps the repository where you are about to submit your data have recommendations? Or the journal where you plan to publish your results?
* Understand your goal with sharing data. Which formal requirements (by e.g. by funder or publisher) need to be fulfilled? Which parts of your data would benefit the most from adopting ontologies?
* Learn the basics about ontologies. This will be helpful when you search for terms in ontologies and want to understand how terms are related to one another.
* Accept that one ontology may not be sufficient to describe your data. It is very common that you have to combine terms from more than one ontology.
* Accept terms that are good enough. Sometimes you you cannot find a term that perfectly match what you want to express. Choosing the best available term is often better than not choosing a term at all. Note that the same concept may also be present in multiple ontologies.


### Solutions

* Define a list of terms that you want to find ontologies for. Include in the list also any alternative term names that you are aware of.
* Search for your listed terms on dedicated web portals. These are a few:
  * {% tool "linked-open-vocabularies" %}
  * {% tool "ontology-lookup-service" %}
  * {% tool "ontobee" %}
  * {% tool "bioportal" %}
  * {% tool "agroportal" %}
  * {% tool "the-open-biological-and-biomedical-ontology-foundry" %}
  * {% tool "evidence-and-conclusion-ontology" %}

## What do you write in a README file?

### Description

A README file is typically a text file written in text (.txt) or markdown (.md) format. The content could either be on study-level or data-level. This is a file for a potential user of your data, including yourself, it is not meant to be machine-actionable.

### Considerations

* README file can be updated with time to include information which was not available before. It is a good practice to create a first version when starting a new project.
* For complex projects, consider to write README files on several levels, not only in the top level of the project.

### Solutions 

Below you will find examples of README files for study-level and data-level. For more information you might want to check [documentation page](https://rdm.elixir-belgium.org/data_documentation#readme-file) from ELIXIR Belgium node.

#### Study/project level README

    This README file was generated on [YYYY-MM-DD] by [NAME]

    GENERAL INFORMATION
    - Study/project title:
    - Description: <provide a short description of the study/project>
    - Principle Investigator:
    - Link to Data management plan

    ORGANIZATION
    - Folder structure: similar to folder structure example above (below)
    - File naming conventions (with examples) <unless your project is big and you have README files in every subfolder with this information provided there>
    - File formats: <Provide a list of all file formats present in this study/project>


#### Data level README 

    This README file was generated on [YYYY-MM-DD] by [NAME]

    GENERAL INFORMATION
    - Dataset title:
    - Description: <provide description of the dataset origin, steps used in its generation, content and its purpose>

    ORGANIZATION
    - Folder structure: similar to folder structure example above (below)
    - File naming conventions: <provide explanation of the elements used, allowed values and examples> 
    - File formats: <Provide a list of all file formats present in this dataset>

    DATA COLLECTION
    - Institutional catalog ID (if applicable):
    - Date of data collection: <provide single date, range, or approximate date; suggested format YYYY-MM-DD>
    - Link to electronic lab book (codebook) where the following is described (if it does not exist, include it here):
      - Methods used for data collection (including references, documentation (e.g. consent form template), links):
      - Geographic location of collection (if applicable):
      - Experimental & environmental conditions of collection (if applicable):
      - Standards and calibration for data collection (if applicable):
      - Uncertainty, precision and accuracy of measurements (if applicable):
      - Known problems & caveats (sampling, blanks, etc.):
      - Codes or symbols used to record missing data with description (if applicable):
    - Link to data dictionary:

    DATA RE-USE
    - DOI/accession number (if dataset is published): 
    - License (if any):
    - Use restrictions (if any):
    - Recommended citation for the data (if any):
