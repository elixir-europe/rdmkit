---
title: Data publication
contributors: [Munazah Andrabi, Ulrike Wittig, Elin Kronander, Flora D'Anna, Aitana Neves, Nazeefa Fatima, Carla Cummins]
description: How to prepare data and find repositories for publication.
page_id: data_publication
related_pages: 
    tool_assembly: []
faircookbook:
- name: Depositing to generic repositories - Zenodo use case
  url: https://w3id.org/faircookbook/FCB009
---


## Can you really deposit your data in a public repository?

### Description
Sometimes it is difficult to determine if publishing data you have at hand is the right thing to do. Some reasons for hesitations might be that you have not used the data in a publication yet and don't want to be scooped, that the data contains personal information about patients or that the data was collected or produced in a collaboration.

### Considerations
* Publishing data does not necessarily mean open access nor public. Data can be published with closed or restricted access.
* Data doesn't have to be published immediately while you are still working on the project. Data can be made available during the revision of the paper or after the publication of the paper.
* Make sure to have the rights or permissions to publish the data.
  * Is the data commercially-sensitive?
  * Does the data contain confidential/restricted information?
  * Who controls the data?

### Solutions
* If ethical, legal or contractual issues apply to your data type (e.g. personal or sensitive data, confidential or third-party data, data with copyright, data with potential economic or commercial value, intellectual property or IP data, etc.), ask for help and advice from the Legal Team, Tech Transfer Office, and/or Data Protection Officer of your institute.
* Decide what is the right [type of access](sharing#what-should-be-considered-for-data-sharing) for your data, for instance:
  * Open access.
  * Registered access or with authentication procedure.
  * Controlled access or via Data Access Committees (DACs).
* Decide what [licence](licensing) should be applied to your metadata and data.
* Certain repositories offer solutions for depositing data that need to be under restricted access. This allows for data to be findable even when it can not be published openly. One example is the {% tool "the-european-genome-phenome-archive" %} that can be used to deposit potentially identifiable genetic and phenotypic human data.
* Many repositories provide the option to put an embargo on a deposited dataset. This might be useful if you prefer to use the data in a publication before making it available for others to use.
* Establish an agreement outlining the controllership of the data and each collaborators' rights and responsibilities.
* Even if the data cannot be published, it is good practice to publish the metadata of your datasets.

## Which repository should you use to publish your data?

### Description
Once you have completed your experiments and have performed quality control of your data it is good scientific practice to share your data in a public repository. Publishing your data is often required by funders and publishers.

The most suitable repository will depend on the data type and your discipline.

### Considerations
  * What type of data are you planning to publish?
  * Does the repository need to provide solutions for restricted access for sensitive data?
  * Do you have the rights to publish the data via the repository?
  * How sustainable is the repository, will the data remain public over time?
  * How FAIR is the repository?
  * Does the funding agency or the scientific journal pose specific requirements regarding data sharing?
  * What are the repository's policies concerning licences and data reuse?

### Solutions
* Based on the possible ethical, legal and contractual implications of your data, decides:
  * The right [type of access](sharing#what-should-be-considered-for-data-sharing) for your data.
  * The [licence](licensing) that should be applied to your metadata and data.
* Check if/what discipline-specific repositories can apply the necessary access conditions and licences to your (meta)data.
* Discipline-specific repositories: if a discipline-specific repository, recognised by the community, exists this should be your first choice since discipline-specific repositories often increases the FAIRness of the data.
  * The {% tool "embl-ebi-s-data-submission-wizard" %} can help you choose a suitable repository based on your data type.
  * There are lists of discipline-specific, community-recognised repositories e.g.:
   * {% tool "elixir-deposition-databases-for-biomolecular-data" %} including {% tool "arrayexpress" %}, {% tool "biomodels" %}, {% tool "biostudies" %}, {% tool "european-nucleotide-archive" %}, {% tool "pdb" %}, {% tool "pride" %}
   * [Scientific Data journal's recommended repositories](https://www.nature.com/sdata/policies/repositories)
   * {% tool "wellcome-open-research-data-guidelines" %}
* Check if there are repositories available for specific data formats, such as images (e.g. {% tool "bioimagearchive" %}, {% tool "empiar" %}) or earth and environmental science data (e.g. {% tool "pangaea" %}).
* General-purpose and institutional repositories: For other cases, a repository that accepts data of different types and disciplines should be considered. It could be a [general-purpose repository](https://www.nature.com/sdata/policies/repositories#general), such as {% tool "zenodo" %}, {% tool "mendeley-data" %}, {% tool "figshare" %}, {% tool "dryad" %} or a centralised repository provided by your institution or university.
* {% tool "re3data" %} or {% tool "repository-finder" %} gather information about existing repositories and allows you to filter them based on access and licence types.
* {% tool "re3data" %} and {% tool "fairsharing" %} websites gather features of repositories, which you can filter by discipline, data type, taxonomy and many other features.

## How do you prepare your data for publication in data repositories?

### Description
Once you have decided where to publish your data, you will have to make your (meta)data ready for repository submission. For this reason it is recommended to become aware of repository's requirements before start collecting the data.

### Considerations
  * What file formats should be used for the data?
  * How is the data uploaded?
  * What metadata do you need to provide?
  * Under which licence should the data be published?
  * Should [sensitive data](data_sensitivity) and metadata be anonymised or pseudonymised prior to a publication? This could notably be the case if you work with [human data](human_data).
  * After data is submitted to a public repository, should the original copy of the data be retained at the central brokering platform and linked to its public counterpart? Or should it be removed and replaced with the ID of the public record?


### Solutions
  * Learn the following information about the chosen repositories:
    * Required metadata schemas
    * Required ontologies or controlled vocabularies
    * Accepted file formats for data and metadata
    * Costs for sharing and storing data
  * Repositories generally have information about data formats, metadata requirements and how data can be uploaded under a section called "submit", "submit data", "for submitters" or something similar. Read this section in detail.
  * To ascertain re-usability data should be released with a clear and accessible data usage [licence](licensing). We suggest making your data available under licences that permit free reuse of data, e.g. a Creative Commons licence, such as CC0 or CC-BY. 
    * Note that every repository can have one default licence for all datasets. For instance, sequence data submitted to for example {% tool "european-nucleotide-archive" %} are implicitly free to reuse by others as specified in the {% tool "international-nucleotide-sequence-database-collaboration" %}.
  * See the corresponding pages for more detailed information about [metadata](metadata_management), [licences](licensing) and [data transfer](data_transfer).
  * There are many tools available to remove human reads from your non-human data, e.g. {% tool "metagen-fastqc" %}

## How do you update or delete a published entry from a data repository?

### Description
You will sometimes need to update or delete some entries that were incomplete or wrongly submitted for publication. Note however that upon creation of a new record, data is generally tagged for distribution and selected metadata fields may be exchanged with other repositories. Thus, redistribution of updated records may not be triggered automatically and updating records fully can be a time consuming and manual process for the repository. Also, in general, submitted data may not be deleted, but may be suppressed from public view upon request. In a nutshell, it is therefore safer to make sure to submit the right entry from the start, rather than updating it or asking for its withdrawal at a later stage.

### Considerations
* Does the repository offer the possibility to update a submission? For the data submitter, is this a manual procedure (e.g. email, web interface) or is it available through an Application Programming Interface (API) or Command Line Interface (CLI)?
* Does the repository offer the possibility to delete (or hide) submissions? 
* Does the repository have a test-server where data can be submitted for testing purpose?

### Solutions
Solutions are very much repository-dependent. For example, on the {% tool "european-nucleotide-archive" %}, entries can be easily updated using a CLI. However, the updated information is not automatically redistributed to other registries linked to ENA. Upon email request, entries may also be suppressed from public view. Note that ENA also has a test server to make test submissions before submitting to the actual production server, which can be very useful when sending large batches of data to test for any systematic errors. Please check these points with your repository of choice.

## Should you include datasets accession numbers in pre-prints or thesis?

### Description
Researchers often deposit their data in public databases (e.g., ArrayExpress, GEO) and receive an accession number for that data. Including these accession numbers in a pre-print or a thesis could make the dataset publicly available, even before the final publication. Whether to include them depends on whether the researcher wants the data to be accessible to the public at an early stage or keep it private until later.

### Considerations
* Pre-prints are often treated as citable publications.
* Some databases may release data upon request if an accession number is cited in a pre-print or in a published thesis.
* Policies vary between repositories — some release data proactively, while others do so only upon inquiry.
* Once an accession number is made public in a pre-print, the dataset may become publicly accessible, even if the preprint is intended to be temporary and even if a second manuscript describing the same data is pending.

### Solutions
* To avoid unintended data release, authors should refrain from including accession numbers in pre-prints if they wish to keep the dataset private. If public availability is not an issue, citing the accession number ensures accessibility.

* Check the guidelines or policies of the data repository of interest before deciding whether to include the accession number in a pre-print. For example, GEO's policy requires that data be publicly accessible once an accession number is cited, even if the manuscript is a pre-print. More information can be found here: [GEO FAQ](https://www.ncbi.nlm.nih.gov/geo/info/faq.html#holdprivate).


