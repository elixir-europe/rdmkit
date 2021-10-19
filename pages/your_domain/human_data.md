---
title: Human data
contributors: [Niclas Jareborg, Nirupama Benis, Ana Portugal Melo, Pinar Alper, Laura Portell Silva, Wolmar Nyberg Åkerström, Nazeefa Fatima]
page_id: human data
related_pages: 
  - your_tasks: [sensitive]
  - tool_assembly: [TSD, Covid-19, transmed]
faircookbook:
  - name: Data licenses
    url: https://fairplus.github.io/the-fair-cookbook/content/recipes/reusability/ATI_licensing_data.html
training:
  - name: Training in TeSS
    registry: TeSS
    registry_url: https://tess.elixir-europe.org
    url: https://tess.elixir-europe.org/search?q=sensitive%20human%20data
  - name: A FAIR guide for data providers to maximise sharing of human genomic data
    url: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005873
  - name: Toward better governance of human genomic data
    url: https://tess.elixir-europe.org/search?q=sensitive%20human%20data**
---

## Introduction

When you do research on data derived from human individuals, there are additional aspects that must be considered during the data life cycle. Note, much of the topics discussed on this page will refer to the EU General Data Protection Regulation (GDPR) as it is a central piece of legislation that affects basically all research done on human subjects in the EU and on individuals residing in the EU. 
Much of the information on this page is of a general nature when it comes to working with human data, an additional focus is on human genomic data and the sharing of such information for research purposes.

## Planning for, and collection of, human research data

### Description

For research on human data, you must follow established research ethical guidelines and legislations. Preferably, planning for these aspects should be done before starting to handle personal data and in some cases such as in the case of the GDPR, it is an important requirement by laws and regulations.

### Considerations

* Have you got an **ethical permit** for your research project?
  * To get an ethical permit, you have to apply for an **ethical review** by an **ethical review board**. 
    - The legislation that governs this differs between countries. Do seek advice from your research institute.
  * In most cases, you should get **informed consents** from your research subjects.
    - An informed consent is an agreement from the research subject to participate in and share personal data for a particular purpose. It shall describe the purpose and any risks involved (along with any mitigations to minimize those risks) in such a way that the research subject can make an informed choice about participating. It should also state under what circumstances the data can be used for the initial purpose, as well as for later re-use by others.
      - Consider describing data use conditions using a machine-readable formalized description such as [DUO](https://github.com/EBISPOT/DUO). This will greatly improve the possibilities to make the data FAIR later on.
    - Informed consents should be aquired for different purposes:
      - It is a cornerstone of _research ethics_. Regardless of legal obligations, it is important to ask for informed consents as it is a good research ethics practice and maintains trust in research.
      - _Ethical permission legislation_ to perform research on human subjects demand informed consents in many cases.
      - _Personal data protection legislation_ might have informed consent as one legal basis for processing the personal data.
      - _**Note that the content of an informed consent, as defined by one piece of legislation, might not live up to the demands of another piece of legislation.**_ For example, an informed consent that is good enough for an ethical permit, might not be good enough for the demands of the GDPR.
  * The [Global Alliance for Genomics and Health (GA4GH)](https://www.ga4gh.org) has recommendations for these issues in their [GA4GH regulatory and ethical toolkit](https://www.ga4gh.org/genomic-data-toolkit/regulatory-ethics-toolkit/).
    - [Consent Clauses for Genomic Research](https://drive.google.com/file/d/1O5Ti7g7QJqS3h0ABm-LyTe02Gtq8wlKM/view?usp=sharing)
* Personal data protection legislation
  * If you are performing research in the EU on human research subjects, or on human research subject in the EU, you must adhere to the General Data Protection Regulation - GDPR.
    * See [Data protection](data_protection) for more information on this law.
    * The sensitivity of your data affects what considerations you have make when handling it, see [Determining the sensitivity of your data](sensitive_data) for more information.
    * For some sensitive data you have to perform a Data Protection Impact Assessments. In general, any biomedical research on human subjects will need to do this.
  * Outside EU 
    * For countries outside the EU, the [International Compilation of Human Research Standards](https://www.hhs.gov/ohrp/sites/default/files/2020-international-compilation-of-human-research-standards.pdf) list relevant legislations.


### Solutions
  * [Tryggve ELSI Checklist](https://scilifelab-data-guidelines.readthedocs.io/en/latest/docs/general/sensitive_data.html) is a list of Ethical, Legal, and Societal Implications (ELSI) to consider for research projects on human subjects.
  * [Data Information System DAISY](https://daisy-demo.elixir-luxembourg.org/) is software tool from ELIXIR that allows the record keeping of data processing activities in research projects. 
  * [DAWID](https://dawid.elixir-luxembourg.org) is a software tool from ELIXIR that allows generation of tailor-made data sharing agreements 
  * [Privacy Impact Assessment Tool](https://www.cnil.fr/en/open-source-pia-software-helps-carry-out-data-protection-impact-assesment) is a software tool to make Data Protection Impact Assessments. 
  * [MONARC](https://open-source-security-software.net/project/MONARC) is a risk assessment tool that can be used to do Data Protection Impact Assessments
  * [Data Use Ontology](https://github.com/EBISPOT/DUO)
  * [Informed Consent Ontology](https://github.com/ICO-ontology/ICO)
  * [GA4GH regulatory and ethical toolkit](https://www.ga4gh.org/genomic-data-toolkit/regulatory-ethics-toolkit/)
  * [EU General Data Protection Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679&from=EN).
  * [BBMRI-ERIC's ELSI Knowledge Base](https://www.bbmri-eric.eu/elsi/knowledge-base/) contains a glossary, agreement templates and guidance. 



## Processing and analysing human research data

### Description

For human data, it is very important to use technical and procedural measures to ensure that the information is kept secure. There might exist legal obligations to document and implement measures to ensure an adequate level of security.

### Considerations

* Establish adequate **Information security** measures. This should be done for all types of research data, but is even more important for human data.
  - Information security is usually described as containing three main aspects - **Confidentiality**, **Integrity**, and **Accessibility**.
    - Confidentiality is about measures to ensure that data is kept confidential from those that do not have rights to access the data.
    - Integrity is about measures to ensure that data is not corrupted or destroyed.
    - Accessibility is about measures to ensure that data can be accessed by those that have a right to access it, when they need to access it.
  - Information security measures are both _procedural_ and _technical_.
  - What information security measures that need to be established should be defined at the planning stage (see above), when doing a risk assessment, e.g. a GDPR Data Protection Impact Assessment. This should identify information security risks, and define measures to mitigate those risks.
  - Contact the IT or Information security office at your institution to get guidance and support to address these issues.
  - [ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001) is an international information security standard adopted by data centres of some universities and research institutes.
* Locating tools and platforms suited to handle human data
  - Local research infrastructures might have established compute and/or storage solutions with strong information security measures tailored for working on human data (see some examples below). Contact your institute or your ELIXIR node for guidance.
    - Denmark - [Computerome](https://computerome.dk/)
    - Finland - [ePouta](https://research.csc.fi/-/epouta), which is part of the [CSC Tools Assembly](fi_csc_assembly)
    - Norway - [TSD Tools Assembly](NO_TSD_assembly)
    - Sweden - [Bianca](https://www.uppmax.uu.se/resources/systems/the-bianca-cluster/)
    - Spain - [MareNostrum](https://www.bsc.es/marenostrum/access-to-supercomputing-resources)
  - There are also emerging alternative approaches to analyse sensitive data, such as doing “distributed” computation, where defined analysis workflows are used to do analysis on datasets that do not leave the place where they are stored.
    - The GA4GH is developing standards for this in their [GA4GH Cloud workstream](https://www.ga4gh.org/how-we-work/2020-2021-roadmap/2020-2021-roadmap-part-ii/cloud-2020-2021-roadmap/)


### Solutions
 
* [EUPID](https://eupid.eu/#/home) is a tool that allows researchers to generate unique pseudonyms for patients that participate in rare disease studies. 
* [RD-Connect Genome Phenome Analysis Platform](https://rd-connect.eu/) is a platform to improve the study and analysis of Rare Diseases.
* [DisGeNET](https://www.disgenet.org/) is a platform containing collections of genes and variants associated to human diseases.
* [PMut](http://mmb.irbbarcelona.org/PMut) is a platform for the study of the impact of pathological mutations in protein structures.
* [IntoGen](https://www.intogen.org) collects and analyses somatic mutations in thousands of tumor genomes to identify cancer driver genes.
* [BoostDM](https://www.intogen.org/boostdm/search) is a method to score all possible point mutations in cancer genes for their potential to be involved in tumorigenesis.
* [Cancer Genome Interpreter](https://www.cancergenomeinterpreter.org) is designed to identify tumor alterations that drive the disease and detect those that may be therapeutically actionable.
* [GA4GH data security toolkit](https://www.ga4gh.org/genomic-data-toolkit/data-security-toolkit/)
* [GA4GH Cloud workstream](https://www.ga4gh.org/how-we-work/2020-2021-roadmap/2020-2021-roadmap-part-ii/cloud-2020-2021-roadmap/)



## Preserving human research data

### Description

It is a good ethical practice to ensure that data underlying research is preserved, preferably in a way that adheres to the FAIR principles. There might also exist legal obligations to preserve the data. With human data, you have to take extra precautions into account when doing this.

### Considerations

* Depositing data in an international repository
  * To make the data as accessible as possible according to the FAIR principles, do deposit the data in an international repository under controlled access whenever possible, see the section _Sharing & Reusing of human research data_ below
* Legal obligations for preserving research data
  * In some countries there are legal obligations to preserve research data long-term, e.g. for ten years. 
  * Even if the data has been deposited in an international repository, this might not live up to the requirements of the law.
  * The legal responsibility for preserving the data would in most cases lie with the research institution where you perform your research. You should consult the Research Data and/or IT support functions of your institution.
* Information security
  * The solutions you use need to provide information security measures that are appropriate for storing personal data, see the section _Processing and Analysing human research data_ above. Note that the providers of the solutions must be made aware that there are probably extra information security measures needed for long-term storage of this type of data.
*  Regardless of where your data is preserved long-term, do ensure that it is associated with proper metadata according to community standards, to promote FAIR sharing of the data.
* Planning for long-term storage 
  * Do address these issues of long-term preservation and data publication as early as possible, preferably already at the planning stage. If you are relying on your research institution to provide a solution, it might need time to plan for this.

### Solutions
* [GA4GH data security toolkit](https://www.ga4gh.org/genomic-data-toolkit/data-security-toolkit/)
* [ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001) is an international information security standard adopted by data centres of some universities and research institutes.


## Sharing and reusing of human research data

### Description
To make human research data reusable for others, it must be discoverable, stored in a safe way, and it must be clear under what circumstances it can be reused.
  
### Considerations

* Selecting suitable access modes for sharing human data
  * Human data often carries restrictions to its use and it would need to be shared in a manner that obeys such restrictions. There are three access modes for sharing research data:
    * **Open access**: Data is shared publicly.  Open-access is a rarely used access mode for the sharing of human data. To use open-access researchers need to ensure that the shared data cannot be traced back to individual study participants. In other words the data needs to be anonymised, which is difficult in practice.
    * **Registered access:** Data is shared with researchers, whose “researcher” status has been vouched for by their institution and who agree to abide by data usage policies of repositories that serve the shared data. Datasets that are shared via registered-access would typically have no restrictions besides the condition that data is to be used for research.   
    * **Controlled access**: Data can only be shared with researchers, whose research is reviewed and approved by a data access committee (DAC). Typically  researchers, who were involved in the primary collection of data will form the DAC. Use conditions for controlled-access could be a multitude and includes allowed research topics, allowed geographical regions, allowed recipients e.g. non-profit organisations.

* Publishing Human Research Data
  * It is highly recommended that Human Research Data is shared under controlled access. There are emerging models of sharing data through repositories under federated models. 
  * The **European Genome-phenome Archive (EGA)** is the prime repository for human genomic and phenotypic data. The EGA applies a controlled access model.

### Solutions
* The [European Genome-phenome Archive (EGA)](https://ega-archive.org/) is an international service for secure archiving and sharing of all types of personally identifiable genetic and phenotypic data resulting from biomedical studies and healthcare centres. Human genomic data is considered Sensitive data and is protected by European GDPR, therefore access must be restricted to authorized users. The EGA platform offers secure and European law-compliant data storage, working with GA4GH standards for encryption and storage. At the same time, data is discoverable in the EGA website and shareable with other researchers through authorization and authentication protocols. The right to allow access belongs to the Data providers (and not to the EGA), who are responsible to sign a DAA (Data Access Agreement) with researchers requesting access to their data. The EGA hosts data from all around the world and distributes it where and when the data providers’ law allows.
* [dbGAP](https://www.ncbi.nlm.nih.gov/gap/) and [JGA](https://www.ddbj.nig.ac.jp/jga/index-e.html) are other international data repositories, based in the USA and Japan respectively, that adopt a controlled-access model based on their national regulations. Due to European GDPR specific requirements, it may not be possible to deposit EU subjects’ data to these repositories.  
* The [GA4GH Beacon](https://beacon-project.io) project is a Global Alliance for Genomics & Health (GA4GH) initiative that enables genomic and clinical data sharing across federated networks. A Beacon is defined as a web-accessible service that can be queried for information about a specific allele with no reference to a specific sample or patient, thereby reducing privacy risks.
* GA4GH  Data Use Ontology [DUO](https://github.com/EBISPOT/DUO) is an international standard, which provides codes to represent data use restrictions for controlled access datasets.

