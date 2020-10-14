---
title: Working with Git
sidebar: contribute
toc: false
---

This is a general workflow if you work on your own fork (copy) of the rdm-toolkit repo:
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
- Open the pull request
- Wait for review by other editors