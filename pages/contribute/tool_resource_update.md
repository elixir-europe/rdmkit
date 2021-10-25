---
title: Updating the tool and resource list
sidebar: contribute
summary: How to add a tool or resource to RDMkit
---

## Way of working

The tools or resources you will find on pages are a filtered set from a [bigger list](all_tools_and_resources). This filtering is done using page_id. If a tool or resource is tagged with for example the page_id `researcher`, it will be automatically listed on the corresponding page. 

Since the `Data life cycle` pages are not listing tools, we do not allow page_id from this section in the tool table. page_id allowed in the tool table are page_id from the following sections: `Your domain`, `Your role`, `Your tasks` and `Tool assembly`. The page_id can be found in the [Website overview page](website_overview). 

The [all_tools_and_resources](all_tools_and_resources) list is based on the [csv file](https://github.com/elixir-europe/rdmkit/blob/master/_data/main_tool_and_resource_list.csv) in the `_data` directory of the RDMkit repository. Tools and resources can be manually linked to [FAIRsharing.org](https://fairsharing.org/),[Bio.tools](https://bio.tools) and [TeSS](https://tess.elixir-europe.org/), but every week we also run a fully automatic check that links tools and resources with the corresponding registries. A GitHub Bot will generate a Pull Request (PR) with the new links added the main data file of the website (a yaml file).

{% include important.html content="The link with FAIRsharing,TeSS and Bio.tools is automatically done using GitHub actions and is weekly updated. These automatic links are not seen in the table. The search query to one of these registries for a tool or resource can be overwritten in the registry column of the main csv tool table. If no FAIRsharing ID, Bio.tools ID or TeSS Query is available for a source, but there is yet one automatically given (faulty), you can overwrite the automatic linking by adding 'NA' as registry." %}

## The main csv table


The table consists of 5 columns:
- **name**: the name of the tool or resource
- **link**: URL to the main page of the tool or resource, make sure to let the URL start with `https://`
- **description**: A short description of the tool or resource. Try to not use the characters `"` or `'` 
- **registry**: 3 registries are supported: [Bio.tools](https://bio.tools), [FAIRsharing.org](https://fairsharing.org/) and [TeSS](https://tess.elixir-europe.org/). The keywords you can use respectively are: `biotools`, `fairsharing`, `fairsharing-coll` and `tess`, specifying the id or query with a colon). FAIRsharing collections have an ID that follows the pattern `bsg-s000XXX`. List multiple registries using a comma `, ` between the keywords to separate the key:value pairs. The values that are given in the table will always overrule the automatic links. If no FAIRsharing ID, Bio.tools ID or TeSS Query is available for a source, you can overwrite the automatic linking by adding 'NA' as registry.
- **related_pages**: This is used to tag the tools so it is listed on the correct page. We only allow page_id that are linked to a page. To find out what the page_id of a page is, please check its metadata attribute `page_id` at the top of the markdown file or the [Website overview](website_overview) page. Since the Data life cycle pages are not listing tools, we do not allow these page_id in the tool table. page_id allowed in the tool table are page_id from the following sections: `Your domain`, `Your role`, `Your tasks` and `Tool assembly`. List multiple page_id by using a comma `, ` between them.
- **country** : If a tool can only be used in a specific country, list those countries with there Alpha-2 code. For a complete list of all country code please visit the [IBAN](https://www.iban.com/country-codes) website. A flag will appear in the `related pages` column.

| name     | link                             | description                                                                               | registry                                    | related_pages                                             |
|----------|----------------------------------|-------------------------------------------------------------------------------------------|---------------------------------------------|--------------------------------------------------|
| Beacon   | https://beacon-project.io/       | The Beacon protocol defines an open standard for genomics data discovery.                 |                                             | researcher, data manager, IT support, human data |
| Bioconda | https://bioconda.github.io/      | Bioconda is a bioinformatics channel for the Conda package manager                        | biotools:bioconda                           | IT support, data analysis                        |
| BrAPI    | https://www.brapi.org            | Specification for a standard API for plant data: plant material, plant phenotyping data   |                                             | IT support, plants                               |
| Conda    | https://docs.conda.io/en/latest/ | Open source package management system                                                    |                                             | IT support, data analysis                        |
| COPO     | https://copo-project.org/        | Portal for scientists to broker more easily rich metadata alongside data to public repos. | biotools:copo, fairsharing-coll:bsg-d001247 | metadata, researcher, plants                     |


## What tool or resource can be added to the table
Tools and resources specifically mentioned in the text of the pages should be present in the main table. If necessary, tools and resources equivalent to the one mentioned in the text could also be added to the table.

## Making changes

Since the csv file is not user-friendly and prone to mistakes because empty fields and commas, we do not recommend making changes using the GitHub website itself. 

### Simple way: changing the Google spreadsheet (recommended)

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
