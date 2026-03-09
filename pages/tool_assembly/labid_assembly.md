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

## What is LabID?
{% tool "labid" %} is an open-source web-based platform for research data management in life science institutes, featuring sample and dataset management, an inventory management system and an electronic lab notebook. 

LabID allows recording extensive experimental information about the provenance of data (samples, reagents, instrument, protocols, assay parameters) and is designed to help individual scientists, research groups and core facilities better manage, annotate and share their research according to FAIR principles. 

LabID also features an electronic lab notebook, and a "workflow integration" to keep track of the execution of workflows such as Galaxy or Nextflow. It also facilitates workflow versioning, and publication by integrating with e.g {% tool "workflowhub" %} and {% tool "git" %} repositories.
Besides, LabID takes advantage of the Workflow RO-Crate and Workflow Run RO-Crate profiles to import workflows from WorkflowHub, and export workflows and workflow runs to other platforms.

{% include image.html file="labid_overview.png" caption="Overview of LabID functionalities" alt="overview of LabID functionalities" %}


## Key Features

LabID is powered by a database that allows recording and interconnecting laboratory entities involved in life-science research (samples, reagents, instruments, protocols...). The result is a comprehensive knowledge graph capturing relationships between experimental components, enabling researchers to trace data provenance and share the full context of their research.

- **Sample Management**: Track and organize biological samples with complete provenance information
- **Dataset Management**: Register and annotate datasets with metadata and experimental parameters
- **Electronic Lab Notebook**: Document experiments and observations
- **Inventory System**: Manage reagents, instruments, and other lab resources
- **Workflow Integration**: Keep track of worflow versions and workflow executions for platforms like Galaxy or Nextflow, and custom scripts. Import and export from/to platforms like WorkflowHub and Git.

Below is a video with an overview of LabID's features (the video dates back from the time the software was called "Stocks", but most presented features are still there).  
{% include video.html file="https://s3.embl.de/gbcs-public/labid-user-docs/labid-overview.mov" caption="LabID overview" %}

## Which tasks can be solved with LabID?
- referencing instruments, reagents and specimen available in an institute or research team
- documenting assays performed in the lab, [associating](data_interlinking) them to the instrument, reagent and specimen used (e.g imaging of some tissue on a microscope)
- [storing and archiving](data_organisation) of raw and processed data (e.g archiving a copy to a S3 bucket)
- [adding metadata](metadata_management) to any entity using custom or controlled vocabulary  
- [sharing](sharing) data, protocols and assays with internal colleagues
- document the execution of a script or workflow, together with the associated data and parameters. Export the resulting "workflow run" as a [Worklfow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/profiles/workflow_run_crate/). 

## How to access LabID?
LabID is typically installed at the level of an institute or research group on a unix server. The LabID user interface is then accessible via a web browser, on client machine that can access the server.    

A public demo server is available at [https://labid-demo.embl.de/](https://labid-demo.embl.de/) so you can get a feeling of the user interface.  
Most [trainings from the user-documentation](https://grp-gbcs.embl-community.io/labid-user-docs/training/) can also be followed along with this demo server.  

## What technology is it built with?
Under the hood, LabID is a client/server solution, similar in its architecture to e.g {% tool "omero" %}. It is made a several components :
- the server or "backend", written in python and using the [Django framework](https://www.djangoproject.com/)
- a postgres relational database, used to store reference to data and metadata 
- the user interface or "frontend", written in [Vue.js](https://vuejs.org/)
- a python library and commmand line interface, to automate e.g data-registration tasks

## Links
* [GitLab repositories](https://gitlab.com/lab-integrated-data)
* [LabID user documentation](https://grp-gbcs.embl-community.io/labid-user-docs/)
* [Slack channel](https://join.slack.com/t/labintegrateddata/shared_invite/zt-2eb4ivxyc-1C4RZP_For0uiWcHeiTw0Q)
* [Demo server](https://labid-demo.embl.de/)

## Funding
LabID is developed and maintained by the [MODIS team](https://www.embl.org/groups/modis/) at the EMBL Heidelberg.

The workflow integration of LabID was supported through the Open Science Clusters’ Action for Research and Society ([OSCARS](oscars-project.eu)) European project under grant agreement Nº101129751.  
See [LabID PROV](https://oscars-project.eu/projects/labid-prov-tracking-and-sharing-data-provenance-ro-crate-lab-integrated-data). 
