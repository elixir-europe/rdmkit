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

### Simple way: changing the google spreadsheet

For people that are not familiar with Git, no worries! The editors will do the work on Git for you. All you need to do is:
- Open this [Google spreadsheet](https://docs.google.com/spreadsheets/d/16RESor_qQ_ygI0lQYHR23kbZJUobOWZUbOwhJbLptDE/edit?usp=sharing).
- Check if a tool or resource is already listed.
- Add or edit tools and resources as described above in "The excel table" paragraph.
- Done! The editors will update the "tool and resource list" in GitHub regularly.

### Advanced way: making your own PR with changes to the excel file

Just like with every change you want to make to the repo, it is possible to do this through Git by working on a local copy. For more information on how to do this, please read our [working with Git](working_with_git) page.

{% include tip.html content="If you want to know wether the conversion of the excel table and your changes are successful, check out the github action check in the PR named 'Validating the tool and resource table / build' " %}


## Let the bot do the rest
If the PR containing the changes to the excel table is merged, a PR will be opened by github-actions. Please check that the changes this PR proposes to the yaml file are in line with what you want to have changed.
