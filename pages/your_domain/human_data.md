---
title: Human Data
contributors: [Niclas Jareborg, Nirupama Benis, Ana Portugal Melo, Pinar Alper]
---

## Introduction

When you do research on data derived from human individuals, there are some extra aspects that you need to consider during the data life cycle.  

## Ethical and legal planning, and Collection 

### Description

To do research on human data you must follow established research ethical guidelines and legislation. Preferably planning for these aspects should be done before starting the research, and in some cases laws even demand it.

### Considerations

* Have you got an **ethical permit** for your research project?
  * To get an ethical permit you have to apply for an **ethical review** by an **ethical review board**. The legislation that governs this differs between countries. Do seek advice from your research institute.
  * Informed consents
  * International standards (GA4GH, ...)
* Data protection legislation
  * EU GDPR
    * [Understanding the GDPR](gdpr)
    * [Determining the sensitivity of your data](data_sensitivity)
    * Data Protection Impact Assessments
  * Outside EU 
    * [International Compilation of Human Research Standards](https://www.hhs.gov/ohrp/sites/default/files/2020-international-compilation-of-human-research-standards.pdf)


### Solutions
  * [Data Information System DAISY](https://daisy-demo.elixir-luxembourg.org/) is software tool from ELIXIR that allows the record keeping of data processing activities in research projects. 
  * [DAWID](https://dawid.elixir-luxembourg.org) is a software tool from ELIXIR that allows generation of tailor-made data sharing agreements 
  * PIA, MONARC (Data protection impact assessment tools)
  * ADA-M 
  * Data Use Ontology (DUO)
  * Informed Consent Ontology (ICO)
  * Trygge ELSI Checklist
  * [GA4GH regulatory and ethical toolkit](https://www.ga4gh.org/genomic-data-toolkit/regulatory-ethics-toolkit/)
  * [EU General Data Protection Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679&from=EN).
  * [BBMRI-ERIC's Ethical Legal Societal Issues (ELSI) Knowledge Base](http://www.bbmri-eric.eu/elsi-knowledgebase) contains a glossary, agreement templates and guidance. 



## Processing and Analysing human data

### Description

This topic concerns the procedure and technical issues to ensure that personal information is protected.

### Considerations

* Information Security
  * Technical measures
  * Procedural measures
* Locating tools and platforms suited to handle human data


### Solutions

* EUPID
* RD-Connect Genome Phenome Analysis Platform
* GA4GH data security toolkit



## Preserving human research data

### Description

It is good research ethical practice to ensure that data underlying research is preserved, preferably in a way that adheres to the FAIR principles. With human data you have to take extra precautions into account when doing this.

### Considerations

* Legal obligations for preserving research data
* Planning for long-term storage 
  * Institutional
  * International Repositories
* Information security

### Solutions
* GA4GH regular and ethical toolkit (?)


## Sharing & Reusing

### Description
To make human research data reusable for others, it must be discoverable, stored in a safe way, and it must be clear under what circumstances it can be reused.
  
### Considerations

* Research collaborations across borders: <br/>
In the context of the GDPR and its country-specific implementations, the re-usability of human-subject data requires extra effort from data users as well as data providers. 
The ELIXIR RDM Toolkit offers help here with a use case demonstrator on **"Federated Access to Human Data"**. Its goals are:
  * identify key considerations for the responsible sharing of human genome-phenome data,
  * showcase a blueprint architecture for federated access to data, which needs stay within national borders,
  * demonstrate how ELIXIR RDM toolkit components can be combined to implement federated access.
                                          

* Sharing data via controlled-access: <br/>
Sensitive human data often carries restrictions to its use and it would need to be shared in a manner that obeys such restrictions. This type of sharing is called controlled-access, where researchers, who typically were involved in the primary collection of data to act as controllers foreseeing the data’s careful dissemination in a manner that honours data’s use conditions. The ELIXIR RDM Toolkit also provides a use case on the **"Re-use of Sensitive Human Data"**, which focuses on the responsibilities of data providers in precise documentation of use restrictions and the mechanisms that can assist data users to matching their requests for use of data against the data’s use restrictions.

* Ethical approvals and Informed consents
* Locating tools and platforms suited to handle human data


### Solutions
* (Federated) EGA
* dbGAP
* Beacon


## Relevant tools and resources

{% include toollist.html tag="human data" %}

## Training materials and events on the management of human-subject data
<!-- Link to Tess query -->




  



