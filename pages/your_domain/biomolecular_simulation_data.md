---
title: Biomolecular simulation data
keywords: [molecular dynamics, docking, virtual screening]
---
## General scope
Here we show what are (bio)simulation data, how we can store them, how it can be reused for new, unexpected projects, and how they can be transformed to make them FAIR (findable, accessible, interoperable and reusable). However, we should stress that these guidelines are not carved to stone and the biomolecular simulation community still needs to address challenges to FAIRify its data.

## Storing and sharing the data from biomolecular simulations
 
### Description

The biomolecular simulation data comes in several forms and multiple formats, which unfortunately are not completely interoperable. Different methods also require slightly different metadata description. 

### Considerations
* What type of data do you have?
  * Molecular dynamics data - by far the most typical and largest biomolecular simulation data. Each molecular dynamics simulation is driven by the used engine, force-field, and multiple other and often hidden simulation parameters to produce trajectories that are further analysed. 
  * Molecular docking data - docking provides the structures of the complex (e.g. ligand-protein, protein-protein, protein-nucleic acid, etc) and its score/energy. 
  * Virtual screening data - virtual screening is used for selection of active compounds from the pool of others. 
  * Free energies and other data from analysis - resulting final data stemming from the analysis of the simulations. 

* Where should you store this data?
  * There’s a long list of repositories available for storing scientific data, that can be divided in two main branches: 
    * Generic:  Repositories that can be used to store any kind of data.
    * Specific:  Repositories designed to store specific data (e.g. MD data).
  * Are you looking for a long-term or short-term storage? Repositories have different options (and sometimes prices) for the storage time of your data.
  * Do you need a static reference for your data? A code (identifier) that can uniquely identify and refer to your data?

*  What data should you store?
  * What type of data should you store from the whole bunch of data generated in our project. Again, the type of data might vary depending on the biomolecular simulation field.
  * Consider what is essential (absolutely needed to reproduce the simulated experiment) versus what can be extracted from this data (analyses). 

* How do you want your data to be shared?
  * You should consider the terms in which other scientists can use your data for other projects, access, modify, or redistribute them.  


### Possibilities / solutions
* Repositories (to be extended by the community) - There’s a long (and incomplete) list of repositories available for this, that can be divided in two main branches: 
  * Generic: Repositories that can be used to store any kind of data. 
    * [Zenodo](https://zenodo.org/)
    * [FigShare](https://figshare.com/)
    * [Mendeley data](https://data.mendeley.com/)
    * [DataDryad](https://datadryad.org/)
    * [OpenScienceFramework](https://osf.io/)
  * Specific: Repositories and databases designed to store specific data (e.g. MD data). 
    * Molecular Dynamics repositories
      * [GPCRmd](http://gpcrmd.org/) - for GPCR protein simulations, [with submission process](https://submission.gpcrmd.org/accounts/login/?next=/accounts/memberpage/).
      * [MoDEL](http://mmb.irbbarcelona.org/MoDEL/) - (https://bio.tools/model) specific database for protein MD simulations. 
      * [BigNASim](http://mmb.irbbarcelona.org/BigNASim/) - (https://bio.tools/bignasim) specific database for Nucleic Acids MD simulations, [with submission process](https://github.com/NMRLipids).
      * [MoDEL-CNS](http://mmb.irbbarcelona.org/MoDEL-CNS/#/) - specific database for Central Nervous System-related, mainly membrane protein, MD simulations.
      * [NMRlipids](http://nmrlipids.blogspot.com/) - project to validate lipid force fields with NMR data with submission process
      * [MolSSI - BioExcel COVID-19 therapeutics hub](https://covid.bioexcel.eu/) - database with COVID-19 related simulations, [with submission process](https://covid.bioexcel.eu/contributing/).

    * Molecular Dynamics databases
      * [BioExcel-CV19](https://bioexcel-cv19.bsc.es/#/) - database and associated web server to offer in a graphical way analyses on top of COVID-19 related MD trajectories stored in the MolSSI-BioExcel COVID-19 therapeutics hub.  
      * [Dynameomics](http://www.dynameomics.org/) - database of folding/unfolding pathways 
      * [MemprotMD](http://memprotmd.bioch.ox.ac.uk/) - database of automatically generated membrane proteins from PDB inserted into simulated lipid bilayers

    * Docking respositories
      * [MolSSI - BioExcel COVID-19 therapeutics hub](https://covid.bioexcel.eu/) - database with COVID-19 related simulations, [with submission process](https://covid.bioexcel.eu/contributing/).
      * [PDB-Dev](https://pdb-dev.wwpdb.org/) - prototype archiving system for structural models using integrative or hybrid modeling, [with submission process] (https://deposit.pdb-dev.wwpdb.org/accounts/login/?next=/account/).
      * [Model Archive](https://www.modelarchive.org/) - theoretical models of macromolecular structures, [with submission process](https://www.modelarchive.org/projects/new/basic).

    * Virtual Screening repositories:
      * [BioActiveConformationalEnsembles](http://mmb.irbbarcelona.org/BCE) - small molecule conformations, [with submission process](http://mmb.irbbarcelona.org/BCE/db/upload).
      * [BindingDB](https://www.bindingdb.org/) - database of measured binding affinities, focusing chiefly on the interactions of protein considered to be drug-targets with small, drug-like molecules, [with submission process](https://www.bindingdb.org/bind/contributedata.jsp). 

    * Free energies and other analyses: 
       * [MolMeDB](https://molmedb.upol.cz/) - for molecule-membrane interactions and free energy profiles, [with submission process](mailto:molmedb@upol.cz).  
       * [ChannelsDB](https://webchemdev.ncbr.muni.cz/ChannelsDB/index.html) - resource of channels, pores and tunnels found in biomacromolecules, [with submission process](https://webchemdev.ncbr.muni.cz/ChannelsDB/contribute.html).

* Type of Data to be Shared
  * Examples of types of essential and optional data depending on the biomolecular simulation data: 
    * Molecular Dynamics:
      * Essentials:
        * Metadata (Temperature, pressure, program, version, …)
        * Complete set of input files that were used in the simulations
        * Trajectory(ies)
        * Topology(ies)
      * Optionals:
        * Analysis data (Free energy, snapshots, clusterization)
    * Docking poses:
      * Essentials:
        * The complete set of molecules tested as well as the scoring functions used and the high-ranking, final poses (3D-structures)
        * Metadata (Identifiers (SMILES, InChI-Key), target (PDBID), energies/scores, program, version, box definition)
      * Optionals:
        * Complete ensemble of poses
    * Virtual Screening:
      * Essentials:
        * List of molecules sorted
        * Metadata (identifiers of ligands and decoy molecules, target, program+version, type of VS (QSAR, ML, Docking,...))
      * Optionals:
        * Details of the method, scores, ... 
    * Free energies and other analyses:
      * Essentials: 
        * Metadata (model, method, program, version, force field(s), etc.)
        * Values (Free energy values, channels, etc.)
      * Optionals:
        * Link to Trajectory (Dynamic PDB?)
* Data Licenses:
  * There’s a list of [datasets licenses available that you can find here](https://help.data.world/hc/en-us/articles/115006114287-Common-license-types-for-datasets). They mainly differ on openness vs restrictiveness. Read carefully to understand the differences and apply the one you think your data should have before distributing them.  

### Related problems
* File formats
Biomolecular simulation field has a tendency to produce a multitude of input/output formats, each of them mainly related to one software package. That makes interoperability and reproducibility really difficult. You can share your data but this data will only be useful if the scientist interested in it has access to the tool that has generated it. The field is working on possible standards (e.g. TNG trajectory).

* Metadata standards
There is no existing standard defining the type and format of the metadata needed to describe a particular project and its associated data. How to store the program, version, parameters used, input files, etc. is still an open question, which has been addressed in many ways and using many formats (json, xml, txt, etc.). Again, different initiatives exist trying to address this issue (see further references). 

* Data size
Data generated in the biomolecular simulation field is growing at an alarming pace. Making this data available to the scientific community sometimes means transferring them to a long-term storage, and even this a priori straightforward process can be cumbersome because of the large data size. 

## External links - further references
* [Sharing Data from Molecular Simulations](https://doi.org/10.1021/acs.jcim.9b00665)
* [Ten simple rules on how to create open access and reproducible molecular simulations of biological systems](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006649)
* [Surviving the deluge of biosimulation data](https://doi.org/10.1002/wcms.1449)
* [An efficient and extensible format, library, and API for binary trajectory data from molecular simulations](https://doi.org/10.1002/jcc.23495)
* [Standards for data handling](https://mmb.irbbarcelona.org/BigNASim/htmlib/help/pdf/d7.3_-_white_paper_on_standards_for_data_handling.pdf)

## Relevant tools and resources

{% include toollist.html tag="biomol sim" %}
