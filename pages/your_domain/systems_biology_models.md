---
title: Systems biology models
search_exclude: false
description: Data management of systems biology models.
contributors: [Carissa Bleker, Frank T. Bergmann, Mihail Anton, Ulrike Wittig]
editors: [Federico Bianchini]
page_id: sysbio_models
related_pages: 
  Your_tasks: [data_analysis, identifiers, licensing, data_publication, metadata, data_quality, data_provenance, machine_actionability, data_discoverability]
  Your_domain: [enzym_biocat, micro_biotech]
  Tool_assembly: []
training:
  - name: TeSS Systems Biology Collection
    registry: TeSS
    url: https://tess.elixir-europe.org/collections/elixir-systems-biology-community-training-events-and-materials1
  - name: TeSS Systems Biology search
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=systems+biology
---

## Introduction

Systems biology leverages computational models to integrate heterogeneous data, formalise biological hypotheses, and generate reproducible predictions. This page focuses specifically on computational and executable models used in systems biology and not on broader systems biology analyses such as omics integration, network analysis, machine learning, or statistical data analysis. These models often evolve over time, are reused in new contexts, and depend on complex software ecosystems. As a result, robust research data management (RDM) practices are essential to ensure that systems biology models remain interpretable, reproducible, and reusable {% cite niarakis2022Addressing %}.

Data management in systems biology encompasses three closely related categories of consideration. First, it concerns the models themselves, including their structure, implementation, documentation, and versioning. Second, it includes the data used to develop, parameterise, and validate models, such as experimental measurements, reference datasets, and derived parameters. Third, it covers *in silico* experiments, including computational workflows used to generate results, and the resulting model simulations and analyses. Effective research data management must address all three categories to ensure that systems biology studies are reproducible, interpretable, and reusable across different contexts and over time.

This page provides practical recommendations for managing systems biology models throughout their life cycle, aligned with the FAIR (Findable, Accessible, Interoperable, Reusable) and CURE (Credible, Understandable, Reproducible, Extensible) principles {% cite sauro2026FAIR %}. It focuses on the first and last of the above categories: the models themselves and simulation experiments and code, since these are essential for making models FAIR. The data used to develop and validate models is covered only where it affects the model, for example through provenance. For managing the experimental data itself, see the relevant domain pages, for example [Enzymology and biocatalysis](enzymology_and_biocatalysis) for the enzyme kinetic data used to parameterise kinetic models.

### What constitutes a systems biology model?

A systems biology model is a formal representation of a biological system that captures its relevant components and their interactions in order to explain, predict, or investigate the system's behaviour. Following the CURE principles, we define a mechanistic model as a representation of a biological system described in terms of its constituent parts and the processes that occur between them. For example, the proteins, phosphorylation states, and enzymatic transformations in a cell-signalling model. Such models can exist at several complementary levels:

- a conceptual model – a qualitative biological/map representation of the system's components and interactions;
- a computational model – a formal mathematical description of the system (e.g. a system of ordinary differential equations (ODEs), stochastic reaction networks, Boolean rules, agent-based models, or a constraint-based network); or
- an executable model – the model instantiated in software or code that can be run to generate simulations and predictions.

### When does RDM come in?

RDM is not a final step carried out once a model is finished. It runs through the whole model life cycle, and choices made early can be costly to change later.

The figure below places model development recommendations along the model life cycle in three phases {% cite hancock2026Making %}. The RDM activities fall into the same phases:

- Before model development: start with a modular and transparent design; use standardised, open formats; plan how the model and its files will be organised.
- During model development: an iterative cycle of testing, describing, and community review of the model, underpinned throughout by versioning and documentation of changes.
- After model development: depositing the version of record in a repository with a persistent identifier, ensuring open access under a clear licence, providing complete metadata, and sharing the simulation experiments and code needed to reproduce results (and checking that they do).

Models are often revised after an initial release, so each new version cycles back through the same steps.

{% capture figure1_caption %}Figure 1. Ten priorities for FAIR and CURE-compliant models mapped onto the model development life cycle (Hancock et al. 2026) {% cite hancock2026Making %}.{% endcapture %}
{% include image.html file="systems_biology_life_cycle_FAIR_CURE.png" caption=figure1_caption alt="Model development life cycle in three phases. Before: use modular and transparent design; use standardised, open formats. During: validate and test, describe and annotate, and engage in community curation, in a cycle supported by versioning and documenting all changes. After: assign persistent identifiers, ensure open access to code and data, provide complete metadata, and share simulation protocols and parameters. Each priority is tagged with the FAIR and CURE principles it supports." %}

## Organise the model in a modular and transparent way

### Description

How a model is structured affects how well it can be managed, reused, and extended. Modular organisation separates biological subsystems, mathematical formulations, and parameter definitions into well-defined components. Transparent organisation means the structure, assumptions, and provenance of the model and its data can be readily inspected and understood.

### Considerations

- Highly coupled or monolithic models are hard to interpret, version, validate, and especially reuse.
- Early design decisions strongly influence downstream reproducibility and extensibility.
- Parameter values and simulation settings that are hard-coded into the model cannot be shared, updated, or reused separately.
- Modules are only reusable if their interfaces and origin are documented.
- Different model types are organised differently, for example reaction networks, rule sets, and Boolean update functions.

### Solutions

- Decompose models into biologically meaningful submodels or modules that can be used independently. For {% tool "systems-biology-markup-language" %} models, consider using hierarchical model composition ([SBML Level 3 comp package](https://sbml.org/documents/specifications/level-3/version-1/comp/)) to explicitly encode modular model structure.
- Separate model structure from parameter values and simulation settings.
- Use clear naming conventions and consistent model organisation.
- Record the origin of data, parameters, and reused modules ([data provenance](data_provenance)), so their lineage can be traced.
- Document design choices directly within the model or accompanying documentation.

## Use standardised, open formats

### Description

Standardised, open model formats enable interoperability between software tools and facilitate long-term accessibility. In systems biology, community standards support model exchange, simulation, and validation across platforms. Different aspects of a modelling study, such as the model, the simulation experiments, and the parameter estimation problems, are covered by complementary standards. The COmputational Modeling in BIology NEtwork ([COMBINE](https://co.mbine.org/)) is an initiative to coordinate the development of the various community standards and formats for computational models.

### Considerations

- The right format depends on the type of model and what it will be used for.
- Format choice is easiest before development starts, because converting later can lose information.
- A model format does not describe how to simulate it or how its parameters were estimated. Simulation experiments and parameter estimation problems need complementary standards (see [Share simulation experiments and the code to run them](#share-simulation-experiments-and-the-code-to-run-them)).
- Proprietary or undocumented formats risk becoming unreadable.

### Solutions

- Encode models using established open standards that suit the model type. COMBINE maintains a list of supported formats in {% tool "fairsharing" %} ([COMBINE collection](https://doi.org/10.25504/FAIRsharing.ad3f2b)). For example:
  - Biochemical reaction networks (e.g. kinetic/ODE models): {% tool "systems-biology-markup-language" %}
  - Multiscale physiological models: {% tool "cellml" %}
  - Constraint-based (including genome-scale metabolic) models: SBML with the [Flux Balance Constraints (fbc) package](https://sbml.org/documents/specifications/level-3/version-1/fbc/)
  - Logical/Boolean models: SBML with the [Qualitative Models (qual) package](https://sbml.org/documents/specifications/level-3/version-1/qual/) (SBML-qual)
  - Modular and hierarchical models: SBML with the [comp package](https://sbml.org/documents/specifications/level-3/version-1/comp/)
  - Multistate molecular species and rule-based representations: SBML with the [multi package](https://sbml.org/documents/specifications/level-3/version-1/multi/)
  - Physiologically based kinetic (PBK) models: SBML following the {% tool "fair-pbk-standard" %}
  - Diagrams and maps of the model: SBGN-ML (the file format of the {% tool "systems-biology-graphical-notation" %}), or the SBML [layout](https://sbml.org/documents/specifications/level-3/version-1/layout/) and [rendering](https://sbml.org/documents/specifications/level-3/version-1/render/) packages.
- State which standards, file formats, and annotation frameworks were used, so that others can judge the model's interoperability and reuse.
- Provide input data (e.g. dose or exposure in PBK models) as external inputs rather than hard-coding them.
- Use complementary standards for the other parts of a modelling study: {% tool "sed-ml" %} for simulation experiments, {% tool "petab" %} for parameter estimation problems, and {% tool "combine-archive" %} to package these artefacts into a single exchange format.
- Avoid proprietary or undocumented file formats for core model representations.

## Annotate the model

### Description

Annotation links the components of a model (species, reactions, genes, parameters, units) to entries in standard identifier systems and ontologies. This lets people and software tell exactly what each component is and how it relates to other resources, so models can be compared, merged, and searched.

### Considerations

- Names and labels are ambiguous and differ between models. Identifiers are not ambiguous.
- Annotation support depends on the model format and type, so the annotation route should be chosen with the format.
- Annotations only help if the identifiers are stable and resolvable. Some repositories, such as {% tool "biomodels" %}, check this.
- The right identifier system depends on the type of component (genes, metabolites, reactions, units, processes).
- Annotations may become outdated when the model changes.
- Semantic annotations should be sufficiently detailed to allow automated comparison, merging, and reuse of models across repositories and software platforms.

### Solutions

- Store annotations in the model file and model metadata.
- Follow the {% tool "miriam" %} guidelines, and annotate each component with identifiers from standard resources, preferably in resolvable form, for example {% tool "identifiers-org" %} URLs (see the [identifiers](identifiers) page).
- Choose namespaces and ontologies from the FAIRsharing collection of [Systems Biology Identifier Systems and Ontologies](https://fairsharing.org/8014/).
- Annotate units as well as components where the format allows it. For SBML models, {% tool "sbmlutils" %} can add MIRIAM annotations and SBO terms and check that units are consistent.
- For PBK models, use the {% tool "fair-pbk-inspector" %} to annotate components and units and to validate the model against the FAIR PBK standard.
- Deposit the model in a repository that checks annotations, such as {% tool "biomodels" %} (see [Deposit, license, and publish](#deposit-license-and-publish)).
- Re-check and update annotations with each new model version.

## Describe the model

### Description

A thorough model description is essential for correct interpretation and reuse. This includes biological context, mathematical formulation, data sources, assumptions, and known limitations.

### Considerations

- A description written for people complements, but does not replace, machine-readable annotation (see [Annotate the model](#annotate-the-model)).
- Documentation held only in a journal article, supplementary file, or project website is easily lost or separated from the model.
- A journal article or its supplementary material is static and rarely holds everything users need.
- A description should not only include what the model is for, but also what it should not be used for.
- The description needs updating when the model changes.

### Solutions

- Provide a clear narrative description of model purpose and scope.
- Explicitly state biological and mathematical assumptions.
- Document parameter sources, estimation methods, calibration procedures, and optimisation settings used to derive model parameters. When parameters come from a database, cite the specific entries, for example from {% tool "sabiork" %} for enzyme kinetic parameters (see also [Enzymology and biocatalysis](enzymology_and_biocatalysis)).
- Specify which datasets were used for model construction, calibration, and independent validation, including persistent identifiers where available.
- Describe limitations and intended use, including the conditions and parameter ranges for which the model was developed and tested.
- Include the elements below, within the model file itself when possible, or in the accompanying documentation:
  - Authorship – Authors and contributors (preferably including {% tool "orcid" %} or similar IDs where available)
  - Model type and operational context – The type of model and how it is used, for example using the {% tool "mathematical-modelling-ontology" %}
  - Model structure – For complex models (for example hierarchical, modular, or multi-agent models), a description of the modules, submodels, and their relationships
  - Model lineage – Whether the model is based on an existing one, with a citation and a link to its source
  - Equations – A readable listing in the documentation, not only in the model file or supplementary material. For SBML models, {% tool "sbml4humans" %} generates an interactive, human-readable report of the model's components and annotations
  - Graphical presentation – A diagram of the model structure that accurately represents the model
- Record technical [metadata](metadata_management): model format and version, the software and versions used to build and run the model, its dependencies, and the computing environment.
- Provide the description as a free-standing document, in a persistent repository that issues digital object identifiers (DOIs), such as {% tool "github" %} ([via Zenodo](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)), {% tool "zenodo" %}, {% tool "figshare" %}, {% tool "dryad" %}, or {% tool "fairdomhub" %}. Link it to the model's persistent identifier, and link the model back to the description.
- Update the description in each new version (see [Version and document all changes](#version-and-document-all-changes)).

## Version and document all changes

### Description

Systems biology models often evolve through iterative development. Versioning allows users to track changes, reproduce past results, and understand how (and why) a model has developed over time.

### Considerations

- Without a clear version history, a published result cannot be tied to the exact model that produced it.
- Versioning should begin from the start of development, not only at publication.
- Changes should be documented where users will find them.

### Solutions

- Use version control systems to manage model development (see also [file versioning](data_organisation#how-do-you-manage-file-versioning)), for example using {% tool "github" %} and linking the repository to {% tool "zenodo" %} to obtain a DOI for each release, as in {% tool "standard-gem" %}. See GitHub's guide on [referencing and citing content](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).
- Maintain clear change logs describing modifications between versions.
- Tag stable releases associated with publications or analyses.
- Archive major versions in persistent repositories.

## Deposit, license, and publish

### Description

Depositing a model in a trusted repository gives it a persistent identifier, preserves it long term, and makes it citable. Open access here means access to the whole model as a research object (model, code, parameters, metadata, protocols, version history, and licence), not only a free article. See also [data publication](data_publication) and [licensing](licensing).

### Considerations

- Links to models hosted on personal, institutional, or journal websites often break over time, so these are not a substitute for a repository.
- Repositories differ in trustworthiness and sustainability. The [TRUST principles](https://doi.org/10.25504/FAIRsharing.03bb0d) (Transparency, Responsibility, User focus, Sustainability, Technology) help in comparing them.
- Permissive Creative Commons licences (CC0, CC BY) maximise reuse. More restrictive ones (e.g. CC BY-NC) can conflict with funder, journal, or repository policies.
- Journal requirements can influence the choice of repository.
- Openness is not always appropriate, for example with sensitive, personal, or proprietary material. In those cases, state the access conditions clearly.

### Solutions

- Deposit the model, code, and associated files in a repository that assigns persistent identifiers such as DOIs, and link the identifier to a specific versioned release.
- Domain repositories such as {% tool "biomodels" %} add expert curation and checks. Use one when your model type is supported.
- The FAIRsharing collection of [Systems Biology Model Repositories](https://fairsharing.org/6576) lists model repositories.
- General-purpose repositories that assign persistent identifiers, such as {% tool "fairdomhub" %}, {% tool "zenodo" %}, and {% tool "figshare" %}, can also be used.
- Reference persistent identifiers in publications and documentation.
- Choose a clear licence that is as open as possible (e.g. CC0 or CC BY), for example with the {% tool "creative-commons-license-chooser" %}, and state it in the repository and in the model documentation.
- Creative Commons licences are not recommended for software, so license code (e.g. simulation scripts) under an open-source licence instead, for example with the help of {% tool "choose-a-license" %}.
- State the access conditions explicitly, and include every file needed to reproduce the published results.

## Share simulation experiments and the code to run them

### Description

Reproducible simulation results depend not only on the model structure but also on the simulation protocols, parameter sets, execution settings, and software used to run it. The model and the code to run it should both be shared, although they can be stored separately.

### Considerations

- Reproducing a result needs more than the model: the solver, settings, initial conditions, and parameter values all matter.
- Users are likely to run the model under conditions different from those in the original publication, so units, inputs, and operating conditions should be stated, not assumed to be obvious.
- Code shared in raw form must be compiled and run by the user, which becomes harder as software ages ("bit rot").
- The right reproducibility check depends on the model type.
- Reproducibility is easier to demonstrate when the protocol is machine-readable and can run on more than one simulation engine.
- Parameter estimation depends on the experimental data, observables, and settings used, so these need to be shared along with the model.

### Solutions

- Share simulation scripts, protocols, and configuration files.
- Document solver choices, algorithm, initial conditions, parameter values, and any data normalisation, along with the software and programming environment used.
- Declare the units of inputs, outputs, and parameters, and the environmental conditions the model assumes (e.g. growth medium).
- Provide example inputs and the expected outputs, so users can test that their own instantiation behaves as expected.
- Use {% tool "sed-ml" %} (Simulation Experiment Description Markup Language) as the standardised route for encoding which models, parameters, simulation procedures, and output plots are used. It implements the {% tool "miase" %} guidelines.
- Specify parameter estimation problems, including experimental data, observables, simulation conditions, parameters, and optimisation settings, in {% tool "petab" %}.
- Package the code together with its dependencies so it can still be run later, for example in a software container ({% tool "apptainer" %} or {% tool "docker" %}) that runs across operating systems. Record the programming language, compiler version, and other dependencies (see [Describe the model](#describe-the-model)).
- Bundle the model with its simulation experiments, metadata, and documentation in a single package. The {% tool "combine-archive" %} is the systems biology option. {% tool "research-object-crate" %} is a generic one: it links all parts of a modelling experiment and can be published on {% tool "zenodo" %} with a DOI.
- Use platforms that support simulation experiments: {% tool "fairdomhub" %} can organise, annotate, and publish modelling experiments together with their data and protocols, and {% tool "biosimulators" %} can run SED-ML files across a range of simulation tools and export Docker images.
- Check models for errors before publication or repository submission, for example with the {% tool "sbml-validator" %}.
- State the platforms and tools on which the model has been tested (for example {% tool "copasi" %}, {% tool "tellurium" %}, {% tool "opencor" %}, MATLAB-based workflows, or BioSimulators-compatible simulation engines).

## Check and report reproducibility

### Description

Reproducibility is the capacity to independently reproduce simulation results, either by writing the code from scratch or by using different software, with the outputs matching within an acceptable numerical tolerance {% cite tiwari2021Reproducibility %}. It underpins the credibility of a model and is interrelated with the other FAIR and CURE principles. Checking it, and reporting how it was checked, shows users and reviewers that the shared files really do give the published results.

### Considerations

- Different model types raise different reproducibility challenges and may need specialised checks.
- [Machine-actionable](machine_actionability) protocols make checks easier.
- A check is only useful to others if its use is reported, so that reviewers can judge whether a model is genuinely repeatable.

### Solutions

- Run the shared {% tool "sed-ml" %} file on more than one simulation engine, for example through {% tool "biosimulators" %}, and compare the outputs within tolerance.
- Apply a reproducibility scorecard where available, such as the [BioModels 8-point reproducibility scorecard](https://www.biomodels.org/reproducibility).
- Use model-type-specific reproducibility checks when possible, for example:
  - [FROG](https://www.biomodels.org/curation/fbc) analysis (Flux variability, Reaction deletion, Objective function, Gene deletion) for genome-scale/constraint-based models;
  - {% tool "memote" %} for genome-scale metabolic models, which tests annotation, stoichiometric consistency, and SBML compliance;
  - EFECT (Empirical Characteristic Function Equality Convergence Test) for stochastic simulation studies, as implemented in {% tool "libssr" %};
  - the validation pipeline of {% tool "biodivine-boolean-models" %} for consistency checks of logical/Boolean models.
- Clearly describe which scorecards or analyses were applied, so reviewers and users can assess repeatability.

## Bibliography

{% bibliography --cited %}
