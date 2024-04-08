---
title: 'HTML核心'
date: 2022-08-10 09:03:02
cover: false
tags:
- HTML
categories: 'HTML'
typora-root-url: HTML核心
---

[TOC]



# `HTML`介绍

## `HTML`基本概念

> `HTML`通过各种各样的标记，将纯文本语义化；
>
> 不同的标签包裹内容，形成不同的元素，表示不同含义的文本或内容；
>
> 嵌套元素增强了语义的表达能力；
>
> 不同元素以一定的规则嵌套，组合形成完整页面

### 什么是`HTML`

> `HTML`通过各种各样的标记，将纯文本文字进行结构化和语义化

超文本标记语言 (英语：**H**yper**t**ext **M**arkup **L**anguage，简称：HTML ) 是一种用来结构化 Web 网页及其内容的标记语言。网页内容可以是：一组段落、一个重点信息列表、也可以含有图片和数据表。

HTML 不是一门编程语言，而是一种用于**定义内容结构**的标记语言。

HTML 由一系列的**元素**（elements）组成，这些元素可以用来包围不同部分的内容，使其以某种方式呈现或者工作。一对标签（ tags）可以为一段文字或者一张图片添加超链接，将文字设置为斜体，改变字号，等等。

### `HTML`元素详解

- 元素的主要部分有：

  ```html
  <p>My cat is very grumpy</p>
  ```

  - **开始标签**（Opening tag）：包含元素的名称（本例为 p），被大于号、小于号所包围。表示元素从这里开始或者开始起作用 —— 在本例中即段落由此开始。
  - **结束标签**（Closing tag）：与开始标签相似，只是其在元素名之前包含了一个斜杠。这表示着元素的结尾 —— 在本例中即段落在此结束。初学者常常会犯忘记包含结束标签的错误，这可能会产生一些奇怪的结果。
  - **内容**（Content）：元素的内容，本例中就是所输入的文本本身。
  - **元素**（Element）：开始标签、结束标签与内容相结合，便是一个完整的元素。

- 元素也可以有属性（Attribute）：

  ```html
  <p class="editor-note">My cat is very grumpy</p>
  ```

  - 属性包含了关于元素的一些额外信息，这些信息本身不应显现在内容中。本例中，`class` 是属性名称，`editor-note` 是属性的值。`class` 属性可为元素提供一个标识名称，以便进一步为元素指定样式或进行其他操作时使用。
  - 属性应该包含：
    1. 在属性与元素名称（或上一个属性，如果有超过一个属性的话）之间的空格符。
    2. 属性的名称，并接上一个等号。
    3. 由引号所包围的属性值。

- 我的理解：不同的标签包裹内容，形成不同的元素，表示不同含义的文本或内容

#### 嵌套元素

- 也可以将一个元素置于其他元素之中 —— 称作**嵌套**。
- 元素必须正确地开始和结束，才能清楚地显示出正确的嵌套层次。否则浏览器就得自己猜测，虽然它会竭尽全力，但很大程度不会给你期望的结果。所以一定要避免！
- 我的理解：嵌套元素增强了语义的表达能力

#### 块和行内元素

在 HTML 中有两种你需要知道的重要元素类别，块级元素和内联元素。

- 块元素（`block element`）

  - 详解：[块级元素 - HTML（超文本标记语言）](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Block-level_elements)
  - 块级元素在页面中以块的形式展现 —— 相对于其前面的内容它会出现在新的一行，其后的内容也会被挤到下一行展现（独占一行）。块级元素通常用于展示页面上结构化的内容，例如段落、列表、导航菜单、页脚等等。一个以 `block` 形式展现的块级元素不会被嵌套进内联元素中，但可以嵌套在其它块级元素中。

  - 占满整行，元素宽高边距等可设置
  - 在网页中，一般通过块元素来进行布局

- 行内元素（`inline element`）

  - 内联元素通常出现在块级元素中并环绕文档内容的一小部分，而不是一整个段落或者一组内容。内联元素不会导致文本换行：它通常出现在一堆文字之间。
  - 不占满整行，宽高、上下边距等不可直接设置
  - 行内元素可以直接设置左右内外边距，无法直接设置上下内外边距
  - 行内元素主要用来包裹文字
  - 一般情况下会在块元素中放行内元素，而不会在行内元素中放块元素
  - 块元素中基本上什么都能放
  - p元素中不能放任何的块元素

- 行内块元素
  - 不占满整行，元素宽高边距等可设置

> **备注：** HTML5 重新定义了元素的类别：见 [元素内容分类](https://html.spec.whatwg.org/multipage/indices.html#element-content-categories)([译文](https://developer.mozilla.org/zh-CN/docs/Web/Guide/HTML/Content_categories))。尽管这些新的定义更精确，但却比上述的“块级元素”和“内联元素”更难理解，因此在之后的讨论中仍使用旧的定义。

> **备注：** 在这篇文章中提到的“块”和“内联”，不应该与 [the types of CSS boxes](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model#types_of_css_boxes) 中的同名术语相混淆。尽管他们默认是相关的，但改变 CSS 显示类型并不会改变元素的分类，也不会影响它可以包含和被包含于哪些元素。防止这种混淆也是 HTML5 摒弃这些术语的原因之一。

> **备注：** 你可以查阅包含了块级元素和内联元素列表的参考页面—see [Block-level elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements) and [Inline elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements).

##### 块元素

HTML（超文本标记语言）中元素大多数都是“块级”元素或[行内元素](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Inline_elements)。块级元素占据其父元素（容器）的整个水平空间，垂直空间等于其内容高度，因此创建了一个“块”。这篇文章帮助解释这个概念。

通常浏览器会在块级元素前后另起一个新行。

块级元素只能出现在`<body>` 元素内。

块级元素与行内元素有几个关键区别：

- 格式

  默认情况下，块级元素会新起一行。

- 内容模型

  一般块级元素可以包含行内元素和其他块级元素。这种结构上的包含继承区别可以使块级元素创建比行内元素更”大型“的结构。

HTML 标准中块级元素和行内元素的区别至高出现在 4.01 标准中。在 HTML5，这种区别被一个更复杂的[内容类别 (en-US)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Content_categories)代替。”块级“类别大致相当于 HTML5 中的[流内容 (en-US)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Content_categories#flow_content)类别，而”行内“类别相当于 HTML5 中的[措辞内容 (en-US)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Content_categories#phrasing_content)类别，不过除了这两个还有其他类别。

以下是 HTML 中所有的块级元素列表（虽然”块级“在新的 HTML5 元素中没有明确定义）

```html
<div>
文档分区。
<address>
联系方式信息。
<article>
文章内容。
<aside>
伴随内容。
<blockquote>
块引用。
<dd>
定义列表中定义条目描述。
<dl>
定义列表。
<fieldset>
表单元素分组。
<figcaption>
图文信息组标题
<figure>
图文信息组 (参照 <figcaption>)。
<footer>
区段尾或页尾。
<form>
表单。
<h1> (en-US), <h2> (en-US), <h3> (en-US), <h4> (en-US), <h5> (en-US), <h6> (en-US)
标题级别 1-6.
<header>
区段头或页头。
<hgroup>
标题组。
<hr>
水平分割线。
<ol>
有序列表。
<p>
行。
<pre>
预格式化文本。
<section>
一个页面区段。
<table>
表格。
<ul>
无序列表。
```

##### 行内元素

一个行内元素只占据它对应标签的边框所包含的空间。

行内元素与块级元素对比：

内容

一般情况下，行内元素只能包含数据和其他行内元素。 而块级元素可以包含行内元素和其他块级元素。这种结构上的包含继承区别可以使块级元素创建比行内元素更”大型“的结构。

格式

默认情况下，行内元素不会以新行开始，而块级元素会新起一行。

下面的元素都是行内元素：

- [b](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/b), [big](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/big), [i](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/i), [small](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/small), [tt](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/tt)
- [abbr](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/abbr), [acronym](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/acronym), [cite](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/cite), [code](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/code), [dfn](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/dfn), [em](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/em), [kbd](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/kbd), [strong](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/strong), [samp](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/samp), [var](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/var)
- [a](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a), [bdo](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/bdo), [br](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/br), [img](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img), [map](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/map), [object](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/object), [q](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/q), [script](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/script), [span](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/span), [sub](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/sub), [sup](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/sup)
- [button](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/button), [input](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/Input), [label](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/label), [select](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/select), [textarea](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/textarea)

##### 小结

`HTML4`及之前的元素类型的概念，和`CSS`盒子类型的概念相关联。块级元素等价于块级盒子，内联元素等价于内联盒子。使用`display`属性更改了盒子的外部显示类型，将`block`改为`inline`，只能说它的`CSS`盒子类型变了，但本身的元素类型还是`block`

为了避免这种混淆，`HTML5`中重新定义了元素的类型：https://html.spec.whatwg.org/multipage/indices.html#element-content-categories

![image-20220831100931309](image-20220831100931309.png)

值得一提的是，`HTML5`对元素类型的新定义，截止2022年8月31日还是非规范性的，了解一下即可

![image-20220831101359740](image-20220831101359740.png)

#### 空元素

- 不包含任何内容的元素称为空元素。比如 `img` 元素：

  ```html
  <img src="images/firefox-icon.png" alt="My test image">
  ```

  本元素包含两个属性，但是并没有 `</img>` 结束标签，元素里也没有内容。

  这是因为图像元素不需要通过内容来产生效果，它的作用是向其所在的位置嵌入一个图像。

  - 该元素通过包含图像文件路径的地址属性 `src`，可在所在位置嵌入图像。
  - `alt` 属性的关键字即“描述文本”。`alt` 文本应向用户完整地传递图像要表达的意思。用 "测试图片" 来描述 Firefox 标志并不合适，修改成 "Firefox 标志：一只盘旋在地球上的火狐" 就好多了。

#### 属性

元素也可以拥有属性，如下：

![我的猫咪脾气爆](grumpy-cat-attribute-small.png)

属性包含元素的额外信息，这些信息不会出现在实际的内容中。

在上述例子中，这个 class 属性给元素赋了一个识别的名字（id），这个名字此后可以被用来识别此元素的样式信息和其他信息。

一个属性必须包含如下内容：

1. 一个空格，在属性和元素名称之间。(如果已经有一个或多个属性，就与前一个属性之间有一个空格。)
2. 属性名称，后面跟着一个等于号。
3. 一个属性值，由一对引号“ ”引起来。

##### 布尔属性

有时你会看到没有值的属性，它是合法的。这些属性被称为布尔属性，他们只能有跟它的属性名一样的属性值。例如[`disabled`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/Input#attr-disabled) 属性，他们可以标记表单输入使之变为不可用 (变灰色)，此时用户不能向他们输入任何数据。

```html
<input type="text" disabled="disabled">
```

方便起见，我们完全可以将其写成以下形式 (我们还提供了一个非禁止输入的表单元素供您参考，以作为对比)：

```html
<!-- 使用 disabled 属性来防止终端用户输入文本到输入框中 -->
<input type="text" disabled>

<!-- 下面这个输入框没有 disabled 属性，所以用户可以向其中输入 -->
<input type="text">
```

##### 省略包围属性值的引号

我们建议始终添加引号——这样可以避免很多问题，并且使代码更易读。

##### 单引号或者双引号？

在目前为止，本章内容所有的属性都是由双引号来包裹。也许在一些 HTML 中，你以前也见过单引号。这只是风格的问题，你可以从中选择一个你喜欢的。以下两种情况都可以：

```html
<a href="http://www.example.com">示例站点链接</a>

<a href='http://www.example.com'>示例站点链接</a>
```

但你应该注意单引号和双引号不能在一个属性值里面混用。下面的语法是错误的：

```html
<a href="http://www.example.com'>示例站点链接</a>
```

在一个 HTML 中已使用一种引号，你可以在此引号中嵌套另外一种引号：

```html
<a href="http://www.example.com" title="你觉得'好玩吗'？">示例站点链接</a>
```

如果你想将引号当作文本显示在 html 中，你就必须使用[实体引用](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Introduction_to_HTML/Getting_started#实体引用：_在html中包含特殊字符)。

### `HTML`文档详解

以上介绍了一些基本的 HTML 元素，但孤木不成林。现在来看看单个元素如何彼此协同构成一个完整的 HTML 页面。

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="My test image">
  </body>
</html>
```

这里有：

- `<!DOCTYPE html>` — 文档类型。混沌初分，HTML 尚在襁褓（大约是 1991/92 年）之时，`DOCTYPE` 用来链接一些 HTML 编写守则，比如自动查错之类。`DOCTYPE` 在当今作用有限，仅用于保证文档正常读取。现在知道这些就足够了。
- `<html></html>` — [`html`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/html) 元素。该元素包含整个页面的内容，也称作根元素。
- `<head></head>` — [`head`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/head) 元素。该元素的内容对用户不可见，其中包含例如面向搜索引擎的搜索关键字（[keywords](https://developer.mozilla.org/zh-CN/docs/Glossary/Keyword)）、页面描述、CSS 样式表和字符编码声明等。
- `<meta charset="utf-8">` — 该元素指定文档使用 UTF-8 字符编码，UTF-8 包括绝大多数人类已知语言的字符。基本上 UTF-8 可以处理任何文本内容，还可以避免以后出现某些问题，没有理由再选用其他编码。
- `<title></title>` — [`title`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/title) 元素。该元素设置页面的标题，显示在浏览器标签页上，也作为收藏网页的描述文字。
- `<body></body>` — [`body`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/body) 元素。该元素包含期望让用户在访问页面时看到的内容，包括文本、图像、视频、游戏、可播放的音轨或其他内容。
- 我的理解：不同元素以一定的嵌套规则，组合形成完整页面

- 备注：国内一般都把元素（`element`），叫做标签（`tag`）

#### HTML 中的空白

无论你在 HTML 元素的内容中使用多少空格 (包括空白字符，包括换行)，当渲染这些代码的时候，HTML 解释器会将连续出现的空白字符减少为一个单独的空格符。

那么为什么我们会在 HTML 元素的嵌套中使用那么多的空白呢？

答案就是为了可读性 —— 如果你的代码被很好地进行格式化，那么就很容易理解你的代码是怎么回事，反之就只有聚做一团的混乱.。在我们的 HTML 代码中，我们让每一个嵌套的元素以两个空格缩进。你使用什么风格来格式化你的代码取决于你 (比如所对于每层缩进使用多少个空格)，但是你应该坚持使用某种风格。

#### 实体引用：在 HTML 中包含特殊字符

[https://www.w3school.com.cn/html/html_entities.asp](https://www.w3school.com.cn/html/html_entities.asp)

在 HTML 中，字符 `<`, `>`,`"`,`'` 和 `&` 是特殊字符。它们是 HTML 语法自身的一部分，那么你如何将这些字符包含进你的文本中呢，比如说如果你真的想要在文本中使用符号&或者小于号，而不想让它们被浏览器视为代码并被解释？

我们必须使用字符引用 —— 表示字符的特殊编码，它们可以在那些情况下使用。每个字符引用以符号&开始，以分号 (;) 结束。

| 显示结果 | 描述   | 实体名称 |
| -------- | ------ | -------- |
|          | 空格   | &nbsp ;  |
| <        | 小于号 | &lt ;    |
| >        | 大于号 | &gt ;    |

完整的实体参考表：[HTML ISO-8859-1 参考手册 ](https://www.w3school.com.cn/charsets/ref_html_8859.asp)

### HTML 注释

```html
<p>我在注释外！</p>

<!-- <p>我在注释内！</p> -->

```

## `head`标签与元数据

在页面加载完成的时候，head 标签里的内容，是不会在页面中显示出来的。它包含了诸如页面的 `<title>`（标题）、指向 CSS 的链接（如果你选择用 CSS 来为 HTML 内容添加样式）、指向自定义图标的链接和其它的元数据（描述 HTML 的数据，比如，作者和描述文档的重要关键词）等信息。本文将涵盖上述内容并拓展，为您对标记的使用打下一个良好的基础。

### `<head> `标签

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>我的测试页面</title>
  </head>
  <body>
    <p>这是我的页面</p>
  </body>
</html>

```

HTML `<head>` 元素与 `<body>` 元素不同，它的内容不会在浏览器中显示，它的作用是保存页面的一些元数据。上述示例的 head 元素非常简短：

```html
<head>
  <meta charset="utf-8">
  <title>我的测试页面</title>
</head>

```

然而，大型页面的 head 会包含很多元数据。可以用[开发者工具](https://developer.mozilla.org/zh-CN/docs/Learn/Common_questions/What_are_browser_developer_tools)查看网页的 head 信息。本节并不打算面面俱到地讲述 head，只是初步介绍几项 head 中重要的常用元素，让我们开始吧。

### 添加标题

之前已经讲过 `<title>` 元素，它可以为文档添加标题。但别和 `<h1>`元素搞混了，`<h1>`是为 body 添加标题的。有时候 `<h1>`也叫作网页标题。但是二者并不相同。

- [`<h1>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) 元素在页面加载完毕时显示在页面中，通常只出现一次，用来标记页面内容的标题（故事名称、新闻摘要，等等）。
- [`<title>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/title) 元素是一项元数据，用于表示整个 HTML 文档的标题（而不是文档内容）。

![demo](title-example.png)

现在很明显的可以看到 `<h1>` 出现的地方，和 `<title>` 出现的地方！

`<title>` 元素也被以其他的方式使用着。比如说，如果你尝试为某个页面添加书签，（在火狐浏览器中：点击*书签 > 将当前标签页添加到书签*，或点击地址栏末尾的星标），你会看到 `<title>` 的内容被作为建议的书签名。

![bookmark ](bookmark-example.png)

`<title>` 元素的内容也被用在搜索的结果中，正如你即将在下面看到的。

### 元数据

元数据就是描述数据的数据，而 HTML 有一个“官方的”方式来为一个文档添加元数据——`<meta>` 元素。

当然，其它的在这篇文章中提到的东西也可以被当作元数据。有很多不同种类的 `<meta>` 元素可以被包含进你的页面的 `<head>` 元素，但是现在我们还不会尝试去解释所有类型，这只会引起混乱。我们会解释一些你常会看到的类型，先让你有个概念。

#### 指定你的文档中字符的编码

```html
<meta charset="utf-8">

```

这个元素简单的指定了文档的字符编码——在这个文档中被允许使用的字符集。`utf-8` 是一个通用的字符集，它包含了任何人类语言中的大部分的字符。意味着该 web 页面可以显示任意的语言；所以对于你的每一个页面都使用这个设置会是一个好主意！比如说，你的页面可以很好的处理英文和日文：

![a web page containing English and Japanese characters, with the character encoding set to universal, or utf-8. Both languages display fine,](correct-encoding.png)

比如说，如果你将你的字符集设置为 `ISO-8859-1`，那么页面将出现乱码：

![a web page containing English and Japanese characters, with the character encoding set to latin. The Japanese characters don't display correctly](bad-encoding.png)

> **备注：** 一些浏览器（比如 Chrome）会自动修正错误的编码，所以取决于你所使用的浏览器，你或许不会看到这个问题。无论如何，你仍然应该为你的页面手动设置编码为 `utf-8`，来避免在其他浏览器中可能出现的潜在问题。

#### 添加作者和描述

许多 `<meta>` 元素包含了 `name` 和 `content` 属性：

- `name` 指定了 meta 元素的类型；说明该元素包含了什么类型的信息。
- `content` 指定了实际的元数据内容

这两个 meta 元素对于定义你的页面的作者和提供页面的简要描述是很有用的。让我们看一个例子：

```html
<meta name="author" content="Chris Mills">
<meta name="description" content="The MDN Web Docs Learning Area aims to provide
complete beginners to the Web with all they need to know to get
started with developing web sites and applications.">

```

指定作者在某些情况下是很有用的：如果你需要联系页面的作者，问一些关于页面内容的问题。一些内容管理系统能够自动获取页面作者的信息，然后用于某些用途。

指定包含关于页面内容的关键字的页面内容的描述是很有用的，因为它可能或让你的页面在搜索引擎的相关的搜索出现得更多（这些行为在术语上被称为：[搜索引擎优化](https://developer.mozilla.org/zh-CN/docs/Glossary/SEO)，或 [SEO](https://developer.mozilla.org/zh-CN/docs/Glossary/SEO)。）

在你喜欢的搜索引擎里搜索“MDN Web Docs”（下图展示的是在谷歌搜索里的情况）。你会看到 description `<meta>` 和 `<title>` 元素如何在搜索结果里显示——很值得这样做哦！

![A Yahoo search result for "Mozilla Developer Network"](mdn-search-result.png)

> **备注：** 在谷歌搜索里，在主页面链接下面，你将看到一些相关子页面——这些是站点链接，可以在 [Google's webmaster tools](https://search.google.com/search-console/about) 配置——一种可以使你的站点对搜索引擎更友好的方式。

> **备注：** 许多 `<meta>` 特性已经不再使用。例如，keyword `<meta>` 元素（`<meta name="keywords" content="fill, in, your, keywords, here">`）——提供关键词给搜索引擎，根据不同的搜索词，查找到相关的网站——已经被搜索引擎忽略了，因为作弊者填充了大量关键词到 keyword，错误地引导搜索结果。

#### 其他类型的元数据

当你在网站上查看源码时，你也会发现其它类型的元数据。你在网站上看到的许多功能都是专有创作，旨在向某些网站（如社交网站）提供可使用的特定信息。

例如，Facebook 编写的元数据协议 [Open Graph Data](https://ogp.me/) 为网站提供了更丰富的元数据。在 MDN Web 文档源代码中，你会发现：

```html
<meta property="og:image" content="https://developer.mozilla.org/static/img/opengraph-logo.png">
<meta property="og:description" content="The Mozilla Developer Network (MDN) provides
information about Open Web technologies including HTML, CSS, and APIs for both Web sites
and HTML5 Apps. It also documents Mozilla products, like Firefox OS.">
<meta property="og:title" content="Mozilla Developer Network">

```

上面代码展现的一个效果就是，当你在 Facebook 上链接到 MDN 时，该链接将显示一个图像和描述：这为用户提供更丰富的体验。

![Open graph protocol data from the MDN homepage as displayed on facebook, showing an image, title, and description.](facebook-output.png)

Twitter 还拥有自己的类型的专有元数据协议（称为：[Twitter Cards](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/abouts-cards)），当网站的 URL 显示在 twitter.com 上时，它具有相似的效果。例如下面：

```html
<meta name="twitter:title" content="Mozilla Developer Network">

```

### 增加自定义图标

为了进一步丰富你的网站设计，你可以在元数据中添加对自定义图标（**favicon**，为“favorites icon”的缩写）的引用，这些将在特定的场合（浏览器的收藏，或书签列表）中显示。

这个不起眼的图标已经存在很多很多年了，16x16 像素是这种图标的第一种类型。你可以看见这些图标出现在浏览器每一个打开的标签页中以及书签页中。

页面添加图标的方式有：

1. 将其保存在与网站的索引页面相同的目录中，以 `.ico` 格式保存（大多数浏览器将支持更通用的格式，如 `.gif` 或 `.png`，但使用 ICO 格式将确保它能在如 Internet Explorer 6 那样古老的浏览器显示）

2. 将以下行添加到 HTML 的 `<head>` 中以引用它：

   ```html
   <link rel="icon" href="favicon.ico" type="image/x-icon">
   ```

如今还有很多其他的图标类型可以考虑。例如，你可以在 MDN Web 文档的源代码中找到它：

```html
<!-- third-generation iPad with high-resolution Retina display: -->
<link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://developer.mozilla.org/static/img/favicon144.png">
<!-- iPhone with high-resolution Retina display: -->
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://developer.mozilla.org/static/img/favicon114.png">
<!-- first- and second-generation iPad: -->
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://developer.mozilla.org/static/img/favicon72.png">
<!-- non-Retina iPhone, iPod Touch, and Android 2.1+ devices: -->
<link rel="apple-touch-icon-precomposed" href="https://developer.mozilla.org/static/img/favicon57.png">
<!-- basic favicon -->
<link rel="icon" href="https://developer.mozilla.org/static/img/favicon32.png">

```

这些注释解释了每个图标的用途——这些元素涵盖的东西提供一个高分辨率图标，这些高分辨率图标当网站保存到 iPad 的主屏幕时使用。

不用担心现在实现所有这些类型的图标——这是一个相当先进的功能，你将不会被要求在这个课堂上学习这个知识点。这里的主要目的是让你提前了解有这一样东西以防当你浏览其他网站的源代码时不理解源代码的含义。

> **备注：** 如果你的网站使用了内容安全策略（Content Security Policy，CSP）来增加安全性，这个策略会应用在图标上。如果你遇到了图标没有被加载的问题，你需要确认 [`Content-Security-Policy`](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Content-Security-Policy) 响应头的 [img-src 指令)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/img-src) 没有禁止访问图标。

### 应用 CSS 和 JavaScript

如今，几乎你使用的所有网站都会使用 CSS 来让网页更加炫酷，并使用 JavaScript 来让网页有交互功能，比如视频播放器、地图、游戏以及更多功能。这些应用在网页中很常见，它们分别使用 `<link>` 元素以及 `<script>` 元素。

`<link>` 元素经常位于文档的头部。这个 link 元素有 2 个属性，`rel="stylesheet"` 表明这是文档的样式表，而 `href` 包含了样式表文件的路径：

```html
<link rel="stylesheet" href="my-css-file.css">
```

`<script>` 元素没必要非要放在文档的 `<head>` 中，并包含 src 属性来指向需要加载的 JavaScript 文件路径，同时最好加上 `defer` 以告诉浏览器在解析完成 HTML 后再加载 JavaScript。这样可以确保在加载脚本之前浏览器已经解析了所有的 HTML 内容（如果脚本尝试访问某个不存在的元素，浏览器会报错）。实际上还有很多方法可用于处理加载 JavaScript 的问题，但这是现代浏览器中最可靠的一种方法。

```html
<script src="my-js-file.js" defer></script>
```

### 为文档设定主语言

最后，值得一提的是可以（而且有必要）为站点设定语言，这个可以通过添加 [`lang` 属性](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes/lang)到 HTML 开始的标签中来实现（参考 [meta-example.html](https://github.com/mdn/learning-area/blob/main/html/introduction-to-html/the-html-head/meta-example.html)），如下所示：

```html
<html lang="zh-CN">
```

这在很多方面都很有用。如果你的 HTML 文档的语言设置好了，那么你的 HTML 文档就会被搜索引擎更有效地索引（例如，允许它在特定于语言的结果中正确显示），对于那些使用屏幕阅读器的视障人士也很有用（例如，法语和英语中都有“six”这个单词，但是发音却完全不同）。

你还可以将文档的分段设置为不同的语言。例如，我们可以把日语部分设置为日语，如下所示：

```html
<p>Japanese example: <span lang="ja">ご飯が熱い。</span>.</p>

```

这些代码是根据 [ISO 639-1](https://zh.wikipedia.org/wiki/ISO_639-1) 标准定义的。你可以在 [Language tags in HTML and XML](https://www.w3.org/International/articles/language-tags/) 找到更多相关内容。



## 文字处理

HTML 的主要工作是编辑文本结构和文本内容（也称为语义[semantics](https://developer.mozilla.org/zh-CN/docs/Glossary/Semantics)），以便浏览器能正确的显示。本文介绍了 [HTML](https://developer.mozilla.org/zh-CN/docs/Glossary/HTML)的使用方法：在一段文本中添加标题和段落，强调语句，创建列表等等。

### 标题和段落

大部分的文本结构由标题和段落组成。不管是小说、报刊、教科书还是杂志等。

内容结构化会使读者的阅读体验更轻松，更愉快。

在 HTML 中，每个段落是通过 `<p>` 元素标签进行定义的，每个标题（Heading）是通过“标题标签”进行定义的，这里有六个标题元素标签 —— `<h1>`、`<h2>`、`<h3>`、`<h4>`、`<h5>`、`<h6>`。每个元素代表文档中不同级别的内容; `<h1>` 表示主标题（the main heading），`<h2>` 表示二级子标题（subheadings），`<h3>` 表示三级子标题（sub-subheadings），等等。

#### 编辑结构层次

这里举一个例子。在一个故事中，`<h1>`表示故事的名字，`<h2>`表示每个章节的标题， `<h3>`表示每个章节下的子标题，以此类推。

```html
<h1>三国演义</h1>

<p>罗贯中</p>

<h2>第一回 宴桃园豪杰三结义 斩黄巾英雄首立功</h2>

<p>话说天下大势，分久必合，合久必分。周末七国分争，并入于秦。及秦灭之后，楚、汉分争，又并入于汉……</p>

<h2>第二回 张翼德怒鞭督邮 何国舅谋诛宦竖</h2>

<p>且说董卓字仲颖，陇西临洮人也，官拜河东太守，自来骄傲。当日怠慢了玄德，张飞性发，便欲杀之……</p>

<h3>却说张飞</h3>

<p>却说张飞饮了数杯闷酒，乘马从馆驿前过，见五六十个老人，皆在门前痛哭。飞问其故，众老人答曰：“督邮逼勒县吏，欲害刘公；我等皆来苦告，不得放入，反遭把门人赶打！”……</p>

```

所涉及的元素具体代表什么，完全取决于作者编辑的内容，只要层次结构是合理的。在创建此类结构时，您只需要记住一些最佳实践：

- 您应该最好只对每个页面使用一次`<h1>` — 这是顶级标题，所有其他标题位于层次结构中的下方。
- 请确保在层次结构中以正确的顺序使用标题。不要使用`<h3>`来表示副标题，后面跟`<h2>`来表示副副标题 - 这是没有意义的，会导致奇怪的结果。
- 在可用的六个标题级别中，您应该只在每页使用不超过三个，除非您认为有必要使用更多。具有许多级别的文档（即，较深的标题层次结构）变得难以操作并且难以导航。在这种情况下，如果可能，建议将内容分散在多个页面上。



#### 为什么我们需要结构化？

回答这个问题前，让我们先来看一段文档示例“[text-start.html](https://github.com/mdn/learning-area/blob/master/html/introduction-to-html/html-text-formatting/text-start.html)” — 并从运行这段文档示例（美味的豆沙食谱）开始。首先，您可以复制一份并保存到本地机器上，在之后的练习中您将用到它。在这个文档的主体（body）中包含了多个内容 — 这些内容没有做任何标记，但是编辑时使用了换行 (输入回车/换行跳转到下一行) 处理。

然而，当您在浏览器中打开文档时，您会看到文本显示为一整块！

![A webpage that shows a wall of unformatted text, because there are no elements on the page to structure it.](screen_shot_2017-03-29_at_09.20.35.png)

这是因为没有元素给内容结构，所以浏览器不知道什么是标题，什么是段落。此外：

- 用户在阅读网页时，往往会快速浏览以查找相关内容，经常只是阅读开头的标题（我们通常在一个网页上会花费很少的时间 [spend a very short time on a web page](http://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/))。如果用户不能在几秒内看到一些有用的内容，他们很可能会感到沮丧并离开。
- 对您的网页建立索引的搜索引擎将标题的内容视为影响网页搜索排名的重要关键字。没有标题，您的网页在[SEO](https://developer.mozilla.org/zh-CN/docs/Glossary/SEO)（搜索引擎优化）方面效果不佳。
- 严重视力障碍者通常不会阅读网页；他们用听力来代替。完成这项工作的软件叫做屏幕阅读器（[screen reader](http://en.wikipedia.org/wiki/Screen_reader)）。该软件提供了快速访问给定文本内容的方法。在使用的各种技术中，它们通过朗读标题来提供文档的概述，让用户能快速找到他们需要的信息。如果标题不可用，用户将被迫听到整个文档的大声朗读。
- 使用[CSS](https://developer.mozilla.org/zh-CN/docs/Glossary/CSS)样式化内容，或者使用[JavaScript](https://developer.mozilla.org/zh-CN/docs/Glossary/JavaScript)做一些有趣的事情，你需要包含相关内容的元素，所以 CSS / JavaScript 可以有效地定位它。



因此，我们需要给我们的内容结构标记。

#### 为什么我们需要语义？

在我们身边的任何地方都要依赖语义学 — 我们依靠以前的经验就知道日常事物都代表什么；当我们看到什么，我们就会知道它代表什么。举个例子，我们知道红色交通灯表示“停止”，绿色交通灯表示”通行“。如果运用了错误的语义，事情会迅速地变得非常棘手 (难道有某个国家使用红色代表通行？我不希望如此)

同样的道理，我们需要确保使用了正确的元素来给予内容正确的意思、作用以及外形。在这里，`<h1>` 元素也是一个语义元素，它给出了包裹在您的页面上用来表示顶级标题的角色（或意义）的文本。

```html
<h1>这是一个顶级标题</h1>
```



一般来说，浏览器会给它一个更大的字形来让它看上去像个标题（虽然你可以使用 CSS 让它变成任何你想要的样式。更重要的是，它的语义值将以多种方式被使用，比如通过搜索引擎和屏幕阅读器（上文提到过的）。

在另一方面，你可以让任一元素看起来像一个顶级标题，如下：

```html
<span style="font-size: 32px; margin: 21px 0;">这是顶级标题吗？</span>

```

这是一个 `<span>` 元素，它没有语义。当您想要对它用 CSS（或者 JS）时，您可以用它包裹内容，且不需要附加任何额外的意义（在未来的课程中你会发现更多这类元素）。我们已经对它使用了 CSS 来让它看起来像一个顶级标题。然而，由于它没有语义值，所以它不会有任何上文提到的帮助。最好的方法是使用相关的 HTML 元素来标记这个元素。

### 列表

现在，让我们学习一下列表。列表在生活中随处可见——从购物清单到回家的路线方案，再到本教程的说明列表。在网络上，列表也随处可见，大致包含了三种不同类型的列表。

#### 无序 Unordered

无序列表用于标记列表项目顺序无关紧要的列表 — 让我们以早点清单为例。

```html
豆浆
油条
豆汁
焦圈
```

每份无序的清单从` <ul>` 元素开始——需要包裹清单上所有被列出的项目：

```html
<ul>
豆浆
油条
豆汁
焦圈
</ul>

```

然后就是用 `<li>` 元素把每个列出的项目单独包裹起来：

```html
<ul>
  <li>豆浆</li>
  <li>油条</li>
  <li>豆汁</li>
  <li>焦圈</li>
</ul>

```

#### 有序 Ordered

有序列表需要按照项目的顺序列出来——让我们以一组方向为例：

```html
沿着条路走到头
右转
直行穿过第一个十字路口
在第三个十字路口处左转
继续走 300 米，学校就在你的右手边
```

这个标记的结构和无序列表一样，除了需要用`<ol>` 元素将所有项目包裹，而不是`<ul>`：

```html
<ol>
  <li>沿着条路走到头</li>
  <li>右转</li>
  <li>直行穿过第一个十字路口</li>
  <li>在第三个十字路口处左转</li>
  <li>继续走 300 米，学校就在你的右手边</li>
</ol>

```

#### 嵌套列表 Nesting lists

将一个列表嵌入到另一个列表是完全可以的。你可能想让一些子项目列在首项目之下。

由于最后两项与它们的前一项非常密切相关（它们看起来更像该项的子项或选项），将它们编辑成无序列表，并嵌套在该项的子项中可能更合理。就像下面这样：

```html
<ol>
  <li>先用蛋白一个、盐半茶匙及淀粉两大匙搅拌均匀，调成“腌料”，鸡胸肉切成约一厘米见方的碎丁并用“腌料”搅拌均匀，腌渍半小时。</li>
  <li>用酱油一大匙、淀粉水一大匙、糖半茶匙、盐四分之一茶匙、白醋一茶匙、蒜末半茶匙调拌均匀，调成“综合调味料”。</li>
  <li>鸡丁腌好以后，色拉油下锅烧热，先将鸡丁倒入锅内，用大火快炸半分钟，炸到变色之后，捞出来沥干油汁备用。</li>
  <li>在锅里留下约两大匙油，烧热后将切好的干辣椒下锅，用小火炒香后，再放入花椒粒和葱段一起爆香。随后鸡丁重新下锅，用大火快炒片刻后，再倒入“综合调味料”继续快炒。
    <ul>
      <li>如果你采用正宗川菜做法，最后只需加入花生米，炒拌几下就可以起锅了。</li>
      <li>如果你在北方，可加入黄瓜丁、胡萝卜丁和花生米，翻炒后起锅。</li>
    </ul>
  </li>
</ol>

```

### 重点强调

在日常用语中，我们常常会加重某个字的读音，或者用加粗等方式突出某句话的重点。与此类似，HTML 也提供了相应的标签，用于标记某些文本，使其具有加粗、倾斜、下划线等效果。下面，我们将学习一些最常见的标签。

#### 强调

在口语表达中，我们有时会强调某些字，用来改变这句话的意思。同样地，在书面用语中，我们可以使用斜体字来达到同样的效果。例如，下面两个句子便有不同的意思：

I am glad you weren't late.

I am *glad* you weren't *late*. (ps: 此句中"*glad"*和"late"为斜体字体)

第一句话听起来真的像松了一口气因为没有迟到。相反，第二句话听起来具有讽刺性而且有隐含的攻击性，表达对一个人迟到的恼怒。

在 HTML 中我们用`<em>`（emphasis）元素来标记这样的情况。这样做既可以让文档读起来更有趣，也可以被屏幕阅读器识别出来，并以不同的语调发出。浏览器默认风格为斜体，但你不应该纯粹使用这个标签来获得斜体风格，为了获得斜体风格，你应该使用`<span>`元素和一些 CSS，或者是`<i>`元素（见下文）。

```html
<p>I am <em>glad</em> you weren't <em>late</em>.</p>

```

#### 非常重要

为了强调重要的词，在口语方面我们往往用重音强调，在文字方面则是用粗体字来达到强调的效果。例如下面这段：

This liquid is **highly toxic**.

I am counting on you. **Do not** be late!

在 HTML 中我们用`<strong>` (strong importance) 元素来标记这样的情况。这样做既可以让文档更加地有用，也可以被屏幕阅读器识别出来，并以不同的语调发出。浏览器默认风格为粗体，但你不应该纯粹使用这个标签来获得粗体风格，为了获得粗体风格，你应该使用`<span>`元素和一些 CSS，或者是`<b>` 元素 (见下文)。

```html
<p>This liquid is <strong>highly toxic</strong>.</p>

<p>I am counting on you. <strong>Do not</strong> be late!</p>

```

#### 斜体字、粗体字、下划线...

迄今为止我们已经讨论的元素都是意义清楚的语义元素。`<b>`, `<i>`, 和 `<u>` 的情况却有点复杂。它们出现于人们要在文本中使用粗体、斜体、下划线但 CSS 仍然不被完全支持的时期。像这样的元素，仅仅影响表象而且没有语义，被称为**表象元素（presentational elements）**并且不应该再被使用。因为正如我们在之前看到的，语义对无障碍，SEO（搜索引擎优化）等非常重要。

HTML5 用新的语义规则重新定义了`<b>`,`<i>`和`<u>`,使得它们的语言显得稍微有点混乱。

这里是最好的经验法则：如果没有更合适的元素，那么使用 `<b>`、`<i>` 或 `<u>` 来表达传统上的粗体、斜体或下划线表达的意思是合适的。然而，始终拥有[无障碍](https://developer.mozilla.org/zh-CN/docs/Learn/Accessibility)的思维模式是至关重要的。斜体的概念对人们使用屏幕阅读器是没有帮助的，对使用其他书写系统而不是拉丁文书写系统的人们也是没有帮助的。

- `<i>` 被用来传达传统上用斜体表达的意义：外国文字，分类名称，技术术语，一种思想……
- `<b>` 被用来传达传统上用粗体表达的意义：关键字，产品名称，引导句……
- `<u>` 被用来传达传统上用下划线表达的意义：专有名词，拼写错误……



### 超链接

超链接非常重要 ——它们使互联网成为一个互联的网络。本文介绍了创建链接所需的语法，并且讨论了链接的最佳实现方法。

#### 什么是超链接？

超链接是互联网提供的最令人兴奋的创新之一，它们从一开始就一直是互联网的一个特性，使互联网成为互联的网络。超链接使我们能够将我们的文档链接到任何其他文档（或其他资源），也可以链接到文档的指定部分，我们可以在一个简单的网址上提供应用程序（与必须先安装的本地应用程序或其他东西相比）。几乎任何网络内容都可以转换为链接，点击（或激活）超链接将使网络浏览器转到另一个网址（[URL](https://developer.mozilla.org/zh-CN/docs/Glossary/URL)）。

> **备注：** URL 可以指向 HTML 文件、文本文件、图像、文本文档、视频和音频文件以及可以在网络上保存的任何其他内容。如果浏览器不知道如何显示或处理文件，它会询问你是否要打开文件（需要选择合适的本地应用来打开或处理文件）或下载文件（以后处理它）。

#### 链接的解析

通过将文本（或其它内容，见块级链接) 包裹在 `<a>` 元素内，并给它一个 `href` 属性（也称为超文本引用或目标，它将包含一个网址）来创建一个基本链接。

```html
<p>我创建了一个指向
<a href="https://www.mozilla.org/zh-CN/">Mozilla 主页</a>的超链接。
</p>

```

结果如下所示：

我创建了一个指向 [Mozilla 主页](https://www.mozilla.org/zh-CN/)的超链接。

##### title 属性

你可能要添加到你的链接的另一个属性是 `title`（标题）；这旨在包含关于链接的补充信息，例如页面包含什么样的信息或需要注意的事情。

```html
<p>我创建了一个指向<a href="https://www.mozilla.org/en-US/"
   title="了解 Mozilla 使命以及如何参与贡献的最佳站点。">Mozilla 主页</a
   >的超链接。
</p>

```

> **备注：** 链接的标题仅当鼠标悬停在其上时才会显示，这意味着使用键盘来导航网页的人很难获取到标题信息。如果标题信息对于页面非常重要，你应该使用所有用户能都方便获取的方式来呈现，例如放在常规文本中。

##### 块级链接

如上所述，你可以将一些内容转换为链接，甚至是块级元素。例如你想要将一个图像转换为链接，你只需把引用了图像文件的` <img>` 元素放到 `<a>` 标签内。

```html
<a href="https://www.mozilla.org/zh-CN/">
  <img src="mozilla-image.png" alt="链接至 Mozilla 主页的 Mozilla 标志">
</a>

```

#### URL与path

要全面地了解链接目标，你需要了解统一资源定位符和文件路径。本小节将介绍相关的信息。

统一资源定位符（英文：**U**niform **R**esource **L**ocator，简写：URL）是一个定义了在网络上的位置的一个文本字符串。例如 Mozilla 的中文主页定位在 `https://www.mozilla.org/zh-CN/`.

URL 使用路径查找文件。路径指定文件系统中你感兴趣的文件所在的位置。

![A simple directory structure. The parent directory is called creating-hyperlinks and contains two files called index.html and contacts.html, and two directories called projects and pdfs, which contain an index.html and a project-brief.pdf file, respectively](simple-directory.png)

此目录结构的**根目录**称为 `creating-hyperlinks`。当在网站上工作时，你会有一个包含整个网站的目录。在根目录，我们有一个 `index.html` 和一个 `contacts.html` 文件。在真实的网站上，`index.html` 将会成为我们的主页或登录页面（作为网站或网站特定部分的入口的网页）。

我们的根目录还有两个目录——`pdfs` 和 `projects`，它们分别包含一个 PDF（`project-brief.pdf`）文件和一个 `index.html` 文件。请注意你可以有两个 `index.html` 文件，前提是他们在不同的目录下，许多网站就是如此。第二个 `index.html` 或许是项目相关信息的主登录界面。

- **指向当前目录**：如果 `index.html`（目录顶层的 `index.html`）想要包含一个超链接指向 `contacts.html`，你只需要指定想要链接的文件名，因为它与当前文件是在同一个目录的。所以你应该使用的 URL 是 `contacts.html`:

  ```html
  <p>要联系某位工作人员，请访问我们的<a
   href="contacts.html">联系人页面</a>。</p>
  ```

- **指向子目录**：如果 `index.html` （目录顶层 `index.html`）想要包含一个超链接指向 `projects/index.html`，你需要先进入 `projects` 项目目录，然后指明要链接到的文件 `index.html`。 通过指定目录的名称，然后是正斜杠，然后是文件的名称。因此你要使用的 URL 是 `projects/index.html`：

  ```html
  <p>请访问<a href="projects/index.html">项目页面</a>。</p>
  
  ```

- **指向上级目录**：如果你想在 `projects/index.html` 中包含一个指向 `pdfs/project-brief.pdf` 的超链接，你必须先返回上级目录，然后再回到 `pdf` 目录。“返回上一个目录级”使用两个英文点号表示（`..`），所以你应该使用的 URL 是 `../pdfs/project-brief.pdf`：

  ```html
  <p>点击打开<a href="../pdfs/project-brief.pdf">项目简介</a>。</p>
  
  ```

##### 文档片段

超链接除了可以链接到文档外，也可以链接到 HTML 文档的特定部分（被称为**文档片段**）。要做到这一点，你必须首先给要链接到的元素分配一个 [`id`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes#attr-id) 属性。例如，如果你想链接到一个特定的标题，可以这样做：

```html
<h2 id="Mailing_address">邮寄地址</h2>

```

然后链接到那个特定的 `id`，你可以在 URL 的结尾使用一个井号指向它，例如：

```html
<p>要提供意见和建议，请将信件邮寄至<a href="contacts.html#Mailing_address">我们的地址</a>。</p>

```

你甚至可以在同一份文档下，通过链接文档片段，来链接到同一份文档的另一部分：

```html
<p>本页面底部可以找到<a href="#Mailing_address">公司邮寄地址</a>。</p>

```

##### 绝对 URL 和相对 URL

你可能会在网络上遇到两个术语，**绝对 URL** 和**相对 URL**（或者称为，**绝对链接**和**相对链接**）

**绝对 URL**：指向由其在 Web 上的绝对位置定义的位置，包括[协议](https://developer.mozilla.org/zh-CN/docs/Glossary/Protocol)和[域名](https://developer.mozilla.org/zh-CN/docs/Glossary/Domain_name)。像下面的例子，如果 `index.html` 页面上传到了 `projects` 这一个目录。并且 `projects` 目录位于 web 服务站点的根目录，web 站点的域名为 `http://www.example.com`，那么这个页面就可以通过 `http://www.example.com/projects/index.html` 访问（或者通过 `http://www.example.com/projects/` 来访问，因为在没有指定特定的 URL 的情况下，大多数 web 服务器会默认访问加载 `index.html` 这类页面）

不管绝对 URL 在哪里使用，它总是指向确定的相同位置。

**相对 URL**：指向与你链接的文件相关的位置，更像我们在前面一节中所看到的位置。例如，如果我们想从示例文件链接 `http://www.example.com/projects/index.html` 转到相同目录下的一个 PDF 文件，URL 就是文件名（例如 `project-brief.pdf`），没有其他的信息要求。如果 PDF 文件能够在 `projects` 的子目录 `pdfs` 中访问到，相对路径就是 `pdfs/project-brief.pdf`（对应的绝对 URL 是 `http://www.example.com/projects/pdfs/project-brief.pdf`）

一个相对 URL 将指向不同的位置，这取决于它所在的文件所在的位置——例如，如果我们把 `index.html` 文件从 `projects` 目录移动到 Web 站点的根目录（最高级别，而不是任何目录中），里面的 `pdfs/project-brief.pdf` 相对 URL 将会指向 `http://www.example.com/pdfs/project-brief.pdf`，而不是 `http://www.example.com/projects/pdfs/project-brief.pdf`

当然，`project-brief.pdf` 文件和 `pdfs` 文件夹的位置不会因为你移动了 `index.html` 文件而突然发生变化——这将使你的链接指向错误的位置，因此如果单击它，它将无法工作。你得小心点！

#### 链接最佳实践

下面是一些在编写链接元素时可以遵循的最佳实践。

##### 使用清晰的链接措辞

把链接放在你的页面上很容易。这还不够。我们需要让所有的读者都可以使用链接，不管他们当前的环境和哪些工具。例如：

- 使用屏幕阅读器的用户喜欢从页面上的一个链接跳到另一个链接，并且脱离上下文来阅读链接。
- 搜索引擎使用链接文本来索引目标文件，所以在链接文本中包含关键词是一个很好的主意，以有效地描述与之相关的信息。
- 读者往往会浏览页面而不是阅读每一个字，他们的眼睛会被页面的特征所吸引，比如链接。他们会找到描述性的链接。

**好的**链接文本：[下载 Firefox](https://www.mozilla.org/firefox/)

```html
<p><a href="https://www.mozilla.org/firefox/">
 下载 Firefox
</a></p>
```

**不好的**链接文本：[点击这里](https://www.mozilla.org/firefox/)下载 Firefox

```html
<p><a href="https://www.mozilla.org/firefox/">
  点击这里
</a>下载 Firefox</p>
```

其他提示：

- 不要重复 URL 作为链接文本的一部分——URL 看起来很丑，当屏幕阅读器一个字母一个字母的读出来的时候听起来就更丑了。
- 不要在链接文本中说“链接”或“链接到”——它只是无用的内容。屏幕阅读器告诉人们有一个链接。可视化用户也会知道有一个链接，因为链接通常是用不同的颜色设计的，并且存在下划线（这个惯例一般不应该被打破，因为用户习惯了它。）
- 保持你的链接标签尽可能短——这非常重要，因为屏幕阅读器需要解释整个链接文本。
- 尽量减少相同文本的多个副本链接到不同地方的情况。如果存在标记为“单击此处”、“单击此处”、“单击此处”这样脱离上下文的链接文本，容易对使用屏幕阅读器的用户带来问题。

##### 链接到非 HTML 资源——留下清晰的指示

当链接到一个需要下载的资源（如 PDF 或 Word 文档）或流媒体（如视频或音频）或有另一个潜在的意想不到的效果（打开一个弹出窗口，或加载 Flash 电影），你应该添加明确的措辞，以减少混乱。

如下的例子会让人反感：

- 你在使用低带宽连接的情况下，点击一个链接，然后就开始下载大文件。
- 你没有安装 Flash 播放器，点击一个链接，然后突然被带到一个需要 Flash 的页面。

让我们看看一些例子，看看在这里可以使用什么样的文本：

```html
<p><a href="https://www.example.com/large-report.pdf">
  下载销售报告（PDF, 10MB）
</a></p>

<p><a href="https://www.example.com/video-stream/" target="_blank">
  观看视频（将在新标签页中播放，HD 画质）
</a></p>

<p><a href="https://www.example.com/car-game">
  进入汽车游戏（需要 Flash 插件）
</a></p>

```

##### 在下载链接时使用 download 属性

当你链接到要下载的资源而不是在浏览器中打开时，你可以使用 download 属性来提供一个默认的保存文件名。下面是一个 Firefox 的 Windows 最新版本下载链接的示例：

```html
<a href="https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=zh-CN"
   download="firefox-latest-64bit-installer.exe">
  下载最新的 Firefox 中文版 - Windows（64位）
</a>

```



#### 电子邮件链接

当点击一个链接或按钮时，打开一个新的电子邮件发送信息而不是连接到一个资源或页面，这种情况是可能做到的。这样做是使用 `<a>` 元素和 `mailto:URL` 的方案。

其最基本和最常用的使用形式为一个 `mailto:` 链接，链接指明收件人的电子邮件地址。例如：

```html
<a href="mailto:nowhere@mozilla.org">向 nowhere 发邮件</a>

```

这会创建一个链接，看起来像这样：[向 nowhere 发邮件](mailto:nowhere@mozilla.org)。

实际上，电子邮件地址是可选的。如果你忘记了（也就是说，你的 [`href`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a#attr-href) 仅仅只是简单的“mailto”），一个新的发送电子邮件的窗口也会被用户的邮件客户端打开，只是没有收件人的地址信息，这通常在“分享”链接是很有用的，用户可以给他们选择的地址发送邮件。

##### 指定详细信息

除了电子邮件地址，你还可以提供其他信息。事实上，任何标准的邮件头字段可以被添加到你提供的 `mailto` URL 中。其中最常用的是主题（subject）、抄送（cc）和主体（body）（这不是一个真正的标头字段，但允许你为新邮件指定一个简短的内容消息）。 每个字段及其值被指定为查询项。

下面是一个包含 cc、bcc、主题和主体的示例：

```html
<a href="mailto:nowhere@mozilla.org?cc=name2@rapidtables.com&bcc=name3@rapidtables.com&subject=The%20subject%20of%20the%20email&body=The%20body%20of%20the%20email">
  Send mail with cc, bcc, subject and body
</a>

```

> **备注：** 每个字段的值必须是使用 URL 编码的，即使用[百分号转义的](https://zh.wikipedia.org/wiki/百分号编码)非打印字符（不可见字符比如制表符、换行符、分页符）和空格。同时注意使用问号（`?`）来分隔主 URL 与参数值，以及使用 & 符来分隔 `mailto:` URL 中的各个参数。 这是标准的 URL 查询标记方法。阅读 [GET 方法](https://developer.mozilla.org/zh-CN/docs/Learn/Forms/Sending_and_retrieving_form_data#get_方法)以了解哪种 URL 查询标记方法是更常用的。

这里有一些其他的示例 `mailto` 链接：

- `mailto:`
- `mailto:nowhere@mozilla.org`
- `mailto:nowhere@mozilla.org,nobody@mozilla.org`
- `mailto:nowhere@mozilla.org?cc=nobody@mozilla.org`
- `mailto:nowhere@mozilla.org?cc=nobody@mozilla.org&subject=This%20is%20the%20subject`



### 高阶文字排版

#### 描述列表

描述列表使用与其他列表类型不同的闭合标签— `<dl>`; 

此外，每一项都用` <dt>` (description term) 元素闭合。每个描述都用 `<dd>` (description definition) 元素闭合。

```html
<dl>
  <dt>内心独白</dt>
    <dd>戏剧中，某个角色对自己的内心活动或感受进行念白表演，这些台词只面向观众，而其他角色不会听到。</dd>
  <dt>语言独白</dt>
    <dd>戏剧中，某个角色把自己的想法直接进行念白表演，观众和其他角色都可以听到。</dd>
  <dt>旁白</dt>
    <dd>戏剧中，为渲染幽默或戏剧性效果而进行的场景之外的补充注释念白，只面向观众，内容一般都是角色的感受、想法、以及一些背景信息等。</dd>
</dl>

```

一个术语 `<dt>` 可以同时有多个描述 `<dd>`

#### 引用

##### 块引用

如果一个块级内容（一个段落、多个段落、一个列表等）从其他地方被引用，你应该把它用`<blockquote>`元素包裹起来表示，并且在cite属性里用 URL 来指向引用的资源。

```html
<blockquote cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
  <p>The <strong>HTML <code>&lt;blockquote&gt;</code> Element</strong> (or <em>HTML Block
  Quotation Element</em>) indicates that the enclosed text is an extended quotation.</p>
</blockquote>

```

浏览器在渲染块引用时默认会增加缩进，作为引用的一个指示符；MDN 是这样做的，但是也增加了额外的样式：

![image-20221115210557933](image-20221115210557933.png)

##### 行内引用

行内元素用同样的方式工作，除了使用`<q>`元素。例如，下面的标记包含了从 MDN`<q>`页面的引用：

```html
<p>The quote element — <code>&lt;q&gt;</code> — is <q cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q">intended
for short quotations that don't require paragraph breaks.</q></p>

```

![image-20221115210722695](image-20221115210722695.png)

##### 引文

cite属性内容不会被浏览器显示、屏幕阅读器阅读，需使用 JavaScript 或 CSS，浏览器才会显示cite的内容。如果你想要确保引用的来源在页面上是可显示的，更好的方法是为`<cite>`元素附上链接：

引文默认的字体样式为斜体

```html
<p>According to the <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
<cite>MDN blockquote page</cite></a>:
</p>

<blockquote cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote">
  <p>The <strong>HTML <code>&lt;blockquote&gt;</code> Element</strong> (or <em>HTML Block
  Quotation Element</em>) indicates that the enclosed text is an extended quotation.</p>
</blockquote>

<p>The quote element — <code>&lt;q&gt;</code> — is <q cite="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q">intended
for short quotations that don't require paragraph breaks.</q> -- <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q">
<cite>MDN q page</cite></a>.</p>

```

![image-20221115211023728](image-20221115211023728.png)

#### 缩略语

`<abbr>`——它常被用来包裹一个缩略语或缩写，并且提供缩写的解释（包含在title属性中）

```html
<p>我们使用 <abbr title="超文本标记语言（Hyper text Markup Language）">HTML</abbr> 来组织网页文档。</p>

<p>第 33 届 <abbr title="夏季奥林匹克运动会">奥运会</abbr> 将于 2024 年 8 月在法国巴黎举行。</p>

```

![image-20221115211247068](image-20221115211247068.png)

#### 标记联系方式

`<address>`，它仅仅包含你的联系方式

```html
<address>
  <p>Chris Mills, Manchester, The Grim North, UK</p>
</address>

<address>
  <p>Page written by <a href="../authors/chris-mills/">Chris Mills</a>.</p>
</address>

```

![image-20221115211500656](image-20221115211500656.png)

#### 上标和下标

当你使用日期、化学方程式、和数学方程式时会偶尔使用上标和下标。`<sup>` 和`<sub>`元素可以解决这样的问题

```html
<p>咖啡因的化学方程式是 C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub>。</p>
<p>如果 x<sup>2</sup> 的值为 9，那么 x 的值必为 3 或 -3。</p>

```

![image-20221115211623019](image-20221115211623019.png)

#### 展示计算机代码

有大量的 HTML 元素可以来标记计算机代码：

- `<code>`：用于标记计算机通用代码。
- `<pre>`：用于保留空白字符（通常用于代码块）——如果您在文本中使用缩进或多余的空白，浏览器将忽略它，您将不会在呈现的页面上看到它。但是，如果您将文本包含在`<pre></pre>`标签中，那么空白将会以与你在文本编辑器中看到的相同的方式渲染出来。
- `<var>`： 用于标记具体变量名。
- `<kbd>`：用于标记输入电脑的键盘（或其他类型）输入。
- `<samp>`：用于标记计算机程序的输出。

```html
    <pre>
        <code>const para = document.querySelector('p');

        para.onclick = function() {
          alert('噢，噢，噢，别点我了。');
        }</code>
    </pre>
        
    <p>请不要使用 <code>&lt;font&gt;</code> 、 <code>&lt;center&gt;</code> 等表象元素。</p>
    
    <p>在上述的 JavaScript 示例中，<var>para</var> 表示一个段落元素。</p>
    
    
    <p>按 <kbd>Ctrl</kbd>/<kbd>Cmd</kbd> + <kbd>A</kbd> 选择全部内容。</p>
    
    <pre>
        $ <kbd>ping mozilla.org</kbd>
        <samp>PING mozilla.org (63.245.215.20): 56 data bytes 64 bytes from 63.245.215.20: icmp_seq=0 ttl=40 time=158.233 ms</samp>
    </pre>
```

![image-20221115212227872](image-20221115212227872.png)

#### 标记时间和日期

HTML 还支持将时间和日期标记为可供机器识别的格式的` <time> `元素

```html
<time datetime="2016-01-20">2016 年 1 月 20 日</time>

```

为什么需要这样做？因为世界上有许多种书写日期的格式，上边的日期可能被写成：

- 20 January 2016
- 20th January 2016
- Jan 20 2016
- 20/06/16
- 06/20/16
- The 20th of next month
- 20e Janvier 2016
- 2016 年 1 月 20 日
- And so on

但是这些不同的格式不容易被电脑识别 — 假如你想自动抓取页面上所有事件的日期并将它们插入到日历中，` <time> `元素允许你附上清晰的、可被机器识别的 时间/日期来实现这种需求。

上述基本的例子仅仅提供了一种简单的可被机器识别的日期格式，这里还有许多其他支持的格式，例如：

```html
<!-- 标准简单日期 -->
<time datetime="2016-01-20">20 January 2016</time>
<!-- 只包含年份和月份-->
<time datetime="2016-01">January 2016</time>
<!-- 只包含月份和日期 -->
<time datetime="01-20">20 January</time>
<!-- 只包含时间，小时和分钟数 -->
<time datetime="19:30">19:30</time>
<!-- 还可包含秒和毫秒 -->
<time datetime="19:30:01.856">19:30:01.856</time>
<!-- 日期和时间 -->
<time datetime="2016-01-20T19:30">7.30pm, 20 January 2016</time>
<!-- 含有时区偏移值的日期时间 -->
<time datetime="2016-01-20T19:30+01:00">7.30pm, 20 January 2016 is 8.30pm in France</time>
<!-- 调用特定的周 -->
<time datetime="2016-W04">The fourth week of 2016</time>

```



### 文档与网站架构

#### 文档的基本组成部分

网页的外观多种多样，但是除了全屏视频或游戏，或艺术作品页面，或只是结构不当的页面以外，都倾向于使用类似的标准组件：

- 页眉

  通常横跨于整个页面顶部有一个大标题 和/或 一个标志。这是网站的主要一般信息，通常存在于所有网页。

- 导航栏

  指向网站各个主要区段的超链接。通常用菜单按钮、链接或标签页表示。类似于标题栏，导航栏通常应在所有网页之间保持一致，否则会让用户感到疑惑，甚至无所适从。许多 web 设计人员认为导航栏是标题栏的一部分，而不是独立的组件，但这并非绝对；还有人认为，两者独立可以提供更好的 [无障碍访问特性](https://developer.mozilla.org/zh-CN/docs/Learn/Accessibility)，因为屏幕阅读器可以更清晰地分辨二者。

- 主内容

  中心的大部分区域是当前网页大多数的独有内容，例如视频、文章、地图、新闻等。这些内容是网站的一部分，且会因页面而异。

- 侧边栏

  一些外围信息、链接、引用、广告等。通常与主内容相关（例如一个新闻页面上，侧边栏可能包含作者信息或相关文章链接），还可能存在其他的重复元素，如辅助导航系统。

- 页脚

  横跨页面底部的狭长区域。和标题一样，页脚是放置公共信息（比如版权声明或联系方式）的，一般使用较小字体，且通常为次要内容。还可以通过提供快速访问链接来进行 [SEO](https://developer.mozilla.org/zh-CN/docs/Glossary/SEO)。

一个“典型的网站”可能会这样布局：

![一个简单站点首页截图](sample-website.png)

#### 构建内容的`HTML`

HTML 代码中可根据功能来为区段添加标记。可使用元素来无歧义地表示上文所讲的内容区段，屏幕阅读器等辅助技术可以识别这些元素，并帮助执行“找到主导航“或”找到主内容“等任务。参见前文所讲的 [页面中元素结构和语义不佳所带来的后果](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals#为什么我们需要结构化)。

为了实现语义化标记，HTML 提供了明确这些区段的专用标签，例如：

- `<header>`：页眉。
- `<nav>`：导航栏。
- `<main>`主内容。主内容中还可以有各种子内容区段，可用`<article>`、`<section>` 和 `<div>` 等元素表示。
- `<aside>`：侧边栏，经常嵌套在 `<main>` 中。
- `<footer>`：页脚。

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>二次元俱乐部</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300|Sonsie+One" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=ZCOOL+KuaiLe" rel="stylesheet">
    <link href="style.css" rel="stylesheet">
  </head>

  <body>
    <header> <!-- 本站所有网页的统一主标题 -->
      <h1>聆听电子天籁之音</h1>
    </header>

    <nav> <!-- 本站统一的导航栏 -->
      <ul>
        <li><a href="#">主页</a></li>
        <!-- 共 n 个导航栏项目，省略…… -->
      </ul>

      <form> <!-- 搜索栏是站点内导航的一个非线性的方式。 -->
        <input type="search" name="q" placeholder="要搜索的内容">
        <input type="submit" value="搜索">
      </form>
    </nav>

    <main> <!-- 网页主体内容 -->
      <article>
        <!-- 此处包含一个 article（一篇文章），内容略…… -->
      </article>

      <aside> <!-- 侧边栏在主内容右侧 -->
        <h2>相关链接</h2>
        <ul>
          <li><a href="#">这是一个超链接</a></li>
          <!-- 侧边栏有 n 个超链接，略略略…… -->
        </ul>
      </aside>
    </main>

    <footer> <!-- 本站所有网页的统一页脚 -->
      <p>© 2050 某某保留所有权利</p>
    </footer>
  </body>
</html>
```

#### 布局元素细节

理解所有 HTML 区段元素具体含义是很有益处的，这一点将随着个人 web 开发经验的逐渐丰富日趋显现。更多细节请查阅 [HTML 元素参考](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element)。现在，你只需要理解以下主要元素的意义：

- `<main>`存放每个页面独有的内容。每个页面上只能用一次 `<main>`，且直接位于 [``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/body) 中。最好不要把它嵌套进其它元素。
- `<article>`包围的内容即一篇文章，与页面其它部分无关（比如一篇博文）。
- `<section>`与 `<article>` 类似，但 `<section>` 更适用于组织页面使其按功能（比如迷你地图、一组文章标题和摘要）分块。
  - 一般的最佳用法是：以 [标题](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Howto/Set_up_a_proper_title_hierarchy) 作为开头；也可以把一篇 `<article>` 分成若干部分并分别置于不同的 `<section>` 中，也可以把一个区段 `<section>` 分成若干部分并分别置于不同的 `<article>` 中，取决于上下文。
- `<header>`是简介形式的内容。如果它是 `<body>` 的子元素，那么就是网站的全局页眉。如果它是 `<article>` 或`<section>` 的子元素，那么它是这些部分特有的页眉（此 `<header>` 非彼 标题）。
-  `<nav>` 包含页面主导航功能。其中不应包含二级链接等内容。
-  `<footer>` 包含了页面的页脚部分。

#### 无语义元素

对于一些要组织的项目或要包装的内容，现有的语义元素均不能很好对应。有时候你可能只想将一组元素作为一个单独的实体来修饰来响应单一的用 CSS 或 JavaScript。

为了应对这种情况，HTML 提供了` <div> `和 `<span>` 元素。应配合使用 class 属性提供一些标签，使这些元素能易于查询。

#### 规划一个简单的网站

在完成页面内容的规划后，一般应按部就班地规划整个网站的内容，要可能带给用户最好的体验，需要哪些页面、如何排列组合这些页面、如何互相链接等问题不可忽略。这些工作称为[信息架构](https://developer.mozilla.org/zh-CN/docs/Glossary/Information_architecture)。在大型网站中，大多数规划工作都可以归结于此，而对于一个只有几个页面的简单网站，规划设计过程可以更简单，更有趣！

1.时刻记住，大多数（不是全部）页面会使用一些相同的元素，例如导航菜单以及页脚内容。若网站为商业站点，不妨在所有页面的页脚都加上联系方式。请记录这些对所有页面都通用的内容：

![所有页面共有的内容，包括：站点标题、Logo、联系方式、版权声明、语言等信息。](common-features.png)

2。时刻记住，大多数（不是全部）页面会使用一些相同的元素，例如导航菜单以及页脚内容。若网站为商业站点，不妨在所有页面的页脚都加上联系方式。请记录这些对所有页面都通用的内容：

![简单的页面布局示意图，有页眉、页脚、主内容、侧边栏。](site-structure.png)

3.下面，对于期望添加进站点的所有其它（通用内容以外的）内容展开头脑风暴，直接罗列出来。

![把假日旅行站点的所有功能罗列到一个列表中](feature-list.png)

4.下一步，试着对这些内容进行分组，这样可以让你了解哪些内容可以放在同一个页面。这种做法和 [卡片分类法](https://developer.mozilla.org/zh-CN/docs/Glossary/Card_sorting) 非常相似。

![假日网站的页面应分 5 类：搜索、特别提供、具体国家信息、搜索结果、购物。](card-sorting.png)

5.接下来，试着绘制一个站点地图的草图，使用一个气泡代表网站的一个页面，并绘制连线来表示页面间的一般工作流。主页面一般置于中心，且链接到其他大多数页面；小型网站的大多数页面都可以从主页的导航栏中链接跳转。也可记录下内容的显示方式。

![img](site-map.png)

## 多媒体与嵌入

本模块要探索怎样用 HTML 来让你的网页包含多媒体，包括可以包含图像的不同方式，以及怎样嵌入视频，甚至是整个其他的网页。

### HTML 中的图片

在这篇文章中，我们将看到怎样深入的使用它，包括基本的用[``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/figure)来添加说明文字，以及怎样把它和 CSS 背景图片链接起来。

#### 怎样将图片放在网页上？

我们可以用`<img>` 元素来把图片放到网页上。

它是一个空元素（它不需要包含文本内容或闭合标签），最少只需要一个` src` （一般读作其全称 source）来使其生效。

`src` 属性包含了指向我们想要引入的图片的路径，可以是相对路径或绝对 URL，就像` <a>` 元素的 href 属性一样。



如果这张图片存储在和 HTML 页面同路径的 `images` 文件夹下（这也是 Google 推荐的做法，利于[SEO](https://developer.mozilla.org/zh-CN/docs/Glossary/SEO)/索引），那么你可以采用如下形式

> **备注：** 搜索引擎也读取图像的文件名并把它们计入 `SEO`。因此你应该给你的图片取一个描述性的文件名：`dinosaur.jpg` 比 `img835.png` 要好。

```html
<img src="images/dinosaur.jpg">
```



你也可以像下面这样使用绝对路径：

```html
<img src="https://www.example.com/images/dinosaur.jpg">
```

但是这种方式是不被推荐的，这样做只会使浏览器做更多的工作，例如重新通过 `DNS` 再去寻找` IP` 地址。通常我们都会把图片和 HTML 放在同一个服务器上。



> 备注： 像`<img>`和`<video>`这样的元素有时被称之为替换元素，因为这样的元素的内容和尺寸由外部资源（像是一个图片或视频文件）所定义，而不是元素自身。

##### 备选文本

属性 `alt` ，它的值应该是对图片的文字描述，用于在图片无法显示或不能被看到的情况。例如，上面的例子可以做如下改进：

```html
<img src="images/dinosaur.jpg"
     alt="The head and torso of a dinosaur skeleton;
          it has a large head with long sharp teeth">
```

本质上，关键在于在图片无法被看见时也提供一个可用的体验，这确保了所有人都不会错失一部分内容。尝试在浏览器中使图片不可见然后看看网页变成什么样了，你会很快意识到在图片无法显示时备选文本能帮上多大忙。

##### 宽度和高度

**备注：** 如果你需要改变图片的尺寸，你应该使用[CSS](https://developer.mozilla.org/zh-CN/docs/Learn/CSS)而不是 HTML。

##### 图片标题

类似于[超链接](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks#使用添加支持信息)，你可以给图片增加`title`属性来提供需要更进一步的支持信息。

```html
<img src="images/dinosaur.jpg"
     alt="一只恐龙头部和躯干的骨架，它有一个巨大的头，长着锋利的牙齿。"
     width="400"
     height="341"
     title="A T-Rex on display in the Manchester University Museum">
```

图片标题并不必须要包含有意义的信息，通常来说，将这样的支持信息放到主要文本中而不是附着于图片会更好。不过，在有些环境中这样做更有用，比如当没有空间显示提示时，也就是在图片栏中。

#### 为图片搭配说明文字

说到说明文字，这里有很多种方法让你添加一段说明文字来搭配图片。比如，没有人会阻止你这么做：

```html
<div class="figure">
  <img src="/images/dinosaur_small.jpg"
     alt="一只恐龙头部和躯干的骨架，它有一个巨大的头，长着锋利的牙齿。"
     width="400"
     height="341">
  <p>曼彻斯特大学博物馆展出的一只霸王龙的化石</p>
</div>
```

有一个更好的做法是使用 HTML5 的 `<figure>` 和 `<figcaption>` 元素，它正是为此而被创造出来的：为图片提供一个语义容器，在标题和图片之间建立清晰的关联。我们之前的例子可以重写为：

```html
<figure>
  <img src="https://raw.githubusercontent.com/mdn/learning-area/master/html/multimedia-and-embedding/images-in-html/dinosaur_small.jpg"
      alt="一只恐龙头部和躯干的骨架，它有一个巨大的头，长着锋利的牙齿。"
      width="400"
      height="341">
  <figcaption>曼彻斯特大学博物馆展出的一只霸王龙的化石</figcaption>
</figure>
```

> **备注：** 从无障碍的角度来说，说明文字和 [`alt`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img#attr-alt) 文本扮演着不同的角色。看得见图片的人们同样可以受益于说明文字，而 [`alt`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img#attr-alt) 文字只有在图片无法显示时才这样。所以，说明文字和 `alt` 的内容不应该一样，因为当图片无法显示时，它们会同时出现。

`<figure>` 可以是几张图片、一段代码、音视频、方程、表格或别的。

#### `CSS`背景图片

CSS 属性 [`background-image`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-image) 和另其他 `background-*` 属性是用来放置背景图片的。比如，为页面中的所有段落设置一个背景图片，你可以这样做：

```css
p {
  background-image: url("images/dinosaur.jpg");
}
```

按理说，这种做法相对于 HTML 中插入图片的做法，可以更好地控制图片和设置图片的位置，那么为什么我们还要使用 HTML 图片呢？如上所述，CSS 背景图片只是为了装饰 — 如果你只是想要在你的页面上添加一些漂亮的东西，来提升视觉效果，那 CSS 的做法是可以的。但是这样插入的图片完全没有语义上的意义，它们不能有任何备选文本，也不能被屏幕阅读器识别。这就是 HTML 图片有用的地方了。

总而言之，如果图像对您的内容里有意义，则应使用 HTML 图像。如果图像纯粹是装饰，则应使用 CSS 背景图片。

### 视频和音频内容

在这篇文章中，我们会使用 `<video>` 和 `<audio>` 元素来做到这件事；然后我们还会看看如何为你的视频添加字幕。

#### `<video>` 

```html
<video src="rabbit320.webm" controls>
  <p>你的浏览器不支持 HTML5 视频。可点击<a href="rabbit320.mp4">此链接</a>观看</p>
</video>
```

`src`

- 同 `<img>` 标签使用方式相同，src 属性指向你想要嵌入网页当中的视频资源，他们的使用方式完全相同。

`controls`

- 用户必须能够控制视频和音频的回放功能。你可以使用 `controls` 来包含浏览器提供的控件界面，同时你也可以使用合适的 [JavaScript API](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement) 创建自己的界面。界面中至少要包含开始、停止以及调整音量的功能。

`<video>` 标签内的内容

- 这个叫做**后备内容** — 当浏览器不支持 `<video>` 标签的时候，就会显示这段内容，这使得我们能够对旧的浏览器提供回退内容。你可以添加任何后备内容，在这个例子中我们提供了一个指向这个视频文件的链接，从而使用户至少可以访问到这个文件，而不会局限于浏览器的支持。

##### 使用多个播放源以提高兼容性

以上的例子中有一个问题，你可能已经注意到了，如果你尝试使用像 Safari 或者 Internet Explorer 这些浏览器来访问上面的链接。视频并不会播放，这是因为不同的浏览器对视频格式的支持不同。幸运的是，你有办法防止这个问题发生。



```html
<video controls>
  <source src="rabbit320.mp4" type="video/mp4">
  <source src="rabbit320.webm" type="video/webm">
  <p>你的浏览器不支持 HTML5 视频。可点击<a href="rabbit320.mp4">此链接</a>观看</p>
</video>
```

现在我们将 src 属性从 `<video>` 标签中移除，转而将它放在几个单独的标签 `<source>` 当中。在这个例子当中，浏览器将会检查 `<source>` 标签，并且播放第一个与其自身 `codec` 相匹配的媒体。你的视频应当包括 `WebM` 和 `MP4` 两种格式，这两种在目前已经足够支持大多数平台和浏览器。

每个 `<source>` 标签页含有一个 `type` 属性，这个属性是可选的，但是建议你添加上这个属性 — 它包含了视频文件的 [MIME types](https://developer.mozilla.org/zh-CN/docs/Glossary/MIME_type) ，同时浏览器也会通过检查这个属性来迅速的跳过那些不支持的格式。如果你没有添加 `type` 属性，浏览器会尝试加载每一个文件，直到找到一个能正确播放的格式，这样会消耗掉大量的时间和资源。

##### 新的特性

```html
<video controls width="400" height="400"
       autoplay loop muted
       poster="poster.png">
  <source src="rabbit320.mp4" type="video/mp4">
  <source src="rabbit320.webm" type="video/webm">
  <p>你的浏览器不支持 HTML5 视频。可点击<a href="rabbit320.mp4">此链接</a>观看</p>
</video>
```

`width` 和 `height`

- 你可以用属性控制视频的尺寸，也可以用 [CSS](https://developer.mozilla.org/zh-CN/docs/Glossary/CSS) 来控制视频尺寸。无论使用哪种方式，视频都会保持它原始的长宽比 — 也叫做**纵横比**。如果你设置的尺寸没有保持视频原始长宽比，那么视频边框将会拉伸，而未被视频内容填充的部分，将会显示默认的背景颜色。

`autoplay`

- 这个属性会使音频和视频内容立即播放，即使页面的其他部分还没有加载完全。建议不要应用这个属性在你的网站上，因为用户们会比较反感自动播放的媒体文件。

`loop`

- 这个属性可以让音频或者视频文件循环播放。同样不建议使用，除非有必要。

`muted`

- 这个属性会导致媒体播放时，默认关闭声音。

`poster`

- 这个属性指向了一个图像的 URL，这个图像会在视频播放前显示。通常用于粗略的预览或者广告。

`preload`

- 这个属性被用来缓冲较大的文件，有 3 个值可选：
  - `"none"` ：不缓冲
  - `"auto"` ：页面加载后缓存媒体文件
  - `"metadata"` ：仅缓冲文件的元数据

#### `<audio> `

`<audio>` 标签与 `<video>` 标签的使用方式几乎完全相同，有一些细微的差别比如下面的边框不同，一个典型的例子如下：

```html
<audio controls>
  <source src="viper.mp3" type="audio/mp3">
  <source src="viper.ogg" type="audio/ogg">
  <p>你的浏览器不支持 HTML5 音频，可点击<a href="viper.mp3">此链接</a>收听。</p>
</audio>
```

音频播放器所占用的空间比视频播放器要小，由于它没有视觉部件 — 你只需要显示出能控制音频播放的控件。一些与 HTML5 `<video>` 的差异如下：

- `<audio>` 标签不支持 `width/height` 属性 — 由于其并没有视觉部件，也就没有可以设置 width/height 的内容。
- 同时也不支持 `poster` 属性 — 同样，没有视觉部件。

除此之外，`<audio>` 标签支持所有 `<video>` 标签拥有的特性

#### 重新播放媒体

任何时候，你都可以在 Javascript 中调用 [`load()`](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/load) 方法来重置媒体。如果有多个由 [`<source>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/source) 标签指定的媒体来源，浏览器会从选择媒体来源开始重新加载媒体。

```js
const mediaElem = document.getElementById("my-media-element");
mediaElem.load();
```

#### 音轨增删事件

你可以监控媒体元素中的音频轨道，当音轨被添加或删除时，你可以通过监听相关事件来侦测到。

具体来说，通过监听 [`AudioTrackList` ](https://developer.mozilla.org/en-US/docs/Web/API/AudioTrackList) 对象的 `addtrack` 事件（即 [`HTMLMediaElement.audioTracks`](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLMediaElement/audioTracks) 对象），你可以及时对音轨的增加做出响应。

```js
const mediaElem = document.querySelector("video");
mediaElem.audioTracks.onaddtrack = function(event) {
  audioTrackAdded(event.track);
}
```

#### 显示音轨文本

有了 [WebVTT ](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) 格式，你可以使用 [`<track>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/track) 标签

WebVTT 是一个格式，用来编写文本文件，这个文本文件包含了众多的字符串，这些字符串会带有一些元数据，它们可以用来描述这个字符串将会在视频中显示的时间，甚至可以用来描述这些字符串的样式以及定位信息。这些字符串叫做 **cues** ，你可以根据不同的需求来显示不同的样式，最常见的如下：

subtitles

- 通过添加翻译字幕，来帮助那些听不懂外国语言的人们理解音频当中的内容。

captions

- 同步翻译对白，或是描述一些有重要信息的声音，来帮助那些不能听音频的人们理解音频中的内容。

timed descriptions

- 将文字转换为音频，用于服务那些有视觉障碍的人。

一个典型的 WebVTT 文件如下：

```
WEBVTT

1
00:00:22.230 --> 00:00:24.606
第一段字幕

2
00:00:30.739 --> 00:00:34.074
第二段

  ...
```

让其与 HTML 媒体一起显示，你需要做如下工作：

1.以 .vtt 后缀名保存文件。

2.用 `<track>` 标签链接 `.vtt` 文件， `<track>` 标签需放在 `<audio>` 或 `<video>` 标签当中，同时需要放在所有 `<source>` 标签之后。使用 kind 属性来指明是哪一种类型，如 subtitles、captions、descriptions。然后，使用 srclang 来告诉浏览器你是用什么语言来编写的 subtitles。

```html
<video controls>
    <source src="example.mp4" type="video/mp4">
    <source src="example.webm" type="video/webm">
    <track kind="subtitles" src="subtitles_en.vtt" srclang="en">
</video>
```

![Video player with stand controls such as play, stop, volume, and captions on and off. The video playing shows a scene of a man holding a spear-like weapon, and a caption reads "Esta hoja tiene pasado oscuro."](video-player-with-captions.png)

如果你想了解更多细节，你可以阅读 [Adding captions and subtitles to HTML5 video](https://developer.mozilla.org/zh-CN/docs/Web/Apps/Build/Audio_and_video_delivery/Adding_captions_and_subtitles_to_HTML5_video)。在 Github 上你可以找到与本文相关的样例，他们由 Ian Devlin 编写，点击[这里](https://iandevlin.github.io/mdn/video-player-with-captions/)可以查看该样例，或者点击[这里](https://github.com/iandevlin/iandevlin.github.io/tree/master/mdn/video-player-with-captions)查看源代码。

### 从对象到 `iframe` - 其他嵌入技术

让我们继续深入学习，来看一些能让你在网页中嵌入各种内容类型的元素：`<iframe>`,` <embed>` 和 `<object> `元素。

`<iframe>`用于嵌入其他网页，另外两个元素则允许你嵌入 PDF，SVG，甚至 Flash — 一种正在被淘汰的技术，但你仍然会时不时的看到它。

#### 嵌入的简史

很久以前，很流行在网络上使用**框架**创建网站——网站的一小部分存储于单独的 HTML 页面中。这些被嵌入在一个称为**框架集**的主文档中，它允许你指定每个框架能够填充在屏幕上的区域，非常像调整表格的列和行的大小。这些做法在 90 年代中期至 90 年代后期被认为是比较酷的，有证据表明，将网页分解成较小的块，这样有利于下载速度——尤其是在那时网络连接速度太慢的情况下更为明显。然而，这些技术有很多问题，随着网络速度越来越快，这些技术带来的问题远超过它们带来的积极因素，所以你再也看不到它们被使用了。

一小段时间之后（20 世纪 90 年代末，21 世纪初），插件技术变得非常受欢迎，例如 `Java Applet` 和 `Flash`——这些技术允许网络开发者将丰富的内容嵌入到网页中，例如视频和动画等，这些内容不能通过 HTML 单独实现。嵌入这些技术是通过诸如 `<object>` 和较少使用的` <embed>` 元素来实现的，当时它们非常有用。由于许多问题，包括无障碍、安全性、文件大小等，它们已经过时了; 如今，大多数移动设备不再支持这些插件，桌面端也逐渐不再支持。

最后，`<iframe>` 元素出现了（连同其他嵌入内容的方式，如` <canvas>`、`<video>` 等），它提供了一种将整个 web 页嵌入到另一个网页的方法，看起来就像那个 web 页是另一个网页的一个 `<img>` 或其它元素一样。`<iframe>` 现在经常被使用。

#### Iframe 详解

`<iframe>` 元素旨在允许你将其他 Web 文档嵌入到当前文档中。这很适合将第三方内容嵌入你的网站，你可能无法直接控制，也不希望实现自己的版本——例如来自在线视频提供商的视频，Disqus 等评论系统，在线地图提供商，广告横幅等。你通过本课程使用的实时可编辑示例就是使用 `<iframe>` 实现的。

我们会在后面提到，关于 `<iframe>` 有一些严重的[安全隐患](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Multimedia_and_embedding/Other_embedding_technologies#安全隐患)需要考虑，但这并不意味着你不应该在你的网站上使用它们——它只需要一些知识和仔细地思考。让我们更详细地探索这些代码。假设你想在其中一个网页上加入 MDN 词汇表，你可以尝试以下方式：

```html
<iframe src="https://developer.mozilla.org/zh-CN/docs/Glossary"
        width="100%" height="500" frameborder="0"
        allowfullscreen sandbox>
  <p> <a href="https://developer.mozilla.org/zh-CN/docs/Glossary">
    Fallback link for browsers that don't support iframes
  </a> </p>
</iframe>
```

此示例包括使用以下所需的 `<iframe>` 基本要素：

`allowfullscreen`

- 如果设置，`<iframe>`则可以通过[全屏 API](https://developer.mozilla.org/zh-CN/docs/Web/API/Fullscreen_API) 设置为全屏模式（稍微超出本文的范围）。

`frameborder`

- 如果设置为 1，则会告诉浏览器在此框架和其他框架之间绘制边框，这是默认行为。0 删除边框。不推荐这样设置，因为在 [CSS 中](https://developer.mozilla.org/zh-CN/docs/Glossary/CSS)可以更好地实现相同的效果。[`border`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border)`: none;`

`src`

- 该属性与 `<video>` / 元素表示文档中的图像。`<img>`一样包含指向要嵌入文档的 URL 路径。

`width 和 height`

- 这些属性指定你想要的 iframe 的宽度和高度。

备选内容

- 与 `<video>` 等其它类似元素相同，你可以在 `<iframe></iframe>` 标签之间包含备选内容，如果浏览器不支持 `<iframe>`，将会显示备选内容，这种情况下，我们已经添加了一个到该页面的链接。现在你几乎不可能遇到任何不支持 `<iframe>` 的浏览器。

`sandbox`

- 该属性需要在已经支持其它 `<iframe>` 功能（例如 IE 10 及更高版本）但稍微更现代的浏览器上才能工作，该属性可以提高安全性设置；我们将在下一节中更加详细地谈到。

> **备注：** 为了提高速度，在主内容完成加载后，使用 JavaScript 设置 iframe 的 `src` 属性是个好主意。这使你的页面可以更快地被使用，并减少你的官方页面加载时间（重要的 [SEO](https://developer.mozilla.org/zh-CN/docs/Glossary/SEO) 指标）。

#### 安全隐患

浏览器制造商和 Web 开发人员了解到网络上的坏人（通常被称为**黑客**，或更准确地说是**破解者**），如果他们试图恶意修改你的网页或欺骗人们进行不想做的事情时常把 iframe 作为共同的攻击目标（官方术语：**攻击向量**），例如显示用户名和密码等敏感信息。因此，规范工程师和浏览器开发人员已经开发了各种安全机制，使`<iframe>`更加安全，这有些最佳方案值得我们考虑 - 我们将在下面介绍其中的一些。

> **备注：** [单击劫持](https://en.wikipedia.org/wiki/Clickjacking)是一种常见的 iframe 攻击，黑客将隐藏的 iframe 嵌入到你的文档中（或将你的文档嵌入到他们自己的恶意网站），并使用它来捕获用户的交互。这是误导用户或窃取敏感数据的常见方式。

一个快速的例子——尝试在浏览器中加载上面的例子）。你将不会看到任何内容，但如果你点击浏览器开发者工具中的控制台，你会看到一条消息，告诉你为什么没有显示内容。在 Firefox 中，你会被告知：`X-Frame-Options `拒绝加载 `https://developer.mozilla.org/zh-CN/docs/Glossary`。

![image-20221116162952170](image-20221116162952170.png)

这是因为构建 MDN 的开发人员已经在网站页面的服务器上设置了一个不允许被嵌入到`<iframe>`的设置。请参阅[配置 CSP 指令](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Multimedia_and_embedding/Other_embedding_technologies#配置_csp_指令)）这是有必要的——整个 MDN 页面被嵌入在其它页面中没有多大意义，除非你想要将其嵌入到你的网站上并将其声称为自己的内容，或尝试通过单击劫持来窃取数据，这都是非常糟糕的事情。此外，如果每个人都这样做，所有额外的带宽将花费 Mozilla 很多资金。

##### 使用 HTTPS 

[HTTPS](https://developer.mozilla.org/zh-CN/docs/Glossary/https) 是 [HTTP](https://developer.mozilla.org/zh-CN/docs/Glossary/HTTP) 的加密版本。你应该尽可能使用 HTTPS 为你的网站提供服务：

1. HTTPS 减少了远程内容在传输过程中被篡改的机会，
2. HTTPS 防止嵌入式内容访问你的父文档中的内容，反之亦然。

使用 HTTPS 需要一个安全证书，这可能是昂贵的（尽管 [Let's Encrypt](https://letsencrypt.org/) 让这件事变得更容易），如果你没有，可以使用 HTTP 来为你的父文档提供服务。但是，由于 HTTPS 的第二个好处，*无论成本如何，你绝对不能使用 HTTP 嵌入第三方内容*（在最好的情况下，你的用户的 Web 浏览器会给他们一个可怕的警告）。所有有声望的公司，例如 Google Maps 或 Youtube，当你嵌入内容时，`<iframe>`将通过 HTTPS 提供 - 查看`<iframe>` `src`属性内的 URL。

##### 始终使用 sandbox 属性

想尽可能减少攻击者在你的网站上做坏事的机会，那么你应该给嵌入的内容仅能完成自己工作的权限。当然，这也适用于你自己的内容。一个允许包含在其里的代码以适当的方式执行或者用于测试，但不能对其他代码库（意外或恶意）造成任何损害的容器称为[沙盒](https://en.wikipedia.org/wiki/Sandbox_(computer_security))。

未沙盒化（Unsandboxed）内容可以做得太多（执行 JavaScript，提交表单，弹出窗口等）默认情况下，你应该使用没有参数的 `sandbox` 属性来强制执行所有可用的限制，如我们前面的示例所示。

如果绝对需要，你可以逐个添加权限（`sandbox=""`属性值内）——请参阅 [`sandbox`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/iframe#attr-sandbox) 所有可用选项的参考条目。其中重要的一点是，你*永远不*应该同时添加`allow-scripts`和`allow-same-origin`到你的`sandbox`属性中——在这种情况下，嵌入式内容可以绕过阻止站点执行脚本的同源安全策略，并使用 JavaScript 完全关闭沙盒。

##### 配置 CSP 指令

[CSP](https://developer.mozilla.org/zh-CN/docs/Glossary/CSP)代表**[内容安全策略](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)**，它提供[一组 HTTP 标头 ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)（由 web 服务器发送时与元数据一起发送的元数据），旨在提高 HTML 文档的安全性。

在`<iframe>`的安全性方面，你可以*[将服务器配置为发送适当的`X-Frame-Options` 标题。](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/X-Frame-Options)*这样做可以防止其他网站在其网页中嵌入你的内容（这将导致[点击](https://en.wikipedia.org/wiki/clickjacking)和一系列其他攻击），正如我们之前看到的那样，MDN 开发人员已经做了这些工作。

#### `<embed>` 和 `<object>` 元素

`<embed>`和`<object>`元素的功能不同于`<iframe>`—— 这些元素是用来嵌入多种类型的外部内容的通用嵌入工具，其中包括像 Java 小程序和 Flash，PDF（可在浏览器中显示为一个 PDF 插件）这样的插件技术，甚至像视频，SVG 和图像的内容！

> **备注：** **插件**是一种对浏览器原生无法读取的内容提供访问权限的软件。

然而，你不太可能使用这些元素——Applet 几年来一直没有被使用；由于许多原因，Flash 不再受欢迎（见下面的[插件案例](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Multimedia_and_embedding/Other_embedding_technologies#针对插件的情况)）；PDF 更倾向于被链接而不是被嵌入；其他内容，如图像和视频都有更优秀、更容易元素来处理。插件和这些嵌入方法真的是一种传统技术，我们提及它们主要是为了以防你在某些情况下遇到问题，比如内部网或企业项目等。

### 在网页中添加矢量图形

矢量图形在很多情况下非常有用 — 它们拥有较小的文件尺寸，却高度可缩放，所以它们不会在镜头拉近或者放大图像时像素化。在这篇文章中，我们将为您呈现如何在网页中添加矢量图形。

> **备注：** 本文的目的并不是教你 SVG；仅仅是告诉你它是什么，以及如何在网页中添加它。

#### 什么是矢量图形？

在网上，你会和两种类型的图片打交道 — 位图和矢量图：

- 位图使用像素网格来定义 — 一个位图文件精确得包含了每个像素的位置和它的色彩信息。流行的位图格式包括 Bitmap (`.bmp`), PNG (`.png`), JPEG (`.jpg`), and GIF (`.gif`.)
- 矢量图使用算法来定义 — 一个矢量图文件包含了图形和路径的定义，电脑可以根据这些定义计算出当它们在屏幕上渲染时应该呈现的样子。 [SVG](https://developer.mozilla.org/zh-CN/docs/Glossary/SVG) 格式可以让我们创造用于 Web 的精彩的矢量图形。

此外，矢量图形相较于同样的位图，通常拥有更小的体积，因为它们仅需储存少量的算法，而不是逐个储存每个像素的信息。

#### SVG 是什么？

`SVG` 是用于描述矢量图像的`XML`语言。它基本上是像 `HTML` 一样的标记，只是你有许多不同的元素来定义要显示在图像中的形状，以及要应用于这些形状的效果。`SVG` 用于标记图形，而不是内容。非常简单，你有一些元素来创建简单图形，如`<circle>` 和`<rect>`。更高级的 SVG 功能包括 `<feColorMatrix>`（使用变换矩阵转换颜色）`<animate>` （矢量图形的动画部分）和 `<mask>`（在图像顶部应用模板）

作为一个简单的例子，以下代码创建一个圆和一个矩形：

```html
<svg version="1.1"
     baseProfile="full"
     width="300" height="200"
     xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="black" />
  <circle cx="150" cy="100" r="90" fill="blue" />
</svg>
```

![image-20221116164145241](image-20221116164145241.png)

从上面的例子可以看出，SVG 很容易手工编码。是的，您可以在文本编辑器中手动编写简单的 SVG，但是对于复杂的图像，这很快就开始变得非常困难。为了创建 SVG 图像，大多数人使用矢量图形编辑器，如 [Inkscape](https://inkscape.org/en/) 或 [Illustrator](https://en.wikipedia.org/wiki/Adobe_Illustrator)。这些软件包允许您使用各种图形工具创建各种插图，并创建照片的近似值（例如 Inkscape 的跟踪位图功能）。

SVG 除了迄今为止所描述的以外还有其他优点：

- 矢量图像中的文本仍然可访问（这也有利于 [SEO](https://developer.mozilla.org/zh-CN/docs/Glossary/SEO)）。
- SVG 可以很好地适应样式/脚本，因为图像的每个组件都是可以通过 CSS 或通过 JavaScript 编写的样式的元素。

那么为什么会有人想使用光栅图形而不是 SVG？其实 SVG 确实有一些缺点：

- SVG 非常容易变得复杂，这意味着文件大小会增加; 复杂的 SVG 也会在浏览器中占用很长的处理时间。
- SVG 可能比栅格图像更难创建，具体取决于您尝试创建哪种图像。
- 旧版浏览器不支持 SVG，因此如果您需要在网站上支持旧版本的 IE，则可能不适合（SVG 从 IE9 开始得到支持）。

由于上述原因，光栅图形更适合照片那样复杂精密的图像

#### 将 SVG 添加到页面

在本节中，我们将介绍将 SVG 矢量图形添加到网页的不同方式。

##### 快捷方式：`<img>`

要通过 `<img>`元素嵌入 SVG，你只需要按照预期的方式在 src 属性中引用它。你将需要一个height或width属性（或者如果您的 SVG 没有固有的宽高比）。

```html
<img
    src="equilateral.svg"
    alt="triangle with all three sides equal"
    height="87px"
    width="100px" />
```

**优点**

- 快速，熟悉的图像语法与`alt`属性中提供的内置文本等效。
- 可以通过在[`<a>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a)元素嵌套`<img>`，使图像轻松地成为超链接。

缺点

- 无法使用 JavaScript 操作图像。
- 如果要使用 CSS 控制 SVG 内容，则必须在 SVG 代码中包含内联 CSS 样式。 （从 SVG 文件调用的外部样式表不起作用）
- 不能用 CSS 伪类来重设图像样式（如`:focus`）。



对于不支持 SVG（IE 8 及更低版本，Android 2.3 及更低版本）的浏览器，您可以从`src`属性引用 PNG 或 JPG，并使用[`srcset`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img#attr-srcset)属性 只有最近的浏览器才能识别）来引用 SVG。在这种情况下，仅支持浏览器将加载 SVG - 较旧的浏览器将加载 PNG：

```html
<img src="equilateral.png" alt="triangle with equal sides" srcset="equilateral.svg">
```

您还可以使用 SVG 作为 CSS 背景图像，如下所示。在下面的代码中，旧版浏览器会坚持他们理解的 PNG，而较新的浏览器将加载 SVG：

```css
background: url("fallback.png") no-repeat center;
background-image: url("image.svg");
background-size: contain;
```

像上面描述的`<img>`方法一样，使用 CSS 背景图像插入 SVG 意味着它不能被 JavaScript 操作，并且也受到相同的 CSS 限制。

如果 SVG 根本没有显示，可能是因为你的服务器设置不正确。如果是这个问题，[这篇文章](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Tutorial/Getting_Started#a_word_on_webservers)将告诉你正确方向。

##### HTML 中引入 SVG 代码

你还可以在文本编辑器中打开 SVG 文件，复制 SVG 代码，并将其粘贴到 HTML 文档中 - 这有时称为将**SVG 内联**或**内联 SVG**。确保您的 SVG 代码在[``](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Element/svg)标签中（不要在外面添加任何内容）。这是一个非常简单的示例，您可以粘贴到文档中：

```html
<svg width="300" height="200">
    <rect width="100%" height="100%" fill="green" />
</svg>
```

**优点**

- 将 SVG 内联减少 HTTP 请求，可以减少加载时间。
- 您可以为 SVG 元素分配`class`和`id`，并使用 CSS 修改样式，无论是在 SVG 中，还是 HTML 文档中的 CSS 样式规则。实际上，您可以使用任何 [SVG 外观属性](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Attribute#presentation_attributes) 作为 CSS 属性。
- 内联 SVG 是唯一可以让您在 SVG 图像上使用 CSS 交互（如`:focus`）和 CSS 动画的方法（即使在常规样式表中）。
- 您可以通过将 SVG 标记包在[`<a>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a)元素中，使其成为超链接。

**缺点**

- 这种方法只适用于在一个地方使用的 SVG。多次使用会导致资源密集型维护（resource-intensive maintenance）。
- 额外的 SVG 代码会增加 HTML 文件的大小。
- 浏览器不能像缓存普通图片一样缓存内联 SVG。
- 您可能会在[`<foreignObject>`](https://developer.mozilla.org/zh-CN/docs/Web/SVG/Element/foreignObject) 元素中包含回退，但支持 SVG 的浏览器仍然会下载任何后备图像。你需要考虑仅仅为支持过时的浏览器，而增加额外开销是否真的值得。

##### 使用 `<iframe>` 嵌入 SVG

您可以在浏览器中打开 SVG 图像，就像网页一样。

```html
<iframe src="triangle.svg" width="500" height="500" sandbox>
    <img src="triangle.png" alt="Triangle with three unequal sides" />
</iframe>
```

这绝对不是最好的方法：

#### 缺点

- 如你所知， `iframe`有一个回退机制，如果浏览器不支持`iframe`，则只会显示回退。
- 此外，除非 SVG 和您当前的网页具有相同的 [origin](https://developer.mozilla.org/zh-CN/docs/Glossary/Origin)，否则你不能在主页面上使用 JavaScript 来操纵 SVG。

## `HTML`表格

### 什么是表格

表格是由行和列组成的结构化数据集（表格数据），它让你快速简单地查找某个表示不同类型数据之间的某种关系的值。比如说，某个人和他的年龄，一天或是一周，当地游泳池的时间表。

1.每一个表格的内容都包含在这两个标签中：`<table`>`</table>`。在你的 HTML 的 `<body>` 中添加这些内容。

2.在表格中，最小的内容容器是单元格，是通过 `<td>` 元素创建的（其中“td”代表“table data”）。把下面的内容添加到你的表格标签中：

```html
<td>Hi, I'm your first cell.</td>
```

3.如果我们想要一行四个单元格，我们需要把这组标签拷贝三次，更新你表中的内容，让它看起来是这样的：

```html
<td>Hi, I'm your first cell.</td>
<td>I'm your second cell.</td>
<td>I'm your third cell.</td>
<td>I'm your fourth cell.</td>
```

你会看到，单元格不会放置在彼此的下方，而是自动与同一行上的其他单元格对齐。每个 `<td>` 元素 创建一个单独单元格，它们共同组成了第一行。我们添加的每个单元格都使行的长度变长。

![image-20221116170116672](image-20221116170116672.png)

如果想让这一行停止增加，并让单元格从第二行开始，我们需要使用` <tr>` 元素（其中“tr”代表“table row”）。让我们现在来证实一下。

1.把你已经创建好的 4 个单元格放入 `<tr>` 标签，就像这样：

```html
<tr>
  <td>Hi, I'm your first cell.</td>
  <td>I'm your second cell.</td>
  <td>I'm your third cell.</td>
  <td>I'm your fourth cell.</td>
</tr>
```

2.现在你已经实现了一行，可以继续增加至两行、三行。每一行都需要一个额外的 `<tr>` 元素来包装，每个单元格的内容都应该写在 `<td>`中。

```html
<tr>
  <td>Hi, I'm your first cell.</td>
  <td>I'm your second cell.</td>
  <td>I'm your third cell.</td>
  <td>I'm your fourth cell.</td>
</tr>
<tr>
  <td>Hi, I'm your fifth cell.</td>
  <td>I'm your sixth cell.</td>
</tr>
```

![image-20221116170304369](image-20221116170304369.png)

### 使用 `<th>` 元素添加标题

现在，让我们把注意力转向表格标题，表格中的标题是特殊的单元格，通常在行或列的开始处，定义行或列包含的数据类型（举个例子，看到本篇文章中第一个示例中的 "单数" 或者 "Object"）。为了说明它们为什么这么有用，来看下面这个例子，首先是源代码：

```html
<table>
  <tr>
    <td>&nbsp;</td>
    <td>Knocky</td>
    <td>Flor</td>
    <td>Ella</td>
    <td>Juan</td>
  </tr>
  <tr>
    <td>Breed</td>
    <td>Jack Russell</td>
    <td>Poodle</td>
    <td>Streetdog</td>
    <td>Cocker Spaniel</td>
  </tr>
  <tr>
    <td>Age</td>
    <td>16</td>
    <td>9</td>
    <td>10</td>
    <td>5</td>
  </tr>
  <tr>
    <td>Owner</td>
    <td>Mother-in-law</td>
    <td>Me</td>
    <td>Me</td>
    <td>Sister-in-law</td>
  </tr>
  <tr>
    <td>Eating Habits</td>
    <td>Eats everyone's leftovers</td>
    <td>Nibbles at food</td>
    <td>Hearty eater</td>
    <td>Will eat till he explodes</td>
  </tr>
</table>

```

![image-20221116170524950](image-20221116170524950.png)

这里的问题是：虽然你可以弄清楚发生了什么，但是尽可能的交叉参考数据并不容易。如果列和行的标题以某种方式出现，那将会更好。

1.为了将表格的标题在视觉上和语义上都能被识别为标题，你可以使用 `<th>` 元素（其中 'th' 代表 'table header'），用法和 `<td>`是一样的，除了它表示为标题，不是普通的单元格以外。进入你的 HTML 文件，将表格中应该是标题的 `<td>` 元素标记的内容，都改为用 `<th>` 元素标记。

```html
<table>
  <tr>
    <th>&nbsp;</th>
    <th>Knocky</th>
    <th>Flor</th>
    <th>Ella</th>
    <th>Juan</th>
  </tr>
  <tr>
    <th>Breed</th>
    <td>Jack Russell</td>
    <td>Poodle</td>
    <td>Streetdog</td>
    <td>Cocker Spaniel</td>
  </tr>
  <tr>
    <th>Age</th>
    <td>16</td>
    <td>9</td>
    <td>10</td>
    <td>5</td>
  </tr>
  <tr>
    <th>Owner</th>
    <td>Mother-in-law</td>
    <td>Me</td>
    <td>Me</td>
    <td>Sister-in-law</td>
  </tr>
  <tr>
    <th>Eating Habits</th>
    <td>Eats everyone's leftovers</td>
    <td>Nibbles at food</td>
    <td>Hearty eater</td>
    <td>Will eat till he explodes</td>
  </tr>
</table>

```

![image-20221116170940283](image-20221116170940283.png)

当标题明显突出的时候，你可以更加简单地找到你想找的数据，设计上也会看起来更好。



表格标题也有额外的好处，随着 `scope` 属性 (我们将在下一篇文章中了解到)，这个属性允许你让表格变得更加无障碍，每个标题与相同行或列中的所有数据相关联。屏幕阅读设备能一次读出一列或一行的数据，这是非常有帮助的。

即使你不给表格添加你自己的样式，表格标题也会带有一些默认样式：加粗和居中，让标题可以突出显示。

### 允许单元格跨越多行和列

有时我们希望单元格跨越多行或多列。以下是一个简单的例子，显示了一些常见动物的名字。在某些情况下，我们要显示动物名称旁边的男性和女性的名字。有时候我们又不需要，那不需要的情况下，我们希望写着动物的名字的单元格的宽度可以是两个单元格的宽度 (因为写着名字的行会有两列，而没有写名字的行只有一列，行的宽度是不一样的)。

一开始的标记写法是这样的：

```html
<table>
  <tr>
    <th>Animals</th>
  </tr>
  <tr>
    <th>Hippopotamus</th>
  </tr>
  <tr>
    <th>Horse</th>
    <td>Mare</td>
  </tr>
  <tr>
    <td>Stallion</td>
  </tr>
  <tr>
    <th>Crocodile</th>
  </tr>
  <tr>
    <th>Chicken</th>
    <td>Hen</td>
  </tr>
  <tr>
    <td>Rooster</td>
  </tr>
</table>

```

但是输出的结果不是我们想要的：

![image-20221116200931939](image-20221116200931939.png)

我们需要一个方法，让 "Animals"、"Hippopotamus" 和 "Crocodile" 的单元格的宽度变为两个单元格， "Horse" 和 "Chicken" 的高度变为两行 (因为要拥有一个男性名字和女性名字，可以先看效果图)。幸好，表格中的标题和单元格有 `colspan` 和 `rowspan` 属性，这两个属性可以帮助我们实现这些效果。这两个属性接受一个没有单位的数字值，数字决定了它们的宽度或高度是几个单元格。比如，`colspan="2"` 使一个单元格的宽度是两个单元格。

1.使用 `colspan` 让 "Animals"、"Hippopotamus" 和 "Crocodile" 占 2 个单元格的宽度。

2.使用 `rowspan` 让 "Horse" 和 "Chicken" 占 2 个单元格的高度。

```html
    <table>
        <tr>
          <th colspan="2">Animals</th>
        </tr>
        <tr>
          <th colspan="2">Hippopotamus</th>
        </tr>
        <tr>
          <th rowspan="2">Horse</th>
          <td>Mare</td>
        </tr>
        <tr>
          <td>Stallion</td>
        </tr>
        <tr>
          <th colspan="2">Crocodile</th>
        </tr>
        <tr>
          <th rowspan="2">Chicken</th>
          <td>Hen</td>
        </tr>
        <tr>
          <td>Rooster</td>
        </tr>
      </table>
```

![image-20221116201240095](image-20221116201240095.png)

### 应用样式

在我们继续介绍之前，我们将介绍本文中的最后一个功能。HTML 有一种方法可以定义整列数据的样式信息：就是 和 元素。它们存在是因为如果你想让一列中的每个数据的样式都一样，那么你就要为每个数据都添加一个样式，这样的做法是令人厌烦和低效的。你通常需要在列中的每个 `<td>` 或 `<th>` 上定义样式，或者使用一个复杂的选择器，比如 [`:nth-child()` (en-US)](https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-child)。

这样不太理想，因为我们不得不在列中的每个单元格中重复那些样式信息（在真实的项目中，我们或许会设置一个 `class` 包含那三个单元格，然后在一个单独的样式表中定义样式）。为了舍弃这种做法，我们可以只定义一次，在 `<col>` 元素中。`<col>` 元素被规定包含在 `<colgroup>` 容器中，而 `<colgroup>`就在 `<table>` 标签的下方。我们可以通过如下的做法来创建与上面相同的效果：

```html
<table>
  <colgroup>
    <col>
    <col style="background-color: yellow">
  </colgroup>
  <tr>
    <th>Data 1</th>
    <th>Data 2</th>
  </tr>
  <tr>
    <td>Calcutta</td>
    <td>Orange</td>
  </tr>
  <tr>
    <td>Robots</td>
    <td>Jazz</td>
  </tr>
</table>

```

![image-20221116201447676](image-20221116201447676.png)

我们使用了两个 `<col>` 来定义“列的样式”，每一个 `<col>` 都会指定每列的样式，对于第一列，我们没有采取任何样式，但是我们仍然需要添加一个空的 `<col>` 元素，如果不这样做，那么我们的样式就会应用到第一列上，这和我们预想的不一样。

如果你想把这种样式信息应用到每一列，我们可以只使用一个 `<col>` 元素，不过需要包含 span 属性，像这样：

```html
<colgroup>
  <col style="background-color: yellow" span="2">
</colgroup>

```

就像 `colspan` 和 `rowspan` 一样，`span` 需要一个无单位的数字值，用来指定让这个样式应用到表格中多少列。

### 高级表格特性

#### 增加标题

你可以为你的表格增加一个标题，通过 `<caption>` 元素，再把 `<caption>` 元素放入 `<table>` 元素中。你应该把它放在`<table>` 标签的下面。

```html
<table>
  <caption>Dinosaurs in the Jurassic period</caption>

  ...
</table>

```

#### 添加 `<thead>`, `<tfoot>`, 和 `<tbody>` 结构

由于你的表格在结构上有点复杂，如果把它们定义得更加结构化，那会帮助我们更能了解结构。一个明确的方法是使用 `<thead>`, `<tfoot>`,和 `<tbody>`, 这些元素允许你把表格中的部分标记为表头、页脚、正文部分。

- `<thead>` 需要嵌套在 table 元素中，放置在头部的位置，因为它通常代表第一行，第一行中往往都是每列的标题，但是不是每种情况都是这样的。如果你使用了 / 元素，那么 `<thead>`元素就需要放在它们的下面。
- `<tfoot>` 需要嵌套在 table 元素中，放置在底部 (页脚) 的位置，一般是最后一行，往往是对前面所有行的总结，比如，你可以按照预想的方式将`<tfoot>`放在表格的底部，或者就放在 `<thead>` 的下面。(浏览器仍将它呈现在表格的底部)
- `<tbody>` 需要嵌套在 table 元素中，放置在 `<thead>`的下面或者是 `<tfoot>` 的下面，这取决于你如何设计你的结构。(`<tfoot>`放在`<thead>`下面也可以生效.)

## 面试题

### `HTML`中有哪些标签？

不要直接说标签，先进行分类

标签分为块级标签、行内标签、行内块标签

- 块级标签：[块级元素](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Block-level_elements)
  - 无语义化：
    - `div` 没有语义，就用来表示一个区块，是用来布局的元素
  - 语义化：
    - 标题
      - `h1`到`h6`
    - 列表
      - 有序列表 `ol`
      - 无序列表 `ul`
      - 自定义列表 `dl`

        - `dt` 用来表示定义的内容
        - `dd` 用来对内容进行解释说明
    - 表单元素
      - `form`
    - 表格元素
      - `table`
    - `h5`中的
      - `header` 表示网页的头部
      - `main` 表示网页中的主体部分，一般只有一个
      - `footer` 表示网页的底部
      - `nav` 表示网页中的导航
      - `aside` 和主体相关的其他内容（侧边栏）
      - `article` 表示一个独立的文章
      - `section` 表示一个独立的区块，上面的标签都不能表示时，用section
    - `blockquote` 表示一个长引用
- 行内标签：[行内元素  ](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Inline_elements)
  - 无语义化
    - `span`
  - 语义化
    - `em` 表示语音语调的一个加重
    - `strong` 表示强调，重要内容
    - `q` 表示一个短引用
    - `i`表示斜体
    - 表单相关的元素
      - `input`输入框
      - `button`按钮
      - `textarea`文本域
      - `select`多选
      - `label`
    - 换行
      - `br`
- 行内块标签：
  - 图片元素
    - `img`
  - 音视频元素
    - `audio`
    - `video`

必须要烂熟于心，平时使用的时候，有意识的记忆

如果想把一个页面的结构做好了，想拿到一个页面时脑子里瞬间就能知道应该怎么搭建结构，一定要牢牢的记住这些标签，向报菜名那样熟练

拿到页面会分析结构，第一步画图（熟练了在脑子里画），图画好了，该用什么标签一目了然

如果连基本的标签有哪些，都记不扎实，别提做项目了，有哪些标签都整不不明白，怎么去做呢？复制粘贴？

所谓编程思想，所谓各种各样的思想，一定是基础知识非常扎实的情况下，把一件件事做好后，再去讨论的

#### 基本标签

- `em` 表示语音语调的一个加重
- `strong` 表示强调，重要内容
- `blockquote` 表示一个长引用
- `q` 表示一个短引用
- `br` 表示页面中的换行
- `div` 没有语义，就用来表示一个区块，是用来布局的元素
- `span` 没有语义

#### 结构语义化标签

- `header` 表示网页的头部
- `main` 表示网页中的主体部分，一般只有一个
- `footer` 表示网页的底部
- `nav` 表示网页中的导航
- `aside` 和主体相关的其他内容（侧边栏）
- `article` 表示一个独立的文章
- `section` 表示一个独立的区块，上面的标签都不能表示时，用section

#### `meta`标签

- `charset` 指定网页的字符集

- `name` 指定的数据的名称

- `content` 指定的数据的内容

- `keywords` 表示网站的关键字，可以同时指定多个关键字，用逗号隔开

  ```html
  <meta name="keyword" content="网上购物,网上商城">
  ```

- `description` 指定网站的描述，网站的描述会显示在搜索引擎的结果中

  ```html
  <meta name="description" content="京东JD.COM-专业的综合网上购物商城"
  ```

- `http-equiv` 页面重定向到另一个网站

  ```html
  <meta http-equiv="refresh" content="3;url=https://www.baidu.com"
  ```

#### 列表

- 有序列表 `ol`

- 无序列表 `ul`

- 自定义列表 `dl`

  - `dt` 用来表示定义的内容
  - `dd` 用来对内容进行解释说明

  ```html
  <dl>
      <dt>结构</dt>
      <dd>网页的结构</dd>
      <dd>网页的结构</dd>
  </dl>
  ```

列表之间可以互相嵌套

#### 图片标签

##### 图片的属性

`img`元素属于替换元素（块和行内元素之间，具有两种元素的特点）

- `src`：指定外部图片的路径（路径规则和超链一样的）
- `alt`：图片的描述，默认情况下不会显示，如果不写alt属性，则图片不会被搜索引擎识别
- `width`：图片的宽度（px）
- `height`：图片的高度（px）；宽度和高度如果只修改了一个，则另一个会等比缩放
  - 注意：一般在pc端，需要多大的图片就做多大的图，在移动端，一般会大图缩小

##### 图片的格式

- `jpeg(jpg)`
  - 支持的颜色比较丰富，不支持透明效果，不支持动图
  - 一般用来显示照片
- `gif`
  - 支持的颜色比较少，支持简单透明，支持动图
  - 颜色单一的图片，动图
- png
  - 支持的颜色丰富，支持复杂透明，不支持动图
  - 颜色丰富，复杂透明图片（专为网页而生）
- webp
  - 这种格式是谷歌新推出的专门用来表示网页中的图片的一种格式
  - 它具备其他图片格式的所有优点，而且文件还特别小
  - 缺点：兼容性不好
- base64
  - 将图片使用base64编码，这样可以将图片转换为字符，通过字符的形式来引入图片
  - vue中的loader相关的知识点中，可以根据指定大小来决定，图片是否为base64
  - 一般都是一些需要和网页一起加载的图片，才会使用base64

使用原则

- 效果一样，用文件小的
- 效果不一样，用效果好的

#### 超链接和路径

- ./ 表示当前文件所在的目录

- ../表示当前文件所在的上一级目录

- target 用来指定超链接打开的位置

  - _self 默认值，在当前页面打开超链接
  - _blank 在一个新的窗口中打开超链接

- 锚点

  ```html
  <a href="bottom">去底部</a>
  <p>paragraph</p>
  <a id="bottom" href="#">回到顶部</a>
  ```

- href 可以将超链接的href属性设置为#，这样点击超链接以后，页面不会发生跳转

- id 每一个标签都可以添加id属性，id属性就是元素的唯一标识，同一个页面中不能出现重复的id属性
  跳转到页面指定位置

#### 音视频标签

audio标签用来向页面引入一个外部的音频文件，默认不允许用户自己控制播放停止

- controls：是否允许用户控制播放

  ```html
  <audio src="./若草恵%20-%20想い,あふれて.mp3" controls></audio>
  ```

  加上`controls`才会在界面上显示

- autoplay：音频文件是否自动播放

- loop：音乐是否循环播放

  ```html
  <audio src="./若草恵%20-%20想い,あふれて.mp3" controls autoplay loop></audio>
  ```

除了通过src来指定外部文件的路径外，还可以通过source来指定文件

```html
<audio controls>	
    <!-- 对不起，您的浏览器不支持播放音频！请升级浏览器！ -->    
    <source src="./若草恵%20-%20想い,あふれて.mp3">    
    <source src="./若草恵%20-%20想い,あふれて.ogg">    
    <!-- 兼容IE8 -->    
    <embed src="./若草恵%20-%20想い,あふれて.mp3" type="video/mp3" width="300" height="100">
</audio>
```

使用video标签来向网页引入一个视频，使用方式和audio基本上是一致的

```html
<video controls>	
    <source src="./flower.webm">    
    <source src="./flower.mp4">    
    <embed src="./flower.mp4" type="video/mp4">
</video>
```

一般情况下，不会直接将音频视频放在本地服务器上的，可以用在云服务器上，或者放在视频网站上





## 其他



### 内联框架

用于向当前页面中引入一个其他页面

- src：指定要引入的路径
- frameborder：指定内联框架的边框（0：没有，1：有）

```html
<iframe src="https://www.qq.com" width="800" height="600" frameborder="1"></iframe>
```

# 响应式设计

## 基本概念

综合运用了三种已有技术（**弹性网格布局**、**弹性图片/媒体**、**媒体查询**）实现了一个解决方案，就叫“响应式Web设计”。

所谓响应式Web设计，就是网页内容会随着访问它的视口及设备的不同而呈现不同的样式

先为小屏幕设计内容、样式，然后再向大屏幕扩展。

能不能适配某个旧平台/版本不是问题，问题在于是否应该去适配它。

## 第一个响应式的例子

先从HTML5结构讲起

浏览器中用于呈现网页的区域叫视口（viewport）。视口通常并不等于屏幕大小，特别是可以 缩放浏览器窗口的情况下。

```html
<meta name="viewport" content="width=device-width">
```

它告诉浏览器怎么渲 染网页。在这里，`<meta>`标签想表达的意思是：按照设备的宽度（device-width）来渲染网 页内容。

# H5

[教程参考](https://www.runoob.com/html/html5-intro.html)

### Canvas绘图

#### Canvas - 文本

使用 canvas 绘制文本，重要的属性和方法如下：

- font - 定义字体
- fillText(text,x,y) - 在 canvas 上绘制实心的文本
- strokeText(text,x,y) - 在 canvas 上绘制空心的文本

#### Canvas - 渐变

- 线性渐变
- 径向渐变

### HTML5 内联 SVG

### HTML5 MathML

### HTML5 拖放（Drag 和 Drop）

### HTML5 Geolocation（地理定位）

### HTML5 Video(视频)

### HTML5 Audio(音频)

### HTML5 新的 Input 类型

### HTML5 表单元素

### HTML5 表单属性

### HTML5 语义元素

### HTML5 Web 存储

HTML5 web 存储,一个比cookie更好的本地存储方式。

### HTML5 Web SQL 数据库

### HTML5 Web Workers

### HTML5 服务器发送事件(Server-Sent Events)

### HTML5 WebSocket

### HTML(5) 代码规范



[视频教程来源]()



### attr&prop

在JS中打断点

JS原生对象的属性，称为property

每一个预定义的attribute都会有一个property与之对应

 非布尔值属性，property和attribute都会同步

布尔值属性，property和attribute的同步问题

- 1.改变property时，不会同步attribute
- 2.在没有动过property时
  - attribute会同步property

- 一旦动过property
  - attribute不会同步property

#### 什么是attribute，什么是property

html标签的预定义和自定义属性我们统称为attribute

js原生对象的直接属性，我们统称为property

#### 什么是布尔值属性，什么是非布尔值属性

property的属性值为布尔类型的，我们统称为布尔值属性

property的属性为非布尔类型的，我们统称为非布尔值属性

#### attribute和property的同步关系

非布尔值属性：实时同步

布尔值属性：

​	property永远都不会同步attribute

​	在没有动过property的情况下

​		attribute会同步property

​	在动过property的情况下

​		attribute不会同步property

#### 用户操作的是property

#### 浏览器认的是property

操作布尔值属性，推荐使用prop方法，操作非布尔值属性，推荐使用attr方法

### H5中的小功能

classList.add() 自定义添加class

classList.remove()自定义删除类

classList.toggle()



自定义属性

```javascript
<body>
    <div id="test" data-atguigu-qhf = 'qhf'>

    </div>
    <script>
        var testNode = document.querySelector("#test")
        console.log(testNode.dataset.atguiguQhf)
        // testNode.dataset.atguiguQhf='111'
        // testNode.dataset.atguiguQhf.add('222')
    </script>
</body>
```



contenteditable = 'true'

### H5和H4的区别

H5的优势

- 跨平台（浏览器）
- 快速迭代
- 降低成本
- 导流入口多
- 分发效率高



H5

1.DOCTYPE和浏览器渲染模式

### 语义化标签

### Canvas基本用法

#### 1.浏览器兼容

```javascript
<canvas id="myCanvas" width="300px" height="300px">
    <span>你的浏览器不支持画布元素，请下载谷歌浏览器</span>
</canvas>
```

#### 2.基本用法

```javascript
window.onload = function() {
    //querySelector身上有坑
    var testNode = document.querySelector("#myCanvas")
    if(testNode.getContext){
        var ctx = testNode.getContext("2d")
        }
}
```

#### 3.绘制矩形

1.绘制矩形

canvas提供了3中绘制矩形的方式：

- 绘制一个填充的矩形（填充默认为黑色）

  `fillRect(x,y,width,height)`

- 绘制一个矩形的边框（默认边框为：一像素实习黑色）

  `strokeRect(x,y,width,height)`

- 清除指定矩形区域，让清除部分完全透明

  `clearRect(x,y,width,height)`

x与y制定了canvas画布上所绘制的矩形的左上角（相对于原点）的坐标。

width和height设置矩形的尺寸。（存在边框会在width上占据一个边框的宽度，height同理）

2.strokeRect时，边框像素渲染问题

按理渲染出的边框应该是1px的，

canvas在渲染矩形边框时，边框宽度是平均分在偏移位置两侧。

- content.strokeRect(10,10,50,50)
  - 边框会渲染在10.5和9.5之间，浏览器是不会让一个像素只用自己的一半的
  - 相当于边框会渲染在9到11之间
- context.strokeRect(10.5,10.5,50,50).
  - 边框会渲染在10到11之间



