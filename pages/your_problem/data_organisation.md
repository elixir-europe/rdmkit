---
title: Data organisation
keywords: [file naming, versioning, folder structures]
contributors: [Siiri Fuchs, Minna Ahokas, Yvonne Kallberg]
tags: [collect, process, analyse, preserve, researcher, IT support, data manager]
---

## What is the best way to name a file?
 
### Description

Brief and descriptive file names are important in keeping your data files organized. A file name is the principal identifier for a file and a good name gives information what the file contains and helps in sorting them, but only if you have been consistent with the naming.

### Considerations

* Best practice is to develop a file naming convention with elements that are important to your project already when the project starts.
* When working in collaboration with others, it is important to follow the same file naming convention.

### Solutions

#### Tips for naming files
* Balance with the amount of elements: too many makes it difficult to understand vs too few makes it general.
* Order the elements from general to specific.
* Use meaningful abbreviations.
* Use underscore (_), hypen (- ) or capitalized letters to separate elements in the name. Don’t use spaces or special characters: ?!& , * % # ; * ( ) @$ ^ ~ ‘ { } [ ] < >.
* Use date format ISO8601: YYYYMMDD, and time if needed HHMMSS.
* Include a version number if appropriate: minimum two digits (V02) and extend it, if needed for minor corrections (V02-03). The leading zeros, will ensure the files are sorted correctly. 
* Write your file naming convention down and explain abbreviations in your data documentation.
* If you need to rename a lot files in order to organize your project data and manage the files easier, it is possible use applications e.g. [Bulk Rename Utility](https://www.bulkrenameutility.co.uk/) (Windows, free), [Renamer4Mac](https://renamer.com/) (Mac). 

#### Example elements to include in the name
* Date of creation
* Project number / Experiment / Acronym
* Type of data (Sample ID, Analysis, Conditions, Modifications etc.)
* Location / Coordinates
* Name / Initials of the creator
* Version number
* Reserve the last 3-letters for file format (e.g. .xls, .rtf, .mov, .tif, .doc)

**Examples of good file names**
* Honeybee project, experiment 2 done in Helsinki, data file created on the second of December 2020
  * File name: 20201202_HB_EXP2_HEL_DATA_V03.xls
  * Explanation: Time_Project abbreviation_ Experiment number _Location_Type of data_Version number
* Cropped image of an ant head taken on the third of December 2020 by Meg Megson
  * 20201203_MM_HEAD_CROPPED_V1.psd
  * Explanation: Time_creator_data type_modification_version

## How to manage file versioning?

### Description
File versioning is a way to keep track of changes made to files and datasets. While the implementation of a good file naming convention will indicate that different versions exist, this will not explain the difference between two (or more) versions. File versioning will enable transparency on which actions and changes were made when, and it will be easier to backtrack and find something that was present in a previous version, but which has later been deleted or changed.

### Considerations
* Do you need to collaborate on files, perhaps at the same time?
* Is there a need to be able to backtrack and restore a previous version?
* Will there be many changes made?

### Solutions
* Smaller demands of versioning can be managed manually e.g. by keeping a log where the changes for each respective file is documented, version by version.
* For automatic management of versioning, conflict resolution and back-tracing capabilities, use a proper version control software such as [Git](https://git-scm.com/), hosted by e.g. [GitHub](https://github.com/) and [BitBucket](https://bitbucket.org/).


## How to organise files in a folder structure?

### Description
A carefully planned folder structure, with intelligible folder names and an intuitive design, is the foundation for good data organisation. The folder structure gives an overview of which information can be found where, enabling present as well as future stakeholders to understand what files have been produced in the project.

### Considerations
* The decisions on how to organise the files should be made during planning and design of the project, so that the strategy can be implemented already from the start.
* Consider to consistently apply the same strategy in every project within the research group.

### Solutions
Folders should:
* follow a structure with folders and subfolders that correspond to the project design and workflow
* have a self-explanatory name that is only as long as is necessary
* have a unique name – avoid assigning the same name to a folder and a subfolder

The top folder should have a README.txt file describing the folder structure and what files are contained within the folders. This file should also contain explanation of the file naming convention.

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
      
<!--- ## Related topics
(Optional section)
* Bullet point list of other pages in this website that are connected to this lifecycle stage -->

## External links
* '[A Quick Guide to Organizing Computational Biology Projects](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)' provides further best-practice suggestions on data organisation.

## Relevant tools and resources

{% include toollist.html tag="data organisation" %}
