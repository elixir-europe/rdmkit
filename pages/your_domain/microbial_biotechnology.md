---
title: Microbial biotechnology
description: Data management solutions for microbial biotechnology data
contributors: [Anil Wipat, David Markham, Christian Atallah, Bradley Brown, Munazah Andrabi]
page_id: micro biotech
related_pages: 
  your_tasks: []
  tool_assembly: []
---

## Introduction

### Microbial Biotechnology and DBTL cycle
The Microbial Biotechnology domain is a very broad field that encompasses the application of microorganisms to the development of useful products and processes. As such, there are a very wide variety of experimental tools, approaches, and ultimately data, that arise in this field. A convenient representation of microbial biotechnology for organisational purposes is the stages of the engineering life cycle drawn from the related field of synthetic biology. 

The **Design-Build-Test-Learn (DBTL) cycle** represents experimental design and analysis steps in synthetic biology. Current data management best practices and guidelines that should be applied throughout the DBTL cycle will be described and discussed here.

#### Design
The design for a system in microbial biotechnology essentially involves two, interrelated exercises: (i) Identification of the biological entities/hosts that will be used to develop the product in question (ii) Identification of the genetic modifications/circuitry/constructs necessary to modify the host if appropriate. The design stage may also include optional approaches: (iii) Metabolic engineering of biosynthetic pathways (iv) Using mathematical modelling to aid the design of the system. Data management best practices and guidelines should be applied for each exercise and approach.

The components of the design stage could be summarised as below.
* [Biological host](microbial_biotechnology#design-biological-hosts---metadata-ontologies-and-metadata-publication) or organism.
* [Synthetic parts](microbial_biotechnology#design-synthetic-parts---existing-data-metadata-collection-and-publication).
* [Metabolomic pathways and enzymes](microbial_biotechnology#design-metabolomic-pathways-and-enzymes---metadata-ontologies-and-metadata-publication).
* [Mathematical model](microbial_biotechnology#design-mathematical-model---standards-and-metadata-publication) for system design.

#### Build
The build stage in the microbial biotechnology and/or synthetic biology life cycle is about building of the microbial systems and involves the application of any number of a range of experimental techniques. In this stage the synthetic parts are assembled and transformed into the biological host.

The main aspects of the build stage are:
* [methods](microbial_biotechnology#build-methods---documentation-and-metadata-publication), protocols and procedures used to build the modified organism.

#### Test
The test stage of a biotechnological study is the most variable in terms of the types of data produced. This stage is mostly about:
* [testing](microbial_biotechnology#test-outcome-tests---metadata-standards-and-metadata-publication) the outcome or output variables and analyse the modified organism.
* Characterising the synthetic parts using experimental data.

#### Learn
The learning stage consists in interpreting the obtained results, share the acquired knowledge and reuse it in combination with other existing data to improve the creation of the modified organism.
* Publish and share data and results.
* Reuse existing data and combine it with new data.
* Feed data back into model(s) to inform the next iteration.

Here, we adopt the stages of **design**, **build** and **test**, and their components or aspects, to categorise the various approaches available for the management of data in microbial biotechnology. 

### Data management challenges
Ultimately, the ideal scenario is that data is captured in a standard format and then uploaded to a repository to ensure that it is Findable, Accessible, Interoperable and Reusable (FAIR). However, for the biotechnology field, data standards are still under development or missing completely and there are still gaps in database provision for some data types.

Due to the interdisciplinary nature of the field, data arising from studies in microbial biotechnology relate to both computational studies, such as modelling and simulation, and the results of wet-lab based studies used for the construction and experimental characterisation of microbial systems. Given the breadth, scope and rapid development of the field of microbial biotechnology, this guide is by no means exhaustive.

This guide is by no means comprehensive. Please get in touch with further suggestions for relevant standards and data sharing tools that can make it more complete. Sites such as [Fairsharing](https://fairsharing.org/) can provide a wealth of data about standards that may be appropriate for a given data type and not mentioned in this brief guide.


## Design: Biological hosts - Metadata, ontologies and (meta)data publication

### Description
Metadata standards and ontologies to capture the taxonomic and phenotypic data about the biological hosts or organism are still evolving, therefore finding and using a correct standard to describe the biological host can be challenging. 

It is recommended to publish and share information about biological hosts in dedicated public data repositories and databases.

### Considerations
 * The recording of taxonomic and genetic data must be considered carefully as part of the design stage.
 * Metadata surrounding the host is essential, such as where it was isolated, growth conditions, recommended protocols etc.
 * Genetic information relating to strains and any modifications needs to be kept track of as modifications are made. Note that capturing the metadata describing a genome sequence and its host is vitally important to facilitate further studies in comparative genomics and phenotypic analysis.
 * To choose what are the appropriate repositories for your (meta)data, you should consider what kind of information about the host you are going to share, since each type of information could be published in a different repository.
   * Species, taxonomy, strain.
   * Phenotypic information.
   * Genomic or nucleotide information.

### Solutions
#### Metadata schemas and ontologies
* Current data standards to capture the  taxonomic and phenotypic data are still evolving, with notable work on the [Access to Biological Collection Data Schema (ABCD)](https://www.tdwg.org/standards/abcd/) and the activities of the [Biodiversity Information Standards task force (TDWG)](https://www.tdwg.org/). The Darwin Core standard from the [(TDWG)](https://www.tdwg.org/) is an appropriate standard to provide metadata about the taxonomic properties of a particular microorganism.
* The [NCBI taxonomy homepage](https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/) can also provide appropriate taxon IDs for recording taxonomic information.
* Information about proposed standardised nomenclature for prokaryotes can be found at the [List of Prokaryotic names with Standing in Nomenclature (LPSN)](https://lpsn.dsmz.de/) ([Parte et al., 2020](https://pubmed.ncbi.nlm.nih.gov/32701423/)).
* Data standards for recording the information about where a microorganism was isolated from do exist and this topic is covered in other RDMkit pages such as the [marine metagenomics](marine_metagenomics) domain. Information can also be found in a publication by Ten Hoopen and colleagues ([Ten Hoopen et al., 2015](https://pubmed.ncbi.nlm.nih.gov/26203332/)). 
* [The Environment Ontology](https://sites.google.com/site/environmentontology/) is also relevant here to describe environmental entities of all kinds, from microscopic to intergalactic scales.
* A set of genetic nomenclature standards have been established by microbiologists and have been used for many years. These are still a useful way of communicating data about the genotype of a strain ([Maloy and Hughes, 2007](https://pubmed.ncbi.nlm.nih.gov/17352909/)).
* Minimal information standards have been established to specify this metadata, such as the MIGS standard ([Field et al., 2008](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2409278/)).

#### (Meta)Data publication and sharing
* For sharing host information, you  can use databases such as the [Bacterial Diversity Metadatabase (Bacdive)](https://bacdive.dsmz.de). You  can also deposit strains and associated information in a strain repository such as the [National Collection of Industrial, Food and Marine Bacteria (NCIMB)](https://www.ncimb.com/culture-collection/) or the [American Type Culture Collection (ATCC)](https://www.lgcstandards-atcc.org/?geo_country=gb). There are also many organisations established for individual species of microorganisms, the [Bacillus Genetic Stock Centre (BGSC)](http://www.bgsc.org/) being one example. 
* Databases such as [CellRepo](https://cellrepo.herokuapp.com/) allow strains that have been barcoded to be tracked using a version control type system ([Tellechea-Luzardo et al., 2020](https://pubmed.ncbi.nlm.nih.gov/32078768/)).
* Genomic information can be captured at the nucleotide level using the well-known [European Nucleotide Archive standard (ENA)](https://www.ebi.ac.uk/ena/browser/home) and [submitted](https://www.ebi.ac.uk/ena/browser/submit) to the ENA database to allow the information to be shared.
* The database collection from the [International Nucleotide Sequence Database Collaboration](http://www.insdc.org/) provides an umbrella for gathering and sharing a variety of sequence data from different sequence databases internationally.
* Other databases such as [GenBank](https://www.ncbi.nlm.nih.gov/genbank/) and the [DNA Data Bank of Japan (DDBJ)](https://www.ddbj.nig.ac.jp/index-e.html) also cater for sequence information.


## Design: Synthetic parts - Existing data, metadata collection and publication

### Description
Appropriate and detailed description of the synthetic parts design is critical for reproducibility. It is important to consider how to record metadata at each point in the design process in a standard way, so that it can be clear to others and reproducible.

### Considerations
* Format of designs may vary depending on the application, whether this be at the sequence level or an entire system.
* Consider existing management tools that can help visualise and modify genetic designs.
* Think about how the information about characterisation of genetic constructs assist in the selection of parts and modelling designs.
* At this stage, it may be desirable to assert which host the designed device is intended to express in and also the intended method of replication in the host - for example, cloned on a particular plasmid or integrated in the host chromosome.

### Solutions

#### Existing data
* Sequences are characterised as parts which can be found with the assistance of various repositories such as: 
  * [iGEM Parts Registry](http://parts.igem.org/Main_Page)
  * [The Joint BioEnergy Institute's Inventory of Composable Elements (JBEI-ICE)](https://ice.jbei.org) ([Ham et al., 2012](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3467034/))
  * [SynBioHub](https://synbiohub.org)
* Sequences can be isolated from standard genetic databases such as [ENA](https://www.ebi.ac.uk/ena/browser/home) and [GenBank](https://www.ncbi.nlm.nih.gov/genbank/).

#### Tools for metadata collection
* You can manage the design stage using genetic computer aided design tools, such as [Benchling](https://benchling.com) for example, where information can be shared within small teams. [Benchling](https://benchling.com) supports a number of different data standards including FASTA, GenBank and SBOL1. 
  * Sometimes FASTA will be the most relevant format, for example when sending for DNA synthesis. 
  * Formats like GenBank, DICOM-SB ([Sainz de Murieta, Bultelle and Kitney, 2016](https://pubmed.ncbi.nlm.nih.gov/26854090/)) or SBOL may be more applicable for instances where more information, such as functional annotation, would be useful to be shared. 
  * SBOL 2.0 and higher allows more than just the genetics of a system to be captured and shared. Using SBOL allows interactions between components in the design to be specified, information about RNA and proteins can be included and the provenance of a design can also be captured. Experimental information relating to the test and build of a system can also be captured and shared.
* SBOL data can be made using tools such as [Benchling](https://benchling.com) (SBOL1 only), [SBOL Designer](https://sboldesigner.github.io/) ([Zhang et al., 2017](https://pubmed.ncbi.nlm.nih.gov/28441476/)) and [ShortBOL](http://shortbol.org/) to name but a few. A more comprehensive list of SBOL tools can be found on the [sbolstandard](https://sbolstandard.org/) website.
* More generally, The [Investigation/Study/Assay (ISA)](https://isa-specs.readthedocs.io/) model can be used in systems biology, life sciences, environmental and biomedical domains to structure research outputs. The [ISA-Tab](https://isa-specs.readthedocs.io/en/latest/isatab.html) format provides a framework for capturing these data in CSV files.
* [Rightfield](https://rightfield.org.uk/download.html) provides a mechanism for capturing metadata using easy to use spreadsheets.

#### (Meta)Data publication and sharing
* Once the design is complete, you can share this information via a repository such as: 
  * [iGEM Parts Registry](http://parts.igem.org/Main_Page)
  * [SynBioHub](https://synbiohub.org)
  * [JBEI-ICE](https://ice.jbei.org)
  * [Addgene](https://www.addgene.org)
* Much information about its performance can be included, varying from experimental results such as fluorescence curves to predicted performance based on modelling. 
* It would be recommended to use standard figures that can be easily understood. 
  * [SBOL-Visual](https://sbolstandard.org/visual-glyphs/) is a good example of a graphical standard; it utilises standard shapes to represent different genetic parts which can help clarify a complex synthetic construct. [SBOL-Visual](https://sbolstandard.org/visual-glyphs/) can be crafted using tools such as [VISBOL](http://visbol.org/).
* Platforms such as [SEEK](https://fair-dom.org/platform/seek/), built on technologies such as ISA, support a large range of systems and synthetic biology projects. [SEEK](https://fair-dom.org/platform/seek/) provides a web-based resource for sharing scientific research datasets, models or simulations, and processes. [SEEK](https://fair-dom.org/platform/seek/) can be installed locally or [FAIRDOMHub](https://fairdomhub.org/), a version of [SEEK](https://fair-dom.org/platform/seek/) which is hosted by FAIRDOM, is available for general community use.


## Design: Metabolomic pathways and enzymes - Metadata, ontologies and (meta)data publication

### Description
Here we describe some of the available options to accurately represent and store information about the designs of metabolic pathways and functional information about assays. 

### Considerations
* Enzymes have specific data standards that should be considered when accessing and recording their data.

### Solutions
#### Metadata and ontologies
* SBOL allows information about the enzymes and the metabolic pathways to be captured in the design document and so this is a viable approach for sharing more than just the genetics of the system.
* Enzymes can be assigned EC numbers, according to the guidance from the [International Union of Biochemistry and Molecular Biology (IUBMB)](https://www.qmul.ac.uk/sbcs/iubmb/), to indicate their function and an entry made in the [BRaunschweig ENzyme DAtabase](https://www.brenda-enzymes.org/) (BRENDA).
* More generally, the [IUPAC-IUBMB Joint Commission on Biochemical Nomenclature (JCBN)](https://www.qmul.ac.uk/sbcs/iupac/jcbn/) encourages the communication of biochemical information using generally understood terminology.

#### (Meta)Data publication
* Databases such as SBOLME ([Kuwahara et al., 2017](https://pubmed.ncbi.nlm.nih.gov/28076956/)) or [SynBioHub](https://synbiohub.org) can be used to share the data.
* Metabolite information can also be submitted to, or referred to in, [ChEBI](https://www.ebi.ac.uk/chebi/).
* [BRaunschweig ENzyme DAtabase](https://www.brenda-enzymes.org/) (BRENDA).


## Design: Mathematical model - Standards and (meta)data publication

### Description
What tools and standards need to be considered when building mathematical models to aid the design of genetic systems?

How can the models be shared via repositories and made  available in a way that makes results replicable?

### Considerations
* A variety of standards and tools are available for model building.
* It is important to associate the genetic design with its corresponding model.

### Solutions
* [Systems Biology Markup Language (SBML)](http://sbml.org/Main_Page) is a popular standardised format for sharing mathematical models for which a variety of tools are available for model building.
* More generally, the [COmputational Modeling in BIology NEtwork (COMBINE)](http://co.mbine.org/), provides a platform for coordinating standardisation of models in biology.
* SBOL can also be used to associate a genetic design with its corresponding model.
* Models can be shared in model repositories such as [biomodels](https://www.ebi.ac.uk/biomodels/).


## Build: Methods - Documentation and (meta)data publication

### Description
The build stage in the microbial biotechnology and/or synthetic biology life cycle involves the application of any number of a range of experimental techniques and, since these techniques are so varied, the domain is therefore very difficult to standardise in terms of the data and metadata to be shared. 

The current method of sharing information about the building of microbial systems is to write a detailed free text in the materials and methods section of a scientific paper.

### Considerations:
* Capturing the information about the build process involves collecting the information arising from DNA amplification, DNA preparation and purification, primer design, restriction enzyme analysis, gel electrophoresis and DNA sequencing to name but a few techniques. 
* If using a protein expression device, the intended vector for its replication in a given host will need to be named.
* The cloning strategy used to assemble the protein expression device and the vector will also need to be specified and shared. 
* The information about how the “final system” was built is highly variable, depending on the DNA synthesis and/or assembly approach used. Consider ways to share this information.

### Solutions
#### Documentation
* To the authors’ knowledge, there are no proposed standards that exist that are able to capture this diverse set of data. Currently, from a pragmatic point of view, the best a data manager can do is to make sure data is captured in some form from the lab scientist and grouped together with as much metadata as possible. 

  The metadata standards for a build exercise are still to be defined and so at the discretion of the data manager.
* SBOL versions 2.0 and above provides a data standard that allows build data that has been grouped to be associated with design data for a part, device or system along with a minimal amount of metadata.
* Similarly, [research object bundles](https://www.researchobject.org/), and more recently [RO-Crates](https://www.researchobject.org/ro-crate/), can be used to gather together build data and test data with information about the overall study.

#### (Meta)Data publication and sharing
* The design information about the vector DNA or RNA sequence should be shared via public databases  such as ENA or Genbank. 
* Various DNA synthesis companies build DNA from a computer specification of the sequence and also a variety of experimental approaches for assembling DNA molecules. This information can be shared as free text attached to a design in SBOL format and uploaded to a repository that supports SBOL2 format and above such as SynBioHub.
* Once grouped together in a free form the data can be archived along with the metadata, collecting the data together in an archived form using a file compression format. The [combine archive format](http://co.mbine.org/specifications/omex.version-1) may also be useful.
 

## Test: Outcome tests - Metadata standards and (meta)data publication

### Description
The test stage of a biotechnological study is the most variable in terms of the types of data produced. The types of experiments carried out to test a microbial system are highly dependent on the intended function of the system under construction. Some common approaches include at the simplest level, characterising the growth of an organism at various scales in different growth regimes and assaying the production of desired product.

The data arising from assays for product development is highly variable and beyond the scope of this short guide, however we propose some recommended resources.

### Considerations

* What types of experiments, e.g.  organism growth, organism characterisation, will you undertake to test your microbial system? What types of data result from those experiments? Will you combine multi-omics assays in your study?
    * Is there a reporting guideline for the type of you are generating?
    * Will you reuse existing testing protocols or generate and share your own protocols?

* Since (meta)data repositories often require compliance to their metadata standards, ontologies and file formats, it is recommended to be aware of those requirements when describing the test stage.

### Solutions

#### Metadata standards
* **Minimum Information Standard for Engineered Organism Experiments (MIEO).** Minimal information necessary to record the growth of an organism in culture, has been described by Hect and colleagues ([Hecht et al., 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6283831/)). 

* **Enzyme.** If your product is a protein such as an enzyme then some standards developed by the [Standards for Reporting Enzyme Data (STRENDA) Consortium](https://www.beilstein-institut.de/en/projects/strenda/) may be helpful ([‘Standards for Reporting Enzyme Data: The STRENDA Consortium: What it aims to do and why it should be helpful’, 2014](https://www.sciencedirect.com/science/article/pii/S2213020914000135)).

* **Microscopy.** Microscopy is often also used to characterise the behaviour of engineered microorganisms. Standards such as the [Open Microscopy Environment Ontology](https://fairsharing.org/bsg-s001430/) and the [Cellular Microscopy Phenotype Ontology (CMPO)](https://www.ebi.ac.uk/cmpo/) can help provide standardised metadata terms.

* **Flow Cytometry data.** The [International Society for the Advancement of Cytometry (ISAC)](https://isac-net.org/page/Data-Standards) provides information on a variety of appropriate data standards for capturing Flow Cytometry data (used to characterise microbial populations at a single cell level) ([Spidlen et al., 2021](https://pubmed.ncbi.nlm.nih.gov/32881398/)).

* **Nucleic acids information.** The [ENA](https://www.ebi.ac.uk/ena/browser/home), amongst others, provides guidance on the metadata for RNAseq datasets.

* **Proteomics.** [HUPO proteomics standards initiative](https://www.hupo.org/Proteomics-Standards-Initiative) provides a range of guidance for capturing and sharing proteomics data.


#### (Meta)Data publication and sharing
* **Protocols.** Protocols used for testing can be shared using platforms such as: 
  * [protocols.io](https://www.protocols.io/). 
  * [iGEM engineering hub](https://2021.igem.org/Engineering/Introduction), which also provides some guidance for a variety of data capture protocols and standardised units.
* **Images.** Images can be shared with the community by repositories such as the [Image Data Resource (IDR)](https://idr.openmicroscopy.org/).
* **Nucleic acids information.** Information about nucleic acids can be shared via
  * [ENA](https://www.ebi.ac.uk/ena/browser/home)
  * [GEO](https://www.ncbi.nlm.nih.gov/geo/)
  * [ArrayExpress](https://www.ebi.ac.uk/arrayexpress/) 
* **Proteomics.** Proteomics data can be shared via [HUPO proteomics standards initiative](https://www.hupo.org/Proteomics-Standards-Initiative).
* **Metabolic studies.** Metabolomic studies can be shared through the [Metabolome Exchange Database](http://www.metabolomexchange.org/site/), which provides a resource for sharing data from metabolic studies and guidance for the submission of metabolome data.
* **Biological sources.** Information about biological sources can be shared via the [BioStudies database](https://www.ebi.ac.uk/biostudies/), which has been set up to capture and share information about multi-omics and other biological studies ([Sarkans et al., 2018](https://pubmed.ncbi.nlm.nih.gov/29069414/)).


## Bibliography

[Field, D. et al. (2008) ‘The minimum information about a genome sequence (MIGS) specification’, Nature biotechnology, 26(5), pp. 541–547. doi: 10.1038/nbt1360.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2409278/)

[Ham, T. S. et al. (2012) ‘Design, implementation and practice of JBEI-ICE: an open source biological part registry platform and tools’, Nucleic acids research, 40(18), p. e141. doi: 10.1093/nar/gks531.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3467034/)

[Hecht, A. et al. (2018) ‘A minimum information standard for reproducing bench-scale bacterial cell growth and productivity’, Communications biology, 1, p. 219. doi: 10.1038/s42003-018-0220-6.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6283831/)

[Kuwahara, H. et al. (2017) ‘SBOLme: a Repository of SBOL Parts for Metabolic Engineering’, ACS synthetic biology, 6(4), pp. 732–736. doi: 10.1021/acssynbio.6b00278.](https://pubmed.ncbi.nlm.nih.gov/28076956/)

[Maloy, S. R. and Hughes, K. T. (2007) ‘Strain Collections and Genetic Nomenclature’, Methods in Enzymology, pp. 3–8. doi: 10.1016/s0076-6879(06)21001-2.](https://pubmed.ncbi.nlm.nih.gov/17352909/)

[Parte, A. C. et al. (2020) ‘List of Prokaryotic names with Standing in Nomenclature (LPSN) moves to the DSMZ’, International journal of systematic and evolutionary microbiology, 70(11), pp. 5607–5612. doi: 10.1099/ijsem.0.004332.](https://pubmed.ncbi.nlm.nih.gov/32701423/)

[Sainz de Murieta, I., Bultelle, M. and Kitney, R. I. (2016) ‘Toward the First Data Acquisition Standard in Synthetic Biology’, ACS synthetic biology, 5(8), pp. 817–826. doi: 10.1021/acssynbio.5b00222.](https://pubmed.ncbi.nlm.nih.gov/26854090/)

[Sarkans, U. et al. (2018) ‘The BioStudies database—one stop shop for all data supporting a life sciences study’, Nucleic Acids Research, pp. D1266–D1270. doi: 10.1093/nar/gkx965.](https://pubmed.ncbi.nlm.nih.gov/29069414/)

[Spidlen, J. et al. (2021) ‘Data File Standard for Flow Cytometry, Version FCS 3.2’, Cytometry. Part A: the journal of the International Society for Analytical Cytology, 99(1), pp. 100–102. doi: 10.1002/cyto.a.24225.](https://pubmed.ncbi.nlm.nih.gov/32881398/)

[‘Standards for Reporting Enzyme Data: The STRENDA Consortium: What it aims to do and why it should be helpful’ (2014) Perspectives in Science, 1(1-6), pp. 131–137. doi: 10.1016/j.pisc.2014.02.012.](https://www.sciencedirect.com/science/article/pii/S2213020914000135)

[Tellechea-Luzardo, J. et al. (2020) ‘Linking Engineered Cells to Their Digital Twins: A Version Control System for Strain Engineering’, ACS synthetic biology, 9(3), pp. 536–545. doi: 10.1021/acssynbio.9b00400.](https://pubmed.ncbi.nlm.nih.gov/32078768/)

[Ten Hoopen, P. et al. (2015) ‘Marine microbial biodiversity, bioinformatics and biotechnology (M2B3) data reporting and service standards’, Standards in genomic sciences, 10, p. 20. doi: 10.1186/s40793-015-0001-5.](https://pubmed.ncbi.nlm.nih.gov/26203332/)

[Zhang, M. et al. (2017) ‘SBOLDesigner 2: An Intuitive Tool for Structural Genetic Design’, ACS synthetic biology, 6(7), pp. 1150–1160. doi: 10.1021/acssynbio.6b00275.](https://pubmed.ncbi.nlm.nih.gov/28441476/)
