---
title: Enzymology and Biocatalysis
search_exclude: true
description: Data management solutions for enzymology and biocatalysis data.
contributors: [Carsten Kettner, Jürgen Pleiss, Johann Rohwer, Hans V. Westerhoff, Ulrike Wittig]
page_id: enzym_biocat
related_pages: 
  your_tasks: [data_publication, data_quality, metadata]
  tool_assembly: []
---

## Introduction

The enzymology and biocatalysis domain is concerned with the collection of experimental data that characterize biocatalysts with regards to their activity, specificity, selectivity, and catalytic mechanism in a chemical reaction. Biocatalysts are macromolecules of biological origin (or synthetic equivalents thereof) that are directly involved in, and enhance the rates of, chemical reactions without themselves being produced or consumed in them. They are mostly proteins (called enzymes) or RNA molecules (ribozymes), but can also be entire networks of enzymes and in living organisms. The complete characterisation of a biocatalyst comprises both structural and functional properties. Amino acid sequence, covalent modification, 3-dimensional structure, formulation, and functional properties constitute the former, whereas the kinetics, reaction stoichiometries (as given by the complete chemical equation of the reaction(s) catalyzed) , selectivity and specificity are parameters that contribute to the latter, functional aspects. The dynamic properties are often referred to as ‘enzyme activity data’. They are ultimately determined by the structural properties of the biocatalysts and their reactants, but the computation of the former from the latter is still much less accurate than inference from direct experimental measurement, which is what the domain ‘Enzymology and Biocatalysis’ focuses on. 

Thermodynamic parameters such as the equilibrium constant and standard Gibbs or metabolic energy of the reaction, are properties only of the complete chemical reaction catalyzed, yet worth mentioning in biocatalyst characterization because they can limit reaction rate, yield and efficiency. Similarly, the process conditions have a major effect on the kinetic and thermodynamic parameters. The parameters are calculated from a series of experimental raw data. Enzyme activity data are widely distributed in the literature and databases and are used when inferring and comparing reaction specificity and mechanisms, when comparing enzymes from various organisms, when trying to understand the physiological function of an enzyme and when making dynamic pathway models to understand genome function. 

Biochemical parameter values vary with the conditions around the biocatalyst. Neither the comparison nor corroboration, analysis or interpretation of this data is possible without specifying those conditions in the assessments. A complete description of the experiment including the materials and methods is therefore necessary for the data to be interoperable and FAIR, i.e., useful for the scientific community at large. Standards for reporting data, definitions of metadata and frameworks for structuring the data for the publication in databases and repositories and for the data exchange greatly assist researchers in carrying out the above tasks by sharing data, reproducing recent findings and collaborating in distributed projects.

Adherence to standards comes with extra requirements in terms of equipment, expense, training, assay conditions and assay time and is not always of immediate benefit of the study at hand. Yet, the utility of the data that comes out is greatly enhanced by the standardisation as is the impact of the work done. The increased impact and citation rate as well as the ‘quality stamp’ obtained, should motivate the adoption of the standards by the community in order to generate complete and robust datasets (manually written or in electronic notebooks) and to apply tools that allow interchangeability of data and to make these datasets publicly findable, available, interoperable and reusable in high quality.

## Standards-compliant data collection
 
### Description
The determination of functional parameters of biocatalysts does not always require catalytic turnover; equilibrium binding constants are functionally important too. Collections and reports of biocatalyst function data must contain a description of the experimental setup. In order to be complete, this should include the identity of the catalytic or binding entity (enzyme, protein, nucleic acid or other molecule), the biological origin or source of the molecule, its amino acid sequence, its purity (also in terms of the fraction that is in the native rather than a denatured state), its formulation, and other characteristics such as post-translational modifications, prosthetic groups, mutations, any modifications made to facilitate expression or purification, and oligomeric state if the biocatalysts forms complexes with itself. The methods and technologies used as well as the experimental conditions (temperature, pH, pressure, additives and solvents, pMg, ionic strength, medium osmolarity (If >0.3 M) and approximate macromolecule concentration) of the assay must be described, certainly if it is a new assay, but also if the assay has been published before (all too often minor modifications of experimental conditions are not reported, leading to irreproducibility and inutility; referencing publications with the original assay description is still recommended). Specific information regarding the operation mode, type of reaction vessel and mixing, and the environment of the reaction need to be provided in the reports. The manner in which the concentration of the added substrates was determined should be described.  In instances where catalytic activity or binding cannot be detected, an estimate of the limit of detection based on the sensitivity and error analysis of the assay should be provided. In such cases a positive control should be assayed, and this should be described. In case activity is observed, a negative control (e.g., with denatured biocatalyst) should be included and described. In end point essays, the way the reaction was brought to a halt should be described.

The analytical equipment (e.g. spectrophotometer, mass spectrometer), relevant metadata (e.g. wavelength), and the measured raw data should be reported, including the ways the measurements were calibrated (e.g. proton release by acid titration). By reporting the measured data (e.g. absorption) and the data used for calibration, the evaluation of concentrations becomes reproducible. Ambiguous terms such as “not detectable” should be avoided or extended by ‘at a detection limit of …’. A description of the software used for data analysis should be included along with calculated errors for all parameters and the biochemical model of the biocatalyst used by the analysis, inclusive of the mathematical equations used.

Additional information is required for both the investigation and reporting of the apparent equilibrium constants of reactions. Both the equilibrium constants and the standard states/conditions need to be clearly defined. When calculating and reporting the value of an equilibrium constant, the units of concentrations, the direction of the reaction as well as the procedure of the calculation of the equilibrium constant itself must be specified. Control experiments should always be performed to detect systematic failures or external effects to exclude interferences from the enzyme or the solution. The chemical equilibrium needs to be defined when the forward and reverse reactions proceed at the same rate (reaction quotient Q does not change with time). It should be demonstrated (e.g. by addition of more substrate) that the reaction did not stop because the biocatalyst lost activity. It should be demonstrated that the position of the measured equilibrium constant does not depend on the amount of added enzyme nor on the initial amount of substrate or product added. 

### Considerations
Prerequisite for the reproducibility of enzyme activity datasets is the reporting in a complete way, without omissions and without the lack of essential information that allows other researchers to corroborate, interpret and reuse the data. Therefore, the major questions to fulfill these aspects include:
* Which data are required to provide complete data sets?
* What is the minimal data accepted to be considered complete?
* What is the minimal data set required to make the data useful for studies of metabolic pathways?
* Which metadata describe both the materials and methods data and results data most appropriately?
* From where can I obtain the metadata?
* What should be the best way to define the metabolic energy of reactions, substrates and metabolites?
* How can I address thermodynamic issues in my experiments?
* How can I ensure that my datasets are reproducible?

### Solutions
The Standards for Reporting Enzymology Data (STRENDA) Commission, a community driven initiative has developed reporting standards that are unique for this domain and include
* [STRENDA Guidelines List Level 1a - Data required for a complete description of an experiment](https://www.beilstein-institut.de/en/projects/strenda/guidelines/#Level1A)
* [STRENDA Guidelines List Level 1b - Description of enzyme activity data](https://www.beilstein-institut.de/en/projects/strenda/guidelines/#Level1B)
* [Recommendations on the design and execution of experiments to obtain the apparent equilibrium constants of enzyme catalyzed reactions](https://www.beilstein-institut.de/en/projects/strenda/guidelines/#thermodynamics)
* [Recommendations on the reporting of the results to determine the equilibrium constant](https://www.beilstein-institut.de/en/projects/strenda/guidelines/#Level1B)
* [STRENDA Biocatalysis Guidelines and Metadata catalogue](https://github.com/Strenda-biocatalysis/Strenda-biocatalysis/tree/main), an extension of the STRENDA Guidelines towards some specialities in biocatalysis
The STRENDA Guidelines which initially propose reporting fundamental enzymology data has been extended by additional parameters for the description of biocatalysis experiments such as for reactors and vessels, mixing conditions and the formulation of the biocatalyst which can be studied in a solved or immobilized form. Not only parameters have been defined but also the corresponding metadata which assist researchers in describing both the biocatalyst and the reaction conditions in more detail.

The nomenclature of an enzyme should follow the systematic classification and numbering recommended by the [Enzyme Commission (EC)](https://iubmb.qmul.ac.uk/enzyme/rules.html) of the International Union of Biochemistry and Molecular Biology (IUBMB). The EC number classifies enzymes based on the catalyzing reaction. If a new enzyme is discovered or the classification changes an EC number can be proposed for reviewing at [https://www.enzyme-database.org/newform.php](https://www.enzyme-database.org/newform.php).

## Data structure and exchange
 
### Description
When sampling and collecting data for the purpose of deposition, sharing and exchanging, the data needs to be structured in a way that both the sender and the recipient of the data are enabled to directly integrate these into their own workflow, i.e. data exchange formats, repositories, databases etc. When structuring data, usually ontologies and metadata catalogs provide a valuable means for the integration of controlled vocabularies, ontologies and additional information that enriches the experimental data. Structured data is required that follows community-based principles to increase the findability of the data in the web.

### Considerations
Before data can be sampled in a structured way, frameworks and tools are required to assist the researcher in compiling complete and high-quality datasets. Therefore, the major questions that address the requirement of standardized and structured data include:
* How to assist with the implementation of repositories, databases and electronic lab notebooks?
* How to structure the data?
* Which ontologies to use?
* How to include ontologies in the definition of data fields?
* How to define metadata so as to enrich experimental data optimally?
* How to increase the findability of datasets?
* How to enhance the utility of data for users?

### Solutions
{% tool "enzymeml" %} is a data exchange format enabling the transfer of enzyme function data between instruments, electronic lab notebooks, modelling tools, and databases. It includes experimental raw data as well as metadata compliant with the STRENDA guidelines and {% tool "systems-biology-markup-language" %}.

{% tool "systems-biology-markup-language" %} is a data exchange format for computational systems biology to describe biological models including enzyme networks, their reactions and kinetic properties.

The model repositories {% tool "jws-online" %} and {% tool "biomodels" %} are home to a large variety of detailed kinetic models of cell biochemistry that are exchangeable through {% tool "systems-biology-markup-language" %}. The models are populated with curated parameter values based on experimental data. As such they serve to structure the data concerning enzymological parameters in a way that shows the implications of the parameter values for physiological functions. This makes models and data immediately useful for the non-modelling expert.

{% tool "bioschemas" %} is a framework that adds bio-related properties and types to {% tool "schemas-org" %} which aims at increasing the findability of datasets in the web. {% tool "schemas-org" %} is a general framework that enriches any webpage with additional metadata. However, as {% tool "schemas-org" %} is a general framework, Bioschemas introduces a domain-specific controlled vocabulary.

The {% tool "ontology-lookup-service" %} provides more than 260 ontologies in the various fields. For the biocatalysis and enzymology domain, the following ontologies may be of interest:
* {% tool "bioassay-ontology" %}
* {% tool "chebi" %}
* {% tool "cell-ontology" %} for cell types
* {% tool "brenda-tissue-ontology" %}, source of an enzyme comprising tissues, cell lines, cell types and cell cultures
* {% tool "protein-modification-ontology" %}
* {% tool "protein-ontology" %}

## Deposition, sharing and reusing of data
 
### Description
Because of their usefulness for comparative enzymology, as well as for understanding the functioning of biochemical pathways and networks through systems biology, data and results should be made available worldwide in the sense of FAIR data. This means that this data needs to be findable and accessible to allow other researchers and software to reuse and reproduce this data as well as to generate new knowledge through comparison and integration. Various databases cover different aspects of enzymology data including enzyme occurrence, catalyzed reactions, binding mechanisms, or kinetic properties. Most of the databases contain manually curated data from literature, while only few also support direct data submission of experimental data. 

### Considerations
* How to find appropriate resources for the deposition and reuse of enzymology data?
* How to upload enzymology and biocatalysis data?
* What is the prerequisite for the upload of data?
* What are the requirements for the publication of data in databases and repositories?
* Are there any tools that support researchers in uploading their data?
* Are the suggested databases and repositories open (freely accessible by the researchers)?
* How to meet the requirements of journals and funding agencies to provide a meaningful data availability statement?
* Is there an indicator of the quality of the data (e.g. in the senses of accuracy and proven reproducibility)?

### Solutions
* For the collection of experimental data in the laboratory electronic lab notebooks (e.g. {% tool "chemotion" %}, {% tool "openbis" %}) should be used to store raw and processed data along with metadata and corresponding protocols. 
* Enzyme-related repositories which enable the direct submission of enzyme function data and experimental conditions are {% tool "strenda-db" %} and {% tool "sabiork" %} via the data exchange formats {% tool "enzymeml" %} and {% tool "systems-biology-markup-language" %}. 
* {% tool "strenda-db" %} is a storage and search platform for authors who are preparing a manuscript containing functional enzymology data. Data sets entered in {% tool "strenda-db" %} are automatically checked for compliance with the {% tool "standards-for-reporting-enzyme-data" %} and prepared for publication after the journal’s reviewing process together with the corresponding paper. The direct deposition of experimental data in {% tool "strenda-db" %} by the authors not only ensures the completeness of information but also simplifies the integration of the data into other enzyme databases.
* Information about the effects of chemical compounds on enzyme protein targets can be uploaded to the {% tool "chembl" %} database.   
* Most of the databases containing enzymology data are based on information manually extracted from literature. The structured format of the literature data in such databases allows the export and reuse of enzyme data (e.g. kinetic parameters) as well as the automatic integration in processing tools for modelling or visualization. Manually curated databases containing enzyme function data are: {% tool "uniprot" %}, {% tool "brenda" %}, {% tool "sabiork" %}, {% tool "m-csa" %}, {% tool "ezcatdb" %}, {% tool "metacyc" %}. An overview about general and more specialized enzyme databases is given in [Enzyme Databases in the Era of Omics and Artificial Intelligence](https://doi.org/10.3390/ijms242316918).
* Besides literature based information there are databases e.g. {% tool "gotenzymes" %} containing predicted kinetic parameters for enzymes or {% tool "topenzyme" %} containing predicted enzyme structure models. 
* Further repositories which are neither domain specific nor store data in a structured way are % tool "zenodo" %}, % tool "figshare" %} and % tool "dataverse" %}. These repositories are often suggested by journals and funding agencies that may be unaware of awareness of the structured repositories mentioned above.

## Data processing
 
### Description
The primary data that emerge directly from experimental analysis are mostly extensive tables of observations (e.g. measured concentrations) as a function of time or of variations in conditions such as substrate concentrations. The functional data of enzyme kinetics and biocatalysis is a much reduced set, typically comprising kinetic and thermodynamic parameters such as equilibrium dissociation constants and Michaelis-Menten and catalytic constants. These parameters completely pin down mathematical models for the biocatalysts. These models then enable the calculation of the rate of the reaction catalyzed by the enzyme for a wide range of concentrations of substrates, products, modifiers, pH values and temperatures. A frequent example of such a model is the reversible Michaelis-Menten equation. The appropriateness of this model for the description of the biocatalyst function is often uncertain or an approximation. It is important that the model used is validated for the biocatalyst under consideration.

### Considerations
* How to find the most appropriate model for my data?
* How to infer the kinetic and thermodynamic parameters from the primary data?
* How to assess the accuracy and reliability of the kinetic and thermodynamic parameters?
* How and to what extent are experimental tests required for the validity of these kinetic models for the particular biocatalysts?

### Solutions
* Many examples of kinetic models for enzymes are available in standard enzyme kinetics textbooks. Moreover, simulation tools such as {% tool "copasi" %} and {% tool "jws-online" %} provide a predefined list of reference kinetic models from which the user can choose when entering a new enzyme reaction.
* {% tool "enzymeml" %} provides a standard format and data model for capturing the raw data, the metadata of the kinetic experiment, the kinetic model used for fitting and the final kinetic and thermodynamic parameters.
* The {% tool "pyenzyme" %} library facilitates the processing of data by providing a programmatic interface to {% tool "enzymeml" %}. {% tool "pyenzyme" %} also interfaces with computational systems biology tools such as {% tool "pysces" %} and {% tool "copasi" %} to assist with numerically solving the kinetic models for parameter estimation.
* Fitting statistics such as the Akaike Information Criterion (AIC) or Bayesian Information Criterion (BIC), which are commonly reported by fitting libraries, can be used to select the most appropriate model from different alternatives.


