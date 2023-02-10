---
title: Processing
page_id: process
description: Introduction to data processing.
contributors: [Rob Hooft, Munazah Andrabi]
related_pages: 
  your_tasks: [data_analysis, data_organisation, data_quality, data_provenance]
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=%22data+process%22#materials
dsw:
- name: List the data formats you will be using for interpretation and describe their
    structure
  uuid: a797cab9-0829-4787-a096-1b5cedc9147f
- name: How will you work with your data?
  uuid: df36fb68-131c-4f31-a42b-684abf523bbc
---

## What is data processing?

Data processing is the phase in the project where data is converted into a desired format and prepared for analysis. When data has been freshly collected, data processing includes some automated steps in a workflow that perform format conversion, quality check and preprocessing following a standardised protocol. The main aim of processing is to:
 * convert data into readable format giving it the shape and form necessary for downstream analysis;
 * discard bad or low quality data in order to create clean, high-quality dataset for reliable results.

When data is imported from existing sources, e.g. data to be reused from another project, processing can also include manual steps to make it suitable for analysis. These steps include but are not limited to:
 * making changes to data formats such that different datasets will be compatible for integration with each other;
 * changing coding systems or ontologies for the data to bring everything to the same level;
 * filtering data such that only data suitable for the project is retained.

 After data processing, clean data is ready for analysis and should therefore be available to the members of the project team that need to perform the next steps.

## Why is data processing important?

Data processing is important to ensure good quality of the collected data and to prepare it for meaningful data analysis. Accurate data processing is also essential for combining two or more datasets into a single dataset. An accurate documentation of every step done during data processing is key for the reproducibility of your result. Processing data correctly makes it easy to arrange, analyse and also saves a lot of space.

## What should be considered for data processing?

The following considerations are important for data processing:

* sensitive data should be pseudonymised/anonymised. Not only should you remove the directly identifying data, but also be attentive to other sources e.g. names written on images;
* appropriate standards for encoding different data fields should be used;
* all steps of encoding and anonymisation should be properly documented. E.g. consider recording:
    * encoding formats used for data fields;
    * significance of empty fields and meaning of any special value;
    * all relationships between data fields (e.g. if a dataset contains "medication" and "disease", is that medication actually used to treat the disease? Or is it a medication that the patient is using for other reasons?).
