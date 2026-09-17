---
title: Markdown cheat sheet
summary: This cheat sheet shows what is possible in Markdown pages.
contributors: [Bert Droesbeke]
search_exclude: true
---

We use Markdown files to manage content in RDMkit in a structured way that is easy to edit. For more information about Markdown, see the [GitHub Markdown documentation](https://docs.github.com/en/get-started/writing-on-github). For more information about the Markdown flavour used by the theme, Kramdown, see the [Kramdown documentation](https://kramdown.gettalong.org/parser/kramdown.html).

Besides the syntax used for main content, RDMkit also uses metadata fields in Markdown files. To learn how metadata unlocks page features, see [Page metadata](page_metadata).

## Titles

Using:
```
## Title
```

### Subtitles

Using:
```
### Subtitles
```

#### Sub-subtitles

Using:
```
#### Sub-subtitles
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

## File names, files and software names

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

## Callouts

Callouts in this theme are styled blockquotes with a title and icon. Put a supported callout class on the line immediately before the blockquote, and use `>` for each line of callout content. Regular blockquotes render as neutral message boxes without a title or icon.

The built-in callout types are `note`, `tip`, `warning`, and `important`.

### Basic callouts

{% raw %}
```md
{: .note }
> This is a note.

{: .tip }
> This is a tip.

{: .warning }
> This is a warning.

{: .important }
> This is important information.
```
{% endraw %}

This renders as:

{: .note }
> This is a note.

{: .tip }
> This is a tip.

{: .warning }
> This is a warning.

{: .important }
> This is important information.

### Custom title and longer content

Add `-title` to provide your own heading. Use a blockquote when the callout needs more than one paragraph, a list, or another block element.

{% raw %}
```md
{: .note-title }
> Before you publish
>
> Check the [Page metadata](page_metadata) page, review `inline code`, and confirm **bold text** renders correctly.
>
> - Confirm the page title.
> - Preview the page on a narrow screen.
```
{% endraw %}

This renders as:

{: .note-title }
> Before you publish
>
> Check the [Page metadata](page_metadata) page, review `inline code`, and confirm **bold text** renders correctly.
>
> - Confirm the page title.
> - Preview the page on a narrow screen.

### Nested callouts

To place a callout inside another callout, add another blockquote level for the nested callout.

{% raw %}
```md
{: .note-title }
> Release checklist
>
> Review the page before opening the pull request:
>
> - Confirm metadata and navigation.
> - Preview desktop and mobile layout.
>
> {: .warning-title }
> > Do not merge yet
> >
> > Hold the release if generated tables or search data are stale.
```
{% endraw %}

This renders as:

{: .note-title }
> Release checklist
>
> Review the page before opening the pull request:
>
> - Confirm metadata and navigation.
> - Preview desktop and mobile layout.
>
> {: .warning-title }
> > Do not merge yet
> >
> > Hold the release if generated tables or search data are stale.

## Images

{% include image.html file="/infrastructures/ELIXIR-logo.svg" caption="Figure 1. ELIXIR logo rendered through the image include." alt="ELIXIR logo" %}

This image is inserted in Markdown using the following snippet:

{% raw %}
```
{% include image.html file="/infrastructures/ELIXIR-logo.svg" caption="Figure 1. ELIXIR logo rendered through the image include." alt="ELIXIR logo" max-width="10" %}
```
{% endraw %}

Or a smaller image:

{% include image.html file="infrastructures/ELIXIR-logo.svg" alt="ELIXIR logo" max-width="3em" %}

This image is inserted in Markdown using the following snippet:

{% raw %}
```
{% include image.html file="infrastructures/ELIXIR-logo.svg" alt="ELIXIR logo" max-width="3em" %}
```
{% endraw %}

Add images to the `images` directory and give them descriptive filenames. Adapt the snippet so it points to your image. Only the filename is needed when the image is stored in the expected directory. Supported attributes are:

* **`click`**: When set to `true`, the image opens in another tab.
* **`url`**: Link the image to another page.
* **`alt`**: Describe the image for screen readers and other assistive technologies.
* **`caption`**: Text that appears under the image.
* **`inline`**: When set to `true`, the image can be used in a list.
* **`max-width`**: Maximum width in `px` or `em`.
* **`class`**: Custom CSS class.


Or use the following Markdown syntax:
{% raw %}
```
![ELIXIR logo](images/infrastructures/ELIXIR-logo.svg)
![ELIXIR logo](images/infrastructures/ELIXIR-logo.svg){: height="200px" width="200px"}
```
{% endraw %}

This renders as:

![ELIXIR logo](images/infrastructures/ELIXIR-logo.svg)
![ELIXIR logo](images/infrastructures/ELIXIR-logo.svg){: height="200px" width="200px"}

{: .important }
> This way of including images does not work well when webpages are served from folder-style URLs, because absolute image links do not work reliably on forks.

## Icons

Go to the [Lucide icon library](https://lucide.dev/icons/) to see the available icons. The theme loads the Lucide icon font, so icons can be added with classes such as `icon-camera` or `icon-book-open`.

Lucide icons inherit the surrounding text size. Use Bootstrap font-size utility classes such as `fs-5`, `fs-4`, and `fs-3` when you want to scale them.

Here is an example of how to scale up a camera icon:

```html
<i class="icon-camera"></i> normal size
<i class="icon-camera fs-5"></i> fs-5
<i class="icon-camera fs-4"></i> fs-4
<i class="icon-camera fs-3"></i> fs-3
```

Here is what they render to:

<i class="icon-camera"></i> normal size
<i class="icon-camera fs-5"></i> fs-5
<i class="icon-camera fs-4"></i> fs-4
<i class="icon-camera fs-3"></i> fs-3

Font Awesome remains supported for existing content and for icons Lucide does not provide, such as brand icons. Go to the [Font Awesome library](https://fontawesome.com/) to see the available icons.

The Font Awesome icons allow you to adjust their size by simply adding `fa-2x`, `fa-3x` and so forth as a class to the icon to adjust their size to two times or three times the original size. As vector icons, they scale crisply at any size.

Here is an example of how to scale up a camera icon:

```html
<i class="fa-solid fa-camera-retro"></i> normal size (1x)
<i class="fa-solid fa-camera-retro fa-lg"></i> fa-lg
<i class="fa-solid fa-camera-retro fa-2x"></i> fa-2x
<i class="fa-solid fa-camera-retro fa-3x"></i> fa-3x
<i class="fa-solid fa-camera-retro fa-4x"></i> fa-4x
<i class="fa-solid fa-camera-retro fa-5x"></i> fa-5x
```

Here is what they render to:

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

## Emojis

Use GitHub emoticons. This [GitHub page about emoticons](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md) has a cheat sheet for all supported emoticons.
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

This renders as:

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


## Lists and sub-lists

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
> Use blockquotes to highlight quoted guidance, important context or a longer note that should stand apart from the surrounding text.
>
> Keep the quoted text concise, and prefer a callout when the content needs a title or a specific visual treatment.
```

Giving:

> Use blockquotes to highlight quoted guidance, important context or a longer note that should stand apart from the surrounding text.
>
> Keep the quoted text concise, and prefer a callout when the content needs a title or a specific visual treatment.


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
