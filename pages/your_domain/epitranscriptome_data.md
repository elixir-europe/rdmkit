---
title: Epitranscriptome data
contributors: [Ernesto Picardi]
page_tag: epitrans
---

## Introduction
Epitranscriptome modifications are emerging as important factors to fine tune gene expression and regulation in a variety of organisms and experimental conditions. To date more than 100 distinct chemical modifications to RNA have been characterized, including transient (i.e. m6A or m1A or m5C) and not-transient (A-to-I or C-to-U RNA editing) nucleotide variants. In the last few years, several methods based on deep sequencing technologies (RNAseq or MeRIPseq or miCLIP or direct RNA sequencing) have been optimized to profile the epitranscriptome in humans and various model organisms. The detection of RNA modifications requires ad hoc bioinformatics pipelines as well as the use of computing intensive tools to handle the huge amount of available deep transcriptome sequencing experiments. A fruitful organization of data and computational workflows is therefore important for a *FAIRification* of epitranscriptome domain.

## Collection of research data
 
### Description
Several high-throughput experimental approaches have been developed for profiling the transcriptome-wide distribution of RNA modifications. While not-transient changes (RNA editing) can be detected using standard RNAseq data, RNA modifications like m6A or m1A or m5C can be identified by a variety of antibody based methods such as MeRIPseq or miCLIP and by means of the RNA directed sequencing. To comply with the FAIR principles, it is important to define the sequencing protocol adopted to produce data as well as related metadata. 

### Considerations
- What is the aim of the experiments? 
- Are you planning to profile transient or not-transient RNA modifications?
- Is the method based on the RNA directed sequencing?

### Solutions
- Define the sequencing protocol depending on the target RNA modification (transient or not-transient). In case of data from public databases, carefully look at the method used to generate them.
- Prefer profiling methods allowing the detection of RNA modifications at single nucleotide level.

## Processing and analysis of epitranscriptome data

### Description
Epitranscriptome is a novel field and in rapid expansion. Since a variety of transcriptome-wide sequencing methods exists, several computational tools have been developed. It is important here to decide which pipeline to adopt.

### Considerations
- Are you using classical RNAseq data?
- Are you profiling not-transient RNA modifications?
- Are you profiling transient RNA changes?

### Solutions
- Epitranscriptome experts often provide reviews on the best tools and practices, so a good starting point is to read such publications. A good example is [Investigating RNA editing in deep transcriptome datasets with REDItools and REDIportal](https://www.nature.com/articles/s41596-019-0279-7).
- For RNA editing events, prefer RNAseq data from total and rRNA depleted RNA. Strand oriented reads will improve the read mappability, mitigating mis-mapping biases.
- Once a pipeline has been adopted, it should be used for all samples.

## Preservation, sharing and reuse of analysis results

### Description
Storing epitranscriptome data is relevant for investigating the biological properties of RNA modifications and facilitating the sharing and reuse.

### Considerations
Which kind of RNA modifications are you studying?

### Solutions
Upload your data and results in available databases. For not transient RNA modifications, [REDIportal](http://srv00.recas.ba.infn.it/atlas/) could be a solution.

