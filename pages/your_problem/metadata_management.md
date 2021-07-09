---
title: Documentation and metadata
contributors: [Flora D'Anna, Marco Carraro, Yvonne Kallberg, Markus Englund, Marco Roos, Korbinian Bösl, Rob Hooft]
tags: [collect, preserve, share, researcher, data manager]
description: how to document and describe your data.
page_tag: metadata
---

## How can you document data during the project?
 
### Description
Data documentation could be defined as the clear description of everything that a new “data user” or “your future-self” would need to know in order to find, understand, reproduce and reuse your data, independently. Data documentation should clearly describe how you generated or used the data, why, and where to find the related files. It could be used also as onboarding documentation for new colleagues, even if the responsible researcher leaves the project.
 
Due to the large variety of experiments, techniques and collaborative studies that usually occur within the same project, it is challenging to keep good documentation. However, lack of good data documentation often leads to data loss, not reproducible results and therefore, waste of money and time for scientists. Here we provide best practices and guidelines to help you properly document your data.
 
### Considerations
* Write the documentation in such a way that someone else who is known to the field can not mis-interpret any of the data, even if they tried.

* It is best practice to use one appropriate tool or an integration of multiple tools (also called tool assembly or ecosystem) for data documentation during a project. Suitable tools for data documentation are Electronic Lab Notebooks (ELNs), Electronic Data Capture (EDC) systems, Laboratory Information Management Systems (LIMS). Moreover, online platforms for collaborative research and file sharing services (such as OSF) could also be used as ELN or data management systems. Check with your institute to know what is offered.

* Independently of the tools you will use, data documentation is needed at two levels: documentation about the entire study or project and documentation about individual records, observations or data points.
  * Study-level documentation describes the project title and summary, study aims, authors, institutions involved, funds, methods, licence and identifier for each dataset, folders structure, file naming conventions, versioning system, relation between files or tables and other general information. 
  * Data-level documentation provides information about individual records or data point, such as the meaning of each variable name, label, ID or type (numeric, string, regular expression, date, etc), units (i.e., cm, kg…), experimental factors, categories, controlled vocabulary or ontology terms accepted as values for each variable, missing values code and so on. An example could be a data file that contains a "sex" field: someone known to the field could try to misinterpret that from "external sex organs present at birth" to "chromosomal XX or XY" or "high or low testosterone level" or "social gender" or other. In order to avoid this, the way the assignment is made must be part of the documentation or of the data itself (controlled vocabulary).

* Both the study- and data-level documentation must be generated as early as possible in the research process and also maintained, in order to be accurate and complete

* Documentation is also required when publishing your data. General-purpose repositories usually require only study-level documentation, while discipline-specific repositories generally require both study-level and data-level documentation. Importantly, repositories often accept data and documentation in a very strict format: they can require a predefined set of attributes or fields (metadata scheme) to be filled, ontology terms to be used, specific data model (e.g., ISA model, MAGE-TAB) to be adopted. We recommend familiarizing yourself with  the requirements of the repositories that could be appropriate for publishing your data already at the beginning of the project, so that you can start documenting and formatting your data accordingly as early as possible.

* Make sure the documentation is kept close to the data, so that nobody will be exposed to the data without being able to find the documentation.
 
### Solutions
* There are many appropriate tools for data documentation during the project. Check with your institute to know what is offered.
  * Electronic Lab Notebooks (ELNs) are usually better for more disparate and unstructured information that requires flexibility. Researchers can use ELN in a personalized way and adapt it to document their every-day work.

  * Laboratory Information Management Systems (LIMS) typically follow pre-defined and highly structured experimental workflow. LIMS are used to document and track biological samples through the experimental processes and can support direct import of data from sources such as instruments.

  * Electronic Data Capture (EDC) systems are usually designated for collection of clinical trial data.

  * Online platforms for collaborative research and file sharing services, which integrate with several data management tools, could also be used for data documentation during the project. For instance, OSF.io has integrations with Mendeley, Dropbox, GitHub, Figshare etc.

  * There is a major area of overlap between the aforementioned tools for data documentation, so it is better to choose the tool(s) that best address your specific need. Some tools can be used at the same time to address different needs and they can be complementary. Comparative lists can help with the choice:
    * [Harvard Medical School – ELN Comparison Grid.](https://datamanagement.hms.harvard.edu/analyze/electronic-lab-notebooks)
    * [University of Cambridge - Electronic Research Notebook Products.](https://www.data.cam.ac.uk/data-management-guide/electronic-research-notebooks/electronic-research-notebook-products)

* Independently of the tools, you should agree on and establish a [data organisation](https://rdmkit.elixir-europe.org/data_organisation.html) system for files (or tables in a database) together with your team or [Data Management Working Group](https://rdmkit.elixir-europe.org/data_quality.html#how-do-you-ensure-the-quality-of-research-data): 
  * Folder structure
  * File naming convention
  * Versioning system

* The established data organization system has to be described in detail in the documentation, preferably in open and machine-readable formats (i.e., XML, JSON, CSV, RDF, HTML). The description of the data organization system has to be placed in the folder at the highest level (e.g. “Project” folder).

* [Study-level and data-level documentation](https://www.ukdataservice.ac.uk/manage-data/document/data-level.aspx) can be provided as
  * README file
  * [Codebook](https://ddialliance.org/training/getting-started-new-content/create-a-codebook)
  * Data dictionary ([see an example](https://webdav-r3lab.uni.lu/public/elixir/templates/Data_dictionary_example.xlsx))
  * Data list

  Each of these files can be made in several formats depending on the features available in your data documentation tool, your needs or skills. Machine readable formats (such as XML, JSON, CSV, RDF, HTML) are preferred to non-machine-readable ones (.txt, xls, pdf). Also non-proprietary formats are preferred over proprietary ones.

* Highly structured data documentation is called **metadata**. Generating metadata in **machine-readable format** makes your data more FAIR . Metadata provides structured and searchable information so that a user can find existing data, evaluate its reusability and cite it.

* It is good practice to use international standard metadata schemes to describe your data. A metadata schema is a fixed set of attributes (elements or fields) about the data that needs to be provided. Some attributes are mandatory, some are only recommended or optional. International standard metadata schemes are developed by and accepted as standards by communities. There are many standard metadata schemes, some generic, while others discipline-specific. See the paragraph about [how to find standard metadata schemes.](https://rdmkit.elixir-europe.org/metadata_management.html#how-do-you-find-appropriate-standard-metadata-for-datasets-or-samples)

* You can use the attributes of a metadata scheme in a format that is not machine readable (e.g., by copying the metadata fields in a README.txt file or in a Codebook.xls). However, using standard metadata schemes in a machine-readable format will increase the findability of your data.

* Metadata schemes usually rely on ontologies and controlled vocabularies, which make your data more reusable and interoperable. See the paragraph about [how to find ontologies and controlled vocabularies.](https://rdmkit.elixir-europe.org/metadata_management.html#how-do-you-find-appropriate-vocabularies-or-ontologies)

* We recommend familiarizing yourself with the requirements of the repositories that could be appropriate for publishing your data already at the beginning of the project, so that you can start documenting and formatting your data according to their requirements as early as possible.




## How do you find appropriate standard metadata for datasets or samples?

### Description

There are multiple standards for different types of data, ranging from generic dataset descriptions (e.g. DCAT, Dublin core, (bio)schema.org) to specific data types (e.g. MIABIS for biosamples). Therefore, *how to find standard metadata*, and *how to find an appropriate repository for depositing your data* become relevant questions.


### Considerations

* Decide at the beginning of the project what are the [recommended repositories](https://elixir-europe.org/platforms/data/elixir-deposition-databases) for your data types.
  * Note that you can use several repositories if you have different data types.
  * Distinguish between generic (e.g. Zenodo) and data type (technique) specific repositories (e.g. EBI repositories).


### Solutions

* If you have a repository in mind:
  * Go to the repository website and check the “help”, "guide" or “how to submit” tab to find information about required metadata.
  * On the repository website, go through the submission process (try to submit some dummy data) to identify metadata requirements. For instance, if you consider publishing your transcriptomic data in ArrayExpress, you can make your metadata spreadsheet by using [Annotare 2.0 submission tool](https://www.ebi.ac.uk/fg/annotare/), at the beginning of the project.
  * Be aware that data type specific repositories usually have check-lists for metadata. For example, the European Nucleotide Archive provides [sample checklists](https://www.ebi.ac.uk/ena/browser/checklists) that can also be downloaded as a spreadsheet after log in.

* If you don’t know yet what repository you will use, look for what is the recommended minimal information (i.e. “Minimum Information ...your topic”, e.g. [MIAME](http://fged.org/projects/miame/) or [MINSEQE](http://fged.org/projects/minseqe/) or [MIAPPE](https://www.miappe.org)) required for your type of data in your community, or other metadata, at the following resources:
  * [Research Data Alliance (RDA): Metadata Dictionary: Standards](https://rd-alliance.github.io/metadata-directory/standards/)
  * [FAIRsharing.org](https://fairsharing.org) at “Standards” and “Collections”
  * [The Digital Curation Centre (DCC): List of Metadata Standards](https://www.dcc.ac.uk/guidance/standards/metadata/list)


## How do you find appropriate vocabularies or ontologies?

### Description

Vocabularies and ontologies are meant for describing concepts and relationships within a knowledge domain. Used wisely, they can enable both humans and computers to understand your data. There is no clear-cut division between the terms "vocabulary" and "ontology", but the latter is more commonly used when dealing with complex (and perhaps more formal) collections of terms.

There are many vocabularies and ontologies to be found on the web. Finding a suitable one can be both difficult and time-consuming.


### Considerations

* Check whether you really need to find a suitable ontology or vocabulary yourself. Perhaps the repository where you are about to submit your data have recommendations? Or the journal where you plan to publish your results?
* Understand your goal with sharing data. Which formal requirements (by e.g. by funder or publisher) need to be fulfilled? Which parts of your data would benefit the most from adopting ontologies?
* Learn the basics about ontologies. This will be helpful when you search for terms in ontologies and want to understand how terms are related to one another.
* Accept that one ontology may not be sufficient to describe your data. It is very common that you have to combine terms from more than one ontology.
* Accept terms that are good enough. Sometimes you you cannot find a term that perfectly match what you want to express. Chosing the best available term is often better than not chosing a term at all. Note that the same concept may also be present in multiple ontologies.


### Solutions

* Define a list of terms that you want to find ontologies for. Include in the list also any alternative term names that you are aware of.
* Search for your listed terms on dedicated web portals. These are a few:
  * [Linked Open Vocabularies (LOV)](https://lov.linkeddata.es/dataset/lov/)
  * [EMBL-EBI Ontology Lookup Service](https://www.ebi.ac.uk/ols/index)
  * [Ontobee](http://www.ontobee.org)
  * [Schemapedia](https://schemapedia.com)

