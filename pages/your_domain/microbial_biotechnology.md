---
title: Microbial biotechnology
description: Data management solutions for microbial biotechnology data.
contributors: [Anil Wipat, David Markham, Christian Atallah, Bradley Brown, Munazah Andrabi]
page_id: micro_biotech
related_pages: 
  Your_tasks: []
  Tool_assembly: []
fairsharing:
- name: Microbial biotechnology collection
  url: https://fairsharing.org/7481
---

## Introduction

### Microbial biotechnology and DBTL cycle
The microbial biotechnology domain is a very broad field that encompasses the application of microorganisms to the development of useful products and processes. As such, there are a very wide variety of experimental tools, approaches, and ultimately data, that arise in this field. A convenient representation of microbial biotechnology for organisational purposes is the stages of the engineering life cycle drawn from the related field of synthetic biology. 

The **Design-Build-Test-Learn (DBTL) cycle** represents experimental design and analysis steps in synthetic biology. Current data management best practices and guidelines that should be applied throughout the DBTL cycle will be described and discussed here.

#### Design
The design for a system in microbial biotechnology essentially involves two, interrelated exercises: (i) Identification of the biological entities/hosts that will be used to develop the product in question and (ii) Identification of the genetic modifications/circuitry/constructs necessary to modify the host if appropriate. The design stage may also include optional approaches: (iii) Metabolic engineering of biosynthetic pathways and (iv) Using mathematical modelling to aid the design of the system. Data management best practices and guidelines should be applied for each exercise and approach.

The components of the design stage can be summarised as:
* [Biological host](microbial_biotechnology#design-biological-hosts---metadata-ontologies-and-metadata-publication) or organism.
* [Synthetic parts](microbial_biotechnology#design-synthetic-parts---existing-data-metadata-collection-and-publication).
* [Metabolomic pathways and enzymes](microbial_biotechnology#design-metabolomic-pathways-and-enzymes---metadata-ontologies-and-metadata-publication).
* [Mathematical model](microbial_biotechnology#design-mathematical-model---standards-and-metadata-publication) for system design.

#### Build
The build stage in the microbial biotechnology and/or synthetic biology life cycle is about the building of the microbial systems and involves the application of any number of a range of experimental techniques. At this stage, the synthetic parts are assembled and transformed into the biological host.

The main aspects of the build stage are:
* [methods](microbial_biotechnology#build-methods---documentation-and-metadata-publication), protocols and procedures used to build the modified organism.

#### Test
The test stage of a biotechnological study is the most variable in terms of the types of data produced. This stage is mostly about:
* [testing](microbial_biotechnology#test-outcome-tests---metadata-standards-and-metadata-publication) the outcome or output variables and analyse the modified organism.
* Characterising the synthetic parts using experimental data.

#### Learn
The learning stage consists of interpreting the obtained results, sharing the acquired knowledge and reusing it in combination with other existing data to improve the creation of the modified organism.
* Publish and share data and results.
* Reuse existing data and combine it with new data.
* Feed data back into model(s) to inform the next iteration.

Here, we adopt the stages of **design**, **build** and **test**, and their components or aspects, to categorise the various approaches available for the management of data in microbial biotechnology. 

### Data management challenges
Ultimately, the ideal scenario is that data is captured in a standard format and then uploaded to a repository to ensure that it is Findable, Accessible, Interoperable and Reusable (FAIR). However, for the biotechnology field, data standards are still under development or missing completely and there are still gaps in database provision for some data types.

Due to the interdisciplinary nature of the field, data arising from studies in microbial biotechnology relate to both computational studies, such as modelling and simulation, and the results of wet lab-based studies used for the construction and experimental characterisation of microbial systems. Given the breadth, scope and rapid development of the field of microbial biotechnology, this guide is by no means exhaustive.

This guide is by no means comprehensive. Please get in touch with further suggestions for relevant standards and data-sharing tools that can make it more complete. Sites such as {% tool "fairsharing" %} can provide a wealth of information about standards that may be appropriate for a given data type and not mentioned in this brief guide. For further information and references on standards, data management, FAIR principles, data analysis, and more, please visit the {% tool "nfdi4microbiotakb" %}.


## Design: Biological hosts - metadata, ontologies and (meta)data publication

### Description
Metadata standards and ontologies to capture the taxonomic and phenotypic data about the biological hosts or organism are still evolving, therefore finding and using a correct standard to describe the biological host can be challenging. 

It is recommended to publish and share information about biological hosts in dedicated public data repositories and databases.

### Considerations
 * The recording of taxonomic and genetic data must be considered carefully as part of the design stage.
 * Metadata surrounding the host is essential, such as where it was isolated, growth conditions, recommended protocols, etc.
 * Genetic information relating to strains and any modifications needs to be kept track of as modifications are made. Note that capturing the metadata describing a genome sequence and its host is vitally important to facilitate further studies in comparative genomics and phenotypic analysis.
 * To choose what are the appropriate repositories for your (meta)data, you should consider what kind of information about the host you are going to share since each type of information could be published in a different repository.
   * Species, taxonomy, strain.
   * Phenotypic information.
   * Genomic or nucleotide information.

### Solutions
#### Metadata schemas and ontologies
* The current data standards to capture the  taxonomic and phenotypic data are still evolving, with notable work on the {% tool "access-to-biological-collection-data-schema" %} and the activities of the {% tool "biodiversity-information-standards" %}. The Darwin Core standard from the {% tool "biodiversity-information-standards" %} is an appropriate standard to provide metadata about the taxonomic properties of a particular microorganism.
* The {% tool "ncbi-taxonomy" %}homepage can also provide appropriate taxon IDs for recording taxonomic information.
* Information about proposed standardised nomenclature for prokaryotes can be found at the {% tool "list-of-prokaryotic-names-with-standing-in-nomenclature" %} {% cite parte2020lpsn %}.
* Data standards for recording the information about where a microorganism was isolated from do exist and this topic is covered in other RDMkit pages such as the [marine metagenomics](marine_metagenomics) domain. Information can also be found in a publication by Ten Hoopen and colleagues {% cite tenhoopen2015m2b3 %}. 
* {% tool "the-environment-ontology" %} is also relevant here to describe environmental entities of all kinds, from microscopic to intergalactic scales.
* A set of genetic nomenclature standards have been established by microbiologists and have been used for many years. These are still a useful way of communicating data about the genotype of a strain {% cite maloy2007strain %}.
* Minimal information standards have been established to specify this metadata, such as the MIGS standard {% cite field2008migs %}.

#### (Meta)data publication and sharing
* For sharing host information, you  can use databases such as the {% tool "bacdive" %}. You  can also deposit strains and associated information in a strain repository such as the {% tool "ncimb" %} or the {% tool "atcc" %}. There are also many organisations established for individual species of microorganisms, the {% tool "bacillus-genetic-stock-center" %} being one example. 
* Databases such as {% tool "cellrepo" %} allow strains that have been barcoded to be tracked using a version control type system {% cite tellechealuzardo2020linking %}.
* Genomic information can be captured at the nucleotide level using the well-known {% tool "european-nucleotide-archive" %} and submitted to the ENA database to allow the information to be shared.
* The database collection from the {% tool "international-nucleotide-sequence-database-collaboration" %} provides an umbrella for gathering and sharing a variety of sequence data from different sequence databases internationally.
* Other databases such as {% tool "genbank" %} and the {% tool "dna-data-bank-of-japan" %} also cater for sequence information.


## Design: Synthetic parts - existing data, metadata collection and publication

### Description
Appropriate and detailed description of the synthetic parts design is critical for reproducibility. It is important to consider how to record metadata at each point in the design process in a standard way, so that it can be reproducible.

### Considerations
* Format of designs may vary depending on the application, whether this be at the sequence level or an entire system.
* Consider existing management tools that can help visualise and modify genetic designs.
* Think about how the information about the characterisation of genetic constructs assist in the selection of parts and modelling designs.
* At this stage, it may be desirable to assert which host the designed device is intended to express in and also the intended method of replication in the host - for example, cloned on a particular plasmid or integrated in the host chromosome.

### Solutions

#### Existing data
* Sequences are characterised as parts which can be found with the assistance of various repositories such as: 
  * {% tool "igem-parts-registry" %}
  * {% tool "jbei-ice" %} {% cite ham2012jbeiice %}
  * {% tool "synbiohub" %}
  * {% tool "freegenes" %} - Repository of IP-free synthetic biological parts
* Sequences can be isolated from standard genetic databases such as {% tool "european-nucleotide-archive" %} and {% tool "genbank" %}.

#### Tools for metadata collection
* You can manage the design stage using genetic computer-aided design tools, such as {% tool "benchling" %} for example, where information can be shared within small teams. {% tool "benchling" %} supports a number of different data standards including FASTA, GenBank and SBOL1. 
  * Sometimes FASTA will be the most relevant format, for example when sending for DNA synthesis. 
  * Formats like GenBank, DICOM-SB {% cite sainzdemurieta2016toward %} or SBOL may be more applicable for instances where more information, such as functional annotation, would be useful to be shared. 
  * SBOL 2.0 and higher allows more than just the genetics of a system to be captured and shared. Using SBOL allows interactions between components in the design to be specified, information about RNA and proteins can be included and the provenance of a design can also be captured. Experimental information relating to the test and build of a system can also be captured and shared.
* SBOL data can be made using tools such as {% tool "benchling" %} (SBOL1 only), {% tool "sboldesigner" %} {% cite zhang2017sboldesigner %} and {% tool "shortbol" %} to name but a few. A more comprehensive list of SBOL tools can be found on the {% tool "synthetic-biology-open-language" %} website.
* More generally, the [Investigation/Study/Assay (ISA)](https://isa-specs.readthedocs.io/) model can be used in systems biology, life sciences, environmental and biomedical domains to structure research outputs. The [ISA-Tab](https://isa-specs.readthedocs.io/en/latest/isatab.html) format provides a framework for capturing these data in CSV files.
* {% tool "rightfield" %} provides a mechanism for capturing metadata using easy to use spreadsheets.

#### (Meta)data publication and sharing
* Once the design is complete, you can share this information via a repository such as: 
  * {% tool "igem-parts-registry" %}
  * {% tool "synbiohub" %}
  * {% tool "jbei-ice" %}
  * {% tool "addgene" %}
* Much information about its performance can be included, varying from experimental results such as fluorescence curves to predicted performance based on modelling. 
* It would be recommended to use standard figures that can be easily understood. 
  * {% tool "sbol-visual" %} is a good example of a graphical standard; it utilises standard shapes to represent different genetic parts which can help clarify a complex synthetic construct. {% tool "sbol-visual" %} can be crafted using tools such as {% tool "visbol" %}.
* Platforms such as {% tool "fairdom-seek" %}, built on technologies such as ISA, support a large range of systems and synthetic biology projects. {% tool "fairdom-seek" %} provides a web-based resource for sharing scientific research datasets, models or simulations, and processes. {% tool "fairdom-seek" %} can be installed locally or {% tool "fairdomhub" %}, a version of {% tool "fairdom-seek" %} is available for general community use.
* Information about biological sources and other data not fitting elsewhere can be shared via the {% tool "biostudies" %} database,


## Design: Metabolomic pathways and enzymes - metadata, ontologies and (meta)data publication

### Description
Here we describe some of the available options to accurately represent and store information about the designs of metabolic pathways and functional information about assays. 

### Considerations
* Enzymes have specific data standards that should be considered when accessing and recording their data.

### Solutions
#### Metadata and ontologies
* SBOL allows information about the enzymes and the metabolic pathways to be captured in the design document and so this is a viable approach for sharing more than just the genetics of the system.
* Enzymes can be assigned EC numbers, according to the guidance from the {% tool "iupac-iubmb-joint-commission-on-biochemical-nomenclature" %} (IUPAC and {% tool "international-union-of-biochemistry-and-molecular-biology" %}), to indicate their function and an entry made in the {% tool "brenda" %} (BRENDA).
* More generally, the {% tool "iupac-iubmb-joint-commission-on-biochemical-nomenclature" %} encourages the communication of biochemical information using generally understood terminology.

#### (Meta)data publication
* Databases such as SBOLME {% cite kuwahara2017sbolme %} or {% tool "synbiohub" %} can be used to share the data.
* Metabolite information can also be submitted to, or referred to in, {% tool "chebi" %}.
* {% tool "brenda" %} (BRENDA).


## Design: mathematical model - standards and (meta)data publication

### Description
What tools and standards need to be considered when building mathematical models to aid the design of genetic systems?

How can the models be shared via repositories and made  available in a way that makes results reproducible?

### Considerations
* A variety of standards and tools are available for model building.
* It is important to associate the genetic design with its corresponding model.

### Solutions
* {% tool "systems-biology-markup-language" %} is a popular standardised format for sharing mathematical models for which a variety of tools are available for model building.
* More generally, the {% tool "computational-modelling-in-biology-network" %}, provides a platform for coordinating the standardisation of models in biology.
* SBOL can also be used to associate a genetic design with its corresponding model.
* Models can be shared in model repositories such as {% tool "biomodels" %}.


## Build: methods - documentation and (meta)data publication

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
* Similarly, [research object bundles](https://www.researchobject.org/), and more recently {% tool "research-object-crate" %}, can be used to gather together build data and test data with information about the overall study.

#### (Meta)data publication and sharing
* The design information about the vector DNA or RNA sequence should be shared via public databases  such as ENA or Genbank. 
* Various DNA synthesis companies build DNA from a computer specification of the sequence and also a variety of experimental approaches for assembling DNA molecules. This information can be shared as free text attached to a design in SBOL format and uploaded to a repository that supports SBOL2 format and above such as {% tool "synbiohub" %}.
* Once grouped together in a free form, the data can be archived along with the metadata, collecting the data together in an archived form using a file compression format. The [combine archive format](https://combinearchive.org/index/) may also be useful.
 

## Test: outcome tests - metadata standards and (meta)data publication

### Description
The test stage of a biotechnological study is the most variable in terms of the types of data produced. The types of experiments carried out to test a microbial system are highly dependent on the intended function of the system under construction. Some common approaches include at the simplest level, characterising the growth of an organism at various scales in different growth regimes and assaying the production of desired product.

The data arising from assays for product development is highly variable and beyond the scope of this short guide, however, we propose some recommended resources.

### Considerations

* What types of experiments, e.g.  organism growth, organism characterisation, will you undertake to test your microbial system? What types of data result from those experiments? Will you combine multi-omics assays in your study?
    * Is there a reporting guideline for the type of you are generating?
    * Will you reuse existing testing protocols or generate and share your own protocols?

* Since (meta)data repositories often require compliance to their metadata standards, ontologies and file formats, it is recommended to be aware of those requirements when describing the test stage.

### Solutions

#### Metadata standards
* **Minimum Information Standard for Engineered Organism Experiments (MIEO).** Minimal information necessary to record the growth of an organism in culture, has been described by Hect and colleagues {% cite hecht2018bacterial %}. 

* **Enzyme.** If your product is a protein such as an enzyme then some standards developed by the {% tool "standards-for-reporting-enzyme-data" %} may be helpful {% cite strenda2014standards %}.

* **Microscopy.** Microscopy is often also used to characterise the behaviour of engineered microorganisms. Standards such as the [Open Microscopy Environment Ontology](https://fairsharing.org/bsg-s001430/) and the {% tool "cellular-microscopy-phenotype-ontology" %} can help provide standardised metadata terms.

* **Flow Cytometry data.** The {% tool "international-society-for-the-advancement-of-cytometry" %} provides information on a variety of appropriate data standards for capturing Flow Cytometry data (used to characterise microbial populations at a single cell level) {% cite spidlen2021data %}.

* **Nucleic acids information.** The {% tool "european-nucleotide-archive" %}, amongst others, provides guidance on the metadata for RNAseq datasets.

* **Proteomics.** {% tool "proteomics-standards-initiative" %} provides a range of guidance for capturing and sharing proteomics data.


#### (Meta)data publication and sharing
* **Protocols.** Protocols used for testing can be shared using platforms such as: 
  * {% tool "protocols-io" %}. 
  * [iGEM engineering hub](https://2021.igem.org/Engineering/Introduction), which also provides some guidance for a variety of data capture protocols and standardised units.
* **Images.** Images can be shared with the community by repositories such as the {% tool "image-data-resource" %}.
* **Nucleic acids information.** Information about nucleic acids can be shared via
  * {% tool "european-nucleotide-archive" %}
  * {% tool "gene-expression-omnibus" %}
  * {% tool "arrayexpress" %} 
* **Proteomics.** Proteomics data can be shared via {% tool "proteomics-standards-initiative" %}.
* **Metabolic studies.** Metabolomic studies can be shared through the {% tool "metabolomexchange" %}, which provides a resource for sharing data from metabolic studies and guidance for the submission of metabolome data.
* **Biological sources.** Information about biological sources can be shared via the {% tool "biostudies" %} database, which has been set up to capture and share information about multi-omics and other biological studies {% cite sarkans2018biostudies %}.


## Bibliography

{% bibliography --cited %}
