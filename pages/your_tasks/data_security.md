---
title: Data security
contributors: [Pinar Alper, Yvonne Kallberg, Vilem Ded, Eva Csosz, Niclas Jareborg]
description: How do you ensure that your data is handled securely.
page_id: data_security
redirect_from: data_protection
related_pages: 
  tool_assembly: [tsd, transmed]
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=data+protection#materials
dsw:
- name: What technical and procedural safeguards have been established for processing
    the data?
  uuid: a30f5047-33c1-45a7-8b3f-b1b90c364fc9
faircookbook:
- name: Downloading data with Aspera protocol
  url: https://w3id.org/faircookbook/FCB015
- name: Transferring data with SFTP protocol
  url: https://w3id.org/faircookbook/FCB014
- name: Creating file checksums
  url: https://w3id.org/faircookbook/FCB052
- name: Validating checksums to verify file integrity
  url: https://w3id.org/faircookbook/FCB053
---

## How do you ensure that your data is handled securely?

### Description

To protect your research data, code, and other information assets you should establish adequate Information security measures. Information security relies on combinations of technical and procedural measures that work together to ensure protection of the data at a suitable level. To note is that failure by humans to follow the procedural measures often poses a higher vulnerability to security risks than shortcomings of the technical measures. 

### Considerations

* Information security is usually described as containing three main aspects - **Confidentiality**, **Integrity**, and **Availability**.
  * Confidentiality is about measures to ensure that data is kept confidential from those that do not have rights to access the data.
  * Integrity is about measures to ensure that data is not corrupted or destroyed during storage or transmission.
  * Availability is about measures that ensure access to the data is possible at the time of need or access does not require an inordinate amount of time.
* What information security measures that need to be established should be defined at the planning stage (e.g. when doing a risk assessment for a GDPR Data Protection Impact Assessment). This should identify information security risks, and define measures to mitigate those risks. 
* Balance the cost and effort for protecting your data at an appropriate level. For this, it is useful to classify the impact of failure for the three different CIA aspects to guide your choices. You should not spend more resources than necessary if the impact of failure is low enough that you can easily cope with it. Nor should you spend too few resources on protective measures for aspects where the impact is high. For example, the Availability aspect will probably differ a lot if your data is used in a clinical versus a research setting, where protecting against a system failure in the research setting can be a lot less resource demanding than in the clinical setting.
* Ensure that everyone that works with the data knows what is expected of them, how the Information Security measures are to be implemented, and who is responsible for ensuring that they are followed and performed as agreed.
* Be sure to contact the IT or Information security office at your institution to get guidance and support to address these issues. They should be able to provide you with suitable solutions for your needs.

### Solution

* Below is a non-exhaustive list of good practices that might be relevant depending on the level of protection required. Note that some of these might be quite costly, such as investing in hardware or hiring highly specialized staff to ensure high levels of security. More on costs for RDM is available on the [Costs of data management](/costs_data_management) page.
* Confidentiality
  * Use password protection on all computers
  * Use two-factor authentication, i.e. using two ways of identification in order to obtain access to the (remote) data
  * Set file and folder permissions, e.g. use read-only access for data that should never be changed, and limit access to only those who needs it
  * Apply a “Lock screen policy” to prevent unauthorised access of systems from those who do not have access rights and permissions.
  * Use encrypted data transfers to avoid eavesdropping
  * Consider implementing systems monitoring measures in order to ensure that hacking attempts are detected
  * Decide on procedures on how systems can be physically accessed. Should data be allowed to reside on personal laptops, or only on designated stationery systems? Should stationary systems be physically protected in locked compartments only accessible to a limited number of individuals?
* Integrity
  * Generate checksums for all files as soon as possible, preferably upon file creation.
  * Keep the number of copies to a minimum to facilitate its management.
  * Adopt a data release workflow which ensures the data are versioned and preserved. Each version shall be protected against any change by users, e.g. by setting permissions to read-only.    
  * Perform quality checks both upon data collection to ensure accuracy and on a regular basis to discover potential integrity errors.
  * Define, document and adopt a back-up strategy for your data.
  * Utilise available tools for data management (data warehouses) ensuring data integrity by default.
* Availability
  * Set up disaster recovery procedures with instructions on *what* data, *how*, and by *who*, recovery of data should be done in case an incident of system failure or data loss happens.
  * If high availability is a must, consider designing a redundant computing and storage strategy where there are physically separated compute and storage resources, that ensures that the data is available at all times even in the event of system failure.
* Organisational Measures
  * The procedures on how the technical protection measures are to be used, and who is responsible for what, must be understood by all personnel that work with the data, code, and other information assets. The procedures should be documented, and staff should have access to relevant training to follow the procedures. This is often the most vulnerable part in an Information Security strategy.
  * Policies are an important component of data management and they are essential for information security. Organisations use policies to announce to their staff and third parties the expectations, roles and responsibilities in data handling. Policies typically cover data classification, storage/backup, transfer, retention/archival, deletion/destruction, acceptable use of IT platforms and the reporting of security incidents and data breaches. In some cases research data requirements would be addressed in dedicated policies. Therefore, at the planning phase, it is important to understand institutional data policies applicable to the project’s data. If the data is considered sensitive as per the institutional data classification, this will have an impact on the IT platforms that can be used to store and transmit the data as well as the specific procedures to be followed.
  * Information inventories and documentation is another requirement for projects dealing with sensitive data. At the planning phase you should identify the various categories of data that will be processed in the project e.g. personal health and biomedical data, sensitive habitat data, IP restricted data from the industry. You should document which platforms will be used to process the data and the applicable security measures in case certain measures are applied to restricted classes of data. See the next section for GDPR-specific documentation requirements. See the [Data Sensitivity](/data_sensitivity) page for more information on sensitive data.
  * [ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001) is an international information security standard adopted by data processing centres worldwide. Some universities and research institutes also acquire an ISO 27001 certification for their IT environments. Such certifications allow institutions to consistently and thoroughly identify information security risks and put in place best practice information security controls. These controls would include all above mentioned technical and organisational safeguards and more.
