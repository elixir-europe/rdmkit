---

title: Luxembourg
search_exclude: true
country_code: LU
contributors: [Pinar Alper, Marina Popleteeva, Vilem Ded, Wei Gu]
coordinators: [Wei Gu]

# Link to other pages in the tool assembly section on the RDMkit by listing the page_id 
related_pages:
  tool_assembly: [transmed]

training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/nodes/luxembourg
  - name: Materials for the ELIXIR Luxembourg course on \"Best Practices in Research Data Management and Stewardship.\"
    registry: Zenodo
    url: https://zenodo.org/communities/elixir-lu/


# Refer to entries of the "main_tool_ and_resource_table" if institutions, organizations and projects from the country contribute to the development of international tools and resources. 
ref_to_main_resources: 
  -  FAIR Cookbook
  -  COVID-19 Disease Map
  -  DAISY
  -  Data Catalog
  -  DPIA Knowledge Model

# List here tools and resources mainly relevant for the specific country
national_resources: 
  - name: learning.DSW 
    description: A training instance of Data Steward Wizard (DSW), which has the FNR and the DPIA templates.
    how_to_access: registration
    instance_of: Data Stewardship Wizard
    related_pages:
      your_tasks: [dmp]
    url: https://learning.ds-wizard.org/dashboard

  - name: DPMRoadmap @ ELIXIR Luxembourg
    description: This instance of DMPOnline is provided by ELIXIR Luxembourg and has FNR template for Data Management Plan (DMP).
    how_to_access: registration
    instance_of: DMPRoadmap
    related_pages:
      your_tasks: [dmp]
    url: https://dmponline.elixir-luxembourg.org/

  - name: Luxembourg Covid-19 data portal
    description: The Luxembourgish COVID-19 Data Portal acts as a collection of links and provides information to support researchers to utilise Luxembourgish and European infrastructures for data sharing.  
      related_pages:
      tool_assembly: [Covid-19]
      your_domain: [human data]
      your_tasks: [sensitive, existing data, data publication]
    url: https://covid19dataportal.lu/

 - name: <!---REPLACE THIS with the national resources about RDM in life sciences such as local instances of tools, guidelines or regulations--->
    description:
    how_to_access: <!--- REPLACE THIS free text to explain if credentials, login, specific affiliations etc are needed to access the resource or tool--->
    instance_of: <!--- REPLACE THIS with the tool name of which this resource is an instance of, taken from the all tools and resources page --->
    related_pages:
      tool_assembly: [<!---REPLACE THIS with the page ID of the tool_assembly pages that you want to list here as related pages--->]
      your_domain: [<!---REPLACE THIS with the page ID of the domain pages that you want to list here as related pages--->]
      your_role: [<!---REPLACE THIS with the page ID of the your_role pages that you want to list here as related pages--->]
      your_tasks: [<!---REPLACE THIS with the page ID of the your_tasks pages that you want to list here as related pages--->]
    url:
    registry:
      biotools: <!--- DELETE ME if not needed --->
      fairsharing: <!--- DELETE ME if not needed --->
      tess: <!--- DELETE ME if not needed --->
---
<!---All the resources added above will appear on the table at the bottom of the page--->

<!---Following information for the page text--->
<!---Use this template as guidance, all fields are optional. Feel free to modify any section if you think it is necessary--->
<!---If the information is already in another resource, please include the link instead of duplicating information--->
<!---Please focus on resources that are relevant for the whole country for life sciences--->

## Introduction 
<!---General RDM considerations for your country, how to deal with RDM on a national level--->
This page provides an overview of data management resources in Luxembourg. The target audience is scientific community in life science. An overview of services provided by ELIXIR-LU can be found on [this webpage](https://elixir-luxembourg.org/services/catalog/).

## Funders
Luxembourg’s main research funding body is the [Fonds National de la Recherche (FNR)](https://www.fnr.lu/). The FNR promotes open-access to scientific publication through its [open-access fund](https://www.fnr.lu/funding-instruments/open-access-fund/). To increase the re-usability of research outputs the FNR adopt a research data management policy and expects all funded projects to prepare and implement Data Management Plans (DMP) in line with Science Europe guidelines. [Data Management Plan guiding questions](https://storage.fnr.lu/index.php/s/urQOCMeKlgXexZF) are provided in FNR grant management system.

## Regulations
<!--- Ethical and legal regulations in the country, committees etc --->

## Research infrastructures and resources 
<!--- e.g. human data, covid-19. Please, only add domain-specific resources that you think don't fit in the table at the bottom--->
[ELIXIR Luxembourg](https://elixir-luxembourg.org) provides resources for life science data management, with the focus areas of translational biomedicine data hosting, data protection, data FAIRification and reproducible research. 

Luxembourg is part of [EATRIS](https://eatris.eu/countries/luxembourg/) and provides services in translational medicine. ELIXIR Luxembourg also provides the [TransMed tool assembly](transmed_assembly) to support research project with sensitive human data.

Luxembourg National Data Exchange Platform (PNED) is a government established infrastructure that provides services for the sharing and secondary use of data. PNED services are domain-agnostic, but includes lifesciences data management.  

[Uni.lu HPC](https://hpc.uni.lu/) and [EuroHPC MeluXina](https://luxprovide.lu/) offer high performance computing infrastructure combined with huge data storage capacity to Luxembourg public research. <!--Access: available to all research and industrial partners for the duration of joint projects. Related pages: data analysis, data storage. -->
