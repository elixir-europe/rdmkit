---
title: Updating tool and resource list
sidebar: contribute
summary: How to add a tool or resource to RDM Toolkit
---

## Way of working

The tools or resources you will find on pages are a filtered set from a bigger list. This filtering is done using tags. The general tool/resource list is based on the [excel file](https://github.com/elixir-europe/rdm-toolkit/blob/master/_data/tool_and_resource_list.xlsx) in the `_data` directory of the RDM Toolkit repository. If changes to this file are pushed to github, a Github Bot will generate a Pull Request (PR) with the changes of the excel file applied to the main data file of the website.

## The excel table


The table consists of 5 columns:
- **name**: the name of the tool or resource
- **link**: URL to the main page of the tool or resource, make sure to let the URL start with https://
- **description**: A short description of the tool or resource. Try to not use the characters `"` or `'` 
- **registry**: 2 registries are supported: [Bio.tools](https://bio.tools) and [FAIRsharing.org](https://fairsharing.org/) 
- **tags**: This is used to tag the tools so it is listed on the correct page. Make sure your tag is listed in the curated list of tags ( The `tags.yaml` file [here](https://github.com/elixir-europe/rdm-toolkit/blob/master/_data/tags.yml) )

| name   	| link                                     	| description                                                                                         	| registry           	| tags             	|
|--------	|------------------------------------------	|-----------------------------------------------------------------------------------------------------	|--------------------	|------------------	|
| BrAPI  	| https://www.brapi.org                    	| Specification for a standard API for plant data: plant material, plant phenotyping data             	|                    	| share            	|
| COPO   	| https://copo-project.org/                	| Portal for scientists to broker more easily rich metadata alongside data to public repos            	|                    	| share            	|
| DAISY  	| https://daisy-demo.elixir-luxembourg.org 	| Data Information System to keep sensitive data inventory and meet GDPR accountability requirement.  	| biotools:DAISY     	| plan, collect    	|
| Phyre2 	| http://www.sbg.bio.ic.ac.uk/~phyre2      	| Protein Homology/analogY Recognition Engine                                                         	| biotools:phyre     	| process, analyse 	|
| MIAPPE 	| https://www.miappe.org/                  	| Minimum Information About a Plant Phenotyping Experiment                                            	| fairsharing:nd9ce9 	| standard         	|


## Making changes

Since the excel file is a binary file and not a text based file, it is not possible to make changes using the Github website itself.

### Simple: Opening an issue
For people that are not familiar with Git, no worries! We are really happy to hear your suggestions using the [issues section](https://docs.github.com/en/github/managing-your-work-on-github/creating-an-issue) on github. Please click *Fixing an existing page or add tool/resource* when opening an issue and follow further instructions. The editors will help you in adding a new tool or resource to the tool/resource table.

### Advanced: Making your own PR with changes to the excel file

In order to do so follow these general Git steps if you did not already do them to contribute to this repository:
- Make a fork of this repository, using the fork button.
- Open a terminal and clone your fork using:
    ```
    git clone git@github.com:USERNAME/rdm-toolkit.git
    cd rdm-toolkit
    ```
- Keep your fork up to date.
    ```
    git remote add upstream https://github.com/elixir-europe/rdm-toolkit.git
    git fetch upstream
    git pull upstream master
    ```
- Create a Branch.
    ```
    git branch -b newtool
    git checkout newtool
    ```
- Open the excel file `rdm-toolkit/_data/tool_and_resource_list.xlsx` with excel or any other program that supports .xlsx files
- Add or change the tool list.
- Save.
- Open terminal and stage your changes:
    ```
    git add .
    ```
- Committing and pushing the changes
    ```
    git commit -m "Changing the tool-resource file"
    git push origin newtool
    ```
- Go to [https://github.com/elixir-europe/rdm-toolkit](https://github.com/elixir-europe/rdm-toolkit) and click on *Compare & pull request*
- Open the pull request

{% include tip.html content="If you want to know wether the conversion of the excel table and your changes are successful, check out the github action check in the PR named 'Validating the tool and resource table / build' " %}


## Let the bot do the rest
If the PR containing the changes to the excel table is merged, a PR will be opened by github-actions. Please check that the changes this PR proposes to the yaml file are in line with what you want to have changed.