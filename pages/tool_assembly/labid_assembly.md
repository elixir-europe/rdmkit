---
title: LabID
contributors: [Laurent Thomas] 
page_id: labid
affiliations: [EMBL Heidelberg]
related_pages: 
  Your_tasks: [data_organisation, data provenance, storage, metadata, machine learning, single-cell sequencing]
  Your_domain: [bioimaging_data, proteomics, plant sciences]
description: LabID is an all-in-one FAIR data management platform for life sciences institutes. It allows keeping track of datasets, samples, workflows and inventory while featuring an Electronic Lab Notebook.
---

{% include image.html file="labid.png" caption="" alt="Logo of LabID" %}

Lab Integrated Data ({% tool "labid" %}) is an open-source web-based platform for research data management in life science institutes, featuring sample and dataset management, an inventory management system and an electronic lab notebook.
LabID allows recording extensive experimental information about the provenance of data (samples, reagents, instrument, protocols, assay parameters) and is designed to help individual scientists, research groups and core facilities better manage, annotate and share their research according to FAIR principles. 
LabID also features an electronic lab notebook, and a "workflow integration" to keep track of the execution of workflows such as Galaxy, Nextflow... It also facilitates workflow versioning, and publication by integrating with e.g {% tool "workflowhub" %} and {% tool "git" %} repositories.
Besides, LabID takes advantage of the Workflow RO-Crate and Workflow Run RO-Crate profiles to import workflows from WorkflowHub, and export workflows and workflow runs to other platforms.

![LabID workflow integration](../../assets/img/labid-screenshot.png)

## Resources
* Open-source repositories for the LabID project are hosted on [GitLab](https://gitlab.com/lab-integrated-data).  
* The documentation is available at https://grp-gbcs.embl-community.io/labid-user-docs/.

## Funding
This work was supported through the Open Science Clusters’ Action for Research and Society ([OSCARS](oscars-project.eu)) European project under grant agreement Nº101129751.  
See [LabID PROV](https://oscars-project.eu/projects/labid-prov-tracking-and-sharing-data-provenance-ro-crate-lab-integrated-data). 
