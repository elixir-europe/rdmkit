---
title: Page metadata
---


## Possible metadata attributes of a page


In order to render the markdown file to the website, it needs a specific frontmatter/metadata section in the top part of the file. This latter can look like:

```
---
title: Title of the page
---
```

Mandatory metadata/frontmatter:
* `title`: Specify here the page title. This will be the H1 title (replacing the top level title using the # in markdown )

Optional metadata/frontmatter: 

* `summary`: By using this attribute it is possible to specify a summary which will be displayed under the page title.

* `description`: Short sentence about the page starting with a lowercase. This sentence is visualized when pages are automatically listed as Related page.

* `contributors`: List here all the contributors that helped in establishing the page, preferibly with their full name. Make sure that the person names that are listed can be found in the CONTRIBUTORS.yaml file in the *_data* directory if you want to link the GitHub ID and other contact information. Multiple contributors will be put in a list like this: [example1, example2].

* `coordinators`: List here the names of the people responsible for the content of the page. People responsible for the content of the National resources pages can be members of the ELIXIR data management network. Make sure that coordinators also listed as contributors in `contributors` and CONTRIBUTORS.yaml. Multiple coordinators will be put in a list like this: [example1, example2].

* `search_exclude`: By setting this field to "true", the page will not end up in the search results of the search bar. `search_exclude: true` is the default for template pages. Make sure to delete this metadata field when creating a new page for contributors, before approving or before merging a pull request.

* `sitemap`: let the page appear in the sitema.xml. Default: true

* `no_robots`: by setting this field to true, the page will not end up in the search results of google or any other search engine.

* `hide_sidebar`: When true, the sidebar will be hidden. Default: false.

* `custom-editme`: This attribute can be used to specify an alternative file/link when clicked on the edit-me button.

* `keywords`: List here all the keywords that can be used to find the page using the search box in the right-upper corner of the page. Multiple keywords are put in a list like this: [example1, example2].

* `sidebar`: Specify here an alternative sidebar. Default: main.

* `toc`: When set to false, the table of contents at the beginning of the page will not be generated.

* `affiliations`: List here all affiliations that made this page possible. This is especially used for tool assembly pages. Countries use the ISO 3166-1-alpha-2 notation, other affiliations must be present in the affiliations.yaml in the _data directory in order to work.

* `page_id`: Unique identifier of a page. It is usually a shortened version of the page name or title, with small letters and spaces, or an acronym, with capital and small letters. Used to list Related pages.

* `related_pages`: List here the page_id of RDMkit pages that you want to display as Related pages, grouped by section (Your tasks, Your domain, Tool assembly).

  If you want pages from the specific section (Your tasks, Your domain, Tool assembly) to be shown here as Related pages, list their `page_id`. If you want to list multiple related pages, make sure to put them in a list like this: [page_id1, page_id2]. The specific sections allowed in each page are specified in each page template. Please, do not add extra sections in the metadata of the page.
  ```yml
  related_pages: 
    your_tasks: [page_id1, page_id2]
    your_domain: [page_id1, page_id2]
    tool_assembly: [page_id1, page_id2]
    ``` 

* `training`: List here training material relevant for the page. We recommend to add your training material in TeSS. However, you can also list here training material that is not yet present in TeSS. Each training item will be automatically added as an entry to the table in the [All training resources page](all_training_resources). If the registry is specified, please use one of the following: TeSS, Youtube, Zenodo or Carpentries.

  ```yml
  training:
    - name: Training in TeSS
      registry: TeSS
      url: https://tess.elixir-europe.org/search?q=data%20analysis

    - name: Training in TeSS
      registry: TeSS
      url: https://tess.elixir-europe.org/search?q=data%20analysis
  ```
* `faircookbook`: Here all relevant FAIR Cookbook recipes are listed. This is automaticity updated based on the [`faircookbook_rdmkit_mapping.yml`](https://github.com/elixir-europe/faircookbook-rdmkit/blob/main/faircookbook_rdmkit_mapping.yml) mapping file. If you want to make a new link, please make a pull request against this file. Every week the changes of this mapping file are used to update the frontmatter of the corresponding markdown files.


* `dsw`: Here all relevant Data Stewardship Wizard questions in the RDMkit knowledge model are listed. This is automaticity updated and can not be altered by humans! If you want to add a link you have to add the link towards the RDMkit page the the knowledge model on DSW.

* `datatable`: use this attribute to activate the pagination + sorting + searching in tables
