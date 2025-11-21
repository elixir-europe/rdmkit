---
title: Style guide
---

In general, we follow the European Commission's [Web Writing Style Guide](https://wikis.ec.europa.eu/display/WEBGUIDE/02.+Web+writing+guidelines) and their more detailed English Style Guide. Search online for "EC English style guide" to find the link, since it changes regularly. Below are the points that you might find most useful, though, and that relate particularly to the RDMkit. 

## General style and tone
  * Keep the tone friendly rather than formal, and use "you". Imagine you were explaining something verbally to someone - how would you say it?
  * Use short, active sentences and short paragraphs (3-4 sentences).
  * Make use of headings and bullet points to break text up so it is easy to scan.
  * Remember that the site is there to help people, so make it clear to the readers how the information can benefit them.
  * Use the words your readers would use. Think of the terms they would use when searching for their problem, and use those terms.

## Text
  * **Acronyms:** spell them out the first time.
  * **Ampersands:** do not use these in the main text or headings. It is fine to use them in menus if you need to save space.
  * **Capitals:** do not use all capitals for emphasis or in headings.
  * **Data:** treat as singular ("Data is..."). (Whether "data" is singular or plural is contentious - see the [Wikipedia article](https://en.wikipedia.org/wiki/Data_(word)) and this [Guardian article](https://www.theguardian.com/news/datablog/2010/jul/16/data-plural-singular).)
  * **Dates:** use Wednesday 7 July 2021 (not Wednesday 7th July 2021, or other variations).
  * **Datasets:** not "data sets".
  * **Email:** not "e-mail".
  * **Email addresses:** spell these out and make the email address the link, e.g. [rdm-toolkit@elixir-europe.org](mailto:rdm-toolkit@elixir-europe.org). Do not hide the email address behind a word or phrase like "contact us".
  * **Etc.** should be avoided. Try using ‘for example’ or ‘such as’ or ‘including’ at the start of a listing. If etc. is used, put a comma before it if it is in a list, like "A, B, etc.". 
  * **Gender:** avoid using gender-specific words like "he" or "she".
  * **Headings:**
    * Only the first word is capitalised unless other words are proper nouns.
    * Headings must be hierarchical. They must go down in order (level one, level two, level three) and not skip a level. It is fine to skip levels when moving back up, e.g. you can skip from level four to level two.
  * **-ise/-ize:** use the "-ise" form.
  * **Life cycle:** two separate words.
  * **Links:** make the link text say where the link goes, e.g. "the Contribute page", not "click here". Avoid using the url as the link text.
  * **Lists:** 
    * _A list of short items_: introduce with a colon, start each bullet point with a capital and don't use punctuation at the end of each bullet point:
      * Item 1
      * Item 2
    * _A list of longer items following an incomplete introductory sentence (e.g. a sentence ending in a colon)_: each item ends with a semi-colon and the final item ends with a full stop. Do not capitalise the first letter of each item, e.g. This is the first part of a sentence that includes:
      * a longer item 1;
      * a longer item 2;
      * a longer item 3.
    * _A list following a complete sentence (with a full stop)_: each item ends with a full stop, and each point begins with a capital letter, e.g. This a complete sentence.
      * This is item 1 of the list.
      * This is item 2 of the list.
      * This is item 3 of the list.
  * **Numbers:** spell the numbers one to ten out. After that, write the numbers (11, 12, 13, etc.).
  * **Quotations:** use double quotes for quotations and single quotes for quotes within quotes.
  * **References:**
    * add your citations as bibtex to the `_bibliography/references.bib` file
    * add `{% cite reference_key %}` to the text where you are citing the reference
    * add  `## Bibliography` `{% bibliography --cited %}` to show a bibliography section with cited refrences on a page.
  * **That/which:** use "that" when you are defining something and "which" when you are adding extra information about it e.g.:
    * "The cat that was on the table suddenly got up" is telling us which cat it was. It is important to the meaning of the sentence because you are not talking about any cat, just the cat on the table.
    * "The cat, which was sitting on the table, suddenly got up" is giving us extra information about the cat. The information is not necessary to understand the sentence. You can remove the clause, and the sentence will still be clear. Clauses starting with "which" usually begin with a comma.
  * **Titles (the "title" in the front matter of pages):** only the first word, proper nouns and acronyms are capitalised.
  * **Tool assembly:** there are multiple tools in **one** assembly. The plural is "tool assemblies".
  * **Training:** training is an uncountable noun and cannot have a plural. You can write "training courses" and "training materials" but not "trainings".

## Bibliography
 * RDMkit uses BibTeX to create page bibliographies.
 * Follow these instuctions to create and display a bibiography on your page:
   1. Add your citations in the `_bibliography/references.bib` file. Refer to the instructions below for more information on the format.
   1. Add {% raw %} `{% cite reference_key %}` {% endraw %} to the text where you are citing one of your entries.
   1. Add {% raw %} `## Bibliography {% bibliography --cited %}` {% endraw %} in your page to show a bibliography section containing the references you have added following the instructions in the previous point. 
* We use a display class based on *Nature* publications. Your BibTeX files should follow a standardised format described below.
  We recommend using {% tool "zotero" %} to automate the process (see below). Alternatively, consider using one of the [converters](https://www.bibtex.com/converters/) from {% tool "paperpile" %}
* An example of the minimal structure required for BibTeX entries is:

```
﻿@article{surname12024lorem,
  title = {Lorem Ipsum},
  author = {Surname1, Alice and Surname2, Bob}
  journal = {Journal},
  volume = {1},
  pages = {1--10},
  year = {2024},
  number = {1},
  doi = {DOI},
  langid = {english}
}
```
Make sure that the *author* field does not contain *et al.*, as this substitution is performed via the class and should
not be part of the information provided by the contributors.

* If you are a {% tool "zotero" %} user, we recommend that you:
  1. Install the {% tool "better-bibtex" %} plugin.
  1. On your desktop version of {% tool "zotero" %}, open the *Better BibTeX preferences* (under *Tools > Better BibTeX*).
  in the *citation keys* tab, change the *citation key formula* to `auth.lower + year + shorttitle(1,0)`
  1. Import the file e.g. by using *Add item by identifier*.
  1. Right click on the item and select *Export item*. Select the *Better BibLateX* format and export.
  1. Edit the resulting .bib file if necessary, and append it to `_bibliography/references.bib`.
  * Optionally, if you have a Zotero account and would like to contribute to RDMkit group library,
  import the items to [this group](https://www.zotero.org/groups/5371154/rdmkit)

## Graphic design
  * **White space:** make sure there is plenty of space so that the main elements stand out and the text does not appear overwhelming.
  * **Colours:** <br/>
    * The headings, links and text will automatically appear in the right colour if you use the site page templates.
    * Use only the following colours in the design, text and illustrations of the site. The RDM life cycle diagram colours are only for use in the pages related to the diagram.
    * | <span style="display: inline-block; width: 20px; height: 20px; background: #C23669;"></span> | #C23669 | Magenta | Logo, Menu highlight, Second level heading (h2), Main theme colour |
      | <span style="display: inline-block; width: 20px; height: 20px; background: #337ab7;"></span> | #376AC3 | Blue | Link colour |
      | <span style="display: inline-block; width: 20px; height: 20px; background: #2a2e3d;"></span> | #2a2e3d | Dark blue | First level headings (h1), Third level heading (h3), Body text, Header, Footer |
      | <span style="display: inline-block; width: 20px; height: 20px; background: #73757d;"></span> | #73757d | Gray | Gray text, Fourth level heading (h4) |
      | <span style="display: inline-block; width: 20px; height: 20px; background: #f3f1f2;"></span> | #f3f1f2 | Light gray | Box backgrounds |
  * **Fonts:** Exo 2 is used for headings and main branding font, Open Sans for body text.
  * **Icons:** the icons used in the data life cycle diagram come from the [Noun Project](https://thenounproject.com/ELIXIRCommunications/kit/rdmkit/). We have a Pro license and the right to publish them without attribution. Other icons on this site are either desgined by Xènia Pérez Sitjà or come from [Font Awesome](https://fontawesome.com/).
  * **Templates:** keep the structure of the pages consistent by using the site templates (see the [contribute page](how_to_contribute)).
  * **Illustrations:** use the colours listed above. The icons we use for illustrations come from the [Noun Project](https://thenounproject.com/ELIXIRCommunications/kit/rdmkit/). Please use these icons in any illustrations. If you need extra icons or any help with illustrations, [open a new issue](https://github.com/elixir-europe/rdmkit/issues) on GitHub or email [rdm-toolkit@elixir-europe.org](mailto:rdm-toolkit@elixir-europe.org).
  * **Images:**
    * Do not use images to display text.
    * Include an 'alt' attribute in images.

## Naming of files, tags, keywords, and navigation titles

* **Markdown file names:**
  * Do not contain spaces or special characters like &, %, #, (, ), è, é, ê, ë, ...
  * Are unique across the website.
  * Are lowercase, except for acronyms.
* **Tags for tools, resources and pages:**
  * Do not contain special characters like &, %, #, (, ), è, é, ê, ë, ...
  * Are lowercase, except for acronyms.
  * Are short if possible but distinguishable from existing tags.
  * Can contain spaces.
* **Keywords:**
  * Are lowercase.
  * Can contain spaces.
* **Titles in the navigation side panel:**
  * First word and acronyms capitalised.
  * Should contain the same words as the filename where this title points to.


## How to suggest amendments or additions to this style guide
[Open a new issue](https://github.com/elixir-europe/rdmkit/issues) on GitHub or email [rdm-toolkit@elixir-europe.org](mailto:rdm-toolkit@elixir-europe.org). See also the [contribute page](how_to_contribute).
