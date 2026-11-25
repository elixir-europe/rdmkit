---
title: IFB
contributors: [Saliha Zenboudji-Beddek, Jean-François Dufayard, Olivier Collin, Marie-Christine Jacquemot, Paulette Lieby, Flora D'Anna, Anne-Françoise Adam-Blondon, Morgane Thomas-Chaullier]
editors: [Korbinian Bösl, Bert Droesbeke, Flora D'Anna]
description: The French Bioinformatics Institute (IFB) offers IT infrastructure and bioinformatics expertise to support researchers in Life Sciences.
page_id: ifb
supported_by: ["ELIXIR Europe", "FR"]
related_pages: 
  Your_tasks: [dmp, data_organisation, storage, data_publication, transfer, metadata, data_analysis]
  Your_domain: []
training:
  - name: IFB/ELIXIR-FR Search query in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=IFB
  - name: The IFB/ELIXIR-FR training materials on RDM in Tess
    registry: TeSS
    url: https://tess.elixir-europe.org/materials?content_provider=IFB+French+Institute+of+Bioinformatics&q=RDM
  - name: IFB/ELIXIR-FR training courses
    url: https://www.ifb-elixir.fr/en/trainings/i-am-looking-for-training/
  - name: FAIR principles in bioinformatics and data management
    url: https://moodle.france-bioinformatique.fr/course/index.php?categoryid=2&lang=fr
  - name: Doranum, the french national resources to support the scientific community for data management and sharing(in French)
    url: https://doranum.fr
Resources:
  - name: Documentation for the IFB/ELIXIR-FR core cluster
    URL: https://ifb-elixirfr.gitlab.io/cluster/doc/
  - name: Documentation for the Biosphere cloud federation
    URL: https://ifb-elixirfr.github.io/biosphere/
  - name: Data management training at the IFB
    URL: https://www.france-bioinformatique.fr/en/training/
  - name: Simplified Guide: Research Data Management for Project Leaders (in French)
    url: https://hal.inrae.fr/hal-03204351v2/file/2024-qualinous-cycle-de-vie-v1.pdf
---

## What is the IFB data management tool assembly?

[IFB/ELIXIR-FR](https://www.ifb-elixir.fr/) develops an infrastructure that supports Life science data management all along the data life cycle. IFB/ELIXIR-FR benefits from and contributes to both the ELIXIR’s [RDM community](https://elixir-europe.github.io/ds-handbook/mm-data-dmp) and Recherche Data Gouv [Recherche.Data.Gouv](https://recherche.data.gouv.fr/en), the French National ecosystem supporting research data management.


## Who can use the IFB/ELIXIR-FR data management tool assembly?

The IFB/ELIXIR-FR infrastructure for Life science data is accessible to the French research community (researchers, engineers, technicians and students)  and their international collaborators. 


## How to use the IFB/ELIXIR-FR data management tool assembly ?

An overview of the IFB/ELIXIR-FR services supporting Open Science and FAIR data management is available on the [Open Science page](https://www.ifb-elixir.fr/en/services/open-science/). To access the computing resources,  users can request an account through the [computing infrastructure page](https://www.ifb-elixir.fr/en/services/computing-infrastructure/). For any other requests,  they can contact IFB/ELIXIR-FR to get support through the dedicated [help pages](https://www.ifb-elixir.fr/en/contact/). As well, it is recommended to contact IFB/ELIXIR-FR during the project’s planning phase to discuss details, as fees may apply based on resource usage.


## Which steps and tools are contained in the IFB data management tool assembly?

{% include image.html file="fr_ifb_assembly_update.svg" caption="Figure 1. The French Bioinformatics Institute (IFB) tool assembly." alt="IFB RDMkit" %}

### Data management planning

IFB/ELIXIR-FR recommends [DMP-OPIDoR](https://dmp.opidor.fr) (supported by French research bodies) or {% tool "data-stewardship-wizard" %} as tools for writing a Data Management Plan (DMP).

DMP-Opidor is hosted and maintained at INIST-CNRS and tailored to the needs of the French research community. Its machine-actionable format is fully compliant with the RDA DMP Common Standard and covers both data and software management within a single plan.

IFB/ELIXIR-FR hosts its own instance [DSW@IFB](https://dsw.france-bioinformatique.fr/wizard/dashboard), freely accessible to the french research community. It has co-developed with the other National Research Infrastructures in Biology and Health ([INBS](https://www.ibisa.net/inbs/)) a multidisciplinary DMP model for core facilities, covering bioimaging, genomics, proteomics, cytometry and metabolomics.


### Data collection

IFB/ELIXIR-FR facilitates data and [metadata collection](https://rdmkit.elixir-europe.org/collecting) through [madbot](https://madbot.france-bioinformatique.fr/), a software that stores metadata along with links to the data in their storage place during the project. Storage capacities are provided by IFB/ELIXIR-FR’s National Network of Computing Resources [NNCR](https://nncr-clusters.france-bioinformatique.fr/). 

To support data collection along with standard metadata, IFB/ELIXIR-FR is providing [{% tool "fairdom-seek" %}](https://seek4science.org/) instance which is available at [GenOuest](https://research-sharing.cesgo.org) core facility. 

### Data processing and analysis 

IFB/ELIXIR-FR infrastructure gives access to several types of computing resources, according to needs and expertise of the users:

* Several high-performance computing [clusters](https://www.ifb-elixir.fr/en/services/computing-infrastructure/ifb-clusters/). 
* The [Galaxy France](https://usegalaxy.fr) portal operated by IFB/ELIXIR-FR members in complement of the [Galaxy Europe](https://usegalaxy.eu). 
* The cloud federation [Biosphere](https://biosphere.france-bioinformatique.fr). A list of the different appliances is available on the [RainBio catalogue](https://biosphere.france-bioinformatique.fr/catalogue/). 

Each of the computing resources offers its own storage solution tailored for the needs of the users (fast access, capacitive).

IFB/ELIXIR-FR core facilities can also assist or perform bioinformatics analyses of the user’s data. Most IFB/ELIXIR-FR core facilities can provide [expertise](https://www.ifb-elixir.fr/en/services/data-analysis/) for data analysis in several domains (genomics, metagenomics, transcriptomics, phenomics, metabolomics...) as well as software development. More generally, a list of tools developed by French teams is available [here](https://www.ifb-elixir.fr/en/services/tools-services-catalog/). 

For bioimage analysis, researchers can explore {% tool "biii" %}, the BioImage Informatics Index. Biii is a community-driven registry that catalogues bioimage analysis software, workflows, training resources and example datasets.

### Data sharing and publishing
 In France, providing access to public research data is mandatory. It is advised to publish such data in dedicated repositories. IFB/ELIXIR-FR encourages researchers to browse the list of  {% tool "elixir-deposition-databases-for-biomolecular-data" %} and the {% tool "elixir-core-data-resources" %} to identify the appropriate repository for their data type. In addition, a list of [trusted repositories](https://recherche.data.gouv.fr/en/repositories) is maintained by Recherche Data Gouv.

 IFB/ELIXIr-FR members contribute to domain-specific thematic repositories hosted in France: - {% tool "imgt" %} and - {% tool "orphadata-science" %}.

 For the semantic annotation of data, software and services, IFB/ELIXIR-FR recommends the use of {% tool "edam" %}, a comprehensive ontology of bioinformatics operations, data types, formats and topics. To ensure that published data are findable and citable, IFB/ELIXIR-FR promotes the attribution of persistent identifiers through {% tool "datacite" %}.

 Research software produced in life science projects can be preserved and shared through {% tool "software-heritage" %}, the global archive of software source code. 

 The French scientific community can publish its data in the [Recherche.Data.Gouv](https://recherche.data.gouv.fr/en) repository, a [national multidisciplinary repository](https://recherche.data.gouv.fr/en/page/recherche-data-gouv-repository) based on Dataverse,only if thematic repository doesn’t exist for one discipline. Support is available from [thematic reference centres](https://recherche.data.gouv.fr/en/page/thematic-reference-centers-providing-expertise-for-individual-scientific-fields) providing domain-specific expertise, and from [regional data management clusters](https://recherche.data.gouv.fr/en/data-management-cluster) offering local support. IFB/ELIXIR-FR is also the [reference centre for Life Science](https://recherche.data.gouv.fr/fr/page/institut-francais-de-bioinformatique-ifb). 

### Compliance monitoring & measurement

IFB/ELXIIR-FR promotes the implementation of FAIR principles. To this end, IFB/ELIXIR-FR provides and encourages the use of [FAIR-Checker](https://fair-checker.france-bioinformatique.fr/), a web service aimed at assenssing and monitoring FAIRness levels of online digital resources. This tool also relies on metadata profiles (mandatory/recommended/optional) such as Bioschemas or Datacite to evaluate metadata completeness. 
