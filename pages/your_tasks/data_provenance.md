---
title: Data provenance
description: How to record information about data provenance.
contributors: [Flora D'Anna, Korbinian Bösl, Nazeefa Fatima]
page_id: data_provenance
related_pages: 
  tool_assembly: []
training:
  - name:
    registry:
    url:
---

## How to document and track your data provenance?
 
### Description

Provenance is the documentation of why and how the data (but also datasets, computational analysis and other research output) was produced, where, when and by whom. 
Data provenance is often used interchangeably with the term “data lineage”, although their definition might slightly differs in some contexts. 
Data provenance/lineage means tracing the movements and the changes of the data that occurred between their origin and their destination system.

Well-documented data provenance is essential for assessing authenticity, credibility, trustworthiness, quality (it helps finding errors) and reusability of data, as well as the reproducibility of the results.

However, knowing what’s the best way to document provenance can be challenging due to the large amount and variety of the information that need to be recorded.

### Considerations

- Provence is part of [documentation and metadata](metadata_management).
- Many aspects of data documentation and metadata are related to provenance information, such as history log, versioning, licence, citation, identifiers, etc. Moreover, data provenance is related to several other aspects of data management, namely data access rights, governance, privacy and security.
- Provence information can be recorded:
    - as free text and unstructured information (mainly readable for humans, not for machines/software), describing data collection and processing method.
    - according to metadata schemas or standards, that can be generic (e.g. Dublin Core) or discipline specific such as [ISO19115-2](https://www.iso.org/standard/67039.html).
    - according to Provenance Data Model ({% tool "prov-dm-the-prov-data-model" %}) and ontology ([PROV-O](https://www.w3.org/TR/prov-o/)).
- As for documentation and metadata, the medium to capture provenance information can also varies. Provenance trails can be captured 
    - in text files or spreadsheets
    - in registries or databases
    - in dedicated software/platforms (such as LIMS)
    - internally and automatically by software tools during their processing activity (such as workflow management systems)
- As for documentation and metadata, provenance information can be recorded and displayed/visualised in machine-readable (see [Machine actionability](machine_actionability) page) and/or human-readable form.


### Solutions

- Record provenance according to schemas or defined profiles. These can be generic or domain-specific, and can be found in {% tool "rda-standards" %} or {% tool "fairsharing" %}. Use metadata schemas containing provenance information in your README file and in any kind of data documentation and metadata file. Best practices for documentation and metadata, and data organisation should be applied for provenance file as well.
- Implement serialisation specification of the [PROV-MODEL](https://www.w3.org/TR/prov-overview/) in your data management tools to record provenance in machine-actionable format (RDF, Linked data, owl, xml, etc.).
- Use [RO-Crate specifications](https://www.researchobject.org/ro-crate/1.1/provenance.html) and/or specific profiles for provenance (e.g., [RO-Crate profiles to capture the provenance of workflow runs](https://www.researchobject.org/workflow-run-crate/)).
- Make use of tools and software that help you record provenance in a manual or an automated way. Use:
  - Electronic Data Capture (EDC) systems, Laboratory Information Management Systems (LIMS) or similar tools.
  - Workflow management systems (such as Kepler, {% tool "galaxy" %}, Taverna, VisTrails); provenance information embedded in such software or tools are usually available to users of the same tool or can be exported as separated file in several formats, such as {% tool "research-object-crate" %}.
  - Registries such as {% tool "workflowhub" %}.
