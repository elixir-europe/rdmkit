---
title: CSC
contributors: [Siiri Fuchs, Minna Ahokas, Janina Juuvinmaa]
editors: [Bert Droesbeke, Flora D'Anna, Korbinian Bösl]
description: The Center of Science (CSC) provides high-quality ICT expert services for researchers in Finland and their collaborators.
page_id: csc
supported_by: [FI, CSC, ELIXIR Europe]
related_pages: 
  Your_tasks: [sensitive, dmp, data_security, gdpr_compliance, storage, data_publication, transfer, data_analysis]
  Your_domain: [human_data]
training:
  - name: CSC Search query in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=csc
  - name: CSC - Bioscience webpages
    url: https://research.csc.fi/biosciences
  - name: CSC - Training and events webpages
    url: https://csc.fi/en/trainings/training-calendar/
  - name: CSC - Learning Materials for Bioscientists
    url: https://research.csc.fi/bioscience-learning-materials
  - name: CSC - Data management YouTube channel
    registry: YouTube
    url: https://www.youtube.com/watch?v=Ol7mniw687E&list=PLD5XtevzF3yEZw-8LadtaGVV8Um6CbMja
  - name: CSC - Research data management services for life science research (YouTube video)
    url: https://youtu.be/lf9L7PYQrBE
  - name: Data analysis with Chipster - Course packages
    url: https://chipster.2.rahtiapp.fi/manual/courses.html
  - name: Tutorials and lecture playlists on different topics YouTube Playlist
    registry: YouTube
    url: https://www.youtube.com/channel/UCnL-Lx5gGlW01OkskZL7JEQ/playlists
---

## What is the CSC data management tool assembly?
[CSC – IT Center for Science ](https://research.csc.fi/home) and [ELIXIR Finland](https://www.elixir-finland.org/en/frontpage/) provide services, tools and software for managing research data throughout the project life cycle. Services cover computing environments, analysis programs, tools for storing and sharing data during the project as well as opening and discovering research data. Furthermore, ELIXIR-FI provides flexible infrastructure for bioinformatics data analysis. Services are actively developed, and hence, please visit [CSC web pages](https://research.csc.fi/home) for the latest updates.


## Who can use the CSC data management tool assembly?
CSC and ELIXIR-FI services are available for researchers affiliated with a Finnish academic organisation or research institutes and their international collaborators. Most of CSC’s services are [free of charge](https://research.csc.fi/free-of-charge-use-cases) for academic research, education and training purposes in Finnish higher education institutions and state research institutes. Researchers can start using services by registering an account and get bioinformatics user support from our [service desk](mailto:servicedesk@csc.fi).


## How can you access the CSC data management tool assembly?
You can access all CSC services through several secure authentication methods. Start by [creating an account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/) with your home organisation HAKA or VIRTU login or by contacting our [service desk](mailto:servicedesk@csc.fi). Afterwards you can also use Life Science login. Find more information from [CSC accounts and support web pages](https://research.csc.fi//accounts-and-projects) how to get access to different services.


## For what can you use the CSC data management tool assembly?

{% include image.html file="fi_csc_assembly_v3.svg" caption="Figure 1. The CSC - IT Center for Science data management tool assembly." alt="CSC RDMkit" %}

### Data management planning
Research funders often require a [data management plan (DMP)](data_management_plan) as part of the funding application process or after funding has been approved. See e.g. guidance on creating a DMP for the [Research Council of Finland](https://www.aka.fi/en/research-funding/apply-for-funding/how-to-apply-for-funding/az-index-of-application-guidelines/data-management-plan/data-management-plan/).

A DMP is a living document that helps researchers plan and document how data will be managed throughout the research lifecycle. In the future, machine-actionable DMPs (maDMPs) may support more automated connections between planning, research workflows, and data services. Research data support services at Finnish research organisations can provide guidance during the planning process.


### Data collection
When you start [collecting](collecting) data and need a storing environment where you can, for example, host cumulating data, [Allas Object Storage](https://research.csc.fi/-/allas) is the recommended option. Indeed, Allas is CSC’s general purpose research data storage server, which can be accessed on the CSC servers as well as from anywhere on the internet. Allas can be used both for static research data that needs to be available for analysis and to collect cumulating data. For example, if you work with sequence data, the sequencing provider can transfer the data directly to Allas under your project. However, as an object storage system, Allas is not suitable for very dynamic data like SQL databases.

Researchers can also discover and [reuse](reusing) existing datasets through services such as [Fairdata Etsin](https://etsin.fairdata.fi/) and [Research.fi](https://research.fi/en/). For restricted or sensitive datasets, access may be requested through services such as [SD Apply](https://sd-apply.csc.fi/). Together, these services support the discoverability, accessibility, and reuse of research data.

### Data processing and analysis 
For [processing](processing), [analysing](analysing) and [storing data](storage) during the research project, CSC offers several [computing platforms](https://research.csc.fi/computing). These include both environments for non-sensitive and [sensitive data](data_sensitivity). Depending on your needs, you can choose from a wide variety of computing resources: use [Chipster](https://chipster.csc.fi/) software for high-throughput data such as RNA-seq and single-cell RNA-seq, build your own custom virtual machine, or utilise the full power of our world-class supercomputers.

CSC hosts the EuroHPC supercomputer [LUMI](https://csc.fi/en/our-expertise/high-performance-computing/lumi-supercomputer/), which is available for researchers across Europe for projects requiring extreme computing capacity. LUMI is one of the world's leading supercomputers and one of the most advanced platforms for artificial intelligence.

In addition, researchers can utilise the national supercomputer [Roihu](https://csc.fi/en/our-expertise/high-performance-computing/roihu-supercomputer/) for scientific computing and data-intensive research. Roihu provides powerful resources for processing, analysing, and modelling large research datasets, as well as for AI and machine learning applications. For more flexible and customised computing environments, researchers can use Pouta cloud services. CSC’s computing services also include a wide range of [preinstalled scientific software and databases](https://research.csc.fi/bioscience-programs) and databases with usage instructions.

For management of sensitive data, the [SD Connect](https://research.csc.fi/-/sd-connect) and [SD Desktop](https://research.csc.fi/-/sd-desktop) services are available. The Sensitive Data Services are designed to facilitate collaborative research across Finland and between Finnish academics and their collaborators.  SD Connect allows you to collect, organise and share your encrypted sensitive data in a secure manner via web browser or programmatically.  SD Desktop is a service that allows a user and their authorised colleagues to access a private computing environment workspace via a web browser and analyse the data within a secure cloud. A restricted version of SD Desktop is also available for processing health and social data for secondary use in compliance with the Finnish law and Findata regulation.


### Data sharing and publishing
It is recommended to [publish](data_publication) data in data-specific repositories. You can find many options from {% tool "elixir-deposition-databases-for-biomolecular-data" %}.

For sensitive datasets requiring controlled access, CSC provides [SD Submit (pilot phase)](https://research.csc.fi/sensitive-data/sensitive-data-sd-services-for-research/), which supports the submission and publication of sensitive research data. For sensitive human biomedical data, CSC and ELIXIR-FI offer {% tool "fega" %}, the Finnish node of the European Genome-phenome Archive ({% tool "the-european-genome-phenome-archive" %}). The services support publication workflows, metadata description, and the controlled reuse of sensitive research data. 

The Finnish node of {% tool "fega" %} is part of a European network of repositories for biomedical data. Researchers remain the data controllers and decide, according to defined access policies, who can access the data for reuse. Controlled-access datasets can be discovered and accessed through appropriate authorisation procedures, supporting FAIR data principles while meeting GDPR requirements. 

In addition to the services described above, researchers can use the national [Fairdata services](https://www.fairdata.fi/en/). Fairdata IDA enables the secure storage and management of research data, including datasets intended for long-term preservation and publication. Data stored in IDA can be described using [Qvain](https://www.fairdata.fi/en/qvain/), a metadata management tool for research datasets.

Published dataset metadata becomes available through [Etsin](https://etsin.fairdata.fi/), the Finnish Research Data Finder, improving the discoverability of research data. Depending on the access rights and availability of the dataset, Etsin may provide access to the data itself or information on how to request access. Metadata from published datasets is also made available through the [Research.fi](https://research.fi/en/) portal.
