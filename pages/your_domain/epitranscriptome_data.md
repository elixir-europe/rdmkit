---
title: Epitranscriptome data
description: Data management solutions for epitranscriptome data.
contributors: [Ernesto Picardi, Laura Portell Silva]
page_id: epitrans
related_pages: 
  Your_tasks: []
  Tool_assembly: []
fairsharing:
- name: Epitranscriptome data collection
  url: https://fairsharing.org/7478
---

## Introduction
Epitranscriptome modifications are emerging as important factors to fine tune gene expression and regulation in a variety of organisms and experimental conditions. To date more than 100 distinct chemical modifications to RNA have been characterized, including transient (i.e. m6A or m1A or m5C) and not-transient (A-to-I or C-to-U RNA editing) nucleotide variants. In the last few years, several methods based on deep sequencing technologies (RNAseq or MeRIPseq or miCLIP or direct RNA sequencing) have been optimized to profile the epitranscriptome in humans and various model organisms. The detection of RNA modifications requires ad hoc bioinformatics pipelines as well as the use of computing intensive tools to handle the huge amount of available deep transcriptome sequencing experiments. A fruitful organization of data and computational workflows is therefore important to make data in the epitranscriptome domain interoperable and resuable in line with the FAIR (Findable, Accessible, Interoperable and Reusable) principles.

## Collection of research data
 
### Description
Several high-throughput experimental approaches have been developed for profiling the transcriptome-wide distribution of RNA modifications. While not-transient changes (RNA editing) can be detected using standard RNAseq data, RNA modifications like m6A or m1A or m5C can be identified by a variety of antibody based methods such as MeRIPseq or miCLIP and by means of the RNA directed sequencing. In order to make the data understandable and reusable, it is important to define the sequencing protocol adopted to produce data as well as related metadata. 

### Considerations
- Are you planning to profile transient or not-transient RNA modifications?
- Is the method based on the RNA directed sequencing?
- Do you collect your own data or reuse them from public databases?

### Solutions
- Define the sequencing protocol depending on the target RNA modification (transient or not-transient). In case of using data from public databases, carefully look at the method used to generate them.
- Prefer profiling methods allowing the detection of RNA modifications at single nucleotide level.
- Epitranscriptome data is generally reused from literature or public and established databases, such as {% tool "rediportal" %}. All data must have an identifier from the original database that it comes from. The source database is used also to retrieve metadata.

## Processing and analysis of epitranscriptome data

### Description
Epitranscriptome is a novel field and in rapid expansion. Since a variety of transcriptome-wide sequencing methods exist, several computational tools have been developed. It is important here to decide which pipeline to adopt.

### Considerations
- What are the compute resources you need to analyse your data? 
- Do you have data storage problems due to the size of the data?
- Are you using RNAseq data?
- Are you profiling or transient not-transient RNA modifications?

### Solutions
- The current pipeline for RNA editing ({% tool "reditools" %}) requires the use of time intensive computational resources to browse position by position all genomic sites covered by RNAseq reads. In order to overcome that, a novel tool ({% tool "reditools2" %}) able to employ HPC resources and reduce the computing time has been developed. However, for transient modifications identified by direct RNA sequencing, compute intensive tools are still required. The computational speed up could be obtained by using GPU graphical cards. In general, for standard RNAseq experiments, each sample requires 8-10 CPUs and at least 8-10 GB of RAM memory. Direct RNA sequencing, instead, requires 8-10 CPUs, at least 1 GPU and 8-10 GB of RAM memory. Once a pipeline has been adopted, it should be used for all samples.
- Data storage is a big issue and not all intermediate files produced during the analyses can be maintained. However, since original data are easily and always available from public sources, analysis files are stored until the end of the established computational workflow. Then, only the final table file including epitranscriptomic variants are recovered and included in {% tool "rediportal" %}. Although this procedure could be time consuming in case of important updates, such as the adoption of a novel genome assembly, it preserves the storage requirements.
- Epitranscriptome experts often provide reviews on the best tools and practices, so a good starting point is to read such publications. A good example is [Investigating RNA editing in deep transcriptome datasets with REDItools and REDIportal](https://www.nature.com/articles/s41596-019-0279-7).
- For RNA editing events, prefer RNAseq data from total and rRNA depleted RNA. Strand oriented reads will improve the read mappability, mitigating mis-mapping biases.

## Preservation, sharing and reuse of analysis results

### Description
Storing epitranscriptome data is relevant for investigating the biological properties of RNA modifications and facilitating the sharing and reuse.

### Considerations
- Which kind of RNA modifications are you studying?
- Do you have data storage problems when preserving the data?
- Can epitranscriptome data be openly shared?

### Solutions
- For long term storage and for preserving epitranscriptome data, raw reads have to be submitted to public databases. This is a mandatory requirement to upload epitranscriptomic annotations in specialized databases. In case of data deposited in public databases such as ENA or SRA, RNA modifications could be uploaded in dedicated databases as {% tool "rediportal" %}.
- To avoid the storage of a large amount of files, raw data is used to complete all computational steps. Soon after, they are removed as well as intermediate files. Only final tables are preserved and stored in our portal. Data is actually preserved because raw data is always available through public and established databases.
- All data included in the REDIportal, including individual variants, annotations and metadata, is sharable and open. Only one database is mentioned here because there is the plan of having a unique and individual resource for epitranscriptome data.
