---
title: Biodiversity
description: Data management solutions for biodiversity data.
contributors: [Josephine Burgin, Joana Pauperio, Anne-Françoise Adam-Blondon, Patrick Ruch, Robert Waterhouse, Valeria Di Cola, Erwan Corre, Yvan Le Bras, Peter Woollard, Bachir Balech, Matteo Montagna, Angela P. Fuentes Pardo, Solenne Correard]
page_id: biodiversity
related_pages: 
  your_tasks: [dmp, data_organisation, metadata, data_brokering, machine_actionability, compliance]
  tool_assembly: [galaxy, fairtracks]
# More information on which page id you can use can be found at https://rdmkit.elixir-europe.org/website_overview
training:
  - name: Training about Biodiversity data
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=biodiversity+data

  - name: TeSS Collection of biodiversity-relevant training resources
    registry: TeSS
    url: https://tess.elixir-europe.org/collections/elixir-biodiversity-community

  - name: Galaxy Training Network
    registry: other
    url: https://training.galaxyproject.org/

  - name: ERGA Knowledge Hub
    registry: other
    url: https://knowledge.erga-biodiversity.eu/

  - name: Glittr
    registry: other
    url: https://glittr.org/

# More information on how to fill in this metadata section can be found here https://rdmkit.elixir-europe.org/page_metadata
---

## Introduction

While there is significant literature around biodiversity loss, there is a limited effort in reviewing biodiversity using high-throughput data acquisition technologies. Today, scientists recognise the important roles that genetic and genomic data (e.g. reference genomes, DNA/RNA barcoding approaches, metagenomics and metabarcoding), can play in biodiversity discovery, assessment, monitoring, conservation, and restoration, and its impact in policy and decision making processes. 

These research activities present unique data management challenges, especially in terms of complexity, data integration, and the need for interoperability across diverse datasets. Some of challenges include:

* Managing biological resources (samples, associated specimens or genetic resources): this requires compliance with the national and international frameworks and adherence to data sharing principles (FAIR principles, {% cite wilkinson2016kl %}) and ethical principles (CARE Principles, {% cite carroll2020wb %}).   
* Metadata in biodiversity research: metadata must go beyond basic descriptions to include detailed context, such as geographical locations, temporal data, methods, and environmental conditions, ideally using standard vocabularies (terminology) and ontology terms. Together, these aid ensuring that the data can be more easily discovered and effectively reused by both humans and machines.  
* Data management and integration systems: current systems still fail often to maintain critical links between the data, the metadata, the physical specimens, and the taxonomic information (e.g., correct scientific names) from which the data originates. Moreover, integrating molecular data (e.g., genomic sequences) with ecological, behavioural, or morphological datasets can be complex due to differences in formats, scales, and metadata structures.  
* Taxonomic harmonisation: taxonomy is an evolving field and linking data to and through taxonomy is challenging due to the spread of available resources and often unharmonised practices.   
* Handling and processing large-scale biodiversity data: molecular data (e.g., genomics or transcriptomics data) handling requires bioinformatics pipelines that are computationally intensive and can scale with large datasets.  
* Tracking provenance: ensuring proper tracking of the provenance, updates, and transformations of datasets is crucial, especially in collaborative biodiversity projects involving multiple stakeholders.

Addressing these challenges requires collaborative solutions involving better metadata practices, advanced bioinformatics tools, improved data integration platforms, and standardization efforts across the global biodiversity research community.

In addition to the specific data management challenges faced in biodiversity research, there is the need to move towards [Open Link Data](https://www.ontotext.com/knowledgehub/fundamentals/linked-data-linked-open-data/) in Biodiversity and a linked **Biodiversity Knowledge Graph** (see [machine actionability](https://rdmkit.elixir-europe.org/machine_actionability) for further information on knowledge graph)**.**   
This shift could fundamentally transform the landscape of biodiversity research by enabling more efficient data integration, discovery, and re-use. Moving towards a **Biodiversity Knowledge Graph** represents an ambitious but essential step in modernizing biodiversity research. While significant challenges remain, the potential for improved data integration, accessibility, and re-use across multiple disciplines could transform the field and open up new avenues for understanding and conserving biodiversity.


## Biological resource management and compliance
 
### Description

Before starting your data collection, you need to plan how you will manage the biological resources (samples, associated specimens or genetic resources) and the data related to your experiment. However, managing biological resources \- such as samples, associated specimens, and genetic materials \- requires strict compliance with national and international frameworks like the Nagoya Protocol and adherence to ethical principles such as the CARE (Collective Benefit, Authority to Control, Responsibility, and Ethics) Principles ({% cite Carroll2020-wb %}). While these frameworks are essential for promoting equitable benefit-sharing and responsible stewardship, they introduce significant data management challenges. Tracking the origin, consent, ownership, and permitted use of biological materials demands accurate and well-maintained metadata, persistent identifiers, and clear documentation of legal and ethical constraints. These requirements often vary across jurisdictions and can evolve over time, making it difficult to standardize processes across institutions and platforms. 

Here, we highlight key considerations to keep in mind when managing biological resource data, and we suggest relevant documents, standards, and frameworks to guide compliance and responsible data stewardship.

### Considerations

* Do you have the required national and international permits for sample collection?  
* Will your sampling include Indigenous locations and/or be associated with traditional knowledge?  
* What biological material should be biobanked and where (samples, specimens, genetic resources)?  
* How will the data be preserved and shared?

### Solutions

* Ensure that due diligence was made regarding Nagoya treaty compliance, possibly with the help of your national focal point or institutional help desk. The Global Genome Biodiversity Network ({% tool "ggbn" %}) has developed a [ABS FactSheet and answer page](https://wiki.ggbn.org/ggbn/ABS_Fact_Sheet_and_Answers_to_Frequently_Asked_Questions) to help their network of biobanks to comply with the Nagoya protocol. More information is available on the [Compliance monitoring & measurement](https://rdmkit.elixir-europe.org/compliance_monitoring#how-can-you-ethically-access-genetic-resources-of-another-country) page. The main steps are summarised below:  
  * Check whether the countries where the samples are to be collected have signed the protocol, and identify the national entities that are issuing the permits for sample collection through the Access and Benefit Sharing Clearing House ([ABSCH](https://absch.cbd.int/en/?_gl=1*1taqnzf*_ga*NTEwOTEwMTYyLjE3Mjc2ODQwOTQ.*_ga_7S1TPRE7F5*MTcyNzY4NDA5My4xLjEuMTcyNzY4NDE5My42MC4wLjA.))  
  * If required, obtain the Prior Informed Consent (PIC) and Mutually Agreed Terms (MAT) and the final national permit of collection from the relevant(s) national focal point(s).  
  * Submit a Due Diligence declaration to the European Web-portal DECLARE (for European researchers) or to the ABSCH to get your Internationally Recognized Certificate of Compliance (IRCC).   
* Ensure that CARE principals are taken into account. If the samples are related to Indigenous Peoples and/or Local Communities, engage with the relevant communities during the planning phase of the experiment ({% cite mc_cartney2023jk %}). Mc Cartney *et al* offer a framework, grounded in environmental justice and the CARE principles, for biodiversity genomic researchers, projects, and initiatives to support and promote the building of trustworthy and sustainable partnerships with Indigenous Peoples & Local Communities. Among other topics, engagement should consider:  
  * How the community will possibly access the specimens/samples collected and data generated.  
  * How the data will be labelled, accessed, and reused, including by the Indigenous communities for their own purposes, using, for example, [Local Contexts Labels and Notices](https://localcontexts.org/fr/).  
* Ensure that your Data Management Plan includes a section on specimen or biomaterial management or develop a specific Specimen management plan (see {% cite bentley2024bo %} for a proposal of guidelines). According to these guidelines this should include:  
  * The definition of the collections repository/biobank where the biomaterial will be stored.  
  * The type and anticipated number of specimens and/or samples, metadata collection and associated data.  
  * Plans for collection and preservation of the biomaterial that should be in line with established best practices for the relevant organisms (including the expectations of specimen curation and care).  
  * Plans for making the specimens/biomaterial available to the research community and for metadata publication and linkage to the data (also see recommendations for the digital extended specimen, {% cite hardisty2022nd %}).  
* You can find more information on Biobanking and data management in {% cite alkhatib2024dc %}.

## Biological material: metadata collection and publication
 
### Description

Collecting and organizing rich metadata for biological materials, such as those stored in biobanks or specimen collections, is essential for enabling data interpretation, reuse, and integration across biodiversity studies. These materials are often linked to other types of data, including genomic sequences, images, phenotypic traits, and environmental context, making consistent metadata especially critical. However, a major challenge lies in identifying and applying suitable metadata standards, as multiple frameworks exist with varying levels of compatibility, coverage, and specificity. This complexity can hinder the accurate and interoperable description of samples, their origin, and associated information. In addition, managing persistent identifiers and maintaining consistent metadata across biological materials and their associated data is crucial for ensuring long-term traceability and interoperability. 

Here, we suggest commonly used metadata standards, as well as repositories and registries for metadata publication, to support effective and FAIR-compliant biobanking and biodiversity data management.

### Considerations

Certain core metadata—such as collection date, biome, and geographical location—should always be collected to ensure basic contextualization and future usability. Beyond these essentials, the specific research context and use case will determine which additional metadata are most valuable. Key considerations include:

* Type of biological material: What kind of sample is being collected and analyzed (e.g., tissue, DNA, environmental sample)?  
* Type and intended use of data: What kind of data will be generated (e.g., genomic, phenotypic, environmental), and how is it expected to be used or reused?  
* Storage context: Will the biological material be preserved in a biobank, museum, or other long-term repository?  
* Data submission destination: Which database, repository, or registry will host the resulting data and metadata?

Collecting extensive (or "long-tail") metadata can greatly enhance data reuse and interoperability, but it also requires time and expertise. Therefore, metadata collection should be prioritized based on its anticipated value to future research and balanced against available human and technical resources.

### Solutions

* Consult your institution or project Data Management Plan to obtain information around the standard metadata that should be collected (also see [Documentation and metadata](https://rdmkit.elixir-europe.org/metadata_management#how-do-you-find-appropriate-standard-metadata-for-datasets-or-samples)), the procedures that should be used and the best practices for storing and sharing your data and metadata. Alternatively you can develop a Data Management Plan specific for your study following the guidelines available [here](https://rdmkit.elixir-europe.org/data_management_plan).  
* The metadata collected should be made available following community widespread standards to promote interoperability. The most relevant standards include the Genomics Standards Consortium Minimal Information About (X) Any Sequence ({% tool "mixs" %}, {% cite field2011of %}) for genomics data, Ecological Metadata Language ({% tool "eml" %}, {% cite michener1997rd %}) for general biodiversity data, and Darwin Core ({% tool "dwc" %}, {% cite wieczorek2012al %}) mainly for taxa and their occurrences. For DNA/RNA barcoding data, the Barcode of Life Database ({% tool "bold" %}, {% cite ratnasingham2007ji %}) is developing the Barcoding Data Model ([BCDM](https://github.com/DNAdiversity/BCDM)). The core {% tool "dwc" %} terms have been aligned with the {% tool "mixs" %} terms ({% cite meyer2023fm %}), with further work underway to align many DwC extension terms to increase the interoperability.

**Sample metadata and checklists**

* Assess the type of sample/organism being analysed and the type of data being produced to identify the relevant metadata to collect. Take into consideration that richer metadata collection enables greater reuse of biodiversity information.  
* Identify the appropriate sample metadata checklist for submission to a public repository. There are several checklists available for different types of samples and analyses:  
  * The {% tool "european-nucleotide-archive" %} has several [sample metadata checklists](https://www.ebi.ac.uk/ena/browser/checklists) for various sequence data types, part of these associated with biodiversity related data, that are adequate for different types of samples and research purposes.   
  * For reference barcodes, {% tool "bold" %} is using the Barcoding Data Model ([BCDM](https://github.com/DNAdiversity/BCDM)).  
  * For reference genomes there are specific guidelines regarding sample metadata collection. For example, the [ERGA](https://www.erga-biodiversity.eu/) (European Reference Genomes Atlas) initiative developed the [ERGA sample manifest](https://github.com/ERGA-consortium/ERGA-sample-manifest) that aligns with current standards and the [Tree of Life Checklist](https://www.ebi.ac.uk/ena/browser/view/ERC000053) at {% tool "european-nucleotide-archive" %}.  
* When referencing in the sample metadata information held in other repositories, as for example taxonomic information (also see the section Biological material: Taxonomic information), specimen collections or sampling protocols, always use persistent identifiers.  
* Also see this page on [documentation and metadata](https://rdmkit.elixir-europe.org/metadata_management).

**Biobanking and specimen linking**

* If possible keep vouchers and your tissues and DNA samples in a biobank/collection with relevant metadata (see Biological resource management and compliance)  
* The {% tool "ggbn" %} is a global network of curated collections of genomic samples, working together to make DNA and tissue collections discoverable for biodiversity research. {% tool "ggbn" %} is actively developing resources and recommendations for data management in relation to biobanking and specimen collections with their networks of repositories \- [GGBN data standard](https://wiki.ggbn.org/ggbn/GGBN_Data_Standard).   
* The Consortium of European Taxonomic Facilities ({% tool "cetaf" %}), an European Network of biological and geological collections, generates specimen identifiers for specimens in CETAF collections.  
* The European research infrastructure {% tool "dissco" %} (Distributed System of Scientific Collections) is working on developing a Digital Specimen Repository where DOIs will be provided for digital specimens.  
* In the sample metadata in {% tool "biosamples" %}, reference the specimen or tissue/DNA samples using persistent identifiers available or using the {% tool "dwc" %} standard (‘triplet’ that includes the institution and collection codes, and specimen catalogue number), see also recommendations in {% cite agosti2022vt %}.  
* In relation with collections of genetic resources that also encompass the intraspecific diversity, part of the recommendations are developed in the frame of FAO’s activities and completed through consortia of researchers supported by initiatives such as the Research Data Alliance.  
* You can also find relevant information by consulting other domain pages related to Biodiversity:  
  * link to Plant genetic resources: [https://rdmkit.elixir-europe.org/plant\_sciences](https://rdmkit.elixir-europe.org/plant_sciences)  
  * Link to Domestic animals: [https://data.faang.org/home](https://data.faang.org/home)   
  * Link to Microbial genetic resources: [https://www.mirri.org/microbial-resources-data/](https://www.mirri.org/microbial-resources-data/) 

**Sample metadata sharing and publication**

* Identify the repository where the sample metadata will be stored:  
  * For samples associated with genomic data, {% tool "biosamples" %} database is recommended, as a persistent identifier will be assigned that will be linked with the data.   
* You can also reach out to data brokers or use brokering tools, that can help manage metadata and data submission to public repositories, as for example:   
  * {% tool "copo" %} (Collaborative OPen Omics) is a data broker that is involved in metadata and data submission for the ERGA initiative  
  * {% tool "madbot" %} (Metadata And Data Brokering Online Tool) is a web application that provides a dashboard for managing research data and metadata.  
  * {% tool "galaxy-ecology" %}, a Biodiversity oriented Galaxy instance, proposing data brokers functionalities in a common platform. Some examples of the tools available:  
    * {% tool "ena-upload-tool" %} to publish in {% tool "european-nucleotide-archive" %},   
    * {% tool "eml" %} oriented tools allowing to create EML metadata,  
    * data packages that can be used to share data through international repositories as [DataONE](https://www.dataone.org/), accepting raw datafiles related to earth observation, or {% tool "gbif" %}, {% tool "obis" %}, [Emodnet](https://emodnet.ec.europa.eu/en) accepting DwC Archives related mainly to taxon occurrences.  
* Modern technology such as mobile phone apps can streamline registration and collection of standardised metadata and field measurements. Automation such as this can reduce the burden on the sample collectors and increase the metadata quality. A great example is the {% tool "nmdc-field-notes" %}.

## Biological material: Taxonomic information
 
### Description

Taxonomy is an evolving field and harmonisation is challenging. Multiple classifications exist for the same group of organisms and these are reported in many taxonomy databases with varying taxonomic and geographic coverage, and quality. For example, {% tool "worms" %}, the World Registry of Marine Species, holds an extensive record for marine species and [AlgaeBase](https://www.algaebase.org/) is a global database of algae including taxonomy, nomenclature and distributional information.   
The data repositories may be associated with or link to different taxonomic databases, so it is not always straightforward to understand what classification should be used in which situation. In addition, the advances in reference library production and in environmental DNA analysis lead to the discovery and identification of new taxa; submitting data for undescribed taxa or from environmental samples may also be challenging.   
This complex taxonomic foundation makes the reporting and linking of data to taxonomy challenging. The different public databases are used by researchers, but the taxonomic references in publications do not usually include persistent identifiers for taxon names or information regarding the taxonomy database used. Moreover, in some national biodiversity studies it is sometimes necessary to use other taxonomic reference systems that are more widely used by public monitoring agencies and that may not have persistent identifiers.

Here we present some considerations regarding ongoing initiatives to facilitate taxonomy mapping, clustering and linking, and provide some guidance for the submission and reporting of taxonomic information.  

### Considerations

There are multiple taxonomic checklists covering different geographic and taxonomic ranges that are included in multiple databases. These checklists follow rules in taxonomic naming that are guided by nomenclature codes according to the type of organism. Most taxon names are published in scientific literature, with a description (taxonomic treatment).  
In addition to published taxonomy, some taxonomic databases also include placeholders for undescribed species and/or clustering mechanisms that identify novel taxonomic units. A classification for environmental samples is also available in {% tool "ncbi-taxonomy" %}.   
Most of the main taxonomic databases and checklists services provide persistent identifiers in different forms for taxon names that should be used when referring to a species in a publication (see {% cite agosti2022vt %}).   
Therefore, key considerations include: 

* Does the work involve organisms or environmental samples?  
* Is the organism being analysed already published in a taxonomic journal?   
* Are there taxonomic treatments (descriptions of the taxa in publications) available for the species?  
* Which taxonomy checklist/backbone is being used?  
* Is there a persistent identifier available for the taxon name?

### Solutions

* If you have questions regarding taxonomic nomenclature you can consult the nomenclature codes, such as the {% tool "iczn" %} and the {% tool "iapt" %}.   
* You can also find information on Taxonomic treatments, i.e. detailed descriptions of a specific group of organisms (a taxon) within a scientific publication, and taxonomic citations on {% tool "treatmentbank" %}, which also provides persistent identifiers for the taxonomic names annotated in nomenclature sections of publications.  
* Choose the reference taxonomic backbone and reference it in the publication including a version if available.   
  * For sequence data, the most used taxonomic databases are {% tool "ncbi-taxonomy" %} used by the International Nucleotide Sequence Database Collaboration {% tool "international-nucleotide-sequence-database-collaboration" %} and {% tool "bold" %} [taxonomy](https://boldsystems.org/data/taxonomy-page/) used by the [International Barcode of Life](https://ibol.org/) (iBOL).  
* {% tool "ncbi-taxonomy" %}, in addition to the published taxon names, also allows for placeholder names for undescribed or novel species. These can then be updated once the taxon is published.   
* If you are using an unpublished name, use available processes for requesting the databases to mint an identifier to a placeholder name (for sequence data and {% tool "ncbi-taxonomy" %} see {% cite blaxter2024be %}).  
* If working with environmental samples, you can use {% tool "ncbi-taxonomy" %} (environmental biome level taxonomy).  
* There are also sequence clustering frameworks, used in some databases and management systems that identify novel taxonomic units (Operational Taxonomic Units \- OTU) and assign them with identifiers:  
  * {% tool "bold" %} processes barcode sequences through an online framework that clusters the sequences into units and generates Barcode Identification Numbers (BINs, {% cite ratnasingham2013yt %}).   
  * {% tool "unite" %}, a database that targets the nuclear ribosomal internal transcribed spacer (ITS) region and is used for molecular identification primarily of fungi, holds a pipeline that clusters ITS sequences into units, the UNITE Species Hypotheses (SHs) to which a unique DOI is assigned {% cite abarenkov2024du %}.  
  * The Catalogue of Life ({% tool "catalogue-of-life" %}) is a global collaboration between taxonomists and bioinformaticians aiming at gathering up-to-date listings of all the world’s known species. {% tool "catalogue-of-life" %} in collaboration with the {% tool "gbif" %} provides a global list of accepted names by integrating existing checklists, both from large scale and national initiatives. The {% tool "gbif" %} taxonomic backbone derives from {% tool "catalogue-of-life" %} and merges additional names from authoritative nomenclatural and taxonomic datasets including identifiers such as BINs from {% tool "bold" %} and SHs from {% tool "unite" %}.   
* Use mapping tools available to facilitate the discovery of taxon names and persistent identifiers, such as:   
  * {% tool "taxize" %} and {% tool "taxonomycleanr" %} R packages  
  * {% tool "checklistbank" %}, a repository of taxonomic datasets, developed in collaboration between {% tool "gbif" %} and {% tool "catalogue-of-life" %}, allows mapping of taxonomic names and identifiers between the different taxonomies/checklists in {% tool "catalogue-of-life" %}.  
* Use persistent identifiers for the taxon name in the data publication if available (e.g. {% tool "catalogue-of-life" %}, {% tool "ncbi-taxonomy" %}, {% tool "bold" %}, {% tool "unite" %}).

## Reference libraries: meta(data) collection and publication
 
### Description

Reference genomes (DNA sequences of an organism's genome) are crucial for scientists to study genetic diversity and evolutionary relationships within, and between populations and species. These also enable analysis of population and functional genomics that facilitate monitoring of ecosystems. [DNA barcoding](https://ibol.org/about/dna-barcoding/) instead consists of the analysis of short, standardised DNA sequences to identify organisms at the species level. This fast and cost-effective approach has helped revolutionise species detection in biodiversity using metabarcoding and eDNA methods. However, the accuracy of metabarcoding methods relies on well-curated DNA barcoding reference libraries, as they provide the essential benchmarks needed for correctly identifying and assigning DNA sequences to the right taxa.

The scaling up of both barcoding and reference genome production for documenting biodiversity raises some data management challenges. These include the application of sequencing, barcoding, and genome analysis standards, the availability and documentation of analysis tools and computing platforms, and the sharing of reference sequence libraries. Collecting rich metadata for reference libraries is essential for ensuring the utility, traceability, and interoperability of genomic data. Proper metadata facilitates comparisons, reproducibility, and downstream analyses.

Here, we highlight key considerations to keep in mind when annotating and sharing reference libraries, and we suggest relevant standards and tools.

### Considerations

* Is the relevant metadata about the specimens being collected and following the recommendations in the section Biological material: metadata collection and publication?  
* Consider collecting additional data, as for example, specimen images, that can be linked to the specimen.  
* Are the current standards for barcoding or reference genome production and publication being followed?  
* Are public bioinformatic pipelines being used or the bioinformatic pipelines and workflows being recorded in public repositories?  
* Consider making the data produced publicly available in an appropriate repository.

### Solutions

**Reference barcodes (meta)data collection and publication**

* Standards for barcoding are being developed by {% tool "bold" %}, the Barcoding Data Model ([BCDM](https://github.com/DNAdiversity/BCDM)) \- these include metadata for sample collection and processing as well as on sequence information and primers.   
* When additional data is collected, as for example, specimen image data, this should also be made available in a public repository. Some museum collections store and make available this information. {% tool "bold" %} stores image data linked with the specimen information. There are also specific databases, such as the {% tool "bioimagearchive" %}, where these are linked with the sample metadata in {% tool "biosamples" %}. For more information on bioimaging see the [BioImaging domain](https://rdmkit.elixir-europe.org/bioimaging_data).   
* The details of the laboratory processes and bioinformatic pipelines (including taxonomic assignment pipelines) and workflows used to produce the reference barcodes, should be captured and made available by registering them into {% tool "github" %} or {% tool "workflowhub" %} ({% cite gustafsson2024sh %}) and linking to them from the data.  
* Publish the samples, raw data (if high throughput sequencing is used) and barcode sequences in the relevant public repositories:  
  * Samples can be submitted to {% tool "bold" %} and to {% tool "biosamples" %}  
  * Raw data and curated barcodes can be submitted to the {% tool "international-nucleotide-sequence-database-collaboration" %} (e.g. in Europe to {% tool "european-nucleotide-archive" %})  
  * Curated barcodes can be submitted to {% tool "bold" %}  
* Use the appropriate reference libraries for your taxonomic area(s) of interest.

**Reference genomes (meta)data collection and publication**

* Standards for reference genomes production are published by the [Earth Biogenome Project](https://www.earthbiogenome.org/) \- these include reports on standards for sample collection and processing to genome analysis and annotations.   
* Reference genomes and raw sequence data should be submitted to the {% tool "international-nucleotide-sequence-database-collaboration" %}, through the {% tool "european-nucleotide-archive" %} (its European node) or {% tool "national-center-for-biotechnology-information" %} or {% tool "dna-data-bank-of-japan" %}, where all the data will be linked to the biosample and bioproject information.  
* When additional data is collected, as for example, specimen image data, this should also be made available in a public repository. Some museum collections also store and make available this information. There are also specific databases, such as the {% tool "bioimagearchive" %}, where these are linked with the sample metadata in {% tool "biosamples" %}. For more information on bioimaging see the [BioImaging domain](https://rdmkit.elixir-europe.org/bioimaging_data).   
* Analysis tools and pipelines should be published and linked to the data. There are some repositories available for capturing information on bioinformatic tools and databases (e.g. {% tool "github" %}, {% tool "bio-tools" %}) and on pipelines and workflows {% tool "workflowhub" %}.  
* The [European Reference Genome Atlas](https://www.erga-biodiversity.eu) (ERGA) initiative has a [Workflow Hub space](https://workflowhub.eu/programmes/33) where genome assembly, annotation and curation pipelines are available.  
* {% tool "genomes-on-a-tree" %} is a powerful data aggregator and portal for reference genomes.  
* You can also use data brokering services or brokering tools that can help manage metadata and data submission to the public repositories (see section on biological material: metadata collection and publication).  
* The bioproject accession should be included in the publication.

## Bibliography 

{% bibliography --cited %}
