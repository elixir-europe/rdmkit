---
title: Compliance monitoring & measurement
contributors: [Christophe Trefois, Wei Gu, Pinar Alper, Markus Englund, Vera Ortseifen]
description: Measure compliance to data management regulations and standards.
page_id: compliance
related_pages:
  tool_assembly: [transmed]
faircookbook:
- name: Creating a data/variable dictionary
  url: https://w3id.org/faircookbook/FCB025
- name: FAIR Evaluator tool
  url: https://w3id.org/faircookbook/FCB049
- name: FAIRshake tool
  url: https://w3id.org/faircookbook/FCB050
---

## How can you measure and document data management capabilities?

### Description

Being able to reliably measure and document capabilities in data management, data protection and information security is important for research institutions.
By knowing their capabilities institutions can spot areas of improvement and direct human and IT resources accordingly. Also, having capabilities documented or formalised by certifications saves a good deal of effort during data management planning.


### Considerations

* Are you being asked to describe information security and data protection arrangements for a project DMP and you find yourself repeating similar descriptions across DMPs of projects?
  *  Contact your institution's Data Protection Officer (DPO) and Chief Information Security Officer (CISO). They may be able to provide you with a standard description of data protection and information security measures for institutional data platforms.
  *  Inquire whether the platforms you will use for your project's data management have an information security or data privacy certification.
* Are you providing a data service, such as data hosting, curation or archival and want to document and assess your service's capabilities?  
  *  Consider measuring the FAIR maturity of your services and the FAIRness of your data assets using community adopted standard metrics.


### Solutions

* FAIR data
  *  GO-FAIR Initiative provides a framework for designing [metrics for the evaluation of FAIRness](https://www.go-fair.org/2017/12/11/metrics-evaluation-fairness/).
* RDA developed a first set of [guidelines and a checklist](https://zenodo.org/record/3909563#.YKZV3i0RpN1) related to the implementation of the FAIR indicators.
* The [FAIRplus project](https://fairplus-project.eu) with its [FAIR Cookbook](https://fairplus.github.io/the-fair-cookbook/content/recipes/assessing-fairness.html#) provides services, tools, and indicators necessary for the assessment or the evaluation of data against the FAIR Principles:
    * [FAIR Evaluators](https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/#%2F!) are an automated approach to evaluate FAIRness of data services.
    * [FAIRassist.org](https://fairassist.org/#!/) aims to collect and describe existing resources for the assessment and/or evaluation of digital objects against the FAIR principles.
* Information Security, Data Protection, Accountability
  *  [21 CFR part 11](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application) is a standard, which outlines criteria for electronic records in an IT system to be as valid as signed paper
records. It is widely adopted in lab information systems and applications used in clinical trials and medical research.
  *  [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html) is an international standard for the management of information security. It is adopted by some universities and research institutes to certify their data centres.
  *  [ISO/IEC 27018](https://www.iso.org/standard/76559.html) is a standard aimed to be a code of practice for protection of personally identifiable information (PII) in public clouds.

## How can you ethically access genetic resources of another country?

### Description

If during your research project you need to access or transport genetic resources and/or associated traditional knowledge from any country, you should comply to all relevant (inter)national legislation. One important legislation in this case is the Nagoya Protocol. The Nagoya Protocol specifies the Access and Benefit-Sharing (ABS) principles, established by the Convention on Biological Diversity (CBD), for countries providing and using genetic resources in a legally binding way.

Article 3 of CBD clarifies, that states have sovereign rights over their own (biological and genetic) resources. Negotiations concluded in 2014 with the Nagoya Protocol on ABS. Since then, working with genetic resources and associated data of another country requires more preparatory measures. The aim of the Nagoya protocol is to ensure fair and equitable sharing of benefits arising from utilisation of genetic resources and from traditional knowledge associated with genetic resources. Many countries, as well as the EU, are parties of the Nagoya Protocol and information on this can be found at the [ABS Clearing House](https://absch.cbd.int/). By enactment of [EU Regulation No. 511/2014](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R0511) the obligations were implemented in the EU on 12.10.2014. Here you can find a short video about [ABS – Simply Explained](https://www.youtube.com/watch?v=09zflWUIKTQ&t=306s).

[Genetic resources are defined](https://ec.europa.eu/environment/nature/biodiversity/international/abs/pdf/Glossary%20for%20Europa.pdf) as “all genetic material of actual or potential value. Essentially, the term encompasses all living organisms (plants, animals and microbes) that carry genetic material potentially useful to humans. Genetic resources can be taken from the wild, domesticated or cultivated. They are sourced from: natural environments (in situ) or human-made collections (ex situ) (e.g. botanical gardens, gene banks, seed banks and microbial culture collections).".
[The definition of “traditional knowledge associated with genetic resources”](https://ec.europa.eu/environment/nature/biodiversity/international/abs/pdf/Glossary%20for%20Europa.pdf) is left to the Parties of the Protocol instead. However, in the context of the Nagoya Protocol, “the term is used in relation to the knowledge, innovations and practices of indigenous and local communities that result from the close interaction of such communities with their natural environment, and specifically to knowledge that may provide lead information for scientific discoveries on the genetic or biochemical properties of genetic resources. It is characteristic of traditional knowledge that it is not known outside the community holding such knowledge.”.


### Considerations

* Since ABS regulations and Nagoya Protocol put high demands on documentation, this legal aspect is time consuming and therefore needs to be taken into account when planning the research project.
* ABS is not relevant for all genetic resources. It applies only to resources that have been accessed from a provider country after October 12, 2014. Some genetic resources are explicitly excluded, like for example human genomes, some crops and some viruses. Moreover, there are countries who are party of the Nagoya Protocol, but have no ABS legislation in place.
* If ABS is relevant to the project it should be part of the Data Management Plan.
* You must comply with the Nagoya Protocol and other national legislation before accessing the genetic resources.
* When negotiating the Mutually Agreed Terms (MAT), it is very important to think about the future reusability of the data generated based on the genetic resources. When sharing this data, it is important to include the necessary metadata regarding ABS and to clarify the legal basis, in order to make the data reusable to others again.

### Solutions

* In the planning stage of your research project, allow extra time to familiarise yourself with the legal requirements. In order to determine if the Nagoya Protocol applies to your research, take a look at:
  * The European documents [Sharing nature's genetic resources – ABS](https://ec.europa.eu/environment/nature/biodiversity/international/abs/index_en.htm) and [Access and Benefit Sharing](https://ec.europa.eu/environment/nature/biodiversity/international/abs/material_en.htm).
  * The dedicated websites [Nagoya Protocol](https://www.cbd.int/abs/) or [ABS Clearing-House](https://absch.cbd.int/).
  * Look for "Nagoya Protocol checklists for researchers" available in your institution to determine if the Nagoya Protocol applies to your research.
  * Ask help to legal experts and get in contact with the corresponding office in your country or the legal team in your institution.
* If ABS principles and Nagoya Protocol apply to your project, make sure to:
  * Investigate the conditions for accessing the genetic resources and/or the associated traditional knowledge in the country of origin.
  * Make a Prior Informed Consent (PIC) with the country that will provide the genetic resources and/or the associated traditional knowledge, to clarify the goal of your research and how you will use the requested resources.
  * Negotiate a Mutually Agreed Terms (MAT) to establish how to share the resulting benefits. The benefits for the provider of the genetic resources and/or the associated traditional knowledge can be monetary, transfer of knowledge and technology, training, etc.
