---
title: Data analysis
contributors: [Olivier Collin]
tags: [analyse, process, reuse, researcher, IT support]
description: how to make data analysis FAIR.
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
By using package and environment management systems like [Conda](https://anaconda.org/) and its bioinformatics specialized channel [Bioconda](https://bioconda.github.io/), you will be able to easily install specific versions of tools, even older ones, in an isolated environment. You can also manage your environment by specifying in a file which tools you need. 

You can combine the usage of Conda with container environments like [Docker](https://www.docker.com/) or [Singularity](https://sylabs.io/docs/). 


#### Workflows reproducibility 

[Scientific Workflow management systems](https://en.wikipedia.org/wiki/Scientific_workflow_system) will help you organize and automate how computational tools are to be executed.

Compared to composing tools using a standalone script, workflow systems also help document the different computatoinal analyses applied to your data, and can help with scalability, such as cloud execution.

There a many workflow management systems available. One can mention:
* [Galaxy](https://galaxyproject.org/)
* [Nextflow](https://www.nextflow.io/)
* [Snakemake](https://snakemake.readthedocs.io/)

It is a flourishing field and [many other workflow management systems](https://s.apache.org/existing-workflow-systems) are available, some of which are general-purpose (e.g. any command line tool), while others are domain-specific and have tighter tool integration. 

#### Notebooks 

Using notebooks, you will be able to create reproducible documents mixing text and code; which can help explain your analysis choices; but also be used as an exploratory method to examine data in detail.

Notebooks can be used in conjunction with the other solutions mentioned above, as typically the notebook can be converted to a script.

Among the most well-known notebooks systems are: 

* [Jupyter](https://jupyter.org/) with built-in support for code in Python, R and Julia, and many other [kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)
* [RStudio](https://rstudio.com/products/rstudio/#rstudio-desktop) based on R 

## Relevant tools and resources

{% include toollist.html tag="data analysis" %}
