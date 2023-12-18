---
title: FAIRtracks
contributors: [Federico Bianchini, Sveinung Gundersen]
description: The FAIRtracks ecosystem provides technical solutions for the FAIRification of genome browser track files
page_id: fairtracks
affiliations: ["NO", "ES", "EMBL-EBI"]
related_pages: 
  your_tasks: [data_publication, data_transfer, metadata]
  your_domain: [human_pathogen_genomics, plants]
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=fairtracks
---

## What is the FAIRtracks tool assembly?

The [FAIRtracks ecosystem](https://fairtracks.net/) is a set of services associated with a "minimum information"
[metadata standard](https://fairtracks.net/standards/#standards-01-fairtracks) for
[genomic tracks](https://fairtracks.net/tracks/#tracks-01-genomic-tracks)
implemented as a [set of JSON Schemas](https://github.com/fairtracks/fairtracks_standard/tree/master/json/schema).
The FAIRtracks ecosystem is developed and provided as part of the national Service Delivery Plans by
[ELIXIR Norway](https://elixir.no/) and [ELIXIR Spain](https://elixir-europe.org/about-us/who-we-are/nodes/spain),
and is supported by the [Track Hub Registry group](https://trackhubregistry.org/) at [EMBL-EBI](https://www.ebi.ac.uk/).
FAIRtracks is endorsed by [ELIXIR Europe](https://elixir-europe.org/) as a
[Recommended Interoperability Resource](https://elixir-europe.org/platforms/interoperability/rirs).

In the context of the Data Life Cycle and its stages, the FAIRtracks ecosystem covers [Collecting](collecting), [Processing](processing),
[Analysing](analysing), [Sharing](sharing), and [Reusing](reusing). It has to be noted, however, that the FAIRtracks ecosystem operates
on derived/secondary data and not on the raw sequencing data, as illustrated in Figure 1.
Sequencing data needs to be handled independently following domain best practices
(see e.g. the pages on [Human pathogen genomics](human_pathogen_genomics) or [Plant sciences](plant_sciences) ).

{% include image.html file="fairtracks-rdmkit-tool-assembly.png" caption="Figure 1. The FAIRtracks tool assembly and the associated workflow."
alt="FAIRtracks RDMkit" %}

## Who can use the FAIRtracks tool assembly?

The FAIRtracks ecosystem is available to everyone.
Distinct services are hosted on different platforms which might require authentication procedures which are not handled centrally by FAIRtracks.
Most of the services are accessible through Application Programming Interfaces (APIs). More details are provided in the description below.
Users of the FAIRtracks ecosystem belong to different categories, which could be summarised as:

- Researchers and data analysts
- Data providers and biocurators
- Developers working on tooling for
  - Research
  - Implementation of the FAIR data principles

Each of these categories benefits specifically from a subset of the global ecosystem.
The core services can be accessed both upstream (for data providers and biocurators) and downstream (for tool developers and analytical end users).

## For what can you use the FAIRtracks tool assembly?

The FAIRtracks tool assembly can be used for a large number of applications; we summarise the main ones below following the steps of the data life-cycle
and focusing on particular tools. 

While the assembly does not include a tool for [Data Management Planning](dmp),
the FAIRtracks metadata standard is registered in {%tool "fairsharing" %}
and, thus, formally connected to several other standards and databases.
The FAIRtracks standard can, thus, be selected on your Data Management Plan in all the instances of {% tool "data-stewardship-wizard" %} through
the integration with FAIRsharing. 

{%tool "omnipy" %} is a high-level Python library for type-driven data wrangling and scalable workflow orchestration;
it is a very important self-standing subset of the FAIRtracks ecosystem covering several steps in the data life-cicle.
It can be used to extract metadata from specific portals, doubling up on the [data Collection](collecting)
capabilities of TrackFind, and to [process](processing) metadata entries to uniform them to a unique standard.
Omnipy workflows are defined as transformations from specific input data models to specific output data models.
Input and output data are validated at each iteration through parsing based on {%tool "pydantic" %}.
Offloading of workflows to external compute resources is provided through the integration of Omnipy with a
workflow engine based on {%tool "prefect" %}.

There is ongoing work into adding {%tool "prefect" %} as one of the services available in the
[National Infrastructure for Research Data (NIRD) service platform](https://www.sigma2.no/nird-service-platform).
This would enable running {%tool "omnipy" %} on data and metadata stored in the [NIRD data storage](https://www.sigma2.no/data-storage).
Refer also to the [Norwegian national page](no_resources) for more details. Note that, while the usage of NIRD storage and services
is certainly convenient for Norwegian users, this is not a central or mandatory part of the tool assembly which is born as an international
service and aims at maintaining this status.

Data [sharing](sharing) and preservation is one of the key components of the FAIRtracks ecosystem.
Since genomic annotations (tracks) typically consist of secondary data files referring to primary data sources,
they are often deposited together with the primary data. The aim of the minimal information metadata model is to
offer a greater level of granularity, providing each track with an identifier and enabling the possibility of analysis across datasets
in a semi-automatised fashion. In order to accomplish this a dedicated registry would be required. Given that this tool does not yet exist,
the current recommendation is to deposit FAIRtracks-compliant metadata files to {%tool "zenodo" %},
as this platform supports both Digital Object identifier (DOI) versioning and DOI reservation before publication.
The identifiers on the metadata FAIRtracks object are then cross-linked with the actual data which is hosted
e.g. in a [Track Hub](https://genome.ucsc.edu/goldenPath/help/hgTrackHubHelp.html) and registered in
the {%tool "track-hub-registry" %}.

Data and metadata organised in this fashion can then be collected for [reuse](reusing) using {%tool "trackfind" %},
a search and curation engine for genomic tracks.
{%tool "trackfind" %} supports crawling of the {%tool "track-hub-registry" %} and other data portals to fetch track metadata,
that can be accessed through hierarchical browsing or by search queries both through a web-based user interface and as a RESTful API.
TrackFind supports advanced SQL-based queries that can be easily built into the user interface.

Additional tools that comprise the core of the FAIRtracks ecosystem are the
[metadata validation](https://fairtracks.net/services/?category=Core%20services&tags%5B0%5D=Metadata%20validation) and the
[metadata augmentation](https://fairtracks.net/services/?category=Core%20services&tags%5B0%5D=Metadata%20augmentation) services.
The former is REST API that extends the standard JSON Schema validation technology through additional modules allowing for:

* validation of ontology terms against specific ontology versions;
* checking Compact Uniform Resource Identifiers (CURIEs) against the registered entries at {%tool "identifiers-org" %};
* checking restrictions on a full set of documents, e.g. whether identifiers are unique and whether the records referred to by foreign keys exist.

The [FAIRtracks augmentation service](https://fairtracks.net/services/?category=Core%20services&tags%5B0%5D=Metadata%20augmentation)
is implemented as a REST API that expands on the information contained in a minimal FAIRtracks JSON by adding
a set of fields with human-readable values. These include ontology labels and versions, summaries, and other relevant fields.
This service bridges the gap between data providers, which are required to submit only minimal information, and data consumers
who require richer information for data discovery and retrieval.
