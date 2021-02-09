---
title: Metadata management
keywords: [ontology, vocabulary]
contributors: [Flora D'Anna, Marco Carraro, Yvonne Kallberg, Markus Englund, Marco Roos]
tags: [collect, preserve, share, researcher, data manager]
---

## How to find appropriate standard metadata for datasets or samples?

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
  * Be aware that data type specific repositories usually have check-lists for metadata. For example, the European Nucleotide Archive provides [sample checklists](https://www.ebi.ac.uk/ena/browser/checklists) that can also be [downloaded as a spreadsheet](https://www.ebi.ac.uk/ena/submit/webin/sample-checklist).
 
* If you don’t know yet what repository you will use, look for what is the recommended minimal information (i.e. “Minimum Information ...your topic”, e.g. [MIAME](http://fged.org/projects/miame/) or [MINSEQE](http://fged.org/projects/minseqe/) or [MIAPPE](https://www.miappe.org)) required for your type of data in your community, or other metadata, at the following resources:
  * [Research Data Alliance (RDA): Metadata Dictionary: Standards](https://rd-alliance.github.io/metadata-directory/standards/)
  * [FAIRsharing.org](https://fairsharing.org) at “Standards” and “Collections”
  * [The Digital Curation Centre (DCC): List of Metadata Standards](https://www.dcc.ac.uk/guidance/standards/metadata/list)
 

## How to find appropriate vocabularies or ontologies?

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


<!-- ## External links -->

## Relevant tools and resources

{% include toollist.html tag="metadata" %}
