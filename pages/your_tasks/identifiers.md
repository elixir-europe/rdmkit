---
title: Identifiers
contributors: [Markus Englund, Flavio Licciulli, Nick Juty, Olivier Collin, Ulrike Wittig, Ivan Mičetić, Karel Berka, Shuxin Zhang, Hinri Kerstens, Flora D'Anna, Yvonne Kallberg, Rob Hooft] 
description: How to use identifiers for research data.
page_id: identifiers
related_pages: 
    tool_assembly: []
dsw:
- name: Will you make explicit cross-reference between physical samples and your digital
    data?
  uuid: 9e238002-da35-4f9b-a9b7-8fe3613a3c03
- name: Will this data be assigned a persistent identifier?
  uuid: d21fdb06-22bf-418e-aa40-dc5ef1485f56
faircookbook:
- name: Creating resolvable identifiers
  url: https://w3id.org/faircookbook/FCB077
- name: Interlinking data from different sources
  url: https://w3id.org/faircookbook/FCB016
- name: Introducing unique, persistent identifiers
  url: https://w3id.org/faircookbook/FCB006
- name: Minting identifiers with Globus Minid client
  url: https://w3id.org/faircookbook/FCB008
---

## Which types of identifiers can you use during data collection?
 
### Description 

A lot of (meta)data is collected in the form of [tables](https://datacarpentry.org/spreadsheet-ecology-lesson/01-format-data/), representing quantitative or qualitative measurements (values in cells) of certain named properties (variables in columns) of a range of subjects or samples (records or observations in rows). It can help your research a lot if you make sure you can address each of these records, variables and values unambiguously, i.e. if each has a unique identifier. This is also true for (meta)data that is not in tabular format (“key”:value format, unstructured data, etc.). Identifiers should always be used for metadata and data independently of the format.

If the research institute or group has a centralised and structured system (such as a central electronic database) in place to describe and store (meta)data, this process can be quite straightforward for the researcher. However, if there is no such system, often researchers have to set up an internal “database” to keep track of each record or observation in a study. This situation can be quite challenging for many reasons, one of which is assigning identifiers. The use of identifiers for records, variables and values will increase the [reusability and interoperability](about#why-are-the-fair-principles-needed) of the data for you, your future self and others.

### Considerations

* At the beginning of your research project, check if your institute or research group has a centralised database where data must be entered during data collection. Usually, large and international research projects, industries, research institutes or hospitals have a centralised electronic database, an Electronic Data Capture (EDC) system, a Laboratory Information Management System (LIMS) or an Electronic Lab Notebook (ELN) with a user interface for data entry. More details about using ELNs are given by e.g. {% tool "university-of-cambridge-electronic-research-notebook-products" %} and {% tool "harvard-medical-school-electronic-lab-notebooks" %}.
* If you can choose how to manage your data entry system, consider what the level of exposure of the identifier for each record or observation in the dataset should be. Define the context in which the identifier should be used and is unique. This is a key aspect of defining what kind of identifier for each individual record is appropriate in your case.
  * Should the identifier of a record or observation be unique within your spreadsheet, your entire research project files or across the whole institute? What is the reference system (or “target audience") of your identifier?
  * Will your reference system change in due time? If it will be opened up later, assigning globally unique identifiers from the beginning may save time.
  * Will the identifiers for individual records or observations be made openly accessible on the internet, during data collection?
* If the identifier of an individual record or observation should be unique only within your research group (within an intranet), and it will not be available on the internet, it can be considered an “internal or [local identifier](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2001414#pbio-2001414-g001)”. A local identifier is unique only in a specific local context (e.g. single collection or dataset).
* Local identifiers can be applied not only for individual records or observations in a tabular dataset but also for each variable or even value ([columns and cells in a tabular dataset](https://datacarpentry.org/spreadsheet-ecology-lesson/01-format-data/index.html), respectively).
* Identifiers for an individual record, variable and value in a dataset can be assigned by using ontology terms (see [metadata page](metadata_management#how-do-you-find-appropriate-vocabularies-or-ontologies)) or accession numbers provided by public databases such as, [EBI](https://www.ebi.ac.uk/services/all) and {% tool "national-center-for-biotechnology-information" %} repositories. Here there are few examples for tabular (meta)data, but the same type of identifiers can be applied independently of the (meta)data structure and format.
  * The patient ID is in its own row, a column header is the variable “[disease](http://www.ebi.ac.uk/efo/EFO_0000408)” from the EFO ontology (ID EFO:0000408), and the value in the cell is the child term “[chronic fatigue syndrome](http://www.ebi.ac.uk/efo/EFO_0004540)” (ID EFO:0004540) of “disease”.
  * The specimen ID is in its own row, a column header is the variable “Ensembl gene ID” from the {% tool "ensembl" %} genome browser and the value in the cell is the identifier for [BRCA1](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012048;r=17:43044295-43170245) gene ENSG00000012048.
* On top of identifiers for domain-specific metadata, more general fields such as research organisation, project participants, and funders are also typically described using identifiers.

### Solutions

* If your institute or research group uses centralised electronic databases (EDC, LIMS, ELN, etc.), follow the related guidelines for generating and assigning identifiers to individual records or observations, within the database. Some institutes have a centralised way of providing identifiers; ask the responsible team for help.
* Internal or local identifiers should be unique names based on specific naming conventions and formal patterns, such as [regular expression](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2001414#pbio-2001414-g001). Encode the regular expression into your spreadsheet or software and make sure to describe your regular expression in the documentation (README file or codebook). Avoid ambiguity. Identifiers that identify specimens (such as a biopsy or a blood sample), animal or plant models or patients could be written to the specimen tubes, the animal or plant model tags and patients files, respectively.
* Avoid embedding meaning into your local identifier. If you need to convey meaning in a short name implement a “label” for human readability only ([Lesson 4. Avoid embedding meaning or relying on it for uniqueness](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2001414#pbio-2001414-g001)).
* Do not use problematic characters and patterns in your local identifier ([Lesson 5. Avoid embedding meaning or relying on it for uniqueness](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2001414#pbio-2001414-g001)). Problematic strings can be misinterpreted by some software. In this case, it is better to fix the bugs or explicitly declare this possible issue in documentation. 
* Ontology terms or accession numbers provided by public databases, such as EBI and NCBI repositories, can be applied to uniquely identify genes, proteins, chemical compounds, diseases, species, etc. Choose exactly one for each type to be the most interoperable with yourself. Identifiers for molecules, assigned by EBI and NCBI repositories, keep track of relations between identifiers (for instance, different versions of a molecule). You can also submit your newly identified molecules to EBI or NCBI repositories to get a unique identifier.
* Applying ontologies to variables keeps clear structure and relations between variables (i.e., "compound & dose", "variable & unit"). Some pieces of software that allow you to integrate ontology terms into a spreadsheet are: {% tool "rightfield" %} and {% tool "onotomaton" %}.
* If you keep track of each record in a tabular format that gets new rows every day, use a versioning system to track the changes. Many cloud [storage](storage#what-features-do-you-need-in-a-storage-solution-when-collecting-data) services offer automatic versioning or keep a versioning log (see [data organisation page](data_organisation#how-do-you-manage-file-versioning)). Some parts of the tabular (meta)data file must be stable to be useful: do not delete or duplicate essential columns. Generate documentation about your tabular (meta)data file (README file, Codebook, etc.).
* If you collect data from a database that is frequently updated (dynamic or evolving database), it is recommended to keep track not only of the database ID, but also of the used version (by timestamp, or by recording date and time of data collection) and of the exact queries that you performed.  In this way, the exact queries can be re-executed against the timestamped data store ([Data citation of evolving data](https://zenodo.org/record/1406002#.YHXAVS0Rrs1)).
* If you reuse an existing dataset, keep the provided identifier for provenance and give a new identifier according to your system, but preserve the relation with the original identifier to be able to trace back to the source. Use a spreadsheet or create a mapping file to keep the relation between provenance and internal identifier.
* To set up a centralised machine-readable database, an EDC, a LIMS or an ELN for large research projects or institutes (available on intranet), highly specialised technical skills in databases, programming and computer science might be needed. We encourage you to talk to the IT team or experts in the field to find software and tools to implement such a system.
* Pieces of software to make a machine-readable system for databases and data collection are available. Their interfaces are quite user friendly but command-line skills might be needed depending on the kind of use that you need.
  * {% tool "molgenis" %} is a modular web application for scientific data. MOLGENIS was born from molecular genetics research but has grown to be used in many scientific areas such as biobanking, rare disease research, patient registries, and even energy research. MOLGENIS provides researchers with user-friendly and scalable software infrastructures to capture, exchange, and exploit the large amounts of data produced by scientific organisations all around the world.
  * {% tool "castor" %} is an EDC system for researchers and institutions. With Castor, you can create and customise your own database in no time. Without any prior technical knowledge, you can build a study in just a few clicks using an intuitive Form Builder. Simply define your data points and start collecting high-quality data, all you need is a web browser.
  * {% tool "redcap" %} is a secure web application for building and managing online surveys and databases. While REDCap can be used to collect virtually any type of data in any environment, it is specifically geared to support online and offline data capture for research studies and operations.
* We do not encourage setting up a centralised electronic database that will be exposed to the internet, unless really necessary. We encourage you to use existing and professional deposition databases to publish and share your datasets (see below).
* For generic fields to enter either your metadata entries or data management plan, it is very common to use:
  * {% tool "ror" %} to indicate affiliation
  * {% tool "orcid" %} to indicate the contributors
  * {% tool "ofr" %} to indicate the funder 
  
## Which type of identifiers should you use for data publication?
 
### Description

When all records and measurements have been collected and you are ready to share your entire dataset with others, it is good practice to assign **globally unique persistent identifiers** to make your dataset more FAIR. "A Globally Unique Identifier (GUID) is a unique number that can be used as an identifier for anything in the universe and the uniqueness of a GUID relies on the algorithm that was used to generate it" ([What is a GUID?](http://guid.one/guid)). “A persistent identifier (PID) is a long-lasting reference to a resource. That resource might be a publication, dataset or person. Equally, it could be a scientific sample, funding body, set of geographical coordinates, unpublished report, or piece of software. Whatever it is, the primary purpose of the PID is to provide the information required to reliably identify, verify, and locate it. A PID may be connected to a set of metadata describing an item rather than to the item itself" ([What is a persistent identifier, OpenAIRE](https://www.openaire.eu/what-is-a-persistent-identifier)). This means that any dataset with a PID will be findable even if the location of the dataset and its web address (URL) changes. The central registry that manages PID will ensure that the given PID will point you to the digital resource's current location. There are different types of PID, such as [DOI](https://www.doi.org/), [PURL](https://sites.google.com/site/persistenturls/), [Handle](http://www.handle.net/), [IGSN](https://www.igsn.org) and [URN](https://en.wikipedia.org/wiki/Uniform_Resource_Name). The [GO FAIR Foundation](https://www.go-fair.org/fair-principles/f1-meta-data-assigned-globally-unique-persistent-identifiers/) provides examples of GUID, PID and services that supply identifiers.

### Considerations

PIDs are essential to make your digital object (datasets or resources) citable, enabling you to claim and receive credit for your research output. In turn, when you reuse someone else research output, you have to cite it.

There are different ways to obtain a globally unique persistent identifier, and you need to decide which one is the best solution for your dataset or resource.
* By publishing into an existing public repository. For most types of data, this is usually the best option because the repository will assign a globally unique persistent identifier or an accession number. Update your internal database to keep the relationship with public identifiers.
* By opening up your local database to the public. This requires that the resource has a sustainability plan, as well as policies for versioning and naming of identifiers. While this option could be a viable solution if there is no public repository that allows for the right level of exposure of your data, it puts a lot of responsibility on your shoulders for future maintenance and availability. 

### Solutions

* If you want to publish your data into an existing public repository, please see our [data publication page](data_publication). The repository will provide globally unique persistent identifiers for your data. Check their guidelines if you need to edit or update your dataset after publication. Generic repositories (such as {% tool "zenodo" %} and {% tool "figshare" %}) use versioning DOI to update a public dataset or document.
* If you want to publish your data in an institutional public repository, ask the institution to obtain a namespace at {% tool "identifiers-org" %} in order to obtain globally unique persistent identifiers for your data.
* If you have the resources and skills to open up your database to the public, obtain a namespace at {% tool "identifiers-org" %} in order to acquire globally unique persistent identifiers for your data.
