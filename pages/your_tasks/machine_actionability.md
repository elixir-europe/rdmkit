---
title: Machine actionability
contributors: [Karel Berka, Flora D’Anna, Erik Hjerde, Yvonne Kallberg, Sirarat Sarntivijai, Nazeefa Fatima, Rafael Andrade Buono, Alex Henderson, Korbinian Bösl, Dominik Martinat, M-Christine Jacquemot-Perbal]
description: how to make machine-actionable (meta)data.
page_id: machine actionability
---

## What does machine-readable, machine-actionable or machine-interpretable mean for data and metadata in RDM?

### Description
More and more often, funders, data managers/stewards, IT staff and institutions in general encourage researchers in Life Sciences to generate metadata (and data) in ways that can be retrieved, read and processed by computers (machines).

### Considerations
* It is common to come across different terms, such as _machine-readable_, _machine-actionable_ and _machine-interpretable_, which express different levels of making “(meta)data for machines”. The definition and the differences between these terms are not always clear and depend on the current technology. Computers, software, programming languages, formats and standards evolve quite fast and therefore new inventions could potentially make machine-readable/actionable any digital object that wasn’t before. 
  * One example is how developments in computer vision are making more and more the information contained in images, and not just the images themselves,  available for processing. 

* While providing an all-encompassing definition for this topic is not within the scope of this platform, it is important to clarify that (meta)data can be used by machines to different extents, depending on its characteristics. Here, we report a few common definitions.
    * "Machine-readable: data in a data format that can be automatically read and processed by a computer, such as [CSV](https://opendatahandbook.org/glossary/en/terms/csv/), [JSON](https://opendatahandbook.org/glossary/en/terms/json/), [XML](https://opendatahandbook.org/glossary/en/terms/xml/), etc. Machine-readable data must be [structured data](https://opendatahandbook.org/glossary/en/terms/structured-data/).", [Open Data Handbook](https://opendatahandbook.org/glossary/it/terms/machine-readable/).
    * "Machine-readable data, or computer-readable data, is data in a format that can be processed by a computer. Machine-readable data must be structured data.", [Wikipedia](https://en.wikipedia.org/wiki/Machine-readable_data).
    * "Machine-actionable: this term refers to information that is structured in a consistent way so that machines, or computers, can be programmed against the structure.", [DDI](https://ddialliance.org/taxonomy/term/198).
    * Machine-interpretable: machines can put the provided information into context and “understand” the meaning (semantics) and relations contained in the digital object. This concept is strictly related to the [Semantic Web](https://www.w3.org/standards/semanticweb/) vision and the [Linked Data](https://www.w3.org/standards/semanticweb/data) concept. See e.g. [What Is the Semantic Web?](https://www.ontotext.com/knowledgehub/fundamentals/what-is-the-semantic-web/).

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
* Be in a format that allows "many types of structure to be represtented.", [Open Data Handbook](https://opendatahandbook.org/glossary/en/terms/structured-data/). For instance, JSON and XML for text files; certain formats for e.g. images that include structured (meta)data in a structured format.
  * Common formats such as XML and JSON contribute to [syntactic interoperability](https://en.wikipedia.org/wiki/Interoperability) between machines.
* Be interpreted by computer systems unambiguously. The meaning (semantic) of the (meta)data should be unique and shared among computer systems.
  * Syntaxes such as JSON-LD and RDF/XML contribute to [semantic interoperability](https://en.wikipedia.org/wiki/Semantic_interoperability#Semantic_as_a_function_of_syntactic_interoperability).
* Not be in PDF format (scanned images of lab books, tables, articles or papers in .pdf)
* Not be in plain text (.txt) nor Word documents (.docx) formats (e.g. README.txt file).
* Not be images, audio nor video (.jpg, png, etc).



## What are the advantages of generating machine-actionable metadata and data, during and after the project?

### Description

Numerous research institutes have already introduced or are going to introduce the use of Electronic Laboratory Notebook (ELN), Laboratory Information Management System (LIMS) or similar systems to manage samples, reagents, metadata and data, during a research project. The reason for this is that this software could organize information in a structured way and make (meta)data “more” machine-actionable, compared to traditional lab books or individual folders and files in a computer. The use of machine-actionable (meta)data allows for scalable solutions that can be applied during a project’s lifetime, increasing efficiency and ensuring that findings and contributions remain relevant within the research group.

Similarly, funders and institutions ask researchers to make their (meta)data FAIR and available in a machine-actionable way. This means that (meta)data should be in databases that can expose it in such a way to allow search engines and [harvesting](https://en.wikipedia.org/wiki/Metadata_discovery) servers to discover it, index it and link it to other relevant contextual information, thus vastly enhancing the likelihood of reusing the data (see [Horizon Europe DMP template](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/temp-form/report/data-management-plan-template_he_en.docx)).


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

* Integration of multiple datasets can be straightforward only if each dataset can be easily queried, processed and formatted via software/programmes that can properly handle structured and big (meta)data files, such as [OpenRefine](https://openrefine.org/#) and programming languages such as Python or R. Otherwise, manual data integration and processing can be very slow and error-prone.


### Advantages

The advantages of having machine-actionable data and metadata are numerous for all the parties involved.

#### For researchers

By providing structured metadata and data to a database that follows standards (metadata schemas, ontologies, file formats, programmatic access, etc.), at the level of each recorded value or observation, researchers:
* Could more easily query and filter (meta)data based on specific variables, experimental conditions, biological sources and many other parameters, based on the capabilities of the used ELN or data management software.
* Can more easily find and reproduce experiments performed in the past by others in  literature or in databases e.g. by using [Europe PMC](https://europepmc.org/) and [EBI Search](https://www.ebi.ac.uk/ebisearch/overview.ebi/about).
* Can easily integrate data from multiple datasets and studies, sharing the same experimental conditions or variables. Datasets integration and manipulation are easier to achieve, more reproducible and can be automated by using common programmes/software such as R and [OpenRefine](https://openrefine.org/#).
* Can make use of visualization and exploration tools, provided by some repositories, to browse and explore the data of multiple datasets at once. For instance, you can use  [Expression Atlas](https://www.ebi.ac.uk/gxa/home) to easily make a query about the expression of a gene in specific conditions, even without knowledge of any data analysis software. As another example, [GISAID](https://www.gisaid.org) allows you to visualise the spreading of viral variants. See the pages in the “Your Domain” section to find domain-specific databases, atlas or portals.
* Can import, export and exchange (meta)data between tools/systems/platforms without data loss. Exchanging and integrating (meta)data between two software or platforms is possible only if the format in which the information is contained can be read and interpreted by both. For instance, (meta)data from both [UniProt](https://www.uniprot.org) and [PDBe-KB](https://www.ebi.ac.uk/pdbe/pdbe-kb) can be accessed in [3DBioNotes](http://3dbionotes-ws.cnb.csic.es/) to enrich the structural analysis with sequence features.
* Can explore and visualise biological knowledge graphs by using software such as [KnetMiner](https://knetminer.com) and [AgroLD](http://agrold.southgreen.fr/agrold/).
* Can perform complex queries, from a single entry point, across multiple distributed databases and across domains via [APIs](https://en.wikipedia.org/wiki/API) or via SPARQL Query Language. For instance: “Retrieve the number of UniProtKB/Swiss-Prot human enzymes that metabolize cholesterol or cholesterol derivatives and that are involved in diseases?" in the [Integrated Database of Small Molecules](https://idsm.elixir-czech.cz/).
* Can more easily find reference data and existing data in general, since machine-actionable (meta)data could be found by search engines and domain specific or generic data catalogs and portals.


#### For software developers and repositories managers
* Implementation of domain specific metadata schemas and ontologies for data and metadata increases the reusability for researchers.
* The use of machine-actionable formats and ontologies contribute to [syntactic](https://en.wikipedia.org/wiki/Interoperability) and [semantic interoperability](https://en.wikipedia.org/wiki/Semantic_interoperability) of the (meta)data, which can be used by other tools/software or platforms.
* Applying RDF syntax to the database can make the (meta)data available for knowledge graphs and semantic web applications.
* If [Application Programming Interface (API)](https://en.wikipedia.org/wiki/API) is available, other software/applications could make complex queries, access the database programmatically and always get up-to-date data.
* If the metadata of your database or repository is exposed according to specific standards, it could function as data provider or data source, and be harvested and indexed by
  * Data catalogues or data portals, such as [OmicsDI](https://www.omicsdi.org) and [COVID-19 Data Portal](https://www.covid19dataportal.org).
  * Other instances of your data repository software, such as [Dataverse](https://guides.dataverse.org/en/latest/admin/dashboard.html#harvesting) and [EUDAT B2FIND](http://b2find.eudat.eu/guidelines/harvesting.html), which use OAI-PMH for metadata harvest.
  * Search engines such as [Google Dataset Search](https://datasetsearch.research.google.com/help), which relies on [sitemaps.org](https://www.sitemaps.org), [schema.org](https://schema.org), [DCAT](https://www.w3.org/TR/vocab-dcat/) and other approaches to datasets discovery.
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











 


