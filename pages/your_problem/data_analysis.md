---
title: Data analysis
contributors: [Olivier Collin, Stian Soiland-Reyes, Michael R. Crusoe]
tags: [analyse, process, reuse, researcher, IT support]
description: how to make data analysis FAIR.
page_tag: data analysis
---

## What are the best practices for data analysis?

### Description

When carrying out your analysis, you should also keep in mind that all your data analysis has to be reproducible. This will complement your research data management approach since your data will be FAIR compliant but also your tools and analysis environments. In other words, you should be able to tell what data and what code or tools were used to generate your results.

This will help to tackle reproducibility problems but also will improve the impact of your research through collaborations with scientists who will reproduce your in silico experiments.

### Considerations

There are many ways that will bring reproducibility to your data analysis. You can act at several levels:
* By providing your code.
* By providing your execution environment.
* By providing your workflows.
* By providing your data analysis execution.

### Solutions

* Make your code available. If you have to develop some software for your data analysis, it is always a good idea to publish your code. The git versioning system offers both a way to release your code but offers also a versioning system. You can also use Git to interact with your software users. Be sure to specify a license for your code (see the [licensing section](../licensing.md)).
* Use package and environment management system. By using package and environment management systems like [Conda](https://anaconda.org/) and its bioinformatics specialized channel [Bioconda](https://bioconda.github.io/), researchers that have got access to your code will be able to easily install specific versions of tools, even older ones, in an isolated environment. They will be able to compile/run your code in an equivalent computational environment, including any dependencies such as the correct version of R or particular libraries and command-line tools your code use. You can also share and preserve your setup by specifying in a [environment file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) which tools you installed.
* Use container environments. As an alternative to package management systems you can consider _container environments_ like [Docker](https://www.docker.com/) or [Singularity](https://sylabs.io/docs/).
* Use workflow management systems. [Scientific Workflow management systems](https://en.wikipedia.org/wiki/Scientific_workflow_system) will help you organize and automate how computational tools are to be executed. Compared to composing tools using a standalone script, workflow systems also help document the different computational analyses applied to your data, and can help with scalability, such as cloud execution. Reproducibility is also enhanced by the use of workflows, as they typically have bindings for specifying software packages or containers for the tools you use from the workflow, allowing others to re-run your workflow without needing to pre-install every piece of software it needs. It is a flourishing field and [many other workflow management systems](https://s.apache.org/existing-workflow-systems) are available, some of which are general-purpose (e.g. any command line tool), while others are domain-specific and have tighter tool integration. Among the many workflow management systems available, one can mention 
   * Workflow platforms that manage your data and provide an interface (web, GUI, APIs) to run complex pipelines and review their results. For instance: [Galaxy]( https://galaxyproject.org/) and [Arvados]( https://arvados.org) ([CWL-based]( https://www.commonwl.org), open source).
   * Workflow runners that take a workflow written in a proprietary or standardized format (such as the [CWL standard]( https://www.commonwl.org)) and execute it locally or on a remote compute infrastructure. For instance, [toil-cwl-runner](https://toil.readthedocs.io/en/latest/running/cwl.html), the reference CWL runner ([cwltool](https://pypi.org/project/cwltool/)), [Nextflow]( https://www.nextflow.io/), [Snakemake]( https://snakemake.readthedocs.io/), Cromwell.
* Use notebooks. Using notebooks, you will be able to create reproducible documents mixing text and code; which can help explain your analysis choices; but also be used as an exploratory method to examine data in detail. Notebooks can be used in conjunction with the other solutions mentioned above, as typically the notebook can be converted to a script. Some of the most well-known notebooks systems are: [Jupyter](https://jupyter.org/), with built-in support for code in Python, R and Julia, and many other [kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels); [RStudio](https://rstudio.com/products/rstudio/#rstudio-desktop) based on R. See the table below for additional tools.


## How can you use package and environment management systems?

### Description
By using package and environment management systems like [Conda](https://anaconda.org/) and its bioinformatics specialized channel [Bioconda](https://bioconda), you will be able to easily install specific versions of tools, even older ones, in an isolated environment. You can also share and preserve your setup by specifying in a [environment file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) which tools you installed.

### Considerations
Conda works by making a nested folder containing the traditional UNIX directory structure `bin/` `lib/` but installed from Conda's repositories instead of from a Linux distribution.
* As such Conda enables consistent installation of computational tools independent of your distribution or operating system version. Conda is  available for Linux, macOS and Windows, giving consistent experience across operating systems (although not all software is available for all OSes).
* Package management systems work particularly well for installing free and Open Source software, but can also be useful for creating an isolated environment for installing commercial software packages; for instance if they requires an older Python version than you have pre-installed.
* Conda is one example of a generic package management, but individual programming languages typically have their environment management and package repositories.
* You may want to consider submitting a release of your own code, or at least the general bits of it, to the package repositories for your programming language.

### Solutions
* MacOS-specific package management systems: [Homebrew](https://brew.sh/), [Macports](https://www.macports.org/).
* Windows-specific package management systems: [Chocolatey](https://chocolatey.org/) and [Windows Package Manager](https://docs.microsoft.com/en-us/windows/package-manager/) `winget`.
* Linux distributions also have their own package management systems (`rpm`/`yum`/`dnf`, `deb`/`apt`) that have a wide variety of tools available, but at the cost of less flexibility in terms of the tool versions, to ensure they exist co-installed.
* Language-specific virtual environments and repositories: [rvm](https://rvm.io/) and [RubyGems](https://rubygems.org/) for Ruby, [pip](https://docs.python.org/3/installing/index.html) and [venv](https://docs.python.org/3/tutorial/venv.html) for Python, [npm](https://www.npmjs.com/) for NodeJS/Javascript, [renv](https://rstudio.github.io/renv/) and [CRAN](https://cran.r-project.org/) for R, [Apache Maven](https://maven.apache.org/) or [Gradle](https://gradle.org/) for Java etc.
* Tips and tricks to navigate the landscape of software package management solutions:
    * If you need multiple tools/programming languages, but your machines have different OS types or versions, list packages in a Conda `environment.yml`.
    * If you need conflicting versions of some tools/libraries for different operations, make separate Conda environments.
    * If you need a few open source libraries for my Python script, none which require complilation, make a `requirements.txt` and reference `pip` packages.


## How can you use container environments?

### Description
Container environments like [Docker](https://www.docker.com/) or [Singularity](https://sylabs.io/docs/) allow you to easily install specific versions of tools, even older ones, in an isolated environment.

### Considerations
In short containers works almost like a virtual machine (VMs), in that it re-creates a whole Linux distibution with separation of processes, files and network.
* Containers are more lightweight than VMs since they don't virtualize hardware. This allows a container to run with a fixed version of the distribution independent of the host, and have just the right, minimal dependencies installed.
* The container isolation also adds a level of _isolation_, which although not as secure as VMs, can reduce the attack vectors. For instance if the database container was compromised by unwelcome visitors, they would not have access to modify the web server configuration, and the container would not be able to expose additional services to the Internet.
* A big advantage of containers is that there are large registries of community-provided container images.
* Note that modifying things inside a container is harder than in a usual machine, as changes from the image are lost when a container is recreated.
* Typically containers run just one tool or applications, and for service deployment this is useful for instance to run mySQL database in a separate container from a NodeJS application.

### Solutions
* [Docker](https://www.docker.com/) is the most well-known container runtime, followed by [Singularity](https://sylabs.io/docs/). These require (and could be used to access) system administrator privileges to be set up.
* [uDocker](https://indigo-dc.gitbook.io/udocker/) and [Podman](https://podman.io/) are also _user space_ alternatives that have compatible command line usage.
* Large registries of community-provided container images are [Docker Hub](https://hub.docker.com/) and [RedHat Quay.io](https://quay.io/search). These are often ready-to-go, not requiring any additional configuration or installations, allowing your application to quickly have access to open source server solutions.
* [Biocontainers](https://biocontainers.pro/) have a large selection of bioinformatics tools.
* To customize a Docker image, it is possible to use techniques such as [volumes](https://docs.docker.com/storage/volumes/) to store data and [Dockerfile](https://docs.docker.com/engine/reference/builder/). This is useful for installing your own application inside a new container image, based on a suitable _base image_ where you can do your `apt install` and software setup in a reproducible fashion - and share your own application as an image on Docker Hub.
* Container linkage can be done by _container composition_ using tools like [Docker Compose](https://docs.docker.com/compose/).
* More advanced container deployment solutions like [Kubernetes](https://kubernetes.io/) and Computational Workflow Management systems can also manage cloud instances and handle analytical usage.
* Tips and tricks to navigate the landscape of container solutions:
    * If you just need to run a database server, describe how to run it as a Docker/Singularity container.
    * If you need several servers running, connected together, set up containers in Docker Compose.
    * If you need to install many things, some of which are not available as packages, make a new `Dockerfile` recipe to build container image.
    * If you need to use multiple tools in a pipeline, find Conda or container images, compose them in a Computational Workflow.
    * If you need to run tools in a cloud instance, but it has nothing preinstalled, use Conda or containers to ensure installion on cloud VM matches your local machine.
    * If you just need a particular open source tool installed, e.g. ImageMagick, check the document how to install: _For Ubuntu 20.04, try `apt install imagemagick`_.
