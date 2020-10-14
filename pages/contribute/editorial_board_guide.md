---
title: Editorial board guide
summary: This guide is there to help editors.
sidebar: contribute
---

## All you need to know about this Github repository

### Overview of the files structure in Github
The content of the website is built up using markdown files found in the [pages](https://github.com/elixir-europe/rdm-toolkit/tree/master/pages) directory.
These markdown files are divided over subdirectories (your_role, your_domain, your_problem,...) for sorting reasons only.

### The metadata/frontmatter of the markdown file
In order for the markdown file to be rendered to the website, it needs a specific frontmatter/metadata section in the top part of the file. This can look like this:

```
---
title: Title of the page
---
```

Mandatory metadata/frontmatter:
* `title`: Specify here the title of the page. This wil be the H1 title (replacing the top level title using the # in markdown )

Optional metadata/frontmatter: 

* `summary`: Using this attribute it is possible to specify a summary which will be displayed under the title of the page. This summary will also be used as description of your page when the page is tagged.

* `contributors`: list here all the contributors that helped in establishing the page. This will be the name of the person. Make sure that the person name that is listed can be found in the CONTRIBUTORS.yaml file in the _data directory if you want to link the github id and other contact information.

* `search`: by setting this field to exclude, the page will not end up in the search results of the searchbar. By default this is true.

* `hide_sidebar`: When true, the sidebar will be hided. Default: false

* `custom-editme`: This attribute can be used to specify an alternative file/link when clicked on the edit-me button

* `keywords`: List here all the keywords that can be used to find the page using the searchbox in the right upper corner of the page.

* `sidebar`: Specify here an alternative sidebar. Default: main

* `toc`: When set to false, the table of contents in the beginning of the page will not be generated.

* `tags`: If you want to tag this page list the tag using this attribute

* `datatable`: use this attribute to activate the pagination + sorting + searching in tables

### Markdown file naming
- The markdown files should be named without capitals and without spaces (replace them with underscores)
- Make sure the markdown file has a unique name
- If the markdown file is named *example.md*, the page will be found at https://rdm.elixir-europe.org/example
- By default a page will not show up in the sidepanel. In order to do so you will have to add the link towards the page to the `.yaml` file in the *_data/sidebars* directory. More info about this can be found [here](#adding-links-to-the-sidebar)

### Github checks
With each PR or or merge to the master, some checks are done using github Actions. One of them checks wether the website builds correctly. The other checks for changes in the tool/resource excel table. When each of them fails, the PR will not be able to be merged. Click on the red dot/failed check to understand more what caused the fail. 

## Label, discuss and assign issues
  * Check open issues regularly or enable notifications by clicking on "WATCH" icon on the top right side of the [GitHub repository](https://github.com/elixir-europe/rdm-toolkit/issues).
  * Assign labels to issues.
  * Discuss who is going to be responsible for each issue with other editors and reviewers (via issue comments or other communication channels).
  * Assign at least one editor/reviewer to the issue, who will discuss the possible content with the contributor.
  * When a Pull Request (PR) or a draft PR related to an issue is created, link the PR to the issue.
  
## Link a Pull Request (PR) to an issue
When you make a pull request resolving an issue, it is possible to link this pull request to that specific issue. This can easily be done by writing in the conversation of the PR: `closes #number_of_issue`, or `fixes #number_of_issue` or even `resolves #number_of_issue`. This is definitely applicable when authors first open an issue announcing a change/requesting a new page, followed up by the pull request. 
For more information about this topic please visit the [Github documentation page](https://docs.github.com/en/free-pro-team@latest/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue).

## Create new page

### Simple way: using the Github interface
Simply copying the TEMPLATE file in the subdirectory and renaming it, is sufficient to generate a new page. To copy a template you have to:

1. Go to the `TEMPLATE_` file of choice in the [github repo](https://github.com/elixir-europe/rdm-toolkit/tree/master/pages), every section has its own TEMPLATE file. For example the [TEMPLATE_your_problem.md](https://github.com/elixir-europe/rdm-toolkit/blob/master/pages/your_problem/TEMPLATE_your_problem.md) file

2. Click "Raw" on the github page to open the file 'as is'
    {% include image.html file="raw_github.png" inline=true alt="Raw button Github." %}

3. Select and copy all the content

4. Go back to the main section were you want to make the new page, in our example this will be in */pages/your_problem*. Click on `Add file` on the right followed up by `Create new file`.
    {% include image.html file="create_new_file_github.png" inline=true alt="Create new file github." %}

5. Paste the copied content from the template

6. Name the file by choosing a unique self explaining short name. Without capitals and without spaces (replace them with underscores).
    {% include image.html file="name_file_github.png" inline=true alt="Name the file in github." %}

7. Check the frontmatter/metadata of the markdown page:
    - delete `search: exclude` attribute
    - add the names of the authors to the contributors list
    - optional: changing the title to an appropriate one

8. Commit to the master branch by clicking `Commit new file`
     {% include image.html file="commit_to_master_github.png" inline=true alt="Commit new file in github." %}

9. If the markdown file is named *example.md*, the page will be rendered at https://rdm.elixir-europe.org/example. This link can be provided to the contributor through the issue.

### Advanced: Working on your own feature branch and pushing local changes

Also as an editor, try to work as much as possible on a different branch than the master branch. This can be on the elixir-europe rdm-toolkit repo or your own fork. Open a pull request if you want to merge your changes with the master branch. This way it is possible for other editors to give feedback on your changes. Typos or other small fixes can off course be done immediately on the master branch. Don't forget to keep your branch/fork up to date with the changes in the master branch.

This is a general workflow if you work on your own fork (copy) of the rdm-toolkit repo:
NOTE: if you already did these steps in the past, start from the `git fetch upstream` command.
- Make a fork of this repository, using the fork button.
- Open a terminal and clone your fork using:
    ```
    git clone git@github.com:USERNAME/rdm-toolkit.git
    cd rdm-toolkit
    ```
    NOTE: Make sure you clone the fork and not the original elixir-europe/rdm-toolkit one.
- Keep your fork up to date (IMPORTANT!).
    ```
    git remote add upstream https://github.com/elixir-europe/rdm-toolkit.git
    git fetch upstream
    git checkout master (if you are not already on the master branch, check with `git branch`)
    git pull upstream master
    ```
- Create a new branch named after your feature/edit.
    ```
    git branch -b 'FEATURE_NAME'
    git checkout 'FEATURE_NAME'
    ```
- Make the changes you want to make using an editor of choice
- Save.
- Open terminal and stage your changes:
    ```
    git add .
    ```
- Committing changes
    ```
    git commit -m "Changing the tool-resource file"
    ```
- Pushing you changes to your fork
    ```
    git push origin 'FEATURE_NAME'
    ```
- Go to [https://github.com/elixir-europe/rdm-toolkit](https://github.com/elixir-europe/rdm-toolkit) and click on *Compare & pull request*
- Open the pull request
- Wait for review by other


## Display a page on the website
By default a page will not show up in the sidepanel on the website, but it will be rendered at https://rdm.elixir-europe.org/file_name.
A page can be displayed in the sidepanel on the website or linked within an existing page.

### Adding page to the sidebar
In order to do so you will have to add the link towards the page to the `.yaml` file in the *_data/sidebars* directory.

### Link page within existing page
* go to the page in which you want to add the link to a new page
* Edit the page by typing: ...


## Linking the github accounts to the contributors
Do you want that the github picture of a contributor is shown next to his name? or maybe you want that the name is clickable and links towards the github page of that person? To enable this please add the name + the necessary metadata to the [CONTRIBUTORS.yaml](https://github.com/elixir-europe/rdm-toolkit/blob/master/_data/CONTRIBUTORS.yaml) file in the *_data* directory.

```


```

## Tagging pages and listing them

### Tagging the pages 
Tagging pages is done by the `tags:` property in the metadata of the markdown page.
Add the tag(s) to a list (square brackets). Make sure your tag corresponds to an existing page. 

This metadata example shows how we tag the "Storage" page with the **research_it** tag:
```md
---
title: Storage
tags: [research_it] 
---
```

### Listing the pages somewhere else

If you than want to list all the pages containing the tag **research_it** you can us the code snippet:

{% raw %}
```
{% include pagelist.html tag='research_it'%}
```
{% endraw %}

Giving:

{% include pagelist.html tag='research_it'%}

This is preferably done on the 'research_it' page. In this way the tag visible on the tagged pages will link to the 'research_it', interlinking everything. 

### Supported tags

To only allow a curated list of tags, make sure you find the tag in the `tags.yaml` file in the `_data` repository. 

## Using the tool/resource list

Here we list all the tools with the tag **monitoring**  by using the code snippet:

{% raw %}
```
{% include toollist.html tag="monitoring" %}
```
{% endraw %}

Giving:

{% include toollist.html tag="monitoring" %}

Make sure the tag exists in the `tool_and_resource_list.yml` file + in the `tags.yml`.

Tools and resources can be added by manipulating the tool_and_resource_list.xlsx file in the `_data` repository.
More information on how to add a tool or resource can be found [here](tool_resource_update).
