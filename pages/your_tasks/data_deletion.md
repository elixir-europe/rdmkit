---
title: Data deletion
contributors: [Vilem Ded, Diana Pilvar, Bert Droesbeke]
description: How to properly delete data
page_id: data_deletion
related_pages: 
  tool_assembly:
training:
dsw:
faircookbook:
---

## How do you properly delete data?

### Description

Data deletion is a critical phase in the data lifecycle, especially in the context of data protection regulations (e.g. GDPR), ethical research practices, and responsible AI development. Deletion ensures that data is not only inaccessible but also irrecoverable when it is no longer needed or permitted to be retained.

Importantly, data should not simply disappear. It should be properly deleted in a controlled and documented manner.

### Considerations

* Data should be deleted once the legally, contractually, or institutionally defined retention period has expired. This ensures compliance with data governance policies and avoids unnecessary storage of outdated information.
* When a research project concludes, data that is not selected for long-term preservation should be deleted. This helps maintain a clean and manageable data environment and reduces long-term storage costs.
* Deleting obsolete, redundant, or unnecessary data supports the principle of data minimisation. It also reduces risks related to data breaches and helps optimise storage resources.
* Even after data is deleted, minimal metadata such as the dataset identifier, deletion date, and reason for deletion should be retained. This supports auditability, provenance tracking, and alignment with the FAIR principles.
* It is important to inform relevant stakeholders, including data providers and repositories (e.g. [UK Data Service – Data Disposal](https://ukdataservice.ac.uk/learning-hub/research-data-management/store-your-data/disposal/)), about the deletion of data. Clear communication ensures transparency and maintains trust in data stewardship practices.

### Solutions
 
* Deletion criteria should be defined in advance, ideally within data management plans (DMPs). This proactive approach ensures that data is deleted in a timely and compliant manner.
* Secure data deletion methods should be employed to ensure information is rendered irrecoverable. This can be achieved through techniques such as disk overwriting when the data is actively overwritten by random values ( {% tool "dban" %},  {% tool "eraser" %}, {% tool "lethe" %}) or destruction of the storage media by degaussing, shredding or crushing.For more detailed guidance and a list of recommended tools, you can refer to the [knowledge base of Brown University](https://ithelp.brown.edu/kb/articles/data-removal-guidelines).
* Regular reviews of data assets should be implemented to identify data that has reached the end of its retention period. This helps ensure that deletion policies are consistently applied.
* Automating deletion workflows using scripts or data management tools can improve efficiency and reduce the risk of human error. Automation also supports scalability in large data environments.
* Detailed logs of deletion events should be maintained, including who deleted the data, when, and why. These logs support accountability, compliance audits, and internal reviews.

