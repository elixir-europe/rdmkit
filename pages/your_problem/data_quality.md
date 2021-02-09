---
title: Data quality
keywords: [collecting]
contributors: [Wei Gu, Pinar Alper]
tags: [collect, process, researcher, data manager]
---

## How can research data quality be ensured?

### Description

Quality is a key attribute of research data. Data quality affects the reliability of research results and it is a key factor increasing the reusability of data for secondary research. Data quality control can take place at any stage during the research data lifecycle. That said, you should ensure that the necessary procedures are defined during data management planning. 


### Considerations

  * What is your data collection mechanism? Quality control is most typically performed during data collection. The elements of data collection in your research will determine the quality measures you can take.
Examples of such measures are:
      * setup data management working group (DMWG) that includes people who generate data, analyse data and data managers,
      * for data collection: DMWG to plan and define data dictionary (including validation rules) before collecting data,
      * for metadata collection: DMWG to plan and define metadata data templates,
      * use electronic data capture systems,
      * automated quality monitoring through tools, pipelines, dashboards,
      * training of study participants and researchers, surveyors or other staff involved,
      * adopting standards,
      * instrument calibrations, 
      * repeated samples, 
      * post collection data curation, 
      * data peer-review.
  
  * Are there standards or established working practices for quality in your field of study? Certain areas such as clinical studies, or those involving Next Generation Sequencing have commonly working methods to ensure data quality.
  

### Solutions

  * Electronic data capturing system: [REDCap](https://www.project-redcap.org) allows you to design electronic data capture forms and allows you to monitor the quality of data collected via those forms.
  * An example of [data dictionary](https://webdav-r3lab.uni.lu/public/elixir/templates/Data_dictionary_example.xlsx) illustrating the elements and factors that should be defined for the variable needed by data collection.
  * The World Bank provides [quality assurance guidance](https://dimewiki.worldbank.org/wiki/Data_Quality_Assurance_Plan) for survey design and execution.
  * The U.S. National Institute's of Health's provides [introductory training material](https://oir.nih.gov/sites/default/files/uploads/sourcebook/documents/ethical_conduct/data_quality_management-2015_05_15.pdf) on data quality.
  * Bio.tools' listing for [computational tools and pipelines for data quality control in life sciences](https://bio.tools/t?page=1&q=quality&sort=score).
  * Data integration tools that include pre-defined building blocks to monitor and check data quality, such as [Pentaho Community Edition (CE)](https://wiki.pentaho.com/display/COM/Community+Edition+Downloads?desktop=true&macroName=ul), [Talend Open Studio](https://sourceforge.net/projects/talend-studio/).
  * Data curation tools such as [OpenRefine](https://openrefine.org/) that help you to identify quality issues, correct (curate) them, carry out transformations in the collected data with easy-to-use graphic interface and visualisation. It also documents all the steps during the curation for reproducibility and backtracking. 

## Relevant tools and resources

{% include toollist.html tag="data quality" %}
