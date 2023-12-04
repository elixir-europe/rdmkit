---
title: NeLS
contributors: [Korbinian Bösl, Federico Bianchini, Erik Hjerde]
description: NeLS provides the necessary tools for data management to researchers in Norway and their collaborators.
page_id: nels
affiliations: ["ELIXIR Europe", "NO"]
related_pages: 
  your_tasks: [dmp, data_organisation, storage, data_publication, data_transfer, metadata]
  your_domain: []
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=norway
---

## What is the NeLS data management tool assembly?

The [Norwegian e-Infrastructure for Life Sciences (NeLS)](https://nels.bioinfo.no/) is an infrastructure provided by [ELIXIR Norway](https://elixir.no/). [NeLS](https://doi.org/10.12688/f1000research.15119.1) provides necessary tools for Data Management and covers [Planning](planning), [Processing](processing), [Analysing](analysing) and [Sharing](sharing) Data Life Cycle stages and offers [Data Storage](storage) capacities.

## Who can use the NeLS data management tool assembly?

NeLS and the underlying infrastructure are accessible to researchers in Norway and their collaborators. Eligible researchers can apply for storage quotas and get support through the National (Norwegian) bioinformatics support desk [contact@bioinfo.no](mailto:contact@bioinfo.no). Most of the tools in NeLS are open-source and can be reused.



## For what can you use the NeLS data management tool assembly?

{% include image.html file="NeLS_toolkit.svg" caption="Figure 1. The Norwegian e-Infrastructure for Life Sciences (NeLS) Data Management tool assembly." alt="NeLS RDMkit" %}

You can access all tools in NeLS using the national solution for secure login and data sharing in the educational and research sector [FEIDE](https://www.feide.no/) when coupled with {% tool "life-science-login" %}.
The NeLS Data Management tool assembly provides support with [Data Management Planning](planning) through an [instance of the Data Steward Wizard](https://elixir-no.ds-wizard.org) following the guidelines of the major national and European funding bodies. Dedicated references guide you through national infrastructure, resources, laws and regulations and also include the {% tool "tryggve-elsi-checklist" %} for Ethical, Legal and Social Implications. Soon you will be able to submit storage request forms for [Data Storage](storage) in NeLS with defined access permissions through the Data Stewardship Wizard.

[Data Storage](storage) is the core functionality of NeLS and builds upon a 3 layer-tiered system: the first layer is intended for short-term storage when computing, processing and analysing data; the second layer of medium capacity (NeLS) is intended for sharing and storing active research data, while the third layer (StoreBioinfo) of high capacity is intended for longer storage until the end of a project.
Data in the second (NeLS) layer is protected against hardware failure on disk or server level and snapshots of the data are kept for 4 weeks. The third layer is implemented on top of the national research data storage solutions operated by Sigma2 Uninett A/S and is protected against data loss by snapshots and geo-replication.
National Norwegian research infrastructures, such as the Norwegian sequencing infrastructure [NorSeq](https://www.norseq.org/) can directly upload data to your NeLS project for you.

For [Processing](processing) and [Analysing](analysing) your data, the NeLS Data Management tool assembly provides access to a national [instance of Galaxy](https://usegalaxy.no) with ~2000 tools.
Data stored in NeLS is directly available within this Galaxy instance, hence you do not need to keep local copies of your data.
 
In order to help you keep track of metadata, NeLS is integrated with the {% tool "fairdom-seek" %} web-based cataloguing and sharing platform. You can use any instance of FAIRDOM-SEEK such as the public {% tool "fairdomhub" %} to [manage metadata](metadata_management) associated with your data stored in NeLS and access the data through FAIRDOM-SEEK. FAIRDOM-SEEK uses the ISA (Investigation, Study, Assay) structure to organise your data and recommended minimal information such as sample characteristics, technologies, measurements and relationships between samples, data and models. Public FAIRDOM-SEEK instances like the {% tool "fairdomhub" %}  can also be used to collaborate on data and to [share](sharing) them publicly. If you are doing modelling, you can also use the inbuilt {% tool "jws-online" %} simulator for your SBML models.
 
One recommended way to share your data is to deposit them in the {% tool "elixir-deposition-databases-for-biomolecular-data" %}. The NeLS Data Management tool assembly will soon offer tools to help you with the deposition step for data stored in NeLS.
