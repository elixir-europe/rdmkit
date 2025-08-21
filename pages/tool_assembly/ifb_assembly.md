---
title: IFB
contributors: [Olivier Collin, Marie-Christine Jacquemot, Paulette Lieby, Flora D'Anna, Anne-Françoise Adam-Blondon]
description: The French Bioinformatics Institute (IFB) offers IT infrastructure and bioinformatics expertise to support researchers in Life Sciences.
page_id: ifb
affiliations: ["ELIXIR Europe", "FR"]
related_pages: 
  Your_tasks: [dmp, data_organisation, storage, data_publication, data_transfer, metadata, data_analysis]
  Your_domain: []
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
The IFB federates around 20 bioinformatics platforms which make physical, operational and human resources available to researchers in a synergistic and efficient way. Each platform brings its own IT infrastructure and bioinformatics expertise to create a better support network, distributed over the country, for Life Sciences research activities. 

IFB data management tool assembly supports data management activities of scientists during all the phases of their projects, from planning to publication. 


## Who can use the IFB data management tool assembly?

IFB and the underlying infrastructure are accessible to researchers in France and their foreign collaborators. Researchers that would like to know more about IFB services can find specific contact details at the unified [IFB help desk page](https://www.france-bioinformatique.fr/en/help-desk/) and get support through the dedicated help pages. Depending on the resources, fees may apply. It is therefore advisable to contact them during the planning phase of the project.

The way you can access the IFB depends on the type of resources (for instance, cluster or cloud), and there will be different authentication procedures (local, national or international). For example, the Biosphere cloud federation uses the EduGAIN federation for authentication, while useGalaxy.fr uses the {% tool "life-science-login" %} authentication. To have additional information on how to access the IFB contact the [help desk](https://www.france-bioinformatique.fr/en/help-desk/). 


## For what can you use the IFB data management tool assembly?

{% include image.html file="fr_ifb_assembly.svg" caption="Figure 1. The French Bioinformatics Institute (IFB) tool assembly." alt="IFB RDMkit" %}

### Data management planning

IFB recommends [DMP-OPIDoR](https://dmp.opidor.fr) or [DSW](https://dsw.france-bioinformatique.fr) as tools for writing a Data Management Plan (DMP).

- DMP-OPIDoR is hosted and maintained at Inist-CNRS and is tailored to meet the needs of many French academic institutes. You will find many DMP templates, in French and/or English, created by funders and academic institutes. A dedicated team offers training and support for DMP templates and DMPs. They can be reached [via this contact form](https://dmp.opidor.fr/contact-us).
The machine actionable version of DMP-OPIDoR allows the production of structured standardized DMP content. It enables the integration of information from funding agencies such as the French National Agency (ANR), and also integration and interactions with computing infrastructures provided by IFB and Genci, the organization in charge of the three supercomputing centres in France. 
DMP OPIDoR is freely accessible to anyone. First, one has to [create an account](https://dmp.opidor.fr/#create-account-form) (login, password). Then this account can be linked to the [Renater identity federation](https://www.renater.fr).
For support about OPIDoR, you can check the [cat-OPIDoR support providers page](https://cat.opidor.fr/index.php/Accompagnement).

- DSW is a tool to collaboratively compose data management plans through customisable questionnaires. IFB has used DSW to develop templates for France Bioimaging ([FBI data management plan](https://dsw.france-bioinformatique.fr)) and for Hosted Scientific Service Management Plan ([HSSMP](https://dsw.genouest.org)). 

### Data collection

Although they are not part of IFB, other infrastructures in France can also help you generate new data. Specifically, some facilities can assist you with in vivo and in vitro experiments, synthetic biology, omics techniques, imaging, structural biology and other techniques and expertise. To find the adequate facility you may use the [Ministry search engine](https://data.enseignementsup-recherche.gouv.fr/pages/feuille_de_route_2018/?sort=acronyme) or the [IBiSA directory](https://www.ibisa.net/trouver-plateforme/) of french facilities in Life Sciences. 

Once your data have been generated by the facility, you will need to [transfer](data_transfer) it to your local system or to the IFB infrastructure, if you intend to use the IFB’s compute services. In both cases it is a good practice to get in touch with IT support (local or IFB), especially if the volume of your data is large. 

If you have to reuse previously generated data, keep in mind that the different IFB platforms provide many specialized databases. A list of the databases is available [here](https://ressources.france-bioinformatique.fr/en/services/data). These databases are, for the most, freely available. 

To support data collection along with standard metadata, IFB is providing SEEK instances available at [URGI](https://urgi.versailles.inrae.fr/fairdom/) and [GenOuest](https://research-sharing.cesgo.org). 


### Data processing and analysis 

IFB infrastructure gives you access to several flavours of computing resources, according to your needs and expertise:

* Several clusters hosted either at IFB-Core or on any of the member platforms. You can [request accounts](https://www.france-bioinformatique.fr/en/ifb-clusters/) on any of the member clusters. 
* The [Galaxy France](https://usegalaxy.fr) portal operated by IFB members in complement of the [Galaxy Europe](https://usegalaxy.eu). 
* The cloud federation [Biosphere](https://biosphere.france-bioinformatique.fr) allows the deployment of ready-to-use appliances (virtual machines with all required software installed for analysis) for several scientific domains (Genomics, Bioimaging, Metabolomics, etc.). A list of the different appliances is available on the [RainBio catalogue](https://biosphere.france-bioinformatique.fr/catalogue/). You can log in [here](https://biosphere.france-bioinformatique.fr/cloudweb/login/?next=/) using your academic credentials. 

Each of the computing resources offers its own storage solution tailored for the needs of the users (fast access, capacitive). You may have to choose a resource according to what its service offers and also according to its proximity to your own location in order to benefit from better support and also better data transfer speed.

IFB infrastructure can also help you with bioinformatics analysis of your data. Many of the IFB member platforms can provide expertise for data analysis in many domains (genomics, metagenomics, transcriptomics) as well as software development. To check the expertise of the platforms, you can use this [catalog](https://ressources.france-bioinformatique.fr/en/expertise). A list of the tools developed by all IFB members is available [here](https://ressources.france-bioinformatique.fr/en/services/tools). 

### Data sharing and publishing

It is good practice to [publish](data_publication) your data on repositories. IFB encourages researchers to browse the list of {% tool "elixir-deposition-databases-for-biomolecular-data" %} to find the appropriate repository. 

The french scientific community benefit from [Recherche.Data.Gouv](https://recherche.data.gouv.fr/en) a national Dataverse repository. This repository is associated with [thematic reference centres](https://recherche.data.gouv.fr/en/page/thematic-reference-centers-providing-expertise-for-individual-scientific-fields) and data management clusters. IFB is the reference centre for Life Science. 

You can also browse [cat-OPIDoR](https://cat.opidor.fr/index.php/Cat_OPIDoR,_wiki_des_services_dédiés_aux_données_de_la_recherche) for an overview of the different services related to data management provided by IFB infrastructure and its stakeholders in France.

### Compliance monitoring & measurement

IFB infrastructure promotes the implementation of the FAIR principles. To this end, IFB provides and encourages the use of the [FAIR-Checker](https://github.com/IFB-ElixirFr/fair-checker), a web interface aimed at monitoring the level of FAIRification of data resources. This tool uses the FAIRMetrics APIs to provide a global assessment and recommendations. It also uses semantic technologies to help users in annotating their resources with high-quality metadata.

