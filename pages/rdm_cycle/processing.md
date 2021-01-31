---
title: Processing
keywords: [data cleaning, data formatting, quality check, data validation]
contributors: [Rob Hooft, Munazah Andrabi]
---

## What is data processing?

Data processing is the phase in the project where data is converted into a desired format and prepared for analysis. When data has been freshly collected, data processing includes some automated steps in a workflow that perform format conversion, quality check and preprocessing following a standardised protocol. The main aim of processing is to:
 * Convert data into readable format giving it the shape and form necessary for downstream analysis. 
 * Discard bad or low quality data in order to create clean, high-quality dataset for reliable results.

When data is imported from existing sources, e.g. data to be reused from another project, processing can also include manual steps to make it suitable for analysis. These steps include but are not limited to:
 * Making changes to data formats such that different datasets will be compatible for integration with each other.
 * Changing coding systems or ontologies for the data to bring everything to the same level.
 * Filtering data such that only data suitable for the project is retained.

 After data processing, clean data is ready for analysis and should therefore be available to the members of the project team that need to perform the next steps.

## Why is data processing important?

Data processing is important to ensure good quality of the collected data and to prepare it for meaningful data analysis. Accurate data processing is also essential for combining two or more datasets into a single dataset. An accurate documentation of every step done during data processing is key for the reproducibility of your result. Processing data correctly makes it easy to arrange, analyse and also saves a lot of space.

## What should be considered for data processing?

The following considerations are important for data processing:

* Sensitive data should be Pseudonymised/anonymised. Not only should you remove the directly identifying data, but also be attentive to other sources e.g. names written on images.
* Appropriate standards for encoding different data fields should be used.
* All steps of anonymisation and encoding should be properly documented, For e.g.
    * The chosen encoding formats used for data fieds should be documented.
    * The special significance of empty or otherwise special data fields.
    * All relationships between data fields should be made explicit (e.g. if a dataset contains "medication" and "disease", is that medication actually used to treat the disease? Or is it a medication that the patient is using for other reasons?).

## Problems to be addressed at this stage

{% include pagelist.html tag="process" %}

## Where can training materials and events about data processing be found?

{% include tess.html search="Data Processing" %}
<!--## External links
missing content -->
