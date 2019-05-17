# Markdown For Typora

## Block Elements

### Paragraph and line breaks

`enter`once to create a new paragraph
`shift`+`enter`to create a new single paragraph

### Headers

use `#`+`num`to create a header
or use `Ctrl`+`num`to create a header

### Block quotes

markdown use `>`characters for block quoting. 

> this is a block quote with two paragraphs.this is the first.
>
> >
> >this is the second paragraph.

### Lists

input`* list item`will create an unordered list-the`*`can be replaced with`+`or`-`

* Gakki
* 新垣结衣
* 森山美栗

input`1. list item`will create an ordered list-their markdown source code is as follows

1. 星野源
2. 津崎平匡

### Task List

task lists are lists with items marked as either`- []` or `- [x]` 

- [x] this is a to do list

- [ ] this is a to do list too

### Code Blocks

Typora only supports fences in GitHub Flavored Markdown.
use```` ` and press `enter`.add an optional language identifier after ```` ` ``` `and we'll run it through syntax highlighting:

```python
# 这是一个python的代码块
def func(n):
	print('-' * 20)
    print(n + 1)
    
func(10)
```

### Math Blocks

you can render `LaTex`mathematical expression using **MathJax**

to add a mathematical expression, input `$$`and press`enter`
However i don't know the syntax
$$
\mathbf{v}_1 \times \mathbf{v}_2 = \begin{vmatrix}
\end{vmatrix}
$$

### Tables

input `|First Header |Second Header|`and press the `enter`.this will create a table with two columns.
after a table is created,you can resize, align, or delete the table.
you can also include inline Markdown such as links, bold, italics, or strikethrough in the table

| name | age  | gender | class | grade | birth |
| ---- | ---- | ------ | ----- | ----- | ----- |
|      |      |        |       |       |       |
|      |      |        |       |       |       |
|      |      |        |       |       |       |

### Footnotes

you can create footnotes like this [^footnote]
`[^footnote]:here is the text of the footnote`
do[^hello]

[^hello]: i think so!

Hover over the `footnote`can see content of the footnote

Horizontal Rules

inputting *** or --- on a blank line and pressing `enter`will draw a horizontal line

***

---

### Table of Contents(TOC)

input `[toc]`and press the`enter`key.This will create a "Table of Contents" section.

[TOC]



## Span Elements

### Links

Markdown supports two styles of links: inline and reference.
In both styles, the link text is delimited by `[square brackets]`.
To create an inline link, use a set of regular parentheses immediately after the link text's closing square bracket. Inside the parentheses, put the URL where you want the link to point , along with an optional title for the link, surrounded in quotes. For example:

This is [my_blog](http://47.100.200.127) link.  And this is the [baidu](http://www.baidu.com) link.

### Internal Links

**You can set the href to headers`**,which will create a bookmark that allow you to jump to that section after clicking.For example:

Command(on Windows:Ctrl) + Click [This link](#Block Elements) will jump to header `Blocj Elements`. To see how to write that, please move cursor or click that link with `Ctrl` key pressed to expand the element into markdown source.

### Reference Links

Reference-style links use a second set of square brackets, inside which you place a label of your choosing to identify the link:

This is [an example][id] reference-style link.

Then ,anywhere in the document, you define your link label on a line by itself like this:

[id]: http://47.100.200.127	" my_blog"

The implicit link name shortcut allows you to omit the name of the link, in which case the link text itself is used as the name. Just use an empty set of square brackets---for example, to link the word "Google" to the google.com web site, you could simply write:

[Google][]
and then define the link:

[Google]: http://google.com	"谷歌"

### URLs

Typora allows you to insert URLs as links, wrapped by `<brackets>`.
Typora will also automatically link standard URLs. e.g:<www.google.com>

### Images

Images have similar syntax as links, but they require an additional ! char before the start of the link. The syntax for inserting an image looks like this:

![Alt text](C:\Users\Jhon\Pictures\480c6c3e23601d1600a3f78df9cd73bc87a09469.jpg)

---

### Emphasis

Markdown treats asterisks( * ) and underscores( _ ) as indicators of emphasis. Text wrapped with one * or _ will be wrapped with an HTML `<em>` tag. E.g:

*single asterisks*

_single underscores_

\*this text is surrounded by literal asterisks\*

### Strong

A double `* `or `_`will cause its enclosed contents to be wrapped with an HTML `<strong>`tag:

**double asterisks**

### Code

To indicate an inline span of code, wrap it with backtick quotes (`) . Unlike a pre-formatted code block, a code span indicates code within a normal paragraph. For example:

use the `printf()`function

### Strikethrough

GFM adds syntax to create strikethrough text, which is missing from standard Markdown.

~~Mistaken text~~

### underlines

Underline is powered by raw HTML.

<u>just like the html tag</u>

### Emoji

Input emoji with syntax : smile: .

User can trigger auto-complete suggestions for emoji by pressing `ESC`key, or trigger it automatically after enabling it on preference panel. Also, inputting UTF-8 emoji characters directly is also supported by going to `Edit` ---> `Emoji & Symbols` in the menu bar(macOS).

:smile_cat:

### Inline Math

To use this feature, please enable it first in the `Preference` Panel ---> `Markdown` Tab. Then, use `$`to warp a TeX command. For example:

$\lim_{x \to \infty} \exp(-x) = 0$

### Superscript

To use this feature, please enable it first in the `Preference` Panel -> `Markdown` Tab. Then, use `^` to wrap superscript content. For example:

x^2^

### Highlight

To use this feature, please enable it first in the `Preference` Panel -> `Markdown` Tab. Then, use `==` to wrap highlight content. For example: 

==highlight==

## HTML

### Embed Contents

Some websites provide iframe-based embed code which you can also paste into Typora. For example:

<iframe height='265' scrolling='no' titile='My Blog' src='http://47.100.200.127' frameborder='no' allowtransparency='true' allowfullscreen='true' style='width: 100%;'></iframe>

### Video

You can use the `<video>`html tag to embed videos. For example:

<video src="xxxxx" />



