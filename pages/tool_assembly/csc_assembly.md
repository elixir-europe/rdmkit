---
title: CSC
contributors: [Siiri Fuchs, Minna Ahokas]
description: The Center of Science (CSC) provides high-quality ICT expert services for researchers in Finland and their collaborators.
page_id: csc
affiliations: [FI, CSC, ELIXIR Europe]
related_pages: 
  your_tasks: [sensitive, dmp, data_security, gdpr_compliance, storage, data_publication, data_transfer, data_analysis]
  your_domain: [human_data]
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=csc
  - name: CSC - Bioscience webpages
    url: https://research.csc.fi/biosciences
  - name: CSC - Training and events webpages
    url: https://www.csc.fi/en/training
  - name: CSC - Learning Materials for Bioscientists
    url: https://research.csc.fi/bioscience-learning-materials
  - name: CSC - Data management youtube channel
    registry: YouTube
    url: https://www.youtube.com/watch?v=Ol7mniw687E&list=PLD5XtevzF3yEZw-8LadtaGVV8Um6CbMja
  - name: CSC - Research data management services for life science research (youtube video)
    url: https://youtu.be/lf9L7PYQrBE
  - name: Data analysis with Chipster - Course packages
    url: https://chipster.rahtiapp.fi/manual/courses.html
  - name: Tutorials and lecture playlists on different topics (youtube)
    registry: YouTube
    url: https://www.youtube.com/channel/UCnL-Lx5gGlW01OkskZL7JEQ/playlists
---

## What is the CSC data management tool assembly?
[CSC – IT Center for Science ](https://research.csc.fi/home) and [ELIXIR Finland](https://www.elixir-finland.org/en/frontpage/) provide services, tools and software for managing research data throughout the project life cycle. Services cover computing environments, analysis programs, tools for storing and sharing data during the project as well as opening and discovering research data. Furthermore, ELIXIR-FI provides flexible infrastructure for bioinformatics data analysis. Services are actively developed, and hence, please visit [CSC web pages](https://research.csc.fi/home) for the latest updates.


## Who can use the CSC data management tool assembly?
CSC and ELIXIR-FI services are accessible for researchers in Finland and to foreign collaborators of Finland-based research groups. Most of CSC's services are [free-of-charge](https://research.csc.fi/free-of-charge-use-cases) for academic research, education and training purposes in Finnish higher education institutions and in state research institutes. Researchers can start using services by registering an [account](https://research.csc.fi//accounts-and-projects) and get bioinformatics user support from our [service desk](mailto:servicedesk@csc.fi).


## How can you access the CSC data management tool assembly?
You can access all CSC services through several secure authentication methods. Start by [registering an account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/) with your home organization HAKA or VIRTU login or by contacting our [service desk](mailto:servicedesk@csc.fi). Afterwards you can also use ELIXIR login. Find more information from [CSC accounts and support web pages](https://research.csc.fi//accounts-and-projects) how to get access to different services.


## For what can you use the CSC data management tool assembly?

{% include image.html file="fi_csc_assembly.svg" caption="Figure 1. The CSC - IT Center for Science data management tool assembly." alt="CSC RDMkit" %}

### Data management planning
You can get support for data management [planning](planning) through [DMPTuuli](https://dmptuuli.fi/), a Finnish instance of DMPonline which includes guidance and templates provided by different organisations and funders. DMPs created in DMPTuuli are not yet machine actionable or linked to the CSC data management tool assembly services. However, a DMP is a valuable document when contacting the CSC research data management services.


### Data collection
When you start [collecting](collecting) data and need a storing environment where you can, for example, host cumulating or changing data, [Allas Object Storage](https://research.csc.fi/-/allas) is the recommended option. Indeed, Allas is CSC's general purpose research data storage server, which can be accessed on the CSC servers as well as from anywhere on the internet. Allas can be used both for static research data that needs to be available for analysis and to collect cumulating or changing data. For example, if you work with sequence data, the sequencing provider can transfer the data directly to Allas under your project.


### Data processing and analysis 
For [processing](processing), [analysing](analysing) and [storing data](storage) during the research project, CSC offers several [computing platforms](https://research.csc.fi/computing). These include both environments for non-sensitive and [sensitive data](sensitive_data). Depending on your needs, you can choose from a wide variety of computing resources: use [Chipster](https://chipster.csc.fi/) software for high-throughput data such as RNA-seq and single cell RNA-seq, build your own custom virtual machine, or utilise the full power of our world-class supercomputers. 

Supercomputers Puhti and Mahti can be used for larger scale analysis and simulations. They will soon be accompanied with the world-class supercomputer {% tool "lumi" %}. Pouta and Rahti cloud computing services offer more flexibility, allowing the user to manage the infrastructure. CSC's computers have a wide range of [preinstalled scientific software and databases](https://research.csc.fi/bioscience-programs) with usage instructions. 

This summer, CSC will be releasing beta versions of new services for sensitive data management: Sensitive Data Desktop (SD Desktop) and Sensitive Data Connect (SD Connect). Sensitive Data Submit (SD Submit) will be available later this year. The new Sensitive Data Services are designed to facilitate collaborative research across Finland and between Finnish academics and their collaborators. [SD Desktop](https://research.csc.fi/-/sd-desktop) is a service that allows a user and their authorized colleagues to access a private computing environment workspace via a web browser and analyze the data within a secure cloud. [SD Connect](https://research.csc.fi/-/sd-connect) allows you to collect, organize and share your encrypted sensitive data in a secure manner via web browser.


### Data sharing and publishing
It is recommended to [publish](data_publication) data in data specific repositories. You can find many options from {% tool "elixir-deposition-databases-for-biomolecular-data" %}. Furthermore, CSC and ELIXIR-FI will offer Federated EGA for sensitive human biomedical data that is linked to the central European Genome-phenome Archive and the SD Submit at the end of 2021. 

SD Submit allows you to publish sensitive data securely in a national repository. The service will give you the tools to describe your dataset (adding the appropriate metadata) and assign a permanent identifier (DOI). After publication, you will remain the data controller and decide according to specific policies, who can access the sensitive data for reuse. According to the GDPR, your data will remain within the Finnish borders and, at the same time, they will be accessible and discoverable according to FAIR data principles.

In addition to the above mentioned services, you can use national [Fairdata.fi services](https://research.csc.fi/-/fairdata-services). Fairdata IDA storage service enables saving, organising and sharing data within the project group and storing the data in an immutable state. After freezing your data in IDA, you can use Qvain, the research dataset description tool, to describe your data and thus create core metadata for your dataset, and publish it. Publishing means that your dataset will be published in Etsin, the research data finder, where you can discover and download any files you have associated with the dataset. Any published dataset is also made available to the [Research.fi portal](https://research.fi/) automatically by Fairdata services.
