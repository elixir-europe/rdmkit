---
title: Data transfer
contributors: [Olivier Collin, Alan R Williams, Flora D'Anna, Frederik Delaere, Munazah Andrabi]
tags: [preserve, share, reuse, IT support, data manager]
description: how to transfer data files.
page_tag: transfer
---

## How do you transfer large data files?

### Description

Often, research in Life Sciences generates massive amounts of digital data, such as output files of ‘omics’ techniques (genomics, transcriptomics, metabolomics, proteomics, etc). Large data files cannot be sent by email because they exceed the file size limit of most common email servers. So, how can large data files be transferred from a local computer to a distant one?

### Considerations

There are many aspects to consider when dealing with data transfer.

* The **size or volume** of the data and the **capacity or bandwidth of the network** that links your local computer with the distant computer are crucial aspects. Data size and bandwidth are tightly linked since transferring large volumes of data on a low bandwidth network will be so time consuming that it could be simpler to send the data on a hard drive through carrier services.

* Data **security**. If you intend to transfer sensitive data to another location, you have to check the regulation and security measures on the remote site. You can interact with the IT departments at both locations in order to establish your strategy. Do not forget to check the [Human Data](human_data) pages of the RDMkit.

* If you have the technical skills and knowledge, consider using appropriate File Transfer Protocols.

* Consider using Cloud Storage Services (see Data Storage page), that provide data sharing solutions, or specialised data transfer services available in your institute or country.

* Consider pros and cons of transferring data by shipping hard disks through carrier services (time, costs, security). This is not a recommended method, unless good internet connection is not available.

* Since data transfer involves so many technical aspects, it is a good idea to interact with your technical/IT team in order to avoid any problem if you want to transfer large amounts of data.

### Solutions

* Try to optimise and ease your data transfer by archiving your data in a single file. This can be done with two tools available on most systems.
    * tar (tape archive) will create an archive, a single file containing several files or directories.
    * gzip: since tar does not compress the archive created, a compression tool such as gzip is often used to reduce the size of the archive.

* Ask the IT team of your institution or organisation about available services for data transfer. Usually, for **small data volume or limited number of files** universities and professional organisations can provide:
    * Secure server- or cloud-based applications where you should store work-related data files, synchronize files from different computers and share files by sending a link for access or download. This solution is ideal in case of a small number of files, since files need to be downloaded one by one and this can be inconvenient. Examples of these kinds of applications are NextCloud, Box, OwnCloud (see Data storage page).
    * Access to Office 365 (Software as a Service, or SaaS) which include cloud storage on OneDrive and SharePoint for collaborations and files sharing. You can “transfer” your data with these services by generating and sending a link for access or download of specific files.

* Usually, universities and institutions strongly **discourage** the use of personal accounts on Google Drive, Amazon Drive, Dropbox and similar, to share and transfer work related data, and especially sensitive or personal data. Moreover, it is not allowed to store human data in clouds which are not hosted in the EU.

* Institutions and professional organisations could also make use of Infrastructure as a Service (IaaS), such as Microsoft Windows Azure, Amazon Web Services (Amazon Simple Storage Service or S3), Oracle Cloud Infrastructure or Google Cloud Platform.

* A useful [comparison of cloud-computing software and providers](https://en.wikipedia.org/wiki/Cloud-computing_comparison ) is on Wikipedia. Cloud-computing infrastructures, services and platforms offer a variety of file hosting services; a [comparison of file hosting services](https://en.wikipedia.org/wiki/Comparison_of_file_hosting_services ) is available on Wikipedia.

* If you are considering transferring data from or to cloud-based services (Microsoft Azure or Amazon S3) by shipping hard disks through carrier services, it is useful to know that services such as Amazon Snowball and Azure Data Box Disk will help you with the shipping of hard disks or appliances through carrier services.

* Countries could provide national file sender services (browser based or other) which could be useful for one time transfer of data files, limited in number and volume (for instance, up to 100 GB or 250 GB), from person to person. Importantly, an academic account is usually needed to use these kinds of services, so ask the IT team in your institute for more information.

* If you have the technical skills and the knowledge, you can use the most common data transfer protocols. These protocols are useful for data volume **bigger than 50GB or for hundreds of data files**.
    * Applications suitable for small to mid size data available on any operating system and that can be used either through command-line (directly or with tools like [cURL](https://curl.se)) or through a graphical interface, are:
        * FTP (File Transfer Protocol) will transfer files between a client and an FTP server, which will require an account in order to transfer the files.
        * Be sure to use a **secure** version of this protocol, such as FTPS or SFTP (SSH File Transfer Protocol). 
        * HTTP (HyperText Transfer Protocol)
        * Rsync (remote synchronization): can be used to transfer files between two computers and to keep the files synchronized between these two computers.
        * SCP (secure copy): SCP will securely transfer files between a client and a server. It will require an account on the server and can use SSH key based authentication.  

    * For massive amounts of data, additional protocols have been developed, parallelizing the flow of data. These transfer solutions require commercial licences for your site and as such they are available mostly on large computational centres.
        * [Aspera Fasp](https://www.ibm.com/products/aspera)
        * GridFTP and [Globus](https://www.globus.org)

    * Data Transfer Protocols with a graphical user interface are:  
        * [FileZilla](https://filezilla-project.org)
        * [WinSCP](https://winscp.net/eng/index.php)


* When using data transfer protocol, make sure to check the transfer. During the transfer some data might become corrupted, thus it is important to check if the files you transfered have conserved their integrity. This can be done with hash algorithms. A checkshum file is calculated for each file before transfer and compared to a checksum calculated on the transferred files. If the checksums are the same, the files are not corrupted.
    * md5
    * SHA

<!-- ## Related topics
(Optional section)
* Bullet point list of other pages in this website that are connected to this lifecycle stage -->
