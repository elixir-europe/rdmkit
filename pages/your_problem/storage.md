---
title: Data storage
keywords:
contributors: [Ulrike Wittig, Elin Kronander, Munazah Andrabi]
tags: [collect, analyse, preserve, share, IT support] 
---

## What storage solutions are available?

There are several different types of storage solutions, for example
* Local storage on your hard drive or local servers
* High performance compute clusters
* Secure storage for sensitive data
* Public repositories
* Cloud service solutions

Depending on what type of data you wish to store, some might be more suitable than others.
The timeline and purpose of the storage are also deciding factors for choosing a storage solution.

### Considerations about the data
* What volume of data do you need a storage solution for?
* Who will need to access the data, only yourself, internal or external collaborators?
* How often will the data be accessed, is it being actively worked on or mainly stored in the current version?
* Do you need the storage solution to be compatible with certain analysis tools?
* Is your data sensitive?

### Considerations about the type of storage solution
* What are the backup procedures for this storage solution?
* What are the costs associated with this storage solution?
* How sustainable is this storage solution, i.e. how is it maintained and funded?

### Solutions
To find out what storage solutions are available to you and which one fits your needs, you can reach out to the IT-department of your host institution. Also, there are often national infrastructures available, for your domain or specialised on computing services, that offers storage solutions as well.

For active data, it is important that it is easily accessible for everyone that needs to work with it. See recommendations on how to store and manage data during the course of your project below. For recommendations about storage after the active phase of a project, see recommendations further down.
For sensitive data, consider the [Data Sensitivity guidelines](data_classification).
For storing your data in a way for others to find and access it, consider a public repository.
For Big Data, local storage is often not suitable.

## How store and manage your data during the course of a project?

During the active phase of your project, it is important to choose a storage solution that suits your need for management, accessibility and security. For collaborative projects a central storage place for intermediate and final results as well as the sharing of research data between the collaboration partners is essential.  

### Considerations
* Technical considerations and costs (storage space, in-house versions, backups etc.)
* Security and data protection rules (see [Data protection](data_protection))
* Usage of standard formats, identifiers, ontologies, controlled vocabularies
* Storage of metadata from the beginning (see [Metadata Management](metadata_management))
* Storage and interlinkage of all available data of an experiment/project (raw data, processed results, protocols, methods etc.)
* Variable access permissions and sharing definitions during the project (private data or intermediate results versus shared or published data)

### Solutions

* [SEEK](https://seek4science.org/) - public SEEK instance [FAIRDOMHub](https://fairdomhub.org)
* [iRODS](https://irods.org/)
* [e!DAL](https://edal.ipk-gatersleben.de/)
* [Research Data Management Platform (RDMP)](https://www.dundee.ac.uk/hic/researchdatamanagementplatform/)

## How store your data after a project ends?

The requirements of a long term storage solution after project completion are different from the requirements during the active phase of a project. The need for quick access is substantially lower and the need to be cost-efficient is higher. Provided that the data also is published in a public repository, the long term storage solution is mainly for archival purposes.

### Considerations

* How much storage is needed?
* For how long should the data be preserved?
* Who will take care of the maintenance?

### Solutions

When the project finishes you should  select which data needs to be stored long term, and ensure that the data is accompanied with sufficient documentation, so that it will be understandable by yourself and others in the future. Ensure that standard, open source, file formats are used instead of proprietary ones. Use compression of the files to reduce the volume, e.g. tar (tape archive) and gzip.

Check with your institution regarding regulations and policies that you have to adhere to regarding archiving.

No matter the solution chosen, someone needs to ensure that the data is maintained appropriately (that it is backed up, that integrity is checked, that it is transferred to new formats or storage media when technology advance, etc). Check with your institution or national infrastructure for cost-effective storage solutions.

### External links

* About tar on Wikipedia: [Tar_(computing)](https://en.wikipedia.org/wiki/Tar_(computing))
* About gzip on Wikipedia: [gzip](https://en.wikipedia.org/wiki/Gzip)

## Relevant tools and resources

{% include toollist.html tag="storage" %}

