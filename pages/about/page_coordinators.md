---
title: Page coordinators
---

## What is a page coordinator?

A page coordinator is a community member who looks after one or more RDMkit pages. Coordinators are usually (co-)authors of the page or experts on its topic, but anyone who knows the subject well and is willing to take on the role is welcome.

Coordinators are listed in the **Coordinators** tab at the bottom of the page they coordinate.

## What a page coordinator is not

Page coordinators are **not page owners**. As described in [How to contribute](how_to_contribute#acknowledgement-and-ownership-of-content), no single contributor, editor or coordinator owns the content of the RDMkit. Content is community-led and decisions are driven by consensus among the contributors and editors.

This means that:

* Anyone can still propose changes to a coordinated page, with or without involving the coordinator.
* The coordinator cannot block or veto changes. Final decisions on merging content remain with the [editorial board](editorial_board).
* Coordinators are not expected to write all content themselves. Their role is to make sure the right people are involved.

## Responsibilities

As a page coordinator, you:

* **Act as contact point** for the page. The [editorial board](editorial_board), contributors and readers can reach out to you with questions, suggestions or proposed changes about its content.
* **Help review pull requests** that change the page. You are asked to check whether proposed changes are accurate, relevant and consistent with the rest of the page. The editorial board takes care of style, formatting and the final merge.
* **Help find the right people** to update the page. If a change requires expertise you do not have, you point the editors to someone who does, or involve them directly.
* **Help find the right content**. When a page becomes outdated or incomplete, you suggest what should be added, changed or removed, and open an issue or pull request where needed.
* **Respond to issues** that are opened about the page, or help the editors to find someone who can.


## How are coordinators listed?

Coordinators are listed in the `coordinators` attribute in the [metadata](page_metadata) of the page. The names used there must match a name in the [CONTRIBUTORS file](https://github.com/elixir-europe/rdmkit/blob/master/_data/CONTRIBUTORS.yaml), so that the GitHub account and contact details of the coordinator can be linked. A coordinator is also listed as a contributor of the page.

```yaml
---
title: Title of the page
contributors: [Full Name, Another Name]
coordinators: [Full Name]
---
```

If a GitHub account is linked to the coordinator in the CONTRIBUTORS file, the editors can mention the coordinator directly in pull requests and issues related to the page.

## How to become a page coordinator

If you want to become the coordinator of a page:

* Open a [pull request](how_to_contribute) adding your name to the `coordinators` attribute of the page, or
* [Open an issue](https://github.com/elixir-europe/rdmkit/issues/new/choose) or contact the editorial board at rdm-editors@elixir-europe.org stating which page you would like to coordinate.

