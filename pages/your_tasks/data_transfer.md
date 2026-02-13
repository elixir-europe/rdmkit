---
title: Data transfer
contributors: [Olivier Collin, Alan R Williams, Flora D'Anna, Frederik Delaere, Munazah Andrabi, Marina Popleteeva, Nazeefa Fatima]
description: How to transfer data files.
page_id: transfer
related_pages: 
    Tool_assembly: []
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=%22data+transfer%22#materials
dsw:
- name: How will the raw data be transported?
  uuid: 2e8d6e55-36ea-46eb-a921-65e550bce5dc
- name: How will your first data come in?
  uuid: f4065e54-d27a-45de-be4c-10384feacd0d
faircookbook:
- name: Transferring data with SFTP protocol
  url: https://w3id.org/faircookbook/FCB014
- name: Downloading data with Aspera protocol
  url: https://w3id.org/faircookbook/FCB015
- name: Creating file checksums
  url: https://w3id.org/faircookbook/FCB052
---

## How do you transfer large data files?

### Description

Often, research in Life Sciences generates massive amounts of digital data, such as output files of ‘omics’ techniques (genomics, transcriptomics, metabolomics, proteomics, etc.). Large data files cannot be sent by email because they exceed the file size limit of most common email servers. Moreover, some data cannot be sent by email due to its sensitive nature. So, how can large data files be transferred from a local computer to a distant one?

### Considerations

There are many aspects to consider when dealing with data transfer.

* The **size or volume** of the data and the **capacity or bandwidth of the network** that links your local computer with the distant computer are crucial aspects. Data size and bandwidth are tightly linked since transferring large volumes of data on a low bandwidth network will be so time consuming that it could be simpler to send the data on a hard drive through carrier services.

* You need to be aware of the **legal and ethical implications** of your data transfer.
    * For personal data, you have to ensure compliance with various legal and ethical frameworks, including the GDPR. You might have to establish a **data processing** or **joint data controller** agreement before you can transfer the data.  We highly recommend you to check the [human data](human_data) pages of the RDMkit.
    * For data relevant for later patenting or other types of commercialisation you  might want to establish a **non-disclosure** or other type of agreement with the other party to protect your interest.
    * You might also have to consider other laws and regulations, for instance regarding **biosecurity** of data affecting pathogens or other aspects of potential **dual-use**.
    * The technical protocol you choose for your data transfer should meet your requirement for **data security** resulting these implications. You can interact with the IT departments at both locations in order to establish your strategy.


* If you have the technical skills and knowledge, consider using appropriate File Transfer Protocols.

* Consider using Cloud Storage Services (see [Data storage page](storage)), that provide data sharing solutions, or specialised data transfer services available in your institute or country.

* Consider pros and cons of transferring data by shipping hard disks through carrier services (time, costs, security). This is not a recommended method, unless good internet connection is not available.

* During a transfer, some data might become corrupted. Thus, it is important to check if the files you transferred have conserved their integrity. This can be done with hash algorithms. A checksum file is calculated for each file before transfer and compared to a checksum calculated on the transferred files. If the checksums are the same, then the files are not corrupted.

* Since data transfer involves so many technical aspects, it is a good idea to interact with your technical/IT team in order to avoid any problem if you want to transfer a large amount of data.

### Solutions

Preferable transfer channel depends on the volume of your data and number of files. However, there are several general approaches to help you with the task. 
* Try to optimise and ease your data transfer by archiving your data in a single file. This can be done with two tools available on most systems.
    * tar (tape archive) will create an archive, a single file containing several files or directories.
    * gzip: since tar does not compress the archive created, a compression tool such as gzip is often used to reduce the size of the archive.

* Ask the IT team of your institution or organisation about available services for data transfer. Usually, for **small data volume or limited number of files** universities and professional organisations can provide:
    * Secure server- or cloud-based applications where you should store work-related data files, synchronise files from different computers and share files by sending a link for access or download. This solution is ideal in case of a small number of files, since files need to be downloaded one by one and this can be inconvenient. Examples of these kinds of applications are NextCloud, {% tool "box" %}, {% tool "owncloud" %} (see [Data storage page](storage)).
    * Access to Office 365 (Software as a Service, or SaaS) that includes cloud storage on {% tool "microsoft-onedrive" %}, and SharePoint for collaborations and files sharing - you can “transfer” your data with these services by generating and sending a link for access or download of specific files.
    * Cloud synchronisation and sharing services (CS3) for that can be used in science, education and research have been implemented by companies (e.g. {% tool "seafile" %}), institutions such as CERN (e.g. {% tool "reva" %}, {% tool "rucio" %}) and initiatives (e.g. {% tool "sciencemesh" %}).

* Usually, universities and institutions strongly **discourage** the use of personal accounts on {% tool "google-drive" %}, Amazon Drive, {% tool "dropbox" %} and similar, to share and transfer work related data, and especially sensitive or personal data. Moreover, it is not allowed to store human data in clouds which are not hosted in the EU.

* Institutions and professional organisations could also make use of Infrastructure as a Service (IaaS), such as {% tool "microsoft-azure" %}, {% tool "amazon-web-services" %} (Amazon Simple Storage Service or S3), Oracle Cloud Infrastructure or Google Cloud Platform.

* A useful [comparison of cloud-computing software and providers](https://en.wikipedia.org/wiki/Cloud-computing_comparison ) is on Wikipedia. Cloud-computing infrastructures, services and platforms offer a variety of file hosting services; a [comparison of file hosting services](https://en.wikipedia.org/wiki/Comparison_of_file_hosting_services ) is available on Wikipedia.

* If you are considering transferring data from or to cloud-based services ({% tool "microsoft-azure" %} or Amazon S3) by shipping hard disks through carrier services, it is useful to know that services such as Amazon Snowball and Azure Data Box Disk will help you with the shipping of hard disks or appliances through carrier services.

* Countries could provide national file sender services (browser based or other) which could be useful for one time transfer of data files, limited in number and volume (for instance, up to 100 GB or 250 GB), from person to person. Importantly, an academic account is usually needed to use these kinds of services, therefore contact the IT team in your institute for more information.

* If you have the technical skills and the knowledge, you can use the most common data transfer protocols. These protocols are useful for data volume **larger than 50GB or for hundreds of data files**.
    * Applications suitable for small to mid size data available on any operating system and that can be used either through command-line (directly or with tools like {% tool "curl" %}) or through a graphical interface, are:
        * FTP (File Transfer Protocol) will transfer files between a client and an FTP server, which will require an account in order to transfer the files.
        * Be sure to use a **secure** version of this protocol, such as FTPS or SFTP (SSH File Transfer Protocol). A possible tool with graphical interface is {% tool "filezilla" %}.
        * HTTP (HyperText Transfer Protocol).
        * Rsync (remote synchronisation) can be used to transfer files between two computers and to keep the files synchronised between these two computers.
        * SCP (secure copy protocol) will securely transfer files between a client and a server. It will require an account on the server and can use SSH key based authentication. A possible tool with graphical interface is {% tool "winscp" %}.

    * For massive amounts of data, additional protocols have been developed, parallelizing the flow of data. These transfer solutions require specific tools and as such they are available mostly on large computational centres.
        * FASP protocol implemented in {% tool "ibm-aspera" %}.
        * GridFTP protocol used by {% tool "globus" %}.

* Several algorithms can be used for checksum calculation.
  * MD5 checksums can be generated and verified in command line of all operational systems or throught tools with a graphical interface, e.g. [MD5Summer](http://www.md5summer.org/) for Windows.
  * SHA-2 set is more secured but slower than MD5. SHA checksums can also be generated and verified in command line of all operational systems.
