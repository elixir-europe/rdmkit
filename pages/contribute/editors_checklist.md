---
title: Editors checklist
summary: Checklist for editors before approving and merging a pull request (PR).
---

## Before approving and merging a pull request (PR), the editors must check that
1. The page layout in preview looks correct.
2. The new page is linked in the appropriate [sidebar](https://github.com/elixir-europe/rdmkit/tree/master/_data/sidebars) menu, in the same branch of the PR.
3. The contributors' names are listed in the [CONTRIBUTORS file](https://github.com/elixir-europe/rdmkit/blob/master/_data/CONTRIBUTORS.yaml), in the same branch of the PR. Advice to have at least one  contributor per page having its contact information in this  [CONTRIBUTORS file](https://github.com/elixir-europe/rdmkit/blob/master/_data/CONTRIBUTORS.yaml).
4. All relevant metadata fields in a specific page are correctly filled in (see the [Editorial board guide](editorial_board_guide) and the [Markdown cheat sheet](markdown_cheat_sheet)). Some critical ones are listed below.
   * unique `page_id` ([Website overview](website_overview)).
   * `contributors`
   * `related_pages` ([Related pages](editorial_board_guide.html#related-pages))
   * `training`
   * `search_exclude` must be deleted
   * `description`
   * `affiliation`
   * `coordinators`(only used in national pages + they must be listed as `contributors` as well)
   * `resources`
5. Items in the "[all tools and resources spreadsheet](https://docs.google.com/spreadsheets/d/16RESor_qQ_ygI0lQYHR23kbZJUobOWZUbOwhJbLptDE/edit#gid=268211668)" are tagged with already existing (merged) `page_id` from "Your role, Your domain, Your tasks, Tool assembly" and that Bert has been informed of the changes.
6. The content is conform to RDMkit scope, [style](style_guide) and templates.
7. There are no [copyright](copyright) issues related to the content of the page.
8. The contributors implemented the requested changes.
9. When a new page is added, a news item is added to the [news.yml file](https://github.com/elixir-europe/rdmkit/blob/master/_data/news.yml), in the same branch of the PR.
10. The contributors are thanked for their effort and informed about the publication of their content.
11. The PR is linked to related issues and can be merged in main branch with no conflicts.
