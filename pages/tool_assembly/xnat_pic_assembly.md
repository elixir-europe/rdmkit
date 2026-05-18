---
title: XNAT-PIC
contributors: [Sara Zullino, Alessandro Paglialonga, Walter Dastrù, Dario Longo, Silvio Aime]
page_id: xnat_pic
affiliations: [Euro BioImaging, IT]
related_pages: 
  Your_tasks: [data_organisation, storage, data_analysis]
  Your_domain: []
description: XNAT for Preclinical Imaging Centers (XNAT-PIC) is a of set of tools to store, process and share preclinical imaging studies built on top of the XNAT imaging informatics platform.
training:
  - name: EOSC-Life website
    url: https://www.eosc-life.eu/d5/
  - name: Euro-Bioimaging website
    url: https://www.eurobioimaging.eu/news/towards-sharing-and-reusing-of-preclinical-image-data
  - name: Data Management - Biological and Preclinical Imaging Perspective
    registry: YouTube
    url: https://www.youtube.com/watch?v=QNiAGuFk53w
  - name: XNAT-PIC - expanding XNAT for image archiving and processing to Preclinical Imaging Centers
    registry: YouTube
    url: ttps://www.youtube.com/cpEcfIJJqCo
---

## What is XNAT-PIC?

Preclinical imaging centers deal with many challenges mostly related to the variety of imaging instrumentation yielding huge volumes of raw data. The current procedures to collect, share and reuse preclinical image data are insufficient, thus revealing an urgent need of standardisation in terms of data storage and image processing. **{% tool "xnat" %} for Preclinical Imaging Centers (XNAT-PIC)** has been developed to overcome this limitation by extending XNAT’s basic functionalities to meet the needs of preclinical imaging facilities.

**XNAT for Preclinical Imaging Centers (XNAT-PIC)** consists of a set of tools built in Python and MATLAB to [store](storage), [process](processing) and [share](sharing) preclinical imaging studies built on top of the {% tool "xnat" %} imaging informatics platform.
 
## Who is XNAT-PIC intended for?

XNAT-PIC is inteded for scientists, researchers and data stewards working in the preclinical and biomedical imaging field to support image data management and processing.

## Which task can be solved with XNAT-PIC?

XNAT-PIC is a set of tools to support preclinical imaging scientists in their data management and processing needs. 
The Extensible Neuroimaging Archive Toolkit {% tool "xnat" %} is an imaging informatics platform developed by the Neuroinformatics Research Group at the Washington University for the management, storage and analysis of biomedical image data. XNAT is an open-source project that can support a wide range of imaging modalities thanks to its extensibility.

{% include image.html file="xnat-pic.png" caption="Figure 1. Schematic overview of the XNAT-PIC tool assembly." alt="Schematic overview of the XNAT-PIC tool assembly." %}

XNAT-PIC consists of:

* {% tool "mri2dicom" %} to [process](processing) Magnetic Resonance (MR) images and convert them from ParaVision® (Bruker, Inc. Billerica, MA) file format to DICOM standard;
* {% tool "xnat-pic-uploader" %} to import and [store](storage) multimodal DICOM image datasets to XNAT;
* {% tool "xnat-pic-pipelines" %} for [analysing](analysing) single or multiple subjects within the same project in XNAT.

## Citation

If you use **XNAT-PIC** please cite: <br>

* S. Zullino, A. Paglialonga, W. Dastrù, D. L. Longo, S. Aime. XNAT-PIC: Extending XNAT to Preclinical Imaging Centers, 2021. Pre-print: https://arxiv.org/abs/2103.02044
