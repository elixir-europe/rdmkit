---
title: TSD for sensitive data - Norway
contributors: [Tina Visnovska, Federico Bianchini, Korbinian Bösl]
summary: This is a Data Management tools assembly for sensitive data around TSD. TSD as an infrastructure is aimed for researchers in Norway and their collaborators, but can be used by anyone.
tags: [IT support, data manager, researcher, human data, DMP, storage, sensitive]
page_tag: TSD
---

## What is the Norwegian tools assembly for sensitive data - TSD data management tools assembly?
The Norwegian ELIXIR tools assembly for sensitive data is centred around 
[TSD - literally for: services for sensitive data](https://www.uio.no/english/services/it/research/sensitive-data/ is an infrastructure provided by [the University of Oslo (UiO)](https://www.uio.no). Together with the other complementary tools provided by ELIXIR, TSD can be used for the management of [sensitive data](sensitive_data), including handling of [Human data](human_data).
This assembly covers [Planning](planning), [Processing](processing), [Analysing](analysing) and [Sharing](sharing) Data Life Cycle stages and offer [Data Storage](storage) capacities and tools for [transfer](data_transfer) of sensitive data, following the requirements of the EU general data protection regulations (GDPR) and its Norwegian implementation. 



## Who can use the TSD data management tools assembly?

Resources on TSD itself are accessible for international users through [EOSC](https://marketplace.eosc-portal.eu/services/tds) and directly through the [University of Oslo](https://www.uio.no/english/services/it/research/sensitive-data/access/). Researchers in Norway can in addition obtain access through the [national e-infrastructure program Sigma2](https://www.sigma2.no/sensitive-data-services) and additional storage quotas (up to 10TB) for existing TSD projects through the (Norwegian) bioinformatics support desk [contact@bioinfo.no](mailto:contact@bioinfo.no).
If you are affiliated to a Norwegian institution which has already stipulated a [data processing and/or service agreement with TSD](https://www.uio.no/tjenester/it/forskning/sensitiv/hjelp/start/kontrakter/index.html), this document can be used or amended to account for your project. Otherwise, you can establish a data agreement for your individual project by contacting [tsd-contact@usit.uio.no](mailto:tsd-contact@usit.uio.no).

## What can you use the TSD data management tools assembly for?

{% include image.html file="TSD_tool_assembly.svg" caption="Figure 1. Norwegian ELIXIR tools assembly for sensitive data - TSD" alt="TSD tool assembly" %}


The Norwegian tools assembly for sensitive data offers support with [Data Management Planning](planning) through an [instance of the Data Stewardship Wizard](https://elixir-no.ds-wizard.org) following the guidelines of the major national and European funding bodys. Dedicated references guide you through national infrastructure, resources, laws and regulations and also include the [Tryggve ELSI Checklist](https://neic.no/tryggve/links/) for Ethical, Legal and Social Implications. Soon you will be able to submit storage request forms for [Data Storage](storage) in TSD with defined access permissions through the Data Stewardship Wizard.

TSD offers [Data Storage](storage) services. Moreover, [Processing](processing) and [Analysing](analysing) of data is performed in a safe environment within TSD. 
As a national user, you can access TSD by identifying yourself using the Norwegian [ID-porten](https://eid.difi.no/en/id-porten) system. International users can get access by contacting [tsd-contact@usit.uio.no}(mailto:tsd-contact@usit.uio.no).

Within TSD, you can access  a Windows or Linux virtual machine (VM) and, upon request, [high performance computing (HPC) resources](https://www.uio.no/english/services/it/research/sensitive-data/use-tsd/hpc/resources.html) and [backup storage](https://www.uio.no/english/services/it/research/sensitive-data/use-tsd/directories-files/backup/index.html). You login using two factor authentication with [Google Authenticator](https://support.google.com/accounts/answer/1066447?co=GENIE.Platform%3DAndroid&hl=en) and a dedicated username and password. The [login in procedure](https://www.uio.no/english/services/it/research/sensitive-data/use-tsd/login/index.html) is different for Windows and Linux VMs on TSD.

As the primary design goal of TSD is security, [transfer of data](data_transfer) by other means to and from [TSD is restricted and logged](https://www.uio.no/english/services/it/research/sensitive-data/use-tsd/import-export/index.html).


### Data management planning

You can access the [ELIXIR-NO instance of the Data Stewardship Wizard](https://elixir-no.ds-wizard.org) using [ELIXIR AAI](https://elixir-europe.org/services/compute/aai), which can be coupled with the national solution for secure login and data sharing in the educational and research sector [FEIDE](https://www.feide.no/).

### Data Collection

If you use one of the National Norwegian research infrastructures, such as the Norwegian sequencing infrastructure [NorSeq](https://www.norseq.org/) they can directly upload data to your TSD project for you, as described in this [page](https://elixir.no/Services-bak/data_produced_NorSeq)

The sensitive data tools assembly provides [Nettskjema](https://nettskjema.no) as a solution for designing and managing data collections using online forms and surveys. This is a secure and GDPR-compliant service. It can be accessed through the  UiO's web pages and it is used through a web browser. Submissions from a Nettskjema questionnaire can be delivered securely (fully encrypted) to your project area within TSD. 
TSD-users are granted access to Nettskjema through [IDporten or FEIDE](https://www.uio.no/tjenester/it/adm-app/nettskjema/mer-om/eksterne-brukere). When the Nettskjema form is complete, you can upload it on TSD following [these instructions](https://www.uio.no/tjenester/it/adm-app/nettskjema/hjelp/koble-skjema-til-tsd.html). After verification, the form can be used for collecting sensitive data. Note that further processing and analysis of the results should be conducted within TSD. If exporting data is necessary, the files should be properly [de-identified or anonymised](sensitive_data.html#how-can-you-de-identify-your-data). 

### Data Processing and Analysis

For [Processing](processing) and [Analysing](analysing) your data,  you can use singularity containers and [individual tools on the HPC cluster](https://www.uio.no/english/services/it/research/sensitive-data/use-tsd/hpc/software/). 
The computing services provided through TSD include an Illumina DRAGEN (Dynamic Read Analysis for GENomics) node, which can be used to speed up genomic analysis of sequencing data. Dragen is a dedicated resource, if you want to run jobs on DRAGEN please send an email to [tsd-drift@usit.uio.no](mailto:tsd-drift@usit.uio.no).
 
### Data Sharing and Preservation
 
One solution for permanent archiving and sharing of personally identifiable genetic and phenotypic datasets resulting from biomedical research data is to deposit them to the [European Genome-phenome Archive (EGA)](https://ega-archive.org/). The EGA applies a controlled access model. There can be limitations, e.g. given consents, for your datasets which prevents them from leaving your jurisdiction or being archived in general. This will be partly addressed in the future by federated EGA services with nodes operating from one country or institution under one specific jurisdiction. This model will enable discovery of publicly shareable metadata about studies/datasets archived at the federated EGA nodes through the Central EGA, while the remaining data is stored in a local solution. These nodes will offer the same APIs and interfaces as the Central EGA and provide independent data distribution to users.
The Norwegian federated EGA (NFEGA) will be accessible through [ELIXIR AAI](https://elixir-europe.org/services/compute/aai), compatible with [FEIDE](https://www.feide.no/).


## Where can I find training materials, documentations and events about the TSD data management tool assembly?

You can find the documentation for the HPC cluster [here](https://www.uio.no/english/services/it/research/sensitive-data/use-tsd/hpc/colossus-userguide.html).

Course on the usage of TSD from the University of Oslo are announced [here](https://www.uio.no/english/for-employees/support/research/research-data/training/courses/). The recording of a previous course on Nettskjema and TSD is accessible [here](https://www.uio.no/for-ansatte/kompetanse/tema/data/nettskjema-tsd/tsd-nettskjema2april.html).


## What tools are used within the TSD data management tools assembly?

{% include toollist.html tag="TSD" %}
