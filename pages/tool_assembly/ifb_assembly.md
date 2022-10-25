---
title: IFB
contributors: [Olivier Collin, Marie-Christine Jacquemot, Paulette Lieby, Flora D'Anna]
description: The French Bioinformatics Institute (IFB) offers IT infrastructure and bioinformatics expertise to support researchers in Life Sciences.
page_id: IFB
affiliations: ["ELIXIR Europe", "FR"]
related_pages: 
  your_tasks: [DMP, data organisation ,storage, data publication, data transfer, metadata, data analysis]
  your_domain: []
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=IFB
  - name: Data management training at the IFB
    url: https://www.france-bioinformatique.fr/en/training/
  - name: Inist and the network of regional scientific information units (Urfist)
    url: https://doranum.fr
  - name: Documentation for the IFB core cluster
    url: https://ifb-elixirfr.gitlab.io/cluster/doc/
  - name: Documentation for the Biosphere cloud federation
    url: https://ifb-elixirfr.github.io/biosphere/
---

## What is the IFB data management tool assembly?

The [IFB](https://www.france-bioinformatique.fr) is the French national Bioinformatics Infrastructure that supports research projects in Life Sciences by provisioning a bioinformatics environment, which consists of IT infrastructure (such as storage and computing resources), software and training, distributed across the country. 
The IFB federates 20 bioinformatics platforms which make physical, operational and human resources available to researchers in a synergistic and efficient way. Each platform brings its own IT infrastructure and bioinformatics expertise to create a better support network, distributed over the country, for Life Sciences research activities. IFB supports scientists since the beginning of a project and relies on the OPIDoR tool to write a data management plan. 


## Who can use the IFB data management tool assembly?

IFB and the underlying infrastructure are accessible to researchers in France and their foreign collaborators. Researchers that would like to know more about IFB services can find specific contact details at the unified [IFB help desk page](https://www.france-bioinformatique.fr/en/help-desk/) and get support through the dedicated help pages. Depending on the resources, fees may apply. It is therefore advisable to contact them during the planning phase of the project.

The way you can access the IFB depends on the type of resources (for instance, cluster or cloud), and there will be different authentication procedures (local, national or international). For example, the Biosphere cloud federation uses the EduGAIN federation for authentication, while useGalaxy.fr uses the [ELIXIR AAI](https://elixir-europe.org/services/compute/aai) authentication. To have additional information on how to access the IFB contact the [help desk](https://www.france-bioinformatique.fr/en/help-desk/). 


## For what can you use the IFB data management tool assembly?

{% include image.html file="fr_ifb_assembly.svg" caption="Figure 1. The French Bioinformatics Institute (IFB) tool assembly." alt="IFB RDMkit" %}

### Data management planning

IFB relies on [Inist](https://www.inist.fr) infrastructure for the [planning](planning) phase of the data life cycle and recommends [DMP-OPIDoR](https://dmp.opidor.fr) as a tool for writing a Data Management Plan (DMP).

DMP-OPIDoR is hosted and maintained at Inist-CNRS, it is based on DMPRoadmad, but it is tailored to meet the needs of the many French research institutes. You will find 37 DMP templates, in French and/or English, created by funders and research institutes. It is a collaborative tool and as such enables sharing of DMPs amongst partners and also experts or services. A dedicated team offers training and support for DMP templates and DMPs. They can be reached [via this contact form](https://dmp.opidor.fr/contact-us).

A new machine actionable version of DMP-OPIDoR will allow the production of structured standardized DMP content. It will enable the integration of information from funding agencies such as the French National Agency (ANR), and also integration and interactions with computing infrastructures provided by IFB and Genci, the organization in charge of the three supercomputing centres in France. 

DMP OPIDoR is freely accessible to anyone. First, one has to [create an account](https://dmp.opidor.fr/#create-account-form) (login, password). Then this account can be linked to the [Renater identity federation](https://www.renater.fr).
For support about OPIDoR, you can check the [cat-OPIDoR support providers page](https://cat.opidor.fr/index.php/Accompagnement).


### Data collection

Although they are not part of IFB, other infrastructures in France can also help you generate new data. Specifically, some facilities can assist you with in vivo and in vitro experiments, synthetic biology, omics techniques, imaging, structural biology and other techniques and expertise. To find the adequate facility you may use the [Ministry search engine](https://data.enseignementsup-recherche.gouv.fr/pages/feuille_de_route_2018/?sort=acronyme) or the [IBiSA directory](https://www.ibisa.net/trouver-plateforme/) of french facilities in Life Sciences. 

Once your data have been generated by the facility, you will need to [transfer](data_transfer) it to your local system or to the IFB infrastructure, if you intend to use the IFB’s compute services. In both cases it is a good practice to get in touch with IT support (local or IFB), especially if the volume of your data is large. 

If you have to reuse previously generated data, keep in mind that the different IFB platforms provide many specialized databases. A list of the databases is available [here](https://ressources.france-bioinformatique.fr/en/services/data). These databases are, for the most, freely available. 



### Data processing and analysis 

IFB infrastructure gives you access to several flavours of computing resources, according to your needs and expertise:

* Several clusters hosted either at IFB-Core or on any of the member platforms. You can [request accounts](https://www.france-bioinformatique.fr/en/ifb-clusters/) on any of the member clusters. 
* The [Galaxy France](https://usegalaxy.fr) portal operated by the IFB or any of the local instances operated by IFB bioinformatics facilities. 
* The cloud federation [Biosphere](https://biosphere.france-bioinformatique.fr) allows the deployment of ready-to-use appliances (virtual machines with all required software installed for analysis) for several scientific domains (Genomics, Bioimaging, Metabolomics, etc.). A list of the different appliances is available on the [RainBio catalogue](https://biosphere.france-bioinformatique.fr/catalogue/). You can log in [here](https://biosphere.france-bioinformatique.fr/cloudweb/login/?next=/) using your academic credentials. 

Each of the computing resources offers its own storage solution tailored for the needs of the users (fast access, capacitive). You may have to choose a resource according to what its service offers and also according to its proximity to your own location in order to benefit from better support and also better data transfer speed.

IFB infrastructure can also help you with bioinformatics analysis of your data. Many of the IFB member platforms can provide expertise for data analysis in many domains (genomics, metagenomics, transcriptomics) as well as software development. To check the expertise of the platforms, you can use this [catalog](https://ressources.france-bioinformatique.fr/en/expertise). A list of the tools developed by all IFB members is available [here](https://ressources.france-bioinformatique.fr/en/services/tools). 

### Data sharing and publishing

It is good practice to [publish](data_publication) your data on repositories. IFB encourages researchers to browse the list of [ELIXIR deposition databases for biomolecular data](https://elixir-europe.org/platforms/data/elixir-deposition-databases) to find the appropriate repository. 

If you are a member of INRAE (one of the stakeholders of IFB infrastructure), you can access the institutional instance of the Dataverse platform [Data INRAE](https://data.inrae.fr). Data INRAE can be used by researchers to store and describe datasets during the project, and to share them according to specific sharing settings. 

You can also browse [cat-OPIDoR](https://cat.opidor.fr/index.php/Cat_OPIDoR,_wiki_des_services_dédiés_aux_données_de_la_recherche) for an overview of the different services related to data management provided by IFB infrastructure and its stakeholders in France.

### Compliance monitoring & measurement

IFB infrastructure promotes the implementation of the FAIR principles. To this end, IFB provides and encourages the use of the [FAIR-Checker](https://github.com/IFB-ElixirFr/fair-checker), a web interface aimed at monitoring the level of FAIRification of resources. This tool uses the FAIRMetrics APIs to provide a global assessment and recommendations. It also uses semantic technologies to help users in annotating their resources with high-quality metadata.

