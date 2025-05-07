---
title: Marine Metagenomics
contributors: [Nazeefa Fatima, Espen Åberg,  Nils Peder Willassens]
description: The Marine Metagenomics tool assembly aims to provide a comprehensive data management toolkit of marine genomics researchers in Norway.
page_id: marine_assembly
affiliations: [ELIXIR Europe, "NO"]
related_pages:
  your_tasks: [dmp, existing_data, data_organisation, storage, data_publication, data_transfer, metadata, data_analysis]
  your_domain: [marine]
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=marine+metagenomics
  - name: ELIXIR Norways training pages
    url: https://elixir.no/training/material
  - name: Workshop materials on ELIXIR-SI eLearning Platform (EeLP)
    url: https://elixir.mf.uni-lj.si/course/index.php?categoryid=16  
---

## What is the Norwegian tool assembly for marine metagenomics data management?
The Norwegian tool assembly for marine metagenomics aims to provide a comprehensive toolkit for management of marine genomic research data throughout a project's data life cycle. The toolkit, developed by students and researchers in Norway, contains resources and software tools for both data management ([Planning](planning), [Processing](processing), [Storing](storage) and [Sharing](sharing)), data [analysis](analysing) and training. It is built on the [Norwegian e-Infrastructure for Life Sciences (NeLS)](nels_assembly) tool assembly of [ELIXIR Norway](https://elixir.no/) and the [Marine Metagenomics Platform (MMP)](https://sfb.mmp2.sigma2.no).

## Who can use the marine metagenomics data management tool assembly?
This tool assembly is useful for students and researchers, in Norway, who are interested in analysing marine datasets (e.g. genomes, metagenomes, and transcriptomes). Parts of the assembly, such as data storage, are based on national infrastructures, laws and regulations, and consequently limited to Norwegian users, while other parts, such as data analysis tools and data repositories, are globally accessible.

## How can you access the marine metagenomics data management tool assembly?
To be able to use resources and tools that are mentioned here, you are recommended to have a [Feide account](https://www.feide.no/). In addition, it is important for you to have a NeLs account in order to access [usegalaxy.no](https://usegalaxy.no/). In case your institution does not use the national Feide secure login service, you can apply for a NeLs IDP through the [ELIXIR Norway help desk](mailto:contact@bioinfo.no?subject=marine%20metagenomics). Note, that Marine Metagenomics Platform (MMP) is an open-access platform that can be accessed without a Feide account at [https://mmp2.sfb.uit.no/](https://sfb.mmp2.sigma2.no).

## For what purpose can you use the marine metagenomics data management tool assembly?

{% include image.html file="mmp_assembly.svg" caption="Figure 1. The Marine Metagenomics data management tool assembly." alt="Diagram on tools in the Data Life Cycle in the Marine Metagenomics tool assembly." %}

### Data management planning
The support for data management planning and the Data Management Plan model for marine metagenomics in Norway is provided through the [ELIXIR-NO instance of the Data Stewardship Wizard](https://elixir-no.ds-wizard.org/projects/create/custom?selected=elixir.no:marinemetagenomics-elixir-norway:0.0.2). To read more on standards and best practices for the metagenomics data life-cycle, we refer you to a [publication for further reading](https://academic.oup.com/gigascience/article/6/8/gix047/3869082). Questions regarding the DSW and data management in general can be directed to the [ELIXIR Norway helpdesk](mailto:contact@bioinfo.no?subject=marine%20metagenomics).

### Data collection
If you use one of the National Norwegian research infrastructures, such as the Norwegian sequencing infrastructure [NorSeq](https://www.norseq.org/), they can directly upload data to your NeLS project for you, as described in [this page](https://elixir.no/Services-bak/data_produced_NorSeq)

### Data storage, sharing and compute
The solutions for data storage, sharing and computation are built on the services and infrastructure delivered by ELIXIR Norway described in the Norwegian e-Infrastructure for Life Sciences (NeLS) [tool assembly](nels_assembly). 

### Data processing and analysis
The {% tool "marine-metagenomics-portal" %} provides a complete service for analysis of marine metagenomic data through the tool [META-pipe](https://sfb.mmp2.sigma2.no/metapipe/). META-pipe is a pipeline that can assemble your high-throughput sequence data, functionally annotate the predicted genes, and taxonomically profile your marine metagenomics samples, helping you to gain insight into the phylogenetic diversity, metabolic and functional potential of environmental communities. You can read more [details about META-pipe in the publication](https://www.ncbi.nlm.nih.gov/labs/pmc/articles/PMC6480938/). Norwegian users with Feide access can access the online version of META-pipe. For other users META-pipe is [downloadable](https://gitlab.com/uit-sfb/metapipe) and can easily be run on any computing environment (e.g. any Linux workstation, SLURM cluster or Kubernetes).

[Usegalaxy.no](https://usegalaxy.no/) is a Norwegian instance of the {% tool "galaxy" %} web-based platform for data intensive life science research that provides users with a unified, easy-to-use graphical interface to a host of more than 200 different analysis tools. Here, you can find tools for a wide variety of analysis for your marine metagenomic and genomic data. The tools are publicly available in the [Galaxy Toolshed](https://toolshed.g2.bx.psu.edu/) which serves as an "appstore" so you can easily transfer them to your favourite Galaxy instance anywhere. You can run the tools interactively, one by one, or combine them into multi-step workflows that can be executed as a single analysis. Premade workflows (i.e for Taxonomic classification of metagenomic sequences) are provided, and you can request installation of your favourite tool by contacting the [ELIXIR Norway help desk](mailto:contact@bioinfo.no?subject=marine metagenomics).

### Data sharing and publishing
ELIXIR Norway acts as a [broker for Norwegian end-users](https://elixir.no/news/52/63/ELIXIR-Norway-broker-data-to-ENA) that wish to submit data to {% tool "elixir-deposition-databases-for-biomolecular-data" %} (such as ENA), providing support in submitting the data on behalf of the data owners directly from the National e-infrastructure for Life Science (NeLS).

If you need help with publishing or are interested in using the brokering service, please contact the [ELIXIR Norway help desk](mailto:contact@bioinfo.no?subject=marine%20metagenomics).

### Data reuse
The {% tool "marine-metagenomics-portal" %} provides you with high-quality curated and freely accessible microbial genomics and metagenomics resources. Through MMP you can access the The Marine reference databases ({% tool "marref" %}), Marine Genome Database({% tool "mardb" %}), database for marine fungi genomes ({% tool "marfun" %}), and salmon specific database of genome sequenced prokaryotes({% tool "saldb" %}) databases. They are built by aggregating data from a number of publicly available sequences, taxonomy and literature databases in a semi-automatic fashion. Other databases or resources such as bacterial diversity and culture collections databases, web mapping service and ontology databases are used extensively for curation of metadata. At present the {% tool "marref" %} contains nearly 1000 complete microbial genomes, and {% tool "mardb" %} hosts more than 13,000 non-complete genomes. The MAR database entries are cross-referenced with ENA and the [World Register of Marine Species](https://www.marinespecies.org) - you can read the [publication about the Mar databases](https://pubmed.ncbi.nlm.nih.gov/29106641/).
