---
title: Style guide
sidebar: contribute
---

In general, we follow the European Commission's [Web Writing Style Guide](https://wikis.ec.europa.eu/display/WEBGUIDE/02.+Web+writing+guidelines). Below are the points that you might find most useful, though, and that relate particularly to the RDMkit.

## General style and tone
  * Keep the tone friendly rather than formal, and use "you". Imagine you were explaining something verbally to someone - how would you say it?
  * Use short, active sentences and short paragraphs (3-4 sentences).
  * Make use of headings and bullet points to break text up so it is easy to scan.
  * Remember that the site is there to help people, so make it clear to the readers how the information can benefit them.
  * Use the words your readers would use. Think of the terms they would use when searching for their problem, and use those terms.

## Text
  * **Acronyms:** spell them out the first time.
  * **Ampersands:** do not use these in the main text or headings. It is fine to use them in menus, if you need to save space.
  * **Capitals:** do not use all capitals for emphasis or in headings.
  * **Data:** treat as singular ("Data is..."). (Whether "data" is singular or plural is contentious - see the [Wikipedia article](https://en.wikipedia.org/wiki/Data_(word)) and this [Guardian article](https://www.theguardian.com/news/datablog/2010/jul/16/data-plural-singular).)
  * **Dates:** use Wednesday 7 July 2021 (not Wednesday 7th July 2021, or other variations).
  * **"Datasets":** not "data sets". 
  * **"Email":** not "e-mail".
  * **"Email addresses":** spell these out and make the email address the link e.g. [rdm-toolkit@elixir-europe.org](mailto:rdm-toolkit@elixir-europe.org). Do not hide the email address behind a word or phrase like "contact us".
  * **Gender:** avoid using gender-specific words like "he" or "she".
  * **Headings:**
    * Only the first word is capitalised, unless other words are proper nouns.
    * Headings must be hierarchical. They must go down in order (level one, level two, level three), and not skip a level. It is fine to skip levels when moving back up e.g. you can skip from level four to level two.
  * **-ise/-ize:** use the "-ise" form.
  * **"Life cycle":** two separate words.
  * **Links:** make the link text say where the link goes e.g. "the Contribute page", not "click here". Avoid using the url as the link text.
  * **Lists:** every line of a list starts with a capital and ends with a full stop.
  * **Numbers:** spell the numbers one to ten out. After that, write the numbers (11, 12, 13, etc).
  * **Quotations:** use double quotes for quotations, and single quotes for quotes within quotes.
  * **References:** use the [Nature Author instructions](https://www.nature.com/srep/author-instructions/submission-guidelines#references) for books and papers. Use "<i>et al.</i>" for more than five authors.
    * Bellin, D. L. <i>et al.</i> Electrochemical camera chip for simultaneous imaging of multiple metabolites in biofilms. Nat. Commun. 7, 10535; [10.1038/ncomms10535](http://www.nature.com/articles/ncomms10535) (2016).
    * Lam, J. <cite>Data Management</cite>. (John Wiley & Sons, Inc., 2019).
  * **That/which:** use "that" when you are defining something and "which" when you are adding extra information about it e.g.:
    * "The cat that was on the table suddenly got up" is telling us which cat it was. It is important to the meaning of the sentence because you are not talking about any cat, just the cat on the table.
    * "The cat, which was sitting on the table, suddenly got up" is giving us extra information about the cat. The information is not necessary to understand the sentence. You can remove the clause and the sentence will still be clear. Clauses starting with "which" usually begin with a comma.
  * **Titles:** Only the first word and acronyms are capitalised.
  * **Training:** training is an uncountable noun and cannot have a plural. You can write "training courses" and "training materials" but not "trainings".

## Graphic design
  * **White space:** make sure there is plenty of space space so that the main elements stand out and the text does not appear overwhelming.
  * **Colours:** <br />
    * The headings, links and text will automatically appear in the right colour if you use the site page templates.
    * Use only the following colours in the design, text and illustrations of the site. The RDM life cycle diagram colours are only for use in the pages related to the diagram.
    * | <span style="display: inline-block; width: 20px; height: 20px; background: #C23669;"></span> | #C23669 | Magenta | Logo, Menu highlight, Second level heading (<h2>), Main theme colour |
      | <span style="display: inline-block; width: 20px; height: 20px; background: #337ab7;"></span> | #376AC3 | Blue | Link colour |
      | <span style="display: inline-block; width: 20px; height: 20px; background: #2a2e3d;"></span> | #2a2e3d | Dark blue | First level headings (<h1>), Third level heading (<h3>), Body text, Header, Footer |
      | <span style="display: inline-block; width: 20px; height: 20px; background: #83858e;"></span> | #83858e | Gray | Gray text, Fourth level heading (<h4>) |
      | <span style="display: inline-block; width: 20px; height: 20px; background: #f3f1f2;"></span> | #f3f1f2 | Light gray | Box backgrounds |
  * **Fonts:** Exo 2 is used for headings and main branding font, Open Sans for body text.
  * **Templates:** keep the structure of the pages consistent by using the site templates (see the [contribute page](how_to_contribute)).
  * **Illustrations:** use the colours listed above. (To do: agreed styles for boxes, arrows, and icons for things like users and databases.)
  * **Images:**
    * Do not use images to display text.
    * Include an 'alt' attribute in images.

## Naming of files, tags, keywords, and navigation titles

* **Markdown file names:**
  * Do not contain spaces or special characters like &, %, #, (, ), è, é, ê, ë, ...
  * Are unique among the website.
  * Are lowercase, except for acronyms.
* **Tags for tools, resources and pages:**
  * Do not contain special characters like &, %, #, (, ), è, é, ê, ë, ...
  * Are lowercase, except for acronyms.
  * Are short if possible, but distinguishable from existing tags.
  * Can contain spaces.
* **Keywords:**
  * Are lowercase.
  * Can contain spaces.
* **Titles in the navigation side panel:**
  * First word and acronyms capitalised.
  * Should contain the same words as the filename where this title points to. 

## RDMkit logo flavours in png and vector (svg)

* RDMkit logo horizontal

  <p>
    <img src="{{ 'assets/img/RDMkit_logo.svg' | relative_url }}" style="max-width: 20%; max-height: 5em; vertical-align: middle" /> 
      [<a href="{{ 'assets/img/RDMkit_logo.svg' | relative_url }}">svg</a>]
      [<a href="{{ 'assets/img/RDMkit_logo.png' | relative_url }}">png</a>]
  </p>

* RDMkit logo horizontal inverted

  <p>
    <img src="{{ 'assets/img/RDMkit_logo_inverted.svg' | relative_url }}" style="max-width: 20%; max-height: 5em; vertical-align: middle" />
      [<a href="{{ 'assets/img/RDMkit_logo_inverted.svg' | relative_url }}">svg</a>]
      [<a href="{{ 'assets/img/RDMkit_logo_inverted.png' | relative_url }}">png</a>]
  </p>

* RDMkit logo condensed

  <p>
    <img src="{{ 'assets/img/RDMkit_logo_condensed.svg' | relative_url }}" style="max-width: 20%; max-height: 5em; vertical-align: middle" />
      [<a href="{{ 'assets/img/RDMkit_logo_condensed.svg' | relative_url }}">svg</a>]
      [<a href="{{ 'assets/img/RDMkit_logo_condensed.png' | relative_url }}">png</a>]
  </p>

* RDMkit logo condensed inverted

  <p>
    <img src="{{ 'assets/img/RDMkit_logo_condensed_inverted.svg' | relative_url }}" style="max-width: 20%; max-height: 5em; vertical-align: middle" />
      [<a href="{{ 'assets/img/RDMkit_logo_condensed_inverted.svg' | relative_url }}">svg</a>]
      [<a href="{{ 'assets/img/RDMkit_logo_condensed_inverted.png' | relative_url }}">png</a>]
  </p>


## How to suggest amendments or additions to this style guide
[Open a new issue](https://github.com/elixir-europe/rdmkit/issues) on GitHub or email [rdm-toolkit@elixir-europe.org](mailto:rdm-toolkit@elixir-europe.org). See also the [contribute page](how_to_contribute).
