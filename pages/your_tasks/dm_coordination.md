---
title: Project data management coordination
description: How to coordinate and organise data management activities in collaborative or multi-parter projects.
contributors: [Robert Andrews, Stefanie Meyer, Tereza Motalova, Graham Parton, Marko Petek, Maja Zagorščak, Karolina Zavoralova, Karel Berka, Korbinian Bösl, Flora D'Anna, Niclas Jareborg, Yvonne Kallberg, Paulette Lieby]
page_id: dm_coordination
related_pages: 
  tool_assembly: []
training:
  - name:
    registry:
    url:
---

## How to organise data management in collaborative projects?
 
### Description

Most national and European funders of (multi-partner) projects now require [Data management plans (DMPs)](data_management_plan) that are evaluated before grant awards. Therefore, coordinators of project consortia need to mobilise a dedicated effort to decide on the approach for data management, developing the DMP, using the DMP as a live document throughout the project, and so on, to ensure that the research outputs from the project follow the [FAIR principles](https://www.nature.com/articles/sdata201618). This is a new terrain for many people, requiring them to grasp what this entails and figure out who to approach.

### Considerations

* During the writing stage of a grant proposal, members of a multi-partner project or consortium need to agree on how to address data management during and after the project, and formalise the way of working on the grant proposal.
* What information regarding data management is needed at different phases (preparation, submission, execution, wrap-up, reporting to the funders) in the project needs to be decided in advance.
* There is a need to understand the institutional landscape in terms of legal requirements, data policies, IT services, and so on, which are essential to carry out the project. They might vary among individual institutions involved in the project consortium:
  * Not every institution has a centralised IT department to support data management; often data management is carried out by the group itself without help from the IT department.
  * Legal and ethical requirements, data policies, etc., can be very different or even not be in place in some institutions.
* Data management strategies and the types of data generated can change during the project.


### Solutions

Here, we provide some advice and methods to help consortia with data management coordination tasks:

* In a consortium, establishing a Data Management Working Group (DMWG) should be one of the first actions taken during the establishment of the consortium. Each partner should have representatives for data management, especially the partners that will generate and/or use a higher volume of data. If possible, the representatives should have a working knowledge of data management. During the writing stage, the DMWG should be responsible for deciding how data management will be addressed during (and after) the project.
* It is highly recommended that, if possible, the establishment of the DMWG is included as a project task, deliverable or milestone. Each partner should allocate personnel time for the DMWG. Dedicating part of the project (a work package, for instance) to data management helps with clarifying tasks and responsibilities. The DMWG should have defined milestones and deliverables in the project plan.
* All partners should agree on what needs to be added to the budget for data management purposes: hardware requirements (long-term storage space, servers, etc.), cloud services, software licensing, software developers and data stewards/managers, that collectively contribute to the costs of making data FAIR. It is advisable to consult with available IT support, data centres, and instrument providers at each partner’s side to evaluate options and costs.
* DMWG should list the types of data to be collected, including descriptions of file types (to enable archive and sharing) and estimated file sizes (to enable storage costing).
* Ideally, the DMWG should agree on: data deposition databases, data sharing and archiving, and metadata standards (model, checklist, format, ontologies and controlled vocabularies) during the writing of the proposal. However, if it is not feasible at the writing stage, making these decisions can be added as early tasks, milestones or deliverables of the project.
* As a monitoring mechanism, some of the milestones and deliverables should be the successful creation of datasets with their metadata and possibly their deposition.
* If applicable, each partner (actually, its representative) should consult with personal data legislation experts (e.g. GDPR or equivalent), Data Protection Officers (DPOs) and the legal office of the institution (e.g. for technology transfer) to reach a consensus at the consortium level about data protection, availability and open science.
* It is recommended to discuss as early as possible the licensing and the intellectual property (IP) rights of project outcomes (datasets, software, tools, etc.), to comply with open science requirements and to avoid legal issues later on. 
* Discuss a common plan for the sharing of data, [documentation and metadata](metadata_management) between partners.
* Tools such as {% tool "fair-implementation-profile" %} and {% tool "fip-wizard" %} could be used to explicitly declare FAIR Implementation Profiles.

## How to execute data management in collaborative projects?

### Description 
Once the project is awarded, the data management plan needs to be executed throughout its duration.

### Considerations 
* Some data management challenges may not have been foreseen at the pre-award stage.
* Possible difficulties during the execution of the DMP by individual partners may arise. Not all partners have the same skills and resources.
* Possible problems with data exchange between partners can resurface during the project. 
* Consider contacting and establishing collaborations for depositing data with key repositories, e.g. setting up an {% tool "ena-compare-data-hubs" %} for depositing sequence data at the {% tool "european-nucleotide-archive" %}
or collaborating with {% tool "biostudies" %}, that can provide a project-specific data collection for early data sharing and sustainable data publishing (see, for example, [this dedicated collection](https://www.ebi.ac.uk/biostudies/EU-ToxRisk/studies) for the [EU-ToxRisk](https://eu-toxrisk.eu/) project on toxicity testing and risk assessment)

### Solutions 
* The DMWG should have regular meetings to find appropriate solutions to arising data management issues.
* The DMWG should make sure all partners are able to implement the data management strategies.
* Establish a strategy for documentation and exchange of data (within the project and with other collaborators):
  * Evaluate the value of your project outcomes (datasets, data, tools, etc.) and establish which of them are worth preserving long term. 
  * Agree on relevant data formats (e.g. TXT, MP4, FASTQ), metadata schemas, checklists and controlled vocabularies/ontologies that are recognised as standards by scientific communities - all these depend on the type of data generated. Read more about [documentation and metadata](metadata_management).
* Ensure that all partners deposit data according to the agreed [data publication](data_publication) strategy.
* The DMP should be revisited on a regular basis and updated when necessary. Things to look out for are:
  * Ensuring that the chosen [data repositories](data_publication#which-repository-should-you-use-to-publish-your-data) are fit for purpose.
  * Ensuring that the metadata standards and the ontologies used are fit for purpose. 
  * Ensuring that the strategy for documentation and data exchange is adequate.
  * Planning for long-term storage and data sharing for all partners.
* Try to keep it simple and find a balance between the amount of necessary details, to avoid making documentation difficult and discouraging.

## How to sustain and monitor data management in collaborative projects?

### Description
If you want to secure a constant effort on research data management across the project period and after the project, with stable data quality, this will require dedicated monitoring and focus from the project management and the DMWG.

### Considerations
* Be aware of a possible lack of storage infrastructure, thus requiring financing that might not be part of the initially proposed project budget.
* Monitor that data is not lost, e.g. by missing or unimplemented backup procedures. 
* Monitor that metadata is collected, and organised according to agreed standards and no discrepancies between metadata and reality exist (e.g. sample ID mismatches).
* Copyright licenses connected to the reuse of the project outputs should be applicable long-term beyond the project's lifetime.
* Some data might need to be made available through restricted access mechanisms, e.g. for sensitive (personal) data. Safeguarding the functionality of a data access committee beyond the project period requires coordination on an institutional level.
* The quality, size, location, and reuse of datasets might be an object of project reporting and be used as a performance indicator. 

### Solutions
* For long-term preservation of valuable project outcomes, try to look for additional funding within your organization or from other funders, or create a feasible strategy to use e.g. institutional, national, or international repositories, with their preservation policy.
* Automate backups as much as possible with your IT department and test them. Backup log files should be actively monitored for potential issues.
* The DMWG should perform regular checks with data hosting project partners to check that data and metadata are produced according to the DMP, and that agreed backup routines are followed. 
* Post-project preservation of data should consider reproducibility/replicability of the data from a long-term perspective, as well as the potential reuse value. You might want to consult a [data preservation](preserving) service (e.g. national data centres) regarding larger amounts of data. As an initial inspiration, you can start from [this data value checklist](https://www.bgs.ac.uk/download/ngdc-data-value-checklist/) and adapt it for your legal framework and domain.
* Do not leave the data holders with the impossible task of trying to figure out who can have access to the resources, but rather use a license that allows the re-use of data. For instance, some projects or funding bodies demand to use CC-BY-4.0 and refrain from using bespoke, non-standard license terms.
* If data is to be made available to others through a restricted access mechanism, the access granting procedure and responsibilities must be defined and implemented. Note that this *must* work after the end of the project.
