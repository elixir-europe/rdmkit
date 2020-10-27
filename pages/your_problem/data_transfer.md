---
title: Data Transfer
keywords:
tags: [research_it] 
---

## Considerations about data transfer

There are many aspects to consider when dealing with data transfer, but the most important are :  

* the data size  
* the network links between your local computer and the distant computer 

These parameters are tightly linked since transferring large volumes of data on a low bandwidth network will be so time consuming that it could be simpler to send the data on a hard drive through carrier services. 

Since data transfer involves so many technical aspects, it is a good idea to interact with your technical team in order to avoid any problem if you want to transfer large amounts of data. 



## Data transfer protocols and applications

The most common data transfer applications available are :

* FTP
* HTTP
* Rsync
* scp 

These applications are suitable for small to mid size data. These applications are available on any operating system. 

For massive amounts of data, additional protocols have been developed, parallelizing the flow of data. 

* Aspera Fasp
* GridFTP and Globus 

These transfer solutions require commercial licences for your site. 


## Optimizing data transfer 

It can be very useful to compress and archive your data in a single to optimize and ease the data transfer. 

* tar
* gzip 


## Checking the transfer

Since during the transfer some data might be corrupted it is important to check if the files you transfered have conserved their integrity. This can be done with hash algorithms. A checkshum file is calculated for each file before transfer and compared to a checksum calculated on the transferred files. If the checksums are the same, the files are not corrupted. 

* md5
* SHA 
