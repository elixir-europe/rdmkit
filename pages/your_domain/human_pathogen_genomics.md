---
title: Human pathogen genomics
search_exclude: true
description: <!---REPLACE THIS with a one sentence description of the page--->
contributors: [Diana Pilvar, Espen Åberg, Wolmar Nyberg Åkerström, Rafael Andrade Buono]
page_id: human_pathogen_genomics
related_pages: 
  your_tasks: [data_brokering, metadata_management, data_transfer]
  tool_assembly: [covid19_data_portal]
  your_domain: [rare_disease_data]
# More information on which page id you can use can be found at https://rdmkit.elixir-europe.org/website_overview
#training:
#  - name:
#    registry:
#    url:
# More information on how to fill in this metadata section can be found here https://rdmkit.elixir-europe.org/page_metadata
---

# Working document for Converge WP9 RDMkit Task force
<blockquote>

* Useful for diagrams: https://app.diagrams.net/
* Markdown guide: https://www.markdownguide.org/extended-syntax/

Please take in mind our style guide https://rdmkit.elixir-europe.org/style_guide when writing the content of this page.

Domain pages should detail the particular data management challenges of the domain, typically by complementing and extending one or more existing Problem pages.
In the event that no adequate Problem page exists for a problem that can be generalized across domains, consider first contributing to create one or raising a GitHub issue. However, if a problem is entirely domain specific, then it should be fully detailed within the respective Domain page.
    
Suggested scope/focus:

* Specimen collected from human host, extracted/isolated produce
* Outbreak data sharing and analysis efforts, both public health surveillance and research studies
* Challenges related to data sharing with samples collected from human hosts and from within health care
* Filtering fragments of human DNA from viral genome reads
* Masking research subject/patient information subject/patient information
* Whats is sensitive data and what is not
Remove human sequences from samples
Link to legal aspects workshop

    
</blockquote>

## Introduction
<blockquote>
In this section you should provide a brief overview of the domain from the data management perspective, mentioning and putting into context the challenges that are particular to the domain, which will be the object of sections below.
</blockquote>



<!---A domain page based on the work of Converge WP9, exact scope to be defined but something on the lines of “Human pathogen genomics”, focusing on sections related to outbreak data sharing and analysis efforts, both public health surveillance and research studies. Also links to the IDTk.--->

Human pathogen genomics analyses the genetic code of disease-causing organisms. This information can be used by researchers and public health authorities to identify and understand the pathogen and by extension to prevent and respond to outbreaks and to develop remedies such as treatments and vaccines. 

* Something about from samples from a single individual and a specific target pathogen to metagenomic studies with genomic data from many pathogens and a larger population.


The human pathogen genomics domain includes the data challenges of research with a public health and policy focus and research with a focus on the characterization of the pathogens themselves. As data initially generated with either focus can be of important reuse value for the other focus (e.g. pathogen surveillance data used for pathogen evolution studies) it is imperative that rich metadata is collected and that provenance and standards are properly recorded. Moreover, considerations on human sensitive data permeate the domain, either through intentional data collection efforts (e.g. patient information recorded as metadata) or as an inherent effect of the methodologies employed (e.g. remnants of human genetic material in sequencing results).
On this page we highlight aspects of the data life cycle that deserve specific attention in this domain.

### Pathogens from healthcare and research studies

* Different frameworks for legal and operational aspects, consent issues, …
* Something about timeliness of data sharing across the two…
* A bullet with [a link][short_link_a]
* Challenge 1:&nbsp;Pathogen surveillance&nbsp;
* Pathogens from healthcare
* Challenge 2: Novel/ not actively monitored pathogens
* Pathogens from research projects


[short_link_a]: https://raw.githubusercontent.com/elixir-europe/rdmkit/master/pages/your_domain/TEMPLATE_your_domain.md



## Planning a study with pathogen genome data

### Description
While the object of interest in this domain are pathogens, the data is usually derived from samples originating from patients and human research subjects. This means that you must plan to either remove or to handle human data during your study.

### Considerations

Consant mixing of human and non-human data.

* What legal and ethical aspects do you need to consider? 
  * Can you separate pathogen and human host material and data?
  * ELSI aspects and contracts with suppliers etc.
  * Who needs to be consulted and how much time would be required to obtain access/permits to get access to samples/data?
* What public health and research initives should you consider aligning with?
  * What data could be shared with or reused from other initiatives during the project?
  * How will you align your practices with convensions from these initiatives to maximise the impact of the data and insight generated by the project? 
  * How will you share data with your collaborators and other initiatives?
* What conventions will you adopt when planning your study?
  * What existing protocols should you consider adopting for sample preparation, sequensing, variant calling etc? 
  * What conventions should you adopt for documenting your research? 

### Solutions
#### Isolate pathogen from host information
* Depending on the pathogen, how it interacts with the host, or the methods applied, it can be possible to generate clean isolates that do not contain host related material. Data produced from a clean isolate could potentially be handled with few restrictions, while other data will be considered to be personal and sensitive.
  * Human data task page
  * Data protection

#### Public health initiaitves
* National and international recommendations from public health authorities, epidemic surveillance programs and research data communities should be considered when planning a new study or surveillance programme. In particular, you could consult relevant guidance issued by national and international surveillance programs while considering widely adopted guidelines for research documentation, and recommendations provided by data sharing platforms and communities.
  * WHO Pathogen genomic initatives
  * ECDC Pathogen genomic initatives
  * [National resources](https://rdmkit.elixir-europe.org/national_resources) 
  * INSDC Pathogens
  * EMBL-EBI Pathogens
  * RDA
  * [ECDC’s Surveillance and study protocols](https://www.ecdc.europa.eu/en/covid-19/surveillance/study-protocols)

#### Documenting sequencing experiments
* Good practices for annotating sequencing experiments suggest that the documentation, at a minimum, should describe the design of the study or surveillance program, the collected specimens and how the samples were prepared, the experimental setup and protocols, and the analysis workflow.

  * [Minimal Information about a high throughput SEQuencing Experiment (MINSEQE)](https://fairsharing.org/FAIRsharing.a55z32)
  * [GSC Minimum Information about any Sequence (MIxS)](https://fairsharing.org/FAIRsharing.9aa0zp) and current Extensions
  * Documentation and metadata task page
  * [Ten simple rules for annotating sequencing experiments](https://doi.org/10.1371/journal.pcbi.1008260)




## Collecting and processing pathogen sequence data

### Description


### Considerations
* What information should you consider recording when collecting data?
  * What should you note when collecting, storing and preparing the samples?
  * How will you capture information about the configuration and quality of the sequencing results?
  * How will you ensure that the information captured is complete and correct?
* What data and file formats should you consider for your project?
  * What are the de-facto standards used for the experiemnt type and down-stream analysis-pipelines?
  * Where are the instrument specific aspects for the data and files formats documented?
* What existing data will you integrate or use as a reference in  your project?
  * What reference genome(s) will you need access to?
  * What is the recommended citation for the data and their versions?

### Solutions
#### Filtering genomic reads coresponding to human dna fragments

* Data files with reads produced by sequencing experiments sometimes contain fragments of the host organism’s DNA. When the host is a human research subject or patient, these fragments can be masked or removed to produce files that could potentially be handled with fewer restrictions.
  * Mapping to human reference genomes
  * Mapping to pathogen genome

#### Contextual information about the sample

* Information about the host phenotype, context and disease is often necessary to answer questions in a research study or policy perspective. This information can contain personal and sensitive data.
  * Checklists...
  * Pathogens checklist(s) can be found among [ENA Sample checklists](https://www.ebi.ac.uk/ena/browser/checklists), including checklists derived from the [MIxS consortium](http://w3id.org/mixs). For example the [ENA virus pathogen reporting standard checklist](https://www.ebi.ac.uk/ena/browser/view/ERC000033) has been recurrently used for SARS-CoV-2 studies.
 
<!--- Other potential checklist examples
   * [ENA prokaryotic pathogen minimal sample checklist](https://www.ebi.ac.uk/ena/browser/view/ERC000028)
* [ENA binned metagenome](https://www.ebi.ac.uk/ena/browser/view/ERC000050)
    * [ENA Global Microbial Identifier reporting standard checklist GMI_MDM:1.1](https://www.ebi.ac.uk/ena/browser/view/ERC000029)
    * [GSC MIxS host associated](https://www.ebi.ac.uk/ena/browser/view/ERC000013)
    * [GSC MIxS human associated](https://www.ebi.ac.uk/ena/browser/view/ERC000014)
    * [GSC MIxS microbial mat biolfilm](https://www.ebi.ac.uk/ena/browser/view/ERC000019)
    * [GSC MIxS human gut](https://www.ebi.ac.uk/ena/browser/view/ERC000015)
    * [GSC MIxS human oral](https://www.ebi.ac.uk/ena/browser/view/ERC000016)
    * [GSC MIxS human skin](https://www.ebi.ac.uk/ena/browser/view/ERC000017)
    * [GSC MIxS human vaginal](https://www.ebi.ac.uk/ena/browser/view/ERC000018)--->

* Other contextual information can include non-host related environmental factors, such as interactions with other pathogens, drugs and geographic proliferation. These information can be used for 
  * Ontologies and checklists
      * [Phenotypic QualiTy Ontology](https://bioportal.bioontology.org/ontologies/PATO)
      * [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/taxonomy)
      * [Disease Ontology](https://disease-ontology.org)
      * [Chemical Entities of Biological Interest](https://bioportal.bioontology.org/ontologies/CHEBI/?p=summary)
      * [UBER anatomy ONtology](https://bioportal.bioontology.org/ontologies/UBERON)

  * Pathogens checklist(s) for ENA/packages for SRA? Etc.?

* Information about the sampled material and how it was processed for sequencing

#### Genomic information and quality assessment
* Make sure you are using common and suitable data formats
  * Enough pathogen materials? Was it stored properly?
  * [High-Throughput Sequencing | LifeScienceRDMLookUp](https://elixir.no/rdm-lookup/sequencing)
  * [B1MG D3.1 - Quality metrics for sequencing](https://doi.org/10.5281/zenodo.4889390)

* Example of a common pipeline structure and corresponding outs with and example of quality information...

* Checklists and convenstion for describing experiment configuration and execution
  * checklists

* Data quality assurance
  * Multi-QC etc
  * [Reference FAIR Cookbook or something](https://faircookbook.elixir-europe.org/content/recipes/interoperability/fastq-file-format-validators.html)


#### Describing samples and processing steps

* Separating pathogen from human
* Sharing/Public
* Dealing with patient/research subject information
* Analysis
* Workflow harmonization
* Link to Galaxy showcase in IDTk
* Automated pipelines
* Collections: Galaxy workflows, WorkflowHub, other sources?

## Sharing and preserving pathogen genomic data


### Description


### Considerations

* What data need to be preserved by the project and for how long?
  * What is preserved by others and how would someone find and access the data?
* What databases should I use to share human pathogen genomics data?


### Solutions
#### Sharing host related and other contextual information
* Something about links to non-sensitive pathogen genome data etc. Aggregate level information, data masking and access to detailed records. Reference human data. Some of this information can be used as metadata for genomic data. 

#### Sharing pathogen genomic data
* Something about INSDC, GISAID, EBI-data base chooser etc. also FEGA, ECDC, national data hubs etc.
* EBI Pathogens data hubs
* Licenses
* Provenance
* Differences between Health and Research
* Sharing
* Data ownership
* Data brokering
* Data sharing agreements/conditions
* Platforms for sharing


## Template
### Description
<blockquote>Sections within Domain pages (aside from "Introduction" at the start and "Relevant tools and resources " at the end) should focus on particular data management problems, which should be described in this first sub-section.
For problems that are fully domain-specific, a detailed description is merited.
For detailing the domain-specific challenges of a problem that is generic, please link to the corresponding generic Problem page before going into the domain-specific challenges.</blockquote>

### Considerations 
<blockquote>Direct and concise considerations, structured in bullet points and typically framed as questions RDMkit reader should ask themselves in order to arrive at the best solution among those listed below. One level of nesting of bullet points within considerations is fine, but more levels should be avoided.</blockquote>


### Solutions
<blockquote>Detail, either in normal text or in bullet points, the domain-specific solutions to the problem. Do not merely list tools or resources, as they will be automatically listed in the bottom section, but you can and should mention tools and resources listed below if you detail their usage to solve the problem. </blockquote>

<!--- ## Section 2 Title --->
<!--- Add more sections as needed, with the same subsections as above. --->

* A bullet with [a link][short_link_a]
