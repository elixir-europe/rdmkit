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
  * Machine-readable.
    * "Data in a data format that can be automatically read and processed by a computer, such as [CSV](https://opendatahandbook.org/glossary/en/terms/csv/), [JSON](https://opendatahandbook.org/glossary/en/terms/json/), [XML](https://opendatahandbook.org/glossary/en/terms/xml/), etc. Machine-readable data must be [structured data](https://opendatahandbook.org/glossary/en/terms/structured-data/).", [Open Data Handbook](https://opendatahandbook.org/glossary/it/terms/machine-readable/).
    * "Machine-readable data, or computer-readable data, is data in a format that can be processed by a computer. Machine-readable data must be structured data.", [Wikipedia](https://en.wikipedia.org/wiki/Machine-readable_data).
  * Machine-actionable.
    * "This term refers to information that is structured in a consistent way so that machines, or computers, can be programmed against the structure.", [DDI](https://ddialliance.org/taxonomy/term/198).
  * Machine-interpretable.
    * Machines can put the provided information into context and “understand” the meaning (semantics) and relations contained in the digital object. This concept is strictly related to the [Semantic Web](https://www.w3.org/standards/semanticweb/) vision and the [Linked Data](https://www.w3.org/standards/semanticweb/data) concept. See e.g. [What Is the Semantic Web?](https://www.ontotext.com/knowledgehub/fundamentals/what-is-the-semantic-web/).

* It is because of the variety of possible definitions for data that can be processed in some form by computers, that we decided to use the term _machine-actionable_ in the remainder of this document to refer to this type of (meta)data.

* Machine-actionable (meta)data doesn't mean just digital. For computers and software, it might not be possible to process the information contained in a digital object (e.g. scanned image). It is also NOT just:
  * A digital file that is readable by  some software (i.e. not broken or corrupted).
  * A digital file in an open (non-proprietary) or free  format (ex: .txt, .pdf) that can be read by some software.
  * A digital file that is readable by some non-proprietary software (e.g. .txt, .pdf).

* "The appropriate machine-actionable format may vary by type of data - so, for example, machine-actionable formats for geographic data may differ from those for tabular data.", [Open Data Handbook](https://opendatahandbook.org/glossary/en/terms/machine-readable/). For instance, [GML](https://en.wikipedia.org/wiki/Geography_Markup_Language) is one of the appropriate format for geographical information.

* Machine-actionable/readable formats are typically difficult to read by humans. Human-readable data is "in a format that can be conveniently read by a human. Some human-readable formats, such as [PDF](https://opendatahandbook.org/glossary/en/terms/pdf/), are not [machine-readable](https://opendatahandbook.org/glossary/en/terms/machine-readable/) as they are not [structured data](https://opendatahandbook.org/glossary/en/terms/structured-data/), i.e. the representation of the data on disk does not represent the actual relationships present in the data.", [Open Data Handbook](https://opendatahandbook.org/glossary/en/terms/human-readable/).
  * For instance, have you ever tried to extract or copy-paste a table from a PDF into a spreadsheet? It is usually very difficult and sometimes even impossible. This is a practical example of why PDF is not easy to read by machines, but it is very easy to read by humans. This occurs because the content in a PDF is described as “characters painted or drawn on a space”. So text is not text and tables are not tables for a PDF. They are just characters on the page space.
  * Tabular data in CSV file can be quite easy to read by humans, unless the table is very very big. A file in CSV format can be read by machines since it is structured in records (lines) and fields (columns) separated by comma, that is as a table. So, the computer reads whatever information stored as CSV in this tabular format.

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


 


