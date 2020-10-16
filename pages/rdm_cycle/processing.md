---
title: Processing
keywords:
contributors: Rob Hooft
---

## What is data processing?

Data processing is the phase in a project where data is prepared for analysis.

When data has freshly been collected the data processing can contain some automated steps in a workflow that performs format conversion changes, and preprocessing that is always done in exactly the same way.

Especially when data is imported from elsewhere, e.g. data that is to be re-used from another project, processing can also include manual steps to make data suitale for analysis, such as
 * Making changes in data formats to make different data sets that will be integrated compatible with each other
 * Changing coding systems or ontologies for the data to bring everything to the same level
 * Filtering data so that only data that is suitable for the project remains.
 
 After data processing, data is readied for analysis, and should therefore be available to the members of the project team that need to perform that step.

## Why is data processing important?

Some text

## What should be considered for data processing

The following considerations are important for data processing:

* Does data need to be pseudonymized / anonymized? Not only be removing directly identifying data, but also e.g. names are sometimes visible in images.
* Are there standards for the encoding of different data fields?
* Is the data properly documented?
    * Are encoding choices documented?
    * Is there a special significance to empty or otherwise special data fields? And is that made explicit?
    * Are all relationships between data fields explicit (e.g. if a dataset contains "medication" and "disease", is that medication actually used to treat the disease? Or is it e.g. medication that the patient is using for other reasons?)

## What tools and resources are available for Data Processing?

{% include toollist.html tag="process" %}

## Where can training materials and events about Data Management Planning be found?

## Related topics

* [Data Storage](https://rdm.elixir-europe.org/storage)

## External links

