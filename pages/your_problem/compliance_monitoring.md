---
title: Compliance monitoring & measurement
tags: [plan, researcher, data manager, policy officer] 
contributors: [Christophe Trefois, Wei Gu, Pinar Alper, Markus Englund, Vera Ortseifen]
description: measure compliance to data management regulations and standards.
---

## How can data management capabilities be measured and documented?

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
  *  The [FAIRplus project](https://fairplus.github.io/cookbook-dev/intro) has identified a set of [FAIR Indicators](https://zenodo.org/record/3909563#.X8ABpi-ZNTY) for data. 
  *  [FAIR Evaluators](https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/evaluations) are an automated approach to evaluate FAIRness of data services. 
* Information Security, Data Protection, Accountability
  *  [21 CFR part 11](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application) is a standard, which outlines criteria for electronic records in an IT system to be as valid as signed paper
records. It is widely adopted in lab information systems and applications used in clinical trials and medical research.
  *  [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html) is an international standard for the management of information security. It is adopted by some universities and research institutes to certify their data centres. 
  *  [ISO/IEC 27018](http://data-reuse.eu/wp-content/uploads/2017/02/ISO-Standards.pdf) is a standard aimed to be a code of practice for protection of personally identifiable information (PII) in public clouds.

## How can I ethically access genetic resources of another country?

### Description
With the enactment of the Convention on Biological Diversity (CBD) in 1993 the Access and Benefit-Sharing (ABS) was anchored as one of the goals. Article 3 of CBD clarifies, that states have sovereign rights over their own (biological & genetic) resources. Negotiations concluded in 2014 with the Nagoya Protocol on ABS). Since then, working with genetic resources and associated data of another country requires more preparatory measures. The aim of the Nagoya protocol is to ensure fair and equitable sharing of benefits arising from utilisation of genetic resources and from traditional knowledge associated with genetic resources. Many contries, as well as the EU, are parties of the Nagoya protocol and information on this can be found at the ABS Clearing House (https://absch.cbd.int/). By enactment of EU Regulation No. 511/2014, the obligations were implemented in the EU on 12.10.2014 (https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R0511).


### Considerations

Associated data about a genetic resources with Access legislation in place also requires special attention. Since ABS regulations put high demands on documentation and is therefore time consuming, this needs to be taken into account when planning a research project. When negotiating the Mutually Agreed Terms, it is very important to think about the future reusability of the data. If ABS is relevant to the project it should be part of the data management plan. Moreover, when sharing data, it is important to include necessary metadata regarding ABS in order to make reuse of the data possible.

ABS is not relevant for all genetic resources. It applies only to resources that have been accessed from a provider country after October 12, 2014. Some genetic resources are explicitly excluded, like for example human genomes, some crops and some viruses. Moreover, there are countries who are party of the Nagoya protocol, but have no ABS legislation in place. 


### Solutions

Plan: 
* Allow extra time to familiarise yourself with the legal requirements. For more information take a look at the European documents https://ec.europa.eu/environment/nature/biodiversity/international/abs/index_en.htm and https://ec.europa.eu/environment/nature/biodiversity/international/abs/material_en.htm
or on the dedicated websites cbd.int/abs/ (Nagoya Protocol) or https://absch.cbd.int/ (ABS Clearing-House).
* Help: Get in contact with the corresponding office in your country
* Actions: First you need a prior informed consent (PIC). In order to use the resource, you must additionally negotiate an agreement (often referred to as Mutually Agreed Terms, MAT) on how to share resulting benefits.

Reuse: 
* In order to make your data reusable to others again, as an important element of the FAIR principles, the legal basis must be clarified.

## Relevant tools and resources

{% include toollist.html tag="compliance" %}
