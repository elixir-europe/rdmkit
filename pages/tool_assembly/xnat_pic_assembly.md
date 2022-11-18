---
title: XNAT-PIC
contributors: [Sara Zullino, Alessandro Paglialonga, Walter Dastrù, Dario Longo, Silvio Aime]
page_id: XNAT-PIC
affiliations: [Euro BioImaging, IT]
related_pages: 
  your_tasks: [data organisation, storage, data analysis]
  your_domain: []
description: XNAT for Preclinical Imaging Centers (XNAT-PIC) is a of set of tools to store, process and share preclinical imaging studies built on top of the XNAT imaging informatics platform.
training:
  - name: EOSC-Life website
    url: https://www.eosc-life.eu/d5/
  - name: Euro-Bioimaging website
    url: https://www.eurobioimaging.eu/news/towards-sharing-and-reusing-of-preclinical-image-data
  - name: Data Management - Biological and Preclinical Imaging Perspective
    registry: YouTube
    url: https://www.youtube.com/QNiAGuFk53w
  - name: XNAT-PIC - expanding XNAT for image archiving and processing to Preclinical Imaging Centers
    registry: YouTube
    url: ttps://www.youtube.com/cpEcfIJJqCo
---

## Summary

Preclinical imaging centers deal with many challenges mostly related to the variety of imaging instrumentation yielding huge volumes of raw data. The current procedures to collect, share and reuse preclinical image data are insufficient, thus revealing an urgent need of standardization in terms of data storage and image processing. **XNAT for Preclinical Imaging Centers (XNAT-PIC)** has been developed to overcome this limitation by extending XNAT’s basic functionalities to meet the needs of preclinical imaging facilities. 

## What is XNAT-PIC?

**XNAT for Preclinical Imaging Centers (XNAT-PIC)** consists of a set of tools built in Python and MATLAB to [store](storage), [process](processing) and [share](sharing) preclinical imaging studies built on top of the [XNAT](https://www.xnat.org/) imaging informatics platform.
 
## Who is XNAT-PIC intended for?

XNAT-PIC is inteded for scientists, researchers and data stewards working in the preclinical and biomedical imaging field to support image data management and processing.

## Which task can be solved with XNAT-PIC?

XNAT-PIC is a set of tools to support preclinical imaging scientists in their data management and processing needs. 
The Extensible Neuroimaging Archive Toolkit [XNAT](https://www.xnat.org/) is an imaging informatics platform developed by the Neuroinformatics Research Group at the Washington University for the management, storage and analysis of biomedical image data. XNAT is an open-source project that can support a wide range of imaging modalities thanks to its extensibility.

XNAT-PIC consists of:

{% include image.html file="xnat-pic.png" caption="Schematic overview of the XNAT-PIC tool assembly." alt="Schematic overview of the XNAT-PIC tool assembly." %}


1. **MRI2DICOM** [processes](processing) Magnetic Resonance (MR) images and convert them from ParaVision® (Bruker, Inc. Billerica, MA) file format to DICOM standard

2. **XNAT-PIC Uploader** to import and [store](storage) multimodal DICOM image datasets to XNAT

3. **XNAT-PIC Pipelines** for [analysing](analysing) single or multiple subjects within the same project in XNAT.


## Citation

If you use **XNAT-PIC** please cite: <br>

* S. Zullino, A. Paglialonga, W. Dastrù, D. L. Longo, S. Aime. XNAT-PIC: Extending XNAT to Preclinical Imaging Centers, 2021. Pre-print: https://arxiv.org/abs/2103.02044

