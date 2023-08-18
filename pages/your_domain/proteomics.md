---
title: Proteomics
description: Data management solutions for proteomics data.
contributors: [Michael Turewicz, Martin Eisenacher, Anika Frericks-Zipper, Ulrike Wittig, Dirk Winkelhardt]
page_id: proteomics
related_pages:
  your_tasks: [metadata]
  tool_assembly: []
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=proteomics
---


## Introduction

The proteomics domain deals with standard data formats, software tools and data repositories for mass spectrometry-based proteomics data. In proteomics, the relatively wide range of mass spectrometry technologies, devices, protocols, study designs and data analysis approaches poses a particular challenge for the standardized description and storage of data and associated metadata. This circumstance forced the proteomics community to deal with the complex definition of suitable standard data formats relatively early in its history. This encouraged, among other things, the development of software tools that can import and export results in standardized formats, and of data repositories in which proteomics data can be stored in a standardized way. The particular challenge for the proteomics community now is to evolve its achievements in data management to date towards a more complete fulfillment of FAIR research data management and to close the remaining gaps in this regard.

## Standard data formats

### Description
To make proteomics data interoperable and reproducible from the first to the last mile of proteomics data analysis pipelines, comprehensive metadata accompanying the data is needed. The crucial metadata includes information on study design, proteomics technology, lab protocol, device, device settings and software settings. All of them have an enormous impact on the resulting data. Thus, to enable data reusability in proteomics appropriate standard data formats are needed.

### Considerations

For different proteomics experiments and different steps of the respective data analysis pipelines there are different kinds of data and metadata that should be recorded. Consequently, the main challenges for data and metadata standardization include:
- What are the definitions of proteomics-specific terms that are needed to describe proteomics experiments?
- Which is the minimal information that is needed to describe a proteomics experiment?
- How should the data and metadata of proteomics raw data and peak lists be stored?
- How should the data and metadata of proteomics identification results be stored?
- How should the data and metadata of proteomics quantification results be stored?
- How can proteomics data and metadata be stored in a simple and human-readable way?


### Solutions
The Human Proteome Organisation (HUPO) Proteomics Standards Initiative ({% tool "proteomics-standards-initiative" %}), a proteomics community-driven organization, provides several different controlled vocabularies, standard data formats, converter and validator software tools. The most important include:
- Controlled vocabularies: PSI-MS, PSI-MI, XLMOD and sepCV, which are provided as OBO files.
- The Minimum Information About a Proteomics Experiment ([MIAPE](https://psidev.info/miape)) guidelines document.
- [mzML](https://www.psidev.info/mzML)  - a standard format for encoding raw mass spectrometer output.
- [mzIdentML](https://www.psidev.info/mzidentml) - a standard exchange format for peptides and proteins identified from mass spectra.
- [mzQuantML](https://psidev.info/mzquantml) - a standard format that is intended to store the systematic description of workflows quantifying molecules (principally peptides and proteins) by mass spectrometry.
- [mzTab](https://www.psidev.info/mztab) - a tab delimited text file format to report proteomics and metabolomics results.


## Processing and analysis of proteomics data

### Description
For all steps within a FAIR proteomics data analysis pipeline software is needed that imports standard data formats and exports standard data formats including all needed results and metadata.

### Considerations
- Can your proteomics raw data recorded by a mass spectrometer be stored as an mzML file?
- Is it possible to convert your raw data to mzML?
- Does your search engine support mzML and/or mzIdentML?
- Does your quantification software support mzQuantML or mzTab?


### Solutions
- Within the proteomics community various converter software tools such as {% tool "msconvert" %} were implemented, which support the conversion of mass spectrometer output formats to the mzML standard data format as well as other conversions to standard data formats.
- Information on software tools that support HUPO-PSI data formats can be found on the standard format-specific web pages of the HUPO-PSI (e.g., [mzML](https://www.psidev.info/mzML) , [mzIdentML](https://www.psidev.info/mzidentml) and [mzTab](https://www.psidev.info/mztab) ). The following list shows just a few tools using standard data formats as input and/or output: 
  * {% tool "comet" %}
  * {% tool "mascot" %}
  * {% tool "openms" %}
  * {% tool "pia-protein-inference-algorithms" %}
  * {% tool "skyline" %}
  * {% tool "paa" %}


## Preserving and sharing proteomics data

### Description
In order to make proteomics data and results worldwide findable and accessible for other researchers and software, FAIR public data repositories are needed.

### Consideration
- How can I find an appropriate proteomics data repository?
- How can I upload my proteomics data into a specific proteomics data repository?
- What are the requirements for my data to be uploaded into a proteomics data repository?
- What are the advantages of uploading data into proteomics data repositories?
- How can public proteomics data be used by other researchers?


### Solution
- You can find an appropriate data repository via the website of the {% tool "proteomexchange" %} Consortium. ProteomeXchange was established to provide globally coordinated standard data submission and dissemination pipelines involving the main proteomics repositories, and to encourage open data policies in the field. Currently, member repositories include {% tool "pride" %}, {% tool "peptideatlas" %}, {% tool "massive" %}, jPOST, iProx and PanoramaPublic.
- Information on data uploads can be found on [ProteomeXchange submissions](http://www.proteomexchange.org/submission) or on the websites of the particular data repositories. E.g. PRIDE uploads are conducted via the {% tool "pride-submission-tool" %}. There are data repository-specific requirements.
- Advantages of data publication: fulfillment of journal requirements, higher visibility of research, free storage, worldwide accessibility, basic re-analysis by repository-associated tools and possible integration in more specialized knowledgebases like: {% tool "human-protein-atlas" %}, {% tool "macpepdb" %}, {% tool "string" %}, {% tool "unimod" %} or {% tool "uniprot" %}
