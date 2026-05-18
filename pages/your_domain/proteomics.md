---
title: Proteomics
description: Data management solutions for proteomics data.
contributors: [Michael Turewicz, Martin Eisenacher, Anika Frericks-Zipper, Ulrike Wittig, Dirk Winkelhardt]
editors: [Bert Droesbeke, Korbinian Bösl, Laura Portell Silva, Federico Bianchini]
page_id: proteomics
related_pages:
  Your_tasks: [metadata]
  Tool_assembly: []
training:
  - name: Proteomics Search query in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=proteomics
fairsharing:
- name: Proteomics collection
  url: https://fairsharing.org/7480
---

## Introduction
The proteomics domain encompasses standard data formats, software tools, and data repositories for mass spectrometry-based proteomics data. In proteomics, the relatively wide range of mass spectrometry technologies, devices, protocols, study designs and data analysis approaches poses a particular challenge for the standardised description and storage of data and associated metadata. This circumstance compelled the proteomics community to address the complex definition of suitable standard data formats relatively early in its history. This encouraged, among other things, the development of software tools that can import and export results in standardised formats, and of data repositories in which proteomics data can be stored in a standardised way. The particular challenge for the proteomics community now is to evolve its achievements in data management to date towards a more complete fulfilment of FAIR research data management and to close the remaining gaps in this regard.

## Standard data formats
### Description
To make proteomics data interoperable and reproducible from the first to the last mile of proteomics data analysis pipelines, comprehensive metadata accompanying the data is needed. The crucial metadata includes information on study design, proteomics technology, lab protocol, device, device settings and software settings. All of them have an enormous impact on the resulting data. Thus, to enable data reusability in proteomics, appropriate standard data formats are needed.

### Considerations
For different proteomics experiments and different steps of the respective data analysis pipelines, there are different kinds of data and metadata that should be recorded. Consequently, the main challenges for data and metadata standardisation include:
- What are the definitions of proteomics-specific terms that are needed to describe proteomics experiments?
- Which is the minimal information that is needed to describe a proteomics experiment?
- How should the data and metadata of proteomics raw data and peak lists be stored?
- How should the data and metadata of proteomics identification results be stored?
- How should the data and metadata of proteomics quantification results be stored?
- How can proteomics data and metadata be stored in a simple and human-readable way?

### Solutions
{% tool "proteomics-standards-initiative" %} is a proteomics community-driven organisation providing several different controlled vocabularies, standard data formats, converter and validator software tools. The most important include:
- Controlled vocabularies: {% tool "psi-ms" %}, {% tool "psi-mi" %}, and {% tool "xlmod" %}, which are provided as OBO files.
- {% tool "miape" %} guidelines document.
- {% tool "mzml" %} - a standard format for encoding raw mass spectrometer output.
- {% tool "mzidentml" %} - a standard exchange format for peptides and proteins identified from mass spectra.
- {% tool "mztab" %} - a tab-delimited text file format to report proteomics and metabolomics results.

## Processing and analysis of proteomics data
### Description
For all steps within a FAIR proteomics data analysis pipeline, software is needed that imports standard data formats and exports standard data formats, including all needed results and metadata.

### Considerations
- Can your proteomics raw data recorded by a mass spectrometer be stored as an {% tool "mzml" %} file?
- Is it possible to convert your raw data to {% tool "mzml" %}?
- Does your search engine support {% tool "mzml" %} and/or {% tool "mzidentml" %}?
- Does your quantification software support {% tool "mztab" %}?

### Solutions
- Within the proteomics community, various converter software tools such as {% tool "msconvert" %} were implemented, which support the conversion of mass spectrometer output formats to the mzML standard data format as well as other conversions to standard data formats.
- Information on software tools that support HUPO-PSI data formats can be found on the specific web pages for {% tool "mzml" %}, {% tool "mzidentml" %}, and {% tool "mztab" %}. The following list shows just a few tools using standard data formats as input and/or output: 
  * {% tool "comet" %}
  * {% tool "mascot" %}
  * {% tool "openms" %}
  * {% tool "pia-protein-inference-algorithms" %}
  * {% tool "skyline" %}
  * {% tool "paa" %}
  * {% tool "apid-interactomes" %}

## Preserving and sharing proteomics data
### Description
FAIR public data repositories are needed to make proteomics data and results worldwide findable and accessible for other researchers and software.

### Consideration
- How can I find an appropriate proteomics data repository?
- How can I upload my proteomics data into a specific proteomics data repository?
- What are the requirements for my data to be uploaded into a proteomics data repository?
- What are the advantages of uploading data into proteomics data repositories?
- How can public proteomics data be used by other researchers?
- How can I increase the transparency and reproducibility of my shared data?

### Solution
- You can find an appropriate data repository via the website of the {% tool "proteomexchange" %} Consortium. ProteomeXchange was established to provide globally coordinated standard data submission and dissemination pipelines involving the main proteomics repositories, and to encourage open data policies in the field. Currently, member repositories include {% tool "pride" %}, {% tool "peptideatlas" %}, {% tool "massive" %}, {% tool "jpostrepo" %}, {% tool "iprox" %}, and {% tool "panoramapublic" %}.
- Information on data uploads can be found on [ProteomeXchange submissions](http://www.proteomexchange.org/submission) or on the websites of the particular data repositories. E.g. PRIDE uploads are conducted via the {% tool "pride-submission-tool" %}. There are data repository-specific requirements.
- Advantages of data publication: fulfilment of journal requirements, higher visibility of research, free storage, worldwide accessibility, basic re-analysis by repository-associated tools and possible integration in more specialised knowledgebases like: {% tool "human-protein-atlas" %}, {% tool "macpepdb" %}, {% tool "string" %}, {% tool "unimod" %}, {% tool "interpro" %}, {% tool "uniprot" %} or {% tool "cath" %}
- You can increase transparency and reproducibility of the mass spectrometry-based proteomics data by providing sample and data relationship file ({% tool "sdrf" %}) along with submission to a data repository (e.g. ProteomeXchange).
