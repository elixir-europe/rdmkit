---
title: Plant Genomics
contributors: [Anne-Françoise Adam-Blondon, Cyril Pommier, Daniel Faria, Paulette Lieby, Sebastian Beier]
description: Tool assembly for managing plant genomic data. 
page_id: plant geno assembly
affiliations:
audience: [ALL]
related_pages: 
  your_tasks: [metadata]
  your_domain: [plants]
---

## What is the plant genomics tool assembly?
The plant genomics tool assembly is a toolkit for the management of plant genomics and genotyping data throughout its lifecycle, with a particular focus on ensuring traceability of the biological materials to enable interoperability with plant phenotyping data.

## Who can use the plant genomics tool assembly?
This tool assembly can be used by any researcher producing plant genomic or genotyping data interested in ensuring their data complies with the FAIR principles.

## How can you access the plant genomics tool assembly?
All the components of this tool assembly are publicly available, but most require registration. So anyone can access the tool assembly provided they register for each tool that requires it.


## For what purpose can you use the plant genomics tool assembly?
{% include image.html file="plant_genomics.svg" caption="Figure 1. The plant genomics tool assembly." alt="Tools and resources used in managing plant genomics and genotyping data." %}

### Metadata collection and tracking
Accurate [documentation](metadata_management.html) of the plant biological materials and samples is critical for interoperability, and should comply with the [MIAPPE](https://www.miappe.org/) standard.
This information should be submitted to [BioSamples](https://www.ebi.ac.uk/biosamples/), with MIAPPE compliance validated using BioSamples' [plant-miappe.json](https://github.com/EBIBioSamples/biosamples-v4/blob/biohackathon_miappe_checklist/webapps/core/src/main/resources/schemas/certification/plant-miappe.json) template.
Submission of sample descriptions to BioSamples can be done as early as the data collection stage, but at the latest, must acompany submission of the genomic data to the [European Nucleotide Archive](https://www.ebi.ac.uk/ena/browser/home) (ENA) or of genotyping data to the [European Variation Archive](https://www.ebi.ac.uk/eva/) (EVA).
[e!DAL-PGP](https://edal-pgp.ipk-gatersleben.de/) can be used to manage and share experimental metadata, as well as data.

### Data processing and analysis
Reference genomes for genome assembly and annotation should be obtained from [ENSEMBL Plants](https://plants.ensembl.org/index.html), if available.
Genetic variant data must be produced in the VCF format, and validated using the EVA vcf-validator (https://github.com/EBIvariation/vcf-validator).

### Data sharing and publishing
Plant genomic data should be submitted to ENA together with metadata compliant to the [GSC MIxS plant associated checklist](https://www.ebi.ac.uk/ena/browser/view/ERC000020), whereas plant genotyping data should be submitted to EVA.
Additionally, data can also be published in e!DAL-PGP.

