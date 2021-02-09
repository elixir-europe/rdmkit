---
title: Editorial board guide
summary: This guide is there to help editors.
sidebar: contribute
---

## All you need to know about this GitHub repository

### General rules

As an editor, try to work as much as possible on a different branch than the master branch. This can be on the elixir-europe rdm-toolkit repo or your own fork. Open a pull request if you want to merge your changes with the master branch. This way it is possible for other editors to give feedback on your changes. Typos or other small fixes can of course be done immediately on the master branch.

### The google doc way of contributing
This process is sketched below.

{% include image.html file="googledoc_way_flow.svg" alt="Process of contributing via Google docs" click=true  %}

### Overview of the file structure in GitHub

The content of the website is built up using markdown files found in the [pages](https://github.com/elixir-europe/rdmkit/tree/master/pages) directory.
These markdown files are divided over subdirectories (your_role, your_domain, your_problem...) for sorting reasons only.

### The metadata/frontmatter of the markdown file

In order to render the markdown file to the website, it needs a specific frontmatter/metadata section in the top part of the file. This latter can look like:

```
---
title: Title of the page
---
```

Mandatory metadata/frontmatter:
* `title`: Specify here the page title. This will be the H1 title (replacing the top level title using the # in markdown )

Optional metadata/frontmatter: 

* `summary`: By using this attribute it is possible to specify a summary which will be displayed under the page title. This summary will also be used as description of your page when the page is tagged.

* `contributors`: List here all the contributors that helped in establishing the page, preferibly with their full name. Make sure that the person names that are listed can be found in the CONTRIBUTORS.yaml file in the *_data* directory if you want to link the GitHub ID and other contact information. Multiple contributors will be put in a list like this: [example1, example2].

* `search`: By setting this field to "exclude", the page will not end up in the search results of the search bar. Default: true.

* `hide_sidebar`: When true, the sidebar will be hidden. Default: false.

* `custom-editme`: This attribute can be used to specify an alternative file/link when clicked on the edit-me button.

* `keywords`: List here all the keywords that can be used to find the page using the search box in the right-upper corner of the page. Multiple keywords are put in a list like this: [example1, example2].

* `sidebar`: Specify here an alternative sidebar. Default: main.

* `toc`: When set to false, the table of contents at the beginning of the page will not be generated.

* `tags`: If you want to tag this page, list the tags using this attribute. If you want to use multiple tags, make sure to put them in a list like this: [example1, example2].

* `datatable`: Use this attribute to activate pagination, sorting  and searching in tables.

### Markdown file naming

- Markdown files should be named without capitals and without spaces (replace them with underscores).
- Make sure that the markdown file has a unique name.
- If the markdown file is named *example.md*, the page will be found at https://rdmkit.elixir-europe.org/example.
- By default a page will not show up in the sidebar. In order to do so you will have to add the link towards the page to the `.yaml` file in the *_data/sidebars* directory or link towards it from another page. More info about this can be found [here](#find-your-newly-added-page-back-on-the-website).

### GitHub checks

With each PR or merge to the master, some checks are done using GitHub actions. One of them checks wether the website builds correctly. The other checks for changes in the tool/resource Excel table. When each of them fails, the PR will not be able to be merged. Click on the red dot/failed check to understand better what caused the fail. 

## Label, discuss and assign issues

  * Check open issues regularly or enable notifications by clicking the "WATCH" icon in the top-right side of the [GitHub repository](https://github.com/elixir-europe/rdmkit/issues).
  * Assign labels to issues.
  * Discuss who is going to be responsible for each issue with other editors and reviewers (via issue comments or other communication channels).
  * Assign at least one editor/reviewer to the issue, who will discuss the possible content with the contributor.
  * When a Pull Request (PR) or a draft PR related to an issue is created, link the PR to the issue.
  
More information about these topics can be found in the GitHub documentation:
- [commenting on PRs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request)
- [start a review](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/reviewing-proposed-changes-in-a-pull-request)

## Review pull requests

If contributors make a pull request to make changes, by default the editors that are responsible for files that will changed by the PR will be assigned and notified. All PR should be assigned to one of the editors. Before merging a PR, pages' tags and keywords, and tools and resources' tags should be checked and assigned according to the established tagging system.
  
## Link a pull request to an issue

When you make a pull request resolving an issue, it is possible to link this pull request to that specific issue. This can be easily done by writing in the conversation of the PR: `closes #number_of_issue`, or `fixes #number_of_issue` or even `resolves #number_of_issue`. This is definitely applicable when authors first open an issue announcing a change or requesting a new page, followed up by the pull request. 
For more information about this topic please visit the [GitHub documentation page](https://docs.github.com/en/free-pro-team@latest/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue).

## Create a new page

### Simple way: using the GitHub interface
To generate a new page it is sufficient to simply copy the TEMPLATE file in the subdirectory and rename it. To copy a template you have to:

1. Go to the `TEMPLATE_` file of choice in the [GitHub repo](https://github.com/elixir-europe/rdmkit/tree/master/pages), every section has its own TEMPLATE file. For example the [TEMPLATE_your_problem.md](https://github.com/elixir-europe/rdmkit/blob/master/pages/your_problem/TEMPLATE_your_problem.md) file.

2. Click "Raw" on the GitHub page to open the file 'as is'
    {% include image.html file="raw_github.png" inline=true alt="Raw button GitHub." %}

3. Select and copy all the content.

4. Go back to the main section were you want to make the new page, in our example this will be in */pages/your_problem*. Click on `Add file` on the right followed up by `Create new file`.
    {% include image.html file="create_new_file_github.png" inline=true alt="Create new file GitHub." %}

5. Paste the copied content from the template.

6. Name the file by choosing a unique self explaining short name without capitals and without spaces (replace them with underscores).
    {% include image.html file="name_file_github.png" inline=true alt="Name the file in GitHub." %}

7. Check the frontmatter/metadata of the markdown page:
    - delete `search: exclude` attribute.
    - add the author names to the contributors list.
    - optional: change the title into an appropriate one.

8. Describe shortly which changes you made in the description of your commit below the page. Commit to the master branch by clicking `Commit new file`.
     {% include image.html file="commit_to_master_github.png" inline=true alt="Commit new file in GitHub." %}

9. If the markdown file is named *example.md* the page will be rendered at https://rdmkit.elixir-europe.org/example. This link can be provided to the contributor through the issue.

{% include note.html content="It is not a problem to immediately duplicate pages in the master branch, but be aware that new content always needs to be pushed to another branch which will give you the option to open a pull request." %}

### Advanced: working on your own feature branch and pushing local changes

Just like with every change you want to make to this repo, it is possible to do this through Git by working on a local copy. For more information on how to do this, please read our [working with Git](working_with_git) page.


## Find your newly added page back on the website

By default your page will not be linked in the sidebar on the website, or on the landing page, but it will exist as an orphan at *https://rdmkit.elixir-europe.org/markdown_file_name*. In order to prevent that people will not find the page back it is better to link towards it in the sidebar or get linked within an existing page. 

### Linking pages in the sidebar and frontpage

Make sure all pages are accessible from the navigation sidebar. Please, avoid generating sub-pages that are not directly accessible from the navigation sidebar.

This website supports multiple sidebars, the one in the main sections of the website is for example different from the one in the contribute section. Both of them are defined by `.yaml` files in the *_data/sidebars* directory. Changing these yaml file will immediately impact the sidebars and the frontpage of the website. The sidebar supports multiple levels and each level in the hierarchy can contain a URL to a page within this website or an external URL.

The attributes that define the structure are:
- `title`: This is the text that will show up in the sidebar.
- `url`: The URL to the internal page you want to link to. This is mostly in the form of: */markdown_file_name.html*.
- `external_url`: Use this instead of URL if you want to link to an external page.
- `folderitems`: To start a second level of links.
- `subfolderitems`: To start a third level of links.

```yaml
- title: Level_1_title
  url: level_1_url
  subitems:
    - title: Level_2_title
      url: level_2_url
```

{% include tip.html content="Copy around existing parts in the yaml file to add pages to the same level" %}

### Link page within existing page

Avoid manual linking to internal pages. If necessary, you can manually link to the pages like this:

If the markdown page is named example_1.md, you can link towards it using:

```md
[Example 1](example_1)
```

{% include important.html content="If you change the file name, you'll have to update all of your links." %}


## Linking the GitHub accounts to the contributors

Do you want that the GitHub picture of a contributor is shown next to their name? Or maybe you want that the name is clickable and links towards the GitHub page of that person? To enable this please add the name and the necessary metadata to the [CONTRIBUTORS.yaml](https://github.com/elixir-europe/rdmkit/blob/master/_data/CONTRIBUTORS.yaml) file in the *_data* directory like this:

```yaml
Bert Droesbeke:
    git: bedroesb
    email: bedro@psb.ugent.be
    gitter: bedroesb
    orcid: 0000-0003-0522-5674

```
{% include important.html content="Make sure that the name in the yaml file is identically the same as the one used in the metadata of the page." %}


## Page tagging

### Tagging the pages 

Tagging pages is done through the `tags:` property in the metadata of the markdown page.
Add the tag(s) to a list (square brackets). Make sure that your tag corresponds to an existing page. 

This metadata example shows how we tag the "Storage" page with the **share** tag:
```md
---
title: Storage
tags: [share, IT support] 
---
```

### Listing the pages somewhere else

If you then want to list all the pages containing the tag **share** you can use the code snippet:

{% raw %}
```
{% include pagelist.html tag="share" %}
```
{% endraw %}

Giving:

{% include pagelist.html tag="share" %}

This is preferably done on the 'IT support' page. In this way the tag visible on the tagged pages will link to the 'IT support', interlinking everything. 

### Supported tags

To only allow a curated list of tags, make sure that you find the tags in the `tags.yaml` file in the `_data` repository. 

## Using the tool/resource list

Here we list all the tools with the tag **data publication**  by using the code snippet:

{% raw %}
```
{% include toollist.html tag="data publication" %}
```
{% endraw %}

Giving:

{% include toollist.html tag="data publication" %}

Add a second tag for filtering using the 'tag2' attribute:

{% raw %}
```
{% include toollist.html tag="data publication" tag2="IT support" %}
```
{% endraw %}

Giving:

{% include toollist.html tag="data publication" tag2="IT support" %}

Tools and resources can be added by manipulating the tool_and_resource_list.xlsx file in the `_data` repository.
More information on how to add a tool or resource can be found [here](tool_resource_update).

### Supported tags

To only allow a curated list of tags, make sure that you find the tags in the `tags.yaml` file in the `_data` repository. 
