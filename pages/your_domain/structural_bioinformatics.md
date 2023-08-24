---
title: Structural Bioinformatics
description: Data management solutions for structural bioinformatics data.
contributors: [Gerardo Tauriello, Ian Sillitoe, Nicola Bordin, Christine Orengo, Mihaly Varadi, Sameer Velankar, Jiří Černý, Carolina Simón Guerrero]
page_id: struct_bioinfo
related_pages: 
  your_tasks: []
  tool_assembly: []
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?utf8=%E2%9C%93&q=Structural+Bioinformatics#workflows
---

## Introduction

Structural bioinformatics provides scientific methods to analyse, predict, and validate the three-dimensional structure of biological macromolecules such as proteins, RNA, DNA, or carbohydrates including small molecules bound to them. It also provides an important link with the genomics and structural biology communities. One objective of structural bioinformatics is the creation of new methods of analysis and manipulation of biological macromolecular data in order to predict their structures, function and interactions. Currently, atomic structures of macromolecules can be obtained both based on experimental and computational methods. This document describes guidelines to deposit computationally or experimentally solved structure models together with relevant metadata according to FAIR principles. While we describe guidelines for the deposition process, predictors are usually required to collect the relevant metadata already while doing the predictions so that the data is available during deposition.

## Storing and sharing structure predictions
 
### Description

Researchers in the field should be able to find predictions of macromolecular structures, access their coordinates, understand how and why they were produced, and have estimates of model quality to assess the applicability of the model for specific applications. The considerations and solutions described below are written from the perspective of protein structure predictions but they also apply to other types of macromolecular structures.

### Considerations

* Is your prediction based on experimental data (i.e. integrative or hybrid modelling) or purely *in silico*? <br> This is important to define the appropriate deposition system.
* What is the purpose of the structure prediction? Is it a large-scale modelling effort using automated prediction methods to (for instance) generally increase structural coverage of known proteins or a single modelling effort performed, possibly with manual intervention, for a specific application?<br> This is important to define the appropriate deposition system.
* What is the source for the sequences of the modelled proteins?<br> This is important to cross-link with existing databases such as UniProtKB.
* What modelling steps were performed?<br> Descriptions here can vary widely among modelling methods but should be detailed enough to enable reproducibility and include references to methods described in manuscripts and publicly available software or web services.
* What input data were used for the modelling steps?<br> For protein structure predictions, this commonly includes the identification of homologous proteins from sequence databases with or without coverage by experimental structures. Knowing the input data greatly facilitates further analysis and reproducibility of the structure prediction.
* What is the expected accuracy of the structure prediction?<br> This is commonly referred to as "model quality" or "model confidence" and is of major relevance to determine whether a given model can be used for downstream analysis. Quality estimates should enable users to judge the expected accuracy of the prediction both globally and locally.
* Under which licence terms can others use your models?<br> Depending on the deposition system, there will be predefined and commonly permissive terms of use, but if this is to be restricted or if models are made available in a self-hosted system, an appropriate usage policy must be defined.

### Solutions

* There are three main options to make your models available:
  * Deposit in {% tool "modelarchive" %} for theoretical models of macromolecular structures. Models deposited in the ModelArchive are made available under the CC BY-SA 4.0 licence (see [here for details](https://modelarchive.org/terms-of-use)).
  * Deposit in {% tool "pdb-dev" %} for models using integrative or hybrid modelling. Models deposited in PDB-Dev are made available under the CC0 1.0 licence (see [here for details](https://www.wwpdb.org/about/usage-policies)). If theoretical models were used as part of the modelling, they can either be included in the PDB-Dev deposition or, if they are expected to be useful by themselves, deposited in ModelArchive and referenced to.
  * Make available using a dedicated web service for large-scale modelling efforts which are updated on a regular basis using automated prediction methods. The solution for rapidly building such a service is to deploy the {% tool "mineprot" %} application, which is able to curate data from most AlphaFold-like systems (see [here for details](https://doi.org/10.1093/database/baad059)). Unified access to these services can be provided with the {% tool "3d-beacons" %} which is being developed by the [ELIXIR 3D-BioInfo Community](https://elixir-europe.org/communities/3d-bioinfo). The data providers currently connected in the network are listed in [the 3D-Beacons documentation](https://www.ebi.ac.uk/pdbe/pdbe-kb/3dbeacons/docs#partners). An appropriate licence must be associated with the models (check the [RDMkit licensing page](licensing) for guidance on this) and must be compatible with CC-BY 4.0 if the models are to be distributed in the 3D-Beacons network.
* Model coordinates are preferably stored in the standard PDB archive format {% tool "pdbx-mmcif-format-and-tools" %}. While, for many purposes, the legacy PDB format may suffice to store model coordinates and is still widely used, the format is no longer being modified or extended.
* Model quality estimates can be computed globally, per-residue, and per-residue-pair. The estimates should be computed using a relatively recent and well benchmarked tool or by the structure prediction method itself. Please check {% tool "cameo" %}, {% tool "casp" %}, and {% tool "capri" %} to find suitable quality estimators. The [3D-BioInfo Community](https://elixir-europe.org/communities/3d-bioinfo) is also currently working to further improve benchmarking for protein complexes, protein-ligand interactions, and nucleic acid structures. By convention, the main per-residue quality estimates are stored in place of B-factors in model coordinate files. In mmCIF files any number of quality estimates can be properly described and stored in the ma_qa_metric category of the PDBx/mmCIF ModelArchive Extension Dictionary described below.
* Metadata for theoretical models of macromolecular structures should preferably be stored using the {% tool "pdbx-mmcif-modelcif-extension-dictionary" %} independently of the deposition process. The extension is being developed by the [ModelCIF working group](https://wwpdb.org/task/modelcif) with input from the community. Feedback and change requests are welcome and can be given on [github](https://github.com/ihmwg/ModelCIF). The same information can also be provided manually during the deposition in ModelArchive and there is [additional documentation](https://modelarchive.org/help) on how to provide metadata and minimal requirements for it. Generally, the metadata must include:
  * a short description of the study for which the model was generated;
  * if available, a citation to the manuscript referring to the models;
  * the source for the sequences of modelled proteins with references to databases such as {% tool "uniprot" %};
  * modelling steps with references to available software or web services used and to manuscripts describing the method;
  * input data needed for the modelling steps. For instance in homology modelling this could include the {% tool "pdb" %} identifiers for the template structures used for modelling and their alignments to the target protein;
  * model quality estimates.
* If necessary, accompanying data can be provided in separate files using different file formats. The files can be added to ModelArchive depositions and referred to in the PDBx/mmCIF ModelArchive extension format.

## Storing and sharing experimentally solved structures
 
### Description

Experimentally solved atomic structures of molecules can be obtained by several methods, such as X-ray crystallography,  Nuclear Magnetic Resonance (NMR) spectroscopy, and 3D Electron Microscopy. Here you can find useful tools and guides for storing and sharing structure models based on these methods.
* Structure models resulting from experimental methods are broadly in the [Protein Data Bank (PDB)](https://www.wwpdb.org/) under the [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).
* Additionally, raw and intermediate data associated with the structure model can be also published in different curated data archives depending on the methods used. Raw EM data and processed 3D volumes and tomograms can be stored in [EMPIAR](https://www.ebi.ac.uk/empiar/) and [EMDB](https://www.ebi.ac.uk/emdb/), respectively. Raw data from NMR studies can be stored in [BMRB](https://bmrb.io/). For X-ray diffraction experiments raw data can be stored in [IRRMC](https://www.proteindiffraction.org/) and [SBGrid-DG](https://data.sbgrid.org/). Data submitted in these repositories can be cross-referenced to related PDB entries.
* To extend molecular context, structure models can be visualized and analyzed along with respective volume maps and [UniProt](https://www.uniprot.org/) sequences using data aggregators such as [3DBionotes-WS](https://3dbionotes.cnb.csic.es/ws), either if they have been published in PDB and EMDB or if not. A bunch of biochemical, biomedical and validation annotations would be mapped on the structure model coordinates and sequence to let the user better understand macromolecular function and interactions. Users can also use the [COVID-19 Structural Hub](https://3dbionotes.cnb.csic.es/ws/covid19), a dedicated summary view for all published SARS-CoV-2 structure models. 
* As well as for computationally solved structures, model coordinates and metadata for experimentally solved structures are also preferably stored using the standard PDB archive format [PDBx/mmCIF](https://mmcif.wwpdb.org/) and the [PDBx/mmCIF ModelCIF Extension Dictionary](https://mmcif.wwpdb.org/dictionaries/mmcif_ma.dic/Index/), respectively.
* Data model and metadata standards for submitting data underpinning macromolecular models depend on the experimental method used. EMDB map distribution format description has broadly followed [CCP4](https://www.ccp4.ac.uk/html/maplib.html) and [MRC](https://www2.mrc-lmb.cam.ac.uk/research/locally-developed-software/image-processing-software/) map format. Metadata is contained in a header file, an XML file that follows the XSD data model. EMPIAR data model schema consists of the main empiar.xsd XML schema file and additional requirements in empiar.sch in Schematron format (see [here](ftp://ftp.ebi.ac.uk/pub/databases/emtest/empiar/schema/) for more details). BMRB (meta)data distribution format is based on NMR-STAR, an extension of the Self-defining Text Archive and Retrieval (STAR) file format.
* As image processing framework, users can operate with workflow managers FAIR compliant such as [Scipion](https://scipion.i2pc.es/) to obtain macromolecular models using Electron Microscopy (3DEM). It integrates several software packages while taking care of formats and conversions and data submissions to public repositories such as EMDB and EMPIAR. It is also possible to deploy a cloud-compatible version of Scipion either in a single server or in a cluster with [ScipionCloud](https://scipion-em.github.io/docs/release-3.0.0/docs/developer/scipion-on-the-cloud.html#scipion-on-the-cloud). It can be also deployed in EOSC cloud infrastructures (see [here](https://marketplace.eosc-portal.eu/services/eosc.cnb-csic.scipioncloud?pv=search/all&q=scipioncloud) for details).
* [ARIA](https://aria.services)  is a platform that projects and infrastructures can use to manage Access, from proposal submission through to reporting. It provides tools for facilities within a distributed infrastructure to manage their equipment.

  If using ARIA to manage access to the facility, it will shortly be possible to link output data and metadata with proposals, publications and other outputs. This work is being funded by a number of EU funded grants.

