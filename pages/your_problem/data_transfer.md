---
title: Data transfer
keywords:
tags: [preserve, share, reuse, IT support, data manager] 
---

## How to transfer large data files?

### Description

Large data files cannot be sent by email because they exceed the file size limit of most common email servers. So, how can large data files be transfered from a local computer to a distant one?

### Considerations

There are many aspects to consider when dealing with data transfer, but the most important are:  

* the data size  
* the capacity or bandwidth of the network links between your local computer and the distant computer
* data security

Data size and bandwidth are tightly linked since transferring large volumes of data on a low bandwidth network will be so time consuming that it could be simpler to send the data on a hard drive through carrier services. 


If you intend to transfer sensitive data to another location, you have to check the regulation and security measures on the remote site. You can interact with the IT departments at both locations in order to establish your strategy. Do not forget to check the [Human Data](human_data) pages of the RDMKit. 


Since data transfer involves so many technical aspects, it is a good idea to interact with your technical/IT team in order to avoid any problem if you want to transfer large amounts of data.

### Solutions

#### Step 1: Optimize data transfer
It can be very useful to archive your data in a single file to optimize and ease the data transfer. This can be done with two tools available on most systems.

* tar (tape archive) will create an archive, a single file containing several files or directories. 
* gzip: since tar does not compress the archive created, a compression tool such as gzip is often used to reduce the size of the archive. 

#### Step 2: Choose an appropriate data transfer protocol or application

The most common data transfer applications available are:

* FTP (File Transfer Protocol): *Be sure to use a secure version of this protocol, such as FTPS or SFTP (SSH File Transfer Protocol)*. FTP will transfer files between a client and an FTP server, which will require an account in order to transfer the files. 
* HTTP (HyperText Transfer Protocol): 
* Rsync (remote synchronization): can be used to transfer files between two computers and to keep the files synchronized between these two computers. 
* SCP (secure copy): SCP will securely transfer files between a client and a server. It will require an account on the server and can use SSH key based authentication.  

These applications are suitable for small to mid size data. These applications are available on any operating system and can be used either through command-line (directly or with tools like cURL) or through a graphical interface. 

For massive amounts of data, additional protocols have been developed, parallelizing the flow of data. 

* Aspera Fasp
* GridFTP and Globus 

These transfer solutions require commercial licences for your site and as such they are available mostly on large computational centres. 

#### Step 3: Check the transfer

During the transfer some data might become corrupted, thus it is important to check if the files you transfered have conserved their integrity. This can be done with hash algorithms. A checkshum file is calculated for each file before transfer and compared to a checksum calculated on the transferred files. If the checksums are the same, the files are not corrupted. 

* md5
* SHA

<!-- ## Related topics
(Optional section)
* Bullet point list of other pages in this website that are connected to this lifecycle stage -->

<!-- ## External links
(Optional section)
* Bullet point list of external links to things that aren't included in any of the tools/resources/training sections above -->

## Relevant tools and resources

{% include toollist.html tag="transfer" %}
