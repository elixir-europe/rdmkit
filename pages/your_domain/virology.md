---
title: Virology
description: Data management solutions for virology data.
contributors: [Niels Geudens, Flora D'Anna]
page_id: virology
related_pages: 
  your_tasks: [data_brokering, gdpr_compliance, ethics, compliance, sensitive, data_security, data_discoverability, identifiers]
  tool_assembly: [covid19_data_portal]
# More information on which page id you can use can be found at https://rdmkit.elixir-europe.org/website_overview
training:
  - name:
    registry:
    url:
fairsharing:
- name: EVORA FAIRsharing collection
  url: https://fairsharing.org/5449
# More information on how to fill in this metadata section can be found here https://rdmkit.elixir-europe.org/page_metadata
---

## Introduction
Virology is a rapidly evolving field that generates diverse and complex datasets, from genomic sequences to clinical trial results and epidemiological data. Effective research data management (RDM) is essential to ensure that these valuable datasets are organised, shared, and preserved in a manner that enables long-term impact.

## Data Heterogeneity
 
### Description
Outbreak surveillance in virology requires the integration of multiple data types, including sequencing, clinical, and epidemiological data. These data types originate from diverse sources, such as hospitals, research laboratories, and public health agencies, making their harmonisation and interoperability critical. Without standardised data management approaches, inconsistencies in metadata, sampling protocols, and data formats can hinder effective outbreak response, cross-study comparisons, and reproducibility of findings.

### Considerations
Key challenges in managing data heterogeneity include:
* Standardising sample collection protocols across clinical and environmental settings to ensure comparability.
* Integrating epidemiological and genomic data to enhance outbreak detection and integrative and global responses.

### Solutions
To effectively manage data heterogeneity in virology outbreak surveillance, several domain-specific solutions are recommended:
* The [Data Provenance page](data_provenance) provides comprehensive guidance on capturing metadata, documenting data origins, and maintaining transparent records, ensuring data traceability and reproducibility.
* Use standardised protocols for sample collection by identifying and reviewing existing guidelines from organisations such as [World Health Organisation](https://www.who.int/publications/who-guidelines), [ECDC](https://www.ecdc.europa.eu/en), and [ISO standards](https://www.iso.org/standards.html) to ensure alignment with best practices.
* Implement metadata standards for data interoperability
  * The [Documentation and metadata page](metadata_management) offers practical recommendations and standards for accurately describing data, ensuring consistent interpretation, interoperability, and long-term usability.
  * Apply {% tool "mixs" %} and the derived {% tool "miuvig" %} for annotating viral sequence data with necessary metadata fields.
  * Adapt generic dataset descriptions (e.g. {% tool "data-catalog-vocabulary" %}, Dublin Core, {% tool "bioschemas" %}) for basic dataset descriptions.
  * Follow {% tool "biosamples" %} Metadata Schema from EBI for structured viral sample metadata.
* Ensure metadata compliance with international repositories
  * The [Data Brokering page](data_brokering) describes strategies and tools for integrating, harmonising, and translating data across diverse formats and sources.
  * Format metadata to meet the submission requirements of repositories like {% tool "gisaid" %} and {% tool "european-nucleotide-archive" %} to ensure smooth data deposition and retrieval.
  * Utilise validation tools and checklists to ensure completeness and accuracy before data submission.
* FAIRsharing resources for metadata selection
  * Refer to the [EVORA collection](https://fairsharing.org/5449) of FAIRsharing-referenced metadata standards for pandemic preparedness and response.
  * Consult {% tool "fairsharing" %} registries to identify suitable standards for different types of virology datasets.
  * Integrate epidemiological and genomic data for outbreak analysis, by utilising phylodynamic workflows (e.g., BEAST, {% tool "nextstrain" %}, or TreeTime), enabling real-time outbreak tracking.
  * Implement structured pipelines for linking viral genome sequences with patient and outbreak metadata.
* Apply domain-specific vocabularies for consistent annotation
  * Utilise the [EVORA ontology](https://www.ebi.ac.uk/ols4/ontologies/evorao) and {% tool "ictv" %} to ensure that virus-related metadata terms are standardised and interoperable.
  * Monitor updates in virology-specific ontologies to maintain alignment with evolving standards.
By implementing these best practices, outbreak surveillance data can be better structured, more interoperable, and more effectively shared, ultimately improving global response efforts to viral outbreaks.

## Data Sensitivity & Ethics
 
### Description
Handling sensitive data in virology outbreak surveillance involves managing patient data, ensuring proper anonymisation, and complying with regulations such as the General Data Protection Regulation (GDPR). The ethical and legal aspects of handling such data are crucial to maintaining patient privacy while allowing researchers and public health authorities to analyse and respond to viral threats effectively.
Proper data governance strategies must balance the need for data accessibility and data security, ensuring that only authorised personnel can access identifiable information. Secure storage, controlled access mechanisms, and appropriate anonymisation techniques must be implemented to meet legal and ethical standards.

### Considerations
Key challenges in managing data sensitivity and ethics include:
* Ensuring compliance with GDPR and other legal frameworks when collecting, processing, and sharing sensitive patient data.
* Anonymising and pseudonymising patient data to reduce privacy risks while preserving data utility for research.
* Implementing secure and scalable storage solutions that support controlled data access, encryption, and long-term preservation.

### Solutions
Organisations must implement robust governance policies, encryption techniques, and controlled data access mechanisms to maintain patient privacy while enabling scientific advancements. The following strategies outline best practices for secure data management and ethical compliance.
* Ensure GDPR and regulatory compliance
  * For guidance on managing sensitive data ethically and in compliance with regulations, the pages on [GDPR compliance](gdpr_compliance), [Ethical aspects](ethics), and [Compliance monitoring & measurement](compliance_monitoring) provide detailed recommendations on protecting personal data, navigating ethical responsibilities, and implementing effective compliance monitoring practices.
  * Identify and mitigate privacy risks associated with human and health-related data (see [Human data](human_data) and [Health data](health_data) domain pages).
  * Establish clear data governance policies defining roles and responsibilities regarding data processing and sharing.
  * Ensure contractual coverage for data exchanges through appropriate agreements (e.g., Data Use Agreements, Consortium Agreements, Data Sharing Agreements), explicitly outlining data usage, retention, reuse, and publication policies. Material Transfer Agreements (MTAs) should similarly address the handling of human data derived from received samples.
  * You can also check the practices included in the {% tool "idtk" %} related to the management of human and pathogen data in the context of infectious diseases.
* Implement effective data anonymisation and pseudonymisation strategies to reduce data sensitivity and protect privacy, following best practices detailed on the [Data Sensitivity](data_sensitivity) page.
* Adopt secure and scalable data storage solutions to ensure long-term data integrity, controlled access, and compliance with relevant standards and best practices, as described on the [Data Storage](storage) page.
  * Store sensitive data in repositories designed for controlled access (e.g., {% tool "the-european-genome-phenome-archive" %}, {% tool "european-nucleotide-archive" %})
  * Use encryption for data at rest and in transit to prevent unauthorised access.
  * Establish strict access control policies, using role-based access and multi-factor authentication where appropriate.
* Implement best practices for data versioning and backup to maintain clear data histories, prevent loss, and enhance reproducibility, following guidelines provided on the [Data Organisation](data_organisation) page.

## Data sharing and access
 
### Description
Effective data sharing and access enable timely surveillance of viral genome evolution, facilitating early detection of mutations and emerging variants. This rapid exchange of outbreak information supports swift global responses while simultaneously addressing critical concerns around data security and patient privacy. 
Researchers have a responsibility to share outbreak-related data ethically, legally, and efficiently, allowing authorised users appropriate access to sensitive materials, such as patient records and genomic sequences, in alignment with national and EU regulatory frameworks. Furthermore, assigning persistent identifiers and utilising structured data repositories enhance the long-term usability, traceability, and discoverability of outbreak data, significantly improving preparedness and response strategies.

### Considerations
Key challenges in data sharing and access include:
* Balancing accesibility with security, ensuring that sensitive data is accessible to authorised users without compromising privacy.
* Adhering to national and international regulations to ensure ethical data sharing.
* Ensuring proper data deposition in repositories that align with domain-specific standards.
* Maintaining dataset integrity and discoverability using persistent identifiers like DOIs and accession numbers.

### Solutions
To ensure secure and effective data sharing in virology outbreak surveillance, researchers and institutions should implement structured strategies:
* Balance accessibility with security in data sharing by implementing measures that protect sensitive data while ensuring it remains discoverable and accessible, following the guidelines provided on the pages for [Data Security](data_security) and [Data Discoverability](data_discoverability)
  * Use controlled-access repositories like [VODAN - GO FAIR](https://www.go-fair.org/implementation-networks/overview/vodan/) to manage and access sensitive patient or outbreak data securely.
  * Implement data access governance models that allow tiered access based on user credentials and need.
  * Utilise {% tool "pathoplexus" %} for managing metadata and access rights in a structured manner. It is an open-source database dedicated to the efficient sharing of human viral pathogen genomic data, fostering global collaboration and public health response.
* Ensure proper deposition of outbreak data into trusted repositories to facilitate data sharing, citation, and reuse, following best practices outlined on the [Data Publication](data_publication) page.
  * Submit viral genomic sequences and epidemiological data to {% tool "gisaid" %}, NCBI {% tool "genbank" %}, and {% tool "european-nucleotide-archive" %} for public accessibility.
  * Use standard submission pipelines to ensure compliance with repository-specific metadata and formatting guidelines.
* Assign persistent identifiers to datasets to enhance discoverability, citation, and long-term accessibility, following recommendations on the [Identifiers](identifiers) page.
  * Register DOIs or accession numbers for datasets to facilitate long-term accessibility and proper citation.
  * Ensure metadata linking persistent identifiers is properly formatted and recorded.
* Comply with national and EU data-sharing regulations by consulting country-specific guidelines and legal frameworks available on the [National Resources](national_resources) page.
  * Align data-sharing practices with GDPR, national laws, and institutional ethical guidelines.
  * Implement data-sharing agreements between collaborating institutions to formalise responsibilities.

