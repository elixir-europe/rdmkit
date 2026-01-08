---

title: Czech Republic
country_code: CZ
contributors: [Karel Berka, Marek Suchánek]
coordinators: [Karel Berka]

# Link to other pages in the tool assembly section on the RDMkit by listing the page_id 
related_pages:
  Tool_assembly: []

training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/content_providers/elixir-the-czech-republic-node
  - name: ELIXIR-CZ YouTube
    registry: YouTube
    url: https://www.youtube.com/channel/UCt0SKet24szBGjN-V1d4EKw
  - name: ELIXIR-CZ GitHub
    registry: GitHub
    url: https://github.com/ELIXIR-CZ
  - name: ELIXIR-CZ Zenodo
    registry: Zenodo
    url: https://zenodo.org/communities/elixir-cz/

ref_to_main_resources: 
  - galaxy
  - data-stewardship-wizard

national_resources: 
  - name: Galaxy MetaCentrum
    description: Galaxy MetaCentrum is a Galaxy instance managed by the Czech ELIXIR node and [e-INFRA](https://www.e-infra.cz/en). It provides extra support for [RepeatExplorer](https://repeatexplorer-elixir.cerit-sc.cz/) tool for plant genomic analysis.
    how_to_access:
    instance_of: galaxy
    related_pages:
      Tool_assembly: []
      Your_domain: [plant]
      Your_role: [researcher]
      Your_tasks: [data_analysis]
    url: https://galaxy.metacentrum.cz/
    registry:
      biotools: repeat_explorer
  - name: e-INFRA CZ (Supercomputing and Data Services)
    description: e-INFRA CZ provides integrated high-performance research computing/data storage environment, providing world-class services to government, industry, and researchers. It also cooperates with European Open Science Cloud (EOSC) implementation in the Czech Republic.
    how_to_access:
    related_pages:
      Tool_assembly: []
      Your_domain: []
      Your_role: [data_steward, research_software_engineer]
      Your_tasks: [data_analysis, storage]
    url: https://www.e-infra.cz/en
  - name: ownCloud@CESNET
    description: CESNET-hosted ownCloud is a 100 GB cloud storage freely available for Czech scientists to manage their data from any research projects.
    how_to_access: To use the CESNET-hosted ownCloud, you have to be an employee or a student of a Czech academic organization. For technical reasons, you have to have an account in [eduID.cz](https://eduid.cz).
    instance_of: owncloud
    related_pages:
      Tool_assembly: []
      Your_domain: []
      Your_role: [researcher, research_software_engineer]
      Your_tasks: [storage, data_transfer, data_organisation]
    url: https://du.cesnet.cz/en/navody/owncloud/start/
  - name: Czech National Repository
    description: National Repository (NR) is a service provided to the scientific and research communities in the Czech Republic to store their generated research data together with persistent DOI identifier. NR service is currently under the pilot program. 
    how_to_access: To use National Repository, you have to be an employee or a student of a Czech academic organization. For technical reasons, you have to have an account in [eduID.cz](https://eduid.cz) and if you want to upload.
    instance_of:
    related_pages:
      Tool_assembly: []
      Your_domain: []
      Your_role: [researcher, data_steward, research_software_engineer]
      Your_tasks: [storage, existing_data, identifiers, dmp]
    url: https://data.narodni-repozitar.cz/

---

## Introduction 

An overview of data management services provided by the ELIXIR Czech Republic can be found on the [ELIXIR Czech Republic website](https://www.elixir-czech.cz/).
Details about national guidelines, tools and services can be found as [RDM services](https://www.elixir-czech.cz/?s=data+management).


## Funders

In line with European funders, Czech research funders are asking for Data Management Plans (DMP) and support Open Science. Consult the funders' webpage and their policy about data management and Open Science.
* [Czech Science Foundation (GAČR)](https://gacr.cz/en/)
  * [GAČR Research policy](https://gacr.cz/en/extracts-from-tender-documents/)
* [Technology Agency of the Czech Republic (TAČR)](https://www.tacr.cz/en/)
* [TAČR Open Access policy](https://www.tacr.cz/en/open-access-in-the-kappa-programme/)
* Special Research Fund (BOF) from Universities
* [ Programme Johannes Amos Comenius (OP JAK)](https://opjak.cz/en/)
* EU-Team and/or Research support team from Universities
  * [Charles University Open Science Support Centre](https://openscience.cuni.cz/OSCIEN-1.html)
  * [Masaryk University Open Science](https://openscience.muni.cz/en)
  * [Palacký University Open Science](https://openscience.upol.cz/en/)
* [National Information Centre for European Research (NICER), Technology Centre Prague](https://www.tc.cz/en/what-we-do/1/national-information-centre-for-european-research-) (for help with navigating the EU funding system)
