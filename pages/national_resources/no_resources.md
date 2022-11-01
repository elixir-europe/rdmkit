---

title: Norway
country_code: "NO"
contributors: [Nazeefa Fatima,Federico Bianchini,Korbinian Bösl]
coordinators: [Korbinian Bösl]

related_pages:
  tool_assembly: [TSD,NeLS,marine assembly]

training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/events?include_expired=true&node=Norway
  - name: ELIXIR Norway community in Zenodo
    registry: Zenodo
    url: https://zenodo.org/communities/elixir-no/?page=1&size=20
#  - name: ELIXIR Norway YouTube
#    registry: Youtube
#    url: https://www.youtube.com/channel/UCva4S9uWxXqyGnbSgxIbcwA


national_resources:
  - name: Feide
    description: Feide is the national solution for secure login and data exchange in education and research. Feide can be linked with [ELIXIR-AAI](https://elixir-europe.org/services/compute/aai) through [eduGAIN](https://edugain.org/).
    how_to_access: Everyone with an affiliation to a Norwegian academic institution.
    related_pages:
      tool_assembly: [TSD, NELS,marine assembly]
    url: https://www.feide.no/
  - name: DS-Wizard ELIXIR-Norway
    description: DS-Wizard is a tool to aid the creation, organisaton and sharing of data management plans. It provides scientists with guidance, facilitating the understanding of the key components of FAIR-oriented Data Stewardship. The template in this instance provides additional guidance on resources, laws and regulations in Norway.
    how_to_access: ELIXIR-AAI with Feide or upon registration
    instance_of: Data Stewardship Wizard
    related_pages:
      tool_assembly: [TSD,NeLS,marine assembly]
      your_tasks: [DMP]
    url: https://elixir-no.ds-wizard.org/
  - name: EasyDMP
    description: DMP tool from [UNINETT Sigma2 (SIKT)](https://www.sigma2.no/)
    instance_of: EasyDMP
    how_to_access: Feide
    related_pages:
      your_tasks: [DMP]
    url: https://easydmp.no/
  - name: Meta-pipe
    description: META-pipe is a pipeline for annotation and analysis of marine metagenomics samples, which provides insight into phylogenetic diversity, metabolic and functional potential of environmental communities.
    how_to_access: Feide or upon application
    related_pages:
      your_tasks: [data analysis]
      tool_assembly: [marine assembly]
    url:  https://mmp2.sfb.uit.no/metapipe/
  - name: Norwegian COVID-19 Data Portal
    description: The Norwegian COVID-19 Data Portal aims to bundle the Norwegian research efforts and offers guidelines, tools, databases and services to support Norwegian COVID-19 researchers.
    related_pages:
      your_domain: [human data]
      your_tasks: [sensitive, existing data, data publication]
      tool_assembly: [covid-19 data portal]
    url: https://covid19dataportal.no/
  - name: Norwegian Federated EGA
    description: Federated instance collects metadata of -omics data collections stored in national or regional archives and makes them available for search through the main EGA portal. With this solution, sensitive data will not physically leave the country, but will reside on TSD.
    how_to_access: ELIXIR-AAI; intended for data from Norwegian institutions
    instance_of: The European Genome-phenome Archive (EGA)
    related_pages:
      your_domain: [human data]
      your_tasks: [sensitive, existing data, data publication]
      tool_assembly: [TSD]
    url: https://ega.elixir.no/
  - name: usegalaxy.no
    description: Galaxy is an open source, web-based platform for data intensive biomedical research. This instance of Galaxy is coupled with NeLS for easy data transfer.
    instance_of: Galaxy
    how_to_access: Feide or upon application
    related_pages:
      your_tasks: [data analysis, sensitive, existing data, data publication]
      tool_assembly: [NeLS]
    url: https://usegalaxy.no
  - name: NeLS
    description: Norwegian e-Infrastructure for Life Sciences enables Norwegian life scientists and their international collaborators to store, share, archive, and analyse their omics-scale data
    how_to_access: Everyone with funding from a Norwegian funder or a project at one of the health regions or universities can get access through Feide or upon application for collaborators.
    related_pages:
      tool_assembly: [NeLS,marine assembly]
    url: https://nels.bioinfo.no
  - name: NIRD
    description: The National Infrastructure for Research Data (NIRD) infrastructure offers storage services, archiving services, and processing capacity for computing on the stored data. It offers services and capacities to any scientific discipline that requires access to advanced, large-scale, or high-end resources for storing, processing, publishing research data or searching digital databases and collections. This service is owned and operatedby [Sigma2 NRIS](https://sigma2.no/nris), which is a joint collaboration between UiO, UiB, NTNU, UiT, and [UNINETT Sigma2](https://www.sigma2.no/)
    how_to_access: A formal application is required to gain access to the storage services.
    related_pages:
      your_tasks: [transfer, storage]
      tool_assembly: [NeLS]
    url: https://documentation.sigma2.no/files_storage/nird.html
  - name: Sigma2 HPC systems
    description: The current Norwegian academic HPC infrastructure consists of three systems for different purposes. The Norwegian academic high-performance computing and storage infrastructure is maintained by [Sigma2 NRIS](https://sigma2.no/nris), which is a joint collaboration between UiO, UiB, NTNU, UiT, and [UNINETT Sigma2 (SIKT)](https://www.sigma2.no/).
    how_to_access: A formal application is required to gain access to the storage services.
    related_pages:
      your_tasks: [data analysis]
    url: https://documentation.sigma2.no/hpc_machines/hardware_overview.html
  - name: Norwegian Research and Education Cloud (NREC)
    description: NREC is an Infrastructure-as-a-Service (IaaS) project between the University of Bergen and the University of Oslo, with additional contributions from NeIC (Nordic e-Infrastructure Collaboration) and Uninett., commonly referred to as a cloud infrastructure An IaaS is a self-service infrastructure where you spawn standardized servers and storage instantly, as needed, from a given resource quota.
    how_to_access: All users at educational institutions via Feide
    instance_of: OpenStack
    related_pages:
      your_tasks: [data analysis,storage]
    url: https://www.nrec.no/
  - name: Educloud Research
    description: Educloud Research is a platform provided by the Centre for information Technology (USIT) at the University of Oslo (UiO). This platform provides access to a work environment accessible to collaborators from other institutions or countries. This service provides a storage solution and a low threshold HPC system that offers batch job submission (SLURM) and interactive nodes. Data up to the [red classification  level](https://www.uio.no/english/services/it/security/lsis/data-classes.html#toc4) can be stored/analysed.
    how_to_access: Educloud Research can be ordered by a project at UiO or by external organisations connected to the University/University College sector. 
    related_pages:
      your_tasks: [data analysis, sensitive, storage]
    url: https://www.uio.no/english/services/it/research/platforms/edu-research/
  - name: TSD
    description: The TSD – Service for Sensitive Data, is a platform for collecting, storing, analysing and sharing sensitive data in compliance with the Norwegian privacy regulation.  TSD is developed and operated by UiO.
    how_to_access: To register a project in TSD you have to attach the ethical approval, to conduct your research, either from REK, NSD, the Norwegian Data Protection Authority or your local Data Protection Officer (DPO). You can access your project through minID-login.
    related_pages:
      your_domain: [human data]
      your_tasks: [data analysis, sensitive, storage]
      tool_assembly: [TSD]
    url: https://www.uio.no/english/services/it/research/sensitive-data/
  - name: HUNTCloud
    description: The HUNT Cloud, established in 2013, aims to improve and develop the collection, accessibility and exploration of large scale information. HUNT Cloud offers cloud services, lab management, and is a key service that has established a framework for data protection, data security, and data management. HUNT Cloud is owned by NTNU and operated by HUNT Research Centre at the Department of Public Health and Nursing at the Faculty of Medicine and Health Sciences.
    how_to_access: Depending on your organisation, data processor agreements may be signed on various organizational levels. For example, your Department will be the internal data controller at NTNU.
    related_pages:
      your_domain: [human data]
      your_tasks: [data analysis, sensitive, storage]
    url: https://www.ntnu.edu/mh/huntcloud
  - name: SAFE
    description: SAFE (secure access to research data and e-infrastructure) is  solution for secure processing of sensitive personal data in research at the University of Bergen. SAFE is based on “Norwegian Code of conduct for information security in the health and care sector” (Normen) and ensures confidentiality, integrity, and availability are preserved when processing sensitive personal data. Through SAFE, the IT-department offers a service where employees, students and external partners get access to dedicated resources for processing of sensitive personal data.
    how_to_access: Access to SAFE requires a University of Bergen computer account. However, each department have approvers who can create external accounts for partners if needed.
    related_pages:
      your_domain: [human data]
      your_tasks: [data analysis, sensitive, storage]
    url: https://www.uib.no/en/it/131011/safe-secure-access-research-data-and-e-infrastructure
  - name: RETTE
    description: System for Risk and compliance. Processing of personal data in research and student projects at UiB.
    how_to_access: Through Feide, only if you are based at the UiB
    related_pages:
      your_domain: [human data]
      your_tasks: [data protection, sensitive]
      your_role: [policy officer, data manager]
    url: https://rette.app.uib.no/
  - name: DataverseNO
    description: DataverseNO is a national, generic repository for open research data. Various Norwegian research institutions have established a partner agreements about using DataverseNO as institutional repositories for open research data.
    how_to_access: open access
    instance_of: DATAVERSE
    related_pages:
      your_domain: []
      your_tasks: [data publication]
      your_role: []
    url: https://dataverse.no/  
  - name: openscience.no
    description: general information about open research, especially open access and guidance for researchers and institutions
    url: https://www.openscience.no/
    
ref_to_main_resources:
  - MarDB
  - MarFun

---

<!---Following information for the page text. All fields are optional--->
<!---If the information is already in another resource, please include the link instead of duplicating information--->
<!---Please focus on resources that are relevant for the whole country for life sciences--->

## Introduction

This page provides an overview of the data management resources in Norway. The target audience is the Norwegian scientific community in the life sciences and collaborators.
The [Data Stewardship Wizard instance from ELIXIR-Norway](https://elixir-no.ds-wizard.org/knowledge-models/elixir.no:lifesciences-elixir-norway:latest/preview) provides an interactive way to navigate this recommendations and resources.

<!---General RDM considerations for your country, how to deal with RDM on a national level--->
The Norwegian government has released a
[National strategy on access to and sharing of research data](https://www.regjeringen.no/en/dokumenter/national-strategy-on-access-to-and-sharing-of-research-data/id2582412/?ch=1) in 2018.

##  Funder policies on research data

List of funders with Data Management Policies in Norway:

* [Norges Forskningsråd (Research Council of Norway)](https://www.forskningsradet.no/en/) is the primary funding body in Norway for research. The research data management  [policy](https://www.forskningsradet.no/contentassets/e4cd6d2c23cf49d4989bb10c5eea087a/the-research-council-of-norways-policy-for-open-access-to-research-data.pdf) of RCN requires a Data Management Plan (DMP) after a positive funding decision for each project and which also has to be submitted as part of the final report. RCN  recommends to follow the  ‘[Practical Guide to the International Alignment of Research Data Management](https://scienceeurope.org/our-resources/practical-guide-to-the-international-alignment-of-research-data-management/)’ by Science Europe, the organisation of research funders and  performers.  In addition to policies for open science and open access to publications, [RCN provides recommendations on how to make data research available](https://www.forskningsradet.no/siteassets/publikasjoner/2021/how-should-we-share-research-data.v2.pdf). 


##  Institutional policies on research data

We provide here a non-exhaustive list of research institutions with Data Management Policies in Norway:

* [Norwegian University of Life Sciences (NMBU)](https://www.nmbu.no/en/research/for_researchers/researchdata/node/34680)
* [Norwegian University of Science and Technology (NTNU)](https://www.ntnu.edu/policy-for-open-science)
* [University of Bergen (UiB)](https://www.uib.no/en/foremployees/142184/university-bergen-policy-open-science)
* [University of Oslo (UiO)](https://www.uio.no/english/for-employees/support/research/research-data-management/policies-and-guidelines/index.html)
* [The Arctic University of Norway (UiT)](https://en.uit.no/regelverk/sentraleregler#innhold_740835)
* [University of Stavanger](https://www.uis.no/en/library/researchdata)
* [University of Agder](https://libguides.uia.no/c.php?g=653927&p=4778251#)
* [Nord University](https://www.nord.no/en/library/research-data)
* [Inland Norway University of Applied Sciences](https://www.inn.no/english/library/research-support/research-data-management/publish-research-data/)
* [SIOS Svalbard](https://sios-svalbard.org/Documents#docSDMS)

### Institutional storage guidelines

Most universities in Norway classify data into four categories, depending on access requirements:
* Open (Green)
* Restricted (Yellow)
* Confidential (Red)
* Strictly confidential (Black)

Details and provided solutions vary according to each institution. They are based on the recommendations from [UNIT](https://www.unit.no/klassifisering-av-informasjon-og-informasjonssikkerhet).

* [Norwegian University of Life Sciences (NMBU)](https://www.nmbu.no/en/research/for_researchers/researchdata/node/38755)
* [Norwegian University of Science and Technology (NTNU)](https://i.ntnu.no/wiki/-/wiki/English/Data+storage+guide)
* [University of Bergen (UiB)](https://www.uib.no/en/it/153608/storage-guide)
* [University of Oslo (UiO)](https://www.uio.no/english/for-employees/support/research/funding/units/hf/imv/data-ethics/storage-guide.html)
* [The Arctic University of Norway (UiT)](https://en.uit.no/research/research-dataportal/art?p_document_id=729174)

### Institutional guidelines related to personal data
* [Norwegian University of Life Sciences (NMBU)](https://www.nmbu.no/en/research/for_researchers/researchdata/node/34780)
* [Norwegian University of Science and Technology - Privacy in research guidelines (NTNU)](https://innsida.ntnu.no/wiki/-/wiki/English/Collection+of+personal+data+for+research+projects),
* [Norwegian University of Science and Technology - Health research guidelines](https://innsida.ntnu.no/helseforskning)
* [University of Bergen (UiB)](https://www.uib.no/personvern)
* [University of Oslo (UiO)](https://www.uio.no/english/for-employees/support/privacy-dataprotection/personal-data-in-research.html)
* [The Arctic University of Norway (UiT)](https://uit.no/Content/755221/cache=1637158889000/Retningslinjer+for+behandling+av+personopplysningar+i+forskings-+og+studentprosjekt+ved+UiT+%28oppdatert+300921%29.pdf)

## Support services

There are several support services available to Norwegian Life Science researchers, including:
* [ELIXIR Norway Helpdesk](https://elixir.no/helpdesk)
* [GBIF Norway Helpdesk for deposition of biodiversity data](https://www.gbif.no/services/)
* [ELSI Helpdesk for biobanking from BBMRI-NO](https://bbmri.no/help-desk-elsi)
* [NSD (SIKT) on (sensitive) personal data in research](https://www.nsd.no/en/data-protection-services)
* Institutional Research Data teams
    * [Norges teknisk-naturvitenskapelige universitet (NTNU)](https://i.ntnu.no/researchdata)
    * [University of Bergen (UiB)](https://www.uib.no/en/ub/111372/open-access-research-data)
    * [University of Oslo (UiO)](https://www.ub.uio.no/english/courses-events/courses/other/research-data/)
    * [The Arctic University of Norway (UiT)](https://uit.no/forskning/forskningsdata)
    * [University of Stavanger (UiS)](https://www.uis.no/en/library/researchdata)
    * [University of Agder](https://libguides.uia.no/c.php?g=653927&p=4778251#)
    * [Nord University](https://www.nord.no/en/library/research-data)
    * [Inland Norway University of Applied Sciences](https://www.inn.no/english/library/research-support/research-data-management/publish-research-data/)
    * [SIOS Svalbard](https://sios-svalbard.org/Documents#docSDMS)

* [NRIS technical and administrative support](https://www.sigma2.no/user-support)

## Data Management Planning
A data management plan (DMP) is currently requested by
* The research performing institutions 
* RCN upon project funding
* International funding programs (e.g. Horizon Europe, European Research Council)

A DMP typically contains information about data handling during a project and after its completion and makes it possible to identify (and budget for) significant issues to be resolved (e.g. storage). While some of the institutions mentioned above require DMPs to follow a certain standard, this does not apply to all local institutions (e.g. [UiO does not currently enforce any specific template](https://www.uio.no/english/for-employees/support/research/research-data-management-old/data-management-plan/)). There are several tools available for creating a DMP. 

<!-- Some of these tools come from international providers (e.g. DMPonline), some are national services, such as EasyDMP (Sigma2) and sikt’s DMP tool. -->

ELIXIR Norway provides access to a [national instance of the Data Stewardship Wizard (DSW)](elixir-no.ds-wizard.org/). This is an internationally developed tool which has been adapted to better suit the needs of Norwegian researchers, PIs and institutions. DSW provides templates which are compliant  with all different funder regulations, is [recommened by RCN](https://www.forskningsradet.no/en/Adviser-research-policy/open-science/open-access-to-research-data/) and offers machine-actionable DMP exports in addition. To facilitate the adoption of best-practises, the ELIXIR-NO DSW instance also provides a collection of exemplar DMPs. These DMPs contain partially prefilled with domain-specific recommendations amd can be used as  a starting point for own projects.


## Life science-specific infrastructures/resources

The following resources and tools are relevant to the implemention of data management practices in your specific research area/topic:

* [Norwegian e-Infrastructure for Life Sciences (NeLS) - Tool Assembly RDMkit Page](nels_assembly)
* [Norwegian node of the European genome-phenome archive for sensitive human (genetic) data](https://ega.elixir.no/)
* [National Norwegian services for sensitive (personal) data - Tool Assembly RDMkit Page](tsd_assembly)
* [The Norwegian Covid-19 Data Portal](https://covid19dataportal.no/)
* [Marine metagenomics Portal - Tool Assembly RDMkit Page](marine_metagenomics_assembly)


## Ethical committees and general authorities
We provide here a list of ethical committees and guidelines, relevant to life sciences data, that are responsible for national regulations in Norway:
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

Through the Research Ethics Committees, the  following recommendations were made binding in Norway and it is therefore advised to take them into consideration for data ethics:
* [The Vancouver Recommendations](https://www.forskningsetikk.no/en/resources/the-research-ethics-library/legal-statutes-and-guidelines/the-vancouver-recommendations/)
* [Declaration of Helsinki](https://www.forskningsetikk.no/en/guidelines/medical-and-health-research/declaration-of-helsinki/)
* [The Oviedo Convention](https://www.forskningsetikk.no/en/resources/the-research-ethics-library/legal-statutes-and-guidelines/oviedo-convention/)


## Laws and regulations relevant to life sciences research data

These are some of the laws relevant for research data management in Norway. You should refer to the relevant laws and ethical guidelines in your DMP (in [DSW NO](https://elixir-no.ds-wizard.org/knowledge-models/elixir.no:lifesciences-elixir-norway:latest/preview?questionUuid=4ed4aadb-6ee8-40c3-8e31-c9f9039a5b1e)). Some of the legal information is only accessible after login with Feide.

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
