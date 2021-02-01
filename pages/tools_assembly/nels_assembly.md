---
title: Nels assembly 
contributors: [Korbinian Bösl, Erik Hjerde]
summary: This is an example of a Data Management tool assembly, NeLS as an infrastructure is funded and aimed for researchers in Norway and their collaborators.
---

## What is the NeLS data management tool assembly?

The [Norwegian e-Infrastructure for Life Sciences (NeLS)](https://nels.bioinfo.no/) is an infrastructure provided by [ELIXIR Norway](https://elixir.no/). NeLS provides necessary tools for Data Management and covers [Planning](planning), [Processing](processing), [Analysing](analysing) and [Sharing](sharing) Data Life Cycle stages and offers [Data Storage](storage) capacities.

## Who can use the NeLS data management tool assembly?

NeLS and the underlying infrastructure are accessible for researchers in Norway and their collaborators. Eligible researchers can apply for storage quotas and get support through the National (Norwegian) bioinformatics support desk [contact@bioinfo.no](mailto:contact@bioinfo.no).  Most of the tools in NeLS are open source and can be reused.



## For what can you use the NeLS data management tool assembly?

{% include image.html file="NeLS_toolkit.svg" caption="Figure 1. The Norwegian e-Infrastructure for Life Sciences (NeLS) Data Management tool assembly." alt="NeLS RDMKit" %}

You can access all tools in NeLS using the the national solution for secure login and data sharing in the educational and research sector [FEIDE](https://www.feide.no/), when coupled with [ELIXIR AII](https://elixir-europe.org/services/compute/aai).
The NeLS Data Management tool assembly can support you with [Data Management Planning](planning) through an [instance of the Data Steward Wizard](https://elixir-no.ds-wizard.org) with a dedicated knowledge model referring to national infrastructure, resources, laws and regulations. Soon you will be able to submit storage request forms for [Data Storage](storage) in NeLS with defined access roles through the Data Steward Wizard.

[Data Storage](storage) is the core of the NeLS and builds upon a 3 layer tiered storage system: The first layer is intended for short term storage during computing, processing and analyse steps; the second layer of medium capacity (NeLS) is intended for sharing and storage of active research data, while the third layer (StoreBioinfo) of high capacity is intended for longer storage until end of a project.
Data in the second (NeLS) layer is protected against hardware failure on disk or server level and snapshots of the data are kept for 4 weeks. The third layer is implemented on top of the national research data storage solutions offered by Sigma2 Uninett A/S and is protected against data loss by snapshots and geo-replication.
National Norwegian research infrastructures, such as the Norwegian sequencing infrastructure [NorSeq](https://www.norseq.org/) can directly upload data to your NeLS project for you. 

For [Processing](processing) and [Analysing](analysing) your data, the NeLS Data Management tool assembly provides access to a national [instance of Galaxy](https://usegalaxy.no) with ~2000 tools.
Data stored in NeLS is directly available within this Galaxy instance, hence you do not need to keep local copies of your data.
 
In order to help you to keep track of metadata NeLS has been integrated with the [SEEK](https://seek4science.org/) web-based cataloguing and sharing platform. You can use any instance of SEEK such as the [FAIRDOMHub](https://fairdomhub.org/) to [manage metadata](metadata_management) associated with your data stored in NeLS and access the data through SEEK. SEEK uses the ISA (Investigation, Study, Assay) structure to structure your data and recommended minimal information such as sample characteristics, technologies, measurements and relationships between samples, data and models. Public SEEK instances like the [FAIRDOMHub](https://fairdomhub.org/) can also be used to collaborate on data and to [share](sharing) them publicly. If you are doing modelling you can also use the inbuilt [JWS Online](jjj.mib.ac.uk) simulator for your SBML models.
 
One good way to share your data is to deposit them in the [ELIXIR Deposition Databases for Biomolecular Data](https://elixir-europe.org/platforms/data/elixir-deposition-databases). The NeLS Data Management tool assembly will soon offer tools to help you with the deposition step for data stored in NeLS.

## External links

Technical article about [Norwegian e-Infrastructure for Life Sciences (NeLS)](https://doi.org/10.12688/f1000research.15119.1)

[Norwegian e-Infrastructure for Life Sciences (NeLS)](https://nels.bioinfo.no/) 

[Data Steward Wizard for Life Scientist in Norway](https://elixir-no.ds-wizard.org)

[usegalaxy.no](https://usegalaxy.no)

[FEIDE](https://www.feide.no/)

[ELIXIR AII](https://elixir-europe.org/services/compute/aai)

[FAIRDOMHub](https://fairdomhub.org/)

[SEEK](https://seek4science.org/)

[JWS Online](jjj.mib.ac.uk)

[ELIXIR Deposition Databases for Biomolecular Data](https://elixir-europe.org/platforms/data/elixir-deposition-databases)

## Where can I find training materials and events about the NeLS data management tool assembly?

{% include tess.html search="Norway" %}


## What tools are used within the NeLS data management tool assembly?

{% include toollist.html tag="nels" %}
