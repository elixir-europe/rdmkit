---
title: Data classification
keywords: [human data, data sensitivity]
contributors: [Rob Hooft, Yvonne Kallberg, Pinar Alper, Markus Englund, Thanasis Vergoulis, Robert Andrews]
tags: [share, collect, process, policy officer]
---

## Is my data sensitive?

### Description

Sensitive data is information that must be protected against unauthorised access. This can for example be personal or commercial information, but also information such as breeding grounds of endangered species. What is considered sensitive information is usually regulated by national laws and may differ between countries. You should be cautious when you are dealing with sensitive, or potentially sensitive, information.

### Considerations

* If you deal with any information about individuals from the EU, you are bound by the GDPR and such data is called “personal data”. 
* Not all personal information is sensitive: The GDPR [Article 9] identifies specific pieces of data as sensitive: data consisting of racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership, genetic data, biometric data, data concerning health or data concerning a natural person's sex life or sexual orientation.  
* Information in Life Science projects are for the most part categorised under health and genetic data and are considered sensitive under the GDPR.
* You need to assess whether or not your dataset contains personally identifying attributes. 
* You need to know the de-identification status of your data. Life Science research data rarely contains personally identifying attributes. Research data would typically be in pseudonymised or anonymised form, meaning devoid of attributes such as name, surname etc. 
* For some studies there is a cohort owner, often a clinical party or a trusted third party that can map study participant keys back to names and surnames. Such data is considered pseudonymous. 
* If there are no means to map the data back to individuals, then the data is considered anonymous and is out of the scope of the GDPR. 
* You should keep in mind that anonymising data is a notoriously difficult task. Does your dataset contain a wide array of attributes, or exhibit unique traits/patterns such that one can reasonably expect that not more than a dozen people in the world have those together? In that case, you can not assume that it is anonymous. Such data run the risk of being linked back to individuals through various technical means. You need to take into account that technical means to identify people in the future may be more powerful than than they are right now: i.e. data that is anonymous right now may not be anonymous forever


### Solutions

* Identify what legislations and regulations there are that you are expected to follow. Your institution's website may give you hints on where you can look for information about sensitive data.
* If you cannot determine if your data is sensitive, contact someone with expert knowledge in that area.


## How can I de-identify my data?

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

## Relevant tools and resources

{% include toollist.html tag="data classification" %}  


