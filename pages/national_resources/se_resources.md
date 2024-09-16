---

title: Sweden
country_code: SE
contributors: [Stephan Nylinder, Yvonne Kallberg, Niclas Jareborg]
coordinators: [Niclas Jareborg, Yvonne Kallberg]

training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/events?include_expired=true&node=Sweden&scientific_topics=Data+management
  - name: SciLifeLab Data Management YouTube
    registry: YouTube
    url: https://www.youtube.com/playlist?list=PL1nnHOyxN_WdqnzLqbmWJz_i0f2anT9cS

national_resources:
  - name: DS-Wizard ELIXIR-SE
    description: Data Stewardship Wizard is a tool to be used when planning for data management, including generating a data management plan (DMP). This instance provides guidance with focus towards Swedish life science researchers, including national resources.   
    how_to_access: ELIXIR AAI login
    instance_of: data-stewardship-wizard
    related_pages:
      your_tasks: [dmp]
    url: https://dsw.scilifelab.se/ 
  - name: SciLifeLab Data Repository (Figshare)
    description: A repository for publishing any kind of research-related data, e.g. documents, figures, or presentations.
    how_to_access: Available to everyone with an affiliation to a Swedish academic institution.
    instance_of: figshare
    related_pages:
      your_tasks: [existing_data, data_publication]
    url: https://scilifelab.figshare.com/
  - name: NBIS Data Management Consultation
    description: Free consultation service regarding data management questions in life science research.
    how_to_access: Available to everyone with an affiliation to a Swedish academic institution.
    related_pages:
      your_tasks: [dmp, data_publication, sensitive]
    url: https://nbis.se/services/guidance-on-data-handling/apply
  - name: Swedish Pathogens Portal
    description: The Swedish Pathogens Portal provides information, guidelines, tools and services to support researchers to utilise Swedish and European infrastructures for data sharing.
    related_pages:
      tool_assembly: [covid19_data_portal]
      your_domain: [human_data]
      your_tasks: [sensitive, existing_data, data_publication]
    url: https://pathogens.se/ 
  - name: NAISS 
    description: The National Academic Infrastructure for Super­computing in Sweden (NAISS) is a national research infrastructure that makes available large-scale high-performance computing resources, storage capacity, and advanced user support, for Swedish research.
    how_to_access: An application is required to gain access to the compute and storage services.
    related_pages:
      your_tasks: [data_analysis, storage]
    url: https://www.naiss.se/ 
  - name: SciLifeLab RDM Guidelines
    description: Knowledge hub for the management of life science research data in Sweden.
    url: https://data-guidelines.scilifelab.se/
  - name: Human Data Guidelines
    description: Guidelines as well as further information on legal considerations when working with human biomedical data.
    related_pages:
      your_domain: [human_data]
      your_tasks: [sensitive]
    url: https://data-guidelines.scilifelab.se/topics/research-involving-human-data/
  - name: Federated EGA Sweden node
    description: Secure archiving and sharing of genetic and phenotypic data resulting from Swedish biomedical research projects.
    instance_of: the-european-genome-phenome-archive
    related_pages:
      your_domain: [human_data]
      your_tasks: [sensitive, existing_data, data_publication]
    url: https://fega.nbis.se/
---

## Introduction 

This page provides a general overview of national resources on research data management (RDM) in Sweden, directed towards researchers and official collaborators. National goals and long term data management achievements are provided in the [**Research Bill 2020/21-60**](https://www.regeringen.se/contentassets/da8732af87a14b689658dadcfb2d3777/forskning-frihet-framtid--kunskap-och-innovation-for-sverige.pdf).
The Swedish ELIXIR node National Bioinformatics Infrastructure Sweden ([**NBIS**](https://nbis.se/)) offers support and training in data management to life science researchers in Sweden, in collaboration with the [**Data Centre**](https://www.scilifelab.se/data/) at Science for Life Laboratory (SciLifeLab).

## Funders with policies

The [**Swedish Research Council**](https://www.vr.se/) has a government mandate to coordinate and promote Sweden’s work on introducing [**open access**](https://www.vr.se/english/mandates/open-science/open-access-to-research-data/the-swedish-research-councils-recommendation.html) to research data, with the goal for transition to open access to research data to be fully implemented by 2026. As of 2019 all who receive grants from the council must have a data management plan (DMP), written according to their [**DMP template**](https://www.vr.se/english/applying-for-funding/requirements-terms-and-conditions/producing-a-data-management-plan/data-management-plan-template.html), which is a partially reworked version of Science Europe’s "Core Requirements for Data Management Plans".

[**Formas**](https://formas.se/) - The Swedish Research Council for Environment, Agricultural Sciences and Spatial Planning - has a [**policy**](https://formas.se/download/18.7357e3f3168752d5a10c7f7/1549956105856/Beslut_policy_oppna_data.pdf) on open access to research data, and requires that a [**DMP**](https://formas.se/soka-finansiering/sa-har-gar-det-till/att-kanna-till-nar-du-skriver-en-ansokan.html) is written and can be shown upon request.

## Authorities and Regulations

If personal data is processed in your research, contact your institute’s Data Protection Officer, and if available, the Research Data Office (see list at end of page), for guidance on ethical and legal compliance. The following is a list of ethical and legal committees, authorities and regulations of interest:

### Authorities

* [Swedish Ethical Review Authority](https://etikprovningsmyndigheten.se/)
* [Swedish Authority for Privacy Protection (IMY)](https://www.imy.se/en/)

### Regulations

* [The Ethics Review Act](https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-2003460-om-etikprovning-av-forskning-som_sfs-2003-460) (in Swedish)
* [The Patient Data Act](https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/patientdatalag-2008355_sfs-2008-355) (in Swedish)
* [The Biobank Act](https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-2002297-om-biobanker-i-halso--och_sfs-2002-297) (in Swedish)
* [The Archives Act](https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/arkivlag-1990782_sfs-1990-782) (in Swedish)
* [Lag (2018:218) med kompletterande bestämmelser till EU:s dataskyddsförordning](https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-2018218-med-kompletterande-bestammelser_sfs-2018-218)

## Domain-specific infrastructures and resources 

The [**SciLifeLab Data Centre**](https://www.scilifelab.se/data)  provides services for IT and data management, including Data Stewardship Wizard instance (for writing data management plans), the Swedish Pathogens Portal, and the SciLifeLab Data Repository. 

Data stewards at [**NBIS**](https://nbis.se/) (ELIXIR-SE) provide consultation and support services regarding data management questions, including e.g. guidance when writing data management plans and when doing submissions to domain-specific repositories. For information about this and other resources at NBIS please see the [**Data Management**](https://nbis.se/services/guidance-on-data-handling) page. An upcoming resource is the [**FEGA Sweden**](https://fega.nbis.se/), a secure data archive and sharing platform for sensitive datasets, which will be integrated with the {% tool "the-european-genome-phenome-archive" %}.

The [**National Academic Infrastructure for Super­computing in Sweden**](https://www.naiss.se/) (NAISS) is a national research infrastructure that provides resources and user support for large scale computation and data storage to meet the needs of researchers from all scientific disciplines and from all over Sweden. Of particular use for life science researchers is the [**NAISS-SENS**](https://www.uppmax.uu.se/projects-and-collaborations/naiss-sens/) project which provides high-performance computing resources for analyzing sensitive data.

[**Swedish National Data Service**](https://snd.gu.se/en) (SND) with its network of almost 40 higher education institutions and public research institutes, provides researchers with a coordinated and quality-assured system for finding, describing, and sharing research data, nationally as well as internationally. The [**SND network**](https://snd.gu.se/en/about-us/snd-network) has agreed to create local units for managing research data (Data Access Units (DAUs)), with the main task to assist researchers in their respective organisation in making research data as accessible as possible, via training and support in data management. SND also provides a [**DMP checklist**](https://snd.gu.se/en/manage-data/guides/dmp-checklist) to support researchers in writing data management plans.
 
List of universities with established Research Data Offices or Data Access Units (DAUs), with links to local online resources and contact information:
* Chalmers University of Technology - [Research Data Support](https://www.chalmers.se/en/infrastructure/ecommons/chalmers-data-office/) - <dataoffice@chalmers.se>
* Karolinska Institutet - [Research Data Support](https://staff.ki.se/research-data-management) - <rdo@ki.se>
* KTH Royal Institute of Technology - [Research Data Support](https://www.kth.se/en/biblioteket/publicera-analysera/hantera-forskningsdata/) - <researchdata@kth.se>
* Linköping University - [Research Data Support](https://ep.liu.se/en/datamanagement.aspx) - <datamanagement@liu.se>
* Linnaeus University - [Research Data Support](https://lnu.se/en/medarbetare/researcher/researcher5/research-data/) - <dau@lnu.se>
* Lund University - [Research Data Support](https://www.lub.lu.se/en/services-and-support/research-data/contacts-and-research-data-initiatives) - See web page for contact information
* Stockholm University - [Research Data Support](https://www.su.se/staff/researchers/research-data) - <opendata@su.se>
* Swedish University of Agricultural Sciences - [Research Data Support](https://www.slu.se/en/subweb/library/publish-and-analyse/archiving-and-publishing-research-data) - <dms@slu.se>
* Umeå University - [Research Data Support](https://www.umu.se/en/library/research-data/) - See [contact page](https://www.umu.se/en/library/research-data/organisation-and-contacts/) for contact information
* University of Gothenburg - [Research Data Support](https://medarbetarportalen.gu.se/service-stod/hantering-av-forskningsdata/?languageId=100001) - <researchdata@gu.se>
* Uppsala University - [Research Data Support](https://mp.uu.se/en/web/info/forska/forskningsdata) - <dataoffice@uu.se>
* Örebro University - [Research Data Support](https://www.oru.se/english/research/research-support/starting-up-your-research-project/data-management-plan-components/do-you-need-help-with-your-research-data/) - See web page for contact information
