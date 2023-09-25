---
title: "Single-Cell Sequencing"
description: "Managing data generated from single-cell sequencing experiments."
contributors: [Johan Rollin, MeInBIo program, Freiburg university, Collaborator's Name, add your name]
output: pdf_document
related_pages:
  your_tasks: [dmp, data_organisation, data_publication, metadata, storage]
  tool_assembly: galaxy
  training:
  - name: Training in Galaxy
    registry: Galaxy
    url: "https://usegalaxy.eu/training-material/topics/single-cell/"
page_id: single_cell_sequencing
---

## Introduction

In this section, we provide an overview of the data management challenges specific to single-cell sequencing experiments. Single-cell sequencing enables the analysis of gene expression at the individual cell level, leading to unique data management requirements due to the high dimensionality and complexity of the data. Single-cell sequencing encompasses a diverse array of techniques, including RNA sequencing (RNAseq), Nucleus sequencing, ATAC sequencing, and Multiome sequencing, each presenting its own set of challenges and considerations. Additionally, the field embraces a wide range of data analysis approaches, further compounding the complexity. Consequently, addressing the standardized description and storage of data and associated metadata becomes paramount in this context. To ensure the reproducibility and reliability of research findings, it is crucial to proactively identify the specific steps in the data workflow that should be preserved. Moreover, decisions regarding data formats must be made collectively to facilitate seamless data sharing, collaboration, and long-term data preservation within the single-cell sequencing community. This document aims to elucidate these challenges and provide practical guidance for navigating them effectively.

###  Preprocessing and Quality Control

Data preprocessing and quality control are integral components of the single-cell sequencing workflow, playing a pivotal role in ensuring the integrity of the data and facilitating accurate downstream analysis. These challenges encompass a spectrum of tasks aimed at enhancing the quality, reliability, and interpretability of the data, making them conducive for subsequent analysis.
By comprehensively addressing data preprocessing and quality control, we aim to provide researchers with a robust framework for navigating these critical stages of the single-cell sequencing process. This includes strategies for addressing technical variability, identifying and mitigating low-quality cells or outliers, managing batch effects, and other sources of variability that may arise within and between datasets.

## Data analysis rational

### Description
Preprocessing encompasses tasks such as data normalization, quality control, and transformation to mitigate technical variations. These steps aim to ensure that the data is in a suitable state for downstream analysis.
Then, the next step's central objectives include the identification of individual cells within the dataset, the assignment of gene expression profiles to each cell, and the generation of count matrices that represent the expression levels of thousands of genes across all cells. To do so, tools like CellRanger or STARsolo are used to facilitate the crucial process of cell and gene assignment. These tools are specifically designed to take the raw sequencing data, typically generated from technologies like droplet-based or plate-based single-cell RNA sequencing (scRNA-seq), and process it into quantifiable and interpretable information. This transformation of raw data into structured, cell-by-gene matrices is fundamental for downstream analyses, such as clustering cells by similarity, identifying cell types, and studying gene expression patterns at a single-cell resolution. In essence, CellRanger and STARsolo play a pivotal role in converting complex sequencing data into a format that researchers can subsequently explore to extract valuable biological insights.
Following the execution of cell and gene assignment, post-processing steps come into play. These post-processing stages involve activities like efficient clustering of cells and biologically relevant annotation of clusters. By carefully orchestrating both pre- and post-processing phases, researchers can enhance the quality, reliability, and interpretability of their single-cell sequencing data, ultimately leading to more accurate and biologically meaningful insights.
### Considerations
##### Pre-cell/gene assignation

- **Normalization and Transformation**: Determine how to effectively normalize and transform the data to account for technical variability.
- **Low-Quality Cell Detection**: Explore methods for identifying and removing low-quality cells or outliers from the dataset.


##### Post-cell/gene assignation

- **Efficient Clustering**: Consider techniques to achieve efficient and meaningful clustering of single-cell data. 
- **Batch Effects Handling**: Develop strategies to mitigate batch effects and other sources of variability within and between datasets.
- **Biological Annotation**: Determine how to annotate the identified cell clusters with biologically relevant labels.

### Solutions

- **Normalization and Transformation**: Consider using established methods such as "LogNormalize" or "scTransform" to address differences in sequencing depth and monitor data quality.
- **Low-Quality Cell Detection**: Evaluate metrics like the number of detected genes per cell, mitochondrial gene content, and UMI counts to define quality criteria. The threshold for data quality acceptability is variable depending of several factors like the number of replicates or the type of organism (procaryote, plant, animal...) used.
- **Batch Effects Handling**: Examining you data to check that the most important elements for the clustering/cell comparison are biological and not technical. Exploring batch correction methods like [Harmony](https://www.nature.com/articles/s41592-019-0619-0) can help reduce technical biases in data integration. 
- **Biological Annotation**: Use known marker genes or reference-based annotation to assign cell types or states to clusters. Database of knwon cell markers (like [CellMarker](http://117.50.127.228/CellMarker/index.html)) can be helpful.

Each of these elements need to be provided with a comprehensive description. Including details on the normalization techniques applied, outlier removal strategies, and batch correction methods employed to enhance data quality and reliability.

## Data Integration and Analysis Across Experiments

### Description

The analysis of single-cell sequencing data frequently requires the integration and comparative examination of data stemming from various experiments. Combining datasets to gain a broader perspective or comparing results from distinct experiments, navigating the intricacies of data integration, harmonization, and interpretation is essential for extracting meaningful insights from single-cell sequencing data. This section addresses these considerations and provides solutions to facilitate the effective analysis and interpretation of integrated data, allowing researchers to draw comprehensive conclusions from diverse experimental sources.

### Considerations

- **Data Integration**:  How can we integrate data from different experiments while accounting for differences in experimental conditions? (ie. sample WT vs KO with several time point)
- **Data Comparison**: What approaches can be used to identify shared cell types and biological signals across datasets? (ie. sample WT vs KO comparison scATAC and scRNAseq)
- **Annotation Consistency**: How should we manage metadata and annotations to ensure consistent interpretation across experiments?

### Solutions

- **Data Integration & Data Comparison**: Use built-in method for data integration & comparison (like [Seurat](https://satijalab.org/seurat/) or [Scanpy](https://scanpy.readthedocs.io/en/stable/) ), including normalization, batch correction methods and dimensionality reduction techniques to see their effect. Here the difficulty is to make sure the integration/comparison made make sense meanning beeing careful that the celltype annotations are consistent and that the number/cell repartition is relevant.
- **Annotation Consistency**: Emphasize the need for consistent metadata and annotation practices, including standardized naming and format usage. 

## Long-Term Data Storage and Accessibility

### Description

Ensuring the long-term storage and accessibility of single-cell sequencing data pose distinct challenges that demand attention. This section delves into the critical considerations for effectively storing and making single-cell sequencing data accessible over an extended period of time.
### Considerations

- **Effective Archiving**: What are the best practices for archiving and safeguarding extensive single-cell sequencing datasets to ensure their long-term preservation?
- **Ethical Data Handling**: How can we guarantee data privacy and adhere to ethical guidelines when sharing sensitive single-cell data with the research community?
- **Collaborative Platforms**: Which platforms or repositories are suitable for simplifying data sharing and encouraging collaboration among researchers?
- **Enhancing Reproducibility**: What specific steps and formats should be employed to enable reproducibility in single-cell sequencing experiments?

### Solutions
- **Effective Archiving**: Use established data repositories like GEO (Gene Expression Omnibus) or ArrayExpress for long-term data preservation. 

- **Ethical Data Handling**: Emphasize the importance of informed consent and ethical considerations in data sharing agreements.

- **Collaboration Platforms**: Explore version control systems (e.g., [Git](https://git-scm.com/)), data sharing platforms (e.g., [Zenodo](https://zenodo.org/)), data analysis platforms (e.g., [Galaxy](https://usegalaxy.eu/)), and domain-specific repositories (e.g., [Single Cell Portal](https://singlecell.broadinstitute.org/single_cell?order=recent)) to facilitate efficient data sharing, analysis, and collaboration.

- **Enhancing Reproducibility**: Provide guidance on enhancing reproducibility, including the use of containerization technologies like [Docker](https://www.docker.com/) to encapsulate analysis environments. Emphasize the importance of documenting analysis workflows, code, and metadata using standardized formats and sharing them in version-controlled repositories.

## analysis step desription and format proposal

- **Raw Sequencing Data**:
    - *Data Type*: Raw FASTQ files for sequencing reads.
    - *Format*: Compressed FASTQ format (*.fastq.gz).
    - *Explanation*: Raw sequencing data is typically stored in compressed FASTQ format (*.fastq.gz). This format retains the original sequencing reads and is space-efficient. Compressed files reduce storage requirements while preserving data integrity.

- **Cell-Gene Assignment**:
    - *Data Type*: Cell-gene assignment matrix indicating gene expression levels per cell.  
    - *Format*: Standardized data matrix format, such as h5, h5ad or CSV.
    - *Explanation*: The cell-gene assignment matrix, representing gene expression per cell, is best stored in a standardized format like h5 h5ad or CSV as it will allow the modification needed for the next step while being readable by most single cell tool.

- **Dimensionality Reduction and Clustering**:
    - *Data Type*: Reduced-dimension representations (e.g., PCA, t-SNE) and cell clusters.
    - *Format*: Include plots and files in common data visualization formats (e.g., PDF, PNG).
    - *Explanation*: Visual formats like PDF and PNG allow easy sharing and visualization.

- **Annotation and Biological Interpretation**:
    - *Data Type*: Annotated cell types, differential gene expression results, and any other biologically meaningful annotations.
    - *Format*: Structured and standardized annotation files, such as Excel spreadsheets, CSV or JSON, alongside visualizations like heatmaps or volcano plots in common visualization formats.
    - *Explanation*: Biologically meaningful annotations, including cell types and differential gene expression results, should be stored in structured formats. Visualizations like heatmaps or volcano plots should be included in standard visual formats for easy interpretation.

- **Analysis Code and Environment**:
    - *Data Type*: All code and scripts used for data preprocessing, analysis, and visualization.
    - *Format*: Version-controlled repositories using Git, ideally, container files to capture analysis environments should be used. Detailed documentation for code execution should be provided.
    - *Explanation*: Analysis code and scripts should be version-controlled using Git repositories. Additionally, capturing the analysis environment using Docker or Singularity container files help to ensure reproducibility. Detailed documentation of code execution is essential for transparency and re-suability.

- **Metadata**:
    - *Data Type*: Comprehensive metadata describing experimental conditions, sample information, and data processing steps.
    - *Format*: Structured metadata files in widely accepted formats like JSON, CSV or Excel spreadsheets, following community-specific metadata standards if available.
    - *Explanation*: Following community-specific metadata standards, if available, ensures consistency and compatibility with other datasets.

By preserving these steps and data in standardized and accessible formats, researchers can enhance the reproducibility of single-cell sequencing experiments, facilitate collaboration, and ensure that others can validate and build upon their work effectively. Other additional file can be kept if useful for the interpretaion (e.g., for scATAC, the results files containing sequences fragments or mapping can be important, they should be kept in standardize format: tsv, bam, bed or bigwig). 

## Relevant Tools and Resources



- Review of single cell best practices: Heumos, L., Schaar, A.C., Lance, C. et al. Best practices for single-cell analysis across modalities. Nat Rev Genet 24, 550–572 (2023) [https://doi.org/10.1038/s41576-023-00586-w](https://doi.org/10.1038/s41576-023-00586-w)

- The single cell best practice book by the single-cell best practices consortium: [https://www.sc-best-practices.org/preamble.html](https://www.sc-best-practices.org/preamble.html)

List relevant tools and resources that researchers can use to address the data management challenges discussed in this protocol. Include links to tools, software, and databases that facilitate data preprocessing, analysis, integration, and storage in the context of single-cell sequencing experiments.
<!-- Feel free to add more sections or subsections as needed. -->
