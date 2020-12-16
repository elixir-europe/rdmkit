---
title: Data Classification
keywords: human data
contributors: [Rob Hooft, Yvonne Kallberg, Pinar Alper]
tags: [share, collect, process, policy officer]
---

## Is my data sensitive?

### Considerations

* If you deal with any information about individuals from the EU, you are bound by the GDPR and such data is called “personal data”. 
* Not all personal information is sensitive: The GDPR [Article 9] identifies specific pieces of data as sensitive: data consisting of racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership, genetic data, biometric data, data concerning health or data concerning a natural person's sex life or sexual orientation.  
* Information in Life Science projects are for the most part categorised under health and genetic data and are considered sensitive under the GDPR.
* You need to assess whether or not your data set contains personally identifying attributes. 
* You need to know the de-identification status of your data. Life Science research data rarely contains personally identifying attributes. Research data would typically be in pseudonymised or anonymised form, meaning devoid of attributes such as name, surname etc. 
* For some studies there is a cohort owner, often a clinical party or a trusted third party that can map study participant keys back to names and surnames. Such data is considered pseudonymous. 
* If there are no means to map the data back to individuals, then the data is considered anonymous and is out of the scope of the GDPR. 
* You should keep in mind that anonymising data is a notoriously difficult task. Does your dataset contain a wide array of attributes, or exhibit unique traits/patterns such that one can reasonably expect that not more than a dozen people in the world have those together? In that case, you can not assume that it is anonymous. Such data run the risk of being linked back to individuals through various technical means. You need to take into account that technical means to identify people in the future may be more powerful than than they are right now: i.e. data that is anonymous right now may not be anonymous forever

Finally; not all sensitive information is personal: information on e.g. breeding grounds of endangered species may be sensitive, but it is not personal information.

### Things that can help you

* links to tools etc...
* links to external help

## Relevant tools and resources

{% include toollist.html tag="data classification" %}