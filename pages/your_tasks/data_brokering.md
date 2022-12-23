---
title: Data brokering
contributors: [Aitana Neves, Parul Tewatia, Wolmar Nyberg Åkerström, Carla Cummins, Nils Peder Willassen, Nazeefa Fatima]
description: Information on brokering data to data repositories on behalf of data producers.
page_id: data_brokering
training:
  - name: Training in TeSS
    registry: TeSS
    registry_url: https://tess.elixir-europe.org
    url: https://tess.elixir-europe.org/search?q=%22submission%22#materials
---

## Taking on the data broker role 
### Description
Sometimes it is challenging to exchange data across data producers, infrastructures and data sharing platforms. Some reasons can be that the data has to be pre-processed or enriched to comply with legal or organisational practices, that the data has to be translated to different data formats, or that transferring data requires expertise and access to special interfaces. By acting as a broker, you can fill this gap by negotiating a contract with data providers and/or recipients and doing the work required to make it convenient for them to exchange data.

![A flowchart displaying necessary steps required for data brokering, from producing data to sharing on behalf of others within a well defined ethical and legal framework.](/images/data_brokering_figure.svg){: height="500px" width="500px"}

**Figure 1: Data Brokering Workflow.** Individual data producers can process the data, store it, and submit it directly to international repositories or public health databases. Alternatively, in the data brokering model, several data producers can submit their data to a common data recipient. This recipient might be in charge of curating the data, analysing it with common pipelines, storing it, and re-sharing parts of the data to public health databases and international repositories (as agreed with the data providers). The latter service is often referred to as “data brokering” i.e. sharing data on behalf of others within a well defined ethical and legal framework. Note that legal aspects should be considered along all the steps.

### Considerations
There are many aspects to consider when getting started as a broker.

* Decide how to interact with the data providers/recipients, such as to what extent you will be able to adapt your workflows to meet their needs/requirements. 
* Identify what kind of processing you will handle as a broker, such as (meta)data curation and validation, data masking/anonymisation, etc.
* Define the time frame for your commitment and your responsibilities for the data, such as how to handle data loss before delivery, what to do with the data after a successful delivery, how to manage changes to data that has already been delivered, etc.
* Identify who is responsible for the data before, during and after delivery, such as the data controller/processor (according to GDPR) and/or intellectual property owner/licensee relationships between the provider and recipient
* Ensure that you will be able to establish contracts/agreements that cover the data and processing that you will handle, such as considerations for [data protection](data_protection), [licensing](licensing), and [compliance](compliance_monitoring).
* Estimate and secure the resources required to keep your commitment, such as staff with time and necessary skills, accounts, compute, storage and software
* Refer to the sections below for considerations related to collecting data from data providers and delivering data to public data repositories.


### Solutions

The solutions that you adopt will vary depending on the agreements you have negotiated with data providers and/or recipients. The following are examples of general solutions that would help you comply with regulations and implement good data management practices.
* [Data management plan](data_management_plan) – Many questions that you would answer while writing a data management plan can be relevant to answer when you specify the terms of service for your brokering service, such as data storage, data standards, legal and ethical, etc. 
* [Data protection](data_protection) – If you are working with data concerning people in the EU, you should make sure to comply with both national and international regulations for data protection.
* Apply for brokering permissions at the repository where you plan to submit data. For example, you can have a broker account at ENA; in this case, please visit [ENA Documentation](https://ena-docs.readthedocs.io/en/latest/faq/data_brokering.html) for guidelines on how to apply for such an account.

## Collecting and processing the metadata and data
### Description
Data brokering involves collecting data from various data providers (metadata and other data e.g. sequencing files), standardising and curating the data if needed, and then preparing the data for re-sharing e.g. in public international repositories. On the brokering platform, it is recommended that data be stored in a structured manner (e.g. in a relational database), using as much as possible controlled vocabularies and ontologies where they exist.

### Considerations
* [Data collection](collecting) should be carefully prepared, notably to define the data model, the metadata and data that are needed for the envisioned applications, assess which fields should be compulsory or optional, follow controlled vocabularies or ontologies, and identify the nature of data (personal, [sensitive data](sensitive) and thereby the required level of security or data treatment (e.g. pseudonymised or anonymised data, ethical consent…).
  * Collection of *metadata* can be done in various ways, each having its advantages and disadvantages, notably in terms of user-friendliness, ease of processing and [data quality](data_quality).
  * Collection of data files (e.g. sequencing data) should also involve minimal validation where possible (e.g. file extensions, regular checks of file sizes across the database to identify potential outliers with issues, integrity checks (checksum), etc).

* Regular data checks should always be performed at the database level, to check unicity of identifiers where expected (e.g. sample identifier within a laboratory is expected to be unique) and identify potential incoherences in the data (e.g. division indicated in the name of a virus versus division indicated in the location field).
* Data brokers should also consider implementing a mechanism for metadata and data files update within their platform, and define mechanisms to pass on the updates to international repositories. Please consider that depending on the update mechanisms in place at the international repositories (e.g.  Application Programming Interface (API) vs manual update via email), this process might become quite time-consuming.
* [Data transfer](data_transfer) from the data providers to the data brokering platform will depend on the nature and volume of data. The volume might be larger if data providers can submit data in batches. 
* Clarify with the data providers how the data will be processed, in terms of data curation/cleaning and downstream [data analyses](data_analysis). 
* [Data storage](storage) needs should be carefully addressed; consider storing data in compressed formats and deleting intermediate files from analyses that could be recomputed if needed to gain a storage space.

### Solutions
Collection of metadata can be done in various ways:

* Electronic forms (e.g. online form, eCRF) allow controlling data at the entry point, ensuring the use of controlled vocabularies and ontologies if properly set up. While user friendly for single uploads, this type of upload can become very cumbersome for batch upload.
* Spreadsheet files enable controlling data at the entry point, thanks to native validation features of spreadsheet tools (e.g Excel). It is at the same time very convenient for batch uploads and users generally like having a file that they can store and easily re-open to check what they have provided.
* Text files (e.g. TSV, CSV, JSON, XML, and so on) are very practical to automate batch submissions on the user side, since scripts can easily generate these files. It is recommended to specify to the users which encoding should be used (e.g. UTF-8). There is however no data control at the entry point and only upon submission to the data brokering database. All data validation is therefore performed upon loading into the database, and error handling should be carefully evaluated prior to implementation. Examples include automatically informing the user of errors and asking them to re-submit, or involving data curators who may correct obvious mistakes and can be in contact with data providers to clarify data validation errors. Some automation may also be implemented to map terms to a controlled list of terms or an ontology even in the case of minor typos.

## Sharing data to public repositories
### Description
Often, a goal of the broker is to [publish the collected and harmonised data](data_publication) in an open archive for the benefit of both the data owners and the wider scientific community. This supports sharing data with collaborators, referencing for publication and provides a [long-term storage solution](storage).

Once relevant repositories are identified for data submission and sharing, being an official data broker for a repository will generally give you additional rights such as the possibility to submit data on behalf of data producers, as well as providing a list of authors and address of the data providers. This is important to ensure that data producers can claim authorship (e.g. via [ORCiD](https://www.orcid.org)) and are given credit for their work.

### Considerations
* Does the repository have a “broker”-like account? This is usually referred to as a “Broker” or “Teams” account and is not always well advertised on the repository web page. Do not hesitate to contact the repository mailing-list for more information on the existence of brokering-like accounts and ask for the related additional rights.
* As a data broker, you generally wish to submit large amounts of data continuously. Hence, having access to a submission command-line-interface (CLI) or API is generally preferred over a user interface.

### Solutions
* For example, ENA offers a submission CLI and API as well as an official data broker role. For more information on data submission as a broker, please visit: [https://ena-docs.readthedocs.io/en/latest/faq/data_brokering.html?highlight=broker](https://ena-docs.readthedocs.io/en/latest/faq/data_brokering.html?highlight=broker) 
