---
title: Updating the tool and resource list
sidebar: contribute
summary: How to add a tool or resource to RDMKit
---

## Way of working

The tools or resources you will find on pages are a filtered set from a [bigger list](all_tools_and_resources). This filtering is done using tags. The general tool/resource list is based on the [csv file](https://github.com/elixir-europe/rdmkit/blob/master/_data/main_tool_and_resource_list.csv) in the `_data` directory of the RDMKit repository. Tools and resources are manually linked to [FAIRsharing.org](https://fairsharing.org/). The link with [Bio.tools](https://bio.tools) is done manually in the scenarios that the automatic lookup fail. Finally, the link with [TeSS](https://tess.elixir-europe.org/) is fully automatic and weekly updated. If changes to this file are pushed to GitHub, a GitHub Bot will generate a Pull Request (PR) with the changes of the csv file applied to the main data file of the website (a yaml file).

{% include important.html content="The link with TeSS is automatically done using GitHub actions and is weekly updated. These automatic links are not seen in the table. The search query to TeSS for a tool or resource can be overwritten in the registry column of the main csv tool table." %}

## The main table


The table consists of 5 columns:
- **name**: the name of the tool or resource
- **link**: URL to the main page of the tool or resource, make sure to let the URL start with https://
- **description**: A short description of the tool or resource. Try to not use the characters `"` or `'` 
- **registry**: 3 registries are supported: [Bio.tools](https://bio.tools), [FAIRsharing.org](https://fairsharing.org/) and [TeSS](https://tess.elixir-europe.org/). The keywords you can use respectively are: `biotools`, `fairsharing` and `tess`, specifying the id or query with a colon). List multiple registries using a comma `, ` between the keywords to separate the key:value pairs. 
- **tags**: This is used to tag the tools so it is listed on the correct page. Make sure your tag is listed in the curated list of tags ( The `tags.yaml` file [here](https://github.com/elixir-europe/rdmkit/blob/master/_data/tags.yml) ). List multiple tags by using a comma `, ` between them.

| name   	| link                                     	| description                                                                                         	| registry           	| tags             	|
|--------	|------------------------------------------	|-----------------------------------------------------------------------------------------------------	|--------------------	|------------------	|
| BrAPI  	| https://www.brapi.org                    	| Specification for a standard API for plant data: plant material, plant phenotyping data             	|                    	| share            	|
| COPO   	| https://copo-project.org/                	| Portal for scientists to broker more easily rich metadata alongside data to public repos            	|                    	| share            	|
| DAISY  	| https://daisy-demo.elixir-luxembourg.org 	| Data Information System to keep sensitive data inventory and meet GDPR accountability requirement.  	| biotools:DAISY     	| plan, collect    	|
| Phyre2 	| http://www.sbg.bio.ic.ac.uk/~phyre2      	| Protein Homology/analogY Recognition Engine                                                         	| biotools:phyre     	| process, analyse 	|
| MIAPPE 	| https://www.miappe.org/                  	| Minimum Information About a Plant Phenotyping Experiment                                            	| fairsharing:nd9ce9 	| standard         	|


## What tool or resource can be added to the table
Tools and resources specifically mentioned in the text of the pages should be present in the main table. If necessary, tools and resources equivalent to the one mentioned in the text could also be added to the table.

## Making changes

Since the csv file is not user-friendly and prone to mistakes because empty fields and commas, we do not recommend making changes using the GitHub website itself. 

### Simple way: changing the Google spreadsheet

For people that are not familiar with Git, no worries! The editors will do the work on Git for you. All you need to do is:
- Open this [Google spreadsheet](https://docs.google.com/spreadsheets/d/16RESor_qQ_ygI0lQYHR23kbZJUobOWZUbOwhJbLptDE/edit?usp=sharing).
- Check if a tool or resource is already listed.
- Add or edit tools and resources as described above.
- Done! The editors will update the "tool and resource list" in GitHub regularly.

### Advanced way: making your own PR with changes to the csv file

Just like with every change you want to make to the repo, it is possible to do this through Git by working on a local copy. For more information on how to do this, please read our [working with Git](working_with_git) page. Open the local copy of the csv file in excel, make your changes and commit them.

{% include tip.html content="If you want to know wether the conversion of the .csv table and your changes are successful, check out the github action check in the PR named 'Validating the tool and resource table / build' " %}


## Let the bot do the rest
If the PR containing the changes to the .csv table is merged, a PR will be opened by github-actions. Please check that the changes this PR proposes to the yaml file are in line with what you want to have changed.
