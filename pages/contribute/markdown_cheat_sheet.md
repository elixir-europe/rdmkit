---
title: Markdown cheat sheet
summary: This is a cheat sheet to showcase what is possible within the markdown pages.
contributors: [Bert Droesbeke]
search_exclude: true
---

We use Markdown files to manage the content on RDMkit in a structured and easy to edit way. For more information about Markdown, please check the [Markdown guidelines](https://guides.github.com/features/mastering-markdown/). If you want more information about the specific markdown flavor we use, Kramdown, please checkout the [Kramdown documentation](https://kramdown.gettalong.org/parser/kramdown.html).

Besides the syntax to describe the main content on which this page focuses, we also make use of metadata fields in the Markdown. If you want to know more about them and how they can unlock certain features on pages, please go to our [page metadata](page_metadata) page


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

{% include callout.html type="note" content="This is my note." %}

{% include callout.html type="tip" content="This is my tip." %}

{% include callout.html type="warning" content="This is my warning." %}

{% include callout.html type="important" content="This is my important info." %}


This is done by using this snippet:
{% raw %}
```
{% include callout.html type="note" content="This is my note." %}
```
{% endraw %}
note can be replaced with tip, warning, important, depending on the type of message you want. 

## Images

{% include image.html file="/infrastructures/ELIXIR-logo.svg" caption="Figure 1. Say something about this pic." alt="ELIXIR logo" %}

This image is inserted in the markdown using following snippet:

{% raw %}
```
{% include image.html file="/infrastructures/ELIXIR-logo.svg" caption="Figure 1. Say something about this pic." alt="ELIXIR logo" max-width="10" %}
```
{% endraw %}

or a smaller image

{% include image.html file="infrastructures/ELIXIR-logo.svg" alt="ELIXIR logo" max-width="3em" %}

This image is inserted in the markdown using following snippet:

{% raw %}
```
{% include image.html file="infrastructures/ELIXIR-logo.svg" alt="ELIXIR logo" max-width="3em" %}
```
{% endraw %}

Make sure that you add the image to the `images` directory and give it an understandable filename. Adapt the snippet so it points towards your image (only the filename is needed). In the case of the example, the image exampleImage.png is loaded. Supported attributes are:

* `click`: if true, the image will be clickable -> the image will be loaded in another tab
* `url`: f you want the image to link to anther page
* `alt`: describes the image and is used for people that are visually impaired
* `caption`: Text that will appear under the image
* `inline`: if true this image can be used in a list
* `max-width`: Max width in px or em


or using following markdown syntax:
{% raw %}
```
![ELIXIR logo](/images/infrastructures/ELIXIR-logo.svg)
![ELIXIR logo](/images/infrastructures/ELIXIR-logo.svg){: height="200px" width="200px"}
```
{% endraw %}

gives:

![ELIXIR logo](/images/infrastructures/ELIXIR-logo.svg)
![ELIXIR logo](/images/infrastructures/ELIXIR-logo.svg){: height="200px" width="200px"}



## Icons

Go to the [Font Awesome library](https://fontawesome.com/) to see the available icons.

The Font Awesome icons allow you to adjust their size by simply adding `fa-2x`, `fa-3x` and so forth as a class to the icon to adjust their size to two times or three times the original size. As vector icons, they scale crisply at any size.

Here's an example of how to scale up a camera icon:

```html
<i class="fa-solid fa-camera-retro"></i> normal size (1x)
<i class="fa-solid fa-camera-retro fa-lg"></i> fa-lg
<i class="fa-solid fa-camera-retro fa-2x"></i> fa-2x
<i class="fa-solid fa-camera-retro fa-3x"></i> fa-3x
<i class="fa-solid fa-camera-retro fa-4x"></i> fa-4x
<i class="fa-solid fa-camera-retro fa-5x"></i> fa-5x
```

Here's what they render to:

<i class="fa-solid fa-camera-retro"></i> 1x
<i class="fa-solid fa-camera-retro fa-lg"></i> fa-lg
<i class="fa-solid fa-camera-retro fa-2x"></i> fa-2x
<i class="fa-solid fa-camera-retro fa-3x"></i> fa-3x
<i class="fa-solid fa-camera-retro fa-4x"></i> fa-4x
<i class="fa-solid fa-camera-retro fa-5x"></i> fa-5x

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


## Enforce space between two lines

To have space between two lines of text, simply leave one empty line in between the line in the markdown. If more is needed, you can force this with:


```md
<br>
```

## Enforce line break

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
