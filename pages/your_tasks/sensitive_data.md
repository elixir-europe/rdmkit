---
title: Sensitive data
contributors: [Rob Hooft, Yvonne Kallberg, Pinar Alper, Markus Englund, Thanasis Vergoulis, Robert Andrews]
description: How to identify the sensitivity of different research data types
page_id: sensitive
related_pages: 
  tool_assembly: [tsd, covid-19, transmed]
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=%22sensitive+data%22#materials
  - name: RDMbites for using REDCap
    registry: TeSS
    url: https://tess.elixir-europe.org/collections/rdmbites-redcap-collection
  - name: RDMbites for sensitive data
    registry: TeSS
    url: https://tess.elixir-europe.org/collections/rdmbites-sensitive-data-collection
dsw:
- name: Are there privacy reasons why your data can not be open?
  uuid: 019db0b3-9067-4134-8bfd-76db3cfc572a
- name: Will you collect any data connected to a person, "personal data"?
  uuid: 49c009cb-a38c-4836-9780-8a8b3dd1cbac
- name: How is pseudonymization handled?
  uuid: 59748a7b-f729-404d-babe-3147e2c6b247
- name: Could the coupling of data create a danger of re-identification of anonymized
    privacy sensitive data?
  uuid: 6b3d62a5-1d4d-49e1-aaf1-0a8b398a7ac3
- name: Does this dataset contain personal data?
  uuid: a1d76760-053c-4706-80a2-cfb6c6a061f3
- name: Does this dataset contain sensitive information?
  uuid: cc95b399-7d8d-4232-bccf-686f78c91bff
- name: Are personal data sufficiently protected?
  uuid: d5990471-0618-42cd-92cb-bbbfd4f61532
faircookbook:
- name: Declaring data's permitted uses
  url: https://w3id.org/faircookbook/FCB035
---

## Is your data sensitive?

### Description

In general, the term "sensitive data" is used for any data that could do harm (for example to people, organisations, countries, or ecosystems) if it would be openly available. 
This can for example be personal or commercial information, but also information such as breeding grounds of endangered species. 
Any such data must be protected against unauthorized access.
What is considered sensitive information is usually regulated by national laws and may differ between countries. You should be cautious when you are dealing with sensitive, or potentially sensitive, information.


### Considerations

* If you deal with any information about individuals from the EU, you are bound by the [General Data Protection Regulation (GDPR)](https://gdpr.eu/what-is-gdpr/). In GDPR, such data is called "personal data".
* In the context of GDPR "special category data" is a subclass of "personal data" that is potentially even more harmful, and GDPR prescribes very strict rules for dealing with this data. Article 9 of GDPR defines the special categories as data consisting of racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership, genetic data, biometric data, data concerning health or data concerning a natural person's sex life or sexual orientation. Confusingly, these special categories are sometimes colloquially called "sensitive data". Note that this page is concerned with the broader definition of "sensitive data".
* Information in Life Science projects are for the most part categorised under health and genetic data and are considered special category data under the GDPR.
* You need to assess whether or not your dataset contains attributes that can lead to the identification of a person. Note that combinations of attributes that are themselves not identifiable can be identifiable together. See the definitions described in the [How can you de-identify your data](#how-can-you-de-identify-your-data) section.
* You need to know the de-identification status of your data. Life Science research data rarely contains directly identifying attributes. Research data would typically be pseudonymised or anonymised. If you work with personal data, you must understand the difference between these two (see under de-identification below).
* For some studies there is a cohort owner, often a clinical party or a trusted third party that can map study participant keys back to names and surnames. Such data is considered pseudonymous.
* If there are no means to map the data back to individuals, then the data is considered anonymous and is out of the scope of the GDPR.
* You should keep in mind that anonymising data is a notoriously difficult task. Does your dataset contain a wide array of attributes, or exhibit unique traits/patterns such that one can reasonably expect that not more than a dozen people in the world have those together? In that case, you can not assume that it is anonymous. Such data run the risk of being linked back to individuals through various technical means. You need to take into account that technical means to identify people in the future may be more powerful than than they are right now: i.e. data that is anonymous right now may not be anonymous forever.


### Solutions

* Identify what legislations and regulations there are that you are expected to follow. Your institution's website may give you hints on where you can look for information about sensitive data.
* If you cannot determine if your data is sensitive, contact someone with expert knowledge in that area.


## How can you de-identify your data?

### Description

Data anonymization is the process of irreversibly modifying personal data in such a way that subjects cannot be identified directly or indirectly by anyone, including the study team. If data are anonymized, no one can link data back to the subject.

Pseudonymization is a process where identifying-fields within data records are replaced by artificial identifiers called pseudonyms or pseudonymized IDs. Pseudonymization ensures no one can link data back to the subject, apart from nominated members of the study team who will be able to link pseudonyms to identifying records, such as name and address.

Data anonymization involves modifying a dataset so that it is impossible to identify a subject from their data. Pseudonymization involves replacing identifying data with artificial IDs, for example, replacing a healthcare record ID with an internal participant ID only known to a named clinician working in the study.

### Considerations

Both anonymization and pseudonymization are approaches that comply with the GDPR.
Simply removing identifiers cannot guarantee data anonymity. A dataset may contain unique traits/patterns that could identify individuals. An example of this would be recording 2 potentially unrelated attributes such as the instance of a rare disease and country of residence, where there is only a single case of this disease in this country.
Data that is anonymous currently may not be anonymous in the future. Future datasets on the same individual may disclose their identity.
Anonymization techniques can sometimes damage the statistical properties of the data, for example, translating current participant age into an age range.

### Solutions

An example of pseudonymization is where participants in a study are assigned a non-identifying ID and all identifying data (such as name and address) are removed from the metadata to be shared. The mapping of this ID to personal data is held separately and securely by a named researcher who will not share this data.
There are well-established data anonymization approaches, such as k-anonymity, l-diversity, and differential privacy.

