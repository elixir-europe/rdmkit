---
title: Data analysis
contributors: [Olivier Collin]
tags: [analyse, process, reuse, researcher, IT support]
---

## What are the best practices for data analysis?
 
### Description

When carrying out your analysis, you should also keep in mind that all your data analysis has to be reproducible. This will complement your research data management approach since your data will be FAIR compliant but also your tools and analysis environments. In other words, you should be able to tell what data and what code or tools were used to generate your results.
This will help to tackle reproducibility problems but also will improve the impact of your research through collaborations with scientists who will reproduce your in silico experiments. 

### Considerations

There are many ways that will bring reproducibility to your data analysis. You can act at several levels:
* by providing your code
* by providing you execution environment
* by providing your workflows 
* by providing your data analysis execution

### Solutions

#### Code availability  

If you have to develop some software for your data analysis, it is always a good idea to publish your code. The git versioning system offers both a way to release your code but offers also a versioning system. You can also use Git to interact with your software users. 

Be sure to specify a license for your code (see the licensing section). 


#### Analysis environment reproducibility

To help others to reproduce your analysis on different infrastructures, you can act at several levels. 
By using package and environment management systems like Conda and its bioinformatics specialized channel Bioconda, you will be able to easily install specific versions of tools, even older ones, in an isolated environment. You can also manage your environment by specifying in a file which tools you need. 

You can combine the usage of Conda with virtual environments like Docker or Singularity. 


#### Workflows reproducibility 

Workflow management systems will help you to keep track and to document the different treatment applied to your data. 

There a many workflow management systems available. One can mention:
* Galaxy 
* Nextflow
* Snakemake 

It is a flourishing field and many other workflow management systems are available. 

#### Notebooks 

Using notebooks, you will be able to create reproducible documents mixing text and code. Notebooks can be used in conjunction with the other solutions mentioned above.
Among the most well-known notebooks systems are: 

* Jupyter
* RStudio


<!-- ## External links
(Optional section)
* Bullet point list of external links to things that aren't included in any of the tools/resources/training sections above -->

## Relevant tools and resources

{% include toollist.html tag="data analysis" %}
