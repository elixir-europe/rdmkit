---

title: Luxembourg
country_code: LU
contributors: [Pinar Alper, Marina Popleteeva, Vilem Ded, Wei Gu]
coordinators: [Wei Gu]

# Link to other pages in the tool assembly section on the RDMkit by listing the page_id 
related_pages:
  Tool_assembly: [transmed]

training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/nodes/luxembourg
  - name: Materials for the ELIXIR Luxembourg course on "Best Practices in Research Data Management and Stewardship."
    registry: Zenodo
    url: https://zenodo.org/communities/elixir-lu/


# Refer to entries of the "main_tool_and_resource_table" if institutions, organisations and projects from the country contribute to the development of international tools and resources. 
ref_to_main_resources: 
  -  fair-cookbook
  -  covid-19-disease-map
  -  daisy
  -  data-catalog
  -  dpia-knowledge-model

# List here tools and resources mainly relevant for the specific country
national_resources: 
  - name: learning.DSW 
    description: A training instance of Data Steward Wizard (DSW), which has the FNR and the DPIA templates.
    how_to_access: registration
    instance_of: data-stewardship-wizard
    related_pages:
      Your_tasks: [dmp]
    url: https://learning.dsw.elixir-europe.org/dashboard

  - name: DPMRoadmap @ ELIXIR Luxembourg
    description: This instance of DMPOnline is provided by ELIXIR Luxembourg and has FNR template for Data Management Plan (DMP).
    how_to_access: registration
    instance_of: dmproadmap
    related_pages:
      Your_tasks: [dmp]
    url: https://dmponline.elixir-luxembourg.org/

  - name: Luxembourg COVID-19 Data Portal
    description: The Luxembourgish COVID-19 Data Portal acts as a collection of links and provides information to support researchers to utilise Luxembourgish and European infrastructures for data sharing.  
    instance_of: covid-19-data-portal
    related_pages:
      Tool_assembly: [covid19_data_portal]
      Your_domain: [human data]
      Your_tasks: [sensitive, existing data, data publication]
    url: https://covid19dataportal.lu/

---
<!---All the resources added above will appear on the table at the bottom of the page--->

<!---Following information for the page text--->
<!---Use this template as guidance, all fields are optional. Feel free to modify any section if you think it is necessary--->
<!---If the information is already in another resource, please include the link instead of duplicating information--->
<!---Please focus on resources that are relevant for the whole country for life sciences--->

## Introduction 
<!---General RDM considerations for your country, how to deal with RDM on a national level--->
On this page you will find an overview of data management resources available for the Luxembourgish life science research community. In addition to information provided here, the reader is advised to read the [Research Luxembourg website](https://www.researchluxembourg.org/en/), which describes the Luxembourg research landscape and developments.

## Funders
Luxembourg’s main research funding body is the [Fonds National de la Recherché (FNR)](https://www.fnr.lu/). The FNR promotes open-access to scientific publication through its [open-access fund](https://www.fnr.lu/funding-instruments/open-access-fund/). To increase the re-usability of research outputs the FNR adopts a [research data management policy](https://www.fnr.lu/open-science-new-fnr-policy-on-research-data-management/) and expects all funded projects to prepare and implement Data Management Plans (DMP) in line with Science Europe guidelines. [DMP guiding questions](https://storage.fnr.lu/index.php/s/urQOCMeKlgXexZF) are provided in the FNR grant management system.

## Regulations
<!--- Ethical and legal regulations in the country, committees etc --->

Luxembourg’s National Commission for Data Protection ([CNPD](https://cnpd.public.lu/en.html)), through its Open Data Protection Laboratory ([DaProLab](https://cnpd.public.lu/en/actualites/national/2020/03/dapro-lab-recherche.html)), provides online guidance and information sessions on data protection for research.

Luxembourg’s National Research Ethics Committee ([CNER](https://www.cner.lu/en-gb/Home)) provides ethical oversight and individual assessment for research projects, particularly for the collection, use and secondary use of data/samples from human subjects.

## Research infrastructures and resources 
<!--- e.g. human data, covid-19. Please, only add domain-specific resources that you think don't fit in the table at the bottom--->
[ELIXIR Lxembourg](https://elixir-luxembourg.org) provides resources for life science data management, focusing on the areas of translational biomedicine data hosting, data protection, data FAIRification and reproducible research. ELIXIR Luxembourg provides the [TransMed tool assembly](transmed_assembly) to support research project with sensitive human data.

The Luxembourgish node of [EATRIS](https://eatris.eu/countries/luxembourg/) provides services in translational medicine.

Luxembourg National Data Service (LNDS) is a government established organisation aiming to support and stimulate value creation from data in Luxembourg. LNDS provides a variety of data management and stewardship services to enable the secondary use of data. LNDS services are domain-agnostic and support the life sciences as well as other domains. 

The Integrated BioBank of Luxembourg ([IBBL](https://www.lih.lu/en/translational-medicine/translational-medicine-operations-hub/integrated-biobank-of-luxembourg-ibbl/)) is a not-for-profit institute and the national biobanking platform hosted within the Luxembourg Institute of Health ([LIH](https://www.lih.lu/en/)). IBBL provides a full range of biobanking services to the biomedical sector including the industry, academia and EU consortia.

University of Luxembourg’s High-Performance Computing Platform ([ULHPC](https://hpc.uni.lu)) and the EuroHPC  Joint Intitiative’s [MeluXina supercomputer](https://docs.lxp.lu) offer HPC capabilities for Luxembourg researchers, public sector and the industry. 
