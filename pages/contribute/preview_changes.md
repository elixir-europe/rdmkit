---
title: Preview changes
summary: Use your own fork to preview changes on the website.
---

## Introduction

Any contributor can preview changes from their own fork. The first part of this guide is mainly relevant for people who can edit the main repository directly and want to make sure their work happens on their fork instead. If you already work on your own fork, you can skip directly to [Preview your changes using GitHub Actions](#preview-your-changes-using-github-actions) or [Preview your changes using GitHub Codespaces](#preview-your-changes-using-github-codespaces).


## Make changes on your fork

If you have write access to the main repository, changes made by clicking on the pencil icon can be committed to a branch on the main website itself. That is often fine, but it is not what you want if you prefer to preview changes from your own fork.

### 1. Make sure you have forked the main branch

Click on the 'fork' button in the top right corner to find out. If a fork is present under your personal GitHub ID, click on it. 

{% include image.html file="your_own_fork.png" alt="Your own fork" %}


Make sure you are in the `main` branch of your fork, seen in the left top corner.

{% include image.html file="change_branch.png" alt="Change branch on GitHUb" %}


### 2. Make sure your fork is up to date

Click on the 'sync fork' button to ensure you have the latest changes of the main branch in your fork. 'Update branch'.

{% include image.html file="sync_branch.png" alt="Click on the sync fork button." %}


### 3. Make changes

You can go to a folder and create a new file, or edit an existing file. See [Contributing using GitHub](/github_way) and [Creating a new page](/editorial_board_guide#create-a-new-page) for more information.

### 4. Commit to a new branch

This step is important. Make sure to commit to a new feature branch which you name in a logical way. 

{% include image.html file="commit_new_branch.png" alt="Propose changes on GitHub" %}


## Preview your changes using GitHub Actions

To preview a branch on your fork, you need to trigger the repository's existing GitHub Pages workflow manually.

1. Go to `Settings > Pages` in your fork and make sure the site is published from **GitHub Actions**.
2. If you want to deploy a feature branch instead of the default branch, go to `Settings > Environments > github-pages` and remove the restriction under **Deployment branches**.
3. Go to the `Actions` tab of your fork and open the `Jekyll site CI` workflow.
4. Click **Run workflow**. This is the GitHub interface for the `workflow_dispatch` trigger that is already defined in the workflow file; you do not need to enable anything extra for it.
5. Select the branch with your changes and start the workflow run.
6. Open the completed workflow run and use the deployment link shown in the workflow graph or the `View deployment` link to open the preview site.

{% include image.html file="deploy_using_gh_actions.png" alt="Got to the settings tab in your repo to enable GitHub pages" %}


## Preview your changes using GitHub Codespaces

GitHub Codespaces is another way to preview your changes without setting up Ruby or Docker on your own computer.

1. Open your fork on GitHub or the and switch to the branch that contains your changes.
2. Click `Code`, open the `Codespaces` tab, and create a new codespace for that branch.
3. In the codespace terminal, install the site dependencies:

   ```bash
   bundle install
   ```

4. Start the local preview server from the repository root:

   ```bash
   bundle exec jekyll serve
   ```

5. Open the preview by clicking the forwarded port link for port `4000`. If it does not open automatically, go to the `PORTS` tab in the codespace and open port `4000` from there.
6. Keep the server running while you edit files. The preview will refresh automatically after you save your changes.

{% include callout.html type="note" content="GitHub Codespaces availability and included usage depend on your GitHub plan or organisation settings." %}


## Open a Pull Request (PR) with your changes

Got to your newly created branch and click 'Contribute'. This will create a PR for the main repository.

{% include image.html file="create_pr_from_fork.png" alt="Create new PR from fork." %}

You can always make changes after the creation of this pull request by going to the files changed tab 

{% include image.html file="files_changed_github.png" alt="Files changed tab on GitHub" %}

and clicking on the 3 dots to edit the file again. After committing new changes to your branch, run the `Jekyll site CI` workflow again from the `Actions` tab to update the preview.

{% include image.html file="3_dots_github.png" alt="File change options on GitHub" %}
