---
title: Add new tool or resource
---

## Way of working

The "Tools and resources on this page" you will find at the bottom of many pages are a subset of the [All tools and resources](all_tools_and_resources) table. The appearance of a tool or resource in this subset is solely determined by the fact that it is mentioned in the content of that page.

The [All tools and resources](all_tools_and_resources) table is described in a central YAML file, [tool_and_resource_list.yml](https://github.com/elixir-europe/rdmkit/blob/master/_data/tool_and_resource_list.yml), in the `_data` directory. Tools and resources can be manually linked to [FAIRsharing.org](https://fairsharing.org/), [Bio.tools](https://bio.tools) and [TeSS](https://tess.elixir-europe.org/), but every week we also run a fully automatic check that links tools and resources with the corresponding registries. A GitHub Bot will generate a Pull Request (PR) with the new links found.

{% include callout.html type="important" content="The link with FAIRsharing, TeSS and Bio.tools is automatically done using GitHub Actions and is updated weekly. If no FAIRsharing ID, Bio.tools ID or TeSS query is available for a source, but there is yet one automatically given (faulty), you can overwrite the automatic linking by adding `NA` as a registry." %}


## When can you add a new tool or resource

Tools and resources mentioned in the text of the pages should be included in the main table. However, not everything qualifies as a tool or resource in the context of RDMkit. Specifically, the following are **not** considered tools or resources:  
- **Publications**: Articles, white papers, or other academic literature.  
- **Policies**: Guidelines, mandates, or institutional frameworks.  
- **Webpages of groups or consortia**: Informational pages or organizational websites without a dedicated tool or service.

Additionally, it is important to note that we do not distinguish between tools and resources; the terms are used interchangeably throughout RDMkit.

Tool and resource mentions are allowed in the following sections:  
- **Your domain**  
- **Your role**  
- **Your tasks**  
- **Tool assembly**  

If your contribution aligns with these criteria, follow the steps outlined below to add it to the main YAML file.

## The main YAML file

Each tool or resource mentioned in the text has metadata stored in the [main YAML file](https://github.com/elixir-europe/rdmkit/blob/master/_data/tool_and_resource_list.yml). The metadata block for each tool consists of 5 attributes:
- **id**: The ID of a tool, in kebab-case, lowercase with hyphens.
- **name**: the name of the tool or resource
- **url**: URL to the main page of the tool or resource, make sure to let the URL start with `https://`
- **description**: A short description of the tool or resource. Try to not use the characters `"` or `'` 
- **registry**: 3 registries are supported: [Bio.tools](https://bio.tools), [FAIRsharing.org](https://fairsharing.org/) and [TeSS](https://tess.elixir-europe.org/). The keywords you can use respectively are: `biotools`, `fairsharing`, `fairsharing-coll` and `tess`, specifying the id or query with a colon. FAIRsharing collections have an ID that follows the pattern `bsg-s000XXX`. List registries under the `registry` attribute as `key: value pairs`. If no FAIRsharing ID, Bio.tools ID or TeSS query is available for a source, you can overwrite the automatic linking by adding 'NA' as a registry.

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

## Linking the tool or resource in the text with the main YAML file

1. Make sure the tool you want to add is not already listed in the [YAML file](https://github.com/elixir-europe/rdmkit/blob/master/_data/tool_and_resource_list.yml). If so, go to step 3, if not, follow the next step.

1. Click on the pencil icon seen on GitHub of the [main YAML file](https://github.com/elixir-europe/rdmkit/blob/master/_data/tool_and_resource_list.yml) as described in our GitHub Guide. Add your tool or resource at the bottom of the file following the structure described in the [The main YAML file section of this page](#the-main-YAML-file). Make sure the indentation follows one of the previously listed items. In case of doubt, copy the content of the YAML file and paste it into an online YAML validator to check the format.

1. Copy the `tool_id` of the tool or resource

1. Add the right context on RDMkit for the tool by mentioning it somewhere in the text using the following syntax:
  
  ```
  {% raw %}
  {% tool "tool_id" %}
  {% endraw %}
  ```

  {% include callout.html type="important" content="Don't forget to add the `\"` double quotes around the tool_id and make sure to use the exact tool_id as described in the YAML file." %}

  Example:

  ```
  {% raw %}
  {% tool "zenodo" %} is a powerful data publication service, which is supported by the European Commission and focused on research data, including supplemental material like software, tables, figures or slides.
  {% endraw %}
  ```
  Will give: 
  
  {% tool "zenodo" %} is a powerful data publication service, which is supported by the European Commission and focused on research data, including supplemental material like software, tables, figures or slides.
