---
title: Data storage
contributors: [Ulrike Wittig, Elin Kronander, Munazah Andrabi, Flora D'Anna, Flavio Licciulli, Ott Oopkaup, Marcus Lundberg, Thanasis Vergoulis, Frederik Coppens, Olivier Collin, Nadia Tonello, Korbinian Bösl]
description: How to find appropriate storage solutions.
page_id: storage
related_pages: 
  tool_assembly: [nels, tsd, ome, transmed, xnat_pic]
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=%22data+storage%22#materials
dsw:
- name: Data storage systems and file naming conventions
  uuid: bc5e3dbf-2923-4025-a49a-f204b01d4018
- name: How long will this data set be kept?
  uuid: d4e6a244-07fb-4573-b93f-c20a9409ac7c
- name: Will you be storing data in an "object store" or a "document store" system?
  uuid: dc39957e-688a-4f71-a6a8-57f52509e7cf
faircookbook:
- name: Licensing Software
  url: https://w3id.org/faircookbook/FCB033
- name: Making Computational Workflows FAIR
  url: https://w3id.org/faircookbook/FCB062
- name: Depositing to generic repositories - Zenodo use case
  url: https://w3id.org/faircookbook/FCB0009
- name: Registering datasets with Wikidata
  url: https://w3id.org/faircookbook/FCB060
---

## What features do you need in a storage solution when collecting data?

### Description

The need for Data storage arises early on in a research project, as space will be required to put your data when starting collection or generation. Therefore, it is a good practice to think about storage solutions during the data management planning phase, and request storage in advance and/or pay for it.

The storage solution for your data should fulfil certain criteria (e.g. space, access & transfer speed, duration of storage, etc.), which should be discussed with the IT team. You may choose a tiered storage system for assigning data to various types of storage media based on requirements for access, performance, recovery and cost. Using tiered storage allows you to classify data according to levels of importance and assign it to the appropriate storage tiers or move it to different tier for e.g. once analysis is completed you have the option to move data to lower tier for preservation or archiving.

Tiered Storage is classified as “Cold” or “Hot” Storage. “Hot” storage is associated with fast access speed, high access frequency, high value data and consists of faster drives such as the Solid State Drives (SSD). This storage is usually located in close proximity to the user such as on campus and incurs high costs. “Cold” storage is associated with low access speed and frequency and consists of slower drives or tapes. This storage is usually off-premises and incurs low cost.

### Considerations

When looking for solutions to store your data during the collection or generation phase, you should consider the following aspects.

* The volume of your data is an important discerning factor to determine the appropriate storage solution. At the minimum, try to estimate the volume of raw data that you are going to generate or collect.
* What kind of access/transfer speed and access frequency will be required for your data.
* Knowing where the data will come from is also crucial. If the data comes from an external facility or needs to be transferred to a different server, you should think about an appropriate [data transfer](data_transfer) method.
* It is a good practice to have a copy of the original raw data in a separate location, to keep it untouched and unchanged (not editable).
* Knowing for how long the raw data, as well as data processing pipelines and analysis workflows need to be stored, especially after the end of the project, is also a relevant aspect for storage.
* It is highly recommended to have metadata, such as an [identifier](identifiers) and file description, associated with your data (see [Documentation and metadata page](metadata_management)). This is useful if you want to retrieve the data years later or if your data needs to be shared with your colleagues for collaboration. Make sure to keep metadata together with the data or establish a clear link between data and metadata files.
* In addition to the original “read-only” raw (meta)data files, you need storage for files used for data processing and analysis as well as the workflows/processes used to produce the data. For these, you should consider:
  * who is allowed  to access the data (in case of collaborative projects), how do they expect to access the data and for what purpose;
  * check if you have the rights to give access to the data, in case of legal limitations or third party rights (for instance, collaboration with industry);
  * consult policy for data sharing outside the institute/country (see [Compliance monitoring page](compliance_monitoring)).

* Keeping track of the changes (version control), conflict resolution and back-tracing capabilities.

### Solutions

* Provide an estimate about the volume of your raw data (i.e., is it in the order of Megabytes, Gigabytes or Terabytes?) to the IT support in your institute when consulting for storage solutions.
* Clarify if your data needs to be transferred from one location to another. Try to provide IT with as much information as possible about the system where the data will come from. See our [Data transfer page](data_transfer) for additional information.
* Ask for a tiered storage solution that gives you easy and fast access to the data for processing and analysis. Explain to the IT support what machine or infrastructure you need to access the data from and if other researchers should have access as well (in case of collaborative projects).
* Ask if the storage solution includes an automatic management of versioning, conflict resolution and back-tracing capabilities (see also our [Data organisation page](data_organisation)).
* Ask the IT support in your institute if they offer technical solutions to keep a copy of your (raw)data secure and untouched (snapshot, read-only access, backup…). You could also keep a copy of the original data file in a separate folder as “read-only”.
* For small data files and private or collaborative projects within your institute, commonly accessible Cloud Storage is usually provided by the institute, such as {% tool "nextcloud" %} (on-premises), {% tool "microsoft-onedrive" %}, {% tool "dropbox" %}, {% tool "box" %}, etc. Do not use personal accounts on similar services for this purpose, adhere to the policies of your institute.
* For large data sets consider cloud storage services, such as {% tool "sciencemesh" %}, {% tool "openstack" %}) and cloud synchronization and sharing services ({% tool "cs3" %}), such as {% tool "cernbox" %} or {% tool "seafile" %}
* It is a requirement from the funders or universities to store raw data and data analysis workflows (for reproducible results) for a certain amount of time after the end of the project (see our [Preserve page](preserving)). This is usually a requirement. Check the data policy for your project or institute to know if a copy of the data should be also stored at your institute for a specific time after the project. This helps you budget for storage costs and helps your IT support with estimation of storage resources needed.
* Make sure to generate good documentation (i.e., README file) and metadata together with the data. Follow best practices for folder structure, file naming and versioning systems (see our [Data organisation page](data_organisation)). Check if your institute provides a (meta)data management system, such as {% tool "irods" %}, {% tool "dataverse" %}, {% tool "fairdom-seek" %} or {% tool "osf" %}. 

## How do you estimate computational resources for data processing and analysis?

### Description

In order to process and analyse your data, you will need access to computational resources. This ranges from your laptop, local compute clusters to High Performance Computing (HPC) infrastructures. However, it can be difficult to be able to estimate the amount of computational resource needed for a process or an analysis.

### Considerations

Below, you can find some aspects that you need to consider to be able to estimate the computational resource needed for data processing and analysis.

* The volume of total data is an important discerning factor to estimate the computational resources needed.
* Consider how much data volume you need “concurrently or at once”. For example, consider the possibility to analyse a large dataset by downloading or accessing only a subset of the data at a  time (e.g., stream 1 TB at a time from a big dataset of 500 TB).
* Define the expected speed and the reliability of connection between storage and compute.
* Determine which software you are going to use. If it is a proprietary software, you should check possible licensing issues. Check if it only runs on specific operative systems (Windows, MacOS, Linux,…).
* Establish if and what reference datasets you need.
* In the case of collaborative projects, define who can access the data and the computational resource for analysis (specify from what device, if possible). Check policy about data access between different Countries. Try to establish a versioning system.

### Solutions

* Try to estimate the volume of:
  * raw data files necessary for the process/analysis;
  * data files generated during the computational analysis as intermediate files;
  * results data files.
* Communicate your expectations about speed and the reliability of connection between storage and compute to the IT team. This could depend on the communication protocols that the compute and storage systems use.
* It is recommended to ask about the time span for analysis to colleagues or bioinformatic support that have done similar work before. This could save you money and time.
* If you need some reference datasets (e.g the reference genomes such as human genome.), ask IT if they provide it or consult  bioinformaticians that can set up automated public reference dataset retrieval.
* For small data files and private projects, using the computational resources of your own laptop might be fine, but make sure to preserve the reproducibility of your work by using data analysis software such as {% tool "galaxy" %} or {% tool "r-markdown" %}.
* For small data volume and small collaborative projects, a commonly accessible cloud storage, such as {% tool "nextcloud" %} (on-premises) or {% tool "owncloud" %} might be fine. Adhere to the policies of your institute.
* For large data volume and bigger collaborative projects, you need a large storage volume on fast hardware that is closely tied to a computational resource accessible to multiple users, such as {% tool "rucio" %}, {% tool "transmart" %}, {% tool "semares" %} or {% tool "research-data-management-platform" %}.

## Where should you store the data after the end of the project?

### Description

After the end of the project, all the relevant (meta)data (to guarantee reproducibility) should be preserved for a certain amount of time, that is usually defined by funders or institution policy. However, where to preserve data that are not needed for active processing or analysis anymore is a common question in data management.

### Considerations

* Data preservation doesn’t refer to a place nor to a specific storage solution, but rather to the way or “how” data can be stored. As described in our [Preservation page](preserving), numerous precautions need to be implemented by people with a variety of technical skills to preserve data.
* Estimate the volume of the (meta)data files that need to be preserved after the end of the project. Consider using a compressed file format to minimize the data volume.
* Define the amount of time (hours, days…) that you could wait in case the data needs to be reanalysed in the future.
* It is a good practice to publish your data in public data repositories. Usually, data publication in repositories is a requirement for scientific journals and funders. Repositories preserve your data for a long time, sometimes for free. See our [Data publication page](data_publication) for more information.
* Institutes or universities could have specific policies for data preservation. For example, your institute can ask you to preserve the data internally for 5 years after the project, even if the same data is available in public repositories.

### Solutions

* Based on the funders or institutional policy about data preservation, the data volume and the retrieval time span, discuss with the IT team what preservation solutions they can offer (i.e., data archiving services in your Country) and the costs, so that you can budget for it in your DMP.
* Publish your data in public repositories, and they will preserve the data for you.
