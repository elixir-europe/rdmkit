---
title: Data brokering
search_exclude: true
contributors: [Aitana Lebrand, Parul Tewatia, Wolmar Nyberg Åkerström, Carla Cummins, Nils Peder Willassen, Nazeefa Fatima]
page_id: data brokering
related_pages: 
  tool_assembly:
training:
  - name: Training in TeSS
    registry: TeSS
    registry_url: https://tess.elixir-europe.org
    url: https://tess.elixir-europe.org/search?q=%22submission%22#materials
---

## Taking on the data broker role 
### Description
Sometimes it is challenging to exchange data across data producers, infrastructures and data sharing platforms. Some reasons can be that the data has to be pre-processed or enriched to comply with legal or organisational practices, that the data has to be translated to different data formats, or that transferring data requires expertise and access to special interfaces. By acting as a broker, you can fill this gap by negotiating a contract with data providers and/or recipients and doing the work required to make it convenient for them to exchange data.

![A flowchart displaying necessary steps required for data brokering, from producing data to sharing on behalf of others within a well defined ethical and legal framework.](/images/data_brokering_figure.svg){: height="300px" width="300px"}

Figure 1: **Data Brokering Workflow.** Individual data producers may process the data, store it, and submit it directly to international repositories or local public health authorities. In the data brokering model instead, several data producers (i.e. the data providers) submit their data to a common data recipient that might be charge of curating the data, analysing it with common pipelines, storing it and re-sharing parts of the data (as agreed with the data providers) to local health authorities and international repositories. The latter service is often referred to as “data brokering”, i.e. sharing data on behalf of others within a well defined ethical and legal framework. Icons attribution; Folder by mambu, Processing by ainul muttaqin, Database by Icons Bazaar, Personal Data by Silviu Ojog, Legal by Irvan Rhomadhani, and Validated File by Miguel Rocha - all icons are available at NounProject.com, and licensed under a [Creative Commons Attribution 3.0 Unported License](https://creativecommons.org/licenses/by/3.0/).

### Considerations
There are many aspects to consider when getting started as a broker.

* Decide how to interact with the data providers/recipients, such as to what extent you will be able to adapt your workflows to meet their needs/requirements. 
* Identify what kind of processing you will handle as a broker, such as (meta)data curation and validation, data masking/anonymisation, etc.
* Define the time frame for your commitment and your responsibilities for the data, such as how to handle data loss before delivery, what to do with the data after a successful delivery, how to manage changes to data that has already been delivered etc.
* Identify who is responsible for the data before, during and after delivery, such as the data controller/processor (according to GDPR) and/or intellectual property owner/licensee relationships between the provider and recipient
* Ensure that you will be able to establish contracts/agreements that cover the data and processing that you will handle, such as considerations for [data protection](data_protection), [licensing](licensing) and [compliance](compliance_monitoring).
* Estimate and secure the resources required to keep your commitment, such as staff with time and necessary skills, accounts, compute, storage and software
* Refer to the sections below for considerations related to collecting data from data providers and delivering data to public data repositories.


### Solutions

The solutions that you adopt will vary depending on the agreements you have negotiated with data providers and/or recipients. The following are examples of general solutions that would help you comply with regulations and implement good data management practices.
* [Data management plan](https://rdmkit.elixir-europe.org/data_management_plan.html) – Many questions that you would answer while writing a data management plan can be relevant to answer when you specify the terms of service for your brokering service, such as data storage, data standards, legal and ethical, etc. 
* [Data protection](https://rdmkit.elixir-europe.org/data_protection.html) – If you are working with data concerning people in the EU, you should make sure to comply with both national and international regulations for data protection.
* [Apply for brokering permissions](https://ena-docs.readthedocs.io/en/latest/faq/data_brokering.html) e.g. [ENA support/helpdesk](https://www.ebi.ac.uk/ena/browser/support) 


## Collecting and processing the metadata and data
### Description
Data brokering involves collecting data from various data providers (metadata and other data e.g. sequencing files), standardising and curating the data if needed, and then preparing the data for re-sharing e.g. in public international repositories. On the brokering platform, it is recommended that data be stored in a structured manner (e.g. in a relational database), using as much as possible controlled vocabularies and ontologies where they exist.

### Considerations
* [Data collection](https://rdmkit.elixir-europe.org/collecting) should be carefully prepared, notably to define the data model, the metadata and data that are needed for the envisioned applications, assess which fields should be compulsory or optional, follow controlled vocabularies or ontologies, and identify the nature of data (personal, sensitive data) and thereby the required level of security or data treatment (e.g. pseudonymised or anonymised data, ethical consent…).
  * Collection of *metadata* can be done in various ways, each having its advantages and disadvantages, notably in terms of user-friendliness, ease of processing and [data quality](https://rdmkit.elixir-europe.org/data_quality.html).
  * Collection of data files (e.g. sequencing data) should also involve minimal validation where possible (e.g. file extensions, regular checks of file sizes across the database to identify potential outliers with issues, integrity checks (checksum)…).

* Regular data checks should always be performed at the database level, to check unicity of identifiers where expected (e.g. sample identifier within a laboratory is expected to be unique) and identify potential incoherences in the data (e.g. division indicated in the name of a virus versus division indicated in the location field).
* Data brokers should also consider implementing a mechanism for metadata and data files update within their platform, and define mechanisms to pass on the updates to international repositories. Please consider that depending on the update mechanisms in place at the international repositories (e.g. API vs manual update via email), this process might become quite time-consuming.
* [Data transfer](https://rdmkit.elixir-europe.org/data_transfer.html) from the data providers to the data brokering platform will depend on the nature and volume of data. The volume might be larger if data providers can submit data in batches. 
* Clarify with the data providers how the data will be processed, in terms of data curation/cleaning and downstream [data analyses](https://rdmkit.elixir-europe.org/data_analysis.html). 
* [Data storage](https://rdmkit.elixir-europe.org/storage.html) needs should be carefully addressed; consider storing data in compressed formats and deleting intermediate files from analyses that could be recomputed if needed to gain storage space.

### Solutions
Collection of metadata can be done in various ways:

* Electronic forms (e.g. online form, eCRF) allow controlling data at the entry point, ensuring the use of controlled vocabularies and ontologies if properly set up. While user friendly for single uploads, this type of upload can become very cumbersome for batch upload.
* Spreadsheet files enable controlling data at the entry point, thanks to native validation features of spreadsheet tools (e.g Excel). It is at the same time very convenient for batch uploads and users generally like having a file that they can store and easily re-open to check what they have provided.
* Text files (TSV, CSV, JSON, XML…) are very practical to automate batch submissions on the user side, since scripts can easily generate these files. It is recommended to specify to the users which encoding should be used (e.g. UTF-8). There is however no data control at the entry point and only upon submission to the data brokering database. All data validation is therefore performed upon loading into the database, and error handling should be carefully evaluated prior to implementation. Examples include automatically informing the user of errors and asking them to re-submit, or involving data curators who may correct obvious mistakes and can be in contact with data providers to clarify data validation errors. Some automation may also be implemented to map terms to a controlled list of terms or an ontology even in the case of minor typos.

## Sharing data to public repositories
### Description
Often, a goal of the broker is to submit the collected and harmonised data in an open archive for the benefit of both the data owners and the wider scientific community. This supports sharing data with collaborators, referencing for publication and provides a [long-term storage solution](https://rdmkit.elixir-europe.org/storage.html).

### Example for genomic data
For sharing of sequencing data within Europe, the [European Nucleotide Archive](https://www.ebi.ac.uk/ena/browser/about) can be used. The ENA is part of the [INSDC](https://www.insdc.org/), a global collaboration for the archival of nucleotide sequence data including NCBI and DDBJ. For information on the structure of ENA content, please see here: https://www.ebi.ac.uk/ena/browser/about/content. A general guide to submissions to the ENA can be found here: https://ena-docs.readthedocs.io/en/latest/submit/general-guide.html

In the particular case of SARS-CoV-2 genomic data, more information will be available on the SARS-CoV-2 domain page (under construction, coming soon).

### Considerations
* There are many data repositories, so it is important to decide where you plan to share the data and adhere to the correct standards and submission protocols for your data type. This may notably include adhering to checklists provided by the chosen data repositories. See here for more information: https://rdmkit.elixir-europe.org/data_publication.html.
* If submitting to open access repositories, ensure clarity on which fields and data to share and, if these fields contain sensitive information, should they be anonymised/pseudonymised
  * metadata anonymisation:  [sensitive data](https://rdmkit.elixir-europe.org/sensitive_data.html), and [human data](https://rdmkit.elixir-europe.org/human_data.html)
  * Need to remove any human data (e.g. reads) prior to submission
* Submitted data may not be deleted, but may be suppressed from public view upon request
* Submitted records may be updated at a later date with new or amended metadata entries. However, it should be noted that upon creation of a new record, data is tagged for distribution and selected metadata fields are exchanged with other repositories. Redistribution of updated records is usually not triggered automatically, so updating records fully can be a time consuming and manual process.
* After data is submitted to a public repository, should the original copy of the data be retained at the central brokering platform and linked to its public counterpart? Or should it be removed and replaced with the ID of the public record?
* Within INSDC databases, data may be submitted and held privately for a period of time by setting a release date at time of submission: https://ena-docs.readthedocs.io/en/latest/faq/release.html
* By default, data submitted using default accounts are accredited to the submitting institute. However, broker accounts have the ability to credit different institutes with different records: https://ena-docs.readthedocs.io/en/latest/faq/data_brokering.html 

### Solutions
* There are many tools available to remove human reads from your non-human data, e.g. https://github.com/alakob/Metagen-FastQC-Docker 
* If submitting to ENA, please find the sample metadata checklist relating to your domain here: https://www.ebi.ac.uk/ena/browser/checklists 
* For information on updating assemblies, see here: https://ena-docs.readthedocs.io/en/latest/update/assembly.html#updating-assemblies
* For information on updating all other data types, see here: https://ena-docs.readthedocs.io/en/latest/submit/general-guide/programmatic.html#submission-xml-update-existing-objects
