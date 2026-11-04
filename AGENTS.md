# AGENTS.md

Instructions for AI coding assistants working in the RDMkit repository. This file is
assistant-agnostic: tools that follow the `AGENTS.md` convention read it directly, and
you can point any other assistant at it manually.

Claude Code is an exception — it reads `CLAUDE.md`, never `AGENTS.md`. The repository
root therefore has a one-line `CLAUDE.md` containing `@AGENTS.md`, which imports this
file at session start. Keep the shared instructions here; that file only bridges them.

RDMkit (<https://rdmkit.elixir-europe.org>) is an ELIXIR research data management
knowledge hub. It is a Jekyll site whose content is Markdown, reviewed by a human
editorial board. **You are contributing prose to a curated, citable resource, not code
to an application.** Accuracy and house style matter more than volume.

This file deliberately does **not** restate the contribution guidelines. They live in
`pages/contribute/` and are the single source of truth for humans and assistants alike.
Read the relevant ones before you start (see [Read before writing](#read-before-writing)).

## Ground rules

1. **Never invent facts.** Do not fabricate ORCIDs, affiliations, DOIs, tool URLs,
   FAIRsharing/bio.tools/TeSS identifiers, standards, or repository capabilities.
   Verify every identifier against the authoritative source, or leave the field out
   and say what is missing.
2. **Every claim on a page should be defensible.** Prefer statements a domain expert
   would sign off on. Cite the literature where a claim is contested or specific.
3. **Follow the contribution guidelines** in `pages/contribute/`, not your own idea of
   good style. In particular, RDMkit uses British `-ise` spelling and sentence-case
   headings.
4. **Follow the templates.** Each section has a `TEMPLATE_*.md` file that defines the
   required heading structure and front matter, with guidance in HTML comments. Do not
   invent new section shapes.
5. **Leave a review trail.** Report what you could not verify rather than papering
   over it. A pull request goes to the editorial board, so unresolved items belong in
   the PR description.

## Read before writing

| Task | Read |
|---|---|
| Any page content | [style_guide.md](pages/contribute/style_guide.md) |
| New page | the section's `pages/*/TEMPLATE_*.md`, [page_metadata.md](pages/contribute/page_metadata.md), [editorial_board_guide.md](pages/contribute/editorial_board_guide.md) (sidebar, news item, related pages, page IDs) |
| Links, images, callouts | [markdown_cheat_sheet.md](pages/contribute/markdown_cheat_sheet.md) |
| Mentioning or adding a tool | [tool_resource_update.md](pages/contribute/tool_resource_update.md) |
| Citations | the Bibliography section of [style_guide.md](pages/contribute/style_guide.md#bibliography) |
| Contributors | the contributors section of [editorial_board_guide.md](pages/contribute/editorial_board_guide.md#adding-extra-info-to-the-contributors) |
| Copyright | [copyright.md](pages/contribute/copyright.md) |
| Before you finish | [editors_checklist.md](pages/contribute/editors_checklist.md) |

These files are Jekyll pages, so they contain Liquid tags such as `{% include %}` and
`{% raw %}`. Read through them for the content.

## Repository layout

| Path | Purpose |
|---|---|
| `pages/your_tasks/` | Task pages: generic RDM problems (metadata, storage, licensing) |
| `pages/your_domain/` | Domain pages: research-field-specific RDM (proteomics, plant sciences) |
| `pages/your_role/` | Role pages (data steward, researcher, policy officer) |
| `pages/tool_assembly/` | Tool assembly pages: coherent sets of tools for a use case |
| `pages/national_resources/` | Per-country resource pages |
| `pages/data_life_cycle/` | Data life cycle stage pages |
| `pages/contribute/` | The contribution guidelines (see above) |
| `_data/tool_and_resource_list.yml` | The single tool and resource table (all `{% tool %}` targets) |
| `_data/CONTRIBUTORS.yaml` | Contributor names, GitHub IDs, ORCIDs, affiliations |
| `_data/sidebars/data_management.yml` | Navigation menu for all content pages |
| `_data/news.yml` | Site news items |
| `_bibliography/references.bib` | BibTeX for all `{% cite %}` references |
| `var/tools_validator.py` | CI validator for the tool table and page metadata |
| `.github/workflows/` | Jekyll build, link check, tool validation, PR checklist |

The theme is remote (`ELIXIR-Belgium/elixir-toolkit-theme`), so layouts and includes
are **not** in this repository. Do not go looking for `_includes/` or `_layouts/`.

## Common mistakes

These rules are documented in the guidelines but are the most frequent causes of broken
pull requests:

- **In-text links use the file name, `related_pages` uses the `page_id`.** They often
  differ. See [Linking to internal pages](pages/contribute/markdown_cheat_sheet.md#linking-to-internal-pages).
  Verify every link target exists as a file before finishing.
- **`{% tool "id" %}` renders the tool's full `name`.** Check the `name` field before
  writing the surrounding sentence, or you will double the spelled-out form. See
  [tool_resource_update.md](pages/contribute/tool_resource_update.md#linking-the-tool-or-resource-in-the-text-with-the-main-yaml-file).
- **Tagging a tool is what lists it at the bottom of the page.** Tag every tool you
  describe, and do not tag one in passing that you do not want listed.
- **`search_exclude: true` comes from the template** and must be deleted from a new
  content page.
- **`fairsharing:` and `dsw:` in page front matter are machine-generated.** Never edit
  them by hand.
- **`related_pages` is not a valid key on a tool entry** in
  `_data/tool_and_resource_list.yml`; the validator rejects it.

## Verifying identifiers

Humans can look things up in a browser; you should query the source directly:

- bio.tools: `https://bio.tools/api/tool/<id>/?format=json`
- TeSS: `https://tess.elixir-europe.org/materials.json_api?q="<name>"`
- DOIs: `https://api.crossref.org/works/<DOI>`. Use the complete author list from
  CrossRef in the BibTeX entry, and brace-protect case-sensitive words in titles
  (`{{mzTab-M}: A Data Standard…}`).
- FAIRsharing: the API needs credentials. If you cannot verify a FAIRsharing ID,
  **omit it**; a weekly GitHub Action fills registry links in automatically.

## Before you finish

Work through [editors_checklist.md](pages/contribute/editors_checklist.md), which is
posted automatically on every pull request touching `pages/`. Also check that:

- every in-text link resolves to a real page file name;
- every `{% cite %}` key exists in `_bibliography/references.bib`;
- every tool you added to the table is used on some page;
- cross-references are reciprocal where it helps the reader: if page A tells readers
  to read page B alongside it, add the matching pointer to B.

## Useful local checks

```bash
# Tool table + page metadata validation (needs ruamel.yaml, requests, python-frontmatter)
python var/tools_validator.py

# Build and serve the site locally
bundle install && bundle exec jekyll serve

# YAML parses
ruby -ryaml -e 'YAML.load_file("_data/tool_and_resource_list.yml"); puts "ok"'
```

Note that `python var/tools_validator.py` **rewrites** `_data/tool_and_resource_list.yml`
in place (normalising key order). Check the resulting diff before committing.

## Scope

Do not restructure the site, change the theme, rewrite unrelated pages, or "fix" the
style of pages you were not asked to touch. Pull requests are reviewed by volunteers;
keep the diff to the task at hand.
