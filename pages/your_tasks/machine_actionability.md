---
title: Machine actionability
contributors: [Karel Berka, Flora D'Anna, Erik Hjerde, Yvonne Kallberg, Sirarat Sarntivijai, Nazeefa Fatima, Rafael Andrade Buono, Alex Henderson, Korbinian Bösl, Dominik Martinat, M-Christine Jacquemot-Perbal]
description: How to make machine-actionable (meta)data.
page_id: machine_actionability
related_pages: 
    tool_assembly: []
dsw:
- name: List the data formats you will be using for interpretation and describe their
    structure
  uuid: a797cab9-0829-4787-a096-1b5cedc9147f
faircookbook:
- name: Introducing unique, persistent identifiers
  url: https://w3id.org/faircookbook/FCB006
- name: Introducing Search Engine Optimization (SEO)
  url: https://w3id.org/faircookbook/FCB010
- name: Creating a metadata profile
  url: https://w3id.org/faircookbook/FCB026
- name: Interlinking data from different sources
  url: https://w3id.org/faircookbook/FCB016
- name: Inventorying tools for converting data to RDF
  url: https://w3id.org/faircookbook/FCB051
- name: Introducing the DATS model
  url: https://w3id.org/faircookbook/FCB082
- name: Creating knowledge graphs from unstructured text
  url: https://w3id.org/faircookbook/FCB081
---

## What does machine-readable, machine-actionable and machine-interpretable mean?

### Description
More and more often, funders, data managers/stewards, IT staff and institutions in general encourage researchers in Life Sciences to generate metadata (and data) in ways that can be retrieved, read and processed by computers (machines).

{% include callout.html type="important" content="This page covers the WHAT, WHY and HOW of machine-actionable files but not what information to put into machine-actionable metadata files. For more information on this, please review the [Metadata management page](metadata_management)." %}

### Considerations
* It is common to come across different terms, such as _machine-readable_, _machine-actionable_ and _machine-interpretable_, which express different levels of making “(meta)data for machines”. The definition and the differences between these terms are not always clear and depend on the current technology. Computers, software, programming languages, formats and standards evolve quite fast and therefore new inventions could potentially make machine-readable/actionable any digital object that wasn’t before. 
  * One example is how developments in computer vision are making more and more the information contained in images, and not just the images themselves,  available for processing. 

* While providing an all-encompassing definition for this topic is not within the scope of this platform, it is important to clarify that (meta)data can be used by machines to different extents, depending on its characteristics. Here, we report a few common definitions.
    * "Machine-readable: data in a data format that can be automatically read and processed by a computer, such as [CSV](https://opendatahandbook.org/glossary/en/terms/csv/), [JSON](https://opendatahandbook.org/glossary/en/terms/json/), [XML](https://opendatahandbook.org/glossary/en/terms/xml/), etc. Machine-readable data must be [structured data](https://opendatahandbook.org/glossary/en/terms/structured-data/).", [Open Data Handbook](https://opendatahandbook.org/glossary/it/terms/machine-readable/).
    * "Machine-readable data, or computer-readable data, is data in a format that can be processed by a computer. Machine-readable data must be structured data.", [Wikipedia](https://en.wikipedia.org/wiki/Machine-readable_data).
    * "Machine-actionable data: structured data that are represented in a way so that a machine (computer) can be programmed to read and process each datum [representation of a concept intended for information processing purposes]", [DDI](https://ddialliance.org/glossary).
    * Machine-interpretable: machines can put the provided information into context and “understand” the meaning (semantics) and relations contained in the digital object. This concept is related to the [Semantic Web](https://www.w3.org/standards/semanticweb/) vision and the [Linked Data](https://www.w3.org/standards/semanticweb/data) concept. See e.g. [What Is the Semantic Web?](https://www.ontotext.com/knowledgehub/fundamentals/what-is-the-semantic-web/).

  The terms _machine-readable_ and _machine-actionable_ are often used interchangeably as synonymous. It is because of the variety of possible definitions for data that can be processed in some form by computers, that we decided to use the term **_machine-actionable_** in the remainder of this document to refer to this type of (meta)data.

* Machine-actionable (meta)data doesn't mean just digital. For computers and software, it might not be possible to process the information contained in a digital object (e.g. scanned image). It is also NOT just:
  * A digital file that is readable by  some software (i.e. not broken or corrupted).
  * A digital file in an open (non-proprietary) or free  format (ex: .txt, .pdf) that can be read by some software.
  * A digital file that is readable by some non-proprietary software (e.g. .txt, .pdf).

* "The appropriate machine-actionable/readable format may vary by type of data - so, for example, machine-actionable/readable formats for geographic data may differ from those for tabular data.", [Open Data Handbook](https://opendatahandbook.org/glossary/en/terms/machine-readable/). For instance, [GML](https://en.wikipedia.org/wiki/Geography_Markup_Language) is one of the appropriate format for geographical information.

* Machine-actionable/readable formats are typically difficult to read by humans. Human-readable data is "in a format that can be conveniently read by a human. Some human-readable formats, such as [PDF](https://opendatahandbook.org/glossary/en/terms/pdf/), are not [machine-actionable/readable](https://opendatahandbook.org/glossary/en/terms/machine-readable/) as they are not [structured data](https://opendatahandbook.org/glossary/en/terms/structured-data/), i.e. the representation of the data on disk does not represent the actual relationships present in the data.", [Open Data Handbook](https://opendatahandbook.org/glossary/en/terms/human-readable/).
  * For instance, have you ever tried to extract or copy-paste a table from a PDF into a spreadsheet? It is usually very difficult and sometimes even impossible. This is a practical example of why PDF is not easy to read by machines, but it is very easy to read by humans. This occurs because the content in a PDF is described as “characters painted or drawn on a space”. So text is not text and tables are not tables for a PDF. They are just characters on the page space.
  * Tabular data in CSV file can be quite easy to read by humans, unless the table is very very big. A file in CSV format can be read by machines since it is organised in records (lines) and fields (columns) separated by comma, that is as a table. So, the computer reads whatever information stored as CSV in this tabular format.

### Solutions 
For RDM in Life Sciences, machine-actionable metadata and data should:
* Be structured data: "data where the structural relation between elements is explicit in the way the data is stored on a computer disk.", [Open Data Handbook](https://opendatahandbook.org/glossary/en/terms/structured-data/).
* Be in a format that allows "many types of structure to be represented.", [Open Data Handbook](https://opendatahandbook.org/glossary/en/terms/structured-data/). For instance, JSON and XML for text files; certain formats for e.g. images that include structured (meta)data in a structured format.
  * Common formats such as XML and JSON contribute to [syntactic interoperability](https://en.wikipedia.org/wiki/Interoperability) between machines.
* Be interpreted by computer systems unambiguously. The meaning (semantic) of the (meta)data should be unique and shared among computer systems.
  * Syntaxes such as JSON-LD and RDF/XML contribute to [semantic interoperability](https://en.wikipedia.org/wiki/Semantic_interoperability#Semantic_as_a_function_of_syntactic_interoperability).
* Not be in PDF format (scanned images of lab books, tables, articles or papers in .pdf)
* Not be in plain text (.txt) nor Word documents (.docx) formats (e.g. README.txt file).
* Not be images, audio nor video (.jpeg, png, etc.).



## What are the advantages of machine-actionable metadata and data?

### Description

Numerous research institutes have already introduced or are going to introduce the use of Electronic Laboratory Notebook (ELN), Laboratory Information Management System (LIMS) or similar systems to manage samples, reagents, metadata and data, during a research project. The reason for this is that this software could organize information in a structured way and make (meta)data “more” machine-actionable, compared to traditional lab books or individual folders and files in a computer. The use of machine-actionable (meta)data allows for scalable solutions that can be applied during a project’s lifetime, increasing efficiency and ensuring that findings and contributions remain relevant within the research group.

Similarly, funders and institutions ask researchers to make their (meta)data FAIR and available in a machine-actionable way. This means that (meta)data should be in databases that can expose it in such a way to allow search engines and [harvesting](https://en.wikipedia.org/wiki/Metadata_discovery) servers to discover it, index it and link it to other relevant contextual information, thus vastly enhancing the likelihood of reusing the data (see [Horizon Europe DMP template](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e502e83f42&appId=PPGMS)).


### Considerations

* During a research project, scientists and researchers should utilize metadata in order to use, reuse, and expand knowledge by:
  * Managing experiments, samples and analysis pipelines. 
  * Expanding current datasets e.g. to increase the sample size.
  * Repeating experiments done by colleagues in the team.
  * Reproducing and confirming findings done by others.
  * Testing new hypotheses on data generated for different purposes.

* Scalable reuse of existing data is possible only if (meta)data is annotated with commonly used terms and findable by computers (e.g. database browser or search engines). The alternative could be very tedious and inefficient since you might have to:
  * Read the lab book of previous colleagues until you find the right page(s) where information about previously generated data is provided.
  * Look through numerous (shared) folders to find the documentation about a specific experiment done by previous colleagues that generated the dataset you are interested in.
  * Read all publications about a topic and check if there is a dataset linked to it and/or available upon request.

* Integration of multiple datasets can be straightforward only if each dataset can be easily queried, processed and formatted via software/programmes that can properly handle structured and big (meta)data files, such as {% tool "openrefine" %} and programming languages such as Python or R. Otherwise, manual data integration and processing can be very slow and error-prone.


### Advantages

The advantages of having machine-actionable data and metadata are numerous for all the parties involved.

#### For researchers

By providing structured metadata and data to a database that follows standards (metadata schemas, ontologies, file formats, programmatic access, etc.), at the level of each recorded value or observation, researchers:
* Could more easily query and filter (meta)data based on specific variables, experimental conditions, biological sources and many other parameters, based on the capabilities of the used ELN or data management software.
* Can more easily find and reproduce experiments performed in the past by others in  literature or in databases e.g. by using {% tool "europe-pmc" %} and [EBI Search](https://www.ebi.ac.uk/ebisearch/overview.ebi/about).
* Can easily integrate data from multiple datasets and studies, sharing the same experimental conditions or variables. Datasets integration and manipulation are easier to achieve, more reproducible and can be automated by using common programmes/software such as R and {% tool "openrefine" %}.
* Can make use of visualization and exploration tools, provided by some repositories, to browse and explore the data of multiple datasets at once. For instance, you can use {% tool "expression-atlas" %} to easily make a query about the expression of a gene in specific conditions, even without knowledge of any data analysis software. As another example, {% tool "gisaid" %} allows you to visualise the spreading of viral variants. See the pages in the [Your Domain](your_domain) section to find domain-specific databases, atlas or portals.
* Can import, export and exchange (meta)data between tools/systems/platforms without data loss. Exchanging and integrating (meta)data between two software or platforms is possible only if the format in which the information is contained can be read and interpreted by both. For instance, (meta)data from both {% tool "uniprot" %} and {% tool "pdbe-kb" %}  can be accessed in {% tool "3dbionotes" %} to enrich the structural analysis with sequence features.
* Can explore and visualise biological knowledge graphs by using software such as {% tool "knetminer" %} and {% tool "agronomic-linked-data" %}.
* Can perform complex queries, from a single entry point, across multiple distributed databases and across domains via [APIs](https://en.wikipedia.org/wiki/API) or via SPARQL Query Language. For instance: “Retrieve the number of UniProtKB/Swiss-Prot human enzymes that metabolize cholesterol or cholesterol derivatives and that are involved in diseases?" in the {% tool "integrated-database-of-small-molecules" %}.
* Can more easily find reference data and existing data in general, since machine-actionable (meta)data could be found by search engines and domain specific or generic data catalogs and portals.


#### For software developers and repositories managers
* Implementation of domain specific metadata schemas and ontologies for data and metadata increases the reusability for researchers.
* The use of machine-actionable formats and ontologies contribute to [syntactic](https://en.wikipedia.org/wiki/Interoperability) and [semantic interoperability](https://en.wikipedia.org/wiki/Semantic_interoperability) of the (meta)data, which can be used by other tools/software or platforms.
* Applying RDF syntax to the database can make the (meta)data available for knowledge graphs and semantic web applications.
* If [Application Programming Interface (API)](https://en.wikipedia.org/wiki/API) is available, other software/applications could make complex queries, access the database programmatically and always get up-to-date data.
* If the metadata of your database or repository is exposed according to specific standards, it could function as data provider or data source, and be harvested and indexed by
  * Data catalogues or data portals, such as {% tool "omicsdi" %} [data format specification](http://blog.omicsdi.org/post/omicsdi-spec/) and [COVID-19 Data Portal](https://www.covid19dataportal.org).
  * The [OpenAIRE aggregator](https://www.openaire.eu/aggregation-and-content-provision-workflows) that collects metadata records via OAI-PMH in the majority of cases.
  * Other instances of your data repository software which use OAI-PMH for metadata harvest, such as {% tool "dataverse" %} [harvesting](https://guides.dataverse.org/en/latest/admin/dashboard.html#harvesting).
  * Search engines such as [Google Dataset Search](https://datasetsearch.research.google.com/help), which relies on [sitemaps.org](https://www.sitemaps.org), {% tool "schema-org" %}, {% tool "data-catalog-vocabulary" %} and other approaches to datasets discovery.
* Machine actionable metadata facilitates the automatization of data handling and validation, allowing for easier development of new tools and analysis strategies (e.g. data visualization tools, machine learning and artificial intelligence applications).

#### For the authors of a machine-actionable public dataset
* High impact of the published data.
* More citations.
* More opportunity for collaborations.
* Opportunity for reproducibility test and confirmation of their results by others.
* Easy way to reuse the same (meta)data for other research.
* Improved scalability of their research efforts.

#### For public funders and institutions/governments
* Proof that their fundings produced knowledge that is findable and reusable.
* Transparency.
* Straightforward collection and indexing of research output in registries for easier impact assessment and report.


## What makes a file machine-actionable?

### Description

Due to the complexity of the topic and the lack of a unified definition, it is often difficult to identify the characteristics that make information contained in a digital object machine-actionable. Moreover, it is important not only to make a digital file machine-actionable, but also interoperable between different machines, so that different systems can exchange information.

The theoretically most machine-actionable format is in practice not achieved or established yet, however we try to list here some of the currently accepted best-practices that should be considered when making a file machine-actionable and interoperable, in Life Sciences research.

### Considerations

For machine-actionability and interoperability, you should consider:
1. File formats that are data exchange formats (e.g. JSON, XML).
2. (Meta)Data schemas recognised and accepted by communities as standards (e.g. [ISA model](https://isa-specs.readthedocs.io/en/latest/isamodel.html), {% tool "ome-data-model-and-file-formats" %}). The (meta)data schema describes the relations, such as hierarchy, of the elements that constitute the (meta)data model or structure.
3. Sets of metadata attributes or metadata checklists recognised and accepted by communities (e.g. MIAPPE, ENA Samples checklists), that capture reporting best practice in the field.
4. Controlled vocabularies and ontologies recognised and accepted by communities to convey meaning or semantics (e.g. EFO, OBI).

#### File format

* Information contained in a digital object is only as accessible as the [file format](https://opendatahandbook.org/glossary/en/terms/file-format/) it is saved in. A file format is the way that information is encoded for storage in a computer file. This is often indicated by the file extension, e.g. .csv for a CSV file. Different file formats are preferred for different purposes. For instance:
  * PDF is tailored to store and display text and graphics to humans, according to specific layouts, but it is not suitable for exchanging information between machines.
  * CSV is appropriate to exchange plain text information in a tabular format, but its flat nature makes a challenge to describe more complex relationships between information. 
  * XML and JSON formats are widely used for data exchange between systems (such as softwares, platforms or hardwares) and on the web. Both are easy to read and interpreted by machines, but not very human-readable.

* Exchange file formats using key-value pairs, such as .xml and .json, can wrap or encode the information to be sent or exchanged in a hierarchical (tree) data model. 
  * XML is a markup language. It is based on “elements” enclosed by pairs of “tags” and “attributes” ```(<tag>element<tag>)```. It is self-explanatory because it contains metadata about the format and “tags” are chosen by the creator of the .xml file. For instance, ```<name>Jaguar<name>```.
  * JSON format can be easily read in any programming language. It is based on key-value pairs separated by colons ( ```{key:value}``` ). For instance, ```{ name: “Jaguar” }```.

* File formats (or file extensions) for expressing data in triplets (e.g. “Jaguar” → “is in” → “Jungle”) in the Resource Description Framework (RDF) data model are .rdf for RDF/XML, .jsonld for JSON-LD, .nt for N-Triples and .ttl for Turtle syntax.

#### (Meta)Data schema
* A (meta)data schema describes the relations, such as hierarchy, among the elements or pieces of information that constitute the (meta)data model or structure.
* The relationship between pieces of information in a (meta)data schema can be implicit, following an agreed order (such as the order of columns in a table), or explicitly expressed by additional information in the file. To allow more universal interpretability, explicit additional information on the relationship between the pieces of information is highly advantageous.
* Some of the (meta)data schemas considered standard in Life Sciences define the relations between elements of the model in a more implicit way (e.g. ISA-TAB,  MAGE-TAB).
* Some data repositories develop customised (meta)data schemas.
* Different metadata schemas are preferred for different purposes. Some examples are listed below. 
  * {% tool "schema-org" %} and {% tool "bioschemas" %} markup are mostly used to describe web resources and make them findable by Web search engines. 
  * {% tool "data-catalog-vocabulary" %} is an RDF vocabulary designed to facilitate interoperability between data catalogs published on the Web.
  * [Investigation-Study-Assay (ISA) model](https://isa-tools.org/isa-api/content/isamodel.html#) was originally designed for describing multi-omics experiments in Life Sciences.
  * The [DAta Tag Suite (DATS)](https://github.com/datatagsuite) is a data description model designed and produced to describe datasets and associated metadata in a number of data deposition repositories.
  * The {% tool "ome-data-model-and-file-formats" %} is a specification for storing and exchanging data on biological imaging.

* The [W3C](https://www.w3.org/) consortium has formalised a universal abstract data model to potentially establish relationships among any resource available on the web (people, places, web pages, events, abstract concepts, etc.) called [Resource Description Framework (RDF)](https://www.w3.org/TR/rdf-concepts/#section-Introduction). This universal abstract data model allows us to describe relationships between multiple resources encoded in different formats, following different standards and stored in different locations/servers on the internet. 

  [RDF model](https://www.w3.org/TR/rdf-concepts/#section-Concepts) consists of sentences in the form of “Subject” →  “Predicate” → “Object”, called Triples, that describe the relationship between different pieces of information. An example could be “Jaguar” → “is in” → “Jungle”. Subject and Object can be any resource available on the internet, Predicate (properties) connects resources to other resources or data values, etc.

* RDF concept can be written and applied to databases using different syntaxes, such as N-Triples, Turtle,  RDF/XML, RDFa, JSON-LD. The benefit is that web browsers can put the provided information with these syntaxes into context and “understand” the meaning (semantics) and relations contained in the digital object. Information provided in RDF syntaxes is *machine-interpretable*. Digital objects in these formats can specify the context and the globally unique definition of each resource by referencing other standard metadata schemas and vocabularies/ontologies to describe web resources, such as Schema.org or Bioschemas.org (for Life Sciences), Data Catalog Vocabulary (DCAT), Dublin Core, etc.
  
  Any metadata schemas and [vocabularies/ontologies](https://www.w3.org/standards/semanticweb/ontology) describing web resources can be expressed according to standards, such as the [Web Ontology Language (OWL)](https://www.w3.org/TR/owl-ref/), the [RDF Schema (RDFS)](https://www.w3.org/TR/rdf-schema/) or the [Simple Knowledge Organisation System (SKOS)](http://www.w3.org/standards/techs/skos#w3c_all) to provide more expressive definition and inferences/relationships between terms or pieces of information.

#### Metadata checklist
* Here, we define metadata checklists as content in the form of a fixed set of attributes or fields, without any particular order nor structure. Compliance to metadata checklists is not related to the format nor the structure, but rather to the content provided.
* Many metadata checklists have been adopted as standards by Life Sciences communities (e.g. MIAPPE). 
* Some data repositories have customised metadata checklists (e.g. ENA Samples checklists).
* Attributes in a metadata checklist can be ontology terms.
* For more information see the [Data documentation and metadata](metadata_management) page.

#### Vocabulary or ontology
Vocabularies and ontologies are meant for describing concepts and relationships within a knowledge domain. For more information see the [Data documentation and metadata](metadata_management#how-do-you-find-appropriate-vocabularies-or-ontologies) page.


### Solutions

* (Meta)Data in data exchange formats (XML, JSON, CSV, etc.) that follows a standard metadata schema can be considered machine-actionable and syntactically interoperable. Ontologies that uniquely identify terms can be included for semantic interoperability.
* RDF syntaxes, such as RDF/XML and JSON-LD, support syntactic and semantic interoperability among machines. In other words, these formats convey the structure of the data being presented and the link to the necessary information to interpret its content, e.g. ontologies. Ontology or vocabulary is a way of expressing semantics/meaning of (meta)data. 

  Example of machine-interpretable metadata for the word “Jaguar” in JSON-LD format, which allows to clarify the intended meaning of the word "Jaguar" (the animal) and distinguishes it from other possible meanings such as car or computer:
  ```
  { 
  "@context": "http://bioschemas.org", → "hey browser, I am using these definitions"
  "@type": "Taxon",
  "@id": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=9690" , 
  "taxonRank": "species",
  "name": "Panthera onca",
  "alternateName": "Jaguar"
  }
  ```
* Metadata schemas and checklists can be found within [RDA curated list of Life Sciences metadata standards](https://rdamsc.bath.ac.uk) or among the [reporting guidelines](https://fairsharing.org/search?fairsharingRegistry=Standards&isMaintained=true&page=1&status=ready&subjects=life%2520science&recordType=reporting_guideline) in {%tool "fairsharing" %}.
* Examples of standard (meta)data schemas, in different formats, in Life Sciences: 
  * [ISA-JSON (.json) and ISA-TAB (.txt)](https://isa-specs.readthedocs.io/en/latest/) - generic metadata framework originally created to describe information about multi-omics experiments.
  * [MAGE-TAB](https://www.ebi.ac.uk/arrayexpress/help/magetab_spec.html) (.txt) - MicroArray Gene Expression Tabular. The format has been developed and adopted by the functional genomics community.
  * {% tool "ome-data-model-and-file-formats" %} (.tiff or .xml) for a wide range of biological imaging modalities. Ontologies to uniquely identify terms can be included. See also Hammer, M., Huisman, M., Rigano, A. et al. Towards community-driven metadata standards for light microscopy: tiered specifications extending the OME model. Nat Methods 18, 1427–1440 (2021). https://doi.org/10.1038/s41592-021-01327-9.
* For more information about metadata schemas and ontologies, see [Documentation and Metadata](metadata_management) page.














 


