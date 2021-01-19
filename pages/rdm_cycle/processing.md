---
title: Processing
keywords:
contributors: [Rob Hooft]
---

## What is Data Processing?

Data processing is the phase in a project where data is prepared for analysis.

When data has freshly been collected the data processing can contain some automated steps in a workflow that performs format conversion changes, and preprocessing that is always done in exactly the same way.

Especially when data is imported from elsewhere, e.g. data that is to be reused from another project, processing can also include manual steps to make data suitable for analysis, such as
 * Making changes in data formats to make different data sets that will be integrated compatible with each other
 * Changing coding systems or ontologies for the data to bring everything to the same level
 * Filtering data so that only data that is suitable for the project remains.

 After data processing, data is readied for analysis, and should therefore be available to the members of the project team that need to perform that step.

## Why is Data Processing important?

Data processing is important to ensure the good quality of the collected data and to prepare for the appropriate data analysis. An accurate documentation of every step done during data processing is key for the reproducibility of your result.

## What should be considered for Data Processing

The following considerations are important for data processing:

* Does data need to be pseudonymized / anonymized? Not only by removing directly identifying data, but also e.g. names are sometimes visible in images.
* Are there standards for the encoding of different data fields?
* Is the data properly documented?
    * Are encoding choices documented?
    * Is there a special significance to empty or otherwise special data fields? And is that made explicit?
    * Are all relationships between data fields explicit (e.g. if a dataset contains "medication" and "disease", is that medication actually used to treat the disease? Or is it e.g. medication that the patient is using for other reasons?)

## Where can training materials and events about Data Processing be found?

{% include tess.html search="Data Processing" %}

## Related topics

{% include pagelist.html tag="process" %}


<!--## External links
missing content -->
