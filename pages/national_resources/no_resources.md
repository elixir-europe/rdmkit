---

title: Norway
country_code: "NO"
contributors: [Nazeefa Fatima,Federico Bianchini,Korbinian Bösl,Erin Calhoun]
coordinators: [Korbinian Bösl, Nazeefa Fatima]

related_pages:
  tool_assembly: [tsd, nels, marine_assembly, fairtracks]

training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/events?include_expired=true&node=Norway
  - name: ELIXIR Norway community in Zenodo
    registry: Zenodo
    url: https://zenodo.org/communities/elixir-no/?page=1&size=20
#  - name: ELIXIR Norway YouTube
#    registry: YouTube
#    url: https://www.youtube.com/channel/UCva4S9uWxXqyGnbSgxIbcwA


national_resources:
  - name: Feide
    description: Feide is the national solution for secure login and data exchange in education and research. Feide can be linked with [Life Science Login (LS Login)](https://elixir-europe.org/services/compute/aai) through [eduGAIN](https://edugain.org/).
    how_to_access: Everyone with an affiliation to a Norwegian academic institution.
    related_pages:
      tool_assembly: [tsd, nels, marine_assembly]
    url: https://www.feide.no/
  - name: DS-Wizard ELIXIR-Norway
    id: dsw-no
    description: DS-Wizard is a tool to aid the creation, organisation and sharing of data management plans. It provides scientists with guidance, facilitating the understanding of the key components of FAIR-oriented Data Stewardship. The template in this instance provides additional guidance on resources, laws and regulations in Norway.
    how_to_access: Life Science Login (LS Login) with Feide or upon registration
    instance_of: data-stewardship-wizard
    related_pages:
      tool_assembly: [tsd, nels, marine_assembly]
      your_tasks: [dmp]
    url: https://elixir-no.ds-wizard.org/
  - name: EasyDMP
    description: DMP tool from [UNINETT Sigma2 (SIKT)](https://www.sigma2.no/).
    instance_of:
    how_to_access: Feide
    related_pages:
      your_tasks: [dmp]
    url: https://easydmp.no/
  - name: Meta-pipe
    description: META-pipe is a pipeline for annotation and analysis of marine metagenomics samples, which provides insight into phylogenetic diversity, metabolic and functional potential of environmental communities.
    how_to_access: Feide or upon application
    related_pages:
      your_tasks: [data_analysis]
      tool_assembly: [marine_assembly]
    url:  https://mmp2.sfb.uit.no/metapipe/
  - name: Norwegian COVID-19 Data Portal
    description: The Norwegian COVID-19 Data Portal aims to bundle the Norwegian research efforts and offers guidelines, tools, databases and services to support Norwegian COVID-19 researchers.
    related_pages:
      your_domain: [human_data]
      your_tasks: [sensitive, existing_data, data_publication]
      tool_assembly: [covid-19_data_portal]
    url: https://covid19dataportal.no/
  - name: Federated EGA Norway node
    description: Federated instance collects metadata of -omics data collections stored in national or regional archives and makes them available for search through the main EGA portal. With this solution, sensitive data will not physically leave the country, but will reside on TSD.
    how_to_access: Life Science Login (LS Login); intended for data from Norwegian institutions
    instance_of: the-european-genome-phenome-archive
    related_pages:
      your_domain: [human_data]
      your_tasks: [sensitive, existing_data, data_publication]
      tool_assembly: [tsd]
    url: https://ega.elixir.no/
  - name: usegalaxy.no
    description: Galaxy is an open-source, web-based platform for data-intensive biomedical research. This instance of Galaxy is coupled with NeLS for easy data transfer.
    instance_of: galaxy
    how_to_access: Feide or upon application
    related_pages:
      your_tasks: [data_analysis, sensitive, existing_data, data_publication]
      tool_assembly: [nels]
    url: https://usegalaxy.no
  - name: NeLS
    description: Norwegian e-Infrastructure for Life Sciences enables Norwegian life scientists and their international collaborators to store, share, archive, and analyse their omics-scale data.
    how_to_access: Everyone with funding from a Norwegian funder or a project at one of the health regions or universities can get access through Feide or upon application for collaborators.
    related_pages:
      tool_assembly: [nels, marine_assembly]
    url: https://nels.bioinfo.no
  - name: NIRD
    description: The National Infrastructure for Research Data (NIRD) infrastructure offers storage services, archiving services, and processing capacity for computing on the stored data. It offers services and capacities to any scientific discipline that requires access to advanced, large-scale, or high-end resources for storing, processing, publishing research data or searching digital databases and collections. This service is owned and operated by [Sigma2 NRIS](https://sigma2.no/nris), which is a joint collaboration between UiO, UiB, NTNU, UiT, and [UNINETT Sigma2](https://www.sigma2.no/).
    how_to_access: A formal application is required to gain access to the storage services.
    related_pages:
      your_tasks: [transfer, storage]
      tool_assembly: [nels, fairtracks]
    url: https://documentation.sigma2.no/files_storage/nird.html
  - name: Sigma2 HPC systems
    description: The current Norwegian academic HPC infrastructure consists of three systems for different purposes. The Norwegian academic high-performance computing and storage infrastructure is maintained by [Sigma2 NRIS](https://sigma2.no/nris), which is a joint collaboration between UiO, UiB, NTNU, UiT, and [UNINETT Sigma2 (SIKT)](https://www.sigma2.no/).
    how_to_access: A formal application is required to gain access to the storage services.
    related_pages:
      your_tasks: [data_analysis]
    url: https://documentation.sigma2.no/hpc_machines/hardware_overview.html
  - name: Norwegian Research and Education Cloud (NREC)
    description: NREC is an Infrastructure-as-a-Service (IaaS) project between the University of Bergen and the University of Oslo, with additional contributions from NeIC (Nordic e-Infrastructure Collaboration) and Uninett., commonly referred to as a cloud infrastructure An IaaS is a self-service infrastructure where you spawn standardized servers and storage instantly, as needed, from a given resource quota.
    how_to_access: All users at educational institutions via Feide
    instance_of: openstack
    related_pages:
      your_tasks: [data_analysis, storage]
    url: https://www.nrec.no/
  - name: Educloud Research
    description: Educloud Research is a platform provided by the Centre for Information Technology (USIT) at the University of Oslo (UiO). This platform provides access to a work environment accessible to collaborators from other institutions or countries. This service provides a storage solution and a low-threshold HPC system that offers batch job submission (SLURM) and interactive nodes. Data up to the [red classification  level](https://www.uio.no/english/services/it/security/lsis/data-classes.html#toc4) can be stored/analysed.
    how_to_access: Educloud Research can be ordered by a project at UiO or by external organisations connected to the University/University College sector. 
    related_pages:
      your_tasks: [data_analysis, sensitive, storage]
    url: https://www.uio.no/english/services/it/research/platforms/edu-research/
  - name: TSD
    description: The TSD – Service for Sensitive Data, is a platform for collecting, storing, analysing and sharing sensitive data in compliance with the Norwegian privacy regulation.  TSD is developed and operated by UiO.
    how_to_access: To register a project in TSD you have to attach the ethical approval, to conduct your research, either from REK, NSD, the Norwegian Data Protection Authority or your local Data Protection Officer (DPO). You can access your project through minID-login.
    related_pages:
      your_domain: [human_data]
      your_tasks: [data_analysis, sensitive, storage]
      tool_assembly: [tsd]
    url: https://www.uio.no/english/services/it/research/sensitive-data/
  - name: HUNTCloud
    description: The HUNT Cloud, established in 2013, aims to improve and develop the collection, accessibility and exploration of large-scale information. HUNT Cloud offers cloud services and lab management. It is a key service that has established a framework for data protection, data security, and data management. HUNT Cloud is owned by NTNU and operated by HUNT Research Centre at the Department of Public Health and Nursing at the Faculty of Medicine and Health Sciences.
    how_to_access: Depending on your organisation, data processor agreements may be signed on various organizational levels. For example, your Department will be the internal data controller at NTNU.
    related_pages:
      your_domain: [human_data]
      your_tasks: [data_analysis, sensitive, storage]
    url: https://www.ntnu.edu/mh/huntcloud
  - name: SAFE
    description: SAFE (secure access to research data and e-infrastructure) is  the solution for the secure processing of sensitive personal data in research at the University of Bergen. SAFE is based on the “Norwegian Code of conduct for information security in the health and care sector” (Normen) and ensures confidentiality, integrity, and availability are preserved when processing sensitive personal data. Through SAFE, the IT department offers a service where employees, students and external partners get access to dedicated resources for processing of sensitive personal data.
    how_to_access: Access to SAFE requires a University of Bergen computer account. However, each department has approvers who can create external accounts for partners if needed.
    related_pages:
      your_domain: [human_data]
      your_tasks: [data_analysis, sensitive, storage]
    url: https://www.uib.no/en/it/131011/safe-secure-access-research-data-and-e-infrastructure
  - name: RETTE
    description: System for Risk and compliance. Processing of personal data in research and student projects at UiB.
    how_to_access: Through Feide, only if you are based at the UiB
    related_pages:
      your_domain: [human_data]
      your_tasks: [data_security, gdpr_compliance, sensitive]
      your_role: [policy_maker, data_steward]
    url: https://rette.app.uib.no/
  - name: DataverseNO
    description: DataverseNO is a national, generic repository for open research data. Various Norwegian research institutions have established partner agreements about using DataverseNO as institutional repositories for open research data.
    how_to_access: open access
    instance_of: dataverse
    related_pages:
      your_domain: []
      your_tasks: [data_publication]
      your_role: []
    url: https://dataverse.no/  
  - name: openscience.no
    description: General information about open research, especially open access and guidance for researchers and institutions.
    url: https://www.openscience.no/
  - name: Nettskjema
    description: Nettskjema is a solution for designing and managing data collections using online forms and surveys. It can be used for collecting sensitive data and offers a high degree of security and privacy.
    how_to_access: Feide, TSD, or via ID-porten upon application.
    related_pages:
      your_tasks: [sensitive]
      tool_assembly: [tsd]
    url: https://nettskjema.no/
ref_to_main_resources:
  - mardb
  - marfun

---

<!---Following information for the page text. All fields are optional--->
<!---If the information is already in another resource, please include the link instead of duplicating information--->
<!---Please focus on resources that are relevant for the whole country for life sciences--->

## Introduction

This page provides an overview of the data management resources in Norway. The target audience is the Norwegian scientific community in the life sciences and collaborators.
The [Data Stewardship Wizard instance from ELIXIR Norway](https://elixir-no.ds-wizard.org/knowledge-models/elixir.no:lifesciences-elixir-norway:latest/preview) provides an interactive way to navigate these recommendations and resources. You can also find condensed information in the interlinked [RDM LookUp from ELIXIR Norway](https://elixir.no/rdm-lookup/).

<!---General RDM considerations for your country, how to deal with RDM on a national level--->
The Norwegian Ministry of Education and Research's "[National strategy on access to and sharing of research data](https://www.regjeringen.no/en/dokumenter/national-strategy-on-access-to-and-sharing-of-research-data/id2582412/?ch=1)" from 2018 is an initiative aimed at fostering open, equitable, and efficient sharing of research data in Norway. For researchers in Norway and their international partners, this strategy lays the groundwork for creating a robust, collaborative research environment where data is shared freely but responsibly. The national strategy underscores Norway's commitment to scientific advancement and maintaining ethical and legal standards in a data-driven era.

##  Funder policies on research data

[Norges Forskningsråd (Research Council of Norway)](https://www.forskningsradet.no/en/) is the primary funding body in Norway for research. The [research data management policy of RCN requires a Data Management Plan (DMP)](https://www.forskningsradet.no/en/research-policy-strategy/open-science/research-data/), preferably also available in the [DMP Common Standard](https://www.rd-alliance.org/group/dmp-common-standards-wg/outcomes/rda-dmp-common-standard-machine-actionable-data-management) as supported by for example by {% tool "data-stewardship-wizard" %} after a positive funding decision for each project. A DMP has to be submitted as part of a final report. RCN recommends following the ‘[Practical Guide to the International Alignment of Research Data Management](https://scienceeurope.org/our-resources/practical-guide-to-the-international-alignment-of-research-data-management/)’ by Science Europe, the organisation of research funders and performers. In addition to advising [policies for open science and open access](https://www.forskningsradet.no/siteassets/forskningspolitisk-radgivning/apen-forskning/nfr-policy-open-science-eng.pdf), [RCN provides recommendations on how to make research data available](https://www.forskningsradet.no/siteassets/publikasjoner/2021/how-should-we-share-research-data.v2.pdf). From 2023 and onwards, a [project grant application submitted to RCN is assessed for open science best practices](https://www.forskningsradet.no/en/processing-grant-applications/processing-applications/assessment-open-science/).


##  Institutional policies on research data

We provide here a non-exhaustive list of research institutions with Data Management Policies in Norway:

* [Norwegian University of Life Sciences (NMBU)](https://www.nmbu.no/forskning/forskningsdata)
* [Norwegian University of Science and Technology (NTNU)](https://www.ntnu.edu/policy-for-open-science)
* [University of Bergen (UiB)](https://www.uib.no/en/foremployees/142184/university-bergen-policy-open-science)
* [University of Oslo (UiO)](https://www.uio.no/english/for-employees/support/research/research-data-management/policies-guidelines.html)
* [The Arctic University of Norway (UiT)](https://en.uit.no/regelverk/sentraleregler#innhold_740835)
* [University of Stavanger](https://www.uis.no/en/library/researchdata)
* [University of Agder](https://libguides.uia.no/c.php?g=653927&p=4778251#)
* [Nord University](https://www.nord.no/en/research/researchers/research-data)
* [Inland Norway University of Applied Sciences](https://www.inn.no/english/library/research-support/research-data-management/publish-research-data/)
* [VID Specialized University](https://www.vid.no/en/files/guidelines-for-managing-research-data-at-vid/)
* [Svalbard Integrated Arctic Earth Observing System, SIOS](https://sios-svalbard.org/Documents#docSDMS)

### Institutional storage guidelines

Most universities in Norway classify data into four categories, depending on access requirements. These categories are based on recommendations from [UNIT](https://www.unit.no/klassifisering-av-informasjon-og-informasjonssikkerhet).
* **Open (Green)**: Information can be available to everyone, without special access rights.
* **Restricted (Yellow)**: Information must have some protections if access by unauthorised persons could harm the institution or collaborators in some way. The information can be available both internally and externally with controlled access rights.
* **Confidential (Red)**: Information must have strict access rights if unauthorised access would cause damage to public interests, individuals, the institution, or collaborators.
* **Strictly confidential (Black)**: Information must have the strictest access rights if unauthorised access could cause significant damage (for example, highly confidential research or confidential addresses).

Details and provided solutions vary according to each institution:
* [Norwegian University of Life Sciences (NMBU) - login](https://www.nmbu.no/node/35651)
* [Norwegian University of Science and Technology (NTNU)](https://i.ntnu.no/wiki/-/wiki/English/Data+storage+guide)
* [University of Bergen (UiB)](https://www.uib.no/en/it/153608/storage-guide)
* [University of Oslo (UiO)](https://www.uio.no/english/for-employees/support/research/funding/units/hf/imv/data-ethics/storage-guide.html)
* [The Arctic University of Norway (UiT)](https://en.uit.no/research/research-dataportal/art?p_document_id=729174)
* [VID Specialized University](https://www.vid.no/en/research/research-data/data-storage-guide/)

### Institutional guidelines related to personal data
* [Norwegian University of Life Sciences (NMBU)](https://www.nmbu.no/forskning/forskningsdata)
* [Norwegian University of Science and Technology (NTNU) - Privacy in research guidelines](https://innsida.ntnu.no/wiki/-/wiki/English/Collection+of+personal+data+for+research+projects), also available [in Norwegian](https://i.ntnu.no/wiki/-/wiki/Norsk/Behandle+personopplysninger+i+student-+og+forskningsprosjekt)
* [Norwegian University of Science and Technology - Health research guidelines](https://i.ntnu.no/helseforskning)
* [University of Bergen (UiB)](https://www.uib.no/en/personaldata/130126/privacy-policy-university-bergen), also available [in Norwegian](https://www.uib.no/personvern)
* [University of Oslo (UiO)](https://www.uio.no/english/for-employees/support/privacy-dataprotection/personal-data-in-research.html)
* [The Arctic University of Norway (UiT)](https://en.uit.no/research/ethics/art?p_document_id=754184), [full guidelines](https://uit.no/Content/800249/cache=1673451716000/Guidelines%20for%20processing%20of%20personal%20data%20in%20research%20and%20student%20projects%20at%20UiT.PDF) available as pdf
* [VID Specialized University](https://www.vid.no/en/privacy-and-gdpr/research-and-publishing/)


## Support services

### Helpdesks

The [ELIXIR Norway Helpdesk](https://elixir.no/helpdesk) offers bioinformatics and data management support together with documentation and support for using ELIXIR Norway's life science infrastructures. Researchers in Norway as well as international collaborators—including private companies and governmental research institutions—can contact the Helpdesk to request access to data management services.

The [Global Biodiversity Information Facility (GBIF) Norway Helpdesk](https://www.gbif.no/services/) supplies IT-services and assistance with deposition of biodiversity data to affiliated organizations. If you are not currently part of the GBIF community, you can follow their guidelines to request endorsement. The GBIF network supports four classes of datasets: resources metadata, checklists, occurrences, and sampling-event data.

The [ELSI helpdesk for biobanking](https://bbmri.no/help-desk-elsi) facilitates compliance with Norway-specific regulations and standards for ethical, legal, and societal issues, as part of Biobank Norway (BBMRI-NO).

### Institutional research data teams
* [Norges teknisk-naturvitenskapelige universitet (NTNU)](https://i.ntnu.no/researchdata)
* [University of Bergen (UiB)](https://www.uib.no/en/ub/111372/open-access-research-data)
* [University of Oslo (UiO)](https://www.ub.uio.no/english/courses-events/courses/other/research-data/)
* [The Arctic University of Norway (UiT)](https://en.uit.no/research/research-dataportal)
* [University of Stavanger (UiS)](https://www.uis.no/en/library/researchdata)
* [University of Agder](https://libguides.uia.no/c.php?g=653927&p=4778251#)
* [Nord University](https://www.nord.no/en/research/researchers/research-data)
* [Inland Norway University of Applied Sciences](https://www.inn.no/english/library/research-support/research-data-management/publish-research-data/)
* [VID Specialized University](https://www.vid.no/en/research/research-data/)
* [Svalbard Integrated Arctic Earth Observing System, SIOS](https://sios-svalbard.org/DMsupport)

### Other data management infrastructures

Sikt is a Norwegian governmental agency that provides [(sensitive) personal data protection services](https://sikt.no/en/data-protection-services) to research and education institutions in Norway. Sikt offers guidelines, tools for creating data management plans, and assistance with the legal aspects of personal data management.

NRIS, a collaboration between Sigma2 (a subsidiary of Sikt) and four universities, gives [technical and administrative support](https://www.sigma2.no/user-support) to researchers in Norway on large-scale data storage and high-performance computing.


### Communities for research data management support personnel

There are several RDM communities (with subject or local focus) in Norway to enable exchange and discussion:
 

* [Life-Science RDM Group](https://elixir.no/organization/biomeddata/Life-Science-RDM-Group)
* [RDA Norway](https://www.rd-alliance.org/groups/rda-norway)
* [University of Oslo Data Manager Network](https://www.ub.uio.no/english/libraries/dsc/data-managers-network/)
* [Bergen Research Data Network](mailto:research-data@uib.no?subject=forskningsdata@uib.no)
* [GIDA-Sápmi -Sámi Research Data Governance, members from Norway, Sweden and Finland](https://uit.no/research/sshf-no/project?pid=788403)
* DataverseNO Network of Expertise
* [FAIR Data Forum by Nordic e-Infrastructure Collaboration (NeIC)](https://neic.no/fairdataforum/)
* [Sensitive Data Forum by NeIC](https://neic.no/sensitivedataforum/)




## Data Management Planning
A data management plan (DMP) is currently requested by:
* The research performing institutions 
* RCN upon project funding
* International funding programs (e.g. Horizon Europe, European Research Council)

A DMP typically contains information about data handling during a project and after its completion and makes it possible to identify (and budget for) significant issues to be resolved (e.g. storage). While some of the institutions mentioned above require DMPs to follow a certain standard, this does not apply to all local institutions (e.g. [UiO does not currently enforce any specific template](https://www.uio.no/english/for-employees/support/research/research-data-management/write-a-dmp.html)). There are several tools available for creating a DMP. 

<!-- Some of these tools come from international providers (e.g. DMPonline), some are national services, such as EasyDMP (Sigma2) and sikt’s DMP tool. -->

ELIXIR Norway provides access to a [national instance of the Data Stewardship Wizard (DSW)](elixir-no.ds-wizard.org/), an internationally developed tool that has been adapted to better suit the needs of Norwegian researchers, PIs, and institutions. Both [RCN]((https://www.forskningsradet.no/en/Adviser-research-policy/open-science/open-access-to-research-data/)) and [BOTT (Bergen, Oslo, Trondheim, Tromsø) university libraries](https://zenodo.org/record/7428542) list the DSW as a preferred tool, particularly for life sciences data. DSW provides templates that are compliant with all different funders' regulations and offers machine-actionable DMP exports. To facilitate the adoption of best-practises, the ELIXIR-NO DSW instance also provides a collection of exemplar DMPs. These DMPs are partially pre-filled with domain-specific recommendations and can be used as a starting point for your own projects.


## Life science-specific infrastructures/resources

We have included here both general and topic-specific resources, that help to simplify and streamline data management practices and to protect your research data. These resources can help you increase productivity while ensuring that your research is compliant, transparent, and reproducible.

### Norwegian e-Infrastructure for Life Sciences (NeLS) tool assembly

ELIXIR Norway offers the comprehensive NeLS tool assembly for researchers in Norway and their international collaborators. NeLS serves as a unified resource for planning, processing, analysing, and sharing research data throughout your project's life cycle. You can use the Norwegian instance of the Data Stewardship Wizard to simplify data management planning, including compliance with relevant laws and regulations. NeLS' multi-tiered storage system, accessible via FEIDE and the ELIXIR Authentication and Authorization infrastructure, provides a secure platform for data storage. Integration with platforms like Galaxy and SEEK gives easy access to versatile data management tools. For more information, visit the [Norwegian e-Infrastructure for Life Sciences (NeLS) tool assembly RDMkit page](nels_assembly).

### Federated European Genome-phenome Archive (EGA) Norway node

Established by ELIXIR Norway and hosted by the University of Oslo, the Norwegian Federated EGA node provides a secure, controlled platform for sharing and archiving sensitive personal data. This service prioritises making sensitive data findable, accessible, interoperable, and reusable (FAIR) while fully complying with GDPR and the Norwegian Personal Data Act. You can boost the visibility of your datasets while maintaining control over access permissions with a designated data access committee. Learn more at the [Norwegian node of the European genome-phenome archive for sensitive human (genetic) data](https://ega.elixir.no/).

### Norwegian tools assembly for sensitive personal data

ELIXIR Norway's tools assembly for personally identifiable datasets is based on the University of Oslo's Services for Sensitive Data (TSD). This infrastructure provides resources to help you comply with Norwegian and European regulations regarding sensitive personal data. You can also store, process, and analyse your data in a secure, restricted environment and use a wide range of integrated data management tools. More details are available on the [National Norwegian services for sensitive (personal) data tool assembly RDMkit page](tsd_assembly).

### The Norwegian Covid-19 data portal

The [Norwegian Covid-19 Data Portal](https://covid19dataportal.no/) acts as a specialised hub for collecting, storing, and analysing Covid-19 related research data. You can access research data, tools, and workflows with the assurance of data security and privacy in compliance with national and EU data protection regulations.

### Marine metagenomics portal tool assembly

The Norwegian marine metagenomics portal tool assembly offers comprehensive resources for researchers and students. While the data storage tools through NeLS are primarily for users in Norway, the data analysis tools and repositories are globally accessible. The Marine Metagenomics Portal (MMP) is a rich collection of high-quality, curated microbial genomics and metagenomics resources. The toolkit is described in detail on the [Marine metagenomics Portal tool assembly RDMkit page](marine_metagenomics_assembly).

## Ethical committees and general authorities
We provide here a list of ethics committees and guidelines, relevant to life sciences data, that are responsible for national regulations in Norway:
### Data privacy
* [Norwegian Data Protection Authority](https://www.datatilsynet.no/)

### Health research

* [Regional Ethic committees (for health research)](https://rekportalen.no/#hjem/home)
* Medical devices, medicines, dietary supplements,natural substances or other substances: [Norwegian Medicine Agency](https://legemiddelverket.no)

### General Research Ethics Committees
* [Norwegian National Research Ethics Committees](https://www.forskningsetikk.no/en/)


## Relevant ethical guidelines

* [General guidelines for research ethics](https://www.forskningsetikk.no/en/guidelines/general-guidelines/)
* [Guidelines for Research Ethics in Science and Technology](https://www.forskningsetikk.no/en/guidelines/science-and-technology/guidelines-for-research-ethics-in-science-and-technology/)
* [Guidelines for research ethical and scientifically assessment of qualitative research projects](https://www.forskningsetikk.no/retningslinjer/med-helse/vurdering-av-kvalitative-forskningsprosjekt-innen-medisin-og-helsefag/)
* [Guidelines for Internet Research Ethics](https://www.forskningsetikk.no/retningslinjer/hum-sam/forskningsetisk-veileder-for-internettforskning/)
* [Guidelines for the use of genetic studies of humans](https://www.forskningsetikk.no/retningslinjer/med-helse/retningslinjer-for-bruk-av-genetiske-undersokelser-av-mennesker-i-medisinsk-og-helsefaglig-forskning/)
* [Payment to participants in medical or health research](https://www.forskningsetikk.no/retningslinjer/med-helse/betaling-til-deltakere-i-medisinsk-eller-helsefaglig-forskning/)
* [Guidelines for the inclusion of women](https://www.forskningsetikk.no/retningslinjer/med-helse/inklusjon-av-kvinner/)
* [Ethical guidelines for clinical trial of drugs](https://www.forskningsetikk.no/ressurser/publikasjoner/kliniske-utprovinger-av-legemidler/)
* [Guidelines for the inclusion of adults with impaired or absent capacity to consent](https://www.forskningsetikk.no/retningslinjer/med-helse/inklusjon-av-voksne-personer-med-manglende-eller-redusert-samtykkekompetanse/)
* [Guidelines for research ethical and scientifically assessment of qualitative research projects](https://www.forskningsetikk.no/retningslinjer/med-helse/vurdering-av-kvalitative-forskningsprosjekt-innen-medisin-og-helsefag/)

Through the Research Ethics Committees, the following recommendations were made binding in Norway and it is therefore advised to take them into consideration for data ethics:
* [The Vancouver Recommendations](https://www.forskningsetikk.no/en/resources/the-research-ethics-library/legal-statutes-and-guidelines/the-vancouver-recommendations/)
* [Declaration of Helsinki](https://www.forskningsetikk.no/en/guidelines/medical-and-health-research/declaration-of-helsinki/)
* [The Oviedo Convention](https://www.forskningsetikk.no/en/resources/the-research-ethics-library/legal-statutes-and-guidelines/oviedo-convention/)


## Laws and regulations relevant to life sciences research data

These are some of the laws relevant for research data management in Norway. You should refer to the relevant laws and ethical guidelines in your DMP (e.g. in [Norway's instance of the Data Stewardship Wizard (DSW)](https://elixir-no.ds-wizard.org/knowledge-models/elixir.no:lifesciences-elixir-norway:latest/preview?questionUuid=4ed4aadb-6ee8-40c3-8e31-c9f9039a5b1e)). Some of the legal information is only accessible after login with Feide.

### Data privacy
* [Personal Data Act](https://lovdata.no/dokument/RFA/lov/2000-04-14-31)
* Regulations on the processing of personal data [Forskrift om behandling av personopplysninger](https://lovdata.no/dokument/SF/forskrift/2018-06-15-876)
* Transitional rules on the processing of personal data [Overgangsregler om behandling av personopplysninger](https://lovdata.no/dokument/SF/forskrift/2018-06-15-877)
* [The Norwegian Data Protection Agency: Journalistic, academic, artistic and literary purposes](https://www.datatilsynet.no/regelverk-og-verktoy/lover-og-regler/personvern-vs.-ytringsfrihet/)
* [The Norwegian Data Protection Agency: Code of Conduct on Information Security and Internal Control](https://www.datatilsynet.no/regelverk-og-verktoy/atferdsnorm/)

### Health research data

* [Health Research Act](https://lovdata.no/dokument/LTI/lov/2008-06-20-44)
* [Regulations on the organization of medical and health research](http://www.lovdata.no/for/sf/ho/ho-20090701-0955.html)
* [Comments to health research legislative work by the Norwegian government](http://www.regjeringen.no/nb/dep/hod/dok/lover_regler/forskrifter/2009/helseforskningsloven.html?id=570542)
* [Health Register Act](https://lovdata.no/dokument/NL/lov/2014-06-20-43)
* [Regulations on population-based health surveys](https://lovdata.no/dokument/SF/forskrift/2018-04-27-645)
* [Health Personnel Act](http://www.lovdata.no/all/nl-19990702-064.html)
* [Patient and User Rights Act](http://www.lovdata.no/all/nl-19990702-063.html)
* [Medicines Act](http://www.lovdata.no/all/nl-19921204-132.html)
* [Regulations on clinical trials of medical products for human use](http://www.lovdata.no/for/sf/ho/ho-20091030-1321.html)
* [Biotechnology Act (on the medical use of biotechnology)](https://lovdata.no/dokument/NL/lov/2003-12-05-100)
* [e-helse Direktoratet: “Normen”: Norms for health data](https://ehelse.no/normen)

### Other laws of potential relevance to life sciences research data

* [Archive Act](https://lovdata.no/dokument/NL/lov/1992-12-04-126)
* [Research Ethics Act](https://lovdata.no/dokument/NL/lov/2017-04-28-23)
* [Patent Act](https://lovdata.no/dokument/NL/lov/1967-12-15-9)
* [Copyright Act](https://lovdata.no/dokument/NL/lov/2018-06-15-40)
* [Act on Universities and Colleges Act](https://lovdata.no/dokument/NL/lov/2005-04-01-15)
* [National Security Act](https://lovdata.no/dokument/NL/lov/2018-06-01-24)
* [Genetic Engineering Act](https://lovdata.no/dokument/NL/lov/1993-04-02-38)
* [Biodiversity Act](https://lovdata.no/dokument/NL/lov/2009-06-19-100)
* [Regulations on the protection of traditional knowledge related to genetic material](https://lovdata.no/dokument/SF/forskrift/2016-11-25-1367)
* [Norwegian Environment Agency: Guidelines on sensitive species data](https://sensitive-artsdata.miljodirektoratet.no/Contentpages/Forsiden.aspx)
