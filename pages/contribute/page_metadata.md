---
title: Page metadata
---


In order to render the website, each markdown file contains a specific frontmatter/metadata section. This section is located at the top of the markdown file, is delimited by two times `---` and contains all key value pairs. This can be seen as settings on pagelevel to enable/disable certain page functions are to deliver extra information which can be displayed in a structured way. An example of how this can look like:

```yaml
---
title: Title of the page
---
```

## Possible metadata attributes of a page


* `title`: Specify here the title of the page. This wil be the H1 title (replacing the top level title using the # in markdown )

* `description`: Short sentence about the page starting with a lowercase. This sentence is visualized when pages are automatically listed using a tag.

* `contributors`: list here all the contributors that helped in establishing the page. This will be the full name of the person. Make sure that the person name that is listed can be found in the CONTRIBUTORS.yaml file in the _data directory if you want to link the github id and other contact information.

* `coordinators`: List here all the coordinators of the page. Use the full name of the person. Make sure that the person name that is listed can be found in the *_data/CONTRIBUTORS.yaml* file in the _data directory if you want to link the github id and other contact information.

* `editors`: List here all the editors of the page. Use the full name of the person. Make sure that the person name that is listed can be found in the *_data/CONTRIBUTORS.yaml* file in the _data directory if you want to link the github id and other contact information.

* `search_exclude`: by setting this field true, the page will not end up in the search results of the searchbar. By default this is false.

* `sitemap`: let the page appear in the sitemap.xml. Default: true

* `no_robots`: by setting this field to true, the page will not end up in the search results of google or any other search engine.

* `toc`: When set to false, the table of contents in the beginning of the page will not be generated.

* `page_id`: Unique identifier of a page. It is usually a shortened version of the page name or title, with small letters and spaces, or an acronym, with capital and small letters. Used to list Related pages.

* `datatable`: use this attribute to activate the pagination + sorting + searching in tables

* `affiliations`: List here all affiliations related to the page. Make sure that the person name that is listed can be found in the _data/affiliations.yaml file. These affiliations will get displayed at the bottom of the page and in the section navigation tile of the page.

### Related pages

* `related_pages`: List here the `page_id` of {{site.title}} pages that you want to display as Related pages, grouped by section.

  If you want pages from the specific section (Your tasks, Your domain, Tool assembly) to be shown here as Related pages, list their `page_id`. If you want to list multiple related pages, make sure to put them in a list like this: [page_id1, page_id2]. The specific sections allowed in each page are specified in each page template. Please, do not add extra sections in the metadata of the page.

  ```yml
  related_pages: 
    - Your_tasks: [page_id1, page_id2]
    - Your_domain: [page_id1, page_id2]
    - Tool_assembly: [page_id1, page_id2]
  ``` 


### More information


* `training`: List here training material relevant for the page. We recommend to add your training material in TeSS. However, you can also list here training material that is not yet present in TeSS.

  ```yml
  training:
    - name: Training in TeSS
      registry: TeSS
      url: https://tess.elixir-europe.org/search?q=data%20analysis

    - name: Training in X
      registry: 
      url: example_url
  ```

  The supported registries that can be used in the `registry` attribute are: *YouTube*, *Zenodo*, *Carpentries*, *GitHub* and *TeSS*.

* `faircookbook`: Here all relevant FAIR Cookbook recipes are listed. This is automatically updated based on the [`faircookbook_rdmkit_mapping.yml`](https://github.com/elixir-europe/faircookbook-rdmkit/blob/main/faircookbook_rdmkit_mapping.yml) mapping file. If you want to make a new link, please make a pull request against this file. Every week the changes of this mapping file are used to update the frontmatter of the corresponding markdown files.


* `dsw`: Here all relevant Data Stewardship Wizard questions in the Researcher knowledge model are listed. This is automatically updated and can not be altered by humans! If you want to add a link you have to add the link towards the RDMkit page the the knowledge model on DSW.

* `fairsharing`: This attribute list the FAIRsharing collection that is built based on the standards and databases that are listed on that page. This is automatically updated and can not be altered by humans! If you want to add a resource to the collection you have to add the resource the the page and link to the FAIRsharing identifier from the tool_and_resource_list.yml.


### Tools and resources

The main tools are described in the mains tools and resources table. How to add a tool are resource can be read [here](tool_resource_update). Using the page metadata attributes to describe tools is only used in national resource pages. We support two types: 


* `ref_to_main_resources`: Refer to entries of the "main_tool_ and_resource_table" if institutions, organizations and projects from the country contribute to the development of international tools and resources. List the nme of the tool your refer to in the main tools table.

  ```yml
  ref_to_main_resources: 
    -  Resource name
  ```
* `national_resources`: List here tools and resources mainly relevant for the specific country
  
  ```yml
  national_resources: 
    - name: Resource name
      description: A general description about the resource.
      how_to_access: explantation on how you can access this resource
      instance_of: github
      related_pages:
        example_pages: [gp3, gp1, gp2]
      registry:
        biotools: bioconda
        tess: Bioconda
      url:
  ```


