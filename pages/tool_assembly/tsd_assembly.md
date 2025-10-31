---
title: TSD
contributors: [Tina Visnovska, Federico Bianchini, Korbinian Bösl, Nazeefa Fatima]
description: The Sensitive Data Service (TSD) provides a platform to store, compute and analyse research sensitive data in compliance with Norwegian regulations regarding individuals’ privacy.
page_id: tsd
affiliations: ["NO", ELIXIR Europe, University of Oslo]
related_pages: 
  Your_tasks: [dmp, storage, sensitive, data_security, gdpr_compliance, transfer]
  Your_domain: [human_data]
training:
  - name: Documentation for the HPC cluster
    url: https://www.uio.no/english/services/it/research/sensitive-data/help/hpc/index.html
  - name: Courses on the usage of TSD from the University of Oslo
    url: https://www.uio.no/for-ansatte/kompetanse/tema/data/nettskjema-tsd/
  - name: Recording of a previous course on Nettskjema and TSD (April 2020)
    url: https://www.uio.no/for-ansatte/kompetanse/tema/data/nettskjema-tsd/tsd-nettskjema2april.html
---

## What is the Norwegian TSD Data Management Tools Assembly?
The Norwegian TSD tools assembly is centred around 
[TSD (services for sensitive data in Norwegian)](https://www.uio.no/english/services/it/research/sensitive-data/); an infrastructure provided by [the University of Oslo (UiO)](https://www.uio.no). Together with the complementary tools provided by ELIXIR, TSD is used for the management of [sensitive data](data_sensitivity), including [Human data](human_data).
This assembly covers Data Life Cycle stages such as [Planning](planning), [Processing](processing), [Analysing](analysing) and [Sharing](sharing) and, in addition, offers [Data Storage](storage) quotas and tools for [transfer](data_transfer) of sensitive data, following the requirements of the {% tool "eu-general-data-protection-regulation" %} and its Norwegian implementation. 


## Who can use the TSD data management tools assembly?

Resources on TSD are accessible for international users through the [User Management in TSD webpage](https://www.uio.no/english/services/it/research/sensitive-data/help/administrative-tasks/administer-users.html#toc2) (maintained by the University of Oslo); the page provides guidance on account creation and administration procedures. Researchers in Norway can also access resources through the [Sigma2 e-infrastructure program](https://www.sigma2.no/sensitive-data-services) which offers additional services and support for sensitive data storage and processing.
If you are affiliated with a Norwegian institution that has a [data processing and/or service agreement with TSD](https://www.uio.no/tjenester/it/forskning/sensitiv/hjelp/start/kontrakter/index.html), you can use/amend the agreement to account for your project. Otherwise, you can establish a data agreement for your individual project by contacting [tsd-contact@usit.uio.no](mailto:tsd-contact@usit.uio.no). 
International users may need to follow additional steps to comply with institutional and international data protection regulations. For example, additional authentication or approval steps may be required. Specific procedures for accessing resources from outside Norway are outlined in the TSD user documentation, and further assistance can be sought from the University of Oslo's support team or through local research infrastructure providers.

## What can you use the TSD data management tools assembly for?

{% include image.html file="TSD_tool_assembly.svg" caption="Figure 1. Norwegian ELIXIR tools assembly for sensitive data - TSD" alt="TSD tool assembly" %}


The Norwegian Tool Assembly for sensitive data offers support with [Data Management Planning](planning) through a [national instance of the Data Stewardship Wizard (DSW)](https://norway.dsw.elixir-europe.org/wizard/) following the guidelines of the major national and European funding bodies. Dedicated references in DSW guide you (user) through national infrastructure, resources, and laws and regulations, and also include the {% tool "tryggve-elsi-checklist" %} for Ethical, Legal and Social Implications. In the future, you will be able to submit storage request forms for [Data Storage](storage) in TSD with defined access permissions through the DSW.

In addition to its storage services, TSD offers safe environments for data [processing](processing) and [analysis](analysing). 
As a national user, you can access TSD by identifying yourself using the Norwegian [ID-porten](https://eid.difi.no/en/id-porten) system. International users can get access by contacting [tsd-contact@usit.uio.no](mailto:tsd-contact@usit.uio.no).

Within TSD, you can access a Windows or Linux virtual machine (VM) and, upon request, [high-performance computing (HPC) resources](https://www.uio.no/english/services/it/research/sensitive-data/help/hpc/index.html) and [backup storage](https://www.uio.no/english/services/it/research/sensitive-data/help/Backup-file-recovery.html). You log in using two-factor authentication with [Google Authenticator](https://support.google.com/accounts/answer/1066447?co=GENIE.Platform%3DAndroid&hl=en) and a dedicated username and password. The [login procedure](https://www.uio.no/english/services/it/research/sensitive-data/help/login.html) is different for Windows and Linux VMs.

As the primary design goal of TSD is data security, [transfer of data](data_transfer) by other means to and from [TSD is restricted and logged](https://www.uio.no/english/services/it/research/sensitive-data/help/import-export.html).


### Data management planning

You can access the [ELIXIR-NO instance of the Data Stewardship Wizard](https://norway.dsw.elixir-europe.org/) using {% tool "life-science-login" %}, which can be coupled with the national solution for secure login and data sharing in the educational and research sector [Feide](https://www.feide.no/).

### Data Collection

If you use one of the Norwegian research infrastructures, such as the Norwegian sequencing infrastructure [NorSeq](https://www.norseq.org/) they can directly upload data to your TSD project for you - the process is described by ELIXIR Norway at [https://elixir.no/Services-bak/data_produced_NorSeq](https://elixir.no/Services-bak/data_produced_NorSeq)

The sensitive data tools assembly provides [Nettskjema](https://nettskjema.no) as a solution for designing and managing data collections using online forms and surveys. This is a secure and GDPR-compliant service. It can be accessed through the UiO's web pages and it is used through a web browser. Submissions from a Nettskjema questionnaire can be delivered securely (fully encrypted) to your project area within TSD. 
TSD-users are granted access to Nettskjema through [IDporten or Feide](https://www.uio.no/tjenester/it/adm-app/nettskjema/mer-om/eksterne-brukere). When the Nettskjema form is complete, you can upload it on TSD following [these instructions](https://www.uio.no/tjenester/it/adm-app/nettskjema/hjelp/koble-skjema-til-tsd.html). After verification, the form can be used for collecting sensitive data. Note that further processing and analysis of the results should be conducted within TSD. If exporting data is necessary, the files should be properly [de-identified or anonymised](data_sensitivity.html#how-can-you-de-identify-your-data). 

### Data Processing and Analysis

For [Processing](processing) and [Analysing](analysing) your data,  you can use singularity containers and [individual tools on the HPC cluster](https://www.uio.no/english/services/it/research/sensitive-data/use-tsd/hpc/software/). 
The computing services provided through TSD include an Illumina DRAGEN (Dynamic Read Analysis for GENomics) node, which can be used to speed up genomic analysis of sequencing data. Dragen is a dedicated resource and if you want to run jobs on DRAGEN, please send an email to [tsd-drift@usit.uio.no](mailto:tsd-drift@usit.uio.no).
 
### Data Sharing and Preservation
 
One solution for permanent archiving and sharing of personally identifiable genetic and phenotypic datasets resulting from biomedical research data is to deposit them to the {% tool "the-european-genome-phenome-archive" %}. The EGA applies a controlled access model. There can be limitations, e.g. given consents, for your datasets which prevents them from leaving your jurisdiction or being archived in general. This is partly addressed by federated EGA services with nodes operating from one country or institution under one specific jurisdiction. This model enables discovery of publicly shareable metadata about studies/datasets archived at the federated EGA nodes through the Central EGA, while the remaining data is stored in a local solution. The federated EGA nodes offer the same APIs as the Central EGA and provide independent data distribution to users. The [Norwegian Federated EGA](https://ega.elixir.no/) is accessible through {% tool "life-science-login" %}, compatible with [Feide](https://www.feide.no/).
