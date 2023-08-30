---
title: Human data
description: Data management solutions for human data.
contributors: [Niclas Jareborg, Nirupama Benis, Ana Portugal Melo, Pinar Alper, Laura Portell Silva, Wolmar Nyberg Åkerström, Nazeefa Fatima, Vilem Ded, Teresa D'Altri]
page_id: human_data
related_pages:
  your_tasks: [sensitive]
  tool_assembly: [tsd, covid-19, transmed]
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=sensitive%20human%20data
  - name: A FAIR guide for data providers to maximise sharing of human genomic data
    url: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005873
  - name: Toward better governance of human genomic data
    url: https://tess.elixir-europe.org/search?q=sensitive%20human%20data
  - name: OMOP Common Data Model and the OHDSI analytics for observational analytics of real world healthcare data courses in EHDEN academy
    url: https://academy.ehden.eu/
dsw:
- name: Will you collect any data connected to a person, "personal data"?
  uuid: 49c009cb-a38c-4836-9780-8a8b3dd1cbac
- name: Will you be allowing authenticated access to the data?
  uuid: 55f03a4a-034b-422a-adf6-757416b7650a
- name: Does the collection of data involve human subjects?
  uuid: b464593d-fb92-4ad9-88e1-764306bb3051
- name: Are personal data sufficiently protected?
  uuid: d5990471-0618-42cd-92cb-bbbfd4f61532
---

## Introduction

When you do research on data derived from human individuals (hereon human data), there are additional aspects that must be considered during the data life cycle. Note, much of the topics discussed on this page will refer to the General Data Protection Regulation (GDPR) as it is a central piece of legislation that affects basically all research taking place in the European Union (EU) using human data or research with data of individuals residing in the EU.
Much of the information on this page is of a general nature when it comes to working with human data, an additional focus is on human genomic data and the sharing of such information for research purposes.

## Planning for projects with human data

### Description

When working with human data, you must follow established research ethical guidelines and legislations. Preferably, planning for these aspects should be done before starting to handle personal data and in some cases such as in the case of the GDPR, it is an important requirement by laws and regulations.

### Considerations

* Have you got an **ethical permit** for your research project?
  * To get an ethical permit, you have to apply for an **ethical review** by an **ethical review board**.
    - The legislation that governs this differs between countries. Do seek advice from your research institute.
  * The [Global Alliance for Genomics and Health (GA4GH)](https://www.ga4gh.org) has recommendations for these issues in their [GA4GH regulatory and ethical toolkit](https://www.ga4gh.org/genomic-data-toolkit/regulatory-ethics-toolkit/), see for instance the [Consent Clauses for Genomic Research](https://drive.google.com/file/d/1O5Ti7g7QJqS3h0ABm-LyTe02Gtq8wlKM/view?usp=sharing)(PDF document).
* The acquisition of data must be legal.
  * **Receiving data/samples directly from data subjects** requires in most cases **informed consents**.
    - An informed consent is an agreement from the research subject to participate in and share personal data for a particular purpose. It shall describe the purpose and any risks involved (along with any mitigations to minimise those risks) in such a way that the research subject can make an informed choice about participating. It should also state under what circumstances the data can be used for the initial purpose, as well as for later re-use by others.
      - Consider adoption of formalised machine-readable description of data use conditions. This will greatly improve the possibilities to make the data FAIR later on.
    - Informed consents should be acquired for different purposes:
      - It is a cornerstone of _research ethics_. Regardless of legal obligations, it is important to ask for informed consents as it is a good research ethics practice and maintains trust in research.
      - _Ethical permission legislation_ to perform research on human subjects demand informed consents in many cases.
      - _Personal data protection legislation_ might have informed consent as one legal basis for processing the personal data.
      - _**Note that the content of an informed consent, as defined by one piece of legislation, might not live up to the demands of another piece of legislation.**_ For example, an informed consent that is good enough for an ethical permit, might not be good enough for the demands of the GDPR.
  * **Receiving data from a collaborator** must be covered by a contract. Ensure detailed provisions on data use, retention, re-use and publication are included in the agreements (Data Use agreement, Consortium agreement, Data Sharing agreement, ...). This applies also to samples you receive from a collaborator. Related contract (e.g. Material Transfer Agreement - MTA) should cover use of human data generated from these samples. Incomplete legal framework for the data use can require lengthy legal amendments and can result in your in-ability to comply with requirements set out by your funder or targeted publisher.
  * **Receiving data from a repository** also comes with certain use restrictions. These are either defined in the license attributed to the data or defined in a dataset specific **access policy** and **terms of service** of the repository.
* Personal data protection legislation:
  * **Within the EU.** If you are performing human data research in the EU, or your data subjects are located in the EU, then you must adhere to the General Data Protection Regulation - GDPR.
    * Requirements for research that fall under the GDPR are outlined in the [RDMkit Data protection page](data_protection). 
    * Attributes of the data determines data sensitivity and  sensitivity affects the considerations for data handling. The [RDMkit Data Sensitivity page](sensitive_data) provides guidance on determining and reducing data sensitivity.
  * **Outside the EU.** For countries outside the EU, the {% tool "international-compilation-of-human-research-standards" %} list relevant legislations.


### Solutions
  * {% tool "tryggve-elsi-checklist" %} is a list of Ethical, Legal, and Societal Implications (ELSI) to consider for research projects on human subjects.
  * {% tool "daisy" %} is software tool from ELIXIR that allows the record keeping of data processing activities in research projects.
  * {% tool "dawid" %} is a software tool from ELIXIR that allows generation of tailor-made data sharing agreements
  * {% tool "pia" %} is a software tool to make Data Protection Impact Assessments.
  * {% tool "monarc" %} is a risk assessment tool that can be used to do Data Protection Impact Assessments
  * {% tool "data-use-ontology" %}
  * {% tool "informed-consent-ontology" %}
  * {% tool "ga4gh-regulatory-and-ethics-toolkit" %}
  * {% tool "eu-general-data-protection-regulation" %}
  * {% tool "bbmri-eric-s-elsi-knowledge-base" %} contains a glossary, agreement templates and guidance.

## Processing and analysing human data

### Description

For human data, it is very important to use technical and procedural measures to ensure that the information is kept secure. There might exist legal obligations to document and implement measures to ensure an adequate level of security.

### Considerations

* Establish adequate **Information security** measures. This should be done for all types of research data, but is even more important for human data.
  - Information security is usually described as containing three main aspects - **Confidentiality**, **Integrity**, and **Accessibility**.
    - Confidentiality is about measures to ensure that data is kept confidential from those that do not have rights to access the data.
    - Integrity is about measures to ensure that data is not corrupted or destroyed.
    - Accessibility is about measures to ensure that data can be accessed by those that have a right to access it, when they need to access it.
  - Information security measures are both _procedural_ and _technical_.
  - What information security measures that need to be established should be defined at the planning stage (see above), when doing a risk assessment, e.g. the GDPR Data Protection Impact Assessment. This should identify information security risks, and define measures to mitigate those risks.
  - Contact the IT or Information security office at your institution to get guidance and support to address these issues.
  - {% tool "iso-iec-27001" %} is an international information security standard adopted by data centres of some universities and research institutes.
* Check whether there are local/national tools and platforms suited to handle human data.
  - Local research infrastructures have established compute and/or storage solutions with strong information security measures tailored for working on human data. The [RDMkit national resources page](national_resources) lists the sensitive data support facilities available in various countries. Contact your institute or your ELIXIR node for guidance. 
  - There are also emerging alternative approaches to analyse sensitive data, such as doing “distributed” computation, where defined analysis workflows are used to do analysis on datasets that do not leave the place where they are stored.
    - The GA4GH is developing standards for this in their [GA4GH Cloud workstream](https://www.ga4gh.org/how-we-work/2020-2021-roadmap/2020-2021-roadmap-part-ii/cloud-2020-2021-roadmap/)
* Take data quality into account. When processing human data, data quality is a very important aspect to consider because it can influence the results of the research. Especially in the healthcare sector, some of the data that is used for research was not collected for research purposes, and therefore it is not guaranteed to have sufficient quality. Check the [RDMkit Data Quality page](data_quality) to learn more about how to assess the quality of health data.


### Solutions

* {% tool "eupid" %} is a tool that allows researchers to generate unique pseudonyms for patients that participate in rare disease studies.
* {% tool "rd-connect-genome-phenome-analysis-platform" %} is a platform to improve the study and analysis of Rare Diseases.
* {% tool "disgenet" %} is a platform containing collections of genes and variants associated to human diseases.
* {% tool "pmut" %} is a platform for the study of the impact of pathological mutations in protein structures.
* {% tool "intogen" %} collects and analyses somatic mutations in thousands of tumor genomes to identify cancer driver genes.
* {% tool "boostdm" %} is a method to score all possible point mutations in cancer genes for their potential to be involved in tumorigenesis.
* {% tool "cancer-genome-interpreter" %} is designed to identify tumor alterations that drive the disease and detect those that may be therapeutically actionable.
* GA4GH's [Data Security](https://www.ga4gh.org/genomic-data-toolkit/data-security-toolkit/), and {% tool "ga4gh-genomic-data-toolkit" %} provide policies, standards for the secure transfer and processing of human genomics data. GA4GH standards are often implemented into multiple tools. For example, the [Crypt4GH data encryption standard](https://www.ga4gh.org/news/crypt4gh-a-secure-method-for-sharing-human-genetic-data/) is implemented both in [SAMTools](http://samtools.github.io/hts-specs/crypt4gh.pdf) and also provided as a utility from the EGA Archive, {% tool "crypt4gh" %}.
* [GA4GH's Cloud Workstream](https://www.ga4gh.org/how-we-work/2020-2021-roadmap/2020-2021-roadmap-part-ii/cloud-2020-2021-roadmap/) is a more recent initiative and focuses on keeping data in secure cloud environments and meanwhile bringing computational analysis to the data.
* The {% tool "erpa" %} is a Web-based tool allowing users to create and manage a register of personal data processing activities (ROPA).
* {% tool "otp" %} is a data management platform for running bioinformatics pipelines in a high-throughput setting, and for organising the resulting data and metadata.

## Preserving human data

### Description

It is a good ethical practice to ensure that data underlying research is preserved, preferably in a way that adheres to the FAIR principles. There might also exist legal obligations to preserve the data. With human data, you have to take extra precautions into account when doing this.

### Considerations

* Depositing data in an international repository
  * To make the data as accessible as possible according to the FAIR principles, do deposit the data in an international repository under controlled access whenever possible, see the section _Sharing & Reusing of human data_ below
* Legal obligations for preserving research data
  * In some countries there are legal obligations to preserve research data long-term, e.g. for ten years.
  * Even if the data has been deposited in an international repository, this might not live up to the requirements of the law.
  * The legal responsibility for preserving the data would in most cases lie with the research institution where you perform your research. You should consult the Research Data and/or IT support functions of your institution.
* Information security
  * The solutions you use need to provide information security measures that are appropriate for storing personal data, see the section _Processing and Analysing human data_ above. Note that the providers of the solutions must be made aware that there are probably extra information security measures needed for long-term storage of this type of data.
*  Regardless of where your data is preserved long-term, do ensure that it is associated with proper metadata according to community standards, to promote FAIR sharing of the data.
* Planning for long-term storage
  * Do address these issues of long-term preservation and data publication as early as possible, preferably already at the planning stage. If you are relying on your research institution to provide a solution, it might need time to plan for this.

### Solutions
* {% tool "ga4gh-data-security-toolkit" %}
* {% tool "iso-iec-27001" %} is an international information security standard adopted by data centres of some universities and research institutes.
* {% tool "the-european-genome-phenome-archive" %} is an international service for secure archiving and sharing of all types of personally identifiable genetic and phenotypic data resulting from biomedical studies and healthcare centres. All services are free of charge. The EGA stores the data and metadata long-term, without ending date of the service. The data is backed-up in two separate geographical locations. The storing is GDPR-compliant, thanks to the use of [Ga4GH encryption standard](https://www.ga4gh.org/news/crypt4gh-a-secure-method-for-sharing-human-genetic-data/) and continuously kept up-to-date. National repositories working as Federated EGA nodes are available in some countries like Sweden, Norway, Finland, Germany and Spain. Those may address specific additional national legal needs, not included in European regulation.
* {% tool "dpia-knowledge-model" %} is a DSW knowledge model guiding users through a set of questions to collect information necessary for a research project Data Protection Impact Assessment (DPIA).

## Sharing and reusing of human data

### Description
To make human data reusable for others, it must be discoverable, stored in a safe way, and it must be clear under what circumstances it can be reused.

### Considerations

* Selecting suitable access modes for sharing human data:
  * Human data often carries restrictions to its use and it would need to be shared in a manner that obeys such restrictions. There are three access modes for sharing research data:
    * **Open access**: Data is shared publicly.  Open-access is a rarely used access mode for the sharing of human data. To use open-access researchers need to ensure that the shared data cannot be traced back to individual study participants. In other words the data needs to be anonymised, which is difficult in practice.
    * **Registered access:** Data is shared with researchers, whose “researcher” status has been vouched for by their institution and who agree to abide by data usage policies of repositories that serve the shared data. Datasets that are shared via registered-access would typically have no restrictions besides the condition that data is to be used for research.   
    * **Controlled access**: Data can only be shared with researchers, whose research is reviewed and approved by a Data Access Committee (DAC) - typically,  researchers who are/were involved in the primary collection of data will form the DAC. Use conditions for controlled-access could be a multitude and includes allowed research topics, allowed geographical regions, allowed recipients e.g. non-profit organisations.

* Publishing human data:
  * It is highly recommended that human data is shared under controlled access. There are emerging models of sharing data through repositories under federated models.
* Transferring human data:
  * Transferring human data has to be done in a secure way in order to avoid breaches of privacy. Encrypting of human data whilst it is being transferred provides successful protection if the data is intercepted by an external party while the transfer is being done.

### Solutions
* The {% tool "the-european-genome-phenome-archive" %} is an international service for secure archiving and sharing of all types of personally identifiable genetic and phenotypic data resulting from biomedical studies and healthcare centres. All services are free of charge. The EGA platform offers secure and European law-compliant data sharing. Data treatment is FAIR-compliant, thus data is discoverable in the EGA website and shareable with other researchers through authorisation and authentication protocols. The right to allow access to any dataset belongs to the Data controllers (and not to the EGA), who are responsible to sign a Data Access Agreement (DAA) with researchers requesting access to their data. Templates of the legal documents are provided. The EGA hosts data from all around the world and distributes it where and when the data controllers permit.
* {% tool "dbgap" %} and {% tool "jga" %} are other international data repositories, based in the USA and Japan respectively, that adopt a controlled-access model based on their national regulations. Due to European GDPR specific requirements, it may not be possible to deposit EU subjects’ data to these repositories.  
* The {% tool "beacon" %} project is a GA4GH initiative that enables genomic and clinical data sharing across federated networks. A Beacon is defined as a web-accessible service that can be queried for information about a specific allele with no reference to a specific sample or patient, thereby reducing privacy risks.
* The {% tool "data-use-ontology" %} is an international standard, which provides codes to represent data use restrictions for controlled access datasets.
* {% tool "crypt4gh" %} is a Python tool to encrypt, decrypt or re-encrypt files, according to the GA4GH encryption file format.
* {% tool "humanmine" %} is an integrative database of *Homo sapiens* genomic data, that integrates many types of human data and provides a powerful query engine, export for results, analysis for lists of data and FAIR access via web services.
