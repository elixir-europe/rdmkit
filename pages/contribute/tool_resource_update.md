---
title: Add new tool or resource
summary: How to add a tool or resource to RDMkit
---

## Way of working

The tools or resources you will find on pages are a selected set from a [bigger list](all_tools_and_resources). This selection is based on the appearance of a tool or resource in the content of the page.

Since the `Data life cycle` pages do not list tools, no tools table will be present on these pages. Tool and resource mentions are  allowed in the following sections: `Your domain`, `Your role`, `Your tasks` and `Tool assembly`. 

The [all_tools_and_resources](all_tools_and_resources) list is based on the [yaml file](https://github.com/elixir-europe/rdmkit/blob/master/_data/tool_and_resource_list.yml) in the `_data` directory of the RDMkit repository. Tools and resources can be manually linked to [FAIRsharing.org](https://fairsharing.org/), [Bio.tools](https://bio.tools) and [TeSS](https://tess.elixir-europe.org/), but every week we also run a fully automatic check that links tools and resources with the corresponding registries. A GitHub Bot will generate a Pull Request (PR) with the new links added to the main data file of the website.

{% include callout.html type="important" content="The link with FAIRsharing,TeSS and Bio.tools is automatically done using GitHub actions and is updated weekly. If no FAIRsharing ID, Bio.tools ID or TeSS Query is available for a source, but there is yet one automatically given (faulty), you can overwrite the automatic linking by adding 'NA' as a registry." %}

## The main yaml file

Each tool or resource mentioned in the text has metadata stored in the [main yaml file](https://github.com/elixir-europe/rdmkit/blob/master/_data/tool_and_resource_list.yml). The metadata block for each tool consists of 5 attributes:
- **id**: The ID of a tool, in kebab-case, lowercase with hyphens.
- **name**: the name of the tool or resource
- **url**: URL to the main page of the tool or resource, make sure to let the URL start with `https://`
- **description**: A short description of the tool or resource. Try to not use the characters `"` or `'` 
- **registry**: 3 registries are supported: [Bio.tools](https://bio.tools), [FAIRsharing.org](https://fairsharing.org/) and [TeSS](https://tess.elixir-europe.org/). The keywords you can use respectively are: `biotools`, `fairsharing`, `fairsharing-coll` and `tess`, specifying the id or query with a colon. FAIRsharing collections have an ID that follows the pattern `bsg-s000XXX`. List registries under the `registry` attribute as `key: value pairs`. If no FAIRsharing ID, Bio.tools ID or TeSS Query is available for a source, you can overwrite the automatic linking by adding 'NA' as a registry.

Example:

```yml
- id: github
  name: GitHub
  url: https://github.com
  description:
    Versioning system, used for sharing code, as well as for sharing of
    small data
  registry:
    tess: GitHub
```


## What tool or resource can be added to the table
Tools and resources specifically mentioned in the text of the pages should be present in the main table. 

## Making changes

1. Make sure the tool you want to add is not yet already described in the [yaml file](https://github.com/elixir-europe/rdmkit/blob/master/_data/tool_and_resource_list.yml). If so, go to step 3, if not, go follow the next step.

1. Click on the pencil icon seen on GitHub of the [main yaml file](https://github.com/elixir-europe/rdmkit/blob/master/_data/tool_and_resource_list.yml) as described in our GitHub Guide. Add your tool or resource at the bottom of the file following the structure described in the [The main yaml file section of this page](#the-main-yaml-file). Make sure the indentation follows one of the previously listed items. Copy the content of the yaml file and paste it in an online yaml validator in case of doubt.

1. Copy the `tool_id` of the tool or resource

1. Add the right context on RDMkit for the tool by mentioning it somewhere in the text using the following syntax:
  
  ```
  {% raw %}
  {% tool "tool_id" %}
  {% endraw %}
  ```

  {% include callout.html type="important" content="Don't forget to add the `\"` double quotes around the tool_id and make sure to use the exact tool_id as described in the yaml file." %}

  Example:

  ```
  {% raw %}
  {% tool "zenodo" %} is a powerful data publication service, which is supported by the European commission and focused on research data, including supplemental material like software, tables, figures or slides.
  {% endraw %}
  ```
  Will give: 
  
  {% tool "zenodo" %} is a powerful data publication service, which is supported by the European commission and focused on research data, including supplemental material like software, tables, figures or slides.
