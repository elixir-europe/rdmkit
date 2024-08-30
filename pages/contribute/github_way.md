---
title: GitHub way
---


This guide tells you how to request and edit a page using GitHub.

Prerequisites:
* Basic knowledge of Markdown. All you need to know is in our [markdown cheat sheet](markdown_cheat_sheet)
* A GitHub account. If you do not have one, [create a free GitHub account](https://github.com/join) before you start.


## Announce and discuss your proposal through GitHub “issues”

1. Go to the [RDMkit repo](https://github.com/elixir-europe/rdmkit) on GitHub.
2. Click “Issues” in the top menu bar and look at the existing issues. See if your idea or suggestion is already being discussed.
    * **If an issue exists**, comment and let people know if you want to contribute.
    * **If no relevant issue exists**, create a new one: click the green “New issue” button on the right and choose a template. You can find more information on creating issues in the [GitHub documentation](https://docs.github.com/en/github/managing-your-work-on-github/creating-an-issue).
3. Discuss your idea with the editors through comments in the issues – you will be notified when others comment.
    * You can read the comments and write your opinion/questions/answers in the “Leave a comment” box. To submit your responses, click the green “Comment” button on the right.
    * You can always return to your opened issue by going to the [issues section](https://github.com/elixir-europe/rdmkit/issues) of our GitHub repo.

{% include callout.html type="tip" content="You can also get to the [RDMkit](https://github.com/elixir-europe/rdmkit) repo on GitHub using the ‘GitHub’ link in the header of this site." %}


## Read the guides {#read-the-guides}

Before starting editing on GitHub:
1. Make sure you are following our [style guide](style_guide).
2. Follow the structure of the provided template for the page you wish to create or update. 
3. We use markdown. To learn how to create paragraphs, headings, format text, add links and images and much more, follow our [markdown cheat sheet](https://rdmkit.elixir-europe.org/markdown_cheat_sheet).

{% include callout.html type="tip" content="For more information on writing and formatting, visit [GitHub’s documentation](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github)." %}


## Start editing {#start-editing}
{% include callout.html type="important" content="Only move to the following steps if you and the editors have agreed on your plans and you have read the guides.
" %}

1. Find where to edit on GitHub
    * If you want to contribute to an existing page, go to the page on the site and click the “Edit me” pencil icon <i class="fa-solid fa-pencil text-primary"></i> next to the page title
    * If you want to create a new page, the editors will provide a link to the page as a comment in your GitHub issue. The page will come with a predefined template based on the kind of content you want to contribute.
2. You will be taken to the correct GitHub repository, where you will look for a pencil icon on the top right.
   {% include image.html file="raw_github.png" inline=true alt="Editing a page on GitHub" %}


## Linking resources and other pages (optional)
* If you have mentioned tools or resources in your text, you will have to add them to the [tool and resource list](tool_resource_update).
* If you want to list training material, add it to the page metadata. This is the training fields that are part of the template, provided at the top of the page.

{% include callout.html type="important" content="In general terms, you must avoid manual interlinking of RDMkit pages." %}


## Submit your first draft

1. When you are happy with your first draft, go to the “Propose changes” section at the end of the page and write a title and a brief explanation of your changes.
    {% include image.html file="propose_changes_github.png" inline=true alt="Propose changes on GitHub" %}
2. Click “Propose changes”. 
3. Create a pull request following [GitHub's documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
    {% include image.html file="draft_pullrequest_github.png" inline=true alt="PrDraft pull request on GitHub" %}
4. In the description of your pull request, link the issue related to this change by typing a hashtag # and the issue number. Suggestions will appear.
    {% include image.html file="linking_issues_github.png" inline=true alt="Linking issues in a pull request on GitHub" %}
{% include callout.html type="tip" content="You can create a draft pull request when you're not ready to submit and will need to work more on it later. You can find more information about draft pull requests in the [GitHub documentation](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests#draft-pull-requests)" %}
{% include callout.html type="tip" content="You can return to your pull request by going to the [pull request section](https://github.com/elixir-europe/rdmkit/pulls) of our GitHub repo." %}


## Address editors' reviews by editing your pull request
When editors add comments or add a review of your pull request, you will be notified. To address comments, you must edit your pull request:
1. Go to your pull request. You can return to it by going to the [pull request section](https://github.com/elixir-europe/rdmkit/pulls) of our GitHub repo
2. * Click on "Files changed" in the top menu bar.
     {% include image.html file="files_changed_github.png" inline=true alt="Files changed tab on GitHub" %}
   * Click on the icon with 3 dots "..." of the file you  want to edit and then click on "Edit file".
     {% include image.html file="3_dots_github.png" inline=true alt="File change options on GitHub" %}
   * Make your changes.
   * Click on “Commit changes”.

3.  Follow [GitHub documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request) for more information. 

When all the requests have been addressed, the editors will mark the conversation as “Resolved” and the proposed changes as “Approved”. This means your content is ready to be published on the main website.

{% include callout.html type="tip" content="You can also edit your pull request any time if you change your mind about anything in your pull request and the request is not closed yet." %}
