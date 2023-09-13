---
title: Ethical aspects
contributors: [Karel Berka , Erin Calhoun, Paulette Lieby, Anamika Chatterjee, Korbinian Bösl]
description: Working on aspects in the management of research data that can raise ethical issues
page_id: ethics
related_pages:
  tool_assembly: [covid-19, transmed, tsd, csc]
training:
- name: 'Ethics/ELSI considerations - From FAIR to fair data sharing - recorded webinar'
  registry: TeSS
  url: https://tess.elixir-europe.org/materials/ethics-elsi-considerations-from-fair-to-fair-data-sharing
- name: 'Biomedical data: Ethical, legal and social implications - e-learning'
  registry: TeSS
  url: https://tess.elixir-europe.org/materials/biomedical-data
- name: 'From Swab to Server: Testing, Sequencing, and Sharing During a Pandemic - free online course'
  registry: TeSS
  url: https://tess.elixir-europe.org/materials/from-swab-to-server-testing-sequencing-and-sharing-during-a-pandemic
---
​
Ethics refers to moral principles and norms that help us identify right from wrong within a particular context. Ethical issues/concerns typically arise when these principles conflict. Navigating through such concerns often requires one to compare the benefits of an action with its potential harmful consequences.
When it comes to research involving human participants, such ethical concerns may appear when accessing, using, or sharing data of a sensitive nature, for example health or personal data. Ethics, however, goes beyond the issue of compliance with legal obligations, and the collection and use of data.
​

The [Open Data Institute](https://www.scribd.com/document/358778144/ODI-Ethical-Data-Handling-2017-09-13) narrows ‘ethics’ in the RDM context to:
​
> “A branch of ethics that evaluates data practices with the potential to adversely impact on people and society – in data collection, sharing and use.”
​

​
## Which aspects of RDM might raise ethical issues?
### Description
Ethical issues refer to moral principles and standards that guide human conduct and define what is considered right or wrong within a particular context.
​
### Considerations
* There are different aspects in the management of research data that can raise ethical issues. It is important to distinguish between ethical issues and legal behaviour.
    * Ethical standards may vary across cultures, disciplines, and professional organisations. Researchers are expected to adhere to these ethical principles even if certain practices are not explicitly prohibited by law. Often these standards are collected in declarations and guidelines, which may be backed by laws.
    * Legal behaviour, on the other hand, refers to compliance with applicable laws, regulations, and policies. Legal requirements provide a baseline level of conduct that researchers must meet to avoid legal sanctions. However, legal compliance does not necessarily guarantee ethical behaviour. Some actions may be legally permissible but raise ethical concerns, while others may be ethically unquestionable but explicitly prohibited by specific legislation.
​
* Ethical issues arise most often in research on or involving humans affecting human dignity and autonomy. These issues are partly addressed by the [General Data Protection Regulation](https://gdprinfo.eu/) (see also the [RDMkit data protection page](data_protection))
There are additional considerations connected to health research. Under the viewpoint of RDM you should especially consider:
    * Free and informed consent, the possibility of its withdrawal, its documentation, withdrawal (connected with data deletion) and its representation in a machine-actionable way (see also [What information must be given individuals whose data is collected](https://commission.europa.eu/law/law-topic/data-protection/reform/rules-business-and-organisations/principles-gdpr/what-information-must-be-given-individuals-whose-data-collected_en), the [EU clinical trials regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32014R0536) and respective national health research legislations)
    * Balancing access to research data and privacy of research participants (see [How much data can be collected](https://commission.europa.eu/law/law-topic/data-protection/reform/rules-business-and-organisations/principles-gdpr/how-much-data-can-be-collected_en), the [EU clinical trials regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32014R0536) and respective national health research legislations)
    * Unintentional discrimination of research participants, such as different perception of symptom severity in different population groups
    * Findings about participants that are outside of the original research question(s): see [Purpose of data processing](https://commission.europa.eu/law/law-topic/data-protection/reform/rules-business-and-organisations/principles-gdpr/purpose-data-processing_en) and [Incidental findings Archives - BBMRI-ERIC](https://www.bbmri-eric.eu/elsi-topic/incidental-findings/)
​
* Other ethical questions are arising from the impact of research outcomes, including data on the interest of communities or individuals
    * Fair management of intellectual property rights - also see e.g. Access and Benefit-sharing (ABS)
    * Publication of research data that might impact the reputation of communities or individuals
    * Publication of research data that might impact economical interests of  communities or individuals
    * Publication of research data that might impact security of society, communities or individuals
​
* There are also general research ethics considerations that are relevant in the context of research data, including:
    * What are the reasons justifying the exclusion/inclusion of research data in a particular context?
    * Is the data source accurate and trustworthy?
    * How can bias in practices of research data management be identified and minimised/avoided?
    * Assessment of models and algorithms used with respect to possible bias
    * Can the research data be misinterpreted?
    * Prevention of withholding of research data
    * Prevention of manipulation and fraud of research data
    * Assessment of who is excluded or included to data access and why
    * How can harm to other beings and the environment be identified and mitigated in a timely manner?
​
### Solutions
* Assess potential ethical implication through an ethics review
    * Your local ethics committee can help you to review the ethical implications of the project or might guide you to more relevant bodies and resources
* In order to address challenges when working with human data (see also the [RDMkit page on human data](human_data))
    * Used standardised consent forms (see e.g. [GA4GH consent toolkit]({% raw %}https://www.ga4gh.org/resource-library/#{%22document%22:{%22category%22:%22Toolkit%20Component%22,%22related_products%22:%22Consent%20Toolkit%22}}{% endraw %}), [BBMRI](https://zenodo.org/record/3928446)) that can be represented in a machine actionable way ([DUO](https://www.ga4gh.org/product/data-use-ontology-duo/))
    * Before you start collecting/processing data, be transparent about these in the consent form and also about the cases when withdrawal is no longer possible due to anonymization, aggregation, or other data processing.  Anticipate the possibility of consent/data withdrawal and implement administrative and technical processes.
    * Data should be anonymized whenever possible (this is a non-reversible process), pseudonymisation (this is a reversible process) enhances data protection in cases where this is not possible (see also [Recommendations on shaping technology according to GDPR provisions](https://op.europa.eu/en/publication-detail/-/publication/a8e7a463-29c5-11e9-8d04-01aa75ed71a1/) and the [RDMkit data protection page](data_protection))
    * Data analysis approaches that have potential to cause stigmatisation should be considered in advance and be discussed as part of an ethics review
    * Create processes for incidental findings before you start collecting data, include the way the participant wants you to deal with it in the consent form
* In order to manage the impact of data collection and sharing:
    * The management of intellectual property rights connected with the data, if any, should be planned early on ([RDMkit data management plan page](dmp)), be part of collaboration/consortium agreements, and make use of [standard licensing terms](licensing)
    * The Nagoya Protocol regulates access to genetic resources and conditions for transfer of genetic resources and traditional knowledge across counties. For implementations into national law please consult the [ABS Clearing House](https://absch.cbd.int/en/) (also see [RDMkit compliance monitoring & measurement](compliance))  
    * Laws & Regulations concerning biosecurity, data export control and national interests might be linked from the [RDMkit national resources pages](national_resources)
    * In order to ensure conformity with ethical research principles, the following should also be considered for data management:
        * Follow general research ethics laws and guidelines (see [below](ethics#how-can-i-identify-regulations-guidelines-and-laws-connected-to-ethics-in-my-research-context))
        * Minimise suffering of animals in research to the absolute minimum, following [the guidelines and laws relevant to your location as a baseline](national_resources). A sound documentation and management of research outputs is an essential cornerstone to reduce unnecessary repetitions of experiments. Consider the use of specialised LIMS systems to capture relevant [metadata](metadata_management)
        * Reflect on potential future implications of the outcome of research and data capture and sharing for society and environment ({% tool "rri-toolkit" %}, {% tool "rri-self-reflection-tool" %}) involving stakeholders of the research is an important measure in order to receive feedback. If data is presented to stakeholders, this should happen in an accessible format and might require pre-processing, visualisation and guidance.
        * Transparency and reproducibility of the research project underpin the scientific rigour of the project and reduce unnecessary duplication of efforts. Good RDM following the FAIR principles is a cornerstone of these efforts. Continuous tracking of [provenance](provenance) from e.g. research subjects to samples to data and semantic annotation of processes ([documentation and metadata](metadata_management)) can enhance the trustworthiness and value of research findings.
        * Automated sharing of research data after a specific period or milestones and deliverables in a project can be a good mechanism to enhance the openness of a project ([data management coordination](dm_coordination))
​

## How can I identify regulations, guidelines and laws connected to ethics in my research context?
​
### Considerations
* In all cases, your institution’s Data Protection Officer (DPO) is the person to refer to when considering ethical and legal aspects of data management.
* When looking for recommendations and regulations, it is best to start from the local, that is, starting what is applicable within your discipline, and nationally. Then (if applicable), EU policies, directives and regulations are to be explored, as well as global recommendations (for example, from the UNESCO).
* The list of resources given below does not attempt to be exhaustive: it tries to highlight the most relevant ones.
​
### Solutions
* Use [domain](your_domain) and [national](national_resources) pages in the RDMkit as a starting point
* Follow national legislation in terms of
    * Data protection
    * Conduct of health research, research on humans and animal studies
    * Framework on research ethics
    * Bio and national security
* Consult national, regional, institutional Ethics Boards
* Make use of guiding principles, recommendations, guidelines, ethical standards and declarations from professional associations and
    * [WMA Declaration of Helsinki – Ethical Principles for Medical Research Involving Human Subjects](https://www.wma.net/policies-post/wma-declaration-of-helsinki-ethical-principles-for-medical-research-involving-human-subjects/)  
    * For animal research: the [Three Rs principle](https://ec.europa.eu/health/scientific_committees/opinions_layman/en/non-human-primates/glossary/tuv/three-rs-principle.htm)  
    * For data produced with Machine Learning (ML) techniques: the [recommendations from UNESCO](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics), and the [DOME guidelines](https://dome-ml.org/), a product of the [ELIXIR ML focus group](https://elixir-europe.org/focus-groups/machine-learning)  
* Resources and Policies from research infrastructures
    * {% tool "bbmri-eric-s-elsi-knowledge-base" %} and the BBMRI [Helpdesk and Services](https://www.bbmri-eric.eu/elsi/helpdesk/)
    * ELIXIR ELSI Policy [ELIXIR Ethics Policy](https://zenodo.org/record/557027#.ZGtrzpFBxD8)  
* Check existing EU policies, directives and regulations
    * The [General Data Protection Regulation](https://gdprinfo.eu/)
    * The European [Clinical Trials Regulation](https://www.ema.europa.eu/en/human-regulatory/research-development/clinical-trials/clinical-trials-regulation)

### Further materials
* Basic ethical principles are compliant with relevant international regulations:
    * Universal Declaration of Human Rights, 10 December 1948
    * Article 8 of the European Convention on Human Rights
    * Council of Europe Convention for the Protection of Individuals with Regard to Automatic Processing of Personal Data 1981 (convention 108)
    * Charter of Fundamental Rights of the European Union 2010/C 83/0215
    * Directive 95/46/EC of the European Parliament of 24 October 1995 on the protection of individuals with regard to the processing of Personal Data and on the free movement of such data
