---
title: Data organisation
contributors: [Siiri Fuchs, Minna Ahokas, Yvonne Kallberg]
description: Best practices to name and organise research data.
page_id: data_organisation
related_pages: 
  tool_assembly: [ome, transmed, xnat-pic]
dsw:
- name: How will you do file naming and file organization?
  uuid: 8e886b55-3287-48e7-b353-daf6ab40f7d8
- name: Are you using a filesystem with files and folders?
  uuid: a12aa967-28a5-4a9b-8df8-f7c533205ea4
- name: Data storage systems and file naming conventions
  uuid: bc5e3dbf-2923-4025-a49a-f204b01d4018
faircookbook:
- name: Creating a data/variable dictionary
  url: https://w3id.org/faircookbook/FCB025
- name: Creating a metadata profile
  url: https://w3id.org/faircookbook/FCB026
- name: Extraction, transformation, and loading process
  url: https://w3id.org/faircookbook/FCB031
---

## What is the best way to name a file?

### Description

Brief and descriptive file names are important in keeping your data files organised. A file name is the principal identifier for a file and a good name gives information what the file contains and helps in sorting them, but only if you have been consistent with the naming.

### Considerations

* Best practice is to develop a file naming convention with elements that are important to your project already when the project starts.
* When working in collaboration with others, it is important to follow the same file naming convention.

### Solutions

#### Tips for naming files
* Balance with the amount of elements: too many makes it difficult to understand vs too few makes it general.
* Order the elements from general to specific.
* Use meaningful abbreviations.
* Use underscore (_), hyphen (- ) or capitalized letters to separate elements in the name. Don’t use spaces or special characters: ?!& , * % # ; * ( ) @$ ^ ~ ‘ { } [ ] < >.
* Use date format ISO8601: YYYYMMDD, and time if needed HHMMSS.
* Include a unique identifier (see: [Identifiers](identifiers))
* Include a version number if appropriate: minimum two digits (V02) and extend it, if needed for minor corrections (V02-03). The leading zeros, will ensure the files are sorted correctly.
* Write your file naming convention down and explain abbreviations in your data documentation.
* If you need to rename a lot of files in order to organize your project data and manage your files better, it is possible to use applications like [Bulk Rename Utility](https://www.bulkrenameutility.co.uk/) (Windows, free) and [Renamer4Mac](https://renamer.com/) (Mac).

#### Example elements to include in the file name
* Date of creation
* Project number / Experiment / Acronym
* Type of data (Sample ID, Analysis, Conditions, Modifications etc.)
* Location / Coordinates
* Name / Initials of the creator
* Version number
* Reserve the last 3-letters for file format (e.g. .xls, .rtf, .mov, .tif, .doc)

**Examples of good file names**
* Honeybee project, experiment 2 done in Helsinki, data file created on the second of December 2020
  * File name: `20201202_HB_EXP2_HEL_DATA_V03.xls`
  * Explanation: `Time_ProjectAbbreviation_ExperimentNumber_Location_TypeOfData_VersionNumber`
* Cropped image of an ant head taken on the third of December 2020 by Meg Megson
  * File name: `20201203_MM_HEAD_CROPPED_V1.psd`
  * Explanation: `Time_CreatorData_TypeModification_Version`

## How do you manage file versioning?

### Description
File versioning is a way to keep track of changes made to files and datasets. While the implementation of a good file naming convention will indicate that different versions exist, this will not explain the difference between two (or more) versions. File versioning will enable transparency about which actions and changes were made and when. This makes it easy to backtrack and find something that was present in a previous version, but was later deleted or changed.

### Considerations
* Do you need to collaborate on files, perhaps at the same time?
* Is there a need to be able to backtrack and restore a previous version?
* Will there be many changes made?

### Solutions
* Smaller demands of versioning can be managed manually e.g. by keeping a log where the changes for each respective file is documented, version by version.
* For automatic management of versioning, conflict resolution and back-tracing capabilities, use a proper version control software such as [Git](https://git-scm.com/), hosted by e.g. [GitHub](https://github.com/) and [BitBucket](https://bitbucket.org/).
* Use a Cloud Storage service (see [Data storage](storage#what-features-do-you-need-in-a-storage-solution-when-collecting-data) page) that provides automatic file versioning. It can be very handy for spreadsheets, text files and slides.


## How do you organise files in a folder structure?

### Description
A carefully planned folder structure, with intelligible folder names and an intuitive design, is the foundation for good data organisation. The folder structure gives an overview of which information can be found where, enabling present as well as future stakeholders to understand what files have been produced in the project.

### Considerations
* The decisions on how to organise the files should be made during planning and design of the project, so that the strategy can be implemented from the start.
* Consider to consistently apply the same strategy in every project within the research group.

### Solutions
Folders should:
* follow a structure with folders and subfolders that correspond to the project design and workflow
* have a self-explanatory name that is only as long as is necessary
* have a unique name – avoid assigning the same name to a folder and a subfolder

The top folder should have a README.txt file describing the folder structure and what files are contained within the folders. This file should also contain explanation of the file naming convention. See also [A Quick Guide to Organizing Computational Biology Projects](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424).

#### An example:

    project/  
      code/                 code needed to go from input files to final results   
      data/                 raw and primary data (never edit!)   
         raw_external/  
         raw_internal/
         meta/  
      doc/                  documentation of the study  
      intermediate/         output files from intermediate analysis steps  
      logs/                 logs from the different analysis steps  
      notebooks/            notebooks that document your day-to-day work  
      results/              output from workflows and analyses  
         figures/  
         reports/  
         tables/  
      scratch/              temporary files that can safely be deleted or lost  
      README.txt            file and folder description  

