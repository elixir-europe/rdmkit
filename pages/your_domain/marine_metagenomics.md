---
title: Marine metagenomics
description: Data management solutions for marine metagenomics data
contributors: [Nils Peder Willassen,Anastasis Oulas,Evangelos Pafilis]
related_pages: 
page_id: marine
related_pages: 
  your_tasks: [metadata]
  tool_assembly: [marine assembly]
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=marine%20metagenomics
---

## Introduction

The marine metagenomics domain is characterized by large datasets that require access to substantial [storage](storage) and High-Performance Computing (HPC) for running complex and memory-intensive [analysis](analysing) pipelines, and therefore are difficult to handle for typical end-users and beyond the resources of many service providers. With respect to [sharing](sharing) metagenomics datasets in compliance with the FAIR principles, so that they can be [reused](reusing), it hinges entirely on recording rich metadata about all the steps from sampling to data analysis.

## Managing marine metagenomic metadata
 
### Description
Metagenomics is a highly complex process the encompasses several steps including: sampling, isolation of DNA, generation of sequencing libraries, sequencing, pre-processing of raw data, taxonomic and functional profiling using reads, assembly, binning, refinement of bins, generation of MAGs, taxonomic classification of MAGs, and archiving of raw or processed data. To comply with the FAIR principles, you need to collect metadata about all these steps.

Moreover, in marine metagenomics, it is also necessary to characterize the marine environment of the sample, including geolocation, and the physico-chemical properties of the water.

### Solutions
- As a starting point to get acquainted with the intricacies of reporting marine metagenomics experiments, the following publications are recommended reading: 
  - [The metagenomic data life-cycle: standards and best practices](https://doi.org/10.1093/gigascience/gix047) which describes the metagenomics data life-cycle in detail.
  - [Marine microbial biodiversity, bioinformatics and biotechnology (M2B3) data reporting and service standards](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4511511/), guided by marine microbial research, and providing clear examples and colour-coded illustrations.
- Metadata standards that apply to marine metagenomics data are the [Genome Standards Consortium](https://gensc.org/) family of minimum information standards, including the core standard, [Minimum Information about any (x) Sequence (MIxS)](https://gensc.org/mixs/), the derived [Minimum Information about (Meta)genome Sequence (MIGS/MIMS)](https://gensc.org/mixs/), and the also derived [Minimum Information About a Metagenome-Assembled Genome (MIMAG)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6436528/) that is presently only available as a scientific publication. 

## Tools and resources for analyzing metagenomics datasets

### Description
The field of marine metagenomics has been in rapid expansion, with many statistical/computational tools and databases developed to explore the huge influx of data. You need to be able to choose between the multiple bioinformatics techniques, tools, and methodologies available for performing each step of a typical metagenomics  analysis, while ensuring that your choice conforms to the best practices for the domain. Moreover you need access to HPC facilities with capacity to execute the analysis and store the resulting data, and therefore should be aware of what computing infrastructures are available to you (and at what cost).

### Considerations 
- Are there particular characteristics of your dataset that would restrict the choice of applicable tools?
- Are the recommended tools freely available?
  - If not, can you afford the software licensing cost?
  - If not, are there freely available alternatives?
- Does your institution have its own HPC facilities, and what are the access conditions?
- Does your country have a research HPC infrastructure, and what are the access conditions?

### Solutions
- Experts in the field often provide reviews on the best tools and practices, so a good starting point is to look up such publications. A good example is [Metagenomics: tools and insights for analyzing next-generation sequencing data derived from biodiversity studies](https://pubmed.ncbi.nlm.nih.gov/25983555/).
- Freely available software and pipelines, such as those listed below, can be an option compared to commercial analysis packages.
- To get access to compute and storage you may contact your local IT department or national ELIXIR node which can guide you to the right facilities.

