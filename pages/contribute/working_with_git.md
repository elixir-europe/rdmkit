---
title: Working with Git
sidebar: contribute
toc: false
---


## Forking - branching - changing - pushing - PR

This is a general workflow in how to work on your own fork (copy) of the rdm-toolkit repo and request changes through a pull request:
NOTE: if you already did these steps in the past, start from the `git fetch upstream` command. 

- Make a fork of this repository, using the fork button.
- Open a terminal and clone your fork using:
    ```
    git clone git@github.com:USERNAME/rdm-toolkit.git
    cd rdm-toolkit
    ```
    NOTE: Make sure you clone the fork and not the original elixir-europe/rdm-toolkit one.
- Keep your fork up to date (IMPORTANT!).
    ```
    git remote add upstream https://github.com/elixir-europe/rdm-toolkit.git
    git fetch upstream
    git checkout master (if you are not already on the master branch, check with `git branch`)
    git pull upstream master
    ```
- Create a new branch named after your feature/edit.
    ```
    git branch -b 'FEATURE_NAME'
    git checkout 'FEATURE_NAME'
    ```
- Make the changes you want to make using an editor of choice
- Save.
- Open terminal and stage your changes:
    ```
    git add .
    ```
- Committing changes
    ```
    git commit -m "Changing the tool-resource file"
    ```
- Pushing you changes to your fork
    ```
    git push origin 'FEATURE_NAME'
    ```
- Go to [https://github.com/elixir-europe/rdm-toolkit](https://github.com/elixir-europe/rdm-toolkit) and click on *Compare & pull request*
- Open the pull request an describe your changes.
- Wait for review by other editors. Editors that are responsible for the sections you make changes to will be assigned as reviewer automatically.

## The advantage of working locally: previewing your changes through your web browser

The website is build on Github using Jekyll, a simple, static site generator based on ruby. When you have a local copy cloned onto your computer, it is possible to generate the website based on this repo. This makes it possible to preview changes live, every time you save a file from within the Github rdm-toolkit repo. Follow these steps to deploy the website based on your local clone (copy) of the rdm-toolkit repo:

1. Make sure you have cloned the rdm-toolkit repo
    ```
    git clone git@github.com:USERNAME/rdm-toolkit.git
    cd rdm-toolkit
    ```

2. Install Jekyll
If you’ve never installed or run a Jekyll site locally on your computer, follow these instructions to install Jekyll:
   * [Install Jekyll on Mac][mydoc_install_jekyll_on_mac]
   * [Install Jekyll on Windows][mydoc_install_jekyll_on_windows]

3. Install Bundler and Jekyll

    ```
    gem install jekyll bundler
    ```

4. Update dependencies

    ```
    bundle update
    ```

5. deploy website

    ```
    bundle exec jekyll serve
    ```