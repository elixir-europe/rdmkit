---
title: Marine Metagenomics - Norway
contributors: [Nazeefa Fatima, Espen Åberg, Nils P Willassen]
summary: Norwegian data management tool assembly for marine metagenomics data
page_tag: marine assembly
---
## What is the Norwegian tool assembly for marine metagenomics data management?
The Norwegian tool assembly for marine metagenomics aims to provide a comprehensive toolkit for management of marine genomic research data throughout a project's data life cycle. The toolkit, developed by students and researchers in Norway, contains resources and software tools for both data management ([Planning](https://rdmkit.elixir-europe.org/planning), [Processing](https://rdmkit.elixir-europe.org/processing), [Storing](https://rdmkit.elixir-europe.org/storage.html) and [Sharing](https://rdmkit.elixir-europe.org/sharing)), data [analysis](https://rdmkit.elixir-europe.org/analysing) and training. It is built on the [Norwegian e-Infrastructure for Life Sciences (NeLS)](https://rdmkit.elixir-europe.org/nels_assembly.html) tool assembly of [ELIXIR Norway](https://elixir.no/) and the [Marine Metagenomics Platform (MMP)](https://mmp2.sfb.uit.no/).

## Who can use the marine metagenomics data management tool assembly?
This tool assembly is useful for students and researchers in Norway who are interested in analysing marine datasets (e.g. genomes and metagenomes and transcriptomes). Parts of the assembly, such as data storage, are based on national infrastructures, laws and regulations, and consequently limited to Norwegian users, while other parts, such as data analysis tools and data repositories, are globally accessible.

## How can you access the marine metagenomics data management tool assembly?
To be able to use resources and tools that are mentioned here, you are recommended to have a Feide account. In addition, it is important for you to have a NeLs account in order to access [usegalaxy.no](https://usegalaxy.no/). In case your institution does not use the national Feide secure login service, you can apply for a NeLs IDP through the [ELIXIR Norway help desk](mailto:contact@bioinfo.no?subject=marine%20metagenomics). Note, that Marine Metagenomics Platform (MMP) is an open-access platform that can be accessed without a FEIDE account at [https://mmp2.sfb.uit.no/](https://mmp2.sfb.uit.no/).

## For what purpose can you use the marine metagenomics data management tool assembly?

{% include image.html file="mmp_assembly.svg" caption="Figure 1. The Marine Metagenomics data management tool assembly." alt="Diagram on tools in the Data Life Cycle in the Marine Metagenomics tool assembly." %}

### Data management planning
The support for data management planning for marine metagenomics in Norway is provided through the [ELIXIR-NO instance of the Data Stewardship Wizard](https://elixir-no.ds-wizard.org/). You can access the Data Management Plan model for marine metagenomics in Norway [here](https://elixir-no.ds-wizard.org/projects/create/custom?selected=elixir.no:marinemetagenomics-elixir-norway:0.0.2). Read more on standards and best practices for the metagenomics data life-cycle [here](https://academic.oup.com/gigascience/article/6/8/gix047/3869082). Questions regarding the DSW and data management in general can be directed to the [ELIXIR Norway help desk](mailto:contact@bioinfo.no?subject=marine%20metagenomics).

### Data collection
If you use one of the National Norwegian research infrastructures, such as the Norwegian sequencing infrastructure [NorSeq](https://www.norseq.org/), they can directly upload data to your NeLS project for you, as described in [this page](https://elixir.no/Services-bak/data_produced_NorSeq)

### Data storage, sharing and compute
The solutions for data storage, sharing and computation are built on the services and infrastructure delivered by ELIXIR Norway described in the Norwegian e-Infrastructure for Life Sciences (NeLS) [tool assembly](https://rdmkit.elixir-europe.org/nels_assembly.html). 

### Data processing and analysis
The Marine Metagenomics Portal provides a complete service for analysis of marine metagenomic data through the tool [META-pipe](https://mmp2.sfb.uit.no/metapipe/). META-pipe is a pipeline that can assemble your high-throughput sequence data, functionally annotate the predicted genes, and taxonomically profile your marine metagenomics samples, helping you to gain insight into the phylogenetic diversity, metabolic and functional potential of environmental communities. You can find more details about META-pipe [here](https://www.ncbi.nlm.nih.gov/labs/pmc/articles/PMC6480938/). Norwegian users with Feide access can access the online version of META-pipe. For other users META-pipe is [downloadable](https://gitlab.com/uit-sfb/metapipe) and can easily be run on any computing environment (e.g. any Linux workstation, SLURM cluster	 or Kubernetes).

[Usegalaxy.no](https://usegalaxy.no/) is a Norwegian instance of the [Galaxy](https://wiki.galaxyproject.org/) web-based platform for data intensive life science research that provides users with a unified, easy-to-use graphical interface to a host of more than 200 different analysis tools. Here you can find tools for a wide variety of analysis for your marine metagenomic and genomic data. The tools are publicly available in the [Galaxy Toolshed](https://toolshed.g2.bx.psu.edu/) which serves as an "appstore" so you can easily transfer them to your favourite Galaxy instance anywhere. You can run the tools interactively, one by one, or combine them into multi-step workflows that can be executed as a single analysis. Premade workflows (i.e for Taxonomic classification of metagenomic sequences) are provided, and you can request installation of your favourite tool by contacting the [ELIXIR Norway help desk](mailto:contact@bioinfo.no?subject=marine metagenomics).

### Data sharing and publishing
ELIXIR Norway acts as a [broker for Norwegian end-users](https://elixir.no/news/52/63/ELIXIR-Norway-broker-data-to-ENA) that wish to submit data to [ELIXIR Deposition Databases](https://elixir-europe.org/platforms/data/elixir-deposition-databases#:~:text=ELIXIR%20Deposition%20Database%20list%20%20%20%20Deposition,%20%20%20%208%20more%20rows%20) (such as ENA), providing support in submitting the data on behalf of the data owners directly from the National e-infrastructure for Life Science (NeLS).

If you need help with publishing or are interested in using the brokering service, please contact the [ELIXIR Norway help desk](mailto:contact@bioinfo.no?subject=marine%20metagenomics).

### Data reuse
The [Marine Metagenomics Portal (MMP)](https://mmp2.sfb.uit.no/) provides you with high-quality curated and freely accessible microbial genomics and metagenomics resources. Through MMP you can access the The [Marine reference databases (MarRef)](https://mmp2.sfb.uit.no/marref/), [Marine Genome Database (MarDb)](https://mmp2.sfb.uit.no/mardb/), [(MarFun)](https://mmp2.sfb.uit.no/marfun/), and [(SalDB)](https://mmp2.sfb.uit.no/saldb/) contextual databases. They are built by aggregating data from a number of publicly available sequence, taxonomy and literature databases in a semi-automatic fashion. Other databases or resources such as bacterial diversity and culture collections databases, web mapping service and ontology databases are used extensively for curation of metadata. At present the MarRef contains nearly 1,000 complete microbial genomes, and MarDB hosts more than 13,000 non-complete genomes. The MAR database entries are cross-referenced with ENA and the [World Register of Marine Species (WoRMS)](http://marinespecies.org/). You can read more about the Mar databases [here](https://pubmed.ncbi.nlm.nih.gov/29106641/).

## Where can I find training materials, documentations and events about the Marine Metagenomics data management tool assembly?
In ELIXIR's training portal TeSS you can discover the latest [training events](https://tess.elixir-europe.org/events) and [materials](https://tess.elixir-europe.org/materials) using for instance [“marine metagenomics”](https://tess.elixir-europe.org/search?utf8=%E2%9C%93&q=marine+metagenomics) or [data management planning](https://tess.elixir-europe.org/search?utf8=%E2%9C%93&q=data+management+planning) as queries. Norwegian users can have a look at ELIXIR Norways [training pages](https://elixir.no/training/material).

You can access previous [workshop materials](https://elixir.mf.uni-lj.si/course/index.php?categoryid=16) on these topics in the [ELIXIR-SI eLearning Platform (EeLP)](https://elixir.mf.uni-lj.si/).

