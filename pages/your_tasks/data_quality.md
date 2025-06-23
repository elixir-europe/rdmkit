---
title: Data quality
contributors: [Wei Gu, Pinar Alper, Kees van Bochove]
description: How to ensure high quality of research data.
page_id: data_quality
related_pages: 
    tool_assembly: []
dsw:
- name: Will you monitor data integrity once it has been collected?
  uuid: 02b3fed1-0b50-4a80-b8b6-a225a1107022
- name: Will you be using quality processes?
  uuid: ba38b16d-2154-4372-b445-7854a6e90443
faircookbook:
- name: Introducing Provenance Information
  url: https://w3id.org/faircookbook/FCB036
---

## How do you ensure the quality of research data?

### Description

Data quality is a term that can be understood in many ways. In enterprise context, it often refers to master data management as defined by the [ISO 8000](https://www.iso.org/standard/50798.html) standards. In science, the quality of data is closely linked to the suitability of the data for (re)use for a particular purpose and it is a key attribute of research data. Data quality affects the reliability of research results and it is a key factor increasing the reusability of data for secondary research. Data quality control can take place at any stage during the research data lifecycle. That said, you should ensure that the necessary procedures are defined during data management planning.

### Considerations

Quality control is most typically performed during data collection but it should not be neglected in later stages of research data lifecycle. The type of data as well as instruments and processes adopted for data collection in your research will determine the quality assurance measures you can take.
Examples of such measures are:

* setup data management working group (DMWG) that includes people who generate data, analyse data and data managers;
* for data collection: DMWG to plan and define data dictionary (including validation rules) before collecting data;
* for metadata collection: DMWG to plan and define metadata data templates;
* use electronic data capture systems;
* automated quality monitoring through tools, pipelines, dashboards;
* training of study participants and researchers, surveyors or other staff involved;
* adopting standards;
* instrument calibrations;
* repeated samples;
* post collection data curation;
* data peer-review.

Certain areas such as clinical studies, or those involving Next Generation Sequencing have commonly working methods to ensure data quality. Consider familiarizing yourself with data quality standards or established working practices in your field of study.

There are many frameworks proposed in the literature to define and evaluate overall data quality, such as:

* the four data quality dimensions (Accuracy, Relevancy, Representation, Accessibility) by [Wang](http://www.jstor.org/stable/40398176?origin=JSTOR-pdf);
* the five C’s of [Sherman](https://doi.org/10.1016/C2012-0-06937-2) (Clean, Consistent, Conformed, Current and Comprehensive), and the three categories from [Kahn](https://dx.doi.org/10.13063/2327-9214.1244) (Conformance, Completeness and Plausibility), for electronic health data. Kahn also proposes two different modes to evaluate these components:
  * verification (focusing on the intrinsic consistency, such as adherence to a format or specified value range);
  * validation (focusing on the alignment of values with respect to external benchmarks).

For health data, a nice example of working out what data quality means can be found in the {% tool "ohdsi" %} community. The context in this case is observational healthcare data represented in the {% tool "omop-cdm" %}.

### Solutions

* Electronic data capturing system: {% tool "redcap" %} allows you to design electronic data capture forms and allows you to monitor the quality of data collected via those forms.
* The World Bank provides [quality assurance guidance](https://dimewiki.worldbank.org/wiki/Data_Quality_Assurance_Plan) for survey design and execution.
* The U.S. National Institute's of Health's provides [introductory training material](https://oir.nih.gov/sites/default/files/uploads/sourcebook/documents/ethical_conduct/data_quality_management-2015_05_15.pdf) on data quality.
* Bio.tools' listing for [computational tools and pipelines for data quality control in life sciences](https://bio.tools/t?page=1&q=quality&sort=score).
* Data integration tools that include pre-defined building blocks to monitor and check data quality, such as [Pentaho Community Edition (CE)](https://pentaho-public.atlassian.net/wiki/spaces/COM/overview), [Talend Open Studio](https://sourceforge.net/projects/talend-studio/).
* Data curation tools such as {% tool "openrefine" %} that help you to identify quality issues, correct (curate) them, carry out transformations in the collected data with easy-to-use graphic interface and visualisation. It also documents all the steps during the curation for reproducibility and backtracking.

* For heath data, the [Book of OHDSI](http://book.ohdsi.org) has several [chapters](https://ohdsi.github.io/TheBookOfOhdsi/EvidenceQuality.html) on methods for assessing the data quality of observational health datasets, split out by data quality, clinical validity, software validity and method validity. Frameworks proposed in the literature, to define and evaluate overall data quality, could be used to create computational representations of the data quality of a dataset. [OHDSI DataQualityDashboard](https://github.com/OHDSI/DataQualityDashboard), which leverages the Kahn framework referenced above (adapted from [original thehyve.nl blogpost](https://www.thehyve.nl/articles/fair-data-for-machine-learning)), is a software framework for assessing the quality and suitability of routinely generated healthcare data that is represented in the {% tool "omop-cdm" %}.
