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

## Ground rules

1. **Never invent facts.** Do not fabricate ORCIDs, affiliations, DOIs, tool URLs,
   FAIRsharing/bio.tools/TeSS identifiers, standards, or repository capabilities.
   Verify every identifier against the authoritative source, or leave the field out
   and say what is missing.
2. **Every claim on a page should be defensible.** Prefer statements a domain expert
   would sign off on. Cite the literature where a claim is contested or specific.
3. **Follow the human style guide**, at [pages/contribute/style_guide.md](pages/contribute/style_guide.md).
   The summary below is a working checklist, not a replacement for it.
4. **Follow the templates.** Each section has a `TEMPLATE_*.md` file that defines the
   required heading structure and front matter. Do not invent new section shapes.
5. **Leave a review trail.** Report what you could not verify rather than papering
   over it. A pull request goes to the editorial board, so unresolved items belong in
   the PR description.

## Repository layout

| Path | Purpose |
|---|---|
| `pages/your_tasks/` | Task pages: generic RDM problems (metadata, storage, licensing) |
| `pages/your_domain/` | Domain pages: research-field-specific RDM (proteomics, plant sciences) |
| `pages/your_role/` | Role pages (data steward, researcher, policy officer) |
| `pages/tool_assembly/` | Tool assembly pages: coherent sets of tools for a use case |
| `pages/national_resources/` | Per-country resource pages |
| `pages/data_life_cycle/` | Data life cycle stage pages |
| `pages/contribute/` | The contribution guide, style guide and editors' checklist |
| `pages/*/TEMPLATE_*.md` | Section template — read before writing a new page |
| `_data/tool_and_resource_list.yml` | The single tool and resource table (all `{% tool %}` targets) |
| `_data/CONTRIBUTORS.yaml` | Contributor names, GitHub IDs, ORCIDs, affiliations |
| `_data/sidebars/data_management.yml` | Navigation menu for all content pages |
| `_data/news.yml` | Site news items |
| `_bibliography/references.bib` | BibTeX for all `{% cite %}` references |
| `var/tools_validator.py` | CI validator for the tool table and page metadata |
| `.github/workflows/` | Jekyll build, link check, tool validation, PR checklist |

The theme is remote (`ELIXIR-Belgium/elixir-toolkit-theme`), so layouts and includes
are **not** in this repository. Do not go looking for `_includes/` or `_layouts/`.

## The three gotchas that cause most broken pull requests

These are not obvious from the files, and they are easy to get wrong.

### 1. In-text links use the FILENAME; `related_pages` uses the `page_id`

Permalinks are `/:basename` (see `_config.yml`), so a Markdown link resolves against
the **file name**, not the `page_id`. The two frequently differ:

| File | `page_id` | In-text link must be |
|---|---|---|
| `pages/your_tasks/metadata_management.md` | `metadata` | `[metadata](metadata_management)` |
| `pages/your_tasks/data_sensitivity.md` | `sensitive` | `[data sensitivity](data_sensitivity)` |
| `pages/your_tasks/data_management_plan.md` | `dmp` | `[DMP](data_management_plan)` |
| `pages/tool_assembly/galaxy_assembly.md` | `galaxy` | `[Galaxy](galaxy_assembly)` |

`related_pages:` in the front matter takes the **`page_id`**. Links are relative and
carry no leading slash and no `.md`. Verify every link target exists before finishing.

### 2. `{% tool "id" %}` renders the tool's full `name` field

The tag expands to the `name` value from `_data/tool_and_resource_list.yml` as link
text. Many names already contain the spelled-out form and the acronym, so wrapping the
tag in your own spelled-out form produces doubled text:

```markdown
<!-- WRONG: renders "the Universal Spectrum Identifier (Universal Spectrum Identifier (USI))" -->
the Universal Spectrum Identifier ({% tool "usi" %})

<!-- RIGHT -->
the {% tool "usi" %}
```

Check the `name` field before writing the surrounding sentence. Using the bare tag
usually satisfies the spell-out-acronyms rule for free.

### 3. Mentioning a tool is what puts it in the page's tool table

The "Tools and resources on this page" block at the bottom of a page is generated
purely from the `{% tool %}` tags in that page's body. So:

- every tool named in the text should be tagged, if it is in the table;
- every tool you add to the table must be used on some page, or it is dead weight;
- do not tag a tool in passing that you do not want listed at the bottom.

## Writing style checklist

From the [style guide](pages/contribute/style_guide.md) (European Commission English
Style Guide as the base):

**Tone.** Friendly, not formal. Address the reader as "you". Short, active sentences.
Paragraphs of 3–4 sentences. Use headings and bullets so the page is scannable. Make
the benefit to the reader explicit. Use the words readers would search for.

**Spelling and usage.**

- British `-ise`, never `-ize` (`randomise`, `normalisation`, `organisation`).
- "data" is singular: "data is heterogeneous".
- "datasets", not "data sets"; "email", not "e-mail"; "life cycle", two words.
- "training" is uncountable — "training materials", never "trainings".
- "tool assembly" / "tool assemblies".
- Spell out acronyms on first use.
- Spell out numbers one to ten; use numerals from 11 up.
- No ampersands in body text or headings. Avoid "etc." — prefer "for example",
  "such as", "including".
- Dates as "Wednesday 7 July 2021".
- Gender-neutral throughout; use they/them where a pronoun is needed.
- "that" defines, "which" adds information (and takes a comma).
- Double quotes for quotations, single quotes for nested quotes.

**Headings.** Sentence case — only the first word, proper nouns and acronyms are
capitalised. Never skip a level going down (h2 → h3 → h4); skipping back up is fine.
No all-caps.

**Links.** Link text says where the link goes ("the Contribute page", not "click
here"). Never use a bare URL as link text. Spell out email addresses and make the
address itself the link.

**Lists.** Three permitted forms:

- short items after a colon: capitalised, no terminal punctuation;
- longer items after an incomplete sentence ending in a colon: lowercase, semicolons,
  full stop on the last item;
- items after a complete sentence: capitalised, each ending in a full stop.

Pick one per list and be consistent.

**Images.** Always give an `alt` attribute. Never render text as an image. Use the
site palette (`#C23669` magenta, `#376AC3` blue, `#2a2e3d` dark blue, `#73757d` gray,
`#f3f1f2` light gray) and Noun Project icons for illustrations.

**File and tag naming.** Markdown filenames are lowercase (except acronyms), unique
across the site, and free of spaces and special characters. Tags and keywords are
lowercase except acronyms and may contain spaces.

## Page front matter

Start from the section's `TEMPLATE_*.md`. Attributes are documented in
[pages/contribute/page_metadata.md](pages/contribute/page_metadata.md).

```yaml
---
title: Page title                     # sentence case; becomes the h1
description: one sentence, starting lowercase, ending with a full stop.
contributors: [Full Name]             # must exist in _data/CONTRIBUTORS.yaml
editors: []                           # filled in by the editorial board
page_id: short_id                     # unique across the site, lowercase, underscores
related_pages:
  Your_tasks: [page_id, page_id]      # page_ids, NOT filenames
  Tool_assembly: [page_id]
training:
  - name: Topic search query in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=topic
---
```

Which `related_pages` sections are allowed depends on the page's own section — see the
table in [pages/contribute/editorial_board_guide.md](pages/contribute/editorial_board_guide.md#related-pages).
Do not add sections beyond those:

| This page is a… | may list |
|---|---|
| Data life cycle page | Your tasks |
| Your tasks page | Tool assembly |
| Your role page | Your tasks |
| Your domain page | Your tasks, Tool assembly |
| Tool assembly page | Your tasks, Your domain |

`search_exclude: true` comes from the template and must be deleted from a new content
page; it is only kept deliberately on a few landing and meta pages. `fairsharing:` and `dsw:` are machine-generated — never edit them by hand.

## Page body structure

Domain, task and role pages all follow the same shape:

```markdown
## Introduction

## Descriptive section title
### Description
### Considerations
### Solutions

## Another section title
### Description
### Considerations
### Solutions

## Bibliography
{% bibliography --cited %}
```

- **Sections are named after problems**, not after tools, sub-fields or products.
- **Description** frames one data management problem. If a generic Task page already
  covers it, link there first, then explain what is different in this context.
- **Considerations** are short questions the reader should ask themselves. One level
  of nesting at most.
- **Solutions** explain *how* to use something to solve the problem. Do not write a
  bare list of tool names — the tool table at the bottom is generated automatically.
- **Bibliography** is optional but expected where the page makes specific claims.

Domain pages should extend existing Task pages rather than duplicate them. If a
problem generalises beyond the domain, the right move is to improve the Task page (or
open an issue proposing one), not to restate it.

## Adding a tool or resource

See [pages/contribute/tool_resource_update.md](pages/contribute/tool_resource_update.md).
Append to `_data/tool_and_resource_list.yml`; keys are stored alphabetically because
`var/tools_validator.py` rewrites the file:

```yaml
- description: One or two sentences. Avoid the characters " and '
  id: kebab-case-id
  name: Full Name (ACRONYM)
  registry:
    biotools: biotoolsID
    fairsharing: alphanumeric part after "FAIRsharing." in the DOI
    tess: TeSS query string
  url: https://example.org/
```

- `id` must be kebab-case, lowercase, alphanumeric plus hyphens — the validator exits
  non-zero otherwise. It must be unique.
- `url` should start with `https://` (some legacy entries still use `http://`), and
  must resolve.
- `registry` accepts only `biotools`, `fairsharing` and `tess`. Verify IDs against the
  live registries (`https://bio.tools/api/tool/<id>/?format=json`,
  `https://tess.elixir-europe.org/materials.json_api?q="<name>"`). The FAIRsharing API
  needs credentials, so if you cannot verify a FAIRsharing ID, **omit it** — a weekly
  GitHub Action fills registry links in automatically. Use `NA` only to suppress a
  wrong automatic link.
- `related_pages` is **not** a valid key on a tool entry; the validator rejects it.

**Not** tools or resources, and not to be added: publications (cite them instead),
policies and guidelines, and plain webpages of groups or consortia. Tool tags are only
allowed in Your domain, Your role, Your tasks and Tool assembly pages.

## Adding a citation

1. Verify the reference (CrossRef: `https://api.crossref.org/works/<DOI>`). Use the
   complete author list — the display class adds "et al.", so `et al.` must never
   appear in the `author` field.
2. Append a BibTeX entry to `_bibliography/references.bib`. Citation key format is
   `auth.lower + year + shorttitle(1,0)`, e.g. `sumner2007Proposed`.
3. Brace-protect case-sensitive words in titles: `{{mzTab-M}: A Data Standard…}`.
4. Cite in the text with `{% cite key %}` and add `## Bibliography` followed by
   `{% bibliography --cited %}` at the end of the page.

## Definition of done for a new page

Mirrors [pages/contribute/editors_checklist.md](pages/contribute/editors_checklist.md),
which is posted automatically as a review comment on every pull request touching
`pages/`. Before you call the work finished:

- [ ] The page follows its section template, with no `search_exclude` left behind.
- [ ] `page_id` is unique; `description`, `contributors`, `related_pages` and
      `training` are filled in.
- [ ] Every contributor is listed in `_data/CONTRIBUTORS.yaml`, in the same branch.
      Add only fields you can verify; do not guess ORCIDs or affiliations.
- [ ] The page is added to `_data/sidebars/data_management.yml`, in the same branch,
      in the correct alphabetical position.
- [ ] A news item is added to `_data/news.yml`, in the same branch, with the pull
      request number in `linked_pr`.
- [ ] Every `{% tool %}` id exists in `_data/tool_and_resource_list.yml`, and every
      tool added to the table is used somewhere.
- [ ] Every in-text link resolves to a real page **filename**.
- [ ] Every `{% cite %}` key exists in `_bibliography/references.bib`.
- [ ] Cross-references are reciprocal where it helps the reader — if page A tells
      readers to read page B alongside it, add the matching pointer to B.
- [ ] Content, style and tone match the style guide.
- [ ] No copyright issues; all content is original or properly attributed.

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
