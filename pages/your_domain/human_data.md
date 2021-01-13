---
title: Human Data
contributors: [Niclas Jareborg, Nirupama Benis, Ana Portugal Melo, Pinar Alper]
---

## Introduction

When you do research on data derived from human individuals, there are some extra aspects that you need to consider during the data life cycle. Note that much of the topics discussed on this page will refer to the EU General Data Protection Regulation (GDPR) as it is a central piece of legislation that affects basically all research done on human subjects in EU and on individuals residing in the EU. 
Much of the information on this page is of a general nature when it comes to working with human data, an additional focus is on human genomic data and the sharing of such information for research purposes.

## Taking ethical and legal implications into consideration for Planning and Collection 

### Description

To do research on human data you must follow established research ethical guidelines and legislation. Preferably planning for these aspects has be done before starting to handle the personal data, and in some cases laws even demand it, such in the case of the GDPR.

### Considerations

* Have you got an **ethical permit** for your research project?
  * To get an ethical permit you have to apply for an **ethical review** by an **ethical review board**. 
    - The legislation that governs this differs between countries. Do seek advice from your research institute.
  * In most cases you should get **informed consents** from your research subjects.
    - An informed consent is an agreement from the research subject to participate in and share personal data for a particular purpose. It shall describe the purpose and any risks involved (along with any mitigations to minimize those risks) in such a way that the research subject can make an informed choice about participating. It should also state under what circumstances the data can be used for the initial purpose, as well as for later re-use by others.
      - Consider describing data use conditions using a machine-readable formalized description such as [DUO](https://github.com/EBISPOT/DUO). This will greatly improve the possibilities to make the data FAIR later on.
    - Informed consents should be aquired for different purposes:
      - It is a cornerstone of _research ethics_. Even if there are no other legal obligations for aquiring informed consents it is bad research ethics not to do it. You harm the trust in research if you don't.
      - _Ethical permission legislation_ to perform research on human subjects demand informed consents in many cases.
      - _Personal data protection legislation_ might have informed consent as one legal basis for processing the personal data.
      - _**Note that the content of an informed consent, as defined by one piece of legislation, might not live up to the demands of another piece of legislation.**_ For example, an informed consent that is good enough for an ethical permit, might not be good enough for the demands of the GDPR.
  * The [Global Alliance for Genomics and Health (GA4GH)](https://www.ga4gh.org) has recommendations for these issues in their [GA4GH regulatory and ethical toolkit](https://www.ga4gh.org/genomic-data-toolkit/regulatory-ethics-toolkit/).
    - [Consent Clauses for Genomic Research](https://drive.google.com/file/d/1O5Ti7g7QJqS3h0ABm-LyTe02Gtq8wlKM/view?usp=sharing)
* Personal data protection legislation
  * If you are performing research in the EU on human research subjects, or on human research subject in the EU, you must adhere to the General Data Protection Regulation - GDPR.
    * See [Understanding the GDPR](data_protection) for more information on this law.
    * The sensitivity of your data affects what considerations you have make when handling it, see [Determining the sensitivity of your data](data_classification) for more information.
    * For some sensitive data you have to perform a Data Protection Impact Assessments. In general, any biomedical research on human subjects will need to do this.
  * Outside EU 
    * For countries outside the EU, the [International Compilation of Human Research Standards](https://www.hhs.gov/ohrp/sites/default/files/2020-international-compilation-of-human-research-standards.pdf) list relevant legislations.


### Solutions
  * [Trygge ELSI Checklist](https://scilifelab-data-guidelines.readthedocs.io/en/latest/docs/general/sensitive_data.html) is a list of Ethical, Legal, and Societal Implications (ELSI) to consider for research projects on human subjects.
  * [Data Information System DAISY](https://daisy-demo.elixir-luxembourg.org/) is software tool from ELIXIR that allows the record keeping of data processing activities in research projects. 
  * [DAWID](https://dawid.elixir-luxembourg.org) is a software tool from ELIXIR that allows generation of tailor-made data sharing agreements 
  * [PIA](https://www.cnil.fr/en/open-source-pia-software-helps-carry-out-data-protection-impact-assesment) is a software tool to make Data Protection Impact Assessments. 
  * [MONARC](https://open-source-security-software.net/project/MONARC) is a risk assessment tool that can be used to do Data Protection Impact Assessments
  * [Data Use Ontology (DUO)](https://github.com/EBISPOT/DUO)
  * [Informed Consent Ontology (ICO)](https://github.com/ICO-ontology/ICO)
  * [GA4GH regulatory and ethical toolkit](https://www.ga4gh.org/genomic-data-toolkit/regulatory-ethics-toolkit/)
  * [EU General Data Protection Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679&from=EN).
  * [BBMRI-ERIC's Ethical Legal Societal Issues (ELSI) Knowledge Base](http://www.bbmri-eric.eu/elsi-knowledgebase) contains a glossary, agreement templates and guidance. 



## Processing and Analysing human data

### Description

For human data it is very important to use technical and procedural measures to ensure that the information is kept secure. There might exist legal obligations to document and implement measures to ensure an adequate level of security.

### Considerations

* Establish adequate **Information security** measures. This should be done for all types of research data, but is even more important for human data.
  - Information security is usually described as containing three main aspects - **Confidentiality**, **Integrity**, and **Accessability**.
    - Confidentiality is about measures to ensure that data is kept confidential from those that do not have rights to access the data.
    - Integrity is about measures to ensure that data is not corrupted or destroyed.
    - Accessability is about measures to ensure that data can be accessed by those that have a right to access it, when they need to access it.
  - Information security measures are both _procedural_ and _technical_.
  - What information security measures that need to be established should be defined at the planning stage (see above), when doing a risk assessment, e.g. a GDPR Data Protection Impact Assessment. This should identify information security risks, and define measures to mitigate those risks.
  - Contact the IT or Information security office at your institution to get guidance and support to address these issues.
  - [ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001) is an international information security standard.
* Locating tools and platforms suited to handle human data
  - Local research infrastructures might have established compute and/or storage solutions with strong information security measures tailored for working on human data. Contact your institute or your ELIXIR node for guidance.


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
In the context of the GDPR and its country-specific implementations, the reusability of human-subject data requires extra effort from data users as well as data providers. 
The ELIXIR RDM Toolkit offers help here with a use case demonstrator on **"Federated Access to Human Data"**. Its goals are:
  * identify key considerations for the responsible sharing of human genome-phenome data,
  * showcase a blueprint architecture for federated access to data, which needs stay within national borders,
  * demonstrate how ELIXIR RDM toolkit components can be combined to implement federated access.
                                          

* Sharing data via controlled-access: <br/>
Sensitive human data often carries restrictions to its use and it would need to be shared in a manner that obeys such restrictions. This type of sharing is called controlled-access, where researchers, who typically were involved in the primary collection of data to act as controllers foreseeing the data’s careful dissemination in a manner that honours data’s use conditions. The ELIXIR RDM Toolkit also provides a use case on the **"Reuse of Sensitive Human Data"**, which focuses on the responsibilities of data providers in precise documentation of use restrictions and the mechanisms that can assist data users to matching their requests for use of data against the data’s use restrictions.

* Ethical approvals and Informed consents
* Locating tools and platforms suited to handle human data


### Solutions
* (Federated) EGA
* dbGAP
* Beacon


## Relevant tools and resources

{% include toollist.html tag="human data" %}

## Training materials on the management of human-subject data
<!-- Link to Tess query -->




  



