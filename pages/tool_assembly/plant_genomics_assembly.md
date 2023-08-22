---
title: Plant Genomics
contributors: [Anne-Françoise Adam-Blondon, Cyril Pommier, Daniel Faria, Paulette Lieby, Sebastian Beier, Erwan Le Floch]
description: Tool assembly for managing plant genomic data.
page_id: plant_geno_assembly
affiliations:
related_pages: 
  your_tasks: [metadata, data_publication]
  your_domain: [plants]
  tool_assembly: [plant_pheno_assembly]
faircookbook:
- name: Improving dataset maturity - the MIAPPE use case
  url: https://w3id.org/faircookbook/FCB061
---

## What is the plant genomics tool assembly?
The plant genomics tool assembly is a toolkit for managing plant genomics and genotyping data throughout their life cycle, with a particular focus on ensuring traceability of the biological material to enable interoperability with plant phenotyping data. To enable this, the same persistent identifiers must be used in both the genotyping and phenotyping experiments. It is recommended that the biological plant material is accurately described using rich metadata and stored in a central repository. The tool assembly also provides guidance on how users should structure their analysis results in the form of VCF files to achieve a higher degree of interoperability.

## Who can use the plant genomics tool assembly?
This tool assembly can be used by any researcher producing plant genomic or genotyping data interested in ensuring their data complies with the FAIR principles.

## How can you access the plant genomics tool assembly?
All the components of this tool assembly are publicly available, but most require registration. So anyone can access the tool assembly provided they register for each tool that requires it.

## For what purpose can you use the plant genomics tool assembly?
{% include image.html file="plant_genomics.svg" caption="Figure 1. The plant genomics tool assembly." alt="Tools and resources used in managing plant genomics and genotyping data." %}

### Data management planning
The general principles to be considered are described in the [Plant Sciences domain page](plant_sciences).

* [Data Stewardship Wizard (DSW)](https://ds-wizard.org/) is a human-friendly tool for machine-actionable DMP collaborative editing. The DSW Plant Sciences project template, available on [ELIXIR's DSW instance for researchers](https://researchers.ds-wizard.org) can be used for any plant sciences project. When creating the DMP Project, choose the option "[From Project Template](https://researchers.ds-wizard.org/projects/create/from-template)" and search for the "Plant Sciences" template.

### Metadata collection and tracking
Accurate [documentation](metadata_management) of the plant biological materials and samples is critical for interoperability, and should comply with the {% tool "miappe" %} standard.
This information should be submitted to {% tool "biosamples" %}, with MIAPPE compliance validated using BioSamples' [plant-miappe.json](https://github.com/EBIBioSamples/biosamples-v4/blob/biohackathon_miappe_checklist/webapps/core/src/main/resources/schemas/certification/plant-miappe.json) template available on the [sample validation](https://www.ebi.ac.uk/biosamples/docs/guides/validation) page.
Submission of sample descriptions to BioSamples can be done as early as the data collection stage, but at the latest, must acompany submission of the genomic data to the {% tool "european-nucleotide-archive" %} (ENA) or of genotyping data to the {% tool "european-variation-archive" %} (EVA). The complete timeline for submitting plant biological material to BioSamples and resulting genotyping experiment results to ENA and EVA should look like this:
1.  Register plant biological material information to BioSamples
2.  Submit Sequencing reads to ENA (using BioSamples IDs to identify material)
3.  Check if used reference genome assembly is INSDC available (GCF / GCA accesion number available)
    1. If yes proceed to submit VCF at step 4, if no proceed to step 3 b
    2. Submit reference genome assembly to INSDC (NCBI Genbank / EBML-EBI ENA / DDBJ) and wait until accession number is issued, then proceed to step 4
4.  Submit VCF file to EVA (using BioSamples IDs to identify material, GCF/GCA accession for the reference genome assembly)

{% include callout.html type="note" content="Metadata associated with a single sample registered with BioSamples can only be updated from the original account." %}

{% tool "e-dal-pgp" %}, FAIRDOM-SEEK instances such as {% tool "fairdomhub" %} or [Recherche Data Gouv](https://recherche.data.gouv.fr/) can be used to manage and share experimental metadata, as well as data.

### Data processing and analysis
Reference genomes for genome assembly and annotation should be obtained from {% tool "ensembl-plants" %} or {% tool "plaza" %}, if available.
Genetic variant data must be produced in the VCF format, and validated using the EVA vcf-validator (https://github.com/EBIvariation/vcf-validator). Please note to only use identifiers of sequences that match the reference genome assembly identifiers.
In order to ensure interoperability of VCF files, the VCF meta-information lines should be used: see the [Plant sciences page](plant_sciences#plant-genotyping-data-sharing-and-deposition) for more details.

### Data sharing and publishing
All sequencing data collected in plant genotyping experiments should be submitted to ENA together with metadata compliant to the [GSC MIxS plant associated checklist](https://www.ebi.ac.uk/ena/browser/view/ERC000020). Final results of such studies in the form of VCF files should be submitted to EVA. Additionally, supplemental data complementing these two data types is encouraged to be submitted to {% tool "e-dal-pgp" %} or [Recherche Data Gouv](https://recherche.data.gouv.fr/).
