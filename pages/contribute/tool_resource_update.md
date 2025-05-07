---
title: Add new tool or resource
---

## Way of working

You will find a "Tools and resources on this page" section at the bottom of most pages. The entries of this section are a subset of the [All tools and resources](all_tools_and_resources) table. The appearance of a tool or resource in this subset is solely determined by the fact that it is mentioned in the content of that page using the syntax described below.

The [All tools and resources](all_tools_and_resources) table is described in a central YAML file, [tool_and_resource_list.yml](https://github.com/elixir-europe/rdmkit/blob/master/_data/tool_and_resource_list.yml), in the `_data` directory. Tools and resources can be manually linked to [FAIRsharing.org](https://fairsharing.org/), [bio.tools](https://bio.tools) and [TeSS](https://tess.elixir-europe.org/). We also run a fully automatic weekly check that links tools and resources with the corresponding registries. A GitHub Bot will open a Pull Request (PR) when new links are found.

{% include callout.html type="important" content="Possible links between a tool or resource and registries such as FAIRsharing, TeSS, or bio.tools are automatically identified using GitHub Actions on a weekly basis. If the automatically proposed link is not relevant, and there is no other FAIRsharing ID, bio.tools ID, or TeSS query available for the source, you can overwrite the automatic linking by adding `NA` as the value of a registry field." %}


## When can you add a new tool or resource

Tools and resources mentioned in the text of the pages should be included in the main table. However, not everything qualifies as a tool or resource in the context of RDMkit. Specifically, the following are **not** considered tools or resources:  
- **Publications**: Articles, white papers, or other academic literature. See our [style guide](https://rdmkit.elixir-europe.org/style_guide#bibliography) on adding publications to a bibliography.
- **Policies**: Guidelines, mandates, or institutional frameworks.  
- **Webpages of groups or consortia**: Informational pages or organisational websites without a dedicated tool or service.

Additionally, it is important to note that we do not distinguish between tools and resources; these terms are used interchangeably throughout RDMkit.

Tool and resource mentions are allowed only in the following sections:  
- **Your domain**  
- **Your role**  
- **Your tasks**  
- **Tool assembly**  

If your contribution aligns with these criteria, follow the steps outlined below to add your entries to the main YAML file.

## The main YAML file

Each tool or resource mentioned in the text has metadata stored in the [main YAML file](https://github.com/elixir-europe/rdmkit/blob/master/_data/tool_and_resource_list.yml). The metadata block for each tool consists of 5 attributes:
- **id**: The ID of a tool, in kebab-case, lowercase with hyphens.
- **name**: the name of the tool or resource
- **url**: URL to the main page of the tool or resource, make sure to let the URL start with `https://`
- **description**: A short description of the tool or resource. Try to not use the characters `"` or `'` 
- **registry**: 3 registries are supported: [Bio.tools](https://bio.tools), [FAIRsharing.org](https://fairsharing.org/) and [TeSS](https://tess.elixir-europe.org/). The keywords you can use respectively are: `biotools`, `fairsharing`, `fairsharing-coll` and `tess`, specifying the id or query with a colon. For FAIRsharing, copy the alphanumeric characters after "FAIRsharing." in the DOI. FAIRsharing collections are not associated with a DOI but use a four-digit ID well-visible on the page. List registries under the `registry` attribute as `key: value pairs`. If no FAIRsharing ID, bio.tools ID or TeSS query is available for a source, you can overwrite the automatic linking by adding 'NA' as a registry.

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
    fairsharing: c55d5e
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
