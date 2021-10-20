---
title: Markdown cheat sheet
sidebar: contribute
summary: This is a cheat sheet to showcase what is possible within the markdown pages.
contributors: [Bert Droesbeke]
search_exclude: true
---

For more information about Markdown, please check the Markdown [guidelines](https://guides.github.com/features/mastering-markdown/).

## Possible metadata attributes of a page

Minimum of metadata in a page:
```
---
title: Demo page
---
```
* `title`: Specify here the title of the page. This wil be the H1 title (replacing the top level title using the # in markdown )

This can be extended with following attributes (each with an example):

```
---
title: Demo page
sidebar: contribute
summary: This is a demo page to showcase what is possible
description: short sentence describing the page.
contributors: [Bert Droesbeke]
search_exclude: true
datatable: true
toc: false
custom-editme: _data/tool_and_resource_list.xlsx
related_pages:
faircookbook:   
---
```

* `summary`: Using this attribute it is possible to specify a summary which will be displayed under the title of the page. This summary will also be used as description of your page when the page is tagged.

* `description`: Short sentence about the page starting with a lowercase. This sentence is visualized when pages are automatically listed using a tag.

* `contributors`: list here all the contributors that helped in establishing the page. This will be the full name of the person. Make sure that the person name that is listed can be found in the CONTRIBUTORS.yaml file in the _data directory if you want to link the github id and other contact information.

* `search_exclude`: by setting this field true, the page will not end up in the search results of the searchbar. By default this is false.

* `hide_sidebar`: When true, the sidebar will be hided. Default: false

* `custom-editme`: This attribute can be used to specify an alternative file/link when clicked on the edit-me button

* `keywords`: List here all the keywords that can be used to find the page using the searchbox in the right upper corner of the page, lowercase.

* `sidebar`: Specify here an alternative sidebar. Default: main

* `toc`: When set to false, the table of contents in the beginning of the page will not be generated.

* `page_id`: Unique identifier of a page. It is usually a shortened version of the page name or title, with small letters and spaces, or an acronym, with capital and small letters. Used to list Related pages.

* `related_pages`: List here the `page_id` of RDMkit pages that you want to display as Related pages, grouped by section (Your tasks, Your domain, Tool assembly).

  If you want pages from the specific section (Your tasks, Your domain, Tool assembly) to be shown here as Related pages, list their `page_id`. If you want to list multiple related pages, make sure to put them in a list like this: [page_id1, page_id2]. The specific sections allowed in each page are specified in each page template. Please, do not add extra sections in the metadata of the page.
  ```yml
  related_pages: 
    - your_tasks: [page_id1, page_id2]
    - your_domain: [page_id1, page_id2]
    - tool_assembly: [page_id1, page_id2]
  ``` 

* `training`: List here training material relevant for the page. We recommend to add your training material in TeSS. However, you can also list here training material that is not yet present in TeSS. Each training item will be automatically added as an entry to the table in the [All training resources page](https://rdmkit.elixir-europe.org/all_training_resources.html).
  ```yml
  training:
    - name: Training in TeSS
      registry: TeSS
      registry_url: https://tess.elixir-europe.org
      url: https://tess.elixir-europe.org/search?q=data%20analysis

    - name: Training in TeSS
      registry: TeSS
      registry_url: https://tess.elixir-europe.org
      url: https://tess.elixir-europe.org/search?q=data%20analysis
  ```
* `faircookbook`: List here all the links towards FAIR Cookbook recipes.
  ```yml
  faircookbook:
  - name: Data licenses
    url: https://fairplus.github.io/the-fair-cookbook/content/recipes/reusability/ATI_licensing_data.html
  ```

* `datatable`: use this attribute to activate the pagination + sorting + searching in tables

## Titles

Using:
```
## Title
```

### Sub titles

Using:
```
### Sub titles
```

#### Sub sub titles

Using:
```
#### Sub sub titles
```

## Bold text

**Bold** text

Using:
```
**Bold** text
```

Make sure there are no spaces between the asterisks and the text you want to put in bold.

## Italic text

*Italic* text

Using:
```
*Italic* text
```

Make sure there are no spaces between the asterisks and the text you want to put in italic.

## File names/ files / software names

`Text` can be highlighted using:

```md
`Text`
```

## Tables

You can use Multimarkdown syntax for tables. The following shows a sample:

```md
| Priority apples | Second priority | Third priority |
|-------|--------|---------|
| ambrosia | gala | red delicious |
| pink lady | jazz | macintosh |
| honeycrisp | granny smith | fuji |
```

**Result:**

| Priority apples | Second priority | Third priority |
|-------|--------|---------|
| ambrosia | gala | red delicious |
| pink lady | jazz | macintosh |
| honeycrisp | granny smith | fuji |

## Message boxes

Change the content attribute in the code snippet to change the text in the message box

{% include note.html content="This is my note." %}

{% include tip.html content="This is my tip." %}

{% include warning.html content="This is my warning." %}

{% include important.html content="This is my important info." %}


This is done by using this snippet:
{% raw %}
```
{% include note.html content="This is my note." %}
```
{% endraw %}
note.html can be replaced with tip.html, warning.html, important.html, depending on the type of message you want. 

## Images

{% include image.html file="exampleImage.png" caption="Figure 1. Say something about this pic." alt="Servers" %}

This image is inserted in the markdown using following snippet:

{% raw %}
```
{% include image.html file="exampleImage.png" caption="Figure 1. Say something about this pic." alt="Servers" %}
```
{% endraw %}

Make sure that you add the image to the `images` directory and give it an understanding filename. Adapt the snippet so it points towards you image (only the filename is needed). In the case of the example, the image exampleImage.png is loaded. Supported attributes are:

* `max-width` : an integer between 1 and 50 to define the relative width of the image
* `click`: if true, the image will be clickable -> the image will be loaded in another tab
* `url`: f you want the image to link to anther page
* `alt`: describes the image and is used for people that are visually impaired
* `caption`: Text that will appear under the image
* `inline`: if true this image can be used in a list

## Icons

Go to the [Font Awesome library](https://fontawesome.com/) to see the available icons.

The Font Awesome icons allow you to adjust their size by simply adding `fa-2x`, `fa-3x` and so forth as a class to the icon to adjust their size to two times or three times the original size. As vector icons, they scale crisply at any size.

Here's an example of how to scale up a camera icon:

```html
<i class="fas fa-camera-retro"></i> normal size (1x)
<i class="fas fa-camera-retro fa-lg"></i> fa-lg
<i class="fas fa-camera-retro fa-2x"></i> fa-2x
<i class="fas fa-camera-retro fa-3x"></i> fa-3x
<i class="fas fa-camera-retro fa-4x"></i> fa-4x
<i class="fas fa-camera-retro fa-5x"></i> fa-5x
```

Here's what they render to:

<i class="fas fa-camera-retro"></i> 1x
<i class="fas fa-camera-retro fa-lg"></i> fa-lg
<i class="fas fa-camera-retro fa-2x"></i> fa-2x
<i class="fas fa-camera-retro fa-3x"></i> fa-3x
<i class="fas fa-camera-retro fa-4x"></i> fa-4x
<i class="fas fa-camera-retro fa-5x"></i> fa-5x

## Links

### Create an external link

When linking to an external site, use:

```md
[Google](http://google.com)
```


### Linking to internal pages

When linking to internal pages, you can manually link to the pages like this:

```md
[Planning](planning)
```
Will link to the planning page.

If you change the file name, you'll have to update all of your links.

## Emoji's

Use GitHub emoticons! This [github page about emoticons](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md) has a cheat sheet for all the emoticons.
:+1: is made with `:+1:`

## Code snippets

For syntax highlighting, use fenced code blocks optionally followed by the language syntax you want:

<pre>
```java
import java.util.Scanner;

public class ScannerAndKeyboard
{

	public static void main(String[] args)
	{	Scanner s = new Scanner(System.in);
		System.out.print( "Enter your name: "  );
		String name = s.nextLine();
		System.out.println( "Hello " + name + "!" );
	}
}
```
</pre>

This looks as follows:

```java
import java.util.Scanner;

public class ScannerAndKeyboard
{

	public static void main(String[] args)
	{	Scanner s = new Scanner(System.in);
		System.out.print( "Enter your name: "  );
		String name = s.nextLine();
		System.out.println( "Hello " + name + "!" );
	}
}
```


## List and sub-list 

* List line 1
* List line 2
    * Sublist line 1

Is made with:

```md
* List line 1
* List line 2
    * Sublist line 1
		* Subsublist line 1
```

Numbered lists look like this:

1. Number one
2. Number two
3. Number three
   1. Sub number one
   2. Sub number two

and are made with:

```md
1. Number one
1. Number two
1. Number three
   1. Sub number one
   1. Sub number two

```

## Block quotes

You can add a blockquote using:

```md
> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 

> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
>
> Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 

```

Giving:

> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 

> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
>
> Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 


## A collapsible piece of text

<details>
  <summary>Click to expand!</summary>
<ol>
Text
</ol>
</details>
<br>
Is made with this code snippet:

```html
<details>
  <summary>Click to expand!</summary>
<ol>
Text
</ol>
</details>
```

## Add "Related pages" to a page 

If you want pages from the specific sections Your tasks, Your domain and Tool assembly to be shown as Related pages, list their `page_id`. If you want to list multiple related pages, make sure to put them in a list like this: [page_id1, page_id2]. 

An overview of all RDMkit pages (belonging to the sections listed above) and their `page_id` can be found in the [Website overview page](website_overview).


```yml
related_pages: 
   - your_tasks: [page_id1, page_id2]
   - your_domain: [page_id1, page_id2]
   - tool_assembly: [page_id1, page_id2]
```

## Listing training material
You can list training material by using the metadata fields as in the example below. Each training item will be automatically added as an entry to the table in the [All training resources page](https://rdmkit.elixir-europe.org/all_training_resources.html).

```yml
training:
   - name: Training in TeSS
     registry: TeSS
     registry_url: https://tess.elixir-europe.org
     url: https://tess.elixir-europe.org/search?q=data%20analysis

   - name: Training in TeSS
     registry: TeSS
     registry_url: https://tess.elixir-europe.org
     url: https://tess.elixir-europe.org/search?q=data%20analysis
```

## Enforce space between two lines

To have space between two lines of text, simply leave one empty line in between the line in the markdown. If more is needed, you can force this with:


```md
<br>
```

## Enforce no space between two lines

When you want to have a line of text.\\
And another line underneath it without space, use:

```md
When you want to have a line of text.\\
And another line underneath it without space, use:
```

Without these backslashes

```
When you want to have a line of text.
And another line underneath it without space, use:
```

looks like this:

When you want to have a line of text.
And another line underneath it without space, use:
