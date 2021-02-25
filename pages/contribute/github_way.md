---
title: GitHub way
sidebar: contribute
---


This guide tells you how you can easily request and edit a page on this website. You do this using GitHub. For other ways of contributing, see [How to contribute](how_to_contribute.html).


**Prerequisite:** [create a GitHub account](https://github.com/join) before you start. It's easy and free.

<!-- The process of contribution via GitHub is sketched below.

{% include image.html file="github_way_flow.svg" alt="Process of contributing via GitHub" click=true %}
-->

## Announce and discuss your proposal through GitHub "issues"
1. Go to the [RDMKit repo](https://github.com/elixir-europe/rdmkit){:target="_blank"} on GitHub.
2. Click on "Issues" in the top menu bar and look at the existing issues. See if your idea or suggestion is already being discussed.
      * **If an issue exists**, add your comments. If you want to edit the content discussed, let people know through the comments.
      * **If no relevant issue exists**, create a new issue by clicking on the green "New issue" button on the right, and choose one of the issues templates. You can find more information on creating issues in the [GitHub documentation](https://docs.github.com/en/github/managing-your-work-on-github/creating-an-issue).
      <!-- {% include image.html class="mt-0 mb-0" file="new_issue_github.png" inline=true alt="Open new issue on GitHub." %} -->
3. Discuss your idea with the editors through comments in the issues. You will be notified when others comment on your issues. Read the comments and write your opinion/questions/answers in the "Leave a comment" box and click on the green "Comment" button on the right.
4. You can always return to your opened issue by going to the [issues section](https://github.com/elixir-europe/rdmkit/issues) of our GitHub repo.

{% include tip.html content="You can also get to the [RDMKit pages](https://github.com/elixir-europe/rdmkit) on GitHub using the 'GitHub' link in the header of this site" %}

## Write your content and make a pull request

1. When you and the editors have agreed on what you will do, go to the page you want to edit on the website. Click on "Edit me" pencil icon :pencil:, shown next to the page title. If you want to add a new page, the editors will give you the link to the page via comments in the issue you created. The page will come with a predefined template, based on the kind of content you want to contribute.
2. The "Edit me" pencil icon will take you to the GitHub repository, where you again click on the pencil icon, shown on the right, and start editing.
    {% include image.html class="mt-0 mb-0" file="raw_github.png" inline=true alt="Editing a page on GitHub" %}
3. You can now edit or add new text and images according to the provided template. GitHub provide a [guide for writing and formatting in GitHub](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github). We also provide a [markdown cheat sheet](markdown_cheat_sheet) to show you how to write in this webpage. Make sure to read our [style guide](style_guide) before start writing. In general, try to avoid manual interlinking of RDMKit pages.
4. If you have mentioned tools or resources in your text, make sure to add them to the [tool and resource list](tool_resource_update).
5. When you are happy with your first draft of the content, go to the “Propose changes” section at the end of the page and write a title and a brief explanation of your changes.
6. Click on “Propose changes”.
    {% include image.html class="mt-0 mb-0" file="propose_changes_github.png" inline=true alt="Propose changes on GitHub" %}
7. You are now redirected to the Pull Request (PR) page. A "pull request" is a request to "pull" your changes into the website. Click on the "Create Pull Request" green button. Here you can choose to:

     * "Create draft pull request": choose this if you have not finished writing. Later on you can always click on "Ready for review" to switch to a normal pull request. You can find more information about draft pull requests in the [GitHub documentation](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests#draft-pull-requests).
     * "Create pull request": choose this if you have finished your text. Editors will then review your request.
    {% include image.html class="mt-0 mb-0" file="draft_pullrequest_github.png" inline=true alt="PrDraft pull request on GitHub" %}

8. In the description of your pull request you can link to the issue that relates to this change by typing a hashtag `#` and the correct issue number. Suggestions will appear. This way it is easy for the editors to link back the issue were this change might have been discussed beforehand.
    {% include image.html class="mt-0 mb-0" file="linking_issues_github.png" inline=true alt="Linking issues in a pull request on GitHub" %}

9. You can return to your pull request by going to the [pull request section](https://github.com/elixir-europe/rdmkit/pulls) of our GitHub repo.

10. If you change your mind about anything in your pull request and the request is not closed, or if the editor tells you to edit your request during the review process, you have to:
    * Go to your pull request
    * Click on "Files changed" in the top menu bar.
      {% include image.html class="mt-0 mb-0" file="files_changed_github.png" inline=true alt="Files changed tab on GitHub" %}
    * Click on the icon with 3 dots "..." of the file you  want to edit and then click on "Edit file".
      {% include image.html class="mt-0 mb-0" file="3_dots_github.png" inline=true alt="File change options on GitHub" %}
    * Make your changes.
    * Click on “Commit changes”.

{% include note.html content="Anyone can comment on your issue or pull request and you can reply. For more information on this, please visit the [GitHub documentation](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request)" %}

## Request a review

If you open a normal pull request then a review is automatically requested. The relevant editors will check your changes. If your request is still in draft, click on "Ready for review" to request a review. You can find more information about draft pull requests in the [GitHub documentation](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/changing-the-stage-of-a-pull-request#marking-a-pull-request-as-ready-for-review).

## Address editors' comments

1. When editors add comments or add a review of your pull request, you will be notified.
2. You need to address editors' comments and requests by editing your pull request as in step 7 (see above).
   * Go to your pull request
   * Click on "Files changed" in the top menu bar.
    {% include image.html class="mt-0 mb-0" file="files_changed_github.png" inline=true alt="Files changed tab on GitHub" %}
   * Click on the icon with 3 dots "..." of the file you  want to edit and then click on "Edit file".
    {% include image.html class="mt-0 mb-0" file="3_dots_github.png" inline=true alt="File change options on GitHub" %}
   * Make your changes.
   * Click on “Commit changes”.
3. When all the requests have been addressed, the editors will mark the conversation as "Resolved" and the proposed changes as "Approved".
4. You content is ready to be merged and published in the main website.
5. Editors publish your content.
