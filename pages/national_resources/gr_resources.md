---
title: Greece
description: A comprehensive guide to research data management (RDM) in Greece, featuring tools, resources, and services tailored for the life sciences community.
country_code: GR
contributors: [Eleni Adamidi, Thanasis Vergoulis, Alexandros Dimopoulos]
coordinators: [Thanasis Vergoulis, Alexandros Dimopoulos]

training:
  - name: "ELIXIR GREECE: Prospects of data and tools for ELIXIR Greece"
    registry: Zenodo
    description: This presentation provides an overview of the data, tools, and standards used in ELIXIR Greece, as well as guidelines for effective research data management, with an emphasis on best practices for open science and data stewardship.
    url: https://zenodo.org/records/4043630#.ZACFtE_Nx60
  - name: "The ELIXIR GREECE Galaxy server including best practices tools and workflows for the analysis of SARS-CoV-2 data"
    registry: Zenodo
    description: This presentation highlights how the local Greek Galaxy instance at usegalaxy.elixir-greece.org makes SARS-CoV-2 data analysis accessible and reproducible using open software and public research infrastructures. It showcases practical workflows in genomics, proteomics, evolution, and cheminformatics, with comprehensive training materials available to support collaborative research.
    url: https://zenodo.org/records/4042834#.ZACFUk9vD9M

# Refer to entries of the "main_tool_and_resource_table" if institutions, organizations and projects from the country contribute to the development of international tools and resources. 

ref_to_main_resources:
  - argos

# List here tools and resources mainly relevant for the specific country
national_resources: 
  - name: HYPATIA - Cloud Infrastructure for ELIXIR Greece
    description:  HYPATIA is a cloud-based infrastructure that has been developed to support the computational needs of the ELIXIR Greece community and the wider life sciences community including researchers and institutions in Greece and internationally.
    how_to_access:  Login via Life Science (LS) Login required.
    related_pages:
      Your_tasks: [data_analysis, storage, transfer]
    url: https://hypatia.athenarc.gr/
    
  - name: National instance of Genomic Data Infrastructure for ELIXIR Greece
    description:  An instance of the Genomic Data Infrastructure [GDI](https://gdi.onemilliongenomes.eu/) on ELIXIR Greece, for secure genomic data management, including storage, discovery, access, and reception. This is a pilot instance based on the GDI Starter Kit.
    how_to_access:  Login via Life Science (LS) Login required to access ELIXIR-Greece GDI Portal.
    related_pages:
      Your_domain: [human_data]
      Your_tasks: [sensitive, data_publication, existing_data]
    url: https://login.gdi.elixir-greece.org/

  - name: Greek COVID-19 Data Portal
    description: Provides information, guidelines, tools and services to support researchers to utilise Greek and European infrastructures for data sharing. The portal is a national node of the European COVID-19 Data Portal.
    url: https://covid19dataportal.gr/
    related_pages:
     Tool_assembly: [covid19_data_portal]
    instance_of: covid-19-data-portal


---

## Introduction 
This page provides useful information and resources with a focus on research data management in Greece. An overview of services provided by ELIXIR Greece can be found on [the node website](https://www.elixir-greece.org/node/268) .

<!---## Funders--->

<!---## Regulations--->
<!--- Ethical and legal regulations in the country, committees, etc. --->

## Funders in Greece
Research funding in Greece is primarily provided by **National and European funding agencies**. The major national funders supporting Open Science and Research Data Management (RDM) include:

- The **[Hellenic Foundation for Research and Innovation (HFRI)](https://www.elidek.gr/)** which is a key funder supporting fundamental and applied research in Greece. 

  HFRI Policies and Requirements:
  - Encourages Open Science and FAIR data principles.
  - Requires researchers to submit a Data Management Plan (DMP) in various time points depending on each call.
  - Supports infrastructure for Open Access to research outputs.

- The **[General Secretariat for Research and Innovation (GSRI)](https://gsri.gov.gr/)** which operates under the Ministry of Development and Investments and funds major research projects in Greece. 

  GSRI Policies and Requirements:
  - Funds research projects across all disciplines, including Open Science initiatives.
  - Promotes adherence to EOSC policies and data sharing.
  - Provides funding for data infrastructures, repositories, and research data management tools.

## Policies and Recommendations for Research Data in Greece

Greece has made significant progress in adopting Open Science policies, aligning with European initiatives such as the European Open Science Cloud (EOSC). The country has established a national initiative called **Hellenic Open Science Initiative** to coordinate and implement national policies for Open Science and research data management.

- The **[Hellenic Open Science Initiative (HOSI)](https://www.hellenicopenscience.gr/en/welcome-to-os-greece/about-hosi)** was founded on February 28, 2022, by 13 leading Greek research, technology, and innovation organizations. Its goal is to support the coordinated and participatory implementation of Open Science policies in Greece while ensuring national representation in EOSC.

  HOSI Key Policies:
   - Open Science is a national priority and is integrated into Greece’s Digital Transformation Strategy.
   - Policies are based on the principle "as open as possible, as closed as necessary."
   - National coordination efforts support FAIR (Findable, Accessible, Interoperable, Reusable) data principles.

- The **National Research Data Management Policy** aims to ensure open access to research data, particularly for publicly funded research. The policy is outlined in the **[National Plan for Open Science](https://zenodo.org/records/3908953#.Ye7gdepBw2w)**, including:

  Key Principles:
   - **Open by default**: Research data must be openly available unless legal or ethical restrictions apply.
   - **FAIR principles**: Research data should be managed following international standards for metadata and licensing.
   - **Permanent Identifiers**: Research data must be assigned persistent digital identifiers (DOIs).
   - **Machine-readable metadata**: Research software must be documented using OpenAIRE Guidelines, codemeta.json, and {% tool "schema-org" %} attributes.
   - **Open Data Licenses**: Researchers should use standardized open licenses, with a preference for CC-BY (Attribution Only).
   - **Mandatory Data Management Plans (DMPs)**: All research projects must include a Data Management Plan (DMP).

- Part of the **National Research Data Management Policy** has been embedded in the Greece’s **[Digital Transformation Strategy 2020-2025](https://digitalstrategy.gov.gr/vivlos_pdf)**. This strategy highlights Open Science as a key pillar for modernizing the country’s research landscape outlining its importance in fostering collaboration, transparency, and innovation in scientific research. The strategy aligns with European Open Science Cloud (EOSC) guidelines, ensuring interoperability with European research infrastructures and reinforcing Greece’s role in EOSC.  

## Domain-specific infrastructures or resources 
The [Greek COVID-19 Portal](https://covid19dataportal.gr/) provides information, guidelines, tools and services to support researchers to utilise Greek and European infrastructures for data sharing. The portal is a national node of the European COVID-19 Data Portal.

