---
title: 'CSS核心基础'
date: 2022-8-9 07:28:42
cover: false
tags:
- CSS
categories: 'CSS'
typora-root-url: CSS核心
---



> 参阅MDN

# `CSS`第一步

## 什么是`CSS`

> 基于`HTML`，对`CSS`有一个概念性的认识
>
> `CSS`是一门基于规则的语言，通过各种规则，让浏览器将`HTML`元素渲染出自定义的样式

**[`CSS`](https://developer.mozilla.org/zh-CN/docs/Glossary/CSS)** (层叠样式表) 让你可以创建好看的网页，但是它具体是怎么工作的呢？ 这篇文章通过一些很简单的例子，告诉我们什么是 `CSS`，同时还会涉及一些和 `CSS` 相关的专业术语。



在 [HTML 概述](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Introduction_to_HTML) 模块我们学习了 HTML 是什么，以及如何使用它来组成页面。 

浏览器能够解析这些页面。标题部分看起来会比正常文本更大，段落则会另起一行，并且相互之间会有一定间隔。链接通过下划线和不同的颜色与其他文本区分开来。

这些都是浏览器的默认样式——当开发者没有指定样式时，浏览器通过这些最简单的样式使页面具有基本可读性。

![image-20220817093605799](image-20220817093605799.png)

如果所有网站都像上图那样，互联网就会非常枯燥。但是使用 `CSS` 就可以完全控制浏览器如何显示 `HTML` 元素，从而充分展示你喜欢的设计样式。

### `CSS`用来干什么

前文提到过，`CSS` 是用来指定文档如何展示给用户的一门语言——如网页的样式、布局、等等。

- `CSS` 可以用于给文档添加样式
  - 比如改变标题和链接的[颜色](https://developer.mozilla.org/zh-CN/docs/Web/CSS/color_value)及[大小](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-size)。

- 它也可用于创建布局 
  - 比如将一个单列文本变成包含主要内容区域和存放相关信息的侧边栏区域的[布局](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Layout_cookbook/Column_layouts)。
- 它甚至还可以用来做一些特效
  - 比如[动画](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Animations)。

### `CSS`基本语法

CSS 是一门基于规则的语言 —— 你能定义用于你的网页中特定元素样式的一组规则

比如“**我希望页面中的主标题是红色的大字**”，下面这段代码使用非常简单的 `CSS` 规则实现了这个效果：

```css
h1 {
    color: red;
    font-size: 5em;
}

```

- 语法由一个 [选择器 (selector)](https://developer.mozilla.org/zh-CN/docs/Glossary/CSS_Selector)起头。
  - 它 *选择 (selects)* 了我们将要用来添加样式的 HTML 元素。在这个例子中我们为一级标题（主标题[`h1`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements)）添加样式。

- 接着输入一对大括号`{ }`。

  - 在大括号内部定义一个或多个形式为 **属性 (`property`):值 (`value`);** 的 **声明 (`declarations`)**。
  - 每个声明都指定了我们所选择元素的一个属性，之后跟一个我们想赋给这个属性的值。

  - 冒号之前是属性，冒号之后是值。不同的 `CSS` [属性 (`properties`) ](https://developer.mozilla.org/en-US/docs/Glossary/property/CSS) 对应不同的合法值。
  - 在这个例子中，我们指定了 `color` 属性，它可以接受许多[颜色值](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Values_and_units#颜色)；还有 `font-size` 属性，它可以接收许多 [`size units`](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Values_and_units#数字，长度和百分比) 值。

### `CSS`包含哪些内容模块

`CSS`模块

你可以通过 CSS 为许多东西添加样式，CSS 由许多*模块 (modules)* 构成。你可以在 MDN 上浏览这些模块的参考内容 (MDN reference)，许多模块都被组织在自己单独的文档页面。例如，我想查找一下 MDN reference 的 [Backgrounds and Borders](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Backgrounds_and_Borders) 模块的相关内容，来了解它是用来做什么的、它还包括什么属性、它还有什么其它特性等。你也可以在 *CSS Specification* 查找（见下文），它定义了 CSS 规范。

在这个阶段你不必过于担心 CSS 是如何组织的 (how CSS is structured)，但是它能帮助你更好的掌握 CSS。例如，你注意到某个属性和另外一些属性的相似点，并且它们可能确实是相同的格式。

举个具体点的例子：如上文中的 Backgrounds and Borders 模块 — 你会发现 [`background-color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-color) 和 [`border-color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-color) 这两个属性在逻辑上相通。并且它也确实如此。



### `CSS`规范

所有的标准 `Web` 技术 (`HTML`, `CSS`,`JavaScript` 等) 都被定义在一个巨大的文档中，称作 规范 `specifications` (或者简称为 "`specs`")，它是由 (像是 [`W3C`](https://developer.mozilla.org/en-US/docs/Glossary/W3C), [`WHATWG`](https://developer.mozilla.org/zh-CN/docs/Glossary/WHATWG), [`ECMA`](https://developer.mozilla.org/zh-CN/docs/Glossary/ECMA) 或 [`Khronos`](https://developer.mozilla.org/en-US/docs/Glossary/Khronos)) 这些规范化组织所发布的，其中还定义了各种技术是如何工作的。

`CSS` 也不例外——它是由 `W3C`(万维网联盟) 中的一个名叫 [`CSS Working Group`](https://www.w3.org/Style/CSS/) 团体发展起来的。这个团体是由浏览器厂商和其他公司中对 `CSS` 感兴趣的人作为代表组成的。也有其他的人员，比如*受邀专家 (`invited experts`)*，他们作为不从属于任何组织的独立声音加入团体。

新的 `CSS` 特性被开发出来，或是因为某个浏览器热衷于开发新功能，或是因为 `Web` 设计人员与开发者要求增加一个新特性，又或是 `CSS Working Group` 内部的讨论决定。`CSS` 始终在发展，并伴随着新的特性。然而，有一件事情从始至终都未改变，那就是不让新的改变破坏旧的网站，即使是 2000 年建立的网站，如今也能正常访问！

作为一个 `CSS` 新手，你会发现阅读 `CSS` 规范 中的内容非常吃力——它旨在为工程师在用户代理 (`user agents`) 中实现对 `CSS` 各种特性的支持，而不是作为一本为 `Web` 开发者理解 `CSS` 内容的教程。即使是有经验的开发者，也更倾向于使用 `MDN` 文档或者其它教程。但是，知晓它的存在，理解 `CSS`、规范 和 浏览器支持（见下文）之间的关系是很有价值的。

### `CSS`浏览器支持

当一个浏览器支持 CSS 后，我们就可以用它来进行 Web 开发了。这意味着我们写在 CSS 文件中的代码可以被指令执行，展示到荧幕中。在 [CSS 如何工作](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/First_steps/How_CSS_works) 一节中我们会学习到更多的相关知识。但是让所有的浏览器都同时支持一个 CSS 新特性是不现实的，通常都会一个空档期——一些浏览器已经支持而另一些仍未支持。因此，查看特性的实现状态 (implementation status) 是非常有用的。在 MDN 上的每个属性的页面中都标有它们对应的状态，你可以通过这种方法来查看你是否可以去使用它。

以下是 CSS [`font-family`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-family) 属性的兼容数据表。

![image-20220817095353587](image-20220817095353587.png)

## `CSS`入门

> 本篇详细的讲解了，`CSS`中各种选择器
>
> 能够掌握各种选择器的写法，正确的利用`CSS`选择器拿到想要的`html`元素，就算是`CSS`入门了
>
> 至于能不能写出正确的样式，那是后面的事情



在这篇文章中，我们将会拿一个简单的 HTML 文档做例子，并且在里面使用 CSS 样式

### `CSS`入门案例

我们先以 HTML 文档展开叙述。如果想在自己电脑试一试，可以复制下面的代码。在你的电脑上，将代码以文件名： `index.html` 的形式保存下来。

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>开始学习 CSS</title>
</head>

<body>

    <h1>我是一级标题</h1>

    <p>这是一个段落文本。在文本中有一个 <span>span element</span>
并且还有一个 <a href="http://example.com">链接</a>.</p>

    <p>这是第二段。包含了一个 <em>强调</em> 元素.</p>

    <ul>
        <li>项目 1</li>
        <li>项目 2</li>
        <li>项目 <em>三</em></li>
    </ul>

</body>

</html>

```

我们最想做的就是让 HTML 文档能够遵守我们给它的 CSS 规则。其实有三种方式可以实现，而目前我们更倾向于利用最普遍且有用的方式——在文档的开头链接 CSS。

在与之前所说的 HTML 文档的相同目录创建一个文件，保存并命名为 `styles.css` 。（看后缀知道此文件就是 CSS 文件）

为了把 `styles.css` 和 `index.html` 连接起来，可以在 HTML 文档中，[`<head>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/head) 语句模块里面加上下面的代码：

```html
<link rel="stylesheet" href="styles.css">
```

[`<link>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/link) 语句块里面，我们用属性 `rel`，让浏览器知道有 CSS 文档存在（所以需要遵守 CSS 样式的规定），并利用属性 `href` 指定，寻找 CSS 文件的位置。 你可以做测试来验证 CSS 是否有效：在 `styles.css` 里面加上 CSS 样式并观察显示的结果。下面，用你的编辑器打出下面的代码。

```css
h1 {
  color: red;
}
```

保存 HTML 和 CSS 文档，刷新浏览器网页，不出意外你将看到网页顶层的大标题变成红色了。如果看到这个现象，恭喜你：你已经成功将某些 CSS 样式运用到 HTML 上了。当然假设没有达到预想结果，可以仔细检查每句代码是否正确，加油：）

![image-20220817100655784](image-20220817100655784.png)

### 样式化 `HTML` 元素

通过上一节将大标题变成红色的例子，我们已经展示了我们可以选中并且样式化 HTML 元素。我们通过触发元素选择器实现这一点——元素选择器，即直接匹配 HTML 元素的选择器。例如，若要样式化一个文档中所有的段落，只需使用选择器 `p`。若要将所有段落变成绿色，你可以利用如下方式：

```css
p {
  color: green;
}

```

![image-20220817103112888](image-20220817103112888.png)

用逗号将不同选择器隔开，即可一次使用多个选择器。譬如，若要将所有段落与列表变成绿色，只需：

```css
p, li {
    color: green;
}

```

![image-20220817103045587](image-20220817103045587.png)



### 改变元素的默认行为

只要一个 HTML 文档标记正确，即使像我们的例子那么简单，浏览器都会尽全力将其渲染至可读状态。标题默认使用大号粗体；列表旁总有项目符号。这是因为浏览器自带一个包含默认样式的样式表，默认对任何页面有效。没有了它们，所有文本会夹杂在一起变得一团糟，我们只得从头开始规定，好糟糕。话说回来，所有现代浏览器的默认样式都没什么差距。

不过你可能对浏览器的默认样式不太满意。没关系，只需选定那个元素，加一条 CSS 规则即可。就拿我们的无序列表 `<ul>`举个例子吧，它自带项目符号，不过要是你跟它有仇，你就可以这样移除它们：

```css
li {
  list-style-type: none;
}

```

把上述代码加到你的 CSS 里面试一试！

![image-20220817103419048](image-20220817103419048.png)

欢迎参阅 MDN 上的 `list-style-type` 属性，看看到底有哪些值被支持。 [`list-style-type`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/list-style-type) 页首提供互动性示例，您可以输入不同的值来瞅一瞅它们到底有什么用。关于每个值的详细描述都规规整整地列在下面。

通过参阅上述页面，你会发现你不仅能移除项目符号——你甚至能改变它们。赶快试试 `square`，它能把默认的小黑球变成方框框。

![image-20220817103448058](image-20220817103448058.png)

### 使用类名

目前为止，我们通过 HTML 元素名规定样式。如果你愿意所有元素都一个样，也不是不可以，但大多数情况下，我估计你都不愿意。我知道你想干啥，你想用这种方式样式化这一片元素，又想用那种方式样式化那一片元素，真贪心。不过没关系，你可以给 HTML 元素加个类名（class），再选中那个类名，这样就可以了，大家基本上都这么用。

举个例子吧，咱们把 [class 属性](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes/class)加到表里面第二个对象。你的列表看起来应该是这样的：

```html
<ul>
  <li>项目一</li>
  <li class="special">项目二</li>
  <li>项目 <em>三</em></li>
</ul>

```

在 CSS 中，要选中这个 `special` 类，只需在选择器的开头加个西文句点（.）。在你的 CSS 文档里加上如下代码：

```css
.special {
  color: orange;
  font-weight: bold;
}

```

保存再刷新，就可以看到变化。

![image-20220817103712140](image-20220817103712140.png)



这个 `special` 类型可不局限于列表，它可以应用到各种元素上。举个例子，你可能也想让段落里边的 `<span>` 一起又橙又粗起来。试试把`special` 类属性加上去，保存，刷新，哇，生活就是这么美好。

有时你会发现选择器中，HTML 元素选择器跟类一起出现：

```css
li.special {
  color: orange;
  font-weight: bold; 
}

```

这个意思是说，“选中每个 `special` 类的 `li` 元素”。你真要这样，好了，它对 `<span>` 还有其它元素不起作用了。你可以把这个元素再添上去就是了：

```css
li.special,
span.special {
  color: orange;
  font-weight: bold;
}

```

你们都是懒人，肯定不想每加一个 special 类的元素就改一遍 CSS 表，你肯定想把一个类的属性应用到多个元素上。所以说，有时还是别管元素，光看类就完事了，除非你意志坚定，坚持对这个类的某一种元素创造规则，还不让其它元素用。

### 根据元素在文档中的位置确定样式

有时候，您希望某些内容根据它在文档中的位置而有所不同。这里有很多选择器可以为您提供帮助，但现在我们只介绍几个选择器。在我们的文档中有两个 `<em>`元素 ——一个在段落内，另一个在列表项内。仅选择嵌套在`<li>` 元素内的`<em>`我们可以使用一个称为**包含选择符**的选择器，它只是单纯地在两个选择器之间加上一个空格。

将以下规则添加到样式表。

```css
li em {
  color: rebeccapurple;
}

```

该选择器将选择`<li>`内部的任何`<em>`元素（`<li>`的后代）。因此在示例文档中，您应该发现第三个列表项内的`<em>`现在是紫色，但是在段落内的那个没发生变化。

![image-20220817104239246](image-20220817104239246.png)

另一些可能想尝试的事情是在 HTML 文档中设置直接出现在标题后面并且与标题具有相同层级的段落样式，为此需在两个选择器之间添加一个 `+` 号 (成为 **相邻选择符**)

也将这个规则添加到样式表中：

```css
h1 + p {
  font-size: 200%;
}

```

下面的示例包含了上面的两个规则。

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>开始学习 CSS</title>
  <link rel="stylesheet" href="styles.css">
</head>

<body>

<h1>我是一级标题</h1>

<p>这是一个段落文本。在文本中有一个 <span>span element</span>
  并且还有一个 <a href="http://example.com">链接</a>.</p>

<p>这是第二段。包含了一个 <em>强调</em> 元素.</p>

<ul>
  <li>项目 <span>1</span></li>
  <li class="special">项目 2</li>
  <li>项目 <em>三</em></li>
</ul>

</body>

</html>

```



```css
li em {
    color: rebeccapurple;
}

h1 + p {
    font-size: 200%;
}
    
```

![image-20220817104957151](image-20220817104957151.png)

> **备注：** 如你所见，CSS 给我们提供了几种定位元素的方法。到目前为止，我们只触及了皮毛！我们将对这些选择器进行适当的研究，更多的内容将在我们后面的[选择器](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Selectors)章节中介绍。

### 根据状态确定样式

在这篇教程中我们最后要看的一种修改样式的方法就是根据标签的状态确定样式。一个直观的例子就是当我们修改链接的样式时。当我们修改一个链接的样式时我们需要定位（针对） [`<a>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a) （锚）标签。取决于是否是未访问的、访问过的、被鼠标悬停的、被键盘定位的，亦或是正在被点击当中的状态，这个标签有着不同的状态。你可以使用 CSS 去定位或者说针对这些不同的状态进行修饰——下面的 CSS 代码使得没有被访问的链接颜色变为粉色、访问过的链接变为绿色。

```css
a:link {
  color: pink;
}

a:visited {
  color: green;
}

```

你可以改变链接被鼠标悬停的时候的样式，例如移除下划线，下面的代码就实现了这个功能。

```css
a:hover {
  text-decoration: none;
}

```

![image-20220817105203486](image-20220817105203486.png)

我们对鼠标悬停于链接上的情况删除了下划线。你当然可以让超链接在任何情况下都没有下划线。但需要注意的是，对一个实际的站点，需要让浏览者知道“链接是链接”。为了让浏览者注意到一段文字中的某些部分是可点击的，最好保留 link 状态下的下划线。— 这是下划线的本来作用。不管你用 CSS 来做什么，都应当使得变化后的文档看上去更加清晰明了。— 在后面，当我们遇到类似的情况时，我们将适时指出。

> **备注：** 在本教程以及整个 MDN 站点中，你会经常看到“无障碍”这个词。“无障碍”一词的意思是，我们的网页应当让每一个访客都能够理解、使用。
>
> 你的访客可能在一台使用鼠标和键盘操作的计算机前，也可能正在使用带有触摸屏的手机，或者正在使用屏幕阅读软件读出文档内容，或者他们需要使用更大的字体，或者仅仅使用键盘浏览站点。
>
> 一个朴素的 HTML 文档一般来说对任何人都是可以无障碍访问的，当你开始为它添加样式，记得不要破坏这种可访问性。

### 同时使用选择器和选择符

你可以同时使用选择器和选择符。来看一些例子：

```css
/* selects any <span> that is inside a <p>, which is inside an <article>  */
article p span { ... }

/* selects any <p> that comes directly after a <ul>, which comes directly after an <h1>  */
h1 + ul + p { ... }

```

你可以将多种类型组合在一起。试试将下面的代码添加到你的代码里：

```css
body h1 + p .special {
  color: yellow;
  background-color: black;
  padding: 5px;
}

```

上面的代码为以下元素建立样式：在 `<body>` 之内，紧接在 `<h1>` 后面的 `<p>` 元素的内部，类名为 special。

在我们提供的原始 HTML 文档中，与之符合的元素只有`<span class="special">`.

如果你现在觉得这份代码太复杂了，别担心，一旦你开始编写更多的 CSS 代码，你很快就能找到窍门。

## `CSS`是如何构建的

> 本篇的介绍的与`CSS`有关若干概念

既然你已经了解了什么是 CSS，以及使用 CSS 的基础知识，是时候更深入的了解该语言本身的结构了。

我们已经见过了本页讨论的很多概念；如果在之后对某些概念感到困惑的话，可以返回至此进行回顾。

### `HTML`中引入`CSS`的三种方法

我们需要了解的第一件事情就是在文档中应用 CSS 的三种方法

#### 外部样式表

将外部样式表链接到页面，这是将 CSS 附加到文档中的最常见和最有用的方法，因为您可以将 CSS 链接到多个页面，从而允许您使用相同的样式表设置所有页面的样式。在大多数情况下，一个站点的不同页面看起来几乎都是一样的，因此您可以使用相同的规则集来获得基本的外观。

外部样式表是指将 CSS 编写在扩展名为`.css` 的单独文件中，并从 HTML `<link>` 元素引用它的情况：

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My CSS experiment</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <h1>Hello World!</h1>
    <p>This is my first CSS example</p>
  </body>
</html>

```

CSS 文件可能如下所示：

```css
h1 {
  color: blue;
  background-color: yellow;
  border: 1px solid black;
}

p {
  color: red;
}

```

[`link`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/link) 元素的 `href` 属性需要引用你的文件系统中的一个文件。

在上面的例子中，CSS 文件和 HTML 文档在同一个文件夹中，但是你可以把 CSS 文件放在其他地方，并调整指定的路径以匹配，例如：

```html
<!-- Inside a subdirectory called styles inside the current directory -->
<link rel="stylesheet" href="styles/style.css">

<!-- Inside a subdirectory called general, which is in a subdirectory called styles, inside the current directory -->
<link rel="stylesheet" href="styles/general/style.css">

<!-- Go up one directory level, then inside a subdirectory called styles -->
<link rel="stylesheet" href="../styles/style.css">

```

#### 内部样式表

内部样式表是指不使用外部 CSS 文件，而是将 CSS 放在 HTML 文件[`head`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/head)标签里的[`style`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/style)标签之中。

于是 HTML 看起来就像下面这个样子：

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My CSS experiment</title>
    <style>
      h1 {
        color: blue;
        background-color: yellow;
        border: 1px solid black;
      }

      p {
        color: red;
      }
    </style>
  </head>
  <body>
    <h1>Hello World!</h1>
    <p>This is my first CSS example</p>
  </body>
</html>

```

有的时候，这种方法会比较有用（比如你使用的内容管理系统不能直接编辑 CSS 文件)，但该方法和外部样式表比起来更加低效 。在一个站点里，你不得不在每个页面里重复添加相同的 CSS，并且在需要更改 CSS 时修改每个页面文件。

#### 内联样式

内联样式表存在于 HTML 元素的 style 属性之中。其特点是每个 CSS 表只影响一个元素：

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My CSS experiment</title>
  </head>
  <body>
    <h1 style="color: blue;background-color: yellow;border: 1px solid black;">Hello World!</h1>
    <p style="color:red;">This is my first CSS example</p>
  </body>
</html>

```

![image-20220818090227023](image-20220818090227023.png)

**除非你有充足的理由，否则不要这样做！** 它难以维护（在需要更新时，你必须在修改同一个文档的多处地方），并且这种写法将文档结构和文档表现混合起来了，这使得代码变得难以阅读和理解。将不同类型的代码分开存放在不同的文档中，会让我们的工作更加清晰。

在某些地方，内联样式更常见，甚至更可取。如果您的工作环境确实很严格（也许网站管理系统 (CMS) 仅允许您编辑 HTML 正文），则可能不得不使用它们。您也会发现它们很长时间被应用在 HTML 电子邮件中，以便与尽可能多的电子邮件客户端兼容。

### 选择器

讲到 CSS 就不得不说到选择器，并且在之前的辅导教程中我们已经列举了一些不同的选择器。为了样式化某些元素，我们会通过选择器来选中 HTML 文档中的这些元素。如果你的样式没有生效，那很可能是你的选择器没有像你想象的那样选中你想要的元素。

每个 CSS 规则都以一个选择器或一组选择器为开始，去告诉浏览器这些规则应该应用到哪些元素上。以下都是有效的选择器或组合选择器的示例。

```css
h1
a:link
.manythings
#onething
*
.box p
.box p:first-child
h1, h2, .intro

```

### 专一性

通常情况下，两个选择器可以选择相同的 HTML 元素。考虑下面的样式表，其中我有一个规则，其中有一个将段落设置为蓝色的 p 选择器，还有一个将选定元素设置为红色的类。

```css
.special {
  color: red;
}

p {
  color: blue;
}

```

比方说，在我们的 HTML 文档中，我们有一个带有特殊类的段落。这两条规则都适用，那么谁赢了？你认为我们的段落会变成什么颜色？

```html
<p class="special">What color am I?</p>

```

CSS 语言有规则来控制在发生碰撞时哪条规则将获胜——这些规则称为级联规则和专用规则。在下面的代码块中，我们为 p 选择器定义了两个规则，但是段落最后是蓝色的。这是因为将其设置为蓝色的声明将出现在样式表的后面，而稍后的样式将覆盖以前的样式。这就是起作用的级联。

```css
p {
  color: red;
}

p {
  color: blue;
}

```

但是，在我们同时使用了类选择器和元素选择器的前一个例子中，类将获胜，使得段落变红——即使它出现在样式表的前面。一个类被描述为比元素选择器更具体，或者具有更多的特异性，所以它获胜了。

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>My CSS experiment</title>
  <style>
      .special {
          color: red;
      }

      p {
          color: blue;
      }

  </style>
</head>
<body>
<p class="special">What color am I?</p>
</body>
</html>

```

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My CSS experiment</title>
  </head>
  <body>
    <p class="special">What color am I?</p>
  </body>
</html>




自己试试上面的实验——将 HTML 添加到您的实验中，然后将两个 `p{.}` 规则添加到样式表中。接下来，将第一个 `p` 选择器更改为 `.special`，以查看它如何更改样式。

一开始，具体性和层叠的规则看起来有点复杂，一旦你积累了更多的 CSS 知识，就更容易理解了。在我们的级联和继承文章 (将在下一个模块中讨论) 中，我将详细解释这一点，包括如何计算专用性。现在，请记住这是存在的，有时 CSS 可能不会像您预期的那样应用，因为样式表中的其他内容具有更高的特异性。确定一个元素可以适用不止一个规则是解决这些问题的第一步

### 属性和值

在最基本的层面上，CSS 由两个组成部分组成：

- **属性：** 人类可读的标识符，指示您想要更改的样式特征 (例如[`font-size`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-size)、[`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width)、[`background-color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-color))。
- **值：** 每个指定的属性都有一个值，该值指示您希望如何更改这些样式特性 (例如，要将字体、宽度或背景色更改为。)

下面的图像突出显示单个属性和值。属性名为 `color`, 值为 `blue`.

![A declaration highlighted in the CSS](declaration.png)

与值配对的属性称为 CSS 声明。CSS 声明放在 CSS 声明块中。下一张图片显示了我们的 CSS，并突出显示了声明块。

![A highlighted declaration block](declaration-block.png)

最后，CSS 声明块与选择器配对，以生成 CSS 规则集 (或 CSS 规则)。我们的图像包含两个规则，一个用于 `h1` 选择器，另一个用于 `p` 选择器。`h1` 的规则被突出显示。

![The rule for h1 highlighted](rules.png)

将 CSS 属性设置为特定值是 CSS 语言的核心功能。CSS 引擎计算哪些声明应用于页面的每个元素，以便适当地布局和样式它。重要的是要记住，在 CSS 中，属性和值都是区分大小写的。每对中的属性和值由冒号 (`:`) 分隔。

> **警告：** 如果属性未知或某个值对给定属性无效，则声明被视为无效，并被浏览器的 CSS 引擎完全忽略。

### 函数

虽然大多数值是相对简单的关键字或数值，但也有一些可能的值以函数的形式出现。一个例子是 calc() 函数。这个函数允许您在 CSS 中进行简单的计算，例如：

```html
<div class="outer"><div class="box">The inner box is 90% - 30px.</div></div>
```

```css
.outer {
  border: 5px solid black;
}

.box {
padding: 10px;
width: calc(90% - 30px);
background-color: rebeccapurple;
color: white;
}

```

![image-20220817143651911](image-20220817143651911.png)

一个函数由函数名和一些括号组成，其中放置了该函数的允许值。在上面的 `calc()` 示例中，我要求此框的宽度为包含块宽度的 90%，减去 30 像素。这不是我可以提前计算的东西，只是在 CSS 中输入值，因为我不知道 90% 会是什么。与所有值一样，MDN 上的相关页面将有使用示例，这样您就可以看到函数是如何工作的。

另一个例子是[`transform`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/transform), 例如 `rotate()`.

```html
<div class="box"></div>

```

```css
.box {
  margin: 30px;
  width: 100px;
  height: 100px;
  background-color: rebeccapurple;
  transform: rotate(0.8turn)
}

```

![image-20220817144019278](image-20220817144019278.png)

### `@rules`

到目前为止，我们还没有遇到 [`@rules`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/At-rule) (发音为 "at-rules")。这是一些特殊的规则，为 CSS 提供了一些关于如何表现的指导。有些 `@rules` 规则很简单，有规则名和值。例如，要将额外的样式表导入主 CSS 样式表，可以使用 `@import`:

```css
@import 'styles2.css';

```

您将遇到的最常见的 @rule 之一是 `@media`，它允许您使用[媒体查询](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Media_Queries)来应用 CSS，仅当某些条件成立 (例如，当屏幕分辨率高于某一数量，或屏幕宽度大于某一宽度时)。

在下面的 CSS 中，我们将给 `<body>` 元素一个粉红色的背景色。但是，我们随后使用 @media 创建样式表的一个部分，该部分仅适用于视口大于 1000px 的浏览器。如果浏览器的宽度大于 1000px，则背景色将为蓝色。

```css
body {
  background-color: pink;
}

@media (min-width: 1000px) {
  body {
    background-color: blue;
  }
}

```

![media](media.gif)

### 速记属性

一些属性，如 [`font`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font), [`background`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background), [`padding`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding), [`border`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border), and [`margin`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin) 等属性称为速记属性--这是因为它们允许您在一行中设置多个属性值，从而节省时间并使代码更整洁。

例如，这一行代码：

```css
/* In 4-value shorthands like padding and margin, the values are applied
   in the order top, right, bottom, left (clockwise from the top). There are also other
   shorthand types, for example 2-value shorthands, which set padding/margin
   for top/bottom, then left/right */
padding: 10px 15px 15px 5px;

```

与这四行代码是等价的：

```css
padding-top: 10px;
padding-right: 15px;
padding-bottom: 15px;
padding-left: 5px;
```

这一行：

```css
background: red url(bg-graphic.png) 10px 10px repeat-x fixed;

```

与这五行代码是等价的：

```css
background-color: red;
background-image: url(bg-graphic.png);
background-position: 10px 10px;
background-repeat: repeat-x;
background-attachment: fixed;

```

### 注释

与任何的代码工作一样，在编写 CSS 过程中，最好的练习方式就是添加注释。这样做可以帮助您在过了几个月后回来修改或优化代码时了解它们是如何工作的，同时也便于其他人理解您的代码。

CSS 中的注释以 `/*` 开头，以 `*/` 结尾。在下面的代码块中，注释标记了不同代码节的开始。当代码库变得更大时，这对于帮助您导航代码库非常有用——在代码编辑器中搜索注释可以高效地定位代码节。

```css
/* Handle basic element styling */
/* -------------------------------------------------------------------------------------------- */
body {
  font: 1em/150% Helvetica, Arial, sans-serif;
  padding: 1em;
  margin: 0 auto;
  max-width: 33em;
}

@media (min-width: 70em) {
  /* Let's special case the global font size. On large screen or window,
     we increase the font size for better readability */
  body {
    font-size: 130%;
  }
}

h1 {font-size: 1.5em;}

/* Handle specific elements nested in the DOM  */
/* -------------------------------------------------------------------------------------------- */
div p, #id:first-line {
  background-color: red;
  border-radius: 3px;
}

div p{
  margin: 0;
  padding: 1em;
}

div p + p {
  padding-top: 0;
}

```

“注释掉”代码这一操作常用于在测试中临时禁用一段代码。例如，如果您试图找出代码的哪一部分会导致错误。在下例中，`.special` selector 规则被“注释”掉了，也就是被禁用了。

### 空白

空白是指实际空格、制表符和新行。以与 HTML 相同的方式，浏览器往往忽略 CSS 中的大部分空白；许多空白只是为了提高可读性。

在下面的第一个示例中，我们将每个声明 (以及规则开始/结束) 都放在自己的行中--这可以说是编写 CSS 的好方法，因为它使维护和理解变得更加容易：

```css
body {
  font: 1em/150% Helvetica, Arial, sans-serif;
  padding: 1em;
  margin: 0 auto;
  max-width: 33em;
}

@media (min-width: 70em) {
  body {
    font-size: 130%;
  }
}

h1 {
  font-size: 1.5em;
}

div p,
#id:first-line {
  background-color: red;
  border-radius: 3px;
}

div p {
  margin: 0;
  padding: 1em;
}

div p + p {
  padding-top: 0;
}

```

您可以编写完全相同的 CSS，删除大部分空格--这在功能上与第一个示例相同，但我相信您肯定也觉得阅读起来有点困难：

```css
body {font: 1em/150% Helvetica, Arial, sans-serif; padding: 1em; margin: 0 auto; max-width: 33em;}
@media (min-width: 70em) { body {font-size: 130%;} }

h1 {font-size: 1.5em;}

div p, #id:first-line {background-color: red; border-radius: 3px;}
div p {margin: 0; padding: 1em;}
div p + p {padding-top: 0;}

```

您选择的代码布局通常是个人偏好，尽管当您开始在团队中工作时，您可能会发现现有团队有自己的样式指南，指定要遵循的约定。

在 CSS 中，属性和它们的值之间的空格需要小心。

例如，以下声明是有效的 CSS：

```css
margin: 0 auto;
padding-left: 10px;

```

以下内容无效：

```css
margin: 0auto;
padding- left: 10px;

```



## `CSS`是如何工作的

我们已经知道了 CSS 是做什么的以及怎么写简单的样式这样基础的 CSS，接下来我将了解到浏览器如何获取 CSS、HTML 和将他们加载成网页。

### `CSS` 究竟是怎么工作的？

当浏览器展示一个文件的时候，它必须兼顾文件的内容和文件的样式信息，下面我们会了解到它处理文件的标准的流程。需要知道的是，下面的步骤是浏览加载网页的简化版本，而且不同的浏览器在处理文件的时候会有不同的方式，但是下面的步骤基本都会出现。

1. 浏览器载入 HTML 文件（比如从网络上获取）。
2. 将 HTML 文件转化成一个 DOM（Document Object Model），DOM 是文件在计算机内存中的表现形式，下一节将更加详细的解释 DOM。
3. 接下来，浏览器会拉取该 HTML 相关的大部分资源，比如嵌入到页面的图片、视频和 CSS 样式。JavaScript 则会稍后进行处理，简单起见，同时此节主讲 CSS，所以这里对如何加载 JavaScript 不会展开叙述。
4. 浏览器拉取到 CSS 之后会进行解析，根据选择器的不同类型（比如 element、class、id 等等）把他们分到不同的“桶”中。浏览器基于它找到的不同的选择器，将不同的规则（基于选择器的规则，如元素选择器、类选择器、id 选择器等）应用在对应的 DOM 的节点中，并添加节点依赖的样式（这个中间步骤称为渲染树）。
5. 上述的规则应用于渲染树之后，渲染树会依照应该出现的结构进行布局。
6. 网页展示在屏幕上（这一步被称为着色）。

结合下面的图示更形象：

![img-render-flow](rendering.svg)

### 关于 DOM

一个 DOM 有一个树形结构，标记语言中的每一个元素、属性以及每一段文字都对应着结构树中的一个节点（Node/DOM 或 DOM node）。节点由节点本身和其他 DOM 节点的关系定义，有些节点有父节点，有些节点有兄弟节点（同级节点）。

对于 DOM 的理解会很大程度上帮助你设计、调试和维护你的 CSS，因为 DOM 是你的 CSS 样式和文件内容的结合。当你使用浏览器 F12 调试的时候你需要操作 DOM 以查看使用了哪些规则。

### `HTML`元素转化为`DOM`

不同于很长且枯燥的案例，这里我们通过一个 HTML 片段来了解 HTML 怎么转化成 DOM

以下列 HTML 代码为例：

```html
<p>
  Let's use:
  <span>Cascading</span>
  <span>Style</span>
  <span>Sheets</span>
</p>

```

在这个 DOM 中，`<p>`元素对应了父节点，它的子节点是一个 text 节点和三个对应了`<span>`元素的节点，`SPAN`节点同时也是他们中的 Text 节点的父节点。

```
P
├─ "Let's use:"
├─ SPAN
|  └─ "Cascading"
├─ SPAN
|  └─ "Style"
└─ SPAN
    └─ "Sheets"
```

上图就是浏览器怎么解析之前那个 HTML 片段——它生成上图的 DOM 树形结构并将它按照如下输出到浏览器：

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My CSS experiment</title>
  </head>
  <body>
  <p>
    Let's use:
    <span>Cascading</span>
    <span>Style</span>
    <span>Sheets</span>
  </p>
  </body>
</html>

### 应用 CSS 到 DOM

接下来让我们看看添加一些 CSS 到文件里加以渲染，同样的 HTML 代码：

```html
<p>
  Let's use:
  <span>Cascading</span>
  <span>Style</span>
  <span>Sheets</span>
</p>

```

以下为 CSS 代码：

```css
span {
  border: 1px solid black;
  background-color: lime;
}

```

浏览器会解析 HTML 并创造一个 DOM，然后解析 CSS。可以看到唯一的选择器就是`span`元素选择器，浏览器处理规则会非常快！把同样的规则直接使用在三个`<span>`标签上，然后渲染出图像到屏幕。

现在的显示如下：

![image-20220817153053649](image-20220817153053649.png)

在我们下一个模块的 [Debugging CSS](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Debugging_CSS) 文章中我们将会使用 F12 调试 CSS 的问题并且更进一步的了解浏览器如何解析 CSS。

### 无法解析的 CSS 代码

在[之前的文章中](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/First_steps/What_is_CSS#浏览器支持)我们提到了浏览器并不会同时实现所有的新 CSS，此外很多人也不会使用最新版本的浏览器。鉴于 CSS 一直不断的开发，因此领先于浏览器可以识别的范围，那么你也许会好奇当浏览器遇到无法解析的 CSS 选择器或声明的时候会发生什么呢？

答案就是浏览器什么也不会做，继续解析下一个 CSS 样式！

如果一个浏览器在解析你所书写的 CSS 规则的过程中遇到了无法理解的属性或者值，它会忽略这些并继续解析下面的 CSS 声明。在你书写了错误的 CSS 代码（或者误拼写），又或者当浏览器遇到对于它来说很新的还没有支持的 CSS 代码的时候上述的情况同样会发生（直接忽略）。

相似的，当浏览器遇到无法解析的选择器的时候，他会直接忽略整个选择器规则，然后解析下一个 CSS 选择器。

在下面的案例中，我使用会导致属性错误的英式拼写来书写"color"，所以我的段落没有被渲染成蓝色，而其他的 CSS 代码会正常执行，只有错误的部分会被忽略。

```html
<p>I want this text to be large, bold and blue.</p>

```



```css
p {
  font-weight: bold;
  colour: blue; /* incorrect spelling of the color property */
  font-size: 200%;
}

```

![image-20220817153330674](image-20220817153330674.png)

这样做好处多多，代表着你使用最新的 CSS 优化的过程中浏览器遇到无法解析的规则也不会报错。当你为一个元素指定多个 CSS 样式的时候，浏览器会加载样式表中的最后的 CSS 代码进行渲染（样式表，优先级等请读者自行了解），也正因为如此，你可以为同一个元素指定多个 CSS 样式来解决有些浏览器不兼容新特性的问题（比如指定两个`width`）。

这一特点在你想使用一个很新的 CSS 特性但是不是所有浏览器都支持的时候（浏览器兼容）非常有用，举例来说，一些老的浏览器不接收`calc()`(calculate 的缩写，CSS3 新增，为元素指定动态宽度、长度等，注意此处的动态是计算之后得一个值) 作为一个值。我可能使用它结合像素为一个元素设置了动态宽度（如下），老式的浏览器由于无法解析忽略这一行；新式的浏览器则会把这一行解析成像素值，并且覆盖第一行指定的宽度。

```css
.box {
  width: 500px;
  width: calc(100% - 50px);
}

```

后面的课程我们会讨论更多关于浏览器兼容的问题。

# `CSS`构建基础

这个模块承接[学习 CSS 第一步](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/First_steps)——即你对 (CSS) 语言和其语法已经足够熟悉、并且有了一些基本的使用经验，该是稍微深入点学习的时候了。

这个模块着眼于级联和继承，所有可供使用的选择器类型，单位，尺寸，背景、边框样式，调试，等等等等。

本文目标是，在你进一步了解 [为文本添加样式](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Styling_text)和[CSS 布局](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout)之前，为你提供一个助你写出合格 CSS 和理解所有基本理论的工具箱。

## 层叠与继承

> 本文旨在让你理解 CSS 的一些最基本的概念——层叠、优先级和继承——这些概念决定着如何将 CSS 应用到 HTML 中，以及如何解决冲突。
>
> 尽管与课程的其他部分相比，完成这节课可能看起来没有那么直接的相关性，而且更学术性一些，但是理解这些东西将为您以后节省很多痛苦！我希望您仔细阅读本节，并在继续下一步学习之前，确保您是否理解了这些概念。



### 冲突规则

CSS 代表**层叠样式表 (Cascading Style Sheets)**，理解第一个词*cascading*很重要— cascade 的表现方式是理解 CSS 的关键。

在某些时候，在做一个项目过程中你会发现一些应该产生效果的样式没有生效。通常的原因是你创建了两个应用于同一个元素的规则。**cascade**, 和它密切相关的概念是 **specificity**，决定在发生冲突的时候应该使用哪条规则。设计元素样式的规则可能不是期望的规则，因此需要了解这些机制是如何工作的。

这里也有**继承**的概念，也就是在默认情况下，一些 css 属性继承当前元素的父元素上设置的值，有些则不继承。这也可能导致一些和期望不同的结果。

我们来快速的看下正在处理的关键问题，然后依次了解它们是如何相互影响的，以及如何和 css 交互的。虽然这些概念难以理解，但是随着不断的练习，你会慢慢熟悉它的工作原理。

#### 层叠

Stylesheets **cascade（样式表层叠）** — 简单的说，css 规则的顺序很重要；当应用两条同级别的规则到一个元素的时候，写在后面的就是实际使用的规则。

下面的例子中，我们有两个关于 `h1` 的规则。`h1` 最后显示蓝色 — 这些规则有相同的优先级，所以顺序在最后的生效。

```html
<h1>This is my heading.</h1>
    
```



```css
h1 { 
    color: red; 
}
h1 { 
    color: blue; 
}
    
```

![image-20220817154423408](image-20220817154423408.png)

#### 优先级

浏览器是根据优先级(`Specificity`)来决定当多个规则有不同选择器对应相同的元素的时候需要使用哪个规则。它基本上是一个衡量选择器具体选择哪些区域的尺度：

- 一个元素选择器不是很具体 — 会选择页面上该类型的所有元素 — 所以它的优先级就会低一些。
- 一个类选择器稍微具体点 — 它会选择该页面中有特定 `class` 属性值的元素 — 所以它的优先级就要高一点。

举例时间 ! 下面我们再来介绍两个适用于 `h1` 的规则。下面的 `h1` 最后会显示红色 — 类选择器有更高的优先级，因此就会被应用——即使元素选择器顺序在它后面。

```html
<h1 class="main-heading">This is my heading.</h1>
    
```

```css
.main-heading { 
    color: red; 
}
        
h1 { 
    color: blue; 
}
    
```

![image-20220817154931024](image-20220817154931024.png)

稍后我们会详细解释优先级评分和其他相关内容。

#### 继承

- 我们为一个元素设置的样式，同时也会应用到它到底后台元素上

- 继承是发生在祖先后代之间的

- 继承的设计是为了方便我们的开发，利用继承我们可以将一些通用的样式，统一设置到共同的祖先元素上，这样只需设置一次即可让所有的元素具有该样式

注意：并不是所有的样式都会被继承，比如，背景相关的，布局相关的等，这些样式都不会被继承



继承也需要在上下文中去理解 —— 一些设置在父元素上的 css 属性是可以被子元素继承的，有些则不能。

举一个例子，如果你设置一个元素的 `color` 和 `font-family` ，每个在里面的元素也都会有相同的属性，除非你直接在元素上设置属性。

```html
<p>As the body has been set to have a color of blue this is inherited through the descendants.</p>
<p>We can change the color by targeting the element with a selector, such as this <span>span</span>.</p>
    
```

```css
body {
    color: blue;
}

span {
    color: black;
}
    
```

![image-20220817155129455](image-20220817155129455.png)

一些属性是不能继承的 — 举个例子如果你在一个元素上设置 [`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width) 50% ，所有的后代不会是父元素的宽度的 50% 。如果这个也可以继承的话，CSS 就会很难使用了！

### 理解这些概念是如何协同工作的

这三个概念一起来控制 css 规则应用于哪个元素；在下面的内容中，我们将看到它们是如何协同工作的。有时候会感觉有些复杂，但是当你对 css 有更多经验的时候，你就可以记住它们，即便忘记了细节，可以在网上查到，有经验的开发人员也不会记得所有细节。

### 理解继承

我们从继承开始。下面的例子中我们有一个`ul`，里面有两个无序列表。我们已经给 `<ul>` 设置了 **border**， **padding** 和 **font color**.

**color** 应用在直接子元素，也影响其他后代 — 直接子元素`<li>`，和第一个嵌套列表中的子项。然后添加了一个 `special` 类到第二个嵌套列表，其中使用了不同的颜色。然后通过它的子元素继承。

```html
<ul class="main">
    <li>Item One</li>
    <li>Item Two
        <ul>
            <li>2.1</li>
            <li>2.2</li>
        </ul>
    </li>
    <li>Item Three
        <ul class="special">
            <li>3.1
                <ul>
                    <li>3.1.1</li>
                    <li>3.1.2</li>
                </ul>
            </li>
            <li>3.2</li>
        </ul>
    </li>
</ul>
    
```

```css
.main {
    color: rebeccapurple;
    border: 2px solid #ccc;
    padding: 1em;
}

.special {
    color: black;
    font-weight: bold;
}
    
```

![image-20220817155511044](image-20220817155511044.png)

像 widths (上面提到的), margins, padding, 和 borders 不会被继承。如果 borders 可以被继承，每个列表和列表项都会获得一个边框 — 可能就不是我们想要的结果！

哪些属性属于默认继承很大程度上是由常识决定的。

#### 控制继承

CSS 为控制继承提供了五个特殊的通用属性值。每个 css 属性都接收这些值。

[`inherit`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/inherit)

设置该属性会使子元素属性和父元素相同。实际上，就是 "开启继承".

[`initial`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/initial)

设置属性值和浏览器默认样式相同。如果浏览器默认样式中未设置且该属性是自然继承的，那么会设置为 `inherit` 。

[`revert` (en-US)](https://developer.mozilla.org/en-US/docs/Web/CSS/revert)

将应用于选定元素的属性值重置为浏览器的默认样式，而不是应用于该属性的默认值。在许多情况下，此值的作用类似于 `unset`。

[`revert-layer` (en-US)](https://developer.mozilla.org/en-US/docs/Web/CSS/revert-layer)

将应用于选定元素的属性值重置为在上一个[层叠层](https://developer.mozilla.org/zh-CN/docs/Web/CSS/@layer)中建立的值。

[`unset`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/unset)

将属性重置为自然值，也就是如果属性是自然继承那么就是 `inherit`，否则和 `initial` 一样



下面的例子你可以通过修改 css 来查看它们的功能，写代码是掌握 html 和 css 最好的办法。

例子：

1. 第二个列表项有类 `my-class-1` 。它设置了内部元素来继承属性。如果你删除这个类，它会如何改变链接的颜色？
2. 你知道为什么第三个和第四个链接会是这样的颜色？ 如果不知道看看之前的内容。
3. 如果你对 `<a>` 添加一个新样式 — 例如 `a { color: red; }`，哪个链接的颜色会改变?

```html
<ul>
    <li>Default <a href="#">link</a> color</li>
    <li class="my-class-1">Inherit the <a href="#">link</a> color</li>
    <li class="my-class-2">Reset the <a href="#">link</a> color</li>
    <li class="my-class-3">Unset the <a href="#">link</a> color</li>
</ul>
    
```

```css
body {
    color: green;
}
          
.my-class-1 a {
    color: inherit;
}
          
.my-class-2 a {
    color: initial;
}
          
.my-class-3 a {
    color: unset;
}
    
```

![image-20220817160321667](image-20220817160321667.png)

#### 重设所有属性值

CSS 的 shorthand 属性（速记属性） `all` 可以用于同时将这些继承值中的一个应用于（几乎）所有属性。它的值可以是其中任意一个 (`inherit`, `initial`, `unset`, or `revert`)。这是一种撤销对样式所做更改的简便方法，以便回到之前已知的起点。

下面的例子中有两个**blockquote** 。第一个用元素本身的样式 ，第二个设置 `all` 为 `unset`

```html
        <blockquote>
            <p>This blockquote is styled</p>
        </blockquote>

        <blockquote class="fix-this">
            <p>This blockquote is not styled</p>
        </blockquote>
    
```

```css
blockquote {
    background-color: red;
    border: 2px solid green;
}
        
.fix-this {
    all: unset;
}
    
```

![image-20220817160931487](image-20220817160931487.png)

试着将 `all` 改成其他可能的值然后观察有什么不一样。

### 理解层叠

我们现在明白了为什么嵌套在 html 结构中的段落和应用于正文中的 css 颜色相同，从入门课程中，我们了解了如何将文档中的任何修改应用于某个对象的 css，无论是把 css 指定某个元素还是创建一个类。现在，我们将要了解层叠如何定义在不止一个元素的时候怎么应用 css 规则。

有三个因素需要考虑，根据重要性排序如下，前面的更重要：

1. 重要程度
2. 优先级
3. 资源顺序

我们从下往上，看看浏览器是如何决定该应用哪个 css 规则的。

#### 资源顺序

我们已经看到了顺序对于层叠的重要性。如果你有超过一条规则，而且都是相同的权重，那么最后面的规则会应用。可以理解为后面的规则覆盖前面的规则，直到最后一个开始设置样式。

#### 优先级

在你了解了顺序的重要性后，会发现在一些情况下，有些规则在最后出现，但是却应用了前面的规则。这是因为前面的有更高的**优先级** — 它范围更小，因此浏览器就把它选择为元素的样式。

就像前面看到的，类选择器的权重大于元素选择器，因此类上定义的属性将覆盖应用于元素上的属性。

这里需要注意虽然我们考虑的是选择器，以及应用在选中对象上的规则，但不会覆盖所有规则，只有相同的属性。

这样可以避免重复的 CSS。一种常见的做法是给基本元素定义通用样式，然后给不同的元素创建对应的类。举个例子，在下面的样式中我给 2 级标题定义了通用样式，然后创建了一些类只修改部分属性的值。最初定义的值应用于所有标题，然后更具体的值通过对应类来实现。

```html
<h2>Heading with no class</h2>
<h2 class="small">Heading with class of small</h2>
<h2 class="bright">Heading with class of bright</h2>
    
```

```css
h2 {
    font-size: 2em;
    color: #000;
    font-family: Georgia, 'Times New Roman', Times, serif;
}
        
.small {
    font-size: 1em;
}
        
.bright {
    color: rebeccapurple;
}         
    
```

![image-20220817162140498](image-20220817162140498.png)

现在让我们来看看浏览器如何计算优先级。我们已经知道一个元素选择器比类选择器的优先级更低会被其覆盖。本质上，不同类型的选择器有不同的分数值，把这些分数相加就得到特定选择器的权重，然后就可以进行匹配。

一个选择器的优先级可以说是由四个部分相加 (分量)，可以认为是个十百千 — 四位数的四个位数：

1. **千位**： 如果声明在 [`style`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes#attr-style) 的属性（内联样式）则该位得一分。这样的声明没有选择器，所以它得分总是 1000。
2. **百位**： 选择器中包含 ID 选择器则该位得一分。
3. **十位**： 选择器中包含类选择器、属性选择器或者伪类则该位得一分。
4. **个位**：选择器中包含元素、伪元素选择器则该位得一分。

> **备注：** 通用选择器 (`*`)，组合符 (`+`, `>`, `~`, ' ')，和否定伪类 (`:not`) 不会影响优先级。
>
> **警告：** 在进行计算时不允许进行进位，例如，20 个类选择器仅仅意味着 20 个十位，而不能视为 两个百位，也就是说，无论多少个类选择器的权重叠加，都不会超过一个 ID 选择器。

下面有几个单独的例子，有空可以看看。试着思考下，理解为什么优先级是这样定的。我们还没有深入介绍选择器，不过你可以在 MDN 上面找到每个选择器的详细信息 [selectors reference](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors).

![image-20220817162419360](image-20220817162419360.png)

在我们继续之前，先看看这个例子。

```html
<div id="outer" class="container">
    <div id="inner" class="container">
        <ul>
            <li class="nav"><a href="#">One</a></li>
            <li class="nav"><a href="#">Two</a></li>
        </ul>
    </div>
</div>
    
```

```css

/* 1. specificity: 1-0-1 */
#outer a {
    background-color: red;
}
        
/* 2. specificity: 2-0-1 */
#outer #inner a {
    background-color: blue;
}

/* 3. specificity: 1-0-4 */
#outer div ul li a {
    color: yellow;
}

/* 4. specificity: 1-1-3 */
#outer div ul .nav a {
    color: white;
}

/* 5. specificity: 0-2-4 */
div div li:nth-child(2) a:hover {
    border: 10px solid black;
}

/* 6. specificity: 0-2-3 */
div li:nth-child(2) a:hover {
    border: 10px dashed black;
}

/* 7. specificity: 0-3-3 */
div div .nav:nth-child(2) a:hover {
    border: 10px double black;
}

a {
    display: inline-block;
    line-height: 40px;
    font-size: 20px;
    text-decoration: none;
    text-align: center;
    width: 200px;
    margin-bottom: 10px;
}

ul {
    padding: 0;
}

li {
    list-style-type: none;
}            
    
```

![image-20220817162621838](image-20220817162621838.png)

这里发生了什么？ 首先，我们先看看最上面的选择器规则，你会发现，我们已经把优先级计算出来放在最前面的注释里。

- 前面两个选择器都是链接背景颜色的样式 — 第二个赢了使得背景变成蓝色因为它多了一个 ID 选择器：优先级 201 vs. 101。
- 第三四个选择器都是链接文本颜色样式 — 第二个（第四个）赢了使得文本变成白色因为它虽然少一个元素选择器，但是多了一个类选择器，多了 9 分。所以优先级是 113 vs. 104。
- 第 5 到 7 个选择器都是鼠标悬停时链接边框样式。第六个显然输给第五个优先级是 23 vs. 24 — 少了个元素选择器。 第七个，比第五第六都高 — 子选择器数量相同，但是有一个元素选择器变成类选择器。所以最后优先级是 33 vs. 23 和 24。

#### `!important`

有一个特殊的 CSS 可以用来覆盖所有上面所有优先级计算，不过需要很小心的使用 — `!important`。用于修改特定属性的值， 能够覆盖普通规则的层叠。

看看这个例子，有两个段落，其中一个有 ID。

```html
<p class="better">This is a paragraph.</p>
<p class="better" id="winning">One selector to rule them all!</p>
    
```

```css

#winning {
    background-color: red;
    border: 1px solid black;
}
    
.better {
    background-color: gray;
    border: none !important;
}
    
p {
    background-color: blue;
    color: white;
    padding: 5px;
}           
    
```

![image-20220817162822375](image-20220817162822375.png)

让我们看看会发生什么 — 如果有什么疑问，试着删除一些属性：

1. 你会发现第三个规则 [`color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/color) 和 [`padding`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding) 的值被应用了，但是 [`background-color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-color) 没有。为什么？ 应该三个都应用，因为顺序规则是后面覆盖前面。
2. 无论如何， 上面的规则赢了，因为类选择器比元素选择器有更高的优先级。
3. 两个元素都有 `better`[`class`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes#attr-class)，但是第二个有 [`id`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes#attr-id) 。因为 ID 选择器比类选择器优先级更高 (一个页面只能有一个独特的 ID，但是很多元素都有相同的类 — ID 对于目标非常独特)，红色背景和1像素的黑色边框， 应该都被应用到第二个元素，根据类选择器，第一个元素应该是灰色背景和没有边框。
4. 第二个元素有红色背景但是没有边框。为什么？因为 `!important` 声明在第二条规则里 — 在 `border: none` 后面，说明即使计算优先级低这个属性也使用这个值。

> **备注：** 覆盖 `!important` 唯一的办法就是另一个 `!important` 具有 相同*优先级* 而且顺序靠后，或者更高优先级。

了解 `!important` 是为了在阅读别人代码的时候知道有什么作用。 **但是，强烈建议除了非常情况不要使用它。** `!important` 改变了层叠的常规工作方式，它会使调试 CSS 问题非常困难，特别是在大型样式表中。

在一种情况下，你可能不得不使用它：当你不能编辑核心的 CSS 模块，不能用任何其他方式覆盖，而你又真的想要覆盖一个样式时。但说真的，如果可以避免的话就不要用它。

### 小结

如果您理解了本文的大部分内容，那么就做得很好了—您已经开始熟悉 CSS 的基本机制。接下来，我们将详细讨论选择器。

如果您没有完全理解层叠，优先级和继承，也请不要担心！这绝对是我们到目前为止在课程中所涉及到的最复杂的事情，即使是专业的 web 开发人员有时也会觉得棘手。我们建议您在继续学习这门课程的过程中，反复阅读这篇文章几次，并继续思考它。

如果您开始遇到样式没有按照预期应用的奇怪问题，请回到这里。这可能是一个优先级的问题。

## `CSS`选择器

[CSS选择器汇总 | mindcons.cn](https://mindcons.cn/sai/45915/)

[CSS](https://developer.mozilla.org/zh-CN/docs/Glossary/CSS)中，选择器用来指定网页上我们想要样式化的[HTML](https://developer.mozilla.org/zh-CN/docs/Glossary/HTML)元素。有 CSS 选择器提供了很多种方法，所以在选择要样式化的元素时，我们可以做到很精细的地步。本文和本文的子篇中，我们将会详细地讲授选择器的不同使用方式，并了解它们的工作原理。

### 选择器是什么？

你也许已经见过选择器了。CSS 选择器是 CSS 规则的第一部分。它是元素和其他部分组合起来告诉浏览器哪个 HTML 元素应当是被选为应用规则中的 CSS 属性值的方式。选择器所选择的元素，叫做“选择器的对象”。

![Some code with the h1 highlighted.](selector.png)

前面的文章中，你也许已经遇到过几种不同的选择器，了解到选择器可以以不同的方式选择元素，比如选择诸如`h1`的元素，或者是根据 class (类) 选择例如`.special`。

CSS 中，选择器由 CSS 选择器规范加以定义。就像是 CSS 的其他部分那样，它们需要浏览器的支持才能工作。你会遇到的大多数选择器都是在[CSS 3](https://www.w3.org/TR/selectors-3/)中定义的，这是一个成熟的规范，因此你会发现浏览器对这些选择器有良好的支持。

### 选择器列表

如果你有多个使用相同样式的 CSS 选择器，那么这些单独的选择器可以被混编为一个“选择器列表”，这样，规则就可以应用到所有的单个选择器上了。例如，如果我的`h1`和`.special`类有相同的 CSS，那么我可以把它们写成两个分开的规则。

```css
h1 {
  color: blue;
}

.special {
  color: blue;
}

```

我也可以将它们组合起来，在它们之间加上一个逗号，变为选择器列表。

```css
h1, .special {
  color: blue;
}

```

空格可以在逗号前或后，你可能还会发现如果每个选择器都另起一行，会更好读些。

```css
h1,
.special {
  color: blue;
}

```

当你使用选择器列表时，如果任何一个选择器无效 (存在语法错误)，那么整条规则都会被忽略。

在下面的示例中，无效的 class 选择器会被忽略，而`h1`选择器仍会被样式化。

```css
h1 {
  color: blue;
}

..special {
  color: blue;
}

```

但是在被组合起来以后，整个规则都会失效，无论是`h1`还是这个 class 都不会被样式化。

```css
h1, ..special {
  color: blue;
}

```

### 选择器的种类

有几组不同的选择器，知道了需要哪种选择器，你会更容易正确使用它们。在本文的子篇中，我们将会来更详细地看下不同种类的选择器。

#### 类型、类和 ID 选择器

这个选择器组，第一个是指向了所有 HTML 元素`<h1>。`

```css
h1 { }
```

它也包含了一个 class 的选择器：

```css
.box { }
```

亦或，一个 id 选择器：

```css
#unique { }
```

### 标签属性选择器

这组选择器根据一个元素上的某个标签的属性的存在以选择元素的不同方式：

```css
a[title] { }
```

或者根据一个有特定值的标签属性是否存在来选择：

```css
a[href="https://example.com"] { }
```

### 伪类与伪元素

这组选择器包含了伪类，用来样式化一个元素的特定状态。例如`:hover`伪类会在鼠标指针悬浮到一个元素上的时候选择这个元素：

```css
a:hover { }
```

它还可以包含了伪元素，选择一个元素的某个部分而不是元素自己。例如，`::first-line`是会选择一个元素（下面的情况中是`<p>`）中的第一行，类似`<span>`包在了第一个被格式化的行外面，然后选择这个`<span>`。

```css
p::first-line { }
```

### 运算符

最后一组选择器可以将其他选择器组合起来，更复杂的选择元素。下面的示例用运算符（`>`）选择了`<article>`元素的初代子元素。

```css
article > p { }
```



你可以看下下面的选择器参考表，可以获得到这个学习章节——或者总体来说是 MDN 上——的各种选择器的直接链接；你也可以继续下去，开始你的了解[类型、类和 ID 选择器](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Selectors/Type_Class_and_ID_Selectors)的旅程。

下面的表格让你可以浏览你可以用的选择器，还有本指南中教你如何使用每种选择器的页面的链接。我还加上了一个能查看浏览器对每个选择器的支持信息的 MDN 页面链接。你可以把这个作为回头的参考，在你以后需要查询文献中提到的选择器的时候，或者是在你广义上实验 CSS 的时候。

| 选择器                                                       | 示例                |
| :----------------------------------------------------------- | :------------------ |
| [类型选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Type_selectors) | `h1 { }`            |
| [通配选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Universal_selectors) | `* { }`             |
| [类选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Class_selectors) | `.box { }`          |
| [ID 选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/ID_selectors) | `#unique { }`       |
| [标签属性选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Attribute_selectors) | `a[title] { }`      |
| [伪类选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Pseudo-classes) | `p:first-child { }` |
| [伪元素选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Pseudo-elements) | `p::first-line { }` |
| [后代选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Descendant_combinator) | `article p`         |
| [子代选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Child_combinator) | `article > p`       |
| [相邻兄弟选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Adjacent_sibling_combinator) | `h1 + p`            |
| [通用兄弟选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/General_sibling_combinator) | `h1 ~ p`            |

## 盒模型

在 CSS 中，所有的元素都被一个个的“盒子（box）”包围着，理解这些“盒子”的基本原理，是我们使用 CSS 实现准确布局、处理元素排列的关键。

本文围绕“盒模型”为主题展开。旨在于完成学习后，您能够在“理解盒装模型原理”的基础上，完成更加复杂的布局任务。	

### 块级盒子（Block box） 和 内联盒子（Inline box）

在 CSS 中我们广泛地使用两种“盒子” —— **块级盒子** (**block box**) 和 **内联盒子** (**inline box**)。这两种盒子会在**页面流**（page flow）和元素之间的关系方面表现出不同的行为：

一个被定义成块级的（block）盒子会表现出以下行为：

- 盒子会在内联的方向上扩展并占据父容器在该方向上的所有可用空间，在绝大数情况下意味着盒子会和父容器一样宽
- 每个盒子都会换行
- [`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width) 和 [`height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/height) 属性可以发挥作用
- 内边距（padding）, 外边距（margin）和 边框（border）会将其他元素从当前盒子周围“推开”

除非特殊指定，诸如标题 (`<h1>`等) 和段落 (`<p>`) 默认情况下都是块级的盒子。

如果一个盒子对外显示为 `inline`，那么他的行为如下：

- 盒子不会产生换行。
- [`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width) 和 [`height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/height) 属性将不起作用。
- 垂直方向的内边距、外边距以及边框会被应用但是不会把其他处于 `inline` 状态的盒子推开。
- 水平方向的内边距、外边距以及边框会被应用且会把其他处于 `inline` 状态的盒子推开。

用做链接的 `<a>` 元素、 `<span>`、 `<em>` 以及 `<strong>` 都是默认处于 `inline` 状态的。

我们通过对盒子[`display`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/display) 属性的设置，比如 `inline` 或者 `block` ，来控制盒子的外部显示类型。

### 内部和外部显示类型

在这里最好也解释下**内部** 和 **外部** 显示类型。如上所述， css 的 box 模型有一个外部显示类型，来决定盒子是块级还是内联。

同样盒模型还有内部显示类型，它决定了盒子内部元素是如何布局的。默认情况下是按照 **[正常文档流](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Normal_Flow) **布局，也意味着它们和其他块元素以及内联元素一样 (如上所述).

但是，我们可以通过使用类似 `flex` 的 `display` 属性值来更改内部显示类型。如果设置 `display: flex`，在一个元素上，外部显示类型是 `block`，但是内部显示类型修改为 `flex`。该盒子的所有直接子元素都会成为 flex 元素，会根据[弹性盒子（Flexbox）](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Flexbox)规则进行布局，稍后您将了解这些规则。

> **备注：** 想要了解更多有关显示值以及盒子在块和内联布局中的工作原理，请参阅[常规流中的块和内联布局](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Flow_Layout/Block_and_Inline_Layout_in_Normal_Flow)。

当你进一步了解 css 布局的更多细节的时候，你会了解到 `flex`，和其他内部显示类型会用到的值，例如 [`grid`](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Grids) 。

块级和内联布局是 web 上默认的行为 —— 正如上面所述， 它有时候被称为 *正常文档流*， 因为如果没有其他说明，我们的盒子布局默认是块级或者内联。

### 不同显示类型的例子

让我们继续看看别的例子。下面三个 html 元素，都有一个外部显示类型 `block`。第一个是一个段落，在 CSS 中加了边框。浏览器把它渲染成一个块级盒子，所以段落从新的一行开始，而且宽度占满一行。

第二个是一个列表，布局属性是 `display: flex`。 将在容器中建立一个 flex 布局，但是每个列表是一个块级元素 —— 像段落一样 —— 会充满整个容器的宽度并且换行。

下面有个块级段落，里面有两个 `<span>` 元素。正常情况下是 `inline`，但是其中一个加了 block 类，设置属性 `display: block`。

```html
<p>I am a paragraph. A short one.</p>
<ul>
  <li>Item One</li>
  <li>Item Two</li>
  <li>Item Three</li>
</ul>
<p>I am another paragraph. Some of the <span class="block">words</span> have been wrapped in a <span>span element</span>.</p>
    
```

```css
p, 
ul {
  border: 2px solid rebeccapurple;
  padding: .5em;
}

.block,
li {
  border: 2px solid blue;
  padding: .5em;
}

ul {
  display: flex;
  list-style: none;
}

.block {
  display: block;
}      
    
```

![image-20220818090604745](image-20220818090604745.png)





我们可以看到 `inline` 元素在下面例子中的表现。 `<span>` 在第一段默认是内联元素所以不换行。

还有一个 `<ul>` 设置为 `display: inline-flex`，使得在一些 flex 元素外创建一个内联框。

最后设置两个段落为 `display: inline`。 `inline flex` 容器和段落在一行上而不是像块级元素一样换行。

**你可以修改 `display: inline` 为 `display: block` 或者 `display: inline-flex` 改为 `display: flex` 来观察显示模式切换。**

```html
<p>
    I am a paragraph. Some of the
    <span>words</span> have been wrapped in a
    <span>span element</span>.
</p>     
<ul>
  <li>Item One</li>
  <li>Item Two</li>
  <li>Item Three</li>
</ul>
<p class="inline">I am a paragraph. A short one.</p>
<p class="inline">I am another paragraph. Also a short one.</p>
    
```

```css
p, 
ul {
  border: 2px solid rebeccapurple;
}

span,
li {
  border: 2px solid blue;
}

ul {
  display: inline-flex;
  list-style: none;
  padding: 0;
} 

.inline {
  display: inline;
}
    
```

​	![image-20220818090851705](image-20220818090851705.png)



在后面的内容中会遇到诸如弹性盒子布局的内容；现在需要记住的是， `display` 属性可以改变盒子的外部显示类型是块级还是内联，这将会改变它与布局中的其他元素的显示方式。

剩下的内容，我们会专注于外部显示类型。

### 什么是 CSS 盒模型

完整的 CSS 盒模型应用于块级盒子，内联盒子只使用盒模型中定义的部分内容。模型定义了盒的每个部分 —— margin, border, padding, and content —— 合在一起就可以创建我们在页面上看到的内容。为了增加一些额外的复杂性，有一个标准的和替代（IE）的盒模型。

#### 盒模型的各个部分

CSS 中组成一个块级盒子需要：

- **Content box**: 这个区域是用来显示内容，大小可以通过设置 [`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width) 和 [`height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/height).
- **Padding box**: 包围在内容区域外部的空白区域； 大小通过 [`padding`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding) 相关属性设置。
- **Border box**: 边框盒包裹内容和内边距。大小通过 [`border`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border) 相关属性设置。
- **Margin box**: 这是最外面的区域，是盒子和其他元素之间的空白区域。大小通过 [`margin`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin) 相关属性设置。

如下图：

![Diagram of the box model](box-model.png)

#### 标准盒模型

在标准模型中，如果你给盒设置 `width` 和 `height`，实际设置的是 *content box*。 padding 和 border 再加上设置的宽高一起决定整个盒子的大小。 见下图。

假设定义了 `width`, `height`, `margin`, `border`, and `padding`:

```css
.box {
  width: 350px;
  height: 150px;
  margin: 25px;
  padding: 25px;
  border: 5px solid black;
}

```

如果使用标准模型宽度 = 410px (350 + 25 + 25 + 5 + 5)，高度 = 210px (150 + 25 + 25 + 5 + 5)，padding 加 border 再加 content box。

![Showing the size of the box when the standard box model is being used.](standard-box-model.png)

> **备注：** margin 不计入实际大小 —— 当然，它会影响盒子在页面所占空间，但是影响的是盒子外部空间。盒子的范围到边框为止 —— 不会延伸到 margin。

#### 替代（IE）盒模型

你可能会认为盒子的大小还要加上边框和内边距，这样很麻烦，而且你的想法是对的 ! 因为这个原因，css 还有一个替代盒模型。使用这个模型，所有宽度都是可见宽度，所以内容宽度是该宽度减去边框和填充部分。使用上面相同的样式得到 (width = 350px, height = 150px).

![Showing the size of the box when the alternate box model is being used.](alternate-box-model.png)

默认浏览器会使用标准模型。如果需要使用替代模型，您可以通过为其设置 `box-sizing: border-box` 来实现。 这样就可以告诉浏览器使用 `border-box` 来定义区域，从而设定您想要的大小。

```css
.box {
  box-sizing: border-box;
}
```

如果你希望所有元素都使用替代模式，而且确实很常用，设置 `box-sizing` 在 `<html>` 元素上，然后设置所有元素继承该属性，正如下面的例子。如果想要深入理解，请看 [the CSS Tricks article on box-sizing](https://css-tricks.com/inheriting-box-sizing-probably-slightly-better-best-practice/)。

```css
html {
  box-sizing: border-box;
}
*, *::before, *::after {
  box-sizing: inherit;
}

```

> **备注：** 一个有趣的历史记录 ——Internet Explorer 默认使用替代盒模型，没有可用的机制来切换。（译者注：IE8+ 支持使用 `box-sizing` 进行切换）

### 玩转盒模型

下面的例子中，你可以看到两个盒子。都有类 `.box`，给了相同的 `width`, `height`, `margin`, `border`, and `padding`。唯一区别是第二个设置了替代模型。

**你能改变第二个盒子的大小 (通过添加 CSS 到 `.alternate` 类中) 让它和第一个盒子宽高一样吗？**

```html
<div class="box">I use the standard box model.</div>
<div class="box alternate">I use the alternate box model.</div>
    
```

```css
.box {
  border: 5px solid rebeccapurple;
  background-color: lightgray;
  padding: 40px;
  margin: 40px;
  width: 300px;
  height: 150px;
}

.alternate {
  box-sizing: border-box;
}
    
```

![image-20220818092251807](image-20220818092251807.png)

> **备注：** [单击此处查看答案](https://github.com/mdn/css-examples/blob/master/learn/solutions.md#the-box-model)。

#### 使用调试工具来查看盒模型

[浏览器开发者工具](https://developer.mozilla.org/zh-CN/docs/Learn/Common_questions/What_are_browser_developer_tools)可以使你更容易地理解 box 模型。如果你在 Firefox 的 DevTools 中查看一个元素，你可以看到元素的大小以及它的外边距、内边距和边框。这是一个很好的检查元素大小的方式，可以便捷的判断你的盒子大小是否符合预期 !

![Inspecting the box model of an element using Firefox DevTools](box-model-devtools.png)

### 外边距，内边距，边框

您已经在上面的示例中看到了[`margin`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin)、[`padding`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding)和[`border`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border)属性。该示例中使用的是属性的**简写**，允许我们一次设置盒子的四个边。这些简写等价于分别控制盒子的不同边的普通写法。

接下来，我们更详细地研究这些属性：

#### 外边距

外边距是盒子周围一圈看不到的空间。它会把其他元素从盒子旁边推开。外边距属性值可以为正也可以为负。设置负值会导致和其他内容重叠。无论使用标准模型还是替代模型，外边距总是在计算可见部分后额外添加。

我们可以使用[`margin`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin)属性一次控制一个元素的所有边距，或者每边单独使用等价的普通属性控制：

- [`margin-top`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin-top)
- [`margin-right`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin-right)
- [`margin-bottom`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin-bottom)
- [`margin-left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin-left)

**在下面的示例中，尝试更改外边距的值，来查看当前元素和其包含元素，在外边距设置为正时是如何推开周边元素，以及设置为负时，是如何收缩空间的。**

```html
<div class="container">
  <div class="box">Change my margin.</div>
</div>
    
```

```css
.container {
    width: 400px;
    height: 150px;
    border: 5px solid blueviolet;
    margin-top: 100px;
    margin-left: 100px;
}

.box {
    width: 250px;
    height: 100px;
    border: 5px solid mediumpurple;
    background-color: darkgrey;
}

.box {
    margin-top: -40px;
    margin-right: 30px;
    margin-bottom: 40px;
    margin-left: 4em;
}

	
```

#### 外边距折叠

理解外边距的一个关键是外边距折叠的概念。如果你有**两个外边距相接**的元素，这些外边距将合并为一个外边距，即最大的单个外边距的大小。

在下面的例子中，我们有两个段落。顶部段落的页 `margin-bottom`为 50px。第二段的`margin-top` 为 30px。因为外边距折叠的概念，所以框之间的实际外边距是 50px，而不是两个外边距的总和。

**您可以通过将第 2 段的 `margin-top` 设置为 0 来测试它。两个段落之间的可见边距不会改变——它保留了第一个段落 `margin-bottom`设置的 50 像素。**

```html
  <div class="container">
    <p class="box box-one">I am paragraph one.</p>
    <p class="box box-two">I am paragraph two.</p>
  </div>
```

```css
.container {
    width: 700px;
    height: 300px;
    border: 5px solid blueviolet;
    margin-top: 100px;
    margin-left: 100px;
}

.box {
    height: 80px;
    border: 5px solid mediumpurple;
    background-color: darkgrey;
}
.box-one {
    margin-bottom: 50px;
}

.box-two {
    margin-top: 30px;
}


```



![image-20220818094435941](image-20220818094435941.png)

有许多规则规定了什么时候外边距会折叠，什么时候不会折叠。相关更多信息，请参阅[外边距重叠](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Box_Model/Mastering_margin_collapsing)。现在首先要记住的事情是，外边距会折叠这个事情。如果你用外边距创建空间而没有得到你想要的效果，那这可能就是这个原因。



#### 边框

边框是在`padding`和`margin`之间绘制的。如果您正在使用标准的盒模型，边框的大小将添加到框的宽度和高度。如果您使用的是替代盒模型，那么边框的大小会使内容框更小，因为它会占用一些可用的宽度和高度。

为边框设置样式时，有大量的属性可以使用——有四个边框，每个边框都有样式、宽度和颜色，我们可能需要对它们进行操作。

可以使用[`border`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border)属性一次设置所有四个边框的宽度、颜色和样式。

分别设置每边的宽度、颜色和样式，可以使用：

- [`border-top`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-top)
- [`border-right`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-right)
- [`border-bottom`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-bottom)
- [`border-left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-left)

设置所有边的颜色、样式或宽度，请使用以下属性：

- [`border-width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-width)
- [`border-style`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-style)
- [`border-color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-color)

设置单边的颜色、样式或宽度，可以使用最细粒度的普通属性之一：

- [`border-top-width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-top-width)
- [`border-top-style`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-top-style)
- [`border-top-color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-top-color)
- [`border-right-width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-right-width)
- [`border-right-style`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-right-style)
- [`border-right-color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-right-color)
- [`border-bottom-width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-bottom-width)
- [`border-bottom-style`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-bottom-style)
- [`border-bottom-color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-bottom-color)
- [`border-left-width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-left-width)
- [`border-left-style`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-left-style)
- [`border-left-color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-left-color)

**设置边框的颜色、样式或宽度，可以使用最细粒度的普通属性或者简写属性。在下面的示例中，我们使用了各种普通属性或者简写属性来创建边框。尝试一下不同的属性，以检查您是否理解它们是如何工作的。MDN 中的边框属性页面为您提供可用的不同边框样式的信息。**

```html
<div class="container">
  <div class="box">Change my borders.</div>
</div>
    
```

```css
.container {
  border-top: 5px dotted green;
  border-right: 1px solid black;
  border-bottom: 20px double rgb(23,45,145);
}

.box {
  border: 1px solid #333333;
  border-top-style: dotted;
  border-right-width: 20px;
  border-bottom-color: hotpink;
}
    
```

![image-20220818095501037](image-20220818095501037.png)

#### 内边距

内边距位于边框和内容区域之间。与外边距不同，您不能有负数量的内边距，所以值必须是 0 或正的值。应用于元素的任何背景都将显示在内边距后面，内边距通常用于将内容推离边框。

我们可以使用[`padding`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding)简写属性控制元素所有边，或者每边单独使用等价的普通属性：

- [`padding-top`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding-top)
- [`padding-right`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding-right)
- [`padding-bottom`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding-bottom)
- [`padding-left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding-left)

**如果在下面的示例中更改类`.box`的内边距值，您可以看到，这将更改文本开始的位置。**

**您还可以更改类`.container`的内边距，这将在容器和方框之间留出空间。任何元素上的内边距都可以更改，并在其边界和元素内部的任何内容之间留出空间。**

```html
<div class="container">
  <div class="box">Change my padding.</div>
</div>
    
```

```css
.container {
    width: 400px;
    height: 150px;
    border: 5px solid blueviolet;
    margin-top: 100px;
    margin-left: 100px;
}

.box {
    width: 250px;
    height: 100px;
    border: 5px solid mediumpurple;
    background-color: darkgrey;

}

.container {
    padding: 20px;
}

.box {
    padding-top: 0;
    padding-right: 30px;
    padding-bottom: 40px;
    padding-left: 4em;
}



```

![image-20220818100650492](image-20220818100650492.png)

### 盒子模型和内联盒子

以上所有的方法都完全适用于块级盒子。有些属性也可以应用于内联盒子，例如由`<span>`元素创建的那些内联盒子。

在下面的示例中，我们在一个段落中使用了`<span>`，并对其应用了宽度、高度、边距、边框和内边距。可以看到，宽度和高度被忽略了。垂直外边距、内边距和边框是生效的，但它们不会改变其他内容与内联盒子的关系，内边距和边框会与段落中的其他单词重叠。水平内边距、边距和边框将其他内容从盒子中移开。

由于垂直方向不会推开其他元素，当`p`指定较小的长度或者缩放浏览器时，文本会与`span`重叠

```html
<p>
    I am a paragraph and this is a <span>span</span> inside that paragraph. A span is an inline element and so does not respect width and height.
</p>     
    
```

```css
span {
    margin: 20px;
    padding: 20px;
    width: 80px;
    height: 50px;
    background-color: lightblue;
    border: 2px solid blue;
}

p {
    width: 300px;
}
```

![image-20220818101248468](image-20220818101248468.png)

当`p`元素不设置长度时

![image-20220818102516323](image-20220818102516323.png)

### 使用 `display: inline-block`

display 有一个特殊的值，它在内联和块之间提供了一个中间状态。这对于以下情况非常有用：您不希望一个项切换到新行，但希望它可以设定宽度和高度，并避免上面看到的重叠。

一个元素使用 `display: inline-block`，实现我们需要的块级的部分效果：

- 设置`width` 和`height` 属性会生效。
- `padding`, `margin`, 以及`border` 会推开其他元素。

但是，它不会跳转到新行，如果显式添加 `width` 和 `height` 属性，它只会变得比其内容更大。

**在上一个示例中，我们将 `display: inline-block` 添加到 `<span>` 元素中。尝试将此更改为 `display: block` 或完全删除行，以查看显示模型中的差异**。

```css
span {
    margin: 20px;
    padding: 20px;
    width: 80px;
    height: 50px;
    background-color: lightblue;
    border: 2px solid blue;

    display: inline-block;
}

p {
    width: 300px;
}
```

![image-20220818103342939](image-20220818103342939.png)

当您想要通过添加内边距使链接具有更大的命中区域时，这是很有用的。`<a>` 是像 `<span>` 一样的内联元素；你可以使用 `display: inline-block` 来设置内边距，让用户更容易点击链接。

这种情况在导航栏中很常见。下面的导航使用 `flexbox` 显示在一行中，我们为 `<a>` 元素添加了内边距，因为我们希望能够在 `<a>` 在鼠标移动到上面时改变背景色。内边距似乎覆盖了 `<ul>` 元素上的边框。这是因为 `<a>` 是一个内联元素。

使用 `.links-list a` 选择器将 `display: inline-block` 添加到样式规则中，你将看到它是如何通过内边距推开其他元素来修复这个问题的。

```html
<nav>
  <ul class="links-list">
    <li><a href="">Link one</a></li>
    <li><a href="">Link two</a></li>
    <li><a href="">Link three</a></li>
  </ul>
</nav>    
    
```

```css
.links-list a {
    background-color: rgb(179,57,81);
    color: #fff;
    text-decoration: none;
    padding: 1em 2em;

    display: inline-block
}

.links-list a:hover {
    background-color: rgb(66, 28, 40);
    color: #fff;
}

ul {
    display: flex;
    list-style: none;
    border: 1px solid black;
}

nav {
    margin-top: 40px;
}
```

`a`标签未设置`display: inline-block`：

![image-20220818104548247](image-20220818104548247.png)

设置之后：

![image-20220818104703783](image-20220818104703783.png)

### 小结

这就是你需要了解的关于盒子模型的大部分内容。如果以后你发现对于盒模型的布局仍有困惑，你将会回来温故这些内容。

在下一节课中，我们将看看如何使用[背景和边框](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Backgrounds_and_borders)来使你的普通盒子看起来更有趣。



## 背景与边框

在这节课中，我们来看看，使用 CSS 背景和边框来做一些，具有一些创造性的事情。渐变、背景图像和圆角，背景和边框的巧妙运用是 CSS 中许多样式问题的答案。

### CSS 的背景样式

CSS [`background`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background) 属性是我们将在本课中学习的许多普通背景属性的简写。如果您在样式表中发现了一个复杂的背景属性，可能会觉得难以理解，因为可以同时传入这么多值。

```css
.box {
  background: linear-gradient(105deg, rgba(255,255,255,.2) 39%, rgba(51,56,57,1) 96%) center center / 400px 200px no-repeat,
  url(big-star.png) center no-repeat, rebeccapurple;
}

```

在本教程的后面部分，我们将返回到简写的工作方式，但是首先，我们通过分开使用各个普通背景属性的方式，看一下在 CSS 中使用背景可以做哪些不同的事情。

#### 背景颜色

[`background-color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-color) 属性定义了 CSS 中任何元素的背景颜色。属性接受任何有效的`<color>值`。背景色扩展到元素的内容和内边距的下面。

在下面的示例中，我们使用了各种颜色值来为元素盒子添加背景颜色：heading 和[`span`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/span)元素。

```html
<div class="box">
  <h2>Background Colors</h2>
  <p>Try changing the background <span>colors</span>.</p>
</div>
    
```

```css
.box {
  background-color: #567895;
}

h2 {
  background-color: black;
  color: white;
}
span {
  background-color: rgba(255,255,255,.5);
}
    
```

![image-20220818105806528](image-20220818105806528.png)

#### 背景图片

[`background-image`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-image) 属性允许在元素的背景中显示图像。在下面的例子中，我们有两个方框——一个是比方框大的背景图像，另一个是星星的小图像。

这个例子演示了关于背景图像的两种情形。默认情况下，大图不会缩小以适应方框，因此我们只能看到它的一个小角，而小图则是平铺以填充方框。在这种情况下，实际的图像只是单独的一颗星星。

```html
<div class="wrapper">
  <div class="box a"></div>
  <div class="box b"></div>
</div>
    
```

```css
.a {
    background-image: url('https://mdn.github.io/css-examples/learn/backgrounds-borders/balloons.jpg');
}

.b {
    background-image: url('https://mdn.github.io/css-examples/learn/backgrounds-borders/star.png');
}

.box {
    width: 250px;
    height: 100px;
}
```

![image-20220818110429595](image-20220818110429595.png)

**如果除了背景图像外，还指定了背景颜色，则图像将显示在颜色的顶部。尝试向上面的示例添加一个 background-color 属性，看看效果如何。**

```css
.a {
    background-image: url('https://mdn.github.io/css-examples/learn/backgrounds-borders/balloons.jpg');
    background-color: darkgrey;
}

.b {
    background-image: url('https://mdn.github.io/css-examples/learn/backgrounds-borders/star.png');
    background-color: darkgrey;

}

.box {
    width: 250px;
    height: 100px;
}
```



![image-20220818110840742](image-20220818110840742.png)

#### 控制背景平铺

[`background-repeat`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-repeat) 属性用于控制图像的平铺行为。可用的值是：

- `no-repeat` — 不重复。
- `repeat-x` —水平重复。
- `repeat-y` —垂直重复。
- `repeat` — 在两个方向重复。

**在示例中尝试这些值。我们已经将值设置为 no-repeat，因此您将只能看到一个星星。尝试不同的值—repeat-x 和 repeat-y—看看它们的效果如何。**

```html
  <div class="wrapper">
    <div class="box b"></div>
  </div>
```

```css
.b {
    background-image: url('https://mdn.github.io/css-examples/learn/backgrounds-borders/star.png');
    background-repeat: no-repeat;
    border: 1px solid black;
}

.box {
    width: 250px;
    height: 100px;
}
```

![image-20220818111436324](image-20220818111436324.png)

#### 调整背景图像的大小

在上面的例子中，我们有一个很大的图像，由于它比作为背景的元素大，所以最后被裁剪掉了。在这种情况下，我们可以使用 [`background-size`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-size)属性，它可以设置长度或百分比值，来调整图像的大小以适应背景。

你也可以使用关键字：

- `cover` —浏览器将使图像足够大，使它完全覆盖了盒子区，同时仍然保持其高宽比。在这种情况下，有些图像可能会跳出盒子外
- `contain` — 浏览器将使图像的大小适合盒子内。在这种情况下，如果图像的长宽比与盒子的长宽比不同，则可能在图像的任何一边或顶部和底部出现间隙。

在下面的例子中，我使用了上面例子中的大图，并使用长度单位来调整方框内的大小。你可以看到这扭曲了图像。

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My CSS experiment</title>
    <link rel="stylesheet" href="./styles.css">

  </head>
  <body>
  <div class="wrapper">
    <div class="box a"></div>
  </div>

  </body>
</html>

```

```css
.a {
    background-image: url('https://mdn.github.io/css-examples/learn/backgrounds-borders/balloons.jpg');
    background-repeat: no-repeat;
    background-size: 100px 80px ;
    border: 1px solid black;
}

.box {
    width: 250px;
    height: 100px;
}
```

![image-20220818111921726](image-20220818111921726.png)

试试下面：

- 改变用于修改背景大小的长度单位。

- 去掉长度单位，看看使用`background-size: cover` or `background-size: contain`会发生什么。

  `cover`

  ![image-20220818112037989](image-20220818112037989.png)

  `contain`

  ![image-20220818112113617](image-20220818112113617.png)

- 如果您的图像小于盒子，您可以更改 background-repeat 的值来重复图像。

#### 背景图像定位

[`background-position`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-position) 属性允许您选择背景图像显示在其应用到的盒子中的位置。它使用的坐标系中，框的左上角是 (0,0)，框沿着水平 (x) 和垂直 (y) 轴定位。

> **备注：** 默认的背景位置值是 (0,0)。

最常见的背景位置值有两个单独的值——一个水平值后面跟着一个垂直值。

你可以使用像`top`和`right`这样的关键字 (在 [`background-image`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-image) 页面上查找其他的关键字):

```css
.box {
  background-image: url(star.png);
  background-repeat: no-repeat;
  background-position: top center;
}

```

或者使用 [长度值](https://developer.mozilla.org/zh-CN/docs/Web/CSS/length) 和 [百分比](https://developer.mozilla.org/zh-CN/docs/Web/CSS/percentage)：

```css
.box {
  background-image: url(star.png);
  background-repeat: no-repeat;
  background-position: 20px 10%;
}

```

你也可以混合使用关键字，长度值以及百分比，例如：

```css
.box {
  background-image: url(star.png);
  background-repeat: no-repeat;
  background-position: top 20px;
}

```

最后，您还可以使用 4-value 语法来指示到盒子的某些边的距离——在本例中，长度单位是与其前面的值的偏移量。所以在下面的 CSS 中，我们将背景从顶部调整 20px，从右侧调整 10px:

```css
.box {
  background-image: url(star.png);
  background-repeat: no-repeat;
  background-position: top 20px right 10px;
}

```

**使用下面的示例来处理这些值并在框内移动星星。**

```html
  <div class="wrapper">
    <div class="box b"></div>
  </div>
```

```css
.b {
    background-image: url('https://mdn.github.io/css-examples/learn/backgrounds-borders/star.png');
    background-repeat: no-repeat;
    border: 1px solid black;
    background-position: 20px center;
}

.box {
    width: 250px;
    height: 100px;
}
```

![image-20220818112751001](image-20220818112751001.png)

#### 渐变背景

当渐变用于背景时，也可以使用像图像一样的 [`background-image`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-image) 属性设置。

您可以在 MDN 的 [`gradient`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/gradient) 数据类型页面上，了解更多关于渐变的不同类型，以及使用它们可以做的事情。使用渐变的一个有趣方法是，使用 web 上可用的许多 CSS 渐变生成器之一，比如[这个](https://cssgradient.io/)。您可以创建一个渐变，然后复制并粘贴生成它的源代码。

在下面的示例中尝试一些不同的渐变。在这两个盒子里，我们分别有一个线性梯度，它延伸到整个盒子上，还有一个径向梯度，它有一个固定的大小，因此会重复。

```html
  <div class="wrapper">
    <div class="box a"></div>
    <div class="box b"></div>
  </div>
```

```css
.a {
    background-image: linear-gradient(105deg, rgba(0,249,255,1) 39%, rgba(51,56,57,1) 96%);
}

.b {
    background-image: radial-gradient(circle, rgba(0,249,255,1) 39%, rgba(51,56,57,1) 96%);
    background-size: 100px 50px;
}

.box {
    width: 250px;
    height: 100px;
}
```

![image-20220818113139871](image-20220818113139871.png)



#### 多个背景图像

也可以有多个背景图像——在单个属性值中指定多个 `background-image` 值，用逗号分隔每个值。

当你这样做时，你可能会以背景图像互相重叠而告终。背景将与最后列出的背景图像层在堆栈的底部，背景图像在代码列表中最先出现的在顶端。

> **备注：** 渐变可以与常规的背景图像很好地混合在一起。

其它 `background-*` 属性，该属性值用逗号分隔的方式设置。例如下列 `background-image`：

```css
background-image: url(image1.png), url(image2.png), url(image3.png), url(image4.png);
background-repeat: no-repeat, repeat-x, repeat;
background-position: 10px 20px,  top right;

```

不同属性的每个值，将与其他属性中相同位置的值匹配。例如，上面的 image1 的 `background-repeat` 值将是 `no-repeat`。但是，当不同的属性具有不同数量的值时，会发生什么情况呢？答案是较小数量的值会循环—在上面的例子中有四个背景图像，但是只有两个背景位置值。前两个位置值将应用于前两个图像，然后它们将再次循环—image3 将被赋予第一个位置值，image4 将被赋予第二个位置值。

**我们来试一试。在下面的示例中包含了两个图像。为了演示叠加顺序，请尝试切换哪个背景图像在列表中最先出现。或使用其他属性更改位置、大小或重复值。**

```html
  <div class="wrapper">
    <div class="box"></div>
  </div>
```

```css
.box {
    background-image: url('https://mdn.github.io/css-examples/learn/backgrounds-borders/star.png'), url('https://mdn.github.io/css-examples/learn/backgrounds-borders/big-star.png');
}

.box {
    width: 250px;
    height: 100px;
}
```

![image-20220818114600342](image-20220818114600342.png)

#### 背景附加

另一个可供选择的背景是指定他们如何滚动时，内容滚动。这是由 [`background-attachment`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-attachment) 属性控制的，它可以接受以下值：

- `scroll`: 使元素的背景在页面滚动时滚动。如果滚动了元素内容，则背景不会移动。实际上，背景被固定在页面的相同位置，所以它会随着页面的滚动而滚动。
- `fixed`: 使元素的背景固定在视图端口上，这样当页面或元素内容滚动时，它就不会滚动。它将始终保持在屏幕上相同的位置。
- `local`: 这个值是后来添加的 (它只在 Internet Explorer 9+中受支持，而其他的在 IE4+中受支持)，因为滚动值相当混乱，在很多情况下并不能真正实现您想要的功能。局部值将背景固定在设置的元素上，因此当您滚动元素时，背景也随之滚动。

[`background-attachment`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-attachment) 属性只有在有内容要滚动时才会有效果，所以我们做了一个示例来演示这三个值之间的区别——看看 [background-attachment.html](https://mdn.github.io/learning-area/css/styling-boxes/backgrounds/background-attachment.html) (或者看看这儿的 [源代码](https://github.com/mdn/learning-area/tree/master/css/styling-boxes/backgrounds)))。

#### 使用 background 的简写

正如我在本课开始时提到的，您将经常看到使用 [`background`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background) 属性指定的背景。这种简写允许您一次设置所有不同的属性。

如果使用多个背景，则需要为第一个背景指定所有普通属性，然后在逗号后面添加下一个背景。在下面的例子中，我们有一个渐变，它指定大小和位置，然后是一个无重复的图像背景，它指定位置，然后是一个颜色。

这里有一些规则，需要在简写背景属性时遵循，例如：

- `background-color` 只能在逗号之后指定。
- `background-size` 值只能包含在背景位置之后，用'/'字符分隔，例如：`center/80%`。

查看 [`background`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background) 的 MDN 页面，以查看所有的注意事项。

```html
<div class="box"></div>
    
```

```css
.box {
    background:
            linear-gradient(105deg, rgba(255,255,255,.2) 39%, rgba(51,56,57,1) 96%) center center / 400px 200px no-repeat,
            url('https://mdn.github.io/css-examples/learn/backgrounds-borders/big-star.png') center no-repeat,
            rebeccapurple;
    width: 320px;
    height: 100px;
}

```

![image-20220818135017051](image-20220818135017051.png)

#### 背景的可访问性考虑

当你把文字放在背景图片或颜色上面时，你应该注意你有足够的对比度让文字对你的访客来说是清晰易读的。如果指定了一个图像，并且文本将被放置在该图像的顶部，您还应该指定一个`background-color` ，以便在图像未加载时文本也足够清晰。

屏幕阅读者不能解析背景图像，因此背景图片应该只是纯粹的装饰；任何重要的内容都应该是 HTML 页面的一部分，而不是包含在背景中。

### 边框

在学习盒子模型时，我们发现了边框如何影响盒子的大小。在这节课中，我们将看看如何创造性地使用边框。通常，当我们使用 CSS 向元素添加边框时，我们使用一个简写属性在一行 CSS 中设置边框的颜色、宽度和样式。我们可以使用 [`border`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border) 为一个框的所有四个边设置边框。

```css
.box {
  border: 1px solid black;
}

```

或者我们可以只设置盒子的一个边，例如：

```css
.box {
  border-top: 1px solid black;
}

```

这些简写的等价于：

```css
.box {
  border-width: 1px;
  border-style: solid;
  border-color: black;
}

```

也可以使用更加细粒度的属性：

```css
.box {
  border-top-width: 1px;
  border-top-style: solid;
  border-top-color: black;
}

```

> **备注：** 这些顶部、右侧、底部和左侧边框属性还具有与文档写入模式相关的映射逻辑属性 (例如，从左到右或从右到左的文本，或从上到下)。在下一课中，我们将探讨这些问题，这包括处理不同的文本指示 [详情](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Handling_different_text_directions)。

#### 圆角

通过使用 [`border-radius`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-radius) 属性和与方框的每个角相关的长边来实现方框的圆角。可以使用两个长度或百分比作为值，第一个值定义水平半径，第二个值定义垂直半径。在很多情况下，您将只传递一个值，这两个值都将使用。

例如，要使一个盒子的四个角都有 10px 的圆角半径：

```css
.box {
  border-radius: 10px;
}

```

或使右上角的水平半径为 1em，垂直半径为 10％：

```css
.box {
  border-top-right-radius: 1em 10%;
}

```

我们在下面的示例中设置了所有四个角，然后更改右上角的值使之不同。您可以使用这些值来更改圆角样式。查看 [`border-radius`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-radius) 的属性页，查看可用的语法选项。

```html
<div class="box">
  <h2>Borders</h2>
  <p>Try changing the borders.</p>
</div>
    
```

```css
.box {
    border: 10px solid rebeccapurple;
    border-radius: 1em;
    border-top-right-radius: 10% 30%;
    width: 320px;
    height: 100px;
}
    
```

![image-20220818140419765](image-20220818140419765.png)

### 小结

我们在这里已经介绍了很多，您可以看到有很多要添加背景或边框到盒子中。如果您想了解更多关于我们讨论过的特性的信息，请浏览不同的属性页面。MDN 上的每个页面都有更多的用法示例，供您玩转并增强您的知识。

在下一课中，我们将了解文档排版与 CSS 的相互影响。以及了解当文本不是从左向右流动时会发生什么？

## 处理不同方向的文本

目前为止我们在 CSS 学习中遇到的许多属性和属性值与显示器的物理尺度紧密相关。例如，我们会在上、右、下、左设置边框。这些物理尺寸与水平排布的文本相得益彰，并且，默认浏览器对方向从左到右的文本（如英文或法文）的支持，要优于从右到左的文本（如阿拉伯语）的支持。

然而，CSS 在最近几年得到了改进，以更好地支持不同方向的文本，包括从右到左，也包括从上到下的文本（如日文）——这些不同的方向属性被称为书写模式。随着学习的深入，当你开始试着对页面进行布局时，对书写模式的了解将会对你很有帮助，为此我们在这里加以介绍。

### 什么是书写模式

CSS 中的书写模式是指文本的排列方向是横向还是纵向的。[`writing-mode`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/writing-mode) 属性使我们从一种模式切换到另一种模式。为此，你不必使用一种竖向的语言——你还可以更改部分文字的方向以实现创新性的布局。

下面的例子中，我们使用`writing-mode: vertical-rl`对一个标题的显示进行设置。现在，标题文本是竖向的了。竖向文本在平面设计中很常见，也可以为你的网页设计增添更加有趣的外观。

```html
<h1>Play with writing modes</h1>
    
```

```css
h1 {
  writing-mode: vertical-rl;
}
    
```

![image-20220818141711691](image-20220818141711691.png)

[`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/writing-mode)的三个值分别是：

- `horizontal-tb`: 块流向从上至下。对应的文本方向是横向的。
- `vertical-rl`: 块流向从右向左。对应的文本方向是纵向的。
- `vertical-lr`: 块流向从左向右。对应的文本方向是纵向的。

因此，`writing-mode`属性实际上设定的是页面上块级元素的显示方向——要么是从上到下，要么是从右到左，要么是从左到右。而这决定了文本的方向。



### 书写模式、块级布局和内联布局

我们已经讨论了块级布局和内联布局（[block and inline layout](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model#block_and_inline_boxes)），也知道外部显示类型元素分为块级元素和内联元素。如上所述，块级显示和内联显示与文本的书写模式（而非屏幕的物理显示）密切相关。如果你使用书写模式的显示是横向的，如英文，那么块在页面上的显示就是从上到下的。

用一个例子可以更清楚地说明这一点。下一个例子中有两个盒子，分别包含一个标题和一个段落。第一个盒子应用的是`writing-mode: horizontal-tb`，这是一个从上到下的横向的书写模式。第二个盒子应用的是`writing-mode: vertical-rl`，这是一个从右到左的纵向的书写模式。

```html
  <div class="wrapper">
    <div class="box horizontal">
      <h2>Heading</h2>
      <p>A paragraph. Demonstrating Writing Modes in CSS.</p>
    </div>
    <div class="box vertical">
      <h2>Heading</h2>
      <p>A paragraph. Demonstrating Writing Modes in CSS.</p>
    </div>
  </div>

```

```css
.horizontal {
    writing-mode: horizontal-tb;
}

.vertical {
    writing-mode: vertical-rl;
}
    
```

![image-20220818142146875](image-20220818142146875.png)

当我们切换书写模式时，我们也在改变块和内联文本的方向。`horizontal-tb`书写模式下块的方向是从上到下的横向的，而 `vertical-rl`书写模式下块的方向是从右到左的纵向的。因此，块维度指的总是块在页面书写模式下的显示方向。而内联维度指的总是文本方向。

这张图展示了在水平书写模式下的两种维度。

![img](horizontal-tb.png)

这张图片展示了纵向书写模式下的两种维度。

![img](vertical.png)

一旦你开始接触 CSS 布局，尤其是更新的布局方法，这些关于块级元素和内联元素的概念会变得非常重要。我之后会返回来再看。

#### 方向

除了书写模式，我们还可以设置文本方向。正如上面所言，有些语言（如阿拉伯语）是横向书写的，但是是从右向左。当你在对页面布局进行创新时，你可能不这么使用——如果你只是想将某部分内容放到右边排列下来，还有其他方法可以选择——然而，重要的是能意识到，这其实是 CSS 本身功能的一部分。网页可不仅限于从左向右排列的语言！

由于书写模式和文本方向都是可变的，新的 CSS 布局方法不再定义从左到右和从上到下，而是将这些连同内联元素和块级元素的*开头*和*结尾*一起考量。现在不必过于担心，但是带着这些概念开始你的布局，你会发现这对你掌握 CSS 非常有用。

### 逻辑属性和逻辑值

我们之所以要在这里探讨书写模式和方向，是因为目前为止我们已经了解了很多与屏幕的物理显示密切相关的很多属性，而书写模式和方向在水平书写模式下会很有意义。

让我们再来看看那两个盒子——一个用`horizontal-tb`设定了书写模式，一个用`vertical-rl`设定了书写模式。我为这两个盒子分别设定了宽度（ [`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width)）。可以看到，当盒子处于纵向书写模式下时，宽度也发生了变化，从而导致文本超出了盒子的范围。

```html
  <div class="wrapper">
    <div class="box horizontal">
      <h2>Heading</h2>
      <p>A paragraph. Demonstrating Writing Modes in CSS.</p>
      <p>These boxes have a width.</p>
    </div>
    <div class="box vertical">
      <h2>Heading</h2>
      <p>A paragraph. Demonstrating Writing Modes in CSS.</p>
      <p>These boxes have a width.</p>
    </div>
  </div>

```

```css
.box {
    width: 120px;
    border: 1px solid black;
}

.horizontal {
    writing-mode: horizontal-tb;
    margin-right: 100px;
}

.vertical {
    writing-mode: vertical-rl;
}

.wrapper {
    display: flex;
    padding-top: 10px;
}
```

![image-20220818143448702](image-20220818143448702.png)

通过这一些列调整，我们想要的实际上是使宽和高随着书写模式一起变化。当处于纵向书写模式之下时，我们希望盒子可以向横向模式下一样得到拓宽。

为了更容易实现这样的转变，CSS 最近开发了一系列映射属性。这些属性用逻辑（**logical**）和相对变化（**flow relative**）代替了像宽`width`和高`height`一样的物理属性。

横向书写模式下，映射到`width`的属性被称作内联尺寸（[`inline-size`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/inline-size)）——内联维度的尺寸。而映射`height`的属性被称为块级尺寸（[`block-size`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/block-size)），这是块级维度的尺寸。下面的例子展示了替换掉`width`的`inline-size`是如何生效的。

```html
  <div class="wrapper">
    <div class="box horizontal">
      <h2>Heading</h2>
      <p>A paragraph. Demonstrating Writing Modes in CSS.</p>
      <p>These boxes have a width.</p>
    </div>
    <div class="box vertical">
      <h2>Heading</h2>
      <p>A paragraph. Demonstrating Writing Modes in CSS.</p>
      <p>These boxes have a width.</p>
    </div>
  </div>

```

```css
.box {
    inline-size: 120px;
    border: 1px solid black;
}

.horizontal {
    writing-mode: horizontal-tb;
    margin-right: 100px;
}

.vertical {
    writing-mode: vertical-rl;
}

.wrapper {
    display: flex;
    padding-top: 10px;
}
```

![image-20220818143716260](image-20220818143716260.png)

#### 逻辑外边距、边框和内边距属性

我们在前面两节中学习了 CSS 的盒模型和 CSS 边框。在外边距、边框和内边距属性中，你会发现许多物理属性，例如 [`margin-top`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin-top)、 [`padding-left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding-left)和 [`border-bottom`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-bottom)。就像 width 和 height 有映射，这些属性也有相应的映射。

`margin-top`属性的映射是[`margin-block-start`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin-block-start)——总是指向块级维度开始处的边距。

[`padding-left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding-left)属性映射到 [`padding-inline-start`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding-inline-start)，这是应用到内联开始方向（这是该书写模式文本开始的地方）上的内边距。[`border-bottom`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-bottom)属性映射到的是[`border-block-end`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-block-end)，也就是块级维度结尾处的边框。

下面是物理和逻辑属性之间的对比。

**如果你用`writing-mode`把盒子`.box`的书写模式改为`vertical-rl`，你将会看到尽管盒子的物理方向变了，盒子的物理属性仍然没变，然而逻辑属性会随着书写模式一起改变。**

**你还可以看到，二级标题[`h2`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements)有一个黑色的底部边框`border-bottom`。你知道如何使得底部边框无论在那种书写模式下都位于文本的下方吗？**

```html
  <div class="wrapper">
    <div class="box physical">
      <h2>Physical Properties</h2>
      <p>A paragraph. Demonstrating Logical Properties in CSS.</p>
    </div>
    <div class="box logical">
      <h2>Logical Properties</h2>
      <p>A paragraph. Demonstrating Logical Properties in CSS.</p>
    </div>
  </div>

```

```css
.box {
    inline-size: 200px;
    writing-mode: horizontal-tb;
}

.logical {
    margin-block-start: 20px;
    padding-inline-end: 2em;
    padding-block-start: 2px;
    border-block-start: 5px solid pink;
    border-inline-end: 10px dotted rebeccapurple;
    border-block-end: 1em double orange;
    border-inline-start: 1px solid black;
}

.physical {
    margin-top: 20px;
    padding-right: 2em;
    padding-top: 2px;
    border-top: 5px solid pink;
    border-right: 10px dotted rebeccapurple;
    border-bottom: 1em double orange;
    border-left: 1px solid black;
}

h2 {
    border-bottom: 5px solid black;
}

```

![image-20220818144124241](image-20220818144124241.png)

对于每一个普通边距，都有许多属性可以参考，你可以在 MDN 页面（[Logical Properties and Values](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties)）查看所有映射属性。

逻辑属性是通过`inline/block/start/end`来区分方向的

#### 逻辑值

目前为止我们看到的都是逻辑属性的名称。还有一些属性的取值是一些物理值（如`top`、`right`、`bottom`和`left`）。这些值同样拥有逻辑值映射（`block-start`、`inline-end`、`block-end`和`inline-start`）。

例如，你可以将一张图片移到左边，并使文本环绕图片。你可以将`left`替换为`inline-start` ，就像下面的例子中一样。

```html
  <div class="wrapper">
    <div class="box logical">
      <img src="https://mdn.github.io/css-examples/learn/backgrounds-borders/big-star.png" alt="star">
      <p>This box uses logical properties. The star image has been floated inline-start, it also has a margin on the inline-end and block-end.</p>
    </div>
  </div>

```

```css
.box {
    inline-size: 200px;
    writing-mode: horizontal-tb;
}

img{
    float: inline-start;
    margin-inline-end: 10px;
    margin-block-end: 10px;
}

.wrapper {
    border: 1px solid black;
}
```

![image-20220818144845468](image-20220818144845468.png)



**将这个例子的书写模式改为`vertical-rl`，看看图片会发生什么。将`inline-start`改为`inline-end`来改变图片的移动。**

```css
.box {
    inline-size: 200px;
    writing-mode: vertical-rl;
}

img{
    float: inline-start;
    margin-inline-end: 10px;
    margin-block-end: 10px;
}

.wrapper {
    border: 1px solid black;
}
```

![image-20220818145008661](image-20220818145008661.png)

这里我们同样使用逻辑边距值来保证在任何书写模式下边距的位置都是对的。

> **备注：** [`float`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/float)的逻辑值暂时只有 Firefox 和 Firefox for Android 支持，上面的例子可能无法生效。

#### 应该使用物理属性还是逻辑属性呢？

逻辑属性是在物理属性之后出现的，因而最近才开始在浏览器中应用。你可以通过查看 MDN 的属性页面来了解浏览器对逻辑属性的支持情况。如果你并没有应用多种书写模式，那么现在你可能更倾向于**使用物理属性**，因为这些在你使用弹性布局和网格布局时非常有用。

### 小结

本章介绍的概念在 CSS 的重要性越来越大。了解块级方向和内联方向，以及文本的排列方向如何随书写模式发生变化，将来会非常有用。即便你仅使用横向的书写模式，这也能帮助你了解。

在下一部分，我们将会看一下 CSS 中的溢出。

## 内容溢出

本节课，我们来了解一下 CSS 中另外一个重要的概念——**溢出**。溢出是在盒子无法容纳下太多的内容的时候发生的。在这篇教程里面，你将会学习到什么是溢出，以及如何控制它。

### 什么是溢出？

我们知道，CSS 中万物皆盒，因此我们可以通过给[`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width)和[`height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/height)（或者 [`inline-size`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/inline-size) 和 [`block-size`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/block-size)）赋值的方式来约束盒子的尺寸。溢出是在你往盒子里面塞太多东西的时候发生的，所以盒子里面的东西也不会老老实实待着。CSS 给了你好几种工具来控制溢出，在学习的早期理解这些概念是很有用的。在你写 CSS 的时候你经常会遇到溢出的情形，尤其是当你以后更加深入到 CSS 布局的时候。

### CSS 尽力减少“数据损失”

我们从两个展示了在碰到溢出的时候，CSS 默认会如何处理的例子开始吧。

第一个例子是，一个盒子，在块方向上已经受到`height`的限制。然后我们已经加了过多的内容，以至于盒子里面没有空间容纳。内容正在从盒子里面溢出，并让自己把盒子下面的段落弄得一团糟。

```html
<div class="box">This box has a height and a width. This means that if there is too much content to be displayed within the assigned height, there will be an overflow situation. If overflow is set to hidden then any overflow will not be visible.</div>

<p>This content is outside of the box.</p>
    
```

```css
.box {
  border: 1px solid #333333;
  width: 200px;
  height: 100px;
}
    
```

![image-20220818145926784](image-20220818145926784.png)

第二个例子是一个单词，位于在内联方向上受到限制的盒子里面。盒子已经被做得小到无法放置那个单词的地步，于是那个单词就突破了盒子的限制。

```html
<div class="word">Overflow</div>

```

```css
.word {
  border: 1px solid #333333;
  width: 100px;
  font-size: 250%;
}
    
```

![image-20220818150042273](image-20220818150042273.png)

你也许会好奇，为什么 CSS 默认会采取如此不整洁的方式，让内容这么凌乱地溢出出来呢？为何不把多余的内容隐藏起来，或者让盒子变大呢？

只要有可能，CSS 就不会隐藏你的内容，隐藏引起的数据损失通常会造成困扰。在 CSS 的术语里面，这会导致一些内容消失，你的访客可能不会注意到这一点，如果消失的是表格上的提交按钮，没有人能填完这个表格，这是很麻烦的事情！所以 CSS 反而会把它以可见的形式溢出出去。这样做的结果就是，你会看到错误的 CSS 导致的一片混乱，或者最坏的情况也只是你的网站的访客会告诉你有些内容冒了出来，你的网站需要修缮。

如果你已经用`width`或者`height`限制住了一个盒子，CSS 假定，你知道你在做什么，而且你已经控制住了溢出的隐患。总之，在盒子里面需要放置文本的时候，限制住块方向的尺寸是会引起问题的，因为可能会有比你在设计网站的时候所预计的文本更多的文本，或者文本变大了——比如用户增加字体大小的时候。

在下面的几节课里，我们会看一下各种不同的控制尺寸的方式，以减少溢出的影响。但是，如果你需要固定的尺寸，你也可以控制溢出表现的形式。那么让我们接着读下去吧！

### overflow 属性

[`overflow`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/overflow)属性是你控制一个元素溢出的方式，它告诉浏览器你想怎样处理溢出。`overflow`的默认值为`visible`，这就是我们的内容溢出的时候，我们在默认情况下看到它们的原因。

如果你想在内容溢出的时候把它裁剪掉，你可以在你的盒子上设置`overflow: hidden`。这就会像它表面上所显示的那样作用——隐藏掉溢出。这可能会很自然地让东西消失掉，所以你只应该在判断隐藏内容不会引起问题的时候这样做。

```html
<div class="box">This box has a height and a width. This means that if there is too much content to be displayed within the assigned height, there will be an overflow situation. If overflow is set to hidden then any overflow will not be visible.</div>

<p>This content is outside of the box.</p>
    
```

```css
.box {
  border: 1px solid #333333;
  width: 200px;
  height: 100px;
  overflow: hidden;
}
    
```

![image-20220818150416726](image-20220818150416726.png)

也许你还会想在有内容溢出的时候加个滚动条？如果你用了`overflow: scroll`，那么你的浏览器总会显示滚动条，即使没有足够多引起溢出的内容。你可能会需要这样的样式，它避免了滚动条在内容变化的时候出现和消失。

```css
.box {
  border: 1px solid #333333;
  width: 200px;
  height: 100px;
  overflow: scroll;
}
    
```

![image-20220818150601051](image-20220818150601051.png)

**如果你移除了下面的盒子里的一些内容，你可以看一下，滚动条是否还会在没有能滚动的东西的时候保留。**

```html
  <div class="box">This box has a height and a width. </div>

  <p>This content is outside of the box.</p>

```

![image-20220818150634699](image-20220818150634699.png)

在以上的例子里面，我们仅仅需要在`y`轴方向上滚动，但是我们在两个方向上都有了滚动条。你可以使用[`overflow-y`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/overflow-y)属性，设置`overflow-y: scroll`来仅在`y`轴方向滚动。

```css
.box {
  border: 1px solid #333333;
  width: 200px;
  height: 100px;
  overflow: scroll;
}
    
```

![image-20220818150748161](image-20220818150748161.png)

你也可以用[`overflow-x`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/overflow-x)，以在 x 轴方向上滚动，尽管这不是处理长英文词的好办法！如果你真的需要在小盒子里面和长英文词打交道，那么你可能要了解一下[`word-break`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/word-break)或者[`overflow-wrap`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/overflow-wrap)属性。除此以外，一些[在 CSS 里面调整大小](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Sizing_items_in_CSS)这节课里面讨论过的方式可能会帮助你创建可以和有变化容量的内容相协调的盒子。

```html
<div class="word">Overflow</div>
    
```

```css
.word {
  border: 5px solid #333333;
  width: 100px;
  font-size: 250%;
  overflow-x: scroll;
}
    
```

![image-20220819082617868](image-20220819082617868.png)

和`scroll`一样，在无论是否有多到需要 用滚动条的内容的时候，页面上都会显示一个滚动条。

> **备注：** 你可以用`overflow`属性指定 x 轴和 y 轴方向的滚动，同时使用两个值进行传递。如果指定了两个关键字，第一个对`overflow-x`生效而第二个对`overflow-y`生效。否则，`overflow-x`和`overflow-y`将会被设置成同样的值。例如，`overflow: scroll hidden`会把`overflow-x`设置成`scroll`，而`overflow-y`则为`hidden`。

如果你只是想让滚动条在有比盒子所能装下更多的内容的时候才显示，那么使用`overflow: auto`。此时由浏览器决定是否显示滚动条。桌面浏览器一般仅仅会在有足以引起溢出的内容的时候这么做。

### 溢出建立了块级排版上下文

CSS 中有所谓**块级排版上下文**（Block Formatting Context，BFC）**的概念**。现在你不用太过在意，但是你应该知道，在你使用诸如`scroll`或者`auto`的时候，你就建立了一个块级排版上下文。结果就是，你改变了`overflow`的值的话，对应的盒子就变成了更加小巧的状态。在容器之外的东西没法混进容器内，也没有东西可以突出盒子，进入周围的版面。激活了滚动动作，你的盒子里面所有的内容会被收纳，而且不会遮到页面上其他的物件，于是就产生了一个协调的滚动体验。

### 网页设计时不需要的溢出

现代网页布局的方式（正如[CSS layout](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout)模块中所介绍的那些）可以很好地处理溢出。我们不一定能预料到网页上会有多少内容，人们很好地设计它们，使得它们能与这种现状协调。但是在以往，开发者会更多地使用固定高度，尽力让毫无关联的盒子的底部对齐。这是很脆弱的，在旧时的应用里面，你偶尔会遇到一些盒子，它们的内容遮到了页面上的其他内容。如果你看到了，那么你现在应该知道，这就是溢出，理论上你应该能重新排布这些布局，使得它不必依赖于盒子尺寸的调整。

在开发网站的时候，你应该一直把溢出的问题挂在心头，你应该用或多或少的内容测试设计，增加文本的字号，确保你的 CSS 可以正常地协调。改变溢出属性的值，来隐藏内容或者增加滚动条，会是你仅仅在少数特别情况下需要的，例如在你确实需要一个可滚动盒子的时候。

### 小结

这节短短的课已经介绍了溢出的概念，你现在明白，CSS 会尽力不让溢出的内容不可见，因为这会造成数据损失。你已经发现，你可以控制住潜在的溢出，同样，你也应该测试你的作品，确保你不会一下子就弄出令人困扰的溢出。

## CSS 的值与单位

CSS 中使用的每个属性都允许拥有一个或一组值，查看 MDN 上的任何属性页将帮助您理解对任何特定属性有效的值。在本节课中，我们将学习一些最常用的值和单位。

### 什么是 CSS 的值？

在 CSS 规范和 MDN 的属性页上，您将能够发现值的存在，因为它们将被尖括号包围，如`<color>`或`<length>`。当您看到值`<color>`对特定属性有效时，这意味着您可以使用任何有效的颜色作为该属性的值，如 [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value)参考页面所列。	

> **备注：** 您还将看到被称为数据类型的 CSS 值。这些术语基本上是可以互换的——当你在 CSS 中看到一些被称为数据类型的东西时，它实际上只是一种表示值的奇特方式。
>
> **备注：** 是的，CSS 值倾向于使用尖括号表示，以区别于 CSS 属性 (例如[`color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/color)属性和 [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value) 数据类型)。您可能还会混淆 CSS 数据类型和 HTML 元素，因为它们都使用尖括号，但这不太可能——它们在完全不一样的上下文中使用。

在下面的例子中，我们使用关键字设置标题的颜色，使用`rgb()`函数设置背景：

```css
h1 {
  color: black;
  background-color: rgb(197,93,161);
}

```

CSS 中的值是一种定义允许子值集合的方法。这意味着如果您看到`<color>`是有效的，那么您就不需要考虑可以使用哪些不同类型的颜色值—关键字、十六进制值、`rgb()`函数等等。假设浏览器支持这些可用的`<color>`值，则可以使用它们任意一个。MDN 上针对每个值的页面将提供有关浏览器支持的信息。例如，如果您查看 [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value)的页面，您将看到浏览器兼容性部分列出了不同类型的颜色值以及对它们的支持。

让我们来看看您可能经常遇到的一些值和单位类型，并提供一些示例，以便您尝试使用各种值的可能性。

### 数字，长度和百分比

您可能会发现自己在 CSS 中使用了各种数值数据类型。以下全部归类为数值：

| 数值类型                                                     | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/integer) | [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/integer)是一个整数，比如 1024 或 -55。 |
| [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/number) | [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/number)表示一个小数——它可能有小数点后面的部分，也可能没有，例如 0.255、128 或 -1.2。 |
| `<dimension>`                                                | `<dimension>`是一个`<number>`，它有一个附加的单位，例如 45deg、5s 或 10px。`<dimension>`是一个伞形类别，包括`<length>`、`<angle>`、`<time>`和`<resolution>`类型。 |
| [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/percentage) | [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/percentage)表示一些其他值的一部分，例如 50%。百分比值总是相对于另一个量，例如，一个元素的长度相对于其父元素的长度。 |

#### 长度

以下都是绝对长度单位——它们与其他任何东西都没有关系，通常被认为总是相同的大小。

| 单位 | 名称         | 等价换算            |
| :--- | :----------- | :------------------ |
| `cm` | 厘米         | 1cm = 96px/2.54     |
| `mm` | 毫米         | 1mm = 1/10th of 1cm |
| `Q`  | 四分之一毫米 | 1Q = 1/40th of 1cm  |
| `in` | 英寸         | 1in = 2.54cm = 96px |
| `pc` | 十二点活字   | 1pc = 1/6th of 1in  |
| `pt` | 点           | 1pt = 1/72th of 1in |
| `px` | 像素         | 1px = 1/96th of 1in |

这些值中的大多数在用于打印时比用于屏幕输出时更有用。例如，我们通常不会在屏幕上使用 cm。

惟一一个您经常使用的值，估计就是 px(像素)。

#### 相对长度单位

| 单位   | 相对于                                                       |
| :----- | :----------------------------------------------------------- |
| `em`   | 在 font-size 中使用是相对于父元素的字体大小，在其他属性中使用是相对于自身的字体大小，如 width |
| `ex`   | 字符“x”的高度                                                |
| `ch`   | 数字“0”的宽度                                                |
| `rem`  | 根元素的字体大小                                             |
| `lh`   | 元素的 line-height                                           |
| `vw`   | 视窗宽度的 1%                                                |
| `vh`   | 视窗高度的 1%                                                |
| `vmin` | 视窗较小尺寸的 1%                                            |
| `vmax` | 视图大尺寸的 1%                                              |

#### 探索一个例子

在下面的示例中，您可以看到一些相对长度单位和绝对长度单位的行为。第一个框以像素为单位设置[`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width)。作为一个绝对单位，这个宽度将保持不变，无论其他如何变化。

第二个框的宽度设置为`vw`(视口宽度) 单位。这个值相对于视口宽度，所以 10`vw`是视口宽度的 10%。如果您更改浏览器窗口的宽度，那么框的大小应该会更改。

第三个盒子使用 em 单位。这些是相对于字体大小的。我在包含[`<div>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/div)的元素上设置了一个 1em 的字体大小，它有一个`.wrapper`类。将这个值更改为 1.5em，您将看到所有元素的字体大小都增加了，但是只有最后一项会变宽，因为宽度与字体大小有关。

按照上面的说明操作之后，尝试以其他方式处理这些值，看看您将收获什么。

```html
  <div class="wrapper">
    <div class="box px">I am 200px wide</div>
    <div class="box vw">I am 10vw wide</div>
    <div class="box em">I am 10em wide</div>
  </div>
```

```css
.wrapper {
    font-size: 1em;
}

.px {
    width: 200px;
}

.vw {
    width: 10vw;
}

.em {
    width: 10em;
}

.box {
    border: 2px solid black;
    background-color: darkorange;
}
```

![image-20220819085618437](image-20220819085618437.png)

#### ems and rems

`em`和`rem`是您在从框到文本调整大小时最常遇到的两个相对长度。了解这些方法是如何工作的以及它们之间的区别是很有意义的，尤其是当您开始学习更复杂的主题时，比如样式化文本或 CSS 布局。下面的示例提供了一个演示。

HTML 是一组嵌套的列表—我们总共有三个列表，并且两个示例都有相同的 HTML。唯一的区别是第一个类具有 ems，第二个类具有 rems。

首先，我们将 16px 设置为`<html>`元素的字体大小。

概括地说，在排版属性中 em 单位的意思是“父元素的字体大小”。带有 ems 类的[`<ul>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/ul)内的[`<li>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/li)元素从它们的父元素中获取大小。因此，每一个连续的嵌套级别都会逐渐变大，因为每个嵌套的字体大小都被设置为 1.3em—是其父嵌套字体大小的 1.3 倍。

概括地说，rem 单位的意思是“根元素的字体大小”。(“根 em”的 rem 标准。)`<ul>`内`<li>`的元素和一个 rems 类从根元素 (`<html>)`中获取它们的大小。这意味着每一个连续的嵌套层都不会不断变大。

但是，如果您在 CSS 中更改`<html>`字体大小，您将看到所有其他相关内容都发生了更改，包括 rem 和 em 大小的文本。

```html
<ul class="ems">
  <li>One</li>
  <li>Two</li>
  <li>Three
    <ul>
      <li>Three A</li>
      <li>Three B
        <ul>
          <li>Three B 2</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<ul class="rems">
  <li>One</li>
  <li>Two</li>
  <li>Three
    <ul>
      <li>Three A</li>
      <li>Three B
        <ul>
          <li>Three B 2</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>
    
```

```css
html {
  font-size: 16px;
}

.ems li {
  font-size: 1.3em;
}

.rems li {
  font-size: 1.3rem;
}

```

![image-20220819090503088](image-20220819090503088.png)

#### 百分比

在许多情况下，百分比与长度的处理方法是一样的。百分比的问题在于，它们总是相对于其他值设置的。例如，如果将元素的字体大小设置为百分比，那么它将是元素父元素字体大小的百分比。如果使用百分比作为宽度值，那么它将是父值宽度的百分比。

在下面的示例中，两个百分比大小的框和两个像素大小的框具有相同的类名。分别为 200px 和 40% 宽。

不同之处在于，第二组两个框位于一个 400 像素宽的包装器中。第二个 200px 宽的盒子和第一个一样宽，但是第二个 40% 的盒子现在是 400px 的 40%——比第一个窄多了！

尝试更改包装器的宽度或百分比值，看看这是如何工作的。

```html
<div class="box px">I am 200px wide</div>
<div class="box percent">I am 40% wide</div>
<div class="wrapper">
  <div class="box px">I am 200px wide</div>
  <div class="box percent">I am 40% wide</div>
</div>
    
```

```css
.wrapper {
    width: 400px;
    border: 5px solid rebeccapurple;
}

.px {
    width: 200px;
}

.percent {
    width: 40%;
}

.box {
    border: 5px solid cornflowerblue;
}
```

![image-20220819091149426](image-20220819091149426.png)

下一个示例以百分比设置字体大小。每个`<li>`都有 80% 的字体大小，因此嵌套列表项在从父级继承其大小时将逐渐变小。

```html
<ul>
  <li>One</li>
  <li>Two</li>
  <li>Three
    <ul>
      <li>Three A</li>
      <li>Three B
        <ul>
          <li>Three B 2</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>  

    
```

```css
li {
  font-size: 80%;
}
    
```

![image-20220819091339930](image-20220819091339930.png)

注意，虽然许多值接受长度或百分比，但也有一些值只接受长度。您可以在 MDN 属性引用页面上看到它能接受哪些值。如果允许的值包括`<length-percent>`，则可以使用长度或百分比。如果允许的值只包含`<length>`，则不可能使用百分比。



#### 数字

有些值接受数字，不添加任何单位。接受无单位数字的属性的一个例子是不透明度属性（`opacity` ），它控制元素的不透明度 (它的透明程度)。此属性接受 0(完全透明) 和 1(完全不透明) 之间的数字。

在下面的示例中，尝试将不透明度值更改为 0 到 1 之间的各种小数值，并查看框及其内容是如何变得透明或者不透明的。

```html
<div class="wrapper">
  <div class="box">I am a box with opacity</div>
</div> 
    
```

```css
.box {
  opacity: 0.6;
}
    
```

![image-20220819091801651](image-20220819091801651.png)

> **备注：** 当您在 CSS 中使用数字作为值时，它不应该用引号括起来。

#### 补充

- 像素
  - 屏幕（显示器）实际上是由一个一个小点点构成的
  - 不同屏幕的像素大小是不同的，像素越小的屏幕，显示效果越清晰
  - 所有同样的200px在不同的设备下显示效果不一样
- 百分比
  - 也可以降属性值设置为相对于其父元素属性的百分比
  - 设置 百分比可以使子元素跟随父元素的改变而改变
- em
  - em是相对于元素的字体大小来计算的
  - 1em = 1fontsize
  - em会根据字体大小的改变而改变
- rem
  - rem是相对于根元素的字体大小来计算

### 颜色

在 CSS 中指定颜色的方法有很多，其中一些是最近才实现的。在 CSS 中，相同的颜色值可以在任何地方使用，无论您指定的是文本颜色、背景颜色还是其他颜色。

现代计算机的标准颜色系统是 24 位的，它允许通过不同的红、绿、蓝通道的组合显示大约 1670 万种不同的颜色，每个通道有 256 个不同的值 (256 x 256 x 256 = 16,777,216)。让我们来看看在 CSS 中指定颜色的一些方法。

> **备注：** 在本教程中，我们将研究具有良好浏览器支持的常用指定颜色的方法；虽然还有其他的，但是他们没有很好的支持，也不太常见。

#### 颜色关键词

在这学习示例或 MDN 上的其他示例中，您经常会看到使用的颜色关键字，因为它们是一种指定颜色的简单易懂的方式。有一些关键词，其中一些有相当有趣的名字！您可以在页面上看到 [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value)值的完整列表。

**在下面的示例中尝试使用不同的颜色值，以了解它们是如何工作的。**

#### 十六进制 RGB 值

您可能遇到的下一种颜色值类型是十六进制代码。每个十六进制值由一个散列/磅符号 (#) 和六个十六进制数字组成，每个十六进制数字都可以取 0 到 f(代表 15) 之间的 16 个值中的一个——所以是 0123456789abcdef。每对值表示一个通道—红色、绿色和蓝色—并允许我们为每个通道指定 256 个可用值中的任意一个 (16 x 16 = 256)。

这些值有点复杂，不太容易理解，但是它们比关键字更通用——您可以使用十六进制值来表示您想在配色方案中使用的任何颜色。

```html
<div class="wrapper">
  <div class="box one">#02798b</div>
  <div class="box two">#c55da1</div>
  <div class="box three">#128a7d</div>
</div>
    
```

```css
.one {
    background-color: #02798b;
}

.two {
    background-color: #c55da1;
}

.three {
    background-color: #128a7d;
}


.box {
    width: 320px;
    height: 100px;
    border-radius: 10px;
    margin: 20px;
    text-align: center;
    line-height: 100px;
    vertical-align: middle;
}
```

![image-20220819092201269](image-20220819092201269.png)

**同样，大胆尝试更改值，看看颜色如何变化吧！**

#### RGB 和 RGBA 的值

我们将在这里讨论的第三种方案是 RGB。RGB 值是一个函数—RGB()—它有三个参数，表示颜色的红色、绿色和蓝色通道值，与十六进制值的方法非常相似。RGB 的不同之处在于，每个通道不是由两个十六进制数字表示的，而是由一个介于 0 到 255 之间的十进制数字表示的——这有点容易理解。

让我们重写上一个例子，使用 RGB 颜色：

```html
  <div class="wrapper">
    <div class="box one">rgb(2, 121, 139)</div>
    <div class="box two">rgb(197, 93, 161)</div>
    <div class="box three">rgb(18, 138, 125)</div>
  </div>


```

```css
.one {
    background-color: rgb(2, 121, 139);
}

.two {
    background-color: rgb(197, 93, 161);
}

.three {
    background-color: rgb(18, 138, 125);
}


.box {
    width: 320px;
    height: 100px;
    border-radius: 10px;
    margin: 20px;
    text-align: center;
    line-height: 100px;
    vertical-align: middle;
}
```

![image-20220819092340839](image-20220819092340839.png)

您还可以使用 RGBA 颜色——它们的工作方式与 RGB 颜色完全相同，因此您可以使用任何 RGB 值，但是有第四个值表示颜色的 alpha 通道，它控制不透明度。如果将这个值设置为`0`，它将使颜色完全透明，而设置为`1`将使颜色完全不透明。介于两者之间的值提供了不同级别的透明度。

> **备注：** 在颜色上设置 alpha 通道与使用我们前面看到的[`opacity`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/opacity)属性有一个关键区别。当你使用不透明度时，你让元素和它里面的所有东西都不透明，而使用 RGBA 颜色只让你指定的颜色不透明。

在下面的例子中，我添加了一个背景图片到我们的彩色方块的包含块中。然后我设置了不同的不透明度值——注意当 alpha 通道值较小时，背景如何显示的。

```html
<div class="wrapper">
  <div class="box one">rgba(2, 121, 139, .3)</div>
  <div class="box two">rgba(197, 93, 161, .7)</div>
  <div class="box three">rgba(18, 138, 125, .9)</div>
</div>
    
```

```css
.one {
    background-color: rgba(2, 121, 139, .3);
}

.two {
    background-color: rgba(197, 93, 161, .7);
}

.three {
    background-color: rgba(18, 138, 125, .9);
}

body {
    background-image: url("https://mdn.github.io/css-examples/learn/values-units/balloons.jpg");
}

.box {
    width: 320px;
    height: 100px;
    border-radius: 10px;
    margin: 20px;
    text-align: center;
    line-height: 100px;
    vertical-align: middle;
}
```

![image-20220819092801835](image-20220819092801835.png)

**在本例中，尝试更改 alpha 通道值，看看它如何影响颜色输出。**

> **备注：** 在某种程度上，现代浏览器得到了更新，从而让`rgba()` 和`rgb()` （以及 `hsl()`和 `hsla()`;见下文）成为彼此的纯别名并开始表现完全相同，因此`rgba()` 和`rgb()` 接受带有和不带有 alpha 通道值的颜色。尝试将上面示例的`rgba()` 函数更改为`rgb()` ，看看颜色是否仍然有效！使用哪种样式由您决定，但是将非透明和透明的颜色定义分开使用不同的功能可以（非常）更好地支持浏览器，并且可以直观地指示代码中定义透明颜色的位置。

#### HSL 和 HSLA 的值

与 RGB 相比，HSL 颜色模型的支持稍差一些 (在旧版本的 IE 中不支持)，它是在设计师们感兴趣之后实现的。`hsl()` 函数接受色调、饱和度和亮度值作为参数，而不是红色、绿色和蓝色值，这些值的不同方式组合，可以区分 1670 万种颜色：

- **色调**：颜色的底色。这个值在 0 和 360 之间，表示色轮周围的角度。
- **饱和度**：颜色有多饱和？它的值为 0 - 100%，其中 0 为无颜色 (它将显示为灰色阴影)，100% 为全色饱和度
- **亮度**：颜色有多亮？它从 0 - 100% 中获取一个值，其中 0 表示没有光 (它将完全显示为黑色)，100% 表示完全亮 (它将完全显示为白色)

我们可以更新 RGB 的例子来使用 HSL 颜色，就像这样：

```html
  <div class="wrapper">
    <div class="box one">hsl(188, 97%, 28%)</div>
    <div class="box two">hsl(321, 47%, 57%)</div>
    <div class="box three">hsl(174, 77%, 31%)</div>
  </div>


```

```css
.one {
    background-color: hsl(188, 97%, 28%);
}

.two {
    background-color: hsl(321, 47%, 57%);
}

.three {
    background-color: hsl(174, 77%, 31%);
}

.box {
    width: 320px;
    height: 100px;
    border-radius: 10px;
    margin: 20px;
    text-align: center;
    line-height: 100px;
    vertical-align: middle;
}
```

![image-20220819093115747](image-20220819093115747.png)

就像 RGB 有 RGBA 一样，HSL 也有 HSLA 等效物，它使您能够指定 alpha 通道值。我已经在下面通过将 RGBA 示例更改为使用 HSLA 颜色来演示了这一点。

```html
<div class="wrapper">
  <div class="box one">hsla(188, 97%, 28%, .3)</div>
  <div class="box two">hsla(321, 47%, 57%, .7)</div>
  <div class="box three">hsla(174, 77%, 31%, .9)</div>
</div>
    
```

```css
.one {
    background-color: hsla(188, 97%, 28%, .3);
}

.two {
    background-color: hsla(321, 47%, 57%, .7);
}

.three {
    background-color: hsla(174, 77%, 31%, .9);
}


body {
    background-image: url("https://mdn.github.io/css-examples/learn/values-units/balloons.jpg");
}

.box {
    width: 320px;
    height: 100px;
    border-radius: 10px;
    margin: 20px;
    text-align: center;
    line-height: 100px;
    vertical-align: middle;
}
```

![image-20220819093224722](image-20220819093224722.png)

您可以在项目中使用这些颜色值中的任何一个。对于大多数项目，您可能会选择一个调色板，然后在整个项目中使用这些颜色——以及您所选择的定义这些颜色的方法。你可以混合使用不同的颜色模型，但是为了一致性，通常最好是你的整个项目使用相同的一个！

#### 补充

- 在css中可以直接使用颜色名，来设置各种颜色
  - 比如：red、orange、yellow...
  - 但是在css中直接使用颜色是非常的不方便
- RGB值
  - RGB通过三种颜色的不同浓度来调配出不同的颜色
  - 每一种颜色在0~255之间
  - 语法：rgb(红,绿,蓝)
- RGBA：
  - 在RGB基础上增加了不透明度
  - 1表示完全不透明，0表示完全透明，0.5表示半透明（0可以省略）
- 十六进制的RGB值
  - 颜色浓度：00~ff
  - 如果颜色两位两位重复，可以简写：#aabbcc---->#abc
- HLS
  - H（色相：0 ~ 360）
  - S（饱和度，颜色的浓度：0% ~ 100%）
  - L（亮度，颜色的亮度：0% ~ 100%）

### 图片

[`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/image) 数据类型用于图像为有效值的任何地方。它可以是一个通过 `url()`函数指向的实际图像文件，也可以是一个渐变。

在下面的例子中，我们演示了一个图像和一个渐变作为 CSS `background-image`属性的值。

```html
<div class="box image"></div>
<div class="box gradient"></div>  
    
```

```css
.image {
  background-image: url(star.png);
}

.gradient {
  background-image: linear-gradient(90deg, rgba(119,0,255,1) 39%, rgba(0,212,255,1) 100%);
}
    
```

![image-20220819093803432](image-20220819093803432.png)

> **备注：** `<image>`还有一些其他可能的值，但是这些都是较新的，并且目前对浏览器的支持很差。如果您想了解`<image>`数据类型，请查看 MDN 页面。

### 位置

[`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/position_value) 数据类型表示一组 2D 坐标，用于定位一个元素，如背景图像 (通过 [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/background-position))。它可以使用关键字 (如 `top`, `left`, `bottom`, `right`, 以及`center` ) 将元素与 2D 框的特定边界对齐，以及表示框的顶部和左侧边缘偏移量的长度。

一个典型的位置值由两个值组成——第一个值水平地设置位置，第二个值垂直地设置位置。如果只指定一个轴的值，另一个轴将默认为 `center`。

在下面的示例中，我们使用关键字将背景图像从容器的顶部到右侧放置了 40px。

```html
<div class="box"></div> 
    
```

```css
.box {
  height: 300px;
  width: 400px;
  background-image: url(star.png);
  background-repeat: no-repeat;
  background-position: right 40px;
}
    
```

![image-20220819094156883](image-20220819094156883.png)

**尝试使用这些值，看看如何把这些图像移来移去。**

### 字符串和标识符

在上面的示例中，我们看到关键字被用作值的地方 (例如`<color>`关键字，如 `red`, `black`, `rebeccapurple`, and `goldenrod`)。这些关键字被更准确地描述为标识符，一个 CSS 可以理解的特殊值。因此它们没有使用引号括起来——它们不被当作字符串。

在某些地方可以使用 CSS 中的字符串，例如 [在指定生成的内容时](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Pseudo-classes_and_pseudo-elements#generating_content_with_before_and_after)。在本例中，引用该值以证明它是一个字符串。在下面的示例中，我们使用非引号括起来的颜色关键字和引号括起来的内容字符串。

```html
<div class="box"></div> 
    
```

```css
.box {
  width:400px;
  padding: 1em;
  border-radius: .5em;
  border: 5px solid rebeccapurple;
  background-color: lightblue;
}

.box::after {
  content: "This is a string. I know because it is quoted in the CSS."
}
    
```

![image-20220819094521123](image-20220819094521123.png)

### 函数

我们将查看的最后一种类型的值是一组称为函数的值。在编程中，函数是一段可重用的代码，可以多次运行，以完成重复的任务，对开发人员和计算机都是如此。函数通常与 JavaScript、Python 或 c++等语言相关联，但它们也以属性值的形式存在于 CSS 中。我们已经在颜色部分看到了函数的作用——`rgb()`、`hsl()`等。用于从文件返回图像的值——`url()`——也是一个函数。

行为更类似于传统编程语言的值是`calc()`函数。这个函数使您能够在 CSS 中进行简单的计算。如果您希望计算出在为项目编写 CSS 时无法定义的值，并且需要浏览器在运行时为您计算出这些值，那么它特别有用。

例如，下面我们使用`calc()`使框宽为 20% + 100px。20% 是根据父容器.wrapper 的宽度来计算的，因此如果宽度改变，它也会改变。我们不能事先做这个计算，因为我们不知道父类的 20% 是多少，所以我们使用`calc()`来告诉浏览器为我们做这个计算。

```html
<div class="wrapper">
  <div class="box">My width is calculated.</div> 
</div>
    
```

```css
.wrapper {
    width: 90vw;
    border-radius: .5em;
    border: 5px solid rebeccapurple;
}

.box {
    width: calc(20% + 100px);
    background-color: lightblue;

}

```

![image-20220819095011974](image-20220819095011974.png)

**尝试拖动浏览器查看**

### 小结

本文简要介绍了您可能会遇到的最常见的值和单位类型。你可以看看所有不同类型的 [CSS 的值和单位](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units) 参考页面；当你学习这些课程时，你将会遇到很多这样的情况。

需要记住的关键一点是，每个属性都有一个已定义的允许值列表，每个值都有一个定义来解释子值是什么。然后您可以在 MDN 上查看详细信息。

## 在 CSS 中调整大小

在前面的课程中你已经看到了几种使用 CSS 为页面中元素设定尺寸的方法。 在我们设计网页的时候，需要理解这些不同方法之间的差异。在本课程中，我们将总结设定元素尺寸的方法，并定义几个术语，这些内容将会在未来对你有所帮助。

### 原始尺寸，或固有尺寸

在受 CSS 设置影响之前，HTML 元素有其原始的尺寸。一个直观的例子就是图像。一副图像的长和宽由这个图像文件自身确定。这个尺寸就是固有尺寸。

如果你把图片放置在网页中的时候没有在`<img>` 标签或 CSS 中设置其尺寸，那么将使用其固有尺寸显示。我们给下面的示例图像绘制了一个边框，以便你看出图像文件的长宽。

![image-20220819100607694](image-20220819100607694.png)

一个空的`<div>`是没有尺寸的。如果你在你的 HTML 文件中添加一个空`<div> `并给予其边框（就像刚才我们为图像做的那样），你会在页面上看到一条线。这是边框被压缩后的效果— 它内部没有内容。在我们下面的例子中，边框宽度扩展到整个容器宽度，因为它是块级元素，而块级元素的行为就是这样的。它没有高度，或者说高度为 0，因为内部没有内容。

![image-20220819100550746](image-20220819100550746.png)

在上面的例子中，试着在空元素内部添加些内容。现在边框内包含一些文字了，因为元素的高度由其所含内容高度确定。**再强调一次，这就是元素的固有尺寸 — 由其所包含的内容决定。**

### 设置具体的尺寸

我们当然可以给设计中的元素指定具体大小。当给元素指定尺寸（然后其内容需要适合该尺寸）时，我们将其称为外部尺寸。以上面例子中的` <div>` 举例 — 我们可以给它一个具体的 width 和 height 值，然后不论我们放什么内容进去它都是该尺寸。 正如我们在上一课有关溢出的内容中所发现的，如果内容的数量超出了元素可容纳的空间，则设置的高度会导致内容溢出。

由于存在溢出问题，在网络上使用长度或百分比固定元素的高度需要非常小心。

### 使用百分数

许多时候，百分数是长度单位，正如我们在[Value and units 这节课中讨论的那样](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Values_and_units#percentages)，它们常常可与长度互换。当使用百分数时，你需要清楚，它是**什么**东西的百分数。对于一个处于另外一个容器当中的盒子，如果你给予了子盒子一个百分数作为宽度，那么它指的是父容器宽度的百分数。

这是因为百分数是以包含盒子的块为根据解析的。如果我们的`<div>`没有被指定百分数的值，那么它会占据 100% 的可用空间，因为它是块级别的元素。如果我们给了它一个百分数作为宽度，那么这就是它原来情况下可以占据空间的百分数。

### 把百分数作为内外边距

如果你把`margins`和`padding`设置为百分数的话，你会注意到一些奇怪的表现。在下面的例子里，我们有一个盒子，我们给了里面的盒子 10% 的[`margin`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin)以及 10% 的[`padding`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding)。盒子底部和顶部的内外边距，和左右外边距有同样的大小。

![image-20220819101009762](image-20220819101009762.png)

或许，你期望元素的上下外边距是其高度的百分比，元素的左右外边距是其宽度的百分比。但情况并非如此！

使用百分比作为元素外边距（margin）或填充（padding）的单位时，值是以包含块的**内联尺寸**进行计算的，也就是元素的水平宽度。在我们的示例中，所有的外边距或填充都是宽度的 10%。请记住一个事实，当你使用百分比作为元素外边距或填充的单位时，你将得到一个相同尺寸的外边距或填充。



### min-和 max-尺寸

除了让万物都有一个确定的大小以外，我们可以让 CSS 给定一个元素的最大或最小尺寸。如果你有一个包含了变化容量的内容的盒子，而且你总是想让它**至少**有个确定的高度，你应该给它设置一个[`min-height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/min-height)属性。盒子就会一直保持大于这个最小高度，但是如果有比这个盒子在最小高度状态下所能容纳的更多内容，那么盒子就会变大。

在以下的示例中，你可以看到两个盒子，两个都有 150 像素的确定高度，左边的盒子有 150 像素高，右边的盒子有需要更多空间才能装下的内容，所以它变得比 150 像素高。

```html
    <div class="box"></div>
    <div class="box">These boxes both have a min-height set, this box has content in it which will need more space than the assigned height, and so it grows from the minimum.These boxes both have a min-height set, this box has content in it which will need more space than the assigned height, and so it grows from the minimum.</div>
```

```css
.box {
    float: left;
    border: 5px solid darkblue;
    min-height: 150px;
    width: 200px;
}


```

![image-20220819101525346](image-20220819101525346.png)

这在避免溢出的同时并处理变化容量的内容的时候是很有用的。

[`max-width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/max-width)的常见用法为，在没有足够空间以原有宽度展示图像时，让图像缩小，同时确保它们不会比这一宽度大。

作为示例，如果你设定一个图像的属性为`width: 100%`，而且它的原始宽度小于容器，图像会被强制拉伸以变大，看起来像素更加明显。如果它的原始宽度大于容器，它则会溢出。两种情形都不是你想要看到的。

如果你使用了`max-width: 100%`，那么图像可以变得比原始尺寸更小，但是不会大于原始尺寸的 100%。

在下面的示例里，我们使用了两次相同的图片。第一次使用，属性值已设为`width: 100%`，位于比图片大的容器里，因此图片拉伸到了与容器相同的宽度；第二次的属性值则设为`max-width: 100%`，因此它并没有拉伸到充满容器；第三个盒子再一次包含了相同的图片，同时设定了`max-width: 100%`属性，这时你能看到它是怎样缩小来和盒子大小相适应的。

```html
<div class="wrapper">
  <div class="box">
    <img src="https://mdn.github.io/css-examples/learn/backgrounds-borders/big-star.png" alt="star" class="width">
  </div>
  <div class="box">
    <img src="https://mdn.github.io/css-examples/learn/backgrounds-borders/big-star.png" alt="star" class="max"></div>
  <div class="minibox">
    <img src="https://mdn.github.io/css-examples/learn/backgrounds-borders/big-star.png" alt="star" class="max">
  </div>
</div>

```

```css
.width {
    width: 100%;
}

.max {
    max-width: 100%;
}

.minibox {
    width: 50px;
}


.box {
    width: 200px;
    border: 1px solid blueviolet;
}
.minibox {
    border: 1px solid blueviolet;

}
```

![image-20220819140705759](image-20220819140705759.png)

这个技术是用来让图片**可响应**的，所以在更小的设备上浏览的时候，它们会合适地缩放。你无论怎样都不应该用这个技术先载入大原始尺寸的图片，再对它们在浏览器中进行缩放。图像应该合适地调整尺寸，以使它们不会比预计中展示时所需要的最大尺寸大。下载过大的图像会造成你的网站变慢，如果用户使用按量收费的网络连接，会让用户花更多钱。

> **备注：**了解更多关于[响应式图片技术](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)的事情。



### 视口单位

视口，即你在浏览器中看到的部分页面，也是有尺寸的。在 CSS 中，我们有与视口尺寸相关的度量单位，即意为视口宽度的`vw`单位，以及意为视口高度的 `vh`单位。使用这些单位，你可以把一些东西做得随用户的视口改变大小。

`1vh`等于视口高度的 1%，`1vw`则为视口宽度的 1%.你可以用这些单位约束盒子的大小，还有文字的大小。在下面的示例里，我们有一个大小被设为 20vh 和 20vw 的盒子。这个盒子里面有一个字母`A`，其[`font-size`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-size)属性被设成了 10vh。

```html
<div class="box">
  A
</div>
    
```

```css
.box {
  border: 5px solid darkblue;
  width: 20vw;
  height: 20vh;
  font-size: 10vh;
}
    
```

![image-20220819141035238](image-20220819141035238.png)

**如果你改变了`vh`和`vw`的对应值，盒子和字体的大小也会改变；视口大小的变化也会让它们的大小变化，因为它们是依照视口来定大小的。想看到随着你改变视口大小的时候示例的变化的话，你需要在一个新浏览器视窗里面载入此示例，因为你可以控制该视窗的大小，同时上面示例所在的嵌入的`<iframe>`的大小即是对上面示例而言的视口。[打开此示例](https://mdn.github.io/css-examples/learn/sizing/vw-vh.html)，调整浏览器视窗的大小，观察在盒子和文本的大小上所发生的事情。**

在你的设计中，根据视口改变物件的大小是很有用的。例如，如果你想要在你其他内容之前，有一个充满整个视口的视觉宣传段落，让你的页面的那个部分有 100vh 高的话，会把剩下的内容推到视口的下面，只有向下滚动文档的时候它们才会出现。

### 小结

本节课，你已经得到了一个对于你可能在约束网站上的内容大小的时候，会遇到的一些关键问题的详细介绍。当你继续学习[CSS 布局](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout)的时候，约束大小会成为掌握不同布局途径的非常重要的基础，所以在继续之前有必要在这里理解这些概念。

## 图像、媒体和表单元素

在这节课里，我们来看一下，CSS 是如何处理某些特殊元素的。图像、其他媒体和表格元素的表现和普通的盒子有些不同，这取决于你使用 CSS 格式化它们的能力。理解什么可能做到，什么不可能做到能够省些力气，本节课将会聚焦于一些你需要知道的主要的事情上。

### 替换元素

图像和视频被描述为**[替换元素](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Replaced_element)**。这意味着 CSS 不能影响它们的内部布局——而仅影响它们在页面上相对于其它元素的位置。但是，正如我们将看到的，CSS 可以对图像执行多种操作。

某些替换元素（例如图像和视频）也具有**宽高比**。这意味着它在水平（x）和垂直（y）方向上均具有大小，并且默认情况下将使用文件的固有尺寸进行显示。

### 调整图像大小

正如你从之前的几节课中所学到的那样，CSS 中万物皆盒。如果你把一张图片放在一个盒子里，而这张图片的原始长和宽比盒子的小或大，那么这张图要么缩在盒子里，要么就从盒子里面溢出。你需要决定如何处理这样的溢出。

下面的示例中有两个盒子，长宽均为 200 像素：

- 一个包含了一张小于 200 像素的图像，它比盒子小，并且不会自动拉伸来充满盒子。
- 另一张图像大于 200 像素，溢出了盒子。

![image-20220819142748332](image-20220819142748332.png)

那么该如何处理溢出问题呢？

正如我们在[之前的课程](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Sizing_items_in_CSS)  所学的那样，一个常用的方法是将一张图片的 max-width 设为 100%。这将会使图片的尺寸小于等于盒子。这个技术也会对其他替换元素（例如 `<video>`，或者 `<iframe>` 起作用。

**上面的示例中的 `<img>` 元素加入 `max-width: 100%`，你会看到，左边那张小的图像没有变化，而大的图像变小了，恰好装在了盒子里。**

你可以选择对容器内的图像作其它方式的处理。例如，你可能想把一张图像调整到能够完全盖住一个盒子的大小。

[`object-fit`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/object-fit) 属性可以在这里帮助你。当使用 `object-fit` 时，替换元素可以以多种方式被调整到合乎盒子的大小。

下面的示例中我们使用了值 `cover` 来缩小图像，同时维持了图像的原始比例。这样图像就可以充满盒子。但由于比例保持不变，图像多余的一部分将会被盒子裁切掉。

```html
<div class="wrapper">
  <div class="box">
    <img src="https://mdn.github.io/css-examples/learn/values-units/balloons.jpg" alt="balloons" class="cover">
  </div>
  <div class="box">
    <img src="https://mdn.github.io/css-examples/learn/values-units/balloons.jpg" alt="balloons" class="contain">
  </div>
</div>
```

```css
.box {
    width: 200px;
    height: 200px;
    border: 1px solid blueviolet;
    margin: 10px;
}

img {
    height: 100%;
    width: 100%;
}

.cover {
    object-fit: cover;
}

.contain {
    object-fit: contain;
}

```

![image-20220819144242311](image-20220819144242311.png)



如果我们使用值 `contain`，图像就会被缩放到足以完整地放到盒子里面的大小。如果它和盒子的比例不同，将会出现“开天窗”的结果。

你可能也想试试 `fill` 值，它可以让图像充满盒子，但是不会维持比例。

### 布局中的替换元素

在对替换元素使用各种 CSS 布局时，你可能会发现他们的表现方式与其他元素有一些细节上的差异。例如，flex 或者 grid 布局中，默认情况下元素会被拉伸到充满整块区域。但是图像不会被拉伸，而会对齐到网格区域或者弹性容器的起始处。

你可以在下面的示例中看到这一现象。该示例有一个两列两行的网格容器，里面有四个物件。所有的 `<div>` 元素有自己的背景色，被拉伸到充满了行和列。但是，图像并没有被拉伸。

```html
<div class="wrapper">
  <img src="https://mdn.github.io/css-examples/learn/backgrounds-borders/big-star.png" alt="star">
  <div></div>
  <div></div>
  <div></div>
</div>
    
```

```css
.wrapper {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 200px 200px;
  gap: 20px;
}

.wrapper > div {
  background-color: rebeccapurple;
  border-radius: .5em;
}
    
```

![image-20220819144741253](image-20220819144741253.png)

如果你是按序阅读这些课程的，那么你可能还没有看到布局的部分。不过没关系，只要记住替换元素在成为网格或者弹性布局的一部分时，有不同的默认行为就好了。这一默认行为很有必要，因为它避免了替换元素被布局拉伸成奇怪的样子。

为了强制图像拉伸，以充满其所在的网格单元，你必须做类似于下面的事情：

```css
img {
  width: 100%;
  height: 100%;
}

```

这将会无条件地拉伸图像，所以很可能不会是你想要的。

![image-20220819144907406](image-20220819144907406.png)

### form 元素

用 CSS 格式化表单元素是一个需要技巧的工作，[HTML 表单指南](https://developer.mozilla.org/zh-CN/docs/Learn/Forms)包含了详细的格式化表单元素的指导，我不会在这里复述。本节需要介绍的是一些值得关注的关键基础内容。

很多表单控件是通过` <input> `元素添加到网页上的。该元素定义了简单的表单区域，例如文字输入。更进一步还有 HTML5 新加入的更加复杂的区域，例如颜色和日期撷取器。另外还有一些其他元素，例如用于多行文本输入的 `<textarea>`，以及那些用来包含和标记表单特定部分的元素，例如 `<fieldset>` 和 `<legend> `。

HTML5 还包含了允许 Web 开发者指定必填区域的特性，甚至还能检验填入内容的类型。如果用户输入了一些不符合要求的内容，或者未填写必填区域，浏览器会显示错误提示。不同的浏览器在给此类元素样式化和自定义方面不尽相同。

#### 样式化文本输入元素

允许文本输入的元素有很多，例如 `<input type="text">`，及其指定特定类型的元素，如 `<input type="email">` 以及 `<textarea>` 元素，这些都是相当容易样式化的，它们和页面上其他盒子的表现相同。只不过在不同的操作系统和浏览器上访问时这些元素默认的样式化方式可能不同。

在下面的示例中，我们已经将一些文本输入元素用 CSS 样式化了。可以看到，边框、内外边距之类的东西都如期生效了。现在，我们使用属性选择器来指向不同的输入类型，尝试通过改变边框、添加输入区域背景色、改变字体和内边距的方式来改变表单的外观。

```html
<form>
  <div><label for="name">Name</label>
  <input type="text" id="name"></div>
  <div><label for="email">Email</label>
  <input type="email" id="email"></div>

  <div class="buttons"><input type="submit" value="Submit"></div>
</form>
    
```

```css
input[type="text"],
input[type="email"] {
    border: 2px solid #000;
    margin: 0 0 1em 0;
    padding: 10px;
    width: 20%;
}

input[type="submit"] {
    border: 3px solid #333;
    background-color: #999;
    border-radius: 5px;
    padding: 10px 2em;
    font-weight: bold;
    color: #fff;
}

input[type="submit"]:hover {
    background-color: #333;
}

    
```

![image-20220819145429928](image-20220819145429928.png)

> **警告：** 你应该谨慎改变表单样式，确保用户仍然能轻松辨认表单元素。原则上，你可以创建一个没有边框和背景的，几乎无法与周围的内容区分开来的输入表单，但这会使辨认和填写变得非常困难。

正如在本教程的 HTML 部分的[样式化表单](https://developer.mozilla.org/zh-CN/docs/Learn/Forms/Styling_web_forms)里解释的那样，许多更加复杂的输入类型是由操作系统渲染的，无法进行样式化。因而你应该总是留意到表单在不同的用户看来差异很大，并在许多浏览器上测试复杂的表单。

#### 继承和表单元素

在一些浏览器中，表单元素默认不会继承字体样式，因此如果你想要确保你的表单填入区域使用 body 中或者一个父元素中定义的字体，你需要向你的 CSS 中加入这条规则。

```css
button,
input,
select,
textarea {
  font-family : inherit;
  font-size : 100%;
}

```

#### form 元素与 box-sizing

跨浏览器的 form 元素对于不同的挂件使用不同的盒子约束规则。你已经在我们的[盒模型课](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/The_box_model)中学习了 `box-sizing` 属性，在样式化表单时候，你可以使用这一知识，确保在给 form 元素设定宽度和高度时可以有统一的体验。

为了保证统一，最好将所有元素的内外边距都设为 `0`，然后在单独进行样式化控制的时候将这些加回来。

```css
button,
input,
select,
textarea {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

```

#### 其他有用的设置

除了上面提到的规则以外，你也应该在 `<textarea>` 上设置 `overflow: auto` 以避免 IE 在不需要滚动条的时候显示滚动条：

```css
textarea {
  overflow: auto;
}

```

#### 将一切都放在一起“重置”

作为最后一步，我们可以将上面讨论过的各式属性包起来，成为以下的“表单重置”，以提供一个统一的在其上继续进行工作的地基，这包含了前三节提到的所有东西：

```css
button,
input,
select,
textarea {
  font-family: inherit;
  font-size: 100%;
  box-sizing: border-box;
  padding: 0; margin: 0;
}

textarea {
  overflow: auto;
}

```

> **备注：** 通用样式表被许多开发者用作所有项目的一系列基础样式，典型就是那些做了和以上提到相似的事情的那些，在你开始自己的 CSS 作业前，它确保了跨浏览器的任何事情都被默认设定为统一样式。它们不像以往那么重要了，因为浏览器显著地要比以往更加统一。但是，如果你想要看一个例子，可以看看这个[Normalize.css](http://necolas.github.io/normalize.css/)，它被许多项目用作基础，是非常流行的样式表。

至于样式化表单的更加深入的信息，可以看下这些教程的 HTML 一节的这两篇文章：

- [Styling HTML Forms](https://developer.mozilla.org/zh-CN/docs/Learn/Forms/Styling_web_forms)
- [Advanced Styling for HTML Forms](https://developer.mozilla.org/zh-CN/docs/Learn/Forms/Advanced_form_styling)

### 小结

这节课致力于说明在你用 CSS 处理图像、媒体和其他不普通的元素时，你会遇到的不同之处。在下篇文章中，我们将会了解一些在你样式化 HTMl 表格时有用的技巧。



## 样式化表格

设计一个 HTML 表格不是世界上最迷人的工作，但有时我们必须这样做。本文提供了一个使 HTML 表格看起来不错的指南，其中一些功能在前面的文章中已作详细介绍。

### 一个典型的 HTML 表格

让我们从一个典型的 HTML 表格开始。恩，我说典型——大多数 HTML 表格都是关于鞋子，天气，或者员工的。我们决定通过制作英国著名的朋克乐队来让事情变得更有趣。标记看起来是这样的

```html
    <table>
      <caption>A summary of the UK's most famous punk bands</caption>
      <thead>
        <tr>
          <th scope="col">Band</th>
          <th scope="col">Year formed</th>
          <th scope="col">No. of Albums</th>
          <th scope="col">Most famous song</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">Buzzcocks</th>
          <td>1976</td>
          <td>9</td>
          <td>Ever fallen in love (with someone you shouldn't've)</td>
        </tr>
        <tr>
          <th scope="row">The Clash</th>
          <td>1976</td>
          <td>6</td>
          <td>London Calling</td>
        </tr>
        <tr>
          <th scope="row">The Damned</th>
          <td>1976</td>
          <td>10</td>
          <td>Smash it up</td>
        </tr>
        <tr>
          <th scope="row">Sex Pistols</th>
          <td>1975</td>
          <td>1</td>
          <td>Anarchy in the UK</td>
        </tr>
        <tr>
          <th scope="row">Sham 69</th>
          <td>1976</td>
          <td>13</td>
          <td>If The Kids Are United</td>
        </tr>
        <tr>
          <th scope="row">Siouxsie and the Banshees</th>
          <td>1976</td>
          <td>11</td>
          <td>Hong Kong Garden</td>
        </tr>
        <tr>
          <th scope="row">Stiff Little Fingers</th>
          <td>1977</td>
          <td>10</td>
          <td>Suspect Device</td>
        </tr>
        <tr>
          <th scope="row">The Stranglers</th>
          <td>1974</td>
          <td>17</td>
          <td>No More Heroes</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <th scope="row" colspan="2">Total albums</th>
          <td colspan="2">77</td>
        </tr>
      </tfoot>
    </table>
```

由于scope、`<caption>`、`<thead>`、`<tbody>`等特性，表格被很好地标记了，易于使用，并且易于访问，不幸的是，它在屏幕上呈现时看起来不太好（见它的预览版 [punk-bands-unstyled.html](https://mdn.github.io/learning-area/css/styling-boxes/styling-tables/punk-bands-unstyled.html)）：

![image-20220819170737716](image-20220819170737716.png)

它看起来很拥挤，很难阅读，也很无聊。我们需要使用一些 CSS 来解决这个问题。

### 自主学习：样式化我们的表格

在这个自主学习部分中，我们将一起来样式化我们的表格。

1. 首先，复制[实例标记](https://github.com/mdn/learning-area/blob/master/css/styling-boxes/styling-tables/punk-bands-unstyled.html)到本地，下载这两个图像 ([noise](https://github.com/mdn/learning-area/blob/master/css/styling-boxes/styling-tables/noise.png)和 [leopardskin](https://github.com/mdn/learning-area/blob/master/css/styling-boxes/styling-tables/leopardskin.jpg))，然后将三个结果文件放在本地计算机的某个工作目录中。
2. 接下来，创建一个名为`style.css`的新文件并将其保存在与其他文件相同的目录中。
3. 将 CSS 链接到 HTML 中，将下面的 HTML 代码放到 HTML 的[`<head>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/head)中：

```css
<link href="style.css" rel="stylesheet" type="text/css">

```

#### 间距和布局

我们需要做的第一件事是整理出空间/布局——默认的表格样式是如此的拥挤！要做到这一点，请将以下 CSS 添加到您的 `style.css` 文件：

需要注意的最重要的部分如下：

- 在你的表上，给`table-layout`属性设置一个为`fixed`的值通常是一个好主意，因为它使表的行为在默认情况下更可预测。通常情况下，表列的尺寸会根据所包含的内容大小而变化，这会产生一些奇怪的结果。通过 `table-layout: fixed`，您可以根据列标题的宽度来规定列的宽度，然后适当地处理它们的内容。这就是为什么我们使用了`thead th:nth-child(n) `选择了四个不同的标题 (`:nth-child`) 选择器（“选择第 n 个子元素，它是一个顺序排列的`<th>`元素，且其父元素是`<thead>`元素”）并给定了它们的百分比宽度。整个列宽度与列标题的宽度是一样的，这是一种很好的设定表列尺寸的方式。Chris Coyier 在[Fixed Table Layouts](https://css-tricks.com/fixing-tables-long-strings/)中更详细地讨论了这一技术。 我们将它与一个 100% 的width组合在一起，这意味着该表将填充它放入的任何容器，并且能很好的响应（虽然它仍然需要更多的工作来让它在窄屏宽度上看起来很好）。

- 一个[`border-collapse`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-collapse)属性的`collapse`值对于任何表样式的工作来说都是一个标准的最佳实践。默认情况下，当您在表元素上设置边框时，它们之间将会有间隔，如下图所示：

  ![image-20220819170346402](image-20220819170346402.png)

- 这看起来不太好 (虽然可能是你想要的样子，谁知道呢？)。使用 `border-collapse: collapse;` ，让边框合为一条，现在看起来好多了：

  ![image-20220819170509482](image-20220819170509482.png)

- 我们在整个表设置了一个[`border`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border)，这是必要的，因为我们将在表页眉和页脚后面设置一些边框——当你在表格外面没有一个边界而且以空隙结尾的时候，它看起来很奇怪，而且是不连贯的。

- 我们在`<th>`和`<td>`元素上设置了一些padding——这些元素使数据项有了一些空间，使表看起来更加清晰。

此刻，我们的表看起来好多了：

![img](table-with-spacing.png)

#### 一些简单的排版

现在我们把类型整理一下。

首先，我们在[Google Fonts](https://www.google.com/fonts)上找到了一种适合于朋克乐队的字体的字体。如果你愿意，你可以去那里找一个不同的。现在，您只需替换我们提供的`<link>`元素和定制的`font-family`声明，并使用 Google 字体提供给您的内容。

首先，将下面的`<link>`元素添加到您的 HTML 头部，就在您现有的 `<link>` 元素之上：

```html
<link href='https://fonts.googleapis.com/css?family=Rock+Salt' rel='stylesheet' type='text/css'>

```

现在将下面的 CSS 添加到您的`style.css`文件，在之前内容后面添加：

```css
/* typography */

html {
  font-family: 'helvetica neue', helvetica, arial, sans-serif;
}

thead th, tfoot th {
  font-family: 'Rock Salt', cursive;
}

th {
  letter-spacing: 2px;
}

td {
  letter-spacing: 1px;
}

tbody td {
  text-align: center;
}

tfoot th {
  text-align: right;
}

```

![image-20220819171636576](image-20220819171636576.png)

这里没有什么特别的东西。我们通常会对字体样式进行调整，使其更易于阅读：

- 我们已经设置了一个全局无衬线字体;这纯粹是一种风格上的选择。我们还在和元素的标题上设置了自定义字体，这是一种很不错的、很有朋克风格的外观。
- 我们在标题和单元格上设置了一些[`letter-spacing`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/letter-spacing)，因为我们觉得它有助于提高可读性。再次强调，这主要是一种风格上的选择。
- 我们在`<tbody>`中的表格单元中对文本进行了居中对齐，使它们与标题对齐。默认情况下，单元格被赋予了一个[`text-align`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-align)的`left`值，并且标题被赋予了一个`center`值，但是通常情况下，让两者对齐看起来更好。标题字体的默认粗体值足以区分它们的外观。
- 我们在`<tfoot>`中对标题进行了右对齐，以便与它的数据点更好地关联。

#### 图形和颜色

现在轮到图形和颜色了！因为表格上充满“朋克“和“个性”，我们需要给它再搭配一些鲜艳的造型。别担心，你不必让你的表格”燥起来“，你可以选择一些更巧妙、更有品位的东西。

首先将下面的 CSS 添加到`style.css`文件中，在底部添加：

```css
thead, tfoot {
  background: url('https://img0.baidu.com/it/u=4245296189,1945278349&fm=253&fmt=auto&app=138&f=JPEG?w=700&h=401');
  color: white;
  text-shadow: 1px 1px 1px black;
}

thead th, tfoot th, tfoot td {
  background: linear-gradient(to bottom, rgba(0,0,0,0.1), rgba(0,0,0,0.5));
  border: 3px solid purple;
}

```

我们已经将一个background-image添加到`<thead>`和`<tfoot>`，并将页眉和页脚的所有文本颜色color更改为白色 (并给它一个text-shadow)，这样它的可读性就更好了。你应该确保你的文字与你的背景形成鲜明的对比，使得它是可读的。

我们还为`<th>`和 `<td>`添加了一个线性渐变，在页眉和页脚中添加了一个漂亮的纹理，同时也为这些元素提供了一个明亮的紫色边框。有多个嵌套的元素是很有用的，这样您就可以将样式层叠在一起。是的，我们可以通过设置多组背景图像属性值来在`<thead>`和 `<tfoot>`元素上同时使用背景图像和线性渐变，但是我们决定分开使用，因为考虑到不支持多个背景图像或线性渐变的老浏览器。

我们还为`<th>`和 `<td>`添加了一个线性渐变，在页眉和页脚中添加了一个漂亮的纹理，同时也为这些元素提供了一个明亮的紫色边框。有多个嵌套的元素是很有用的，这样您就可以将样式层叠在一起。是的，我们可以通过设置多组背景图像属性值来在`<thead>`和 `<tfoot>`元素上同时使用背景图像和线性渐变，但是我们决定分开使用，因为考虑到不支持多个背景图像或线性渐变的老浏览器。

#### 斑马条纹图案

我们想用一个单独的部分来展示如何实现斑马条纹（**zebra stripes**）——通过改变不同数据行的颜色，使表中交替行不同的数据行可以更容易地进行解析和读取。将下面的 CSS 添加到您的 `style.css` 文件底部：

```css

tbody tr:nth-child(odd) {
    background-color: rgba(238, 238, 238, 0.78);
}

tbody tr:nth-child(even) {
    background-color: rgba(114, 114, 114, 0.6);
}



```

![image-20220820104647954](image-20220820104647954.png)

#### 样式化标题

对我们的表格还有最后一点处理——样式化标题。要做到这一点，请将以下内容添加到您的`style.css` 文件底部：

```css
caption {
  font-family: 'Rock Salt', cursive;
  padding: 20px;
  font-style: italic;
  caption-side: bottom;
  color: #666;
  text-align: right;
  letter-spacing: 1px;
}

```

这里没有什么值得注意的地方，除了[`caption-side`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/caption-side)属性，它被赋予了一个`bottom`的值。这就导致标题被放置在表格的底部，与其他声明一起提供了最后的外观

![image-20220820104706764](image-20220820104706764.png)

### 自主学习：样式化你自己的表格

现在，我们希望您可以使用我们的示例表格 HTML(或者使用您自己的一些！)，并将其样式设计成比我们的表更好的设计和不那么花哨的东西。

#### 表格样式小贴士

在继续之前，我们认为我们将为您提供一个快速列表，列出了上面提到的最有用的点：

- 使您的表格标记尽可能简单，并且保持灵活性，例如使用百分比，这样设计就更有响应性。
- 使用 [`table-layout`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/table-layout)`: fixed` 创建更可控的表布局，可以通过在标题[`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width)中设置[`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width)来轻松设置列的宽度。
- 使用 [`border-collapse`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-collapse)`: collapse` 使表元素边框合并，生成一个更整洁、更易于控制的外观。
- 使用`<thead>`, `<tbody>`和`<tfoot>` 将表格分割成逻辑块，并提供额外的应用 CSS 的地方，因此如果需要的话，可以更容易地将样式层叠在一起。
- 使用斑马线来让其他行更容易阅读。
- 使用 `text-align`直线对齐您的`<th>`和`<td>`文本，使内容更整洁、更易于跟随。

### 小结

现在，我们身后的表格样式令人炫目，令人兴奋，我们需要一些其他的东西来占据我们的时间。不要担心——下一章会介绍如何调试 CSS，如何解决诸如布局不能像所应该的那样进行呈现的问题，或者元素无法像你预料的那样生效的问题。那里包含了使用浏览器开发者工具寻找你的问题的解决方案的信息。

## 调试`CSS`

参考链接：https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Debugging_CSS

## 组织`CSS`

参考链接：	https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Organizing

# 样式化文本

掌握了 CSS 语言的基础之后，对于您来说，下一个需要关心的 CSS 主题就是为文本添加样式——一个您将会最经常使用 CSS 做的事情。在这里，我们专注于为文本样式的基础，包括设置字体、粗细、斜体、行还有字符间距、阴影以及文本的其他特征。我们将会通过在您的网页中应用自定义字体、样式化列表以及链接来圆满地结束本模块。

## 基本文本和字体样式

这里我们将详细介绍文本/字体样式的所有基本原理，包括设置文字的粗细，字体和样式，文字的属性简写，文字的对齐，和其他效果，以及行和字母间距。

### CSS 中的文字样式涉及什么？

正如你已经在你使用 HTML 和 CSS 完成工作时所经历的一样，元素中的文本是布置在元素的内容框中。以内容区域的左上角作为起点 (或者是右上角，是在 RTL 语言的情况下)，一直延续到行的结束部分。一旦达到行的尽头，它就会进到下一行，然后继续，再接着下一行，直到所有内容都放入了盒子中。文本内容表现地像一些内联元素，被布置到相邻的行上，除非到达了行的尽头，否则不会换行，或者你想强制地，手动地造成换行的话，你可以使用 [`<br>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/br) 元素。

用于样式文本的 CSS 属性通常可以分为两类，我们将在本文中分别观察。

- **字体样式**: 作用于字体的属性，会直接应用到文本中，比如使用哪种字体，字体的大小是怎样的，字体是粗体还是斜体，等等。
- **文本布局风格**: 作用于文本的间距以及其他布局功能的属性，比如，允许操纵行与字之间的空间，以及在内容框中，文本如何对齐。

> 备注： 请记住，包含在元素中的文本是作为一个单一的实体。你不能将文字其中一部分选中或添加样式，如果你要这么做，那么你必须要用适合的元素来包装它们，比如 ( `<span>` 或者 `<strong>`), 或者使用伪元素，像::first-letter (选中元素文本的第一个字母), `::first-line` (选中元素文本的第一行), 或者 `::selection` (当前光标双击选中的文本)

### 字体

我们直接来看看样式字体的属性。在这个例子中，我们会在一个相同的 HTML 示例中应用一些不同的 CSS 属性，就像这样：

```html
<h1>Tommy the cat</h1>

<p>I remember as if it were a meal ago...</p>

<p>Said Tommy the Cat as he reeled back to clear whatever foreign matter
 may have nestled its way into his mighty throat. Many a fat alley rat
had met its demise while staring point blank down the cavernous barrel of
 this awesome prowling machine. Truly a wonder of nature this urban
predator — Tommy the cat had many a story to tell. But it was a rare
occasion such as this that he did.</p>

```

你可以在这找到完成版本 [finished example on Github](https://mdn.github.io/learning-area/css/styling-text/fundamentals/) (也可以看源码 [the source code](https://github.com/mdn/learning-area/blob/master/css/styling-text/fundamentals/index.html).)

#### 颜色

[`color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/color) 属性设置选中元素的前景内容的颜色 (通常指文本，不过也包含一些其他东西，或者是使用 [`text-decoration`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-decoration) 属性放置在文本下方或上方的线 (`underline overline`)。

`color` 也可以接受任何合法的 [CSS 颜色单位](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units#colors), 比如：

```css
p {
  color: red;
}

```

这将导致段落变为红色，而不是标准的浏览器默认的黑色

![image-20220820145556172](image-20220820145556172.png)

#### 字体种类

要在你的文本上设置一个不同的字体，你可以使用 [`font-family`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-family) 属性，这个允许你为浏览器指定一个字体 (或者一个字体的列表)，然后浏览器可以将这种字体应用到选中的元素上。浏览器只会把在当前机器上可用的字体应用到当前正在访问的网站上；如果字体不可用，那么就会用浏览器默认的字体代替 [default font](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Styling_text/Fundamentals#默认字体). 下面是一个简单的例子：

```css
p {
  font-family: arial;
}

```

这段语句使所有在页面上的段落都采用 arial 字体，这个字体可在任何电脑上找到。

##### 网页安全字体

说到字体可用性，只有某几个字体通常可以应用到所有系统，因此可以毫无顾忌地使用。这些都是所谓的 **网页安全字体**。

大多数时候，作为网页开发者，我们希望对用于显示我们的文本内容的字体有更具体的控制。问题在于，需要一个方法来知道当前正在浏览我们的网站网页的电脑，它有哪些可用字体。我们并不是总能在每种情况下都知道这一点，但是网络安全字体在几乎所有最常用的操作系统（Windows，Mac，最常见的 Linux 发行版，Android 和 iOS 版本）中都可用。

实际的 Web 安全字体列表将随着操作系统的发展而改变，但是可以认为下面的字体是网页安全的，至少对于现在来说 (它们中的许多都非常流行，这要感谢微软在 90 年代末和 21 世纪初期的倡议*[Core fonts for the Web](https://en.wikipedia.org/wiki/Core_fonts_for_the_Web)* )：

|                 |            |                                                              |
| :-------------- | :--------- | :----------------------------------------------------------- |
| 字体名称        | 泛型       | 注意                                                         |
| Arial           | sans-serif | 通常认为最佳做法还是添加 Helvetica 作为 Arial 的首选替代品，尽管它们的字体面几乎相同，但 Helvetica 被认为具有更好的形状，即使 Arial 更广泛地可用。 |
| Courier New     | monospace  | 某些操作系统有一个 Courier New 字体的替代（可能较旧的）版本叫 Courier。使用 Courier New 作为 Courier 的首选替代方案，被认为是最佳做法。 |
| Georgia         | serif      |                                                              |
| Times New Roman | serif      | 某些操作系统有一个 Times New Roman 字体的替代（可能较旧的）版本叫 Times。使用 Times 作为 Times New Roman 的首选替代方案，被认为是最佳做法。 |
| Trebuchet MS    | sans-serif | 您应该小心使用这种字体——它在移动操作系统上并不广泛。         |
| Verdana         | sans-serif |                                                              |

> **备注：** 在各种资源中，[cssfontstack.com](http://www.cssfontstack.com/) 网站维护了一个可用在 Windows 和 Mac 操作系统上使用的网页安全字体的列表，这可以帮助决策网站的安全性。

> **备注：** 有一个可以下载来自一个网页的自定义字体的方法，允许你通过任何你想要的方法来定制你使用的字体：**网页字体**。这个有一点复杂，我们将在这个模块中的另一篇文章中讨论这一点。

##### 默认字体

CSS 定义了 5 个常用的字体名称: `serif`, `sans-serif`, `monospace`, `cursive`, 和 `fantasy`. 这些都是非常通用的，当使用这些通用名称时，使用的字体完全取决于每个浏览器，而且它们所运行的每个操作系统也会有所不同。这是一种糟糕的情况，浏览器会尽力提供一个看上去合适的字体。 `serif`, `sans-serif` 和 `monospace` 是比较好预测的，默认的情况应该比较合理，另一方面，`cursive` 和 `fantasy` 是不太好预测的，我们建议使用它们的时候应该稍微注意一些，多多测试。



##### 字体栈

由于你无法保证你想在你的网页上使用的字体的可用性 (甚至一个网络字体可能由于某些原因而出错), 你可以提供一个**字体栈** (**font stack**)，这样的话，浏览器就有多种字体可以选择了。只需包含一个`font-family属性`，其值由几个用逗号分离的字体名称组成。比如

```css
p {
  font-family: "Trebuchet MS", Verdana, sans-serif;
}

```

在这种情况下，浏览器从列表的第一个开始，然后查看在当前机器中，这个字体是否可用。如果可用，就把这个字体应用到选中的元素中。如果不可用，它就移到列表中的下一个字体，然后再检查。

在字体栈的最后提供一个合适的通用的字体名称是个不错的办法，这样的话，即使列出的字体都无法使用，浏览器至少可以提供一个还算合适的选择。为了强调这一点，如果没有其他选项可用，那么段落将被赋予浏览器的默认衬线字体 - 通常是 Time New Roman - 这对于 sans-serif 字体是不利的！

> **备注：** 有一些字体名称不止一个单词，比如`Trebuchet MS` ，那么就需要用引号包裹。



##### 一个使用 font-family 的例子

```css
p {
  color: red;
  font-family: Helvetica, Arial, sans-serif;
}

```

#### 字体大小

在我们之前的模块中的[CSS values and units](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units) 文章，我们回顾了[length and size units](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units#length_and_size). 字体大小 (通过 [`font-size`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-size) 属性设置) 可以取大多数这些单位的值 (以及其他，比如百分比 [percentages](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units#percentages))，然而你在调整字体大小时，最常用的单位是：

- `px` (像素): 将像素的值赋予给你的文本。这是一个绝对单位， 它导致了在任何情况下，页面上的文本所计算出来的像素值都是一样的。
- `em`: 1em 等于我们设计的当前元素的父元素上设置的字体大小 (更加具体的话，比如包含在父元素中的大写字母 M 的宽度) 如果你有大量设置了不同字体大小的嵌套元素，这可能会变得棘手，但它是可行的，如下图所示。为什么要使用这个麻烦的单位呢？当你习惯这样做时，那么就会变得很自然，你可以使用`em`调整任何东西
- `rem`: 这个单位的效果和 em 差不多，除了 `1rem` 等于 HTML 中的根元素的字体大小， (i.e. `<html>`) ，而不是父元素。这可以让你更容易计算字体大小，但是遗憾的是， `rem` 不支持 `Internet Explorer 8` 和以下的版本。如果你的项目需要支持较老的浏览器，你可以坚持使用`em` 或`px`, 或者是 polyfill 就像 REM-unit-polyfill. （这个单位在“CSS 的值和单位”一节也有讲解）

元素的 `font-size` 属性是从该元素的父元素继承的。所以这一切都是从整个文档的根元素——`<html>`开始，浏览器的 `font-size` 标准设置的值为 16px。在根元素中的任何段落 (或者那些浏览器没有设置默认大小的元素)，会有一个最终的大小值：16px。其他元素也许有默认的大小，比如 `<h1>` 元素有一个 `2em` 的默认值，所以它的最终大小值为 32px。当你开始更改嵌套元素的字体大小时，事情会变得棘手。比如，如果你有一个`<article>` 元素在你的页面上，然后设置它的 `font-size` 为 `1.5em` (通过计算，可以得到大小为 24px)，然后想让 `<article>` 元素中的段落获得一个计算值为 `20px` 的大小，那么你应该使用多少 `em`。

```html
<!-- document base font-size is 16px -->
<article> <!-- If my font-size is 1.5em -->
  <p>My paragraph</p> <!-- How do I compute to 20px font-size? -->
</article>

```

你需要将 em 的值设置为 20/24, 或者 `0.83333333em`. 这个计算可能比较复杂，所以当你设置的时候，你需要仔细一些。如果可以使用 rem 的话，那实现起来就变得简单不少，避免在可能的情况下设置容器元素的字体大小。

##### 一个简单的 size 示例

当调整你的文本大小时，将文档 (document) 的基础 `font-size` 设置为 10px 往往是个不错的主意，这样之后的计算会变得简单，所需要的 (r)em 值就是想得到的像素的值除以 10，而不是 16。做完这个之后，你可以简单地调整在你的 HTML 中你想调整的不同类型文本的字体大小。在样式表的指定区域列出所有`font-size`的规则集是一个好主意，这样它们就可以很容易被找到。

我们的新结果是这样的：

```css
html {
  font-size: 10px;
}

h1 {
  font-size: 2.6rem;
}

p {
  font-size: 1.4rem;
  color: red;
  font-family: Helvetica, Arial, sans-serif;
}

```

#### 字体样式、字体粗细、文本转换和文本装饰

- `font-style`

  用来打开和关闭文本 italic (斜体)。可能的值如下 (你很少会用到这个属性，除非你因为一些理由想将斜体文字关闭斜体状态)：

  - `normal`: 将文本设置为普通字体 (将存在的斜体关闭)
  - `italic`: 如果当前字体的斜体版本可用，那么文本设置为斜体版本；如果不可用，那么会利用 oblique 状态来模拟 italics。
  - `oblique`: 将文本设置为斜体字体的模拟版本，也就是将普通文本倾斜的样式应用到文本中。

- `font-weight`: 设置文字的粗体大小。这里有很多值可选 (比如 `-light, -normal, -bold, -extrabold, -black`, 等等), 不过事实上你很少会用到 `normal` 和 `bold`以外的值：

  - `normal, bold`: 普通或者加粗的字体粗细
  - `lighter, bolder`: 将当前元素的粗体设置为比其父元素粗体更细或更粗一步。`100–900`: 数值粗体值，如果需要，可提供比上述关键字更精细的粒度控制。

- `text-transform`: 允许你设置要转换的字体。值包括：

  - `none`: 防止任何转型。
  - `uppercase`: 将所有文本转为大写。
  - `lowercase`: 将所有文本转为小写。
  - `capitalize`: 转换所有单词让其首字母大写。
  - `full-width`: 将所有字形转换成全角，即固定宽度的正方形，类似于等宽字体，允许拉丁字符和亚洲语言字形（如中文，日文，韩文）对齐。

- [`text-decoration`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-decoration): 设置/取消字体上的文本装饰 (你将主要使用此方法在设置链接时取消设置链接上的默认下划线。) 可用值为：

  - `none`: 取消已经存在的任何文本装饰。

  - `underline`: 文本下划线。

  - `overline`: 文本上划线

  - `line-through`: 穿过文本的线。

    你应该注意到 [`text-decoration`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-decoration) 可以一次接受多个值，如果你想要同时添加多个装饰值， 比如 `text-decoration: underline overline`.。同时注意 [`text-decoration`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-decoration) 是一个缩写形式，它由 [`text-decoration-line`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-decoration-line), [`text-decoration-style`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-decoration-style) 和 [`text-decoration-color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-decoration-color) 构成。你可以使用这些属性值的组合来创建有趣的效果，比如 `text-decoration: line-through red wavy`.

#### 文字阴影

你可以为你的文本应用阴影，使用 [`text-shadow`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-shadow) 属性。这最多需要 4 个值，如下例所示：

```css
text-shadow: 4px 4px 5px red;

```



4 个属性如下：

1. 阴影与原始文本的水平偏移，可以使用大多数的 CSS 单位 [length and size units](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units#length_and_size), 但是 px 是比较合适的。这个值必须指定。
2. 阴影与原始文本的垂直偏移;效果基本上就像水平偏移，除了它向上/向下移动阴影，而不是左/右。这个值必须指定。
3. 模糊半径 - 更高的值意味着阴影分散得更广泛。如果不包含此值，则默认为 0，这意味着没有模糊。可以使用大多数的 CSS 单位 [length and size units](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units#length_and_size).
4. 阴影的基础颜色，可以使用大多数的 CSS 颜色单位 [CSS color unit](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units#colors). 如果没有指定，默认为 `black`.

> **备注：** 正偏移值可以向右移动阴影，但也可以使用负偏移值来左右移动阴影，例如 `-1px -1px`.

##### 多种阴影

您可以通过包含以逗号分隔的多个阴影值，将多个阴影应用于同一文本，例如：

```css
text-shadow: -1px -1px 1px #aaa,
             0px 4px 1px rgba(0,0,0,0.5),
             4px 4px 5px rgba(0,0,0,0.7),
             0px 0px 7px rgba(0,0,0,0.4);

```

如果我们把这个样式应用到我们 "Tommy the cat" 示例中的 [`<h1>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) 元素

![image-20220820191446903](image-20220820191446903.png)



### 文本布局

有了基本的字体属性，我们来看看我们可以用来影响文本布局的属性。

#### 文本对齐

[`text-align`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-align) 属性用来控制文本如何和它所在的内容盒子对齐。可用值如下，并且在与常规文字处理器应用程序中的工作方式几乎相同：

- `left`: 左对齐文本。
- `right`: 右对齐文本。
- `center`: 居中文字
- `justify`: 使文本展开，改变单词之间的差距，使所有文本行的宽度相同。你需要仔细使用，它可以看起来很可怕。特别是当应用于其中有很多长单词的段落时。如果你要使用这个，你也应该考虑一起使用别的东西，比如 [`hyphens`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/hyphens)，打破一些更长的词语。

如果我们应用 `text-align: center;` 到我们例子中的 [`<h1>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) 元素中，结果如下：

![image-20220820202957446](image-20220820202957446.png)

#### 行高

[`line-height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/line-height) 属性设置文本每行之间的高，可以接受大多数单位 [length and size units](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units#length_and_size)，不过也可以设置一个无单位的值，作为乘数，通常这种是比较好的做法。无单位的值乘以 [`font-size`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-size) 来获得 `line-height`。当行与行之间拉开空间，正文文本通常看起来更好更容易阅读。推荐的行高大约是 1.5–2 (双倍间距。) 所以要把我们的文本行高设置为字体高度的 1.5 倍，你可以使用这个：

```css
line-height: 1.5;
```

如果要使文本垂直居中，可以设置行高等于外部盒子的高度

#### 字母和单词间距

[`letter-spacing`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/letter-spacing) 和 [`word-spacing`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/word-spacing) 属性允许你设置你的文本中的字母与字母之间的间距、或是单词与单词之间的间距。你不会经常使用它们，但是可能可以通过它们，来获得一个特定的外观，或者让较为密集的文字更加可读。它们可以接受大多数单位 [length and size units](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units#length_and_size).

所以作为例子，如果我们把这个样式应用到我们的示例中的 [`<p>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/p) 段落的第一行：

```css
p::first-line {
  letter-spacing: 2px;
  word-spacing: 4px;
}

```

![image-20220820203639387](image-20220820203639387.png)

#### 其他一些值得看一下的属性

以上属性让你了解如何开始在网页上设置文本，但是你可以使用更多的属性。我们只是想介绍最重要的。一旦你习惯使用上面的内容，你还应该探索以下几点：

Font 样式：

- [`font-variant`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-variant): 在小型大写字母和普通文本选项之间切换。
- [`font-kerning`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-kerning): 开启或关闭字体间距选项。
- [`font-feature-settings`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-feature-settings): 开启或关闭不同的 [OpenType](https://en.wikipedia.org/wiki/OpenType) 字体特性。
- [`font-variant-alternates`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-variant-alternates): 控制给定的自定义字体的替代字形的使用。
- [`font-variant-caps`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-variant-caps): 控制大写字母替代字形的使用。
- [`font-variant-east-asian` (en-US)](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-east-asian): 控制东亚文字替代字形的使用，像日语和汉语。
- [`font-variant-ligatures`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-variant-ligatures): 控制文本中使用的连写和上下文形式。
- [`font-variant-numeric`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-variant-numeric): 控制数字，分式和序标的替代字形的使用。
- [`font-variant-position`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-variant-position): 控制位于上标或下标处，字号更小的替代字形的使用。
- [`font-size-adjust`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-size-adjust): 独立于字体的实际大小尺寸，调整其可视大小尺寸。
- [`font-stretch`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-stretch): 在给定字体的可选拉伸版本中切换。
- [`text-underline-position`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-underline-position): 指定下划线的排版位置，通过使用 `text-decoration-line` 属性的`underline` 值。
- [`text-rendering`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-rendering): 尝试执行一些文本渲染优化。

文本布局样式：

- [`text-indent`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-indent): 指定文本内容的第一行前面应该留出多少的水平空间。
- [`text-overflow`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-overflow): 定义如何向用户表示存在被隐藏的溢出内容。
- [`white-space`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/white-space): 定义如何处理元素内部的空白和换行。
- [`word-break`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/word-break): 指定是否能在单词内部换行。
- [`direction`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/direction): 定义文本的方向 (这取决于语言，并且通常最好让 HTML 来处理这部分，因为它是和文本内容相关联的。)
- [`hyphens`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/hyphens): 为支持的语言开启或关闭连字符。
- [`line-break`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/line-break): 对东亚语言采用更强或更弱的换行规则。
- [`text-align-last`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-align-last): 定义一个块或行的最后一行，恰好位于一个强制换行前时，如何对齐。
- [`text-orientation`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-orientation): 定义行内文本的方向。
- [`word-wrap`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/overflow-wrap): 指定浏览器是否可以在单词内换行以避免超出范围。
- [`writing-mode`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/writing-mode): 定义文本行布局为水平还是垂直，以及后继文本流的方向。

### Font 简写

许多字体的属性也可以通过 [`font`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font) 的简写方式来设置 . 这些是按照以下顺序来写的： [`font-style`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-style), [`font-variant`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-variant), [`font-weight`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-weight), [`font-stretch`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-stretch), [`font-size`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-size), [`line-height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/line-height), and [`font-family`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-family).

如果你想要使用 `font` 的简写形式，在所有这些属性中，只有 `font-size` 和 `font-family` 是一定要指定的。

[`font-size`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-size) 和 [`line-height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/line-height) 属性之间必须放一个正斜杠。

一个完整的例子如下所示：

```css
font: italic normal bold normal 3em/1.5 Helvetica, Arial, sans-serif;

```

## 样式列表

[List 列表](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals#lists) 大体上和其他文本一样，但是仍有一些你需要知道的特殊 CSS 属性，和一些可供参考的最佳实践，这篇文章将阐述这一切。

### 一个简单的例子

首先，让我们看一个简单的例子。文章中我们将看到无序，有序和描述列表——它们都具有相似的样式特性，而某些特性却又各不相同。

例子中列表的 HTML 代码如下：

```css
<h2>Shopping (unordered) list</h2>

<p>Paragraph for reference, paragraph for reference, paragraph for reference,
paragraph for reference, paragraph for reference, paragraph for reference.</p>

<ul>
  <li>Humous</li>
  <li>Pitta</li>
  <li>Green salad</li>
  <li>Halloumi</li>
</ul>

<h2>Recipe (ordered) list</h2>

<p>Paragraph for reference, paragraph for reference, paragraph for reference,
paragraph for reference, paragraph for reference, paragraph for reference.</p>

<ol>
  <li>Toast pitta, leave to cool, then slice down the edge.</li>
  <li>Fry the halloumi in a shallow, non-stick pan, until browned on both sides.</li>
  <li>Wash and chop the salad.</li>
  <li>Fill pitta with salad, humous, and fried halloumi.</li>
</ol>

<h2>Ingredient description list</h2>

<p>Paragraph for reference, paragraph for reference, paragraph for reference,
paragraph for reference, paragraph for reference, paragraph for reference.</p>

<dl>
  <dt>Humous</dt>
  <dd>A thick dip/sauce generally made from chick peas blended with tahini, lemon juice, salt, garlic, and other ingredients.</dd>
  <dt>Pitta</dt>
  <dd>A soft, slightly leavened flatbread.</dd>
  <dt>Halloumi</dt>
  <dd>A semi-hard, unripened, brined cheese with a higher-than-usual melting point, usually made from goat/sheep milk.</dd>
  <dt>Green salad</dt>
  <dd>That green healthy stuff that many of us just use to garnish kebabs.</dd>
</dl>

```

现在，如果你去到例子的展示页面，并使用[浏览器开发者工具](https://developer.mozilla.org/zh-CN/docs/Learn/Common_questions/What_are_browser_developer_tools)查看那些列表元素，你会注意到若干个默认的样式预设值：

- `<ul>` 和 `<ol>` 元素设置`margin`的顶部和底部：`16px(1em) 0;`和 `padding-left: 40px(2.5em);` （在这里注意的是浏览器默认字体大小为 16px）。

  ![image-20220820205714180](image-20220820205714180.png)

- `<li>` 默认是没有设置间距的。

- `<dl>` 元素设置 `margin` 的顶部和底部：`16px(1em) `，无内边距设定。

- `<dd>` 元素设置为： `margin-left 40px (2.5em)`。

- 在参考中提到的 `<p>` 元素设置 `margin` 的顶部和底部：`16px(1em)`，和其他的列表类型相同。

### 处理列表间距

当您创建样式列表时，您需要调整样式，使其保持与周围元素相同的垂直间距（例如段落和图片，有时称为垂直节奏））和相互间的水平间距（您可以在 Github 上参考[完成的样式示例](https://mdn.github.io/learning-area/css/styling-text/styling-lists/) ，也可以找到[源代码](https://github.com/mdn/learning-area/blob/master/css/styling-text/styling-lists/index.html)。）

用于文本样式和间距的 CSS 如下所示：

```css
/* General styles */

html {
  font-family: Helvetica, Arial, sans-serif;
  font-size: 10px;
}

h2 {
  font-size: 2rem;
}

ul,ol,dl,p {
  font-size: 1.5rem;
}

li, p {
  line-height: 1.5;
}

/* Description list styles */


dd, dt {
  line-height: 1.5;
}

dt {
  font-weight: bold;
}

dd {
  margin-bottom: 1.5rem;
}

```

- 第一条规则集设置一个网站字体，基准字体大小为 10px。页面上的所有内容都将继承该规则集。
- 规则集 2 和 3 为标题、不同的列表类型和段落以及设置了相对字体大小（这些列表的子元素将会继承该规则集），这就意味着每个段落和列表都将拥有相同的字体大小和上下间距，有助于保持垂直间距一致。
- 规则集 4 在段落和列表项目上设置相同的 [`line-height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/line-height) ，因此段落和每个单独的列表项目将在行之间具有相同的间距。这也将有助于保持垂直间距一致。
- 规则集 5-7 适用于描述列表 - 我们在描述列表的术语和其描述上设置与段落和列表项相同的行高，以及 [`margin-bottom`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin-bottom) 为 1.5 rem（与段落（p）和列表项目（li））相同。再次强调一遍，这里很好地实现了一致性！我们还使描述术语具有粗体字体，因此它们在视觉上脱颖而出。



### 列表特定样式

现在我们来看一下列表的一般间距，我们来研究一些列表具有的特定属性。我们从三个属性开始了解，这三个属性可以在 `<ul>` 或 `<ol>` 元素上设置：

- [`list-style-type`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/list-style-type) ：设置用于列表的项目符号的类型，例如无序列表的方形或圆形项目符号，或有序列表的数字，字母或罗马数字。
- [`list-style-position`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/list-style-position) ：设置在每个项目开始之前，项目符号是出现在列表项内，还是出现在其外。
- [`list-style-image`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/list-style-image) ：允许您为项目符号使用自定义图片，而不是简单的方形或圆形。

#### 符号样式

像上面所提及的， [`list-style-type`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/list-style-type) 属性允许你设置项目符号点的类型，在我们的例子中，我们在有序列表上设置了大写罗马数字：

```css
ol {
  list-style-type: upper-roman;
}

```

效果显示如下：

![image-20220821071645272](image-20220821071645272.png)

您可以通过 [`list-style-type`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/list-style-type) 参考页面查找到更多选项。

#### 项目符号位置

[`list-style-position`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/list-style-position) 设置在每个项目开始之前，项目符号是出现在列表项内，还是出现在其外。如上所示，默认值为 outside，这使项目符号位于列表项之外。

如果值设置为 inside，项目条目则位于行内。

![image-20220821071846481](image-20220821071846481.png)

#### 使用自定义的项目符号图片

[`list-style-image`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/list-style-image) 属性允许对于项目符号使用自定义图片。其语法相当简单：

```css
ul {
  list-style-image: url(star.svg);
}

```

然而，这个属性在控制项目符号的位置，大小等方面是有限的。您最好使用[`background`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background) 系列属性，您将在 [Styling boxes](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks) 模块中了解更多信息。在这里我们仅做一点尝试！

结束我们的例子，我们样式化无序列表像这样（放到您之前所见的顶部）：

```css
ul {
  padding-left: 2rem;
  list-style-type: none;
}

ul li {
  padding-left: 2rem;
  background-image: url('https://mdn.github.io/css-examples/learn/backgrounds-borders/star.png');
  background-position: 0 0;
  background-size: 1.6rem 1.6rem;
  background-repeat: no-repeat;
}

```

![image-20220821072236768](image-20220821072236768.png)

我们的所做如下：

- 
- 将 `<ul>` 的`padding-left` 从默认的 40px设置为 20px，然后在列表项上设置相同的数值。这就是说，整个列表项仍然排列在列表中，但是列表项产生了一些用于背景图像的填充。如果我们没有设置填充，背景图像将与列表项文本重叠，这看起来会很乱。
- 将 [`list-style-type`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/list-style-type) 设置为 none，以便默认情况下不会显示项目符号。我们将使用 [`background`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background) 属性来代替项目符号。
- 为每个无序列表项插入项目符号，其相应的属性如下：
  - [`background-image`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-image): 充当项目符号的图片文件的参考路径
  - [`background-position`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-position): 这定义了所选元素背景中的图像将出现在哪里 - 在我们的示例中设置 `0 0`，这意味着项目符号将出现在每个列表项的最左上侧。
  - [`background-size`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-size): 设置背景图片的大小。理想条件下，我们想要项目符号与列表项的大小相同（比列表项稍大或稍小亦可）。我们使用的尺寸为 1.6rem（16px），它非常吻合我们为项目符号设置的 20px 的填充， 16px 加上 4px 的空格间距，可以使项目符号和列表项文本效果更好。
  - [`background-repeat`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-repeat)：默认条件下，背景图片不断复制直到填满整个背景空间，在我们的例子中，背景图片只需复制一次，所以我们设置值为 `no-repeat`。

#### list-style 速记

上述提到的三种属性可以用一个单独的速记属性 [`list-style`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/list-style) 来设置。例如：

```css
ul {
  list-style-type: square;
  list-style-image: url(example.png);
  list-style-position: inside;
}

```

可以被如下方式代替：

```css
ul {
  list-style: square url(example.png) inside;
}

```

属性值可以任意顺序排列，你可以设置一个，两个或者三个值（该属性的默认值为 disc, none, outside），如果指定了 type 和 image，如果由于某种原因导致图像无法加载，则 type 将用作回退。



### 管理列表计数

有时，您可能想在有序列表上进行不同的计数方式。例如：从 1 以外的数字开始，或向后倒数，或者按步或多于 1 计数。HTML 和 CSS 有一些工具可以帮助您

#### start

[`start`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/ol#attr-start) 属性允许你从 1 以外的数字开始计数。示例如下：

```html
<ol start="4">
  <li>Toast pitta, leave to cool, then slice down the edge.</li>
  <li>Fry the halloumi in a shallow, non-stick pan, until browned on both sides.</li>
  <li>Wash and chop the salad.</li>
  <li>Fill pitta with salad, humous, and fried halloumi.</li>
</ol>

```

输出的结果如下：

![image-20220821072608841](image-20220821072608841.png)

#### reversed

[`reversed`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/ol#attr-reversed) 属性将启动列表倒计数。示例如下：

```html
<ol start="4" reversed>
  <li>Toast pitta, leave to cool, then slice down the edge.</li>
  <li>Fry the halloumi in a shallow, non-stick pan, until browned on both sides.</li>
  <li>Wash and chop the salad.</li>
  <li>Fill pitta with salad, humous, and fried halloumi.</li>
</ol>

```

![image-20220821072737083](image-20220821072737083.png)

#### value

[`value`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/ol#attr-value) 属性允许设置列表项指定数值，示例如下：

```html
<ol>
  <li value="2">Toast pitta, leave to cool, then slice down the edge.</li>
  <li value="4">Fry the halloumi in a shallow, non-stick pan, until browned on both sides.</li>
  <li value="6">Wash and chop the salad.</li>
  <li value="8">Fill pitta with salad, humous, and fried halloumi.</li>
</ol>

```

![image-20220821072828812](image-20220821072828812.png)

> **备注：** 纵然你使用非数字的 [`list-style-type`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/list-style-type), 你仍需要使用与数值同等意义的值作为 value 的属性。

## 样式化链接

当为 [links](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks) 添加样式时，理解利用伪类有效地建立链接状态是很重要的，以及如何为链接添加样式来实现常用的功能，比如说导航栏、选项卡。我们将在本文中关注所有这些主题。

### 让我们来看一些链接

根据最佳实践 [创建超链接](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks) 中的练习，我们看到了如何在你的 HTML 中实现链接。在本篇文章中，我们会以这个知识为基础，向你展示将样式应用到链接的最佳实践

#### 链接状态

第一件需要理解的事情是链接状态的概念，链接存在时处于不同的状态，每一个状态都可以用对应的 [伪类](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors#pseudo-classes) 来应用样式：

- **Link (没有访问过的)**: 这是链接的默认状态，当它没有处在其他状态的时候，它可以使用[`:link`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:link) 伪类来应用样式。
- **Visited**: 这个链接已经被访问过了 (存在于浏览器的历史纪录), 它可以使用 [`:visited`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:visited) 伪类来应用样式。
- **Hover**: 当用户的鼠标光标刚好停留在这个链接，它可以使用 [`:hover`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:hover) 伪类来应用样式。
- **Focus**: 一个链接当它被选中的时候 (比如通过键盘的 Tab 移动到这个链接的时候，或者使用编程的方法来选中这个链接 [`HTMLElement.focus()` (en-US)](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus)) 它可以使用 [`:focus`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:focus) 伪类来应用样式。
- **Active**: 一个链接当它被激活的时候 (比如被点击的时候)，它可以使用 [`:active`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:active) 伪类来应用样式。



#### 默认的样式

下面的例子说明了一个链接的默认行为表现 (这里的 CSS 仅仅是为了放大和居中文本，使内容更加突出)

```html
<p><a href="https://mozilla.org">A link to the Mozilla homepage</a></p>

```



```html
p {
  font-size: 2rem;
  text-align: center;
}

```

当你观察默认样式的时候，你也许会注意到一些东西：

- 链接具有下划线。
- 未访问过的 (Unvisited) 的链接是蓝色的。
- 访问过的 (Visited) 的链接是紫色的。
- 悬停 (Hover) 在一个链接的时候鼠标的光标会变成一个小手的图标。
- 选中 (Focus) 链接的时候，链接周围会有一个轮廓，你应该可以按 tab 来选中这个页面的链接 (在 Mac 上，你可能需要使用*Full Keyboard Access: All controls* 选项，然后再按下 Ctrl + F7 ，这样就可以起作用)
- 激活 (Active) 链接的时候会变成红色 (当你点击链接时，请尝试按住鼠标按钮。)

有趣的是，这些默认的样式与 20 世纪 90 年代中期浏览器早期的风格几乎相同。这是因为用户知道以及期待链接就是这样变化的，如果链接的样式不同，就会让一些人感到奇怪。不过这不意味着你不应该为链接添加任何样式，只是你的样式不应该与用户预期的相差太大，你应该至少：

- 为链接使用下划线，但是不要在其他内容上也用下划线，以作区分。如果你不想要带有下划线的链接，那你至少要用其他方法来高亮突出链接。
- 当用户悬停或选择 (hover 或者 focused) 的时候，使链接有相应的变化，并且在链接被激活 (active) 的时候，变化会有一些不同。可以使用以下 CSS 属性关闭/更改默认样式：
- [`color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/color) 文字的颜色
- [`cursor`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/cursor) 鼠标光标的样式，你不应该把这个关掉，除非你有非常好的理由。
- [`outline`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/outline) 文字的轮廓 (轮廓有点像边框，唯一的区别是边框占用了盒模型的空间，而轮廓没有； 它只是设置在背景图片的顶部)。outline 是一个有用的辅助功能，所以在把它关掉之前考虑清楚；你至少应该将悬停 (hover) 状态的样式同时应用到选中 (focus) 状态上。

#### 将样式应用到一些链接

现在我们已经详细地看了默认的状态，让我们看一下典型的链接样式的设置。

开始之前，我们先写出我们的空规则集：

```css
a {

}


a:link {

}

a:visited {

}

a:focus {

}

a:hover {

}

a:active {

}

```

这几个规则的顺序是有意义的，因为链接的样式是建立在另一个样式之上的，比如，第一个规则的样式也会在后面的规则中生效，一个链接被激活 (activated) 的时候，它也是处于悬停 (hover) 状态的。如果你搞错了顺序，那么就可能不会产生正确的效果。要记住这个顺序，你可以尝试这样帮助记忆：**L**o**V**e **F**ears **HA**te.

现在让我们再添加一些信息，得到正确的样式：

```css
body {
    width: 300px;
    margin: 0 auto;
    font-size: 1.2rem;
    font-family: sans-serif;
}

p {
    line-height: 1.4;
}

a {
    outline: none;
    text-decoration: none;
    padding: 2px 1px 0;
}

a:link {
    color: #265301;
}

a:visited {
    color: #437A16;
}

a:focus {
    border-bottom: 1px solid;
    background: #BAE498;
}

a:hover {
    border-bottom: 1px solid;
    background: #CDFEAA;
}

a:active {
    background: #265301;
    color: #CDFEAA;
}
```

```html
<p>There are several browsers available, such as <a href="https://www.mozilla.org/zh-CN/firefox/">Mozilla
Firefox</a>, <a href="https://www.google.com/chrome/index.html">Google Chrome</a>, and
<a href="https://www.microsoft.com/zh-CN/windows/microsoft-edge">Microsoft Edge</a>.</p>

```

![image-20220821073753159](image-20220821073753159.png)

### 在链接中包含图标

常见的做法是在链接中包含图标，使链接提供更多关于链接指向的内容的信息。让我们来看一个简单的例子，例子中为一个外部链接 (链接指向的不是本站，而是外部站点)。这样的图标通常看起来像一个指向盒子的小箭头，比如，我们会使用[icons8.com 上的这个优秀的范例](https://icons8.com/web-app/741/external-link)。

让我们来看一些能给我们这个效果的 HTML 和 CSS。先是一些简单的等待你样式化的 HTML：

```html
<p>For more information on the weather, visit our <a href="weather.html">weather page</a>,
look at <a href="https://en.wikipedia.org/wiki/Weather">weather on Wikipedia</a>, or check
out <a href="http://www.extremescience.com/weather.htm">weather on Extreme Science</a>.</p>

```

```css
body {
  width: 300px;
  margin: 0 auto;
  font-family: sans-serif;
}

p {
  line-height: 1.4;
}

a {
  outline: none;
  text-decoration: none;
  padding: 2px 1px 0;
}

a:link {
  color: blue;
}

a:visited {
  color: purple;
}

a:focus, a:hover {
  border-bottom: 1px solid;
}

a:active {
  color: red;
}

a[href*="http"] {
  background: url('https://mdn.mozillademos.org/files/12982/external-link-52.png') no-repeat 100% 0;
  background-size: 16px 16px;
  padding-right: 19px;
}

```



那么这里发生了什么？我们将跳过大部分的 CSS，因为那些只是你之前看过的相同的信息。最后一条规则很有趣，这里，我们在外部链接上插入了一个自定义背景图片，这和上篇[自定义列表项目符号](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Styling_text/Styling_lists#using_a_custom_bullet_image)文章的做法很像。这次，我们使用了 [`background`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background) 简写，而不是分别使用多个属性。我们设置了我们想要插入的图片的路径，指定了 `no-repeat` ，这样我们只插入了一次图片，然后指定位置为 100%，使其出现在内容的右边，距离上方是 0px。

我们也使用 [`background-size`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-size) 来指定要显示的背景图像的大小，为了满足响应式网站设计的需要，在图标更大，需要再重新调整它的大小的时候，这样做是很有帮助的。但是，这仅适用于 IE 9 及更高版本。所以你如果需要支持那些老的浏览器，只能调整图像的原始大小，然后插入。

最后，我们在链接上设置 [`padding-right`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding-right) ，为背景图片留出空间，这样就不会让它和文本重叠了。

最后的问题，我们是如何只选中了外部链接的？如果你正确编写你的`HTML` 链接 ，你应该只会在外部链接上使用绝对 `URL`，如果链接是链接你的站点的其他部分，那么使用相对链接是更加高效的。因此“`http`”文本应该只出现在外部链接上，为此我们可以使用一个属性选择器——`a[href*="http"]` ——选中`<a>` 元素，但是这样只会选中那些拥有 `href` 属性，且属性的值包含 "`http`" 的 `<a>`的元素。

就这样啦，尝试重新审视上面的动手练习部分，尝试这种新技术！

### 样式化链接为按钮

目前在本文中探索的用法也可以用在其他方面。比如，悬停 (hover) 的状态可以为不同的元素应用样式，不只是链接，你也许会想添加悬停状态的样式到段落、列表项、或者是其他东西。

此外，在某些情况下，链接通常会应用样式，使它看上去的效果和按钮差不多，一个网站导航菜单通常是标记为一个列表，列表中包含链接，这可以很容易地被设计为看起来像一组控制按钮或是选项卡，主要是用于让用户可以访问站点的其他部分，现在让我们来看一看。

```html
    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">Pizza</a></li>
        <li><a href="#">Music</a></li>
        <li><a href="#">Wombats</a></li>
        <li><a href="#">Finland</a></li>
    </ul>
```

```css
body,
html {
    margin: 0;
    font-family: sans-serif;
}

ul {
    padding: 0;
    width: 100%;
}

li {
    display: inline;
}

a {
    outline: none;
    text-decoration: none;
    display: inline-block;
    width: 19.5%;
    margin-right: 0.625%;
    text-align: center;
    line-height: 3;
    color: black;
}

li:last-child a {
    margin-right: 0;
}

a:link,
a:visited,
a:focus {
    background: yellow;
}

a:hover {
    background: orange;
}

a:active {
    background: red;
    color: white;
}
```

![image-20220821074929735](image-20220821074929735.png)

### 小结

我们希望本文为你提供有关链接的所有知识——目前！我们的样式文本模块中的最后一篇文章详细介绍了如何在你的网站上使用自定义字体，或者更熟悉网络字体。

## Web 字体

在模块的第一篇文章中，我们探讨了用于样式化字体和文本的基本 CSS 特性。在这篇文章中，我们将更进一步，详细地探索 web 字体——它们允许您下载自定义字体和您的 web 页面，以允许更多不同的、自定义的文本样式。

### 字体种类回顾

正如我们在[基本文本和字体样式](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals)中所看到的那样，应用到您的 HTML 的字体可以使用 [`font-family`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-family)属性来控制。您需要提供一个或多个字体种类名称，浏览器会在列表中搜寻，直到找到它所运行的系统上可用的字体。

```css
p {
  font-family: Helvetica, "Trebuchet MS", Verdana, sans-serif;
}

```

这个系统运行良好，但是对于传统的 web 开发人员来说，字体选择是有限的。只有少数几种字体可以保证兼容所有流行的操作系统——这就是所谓的 [Web-safe 字体](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals#web_safe_fonts)。您可以使用字体堆栈来指定可选择的字体，后面是 Web-safe 的替代选项，然后是默认的系统字体，但是为了确保您的设计在每种字体中都显示正常，这样增加了测试的开销。



### Web 字体

但是还有一种选择，它非常有效，回到 IE 版本 6。Web 字体是一种 CSS 特性，允许您指定在访问时随您的网站一起下载的字体文件，这意味着任何支持 Web 字体的浏览器都可以使用您指定的字体。太酷啦！所需的语法如下所示：

首先，在 CSS 的开始处有一个[`@font-face`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/@font-face)块，它指定要下载的字体文件：

```css
@font-face {
  font-family: "myFont";
  src: url("myFont.ttf");
}

```

在这个下面，你可以使用 @font-face 中指定的字体种类名称来将你的定制字体应用到你喜欢的任何东西上，比如说：

```css
html {
  font-family: "myFont", "Bitstream Vera Serif", serif;
}

```

语法确实比这更复杂，下面我们将详细介绍。

关于网页字体有两件重要的事情要记住：

1. 浏览器支持不同的字体格式，因此您需要多种字体格式以获得良好的跨浏览器支持。例如，大多数现代浏览器都支持 WOFF / WOFF2(Web Open Font Format versions 1 and 2，Web 开放字体格式版本 1 和 2)，它是最有效的格式，但是旧版本 IE 只支持 EOT (Embedded Open Type，嵌入式开放类型) 的字体，你可能需要包括一个 SVG 版本的字体支持旧版本的 iPhone 和 Android 浏览器。我们将向您展示如何生成所需的代码。
2. 字体一般都不能自由使用。您必须为他们付费，或者遵循其他许可条件，比如在代码中 (或者在您的站点上) 提供字体创建者。你不应该在没有适当的授权的情况下偷窃字体。

> **备注：** Web 字体作为一种技术从 Internet Explorer 4 开始就得到了的支持！



### 自主学习:web 字体示例

你应该使用 [web-font-start.html](https://github.com/mdn/learning-area/blob/master/css/styling-text/web-fonts/web-font-start.html) 和 [web-font-start.css](https://github.com/mdn/learning-area/blob/master/css/styling-text/web-fonts/web-font-start.css) 文件作为开始添加到你的代码中（又见[预览版](https://mdn.github.io/learning-area/css/styling-text/web-fonts/web-font-start.html)。）现在，在你的电脑上的一个新目录中复制这些文件。在 `web-font-start.css`文件中，您将找到一些最小的 CSS 来处理这个示例的基本布局和排版。

```html
<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Web font example</title>
    <link href="web-font-start.css" rel="stylesheet" type="text/css">
  </head>
  <body>
    <h1>Hipster ipsum is the best</h1>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl typewriter. Tacos PBR&amp;B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin coffee cold-pressed. PBR&amp;B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub hammock.</p>

    <p>Cray food truck brunch, XOXO +1 keffiyeh pickled chambray waistcoat ennui. Organic small batch paleo 8-bit. Intelligentsia umami wayfarers pickled, asymmetrical kombucha letterpress kitsch leggings cold-pressed squid chartreuse put a bird on it. Listicle pickled man bun cornhole heirloom art party.</p>

    <h2>It is the quaintest</h2>

    <p>Bespoke green juice aesthetic leggings DIY williamsburg selvage. Bespoke health goth tote bag, fingerstache venmo ennui thundercats butcher trust fund cardigan hella. Wolf vinyl you probably haven't heard of them taxidermy, ugh quinoa neutra meditation asymmetrical mixtape church-key kitsch man bun occupy. Knausgaard butcher raw denim ramps, offal seitan williamsburg venmo gastropub mlkshk cardigan chillwave chartreuse single-origin coffee twee. Ethical asymmetrical banjo typewriter fap. Polaroid waistcoat tousled selfies four dollar toast locavore thundercats. Truffaut post-ironic skateboard trust fund.</p>

    <h2>No, really...</h2>

    <p>Trust fund celiac farm-to-table PBR&amp;B. Brunch art party mumblecore, fingerstache cred echo park literally stumptown humblebrag chambray. Mlkshk vinyl distillery humblebrag crucifix. Mustache craft beer put a bird on it, irony deep v poutine ramps williamsburg heirloom brooklyn.</p>

    <p>Taxidermy tofu YOLO, sustainable etsy flexitarian art party stumptown portland. Ethical williamsburg retro paleo. Put a bird on it leggings yuccie actually, skateboard jean shorts paleo lomo salvia plaid you probably haven't heard of them.</p>
  </body>
</html>
```

```css
/* General setup */

html {
    font-size: 10px;
    margin: 0;
    font-family: sans-serif;
}

body {
    width: 80%;
    max-width: 800px;
    margin: 0 auto;
}

/* Typography */

h1 {
    font-size: 4.2rem;
    font-family: 'alex_brushregular', serif;
}

h2 {
    font-size: 3rem;
    font-family: 'alex_brushregular', serif;
}

p {
    font-size: 1.8rem;
    line-height: 1.6;
    word-spacing: 0.6rem;
    font-family: 'milkshakeregular', serif;
}

/*! Generated by Font Squirrel (https://www.fontsquirrel.com) on August 20, 2022 */



@font-face {
    font-family: 'alex_brushregular';
    src: url('./fonts/alexbrush-regular-webfont.woff2') format('woff2'),
        url('./fonts/alexbrush-regular-webfont.woff') format('woff');
    font-weight: normal;
    font-style: normal;

}

@font-face {
    font-family: 'milkshakeregular';
    src: url('./fonts/milkshake-webfont.woff2') format('woff2'),
        url('./fonts/milkshake-webfont.woff') format('woff');
    font-weight: normal;
    font-style: normal;

}
```

#### 查找字体

对于本例，我们将使用两种 web 字体，一种用于标题，另一种用于正文文本。首先，我们需要找到包含字体的字体文件。字体是由字体铸造厂创建的，并且存储在不同的文件格式中。 通常有三种类型的网站可以获得字体：

- 免费的字体经销商：这是一个可以下载免费字体的网站 (可能还有一些许可条件，比如对字体创建者的信赖)。比如： [Font Squirre](https://www.fontsquirrel.com/)，[dafont](http://www.dafont.com/) 和 [Everything Fonts](https://everythingfonts.com/)。
- 收费的字体经销商：这是一个收费则字体可用的网站，例如[fonts.com](http://www.fonts.com/)或[myfonts.com](http://www.myfonts.com/)。您也可以直接从字体铸造厂中购买字体，例如[Linotype](https://www.linotype.com/)，[Monotype](http://www.monotype.com/) 或 [Exljbris](http://www.exljbris.com/)。
- 在线字体服务：这是一个存储和为你提供字体的网站，它使整个过程更容易。更多细节见[使用在线字体服务](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Styling_text/Web_fonts#使用在线字体服务)。



下载一：https://www.boldfacedgoods.com/a/downloads/-/aa79fcef4a602fe5/fdee7b4c0ccf9008

下载二：https://www.fontsquirrel.com/fonts/download/alex-brush

让我们找到一些字体！前往[Font Squirrel](https://www.fontsquirrel.com/) 并选择两种字体——一种用于标题的有趣的字体 (可能是一种不错的显示字体或无衬线字体)，和一种用于段落，稍微不那么华丽，更易于阅读的字体。当您找到每种字体时，按下下载按钮，并将该文件保存在与您先前保存的 HTML 和 CSS 文件相同的目录中。无论它们是 TTF(True Type Fonts)) 还是 OTF(Open Type 字体) 都不重要。

在每种情况下，都要解压字体包 (Web 字体通常分布在包含字体文件和许可信息的 ZIP 文件中。) 您可能会在包中发现多个字体文件，一些字体是作为一个具有不同变体的家庭分布的，例如，瘦、中、粗体、斜体、斜体等等。对于这个例子，我们只是想让您自己考虑一个单一的字体文件。

#### 生成所需代码

现在您需要生成所需的代码 (以及字体格式)。对于每种字体，遵循以下步骤：

1. 确保您已经满足了任何许可证的要求，如果您打算在一个商业和/或 Web 项目中使用它。
2. 前往 Fontsquirrel [Webfont Generator](https://www.fontsquirrel.com/tools/webfont-generator).
3. 使用上传字体按钮上传你的两个字体文件。
4. 勾选复选框，“是的，我上传的字体符合网络嵌入的合法条件。
5. 点击下载你的套件（kit）。

在生成器完成处理之后，您应该得到一个 ZIP 文件，将它保存在与 HTML 和 CSS 相同的目录中。

#### 在演示中实现代码

在这一点上解压您刚刚生成的 webfont 套件。在解压的目录中，您将看到三个有用的条目：

- 每个字体的多个版本：（比如 `.ttf`, `.woff`, `.woff2`…… 随着浏览器支持需求的改变，提供的字体将随着时间的推移而不断更新。）正如上面提到的，跨浏览器支持需要使用多种字体——这是 Fontsquirrel 的方法，确保你得到了你需要的一切。
- 每个字体的一个演示 HTML 文件在你的浏览器中加载，看看在不同的使用环境下字体会是什么样子。
- 一个 `stylesheet.css` 文件，它包含了你需要的生成好的 @font-face 代码。

要在演示中实现这些字体，请遵循以下步骤：

1. 将解压缩的目录重命名为简易的目录，比如`fonts`

2. 打开 `stylesheet.css` 文件，把包含在你的网页中的 `@font-face`块复制到你的 `web-font-start.css` 文件—— 你需要把它们放在最上面，在你的 CSS 之前，因为字体需要导入才能在你的网站上使用。

3. 每个`url()`函数指向一个我们想要导入到我们的 CSS 中的字体文件——我们需要确保文件的路径是正确的，因此，在每个路径的开头添加`fonts/` （必要时进行调整）。

4. 现在，您可以在字体栈中使用这些字体，就像任何 web 安全或默认的系统字体一样。 例如：

   ```csss
   font-family: 'zantrokeregular', serif;
   ```

你应该得到一个演示页面，上面有一些漂亮的字体。因为不同字体的字体大小不同，你可能需要调整大小、间距等，以区分外观和感觉。

![image-20220821101636128](image-20220821101636128.png)



### 使用在线字体服务

在线字体服务通常会为你存储和服务字体，这样你就不用担心写`@font-face`代码了，通常只需要在你的网站上插入一两行代码就可以让一切都运行。例子包括[Typekit](https://typekit.com/) 和[Cloud.typography](http://www.typography.com/cloud/welcome/)。大多数这些服务都是基于订阅的，除了[Google Fonts](https://www.google.com/fonts)，这是一个有用的免费服务，特别是对于快速的测试工作和编写演示。

大多数这些服务都很容易使用，所以我们不会详细地介绍它们。让我们快速浏览一下 Google Fonts，这样你就能明白它的意思了。再次的，使用`web-font-start.html` 和 `web-font-start.css` a 的副本作为你的开始。

1. 前往 [Google Fonts](https://www.google.com/fonts).
2. 使用左边的过滤器来显示你想要选择的字体类型，并选择一些你喜欢的字体。
3. 要选择字体种类，按下按钮旁边的 ⊕ 按钮。
4. 当您选择好字体种类时，按下页面底部的*[Number]* 种类选择。
5. 在生成的屏幕中，首先需要复制所显示的 HTML 代码行，并将其粘贴到 HTML 文件的头部。将其置于现有的[``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/link)元素之上，使得字体是导入的，然后在你的 CSS 中使用它。
6. 然后，您需要将 CSS 声明复制到您的 CSS 中，以便将自定义字体应用到您的 HTML。



就是引用在线的字体样式

### 关于 @font-face 的更多细节

让我们来探索由 fontsquirrel 为您生成的`@font-face`语法。这是其中一个块的样子：

```css
@font-face {
  font-family: 'ciclefina';
  src: url('fonts/cicle_fina-webfont.eot');
  src: url('fonts/cicle_fina-webfont.eot?#iefix') format('embedded-opentype'),
         url('fonts/cicle_fina-webfont.woff2') format('woff2'),
         url('fonts/cicle_fina-webfont.woff') format('woff'),
         url('fonts/cicle_fina-webfont.ttf') format('truetype'),
         url('fonts/cicle_fina-webfont.svg#ciclefina') format('svg');
  font-weight: normal;
  font-style: normal;
}

```

这被称为"bulletproof @font-face syntax（刀枪不入的 @font-face 语法）", 这是 Paul Irish 早期的一篇文章提及后 @font-face 开始流行起来 ([Bulletproof @font-face Syntax](https://www.paulirish.com/2009/bulletproof-font-face-implementation-syntax/)。让我们来看看它是怎么做的：

- `font-family`：这一行指定了您想要引用的字体的名称。你可以把它作为你喜欢的任何东西，只要你在你的 CSS 中始终如一地使用它。
- `src`：这些行指定要导入到您的 CSS(`url`部分) 的字体文件的路径，以及每种字体文件的格式 (`format`部分)。后面的部分不是必要的，但是声明它是很有用的，因为它允许浏览器更快地找到可以使用的字体。可以列出多个声明，用逗号分隔——浏览器会搜索并使用它能找到的第一个——因此，最好是把新的、更好的格式比如 WOFF2 放在前面，把偏老的，不是那么好的格式像 TTF 这样的放在后面。唯一的例外是 EOT 字体——他们首先在旧版本的 IE 中修复了几个 bug，这样它就会尝试使用它找到的第一件东西，即使它不能真正使用字体。
- [`font-weight`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-weight)/[`font-style`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-style): 这些行指定字体的粗细，以及它是否斜体。如果您正在导入相同字体的多个粗细，您可以指定它们的粗细/样式，然后使用不同的[`font-weight`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-weight)/[`font-style`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-style)来选择它们之间的不同值，而不必调用字体种类不同名称的所有不同成员。Roger Johansson 写的 [@font-face tip: define font-weight and font-style to keep your CSS simple](http://www.456bereastreet.com/archive/201012/font-face_tip_define_font-weight_and_font-style_to_keep_your_css_simple/) 更详细地说明了该做些什么。

# `CSS`排版

此刻，我们已经看过 CSS 的基础知识，如何设置文本的样式，以及如何设置和操作内容所在的框。现在是时候看看如何把你的盒子放在与视口相关的正确位置上。我们已经涵盖了必要的先决条件，所以我们现在可以深入到 CSS 布局，查看不同的显示设置，涉及浮动和定位的传统布局方法，以及像 flexbox 这样的现代布局工具。

## 介绍 CSS 布局

本文将回顾我们以前模块中已经介绍过的一些 CSS 布局特性——例如不同的[`display`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/display)值——并介绍我们将在本模块中使用的一些概念。

CSS 页面布局技术允许我们拾取网页中的元素，并且控制它们相对正常布局流、周边元素、父容器或者主视口/窗口的位置。在这个模块中将涉及更多关于页面[布局技术](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Layout_mode)的细节：

- 正常布局流
- [`display`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/display)属性
- 弹性盒子
- 网格
- 浮动
- 定位
- CSS 表格布局
- 多列布局

每种技术都有它们的用途，各有优缺点，相互辅助。通过理解各个布局方法的设计理念，你能够找到构建你想要的网页需要的布局方案。

### 正常布局流 (Normal flow)

正常布局流 (normal flow) 是指在不对页面进行任何布局控制时，浏览器默认的 HTML 布局方式。让我们快速地看一个 HTML 的例子：

```html
<p>I love my cat.</p>

<ul>
  <li>Buy cat food</li>
  <li>Exercise</li>
  <li>Cheer up friend</li>
</ul>

<p>The end!</p>

```

默认情况下，浏览器的显示如下：

![image-20220821103525993](image-20220821103525993.png)



注意，HTML 元素完全按照源码中出现的先后次序显示——第一个段落、无序列表、第二个段落。

出现在另一个元素下面的元素被描述为**块**元素，与出现在另一个元素旁边的**内联元素**不同，内联元素就像段落中的单个单词一样。

> **备注：** 块元素内容的布局方向被描述为**块方向**。块方向在英语等具有水平**书写模式**(`writing mode`) 的语言中垂直运行。它可以在任何垂直书写模式的语言中水平运行。对应的**内联方向**是内联内容（如句子）的运行方向。

当你使用 css 创建一个布局时，你正在离开**正常布局流**，但是对于页面上的多数元素，**正常布局流**将完全可以创建你所需要的布局。从一个结构良好的 Html 文档开始是非常重要，因为你可以按照默认的方式来搭建页面，而不是自造车轮。

下列布局技术会覆盖默认的布局行为：

- **[`display`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/display)** 属性 — 标准的 value，比如`block`, `inline` 或者 `inline-block` 元素在正常布局流中的表现形式 (见 [Types of CSS boxes](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model#types_of_css_boxes)). 接着是全新的布局方式，通过设置`display`的值，比如 [CSS Grid](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Grids) 和 [Flexbox](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox).
- **浮动**——应用 **[`float`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/float)** 值，诸如 `left` 能够让块级元素互相并排成一行，而不是一个堆叠在另一个上面。
- **[`position`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/position)** 属性 — 允许你精准设置盒子中的盒子的位置，正常布局流中，默认为 `static` ，使用其它值会引起元素不同的布局方式，例如将元素固定到浏览器视口的左上角。
- **表格布局**— 表格的布局方式可以用在非表格内容上，可以使用`display: table`和相关属性在非表元素上使用。
- **多列布局**— 这个 [Multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Columns) 属性 可以让块按列布局，比如报纸的内容就是一列一列排布的。

### display 属性

在 css 中实现页面布局的主要方法是设定`display`属性的值。此属性允许我们更改默认的显示方式。正常流中的所有内容都有一个`display`的值，用作元素的默认行为方式。例如，英文段落显示在一个段落的下面，这是因为它们的样式是`display:block`。如果在段落中的某个文本周围创建链接，则该链接将与文本的其余部分保持内联，并且不会打断到新行。这是因为[`<a>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a)元素默认为`display:inline`。

您可以更改此默认显示行为。例如，[`<li>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/li)元素默认为`display:block`，这意味着在我们的英文文档中，列表项显示为一个在另一个之下。如果我们将显示值更改为`inline`，它们现在将显示在彼此旁边，就像单词在句子中所做的那样。事实上，您可以更改任何元素的`display`值，这意味着您可以根据它们的语义选择 html 元素，而不必关心它们的外观。他们的样子是你可以改变的。

除了可以通过将一些内容从`block`转换为`inline`（反之亦然）来更改默认表示形式之外，还有一些更大的布局方法以`display`值开始。但是，在使用这些属性时，通常需要调用其他属性。在讨论布局时，对我们来说最重要的两个值是`display`:`flex`和`display`:`grid`。

### 弹性盒子

Flexbox 是 CSS 弹性盒子布局模块（[Flexible Box Layout](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Flexible_Box_Layout) Module）的缩写，它被专门设计出来用于创建横向或是纵向的一维页面布局。要使用 flexbox，你只需要在想要进行 flex 布局的父元素上应用`display: flex` ，所有直接子元素都将会按照 flex 进行布局。我们来看一个例子。

#### 设置 display:flex

下面这些 HTML 标记描述了一个 class 为`wrapper`的容器元素，它的内部有三个`<div>`元素。它们在我们的英文文档当中，会默认地作为块元素从上到下进行显示。

现在，当我们把`display: flex`添加到它的父元素时，这三个元素就自动按列进行排列。这是由于它们变成了*flex 项 (flex items)*，按照 flex 容器（也就是它们的父元素）的一些 flex 相关的初值进行 flex 布局：它们整整齐齐排成一行，是因为父元素上`flex-direction`的初值是`row`。它们全都被拉伸至和最高的元素高度相同，是因为父元素上`align-items`属性的初值是`stretch`。这就意味着所有的子元素都会被拉伸到它们的 flex 容器的高度，在这个案例里就是所有 flex 项中最高的一项。所有项目都从容器的开始位置进行排列，排列成一行后，在尾部留下一片空白。

```html
<div class="wrapper">
  <div class="box1">One</div>
  <div class="box2">Two</div>
  <div class="box3">Three</div>
</div>

```

``` css
.wrapper {
  display: flex;
}

```

![image-20220821151440957](image-20220821151440957.png)

#### 设置 flex 属性

除了上述可以被应用到 flex 容器的属性以外，还有很多属性可以被应用到 flex 项 (flex items) 上面。这些属性可以改变 flex 项在 flex 布局中占用宽/高的方式，允许它们通过伸缩来适应可用空间。

作为一个简单的例子，我们可以在我们的所有子元素上添加[`flex`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex) 属性，并赋值为`1`，这会使得所有的子元素都伸展并填充容器，而不是在尾部留下空白，如果有更多空间，那么子元素们就会变得更宽，反之，他们就会变得更窄。除此之外，如果你在 HTML 标记中添加了一个新元素，那么它们也会变得更小，来为新元素创造空间——不管怎样，最终它们会调整自己直到占用相同宽度的空间。

```css
.wrapper {
    display: flex;
  }
.box1, .box2, .box3 {
    flex: 1;
    background-color: rgb(93, 205, 224);
    margin: 0 10px;
}  
```

![image-20220821151957722](image-20220821151957722.png)



> **备注：** 为了找到更多关于 Flexbox 的信息，看看我们的 [Flexbox](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox) 的文章。

### Grid 布局

Flexbox 用于设计横向或纵向的布局，而 Grid 布局则被设计用于同时在两个维度上把元素按行和列排列整齐。

#### 设置 display: grid

同 flex 一样，你可以通过指定 display 的值来转到 grid 布局：`display: grid`。下面的例子使用了与 flex 例子类似的 HTML 标记，描述了一个容器和若干子元素。除了使用`display:grid`，我们还分别使用 [`grid-template-rows`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/grid-template-rows) 和 [`grid-template-columns`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/grid-template-columns) 两个属性定义了一些行和列的轨道。定义了三个`1fr`的列，还有两个`100px`的行之后，无需再在子元素上指定任何规则，它们自动地排列到了我们创建的格子当中。

```html
<div class="wrapper">
    <div class="box1">One</div>
    <div class="box2">Two</div>
    <div class="box3">Three</div>
    <div class="box4">Four</div>
    <div class="box5">Five</div>
    <div class="box6">Six</div>
</div>

```

```css
.wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 100px 100px;
    grid-gap: 10px;
}

```

#### 在网格内放置元素

一旦你拥有了一个 grid，你也可以显式地将元素摆放在里面，而不是依赖于浏览器进行自动排列。在下面的第二个例子里，我们定义了一个和上面一样的 grid，但是这一次我们只有三个子元素。我们利用 [`grid-column`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/grid-column) 和 [`grid-row`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/grid-row) 两个属性来指定每一个子元素应该从哪一行/列开始，并在哪一行/列结束。这就能够让子元素在多个行/列上展开。

```html
<div class="wrapper">
    <div class="box1">One</div>
    <div class="box2">Two</div>
    <div class="box3">Three</div>
</div>

```

```css
.wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 100px 100px;
    grid-gap: 10px;
}

.box1 {
    grid-column: 2 / 4;
    grid-row: 1;
}

.box2 {
    grid-column: 1;
    grid-row: 1 / 3;
}

.box3 {
    grid-row: 2;
    grid-column: 3;
}

.wrapper > div {
    background-color: rgb(82, 212, 195);
}
```

> **备注：** 这两个例子只是展示了 grid 布局的冰山一角，要深入了解 grid 布局，请参阅我们的文章[Grid Layout](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Grids)。
>
> 这篇指南的其余部分介绍了其他

这篇指南的其余部分介绍了其他的布局方式，它们与你的页面的主要布局结构关系不大，但是却能够帮助你实现特殊的操作。同时，只要你理解了每一个布局任务的初衷，你就能够马上意识到哪一种布局更适合你的组件。

### 浮动

把一个元素“浮动”(float) 起来，会改变该元素本身和在正常布局流（normal flow）中跟随它的其他元素的行为。这一元素会浮动到左侧或右侧，并且从正常布局流 (normal flow) 中移除，这时候其他的周围内容就会在这个被设置浮动 ([`float`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/float)) 的元素周围环绕。

[`float`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/float) 属性有四个可能的值：

- `left` — 将元素浮动到左侧。
- `right` — 将元素浮动到右侧。
- `none` — 默认值，不浮动。
- `inherit` — 继承父元素的浮动属性。

在下面这个例子当中，我们把一个`<div>`元素浮动到左侧，并且给了他一个右侧的[`margin`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin)，把文字推开。这给了我们文字环绕着这个`<div>`元素的效果，在现代网页设计当中，这是你唯一需要学会的事情。

```html
<h1>Simple float example</h1>

<div class="box">Float</div>

<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus aliquam dolor, eu lacinia lorem placerat vulputate. Duis felis orci, pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at ultricies tellus laoreet sit amet. Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet orci vel, viverra egestas ligula. Curabitur vehicula tellus neque, ac ornare ex malesuada et. In vitae convallis lacus. Aliquam erat volutpat. Suspendisse ac imperdiet turpis. Aenean finibus sollicitudin eros pharetra congue. Duis ornare egestas augue ut luctus. Proin blandit quam nec lacus varius commodo et a urna. Ut id ornare felis, eget fermentum sapien.</p>

```

```css
.box {
    float: left;
    width: 150px;
    height: 150px;
    margin-right: 30px;
}

```

![image-20220821213141985](image-20220821213141985.png)

> **备注：** CSS 浮动的知识会在我们关于 [浮动](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Floats)的教程当中被详细地解释。除此之外，如果您想要了解在 Flexbox 和 Grid 布局出现之前我们是如何进行列布局的（仍然有可能碰到这种情形），请阅读我们关于[传统布局方式](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Legacy_Layout_Methods)的文章。

### 定位技术

定位 (positioning) 能够让我们把一个元素从它原本在正常布局流 (normal flow) 中应该在的位置移动到另一个位置。定位 (positioning) 并不是一种用来给你做主要页面布局的方式，它更像是让你去管理和微调页面中的一个特殊项的位置。

有一些非常有用的技术在特定的布局下依赖于[`position`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/position)属性。同时，理解定位 (positioning) 也能够帮助你理解正常布局流 (normal flow)，理解把一个元素移出正常布局流 (normal flow) 是怎么一回事。

有五种主要的定位类型需要我们了解：

- **静态定位 (Static positioning)**是每个元素默认的属性——它表示“将元素放在文档布局流的默认位置——没有什么特殊的地方”。
- **相对定位 (Relative positioning)**允许我们相对于元素在正常的文档流中的位置移动它——包括将两个元素叠放在页面上。这对于微调和精准设计 (design pinpointing) 非常有用。
- **绝对定位 (Absolute positioning)**将元素完全从页面的正常布局流 (normal layout flow) 中移出，类似将它单独放在一个图层中。我们可以将元素相对于页面的 `<html>` 元素边缘固定，或者相对于该元素的*最近被定位祖先元素 (nearest positioned ancestor element)*。绝对定位在创建复杂布局效果时非常有用，例如通过标签显示和隐藏的内容面板或者通过按钮控制滑动到屏幕中的信息面板。
- **固定定位 (Fixed positioning)**与绝对定位非常类似，但是它是将一个元素相对浏览器视口固定，而不是相对另外一个元素。这在创建类似在整个页面滚动过程中总是处于屏幕的某个位置的导航菜单时非常有用。
- **粘性定位 (Sticky positioning)**是一种新的定位方式，它会让元素先保持和`position: static`一样的定位，当它的相对视口位置 (offset from the viewport) 达到某一个预设值时，他就会像`position: fixed`一样定位。

#### 简单定位示例

我们将展示一些示例代码来熟悉这些布局技术。这些示例代码都作用在下面这一个相同的 HTML 上：

```html
<h1>Positioning</h1>

<p>I am a basic block level element.</p>
<p class="positioned">I am a basic block level element.</p>
<p>I am a basic block level element.</p>

```

该 HTML 将使用以下 CSS 默认样式：

```css
body {
  width: 500px;
  margin: 0 auto;
}

p {
    background-color: rgb(207,232,220);
    border: 2px solid rgb(79,185,227);
    padding: 10px;
    margin: 10px;
    border-radius: 5px;
}

```

![image-20220822055123949](image-20220822055123949.png)

#### 相对定位

相对定位 (relative positioning) 让你能够把一个正常布局流 (normal flow) 中的元素从它的默认位置按坐标进行相对移动。比如将一个图标往下调一点，以便放置文字。我们可以通过下面的规则添加相对定位来实现效果:

```css
.positioned {
  position: relative;
  top: 30px;
  left: 30px;
}

```

这里我们给中间段落的[`position`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/position) 一个 `relative`值——这属性本身不做任何事情，所以我们还添加了[`top`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/top)和[`left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/left)属性。这些可以将受影响的元素向下向右移——这可能看起来和你所期待的相反，但你需要把它看成是左边和顶部的元素被“推开”一定距离，这就导致了它的向下向右移动。

添加此代码将给出以下结果：

```css
.positioned {
  position: relative;
  background: rgba(255,84,104,.3);
  border: 2px solid rgb(255,84,104);
  top: 30px;
  left: 30px;
}

```

![image-20220822055605043](image-20220822055605043.png)

#### 绝对定位

绝对定位用于将元素移出正常布局流 (normal flow)，以坐标的形式相对于它的容器定位到 web 页面的任何位置，以创建复杂的布局。有趣的是，它经常被用于与相对定位和浮动的协同工作。

回到我们最初的非定位示例，我们可以添加以下的 CSS 规则来实现绝对定位：

```css
.positioned {
  position: absolute;
  top: 30px;
  left: 30px;
}

```

这里我们给我们的中间段一个[`position`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/position)的 `absolute`值，并且和前面一样加上 [`top`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/top) 和[`left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/left) 属性。但是，添加此代码将给出以下结果：

```css
.positioned {
    position: absolute;
    background: rgba(255,84,104,.3);
    border: 2px solid rgb(255,84,104);
    top: 30px;
    left: 30px;
}

```

![image-20220822055830832](image-20220822055830832.png)



这和之前截然不同！定位元素现在已经与页面布局的其余部分完全分离，并位于页面的顶部。其他两段现在靠在一起，好像之前那个中间段落不存在一样。[`top`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/top)和[`left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/left)属性对绝对位置元素的影响不同于相对位置元素。在这一案例当中，他们没有指定元素相对于原始位置的移动程度。相反，在这一案例当中，它们指定元素应该从页面边界的顶部和左边的距离 (确切地说，是 `<html>`元素的距离)。我们也可以修改作为容器的那个元素（在这里是`<html>`元素），要了解这方面的知识，参见关于[定位 (positioning)](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Positioning)的课程

我们现在暂时不讨论固定定位（fixed positioning）——它基本上以相同的方式工作，除了它仍然固定在浏览器窗口的边缘，而不是它定位的父节点的边缘。

#### 固定定位

固定定位 (fixed positioning) 同绝对定位 (absolute positioning) 一样，将元素从文档流 (document flow) 当中移出了。但是，定位的坐标不会应用于"容器"边框来计算元素的位置，而是会应用于视口 (viewport) 边框。利用这一特性，我们可以轻松搞出一个固定位置的菜单，而不受底下的页面滚动的影响。

在这个例子里面，我们在 HTML 加了三段很长的文本来使得页面可滚动，又加了一个带有`position: fixed`的盒子。

```html
<h1>Fixed positioning</h1>

<div class="positioned">Fixed</div>

<p>Paragraph 1.</p>
<p>Paragraph 2.</p>
<p>Paragraph 3.</p>

```

```css
.positioned {
    position: fixed;
    top: 30px;
    left: 30px;
}

```

![image-20220822061501527](image-20220822061501527.png)

#### 粘性定位

粘性定位 (sticky positioning) 是最后一种我们能够使用的定位方式。它将默认的静态定位 (static positioning) 和固定定位 (fixed positioning) 相混合。当一个元素被指定了`position: sticky`时，它会在正常布局流中滚动，直到它出现在了我们给它设定的相对于容器的位置，这时候它就会停止随滚动移动，就像它被应用了`position: fixed`一样。

```css
.positioned {
  position: sticky;
  top: 30px;
  left: 30px;
}
```

![image-20220822061609334](image-20220822061609334.png)

> **备注：** 想要发现更多关于定位的信息，请参阅我们的[Positioning](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Positioning)和[Practical positioning examples](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Practical_positioning_examples)文章。

### 表格布局

HTML 表格对于显示表格数据是很好的，但是很多年前——在浏览器中支持基本的 CSS 之前——web 开发人员过去也常常使用表格来完成整个网页布局——将它们的页眉、页脚、不同的列等等放在不同的表行和列中。这在当时是有效的，但它有很多问题——表布局是不灵活的，繁重的标记，难以调试和语义上的错误（比如，屏幕阅读器用户在导航表布局方面有问题）。

一个`<table>`标签之所以能够像表格那样展示，是由于 css 默认给`<table>`标签设置了一组 table 布局属性。当这些属性被应用于排列非`<table>`元素时，这种用法被称为“使用 CSS 表格”。

下面这个例子展示了一个这样的用法。使用 CSS 表格来进行布局，在现在这个时间点应该被认为是一种传统方法，它通常会被用于兼容一些不支持 Flexbox 和 Grid 的浏览器。

让我们来看一个例子。首先，创建 HTML 表单的一些简单标记。每个输入元素都有一个标签，我们还在一个段落中包含了一个标题。为了进行布局，每个标签/输入对都封装在[`<div>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/div)中。

```html
<form>
  <p>First of all, tell us your name and age.</p>
  <div>
    <label for="fname">First name:</label>
    <input type="text" id="fname">
  </div>
  <div>
    <label for="lname">Last name:</label>
    <input type="text" id="lname">
  </div>
  <div>
    <label for="age">Age:</label>
    <input type="text" id="age">
  </div>
</form>

```

现在，我们例子中的 CSS。除了使用 display 属性外，大多数 CSS 都是相当普通的。 `<form>`, `<div>`,` <label>`和`<input>`被告知要分别显示表、表行和表单元——基本上，它们会像 HTML 表格标记一样，导致标签和输入在默认情况下排列整齐。我们所要做的就是添加一些大小、边缘等等，让一切看起来都好一点，我们就完成了。

你会注意到标题段落已经给出了 `display: table-caption;`——这使得它看起来就像一个表格`<caption>` ——同时出于设计需要，我们通过`caption-side: bottom;` 告诉标题应该展示在表格的底部，即使这个`<p>`标记在源码中是在`<input>`之前。这就能让你有一点灵活的弹性。

```css
html {
  font-family: sans-serif;
}

form {
  display: table;
  margin: 0 auto;
}

form div {
  display: table-row;
}

form label, form input {
  display: table-cell;
  margin-bottom: 10px;
}

form label {
  width: 200px;
  padding-right: 5%;
  text-align: right;
}

form input {
  width: 300px;
}

form p {
  display: table-caption;
  caption-side: bottom;
  width: 300px;
  color: #999;
  font-style: italic;
}

```

![image-20220822062021184](image-20220822062021184.png)

### 多列布局

多列布局模组给了我们 一种把内容按列排序的方式，就像文本在报纸上排列那样。由于在 web 内容里让你的用户在一个列上通过上下滚动来阅读两篇相关的文本是一种非常低效的方式，那么把内容排列成多列可能是一种有用的技术。

要把一个块转变成多列容器 (multicol container)，我们可以使用 [`column-count`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/column-count)属性来告诉浏览器我们需要多少列，也可以使用[`column-width` ](https://developer.mozilla.org/en-US/docs/Web/CSS/column-width)来告诉浏览器以至少某个宽度的尽可能多的列来填充容器。

在下面这个例子中，我们从一个 class 为`container`的`<div>`容器元素里边的一块 HTML 开始。

```html
    <div class="container">
        <h1>Multi-column layout</h1>
    
        <p class="one">Paragraph 1. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Porro odio officia voluptatem magnam harum nulla. Quae maxime et molestiae laboriosam. Nesciunt commodi quod voluptate nulla fuga numquam itaque? Quis illum, voluptates dolorem fuga et, reprehenderit ullam, aperiam neque in illo quasi excepturi natus id! Dolorum quibusdam mollitia facere veniam voluptatum. Eveniet facilis debitis ea blanditiis rem accusantium quod modi dolorum? Esse voluptatem at quaerat quasi laudantium a, recusandae aliquid ratione aliquam reprehenderit nemo numquam officia labore necessitatibus, alias in officiis odio rem est delectus, dicta facere. Illum inventore odit similique totam veniam, provident quibusdam delectus numquam qui aspernatur odio eius.</p>
        <p class="two">Paragraph 2. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolor expedita inventore sint perspiciatis accusamus eveniet deleniti rerum exercitationem aut tenetur obcaecati, quam odit neque iure ratione beatae amet consequuntur eos dignissimos. Similique, officiis repellat deleniti aspernatur molestiae corporis expedita et eveniet iusto temporibus id fuga incidunt dicta autem molestias ratione velit inventore natus? Labore exercitationem rem sit dolorum veritatis minus quis mollitia laudantium perspiciatis expedita deserunt sapiente fugiat, consequatur amet itaque. Velit corrupti totam ab, repudiandae minus unde excepturi suscipit quisquam porro tenetur ullam officiis temporibus atque laboriosam impedit maiores debitis, quaerat ex accusantium adipisci vitae nihil dicta incidunt ipsa.</p>
    
    </div>
    
```

我们指定了该容器的`column-width`为 200 像素，这让浏览器创建了尽可能多的 200 像素的列来填充这一容器。接着他们共同使用剩余的空间来伸展自己的宽度。

```css
.container {
    column-width: 200px;
}

.one {
    color: rgb(4, 172, 116);
}

.two {
    color: rgb(172, 97, 0);
}
```

![image-20220822062626766](image-20220822062626766.png)

### 小结

本文提供了关于您应该了解的所有布局技术的简要概述。阅读更多关于每一项技术的信息！



## 正常布局流

这篇文章介绍正常的流布局，或者说，在你没有改变默认布局规则情况下的页面元素布局方式。

如上小节对布局的介绍，如果你未曾应用任何 CSS 规则来改变它们的展现方式，网页上的元素将会按照正常布局流来组织。同样的，开始探索前，你可以通过调整元素位置，或者完全的移除元素来改变它们的表现效果。从一副简单的、结构良好并且在正常布局流下仍然易读的文档开始，是上手任何页面的最佳方式（译者注：几乎没有很简单的 CSS，标签组织符合一般用法）。这样确保了你的内容的易读性，即便用户使用受限的浏览器或者屏幕阅读设备（译者注：比如有些老旧浏览器对某些 CSS 特性的支持不理想，或者有用户自定义 CSS 样式）。此外，由于正常布局流的设计初衷在于构建易读、合理的文档，遵循这样的指引原则，你在对布局做出改动时应该是与文档协同，而不是与之对抗。

在深入探索不同的布局方式之前，你最好回顾下在之前模块学习到的关于正常布局流的知识点（译者注：比如 position display float table flex-box grid-layout）.

### 默认情况下，元素是如何布局的？

首先，取得元素的内容来放在一个独立的元素盒子中，然后在其周边加上内边距、边框和外边距 --- 就是我们之前看到的盒子模型。

默认的，一个[块级元素](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Block-level_elements)的内容宽度是其父元素的 100%，其高度与其内容高度一致。[内联元素](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Inline_elements)的 height width 与内容一致。你无法设置内联元素的 height width --- 它们就那样置于块级元素的内容里。如果你想控制内联元素的尺寸，你需要为元素设置`display: block;` （或者，`display: inline-block;` inline-block 混合了 inline 和 block 的特性。)

这样解释了独立元素的布局，但是元素之间又是如何相互影响的呢？ 正常布局流（在布局介绍里提到过）是一套在浏览器视口内放置、组织元素的系统。默认的，块级元素按照基于其父元素的[书写顺序](https://developer.mozilla.org/zh-CN/docs/Web/CSS/writing-mode)(*默认值：* horizontal-tb) 的*块流动方向 (block flow direction)*放置 --- 每个块级元素会在上一个元素下面另起一行，它们会被设置好的 margin 分隔。在英语，或者其他水平书写、自上而下模式里，块级元素是垂直组织的。

内联元素的表现有所不同 --- 它们不会另起一行；只要在其父级块级元素的宽度内有足够的空间，它们与其他内联元素、相邻的文本内容（或者被包裹的）被安排在同一行。如果空间不够，溢出的文本或元素将移到新的一行。

我们来看一个对全部这些做出解释的简单例子：

```html
    <h1>Basic document flow</h1>

    <p>I am a basic block level element. My adjacent block level elements sit on new lines below me.</p>

    <p>By default we span 100% of the width of our parent element, and we are as tall as our child content. Our total
        width and height is our content + padding + border width/height.</p>

    <p>We are separated by our margins. Because of margin collapsing, we are separated by the width of one of our
        margins, not both.</p>

    <p>inline elements <span>like this one</span> and <span>this one</span> sit on the same line as one another, and
        adjacent text nodes, if there is space on the same line. Overflowing inline elements will <span>wrap onto a new
            line if possible (like this one containing text)</span>, or just go on to a new line if not, much like this
        image will do: <img src="https://mdn.github.io/css-examples/learn/backgrounds-borders/star.png"></p>

```

```css
body {
    width: 500px;
    margin: 0 auto;
}

p {
    background: rgba(255, 84, 104, 0.3);
    border: 2px solid rgb(255, 84, 104);
    padding: 10px;
    margin: 10px;
}

span {
    background: white;
    border: 1px solid black;
}
```

![image-20220822070952744](image-20220822070952744.png)

### 小结

现在你对正常布局流有所了解，知晓浏览器默认怎么组织元素，继续下一节，学习如何改变默认布局以产出符合你的设计的布局。

## 弹性盒子

弹性盒子是一种用于按行或按列布局元素的一维布局方法。元素可以膨胀以填充额外的空间，收缩以适应更小的空间。本文将解释所有的基本原理。

### 为什么是 弹性盒子？

长久以来，CSS 布局中唯一可靠且跨浏览器兼容的创建工具只有 [floats](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Floats) 和 [positioning](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Positioning)。这两个工具大部分情况下都很好使，但是在某些方面它们具有一定的局限性，让人难以完成任务。

以下简单的布局需求是难以或不可能用这样的工具（ [floats](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Floats) 和 [positioning](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Positioning)）方便且灵活的实现的：

- 在父内容里面垂直居中一个块内容。
- 使容器的所有子项占用等量的可用宽度/高度，而不管有多少宽度/高度可用。
- 使多列布局中的所有列采用相同的高度，即使它们包含的内容量不同。

正如你将在后面的章节中看到的一样，弹性盒子使得很多布局任务变得更加容易。让我们继续吧！

### 一个简单的例子

在本文中，我们将通过一系列练习来帮助你了解 弹性盒子的工作原理。开始前，您应该拷贝 mozilla github 仓库的 [弹性盒子 0.html](https://github.com/mdn/learning-area/blob/master/css/css-layout/flexbox/flexbox0.html) 到本地 。在现代浏览器里打开它（比如 Firefox、Chrome），然后打开你的编辑器看一眼它的代码。你可以看它的[线上](https://mdn.github.io/learning-area/css/css-layout/flexbox/flexbox0.html)实例。

你可以看到这个页面有一个含有顶级标题的 `<header>` 元素，和一个包含三个` <article>` 的 `<section>` 元素。我们将使用这些来创建一个非常的标准三列布局，如下所示：

```html
<!DOCTYPE html>
<html lang="en-us">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Flexbox 0 — starting code</title>
  <style>
      html {
          font-family: sans-serif;
      }

      body {
          margin: 0;
      }

      header {
          background: purple;
          height: 100px;
      }

      h1 {
          text-align: center;
          color: white;
          line-height: 100px;
          margin: 0;
      }

      article {
          padding: 10px;
          margin: 10px;
          background: aqua;
      }

      /* Add your flexbox CSS below here */


  </style>
</head>
<body>
<header>
  <h1>Sample flexbox example</h1>
</header>

<section>
  <article>
    <h2>First article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>
  </article>

  <article>
    <h2>Second article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>
  </article>

  <article>
    <h2>Third article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>

    <p>Cray food truck brunch, XOXO +1 keffiyeh pickled chambray waistcoat ennui. Organic small batch paleo 8-bit.
      Intelligentsia umami wayfarers pickled, asymmetrical kombucha letterpress kitsch leggings cold-pressed squid
      chartreuse put a bird on it. Listicle pickled man bun cornhole heirloom art party.</p>
  </article>
</section>
</body>
</html>
```

![image-20220822091433457](image-20220822091433457.png)

### 指定元素的布局为 flexible

首先，我们需要选择将哪些元素将设置为柔性的盒子。我们需要给这些 flexible 元素的父元素 display 设置一个特定值。在本例中，我们想要设置 `<article>` 元素，因此我们给 `<section>`（变成了 flex 容器）设置 display：

```css
section {
  display:flex
}

```

结果如下：

![image-20220822091839296](image-20220822091839296.png)

所以，就这样一个简单的声明就给了我们所需要的一切—非常不可思议，对吧？我们的多列布局具有大小相等的列，并且列的高度都是一样。这是因为这样的 flex 项（flex 容器的子项）的默认值是可以解决这些的常见问题的。后面还有更多内容。

> **备注：** 假如你想设置行内元素为 flexible box，也可以置 [`display`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/display) 属性的值为 `inline-flex。`



### flex 模型说明

当元素表现为 flex 框时，它们沿着两个轴来布局：

（当元素的内部显示类型为`flex`时，它的子元素们沿着两个轴来布局）

![flex_terms.png](flex_terms.png)



- **主轴**（main axis）是沿着 flex 元素放置的方向延伸的轴（比如页面上的横向的行、纵向的列）。该轴的开始和结束被称为 **main start** 和 **main end**。
- **交叉轴**（cross axis）是垂直于 flex 元素放置方向的轴。该轴的开始和结束被称为 **cross start** 和 **cross end**。
- 设置了 `display: flex` 的父元素（在本例中是 [`<section>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/section)）被称之为 **flex 容器（flex container）。**
- 在 flex 容器中表现为柔性的盒子的元素被称之为 **flex 项**（**flex item**）（本例中是 [`<article>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/article) 元素。

了解这些术语以便你阅读后续章节。如果您对使用的任何术语感到困惑，您可以随时返回这里。

### 列还是行？

弹性盒子提供了 [`flex-direction`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-direction) 这样一个属性，它可以指定主轴的方向（弹性盒子子类放置的地方）— 它默认值是 `row`，这使得它们在按你浏览器的默认语言方向排成一排（在英语/中文浏览器中是从左到右）。

尝试将以下声明添加到 section 元素的 css 规则里：

```css
flex-direction: column;

```

你会看到，这会将那些元素设置为列布局，就像我们添加这些 CSS 之前。在继续之前，请从示例中删除此规则。

**备注：** 你还可以使用 `row-reverse` 和 `column-reverse` 值反向排列 flex 项目。用这些值试试看吧！

`flex-direction`

- `row`

- `column`
- `row-reverse`
- `column-reverse`



### 换行

当你在布局中使用定宽或者定高的时候，可能会出现问题即处于容器中的 弹性盒子子元素会溢出，破坏了布局。你可以看一下 [弹性盒子-wrap0.html](https://github.com/mdn/learning-area/blob/master/css/css-layout/flexbox/flexbox-wrap0.html) 示例（你也可以拷贝到本地），如下所示：

```html
<!DOCTYPE html>
<html lang="en-us">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Flexbox wrap 0 — children overflowing</title>
  <style>
      html {
          font-family: sans-serif;
      }

      body {
          margin: 0;
      }

      header {
          background: purple;
          height: 100px;
      }

      h1 {
          text-align: center;
          color: white;
          line-height: 100px;
          margin: 0;
      }

      article {
          padding: 10px;
          margin: 10px;
          background: aqua;
      }

      /* Add your flexbox CSS below here */

      section {
          display: flex;
          flex-direction: row;
      }

      article {

      }


  </style>
</head>
<body>
<header>
  <h1>Sample flexbox example</h1>
</header>

<section>
  <article>
    <h2>First article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>
  </article>

  <article>
    <h2>Second article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>
  </article>

  <article>
    <h2>Third article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>

    <p>Cray food truck brunch, XOXO +1 keffiyeh pickled chambray waistcoat ennui. Organic small batch paleo 8-bit.
      Intelligentsia umami wayfarers pickled, asymmetrical kombucha letterpress kitsch leggings cold-pressed squid
      chartreuse put a bird on it. Listicle pickled man bun cornhole heirloom art party.</p>
  </article>

  <article>
    <h2>Fourth article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>
  </article>

  <article>
    <h2>Fifth article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>
  </article>

  <article>
    <h2>Sixth article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>

    <p>Cray food truck brunch, XOXO +1 keffiyeh pickled chambray waistcoat ennui. Organic small batch paleo 8-bit.
      Intelligentsia umami wayfarers pickled, asymmetrical kombucha letterpress kitsch leggings cold-pressed squid
      chartreuse put a bird on it. Listicle pickled man bun cornhole heirloom art party.</p>
  </article>

  <article>
    <h2>Seventh article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>
  </article>

  <article>
    <h2>Eighth article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>
  </article>

  <article>
    <h2>Ninth article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>

    <p>Cray food truck brunch, XOXO +1 keffiyeh pickled chambray waistcoat ennui. Organic small batch paleo 8-bit.
      Intelligentsia umami wayfarers pickled, asymmetrical kombucha letterpress kitsch leggings cold-pressed squid
      chartreuse put a bird on it. Listicle pickled man bun cornhole heirloom art party.</p>
  </article>

  <article>
    <h2>Tenth article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>
  </article>

  <article>
    <h2>Eleventh article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>
  </article>

  <article>
    <h2>Twelfth article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>

    <p>Cray food truck brunch, XOXO +1 keffiyeh pickled chambray waistcoat ennui. Organic small batch paleo 8-bit.
      Intelligentsia umami wayfarers pickled, asymmetrical kombucha letterpress kitsch leggings cold-pressed squid
      chartreuse put a bird on it. Listicle pickled man bun cornhole heirloom art party.</p>
  </article>
</section>
</body>
</html>
```

![image-20220822093943530](image-20220822093943530.png)

在这里我们看到，子代确实超出了它们的容器。解决此问题的一种方法是将以下声明添加到 section css 规则中：

```css
flex-wrap: wrap

```

同时，把以下规则也添加到`<article>` 规则中：

```css
flex: 200px;

```

现在尝试一下吧；你会看到布局比原来好多了：

![image-20220822094233759](image-20220822094233759.png)

现在我们有了多行 弹性盒子— 任何溢出的元素将被移到下一行。

在 article 元素上设置的 flex: 200px 规则，意味着每个元素的宽度至少是 200px（不一定是200px，但一定大于等于200px）；我们将在后面更详细地讨论这个属性。

你可能还注意到，最后一行上的最后几个项每个都变得更宽，以便把整个行填满。

![image-20220822094647722](/image-20220822094647722.png)

但是这里我们可以做得更多。首先，改变 [`flex-direction`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-direction) 属性值为 `row-reverse` — 你会看到仍然有多行布局，但是每一行元素排列的方向和原来是相反的了。

![image-20220822094801771](image-20220822094801771.png)

`flex-wrap`

- `nowrap`
- `wrap`
- `wrap-reverser`

### flex-flow 缩写

到这里，应当注意到存在着 [`flex-direction`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-direction) 和 [`flex-wrap`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-wrap) — 的缩写 [`flex-flow`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-flow)。比如，你可以将

```css
flex-direction: row;
flex-wrap: wrap;

```

替换为

```css
flex-flow: row wrap;

```

### flex 项的动态尺寸

现在让我们回到第一个例子，看看是如何控制 flex 项占用空间的比例的。打开你本地的 [弹性盒子 0.html](https://github.com/mdn/learning-area/blob/master/css/css-layout/flexbox/flexbox0.html)，或者拷贝 [弹性盒子 1.html](https://github.com/mdn/learning-area/blob/master/css/css-layout/flexbox/flexbox1.html) 作为新的开始（[查看线上](https://mdn.github.io/learning-area/css/css-layout/flexbox/flexbox1.html)）。

```html
<!DOCTYPE html>
<html lang="en-us">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Flexbox 1 — basic flexbox model chosen</title>
  <style>
      html {
          font-family: sans-serif;
      }

      body {
          margin: 0;
      }

      header {
          background: purple;
          height: 100px;
      }

      h1 {
          text-align: center;
          color: white;
          line-height: 100px;
          margin: 0;
      }

      article {
          padding: 10px;
          margin: 10px;
          background: aqua;
      }

      /* Add your flexbox CSS below here */

      section {
          display: flex;
      }


  </style>
</head>
<body>
<header>
  <h1>Sample flexbox example</h1>
</header>

<section>
  <article>
    <h2>First article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>
  </article>

  <article>
    <h2>Second article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>
  </article>

  <article>
    <h2>Third article</h2>

    <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl
      typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin
      coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub
      hammock.</p>

    <p>Cray food truck brunch, XOXO +1 keffiyeh pickled chambray waistcoat ennui. Organic small batch paleo 8-bit.
      Intelligentsia umami wayfarers pickled, asymmetrical kombucha letterpress kitsch leggings cold-pressed squid
      chartreuse put a bird on it. Listicle pickled man bun cornhole heirloom art party.</p>
  </article>
</section>
</body>
</html>
```



第一步，将以下规则添加到 CSS 的底部：

```css
article {
  flex: 1;
}

```

这是一个无单位的比例值，表示每个 flex 项沿主轴的可用空间大小。

本例中，我们设置 [`<article>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/article) 元素的 flex 值为 1，这表示每个元素占用空间都是相等的，占用的空间是在设置 padding 和 margin 之后剩余的空间。因为它是一个比例，这意味着将每个 flex 项的设置为 400000 的效果和 1 的时候是完全一样的。

现在在上一个规则下添加：



```css
article:nth-of-type(3) {
  flex: 2;
}

```

现在当你刷新，你会看到第三个 `<article>` 元素占用了两倍的可用宽度和剩下的一样 — 现在总共有四个比例单位可用。前两个 flex 项各有一个，因此它们占用每个可用空间的 1/4。第三个有两个单位，所以它占用 2/4 或这说是 1/2 的可用空间。

`First article`和`Second article`的`content`宽度为`307.25`

![image-20220822101800411](image-20220822101800411.png)

`Third article`的宽度为`307.25*2=614.5`

![image-20220822101857456](/image-20220822101857456.png)

您还可以指定 flex 的最小值。尝试修改现有的 article 规则：

```css
article {
  flex: 1 200px;
}

article:nth-of-type(3) {
  flex: 2 200px;
}

```

这表示“每个 flex 项将首先给出 200px 的可用空间，然后，剩余的可用空间将根据分配的比例共享“。尝试刷新，你会看到分配空间的差别。

整个`section`宽度为1366（查看时不要出现竖直滚动条），减去所有的内边距和边框`40*3=120`，剩余`1366-120=1246`

每个`flex`项先给出`200px`的空间，剩余`1246-200*3=646`

剩余空间将根据分配的比例共享

- `First article`和`Second article`各占一份，`content`宽度为`646*1/4+200=361.5`
- `Third article`的`content`宽度为`646*2/4+200=523`

![image-20220822103441520](image-20220822103441520.png)



弹性盒子的真正价值可以体现在它的灵活性/响应性，如果你调整浏览器窗口的大小，或者增加一个 `<article>` 元素，这时的布局仍旧是好的。

### flex: 缩写与全写

[`flex`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex) 是一个可以指定最多三个不同值的缩写属性：

- 第一个就是上面所讨论过的无单位比例。可以单独指定全写 [`flex-grow`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-grow) 属性的值。
  - 表示可拉伸

- 第二个无单位比例 — [`flex-shrink`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-shrink) — 一般用于溢出容器的 flex 项。这指定了从每个 flex 项中取出多少溢出量，以阻止它们溢出它们的容器。这是一个相当高级的弹性盒子功能，我们不会在本文中进一步说明。
  - 表示可压缩

- 第三个是上面讨论的最小值。可以单独指定全写 [`flex-basis`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-basis) 属性的值。
  - 表示当前元素的宽度


我们建议不要使用全写属性，除非你真的需要（比如要去覆盖之前写的）。使用全写会多写很多的代码，它们也可能有点让人困惑。

`flex`默认值：

- 不允许被拉伸，但可以被压缩，以剩余空间为基准

```css
flex-grow: 0;
flex-shrink: 1;
flex-basis: auto;
```

`flex: 1;`，同时会导致父元素宽度自动为100%

- 不以自身大小为基准，以剩余空间为基准

```css
flex-grow: 1;
flex-shrink: 1;
flex-basis: 0%;
```

`flex: auto;`

```css
flex-grow: 1;
flex-shrink: 1;
flex-basis: auto;
```

### 水平和垂直对齐

还可以使用 弹性盒子的功能让 flex 项沿主轴或交叉轴对齐。让我们一起看一下新例子 — [flex-align0.html](https://github.com/mdn/learning-area/blob/master/css/css-layout/flexbox/flex-align0.html)（[在线浏览](https://mdn.github.io/learning-area/css/css-layout/flexbox/flex-align0.html)）— 我们将会有一个整洁，灵活的按钮/工具栏。此时，你看到了一个水平菜单栏，其中一些按钮卡在左上角，就像下面这样：

```html

<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Flexbox align 0 — starting code</title>
    <style>
      html {
        font-family: sans-serif;
      }

      body {
        width: 70%;
        max-width: 960px;
        margin: 20px auto;
      }

      button {
        font-size: 18px;
        line-height: 1.5;
        width: 15%;
      }

      div {
        height: 100px;
        border: 1px solid black;
      }

      /* Add your flexbox CSS below here */

      
    </style>
  </head>
  <body>
    <div>
      <button>Smile</button>
      <button>Laugh</button>
      <button>Wink</button>
      <button>Shrug</button>
      <button>Blush</button>
    </div>
  </body>
</html>
```

![image-20220822105007948](image-20220822105007948.png)



首先，拷贝一份到本地。

然后，将下面的 CSS 添加到例子的底部：

```css
div {
  display: flex;
  align-items: center;
  justify-content: space-around;
}

```

刷新一下页面，你就会看到这些按钮很好的垂直水平居中了。我们是通过下面所说的两个新的属性做到的。

[`align-items`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/align-items) 控制 flex 项在交叉轴上的位置。

- 默认的值是 `stretch`，其会使所有 flex 项沿着交叉轴的方向拉伸以填充父容器。如果父容器在交叉轴方向上没有固定宽度（即高度），则所有 flex 项将变得与最长的 flex 项一样长（即高度保持一致）。我们的第一个例子在默认情况下得到相等的高度的列的原因。

  ![image-20220822105534500](image-20220822105534500.png)

- 在上面规则中我们使用的 `center` 值会使这些项保持其原有的高度，但是会在交叉轴居中。这就是那些按钮垂直居中的原因。

  ![image-20220822105600500](image-20220822105600500.png)

- 你也可以设置诸如 `flex-start` 或 `flex-end` 这样使 flex 项在交叉轴的开始或结束处对齐所有的值。查看 [`align-items`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/align-items) 了解更多。

  ![image-20220822105626009](image-20220822105626009.png)

你可以用 [`align-self`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/align-self) 属性覆盖 [`align-items`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/align-items) 的行为。比如，你可以这样：

```css
button:first-child {
  align-self: flex-end;
}

```

去看看它产生的效果，然后删除它。

![image-20220822105726155](image-20220822105726155.png)

[`justify-content`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/justify-content) 控制 flex 项在主轴上的位置。

- 默认值是 `flex-start`，这会使所有 flex 项都位于主轴的开始处。

  ![image-20220822105906113](image-20220822105906113.png)

- 你也可以用 `flex-end` 来让 flex 项到结尾处。

  ![image-20220822105954642](image-20220822105954642.png)

- `center` 在 `justify-content` 里也是可用的，可以让 flex 项在主轴居中。

  ![image-20220822110011487](image-20220822110011487.png)

- 而我们上面用到的值 `space-around` 是很有用的——它会使所有 flex 项沿着主轴均匀地分布，在任意一端都会留有一点空间。

  ![image-20220822110040716](image-20220822110040716.png)

- 还有一个值是 `space-between`，它和 `space-around` 非常相似，只是它不会在两端留下任何空间。

  ![image-20220822110104085](image-20220822110104085.png)

- 还有一个值是`space-evenly`，它会使所有的`flex`项周围的空白空间都保持一致（首尾元素比`space-around`多了一点空白）

  ![image-20220822110143310](image-20220822110143310.png)

  在继续下面之前，多多使用提到过的属性吧，看看它们的效果。

### flex 项排序

弹性盒子也有可以改变 flex 项的布局位置的功能，而不会影响到源顺序（即 dom 树里元素的顺序）。这也是传统布局方式很难做到的一点。

代码也很简单，将下面的 CSS 添加到示例代码下面。

```css
button:first-child {
  order: 1;
}

```

![image-20220822110537144](image-20220822110537144.png)

刷新下，然后你会看到 "Smile" 按钮移动到了主轴的末尾。下面我们谈下它实现的一些细节：

- 所有 flex 项默认的 [`order`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/order) 值是 0。
- order 值大的 flex 项比 order 值小的在显示顺序中更靠后。
- 相同 order 值的 flex 项按源顺序显示。所以假如你有四个元素，其 order 值分别是 2，1，1 和 0，那么它们的显示顺序就分别是第四，第二，第三，和第一。
- 第三个元素显示在第二个后面是因为它们的 order 值一样，且第三个元素在源顺序中排在第二个后面。

你也可以给 order 设置负值使它们比值为 0 的元素排得更前面。比如，你可以设置 "Blush" 按钮排在主轴的最前面：

```css
button:last-child {
  order: -1;
}
```

### flex 嵌套

弹性盒子也能创建一些颇为复杂的布局。设置一个元素为 flex 项目，那么他同样成为一个 flex 容器，它的孩子 (直接子节点) 也表现为 flexible box。看一下 [complex-弹性盒子.html](https://github.com/mdn/learning-area/blob/master/css/css-layout/flexbox/complex-flexbox.html)（[在线浏览](https://mdn.github.io/learning-area/css/css-layout/flexbox/complex-flexbox.html)）。



![image-20220822110831323](image-20220822110831323.png)



### 跨浏览器兼容性

大多数浏览器都支持 弹性盒子，诸如 Firefox, Chrome, Opera, Microsoft Edge 和 IE 11，较新版本的 Android/iOS 等等。但是你应该要意识到仍旧有被人使用的老浏览器不支持 弹性盒子（或者支持，但是只是支持非常非常老版本的 弹性盒子）。

虽然你只是在学习和实验，这不太要紧; 然而，如果您正在考虑在真实网站中使用弹性盒子，则需要进行测试，并确保在尽可能多的浏览器中您的用户体验仍然可以接受。

弹性盒子相较其他一些 CSS 特性可能更为棘手。例如，如果浏览器缺少 CSS 阴影，则该网站可能仍然可用。但是假如不支持 弹性盒子功能就会完全打破布局，使其不可用。

我们将在未来的模块中讨论克服棘手的跨浏览器支持问题的策略。

### 小结

到这里，介绍弹性盒子的基础知识就结束了。我们希望你体会到乐趣，并且玩的开心，能随着你的学习与你一起向前。接下来，我们将看到 CSS 布局的另一个重要方面—网格系统。

## 网格

CSS 网格是一个用于 web 的二维布局系统。利用网格，你可以把内容按照行与列的格式进行排版。另外，网格还能非常轻松地实现一些复杂的布局。关于使用网格进行页面排版，这篇文章包含了你需要的一切知识。

> **备注：** 本篇中旧版教程主要讲如何自己编写网格布局，最后过渡到浏览器支持的 CSS Grid Layout。而当前（2019-04-29）大多数浏览器已经支持了 CSS Grid Layout，没必要自己编写了，新版教程仅介绍 CSS Grid Layout 的用法

### 什么是网格布局？

网格是由一系列水平及垂直的线构成的一种布局模式。根据网格，我们能够将设计元素进行排列，帮助我们设计一系列具有固定位置以及宽度的元素的页面，使我们的网站页面更加统一。

一个网格通常具有许多的**列（column）**与**行（row）**，以及行与行、列与列之间的间隙，这个间隙一般被称为**沟槽（gutter）**。

![img](/grid.png)

> **备注：** 任何有设计背景的人似乎都感到惊讶，CSS 没有内置的网格系统，而我们似乎使用各种次优方法来创建网格状的设计。正如你将在本文的最后一部分中发现的那样，这将被改变，但是你可能需要知道在未来一段时间内创建网格的现有方法。

### 在 CSS 中创建自己的网格

决定好你的设计所需要的网格后，你可以创建一个 CSS 网格版面并放入各类元素。我们先来看看网格的基础功能，然后尝试做一个简单的网格系统。

#### 定义一个网格

一如既往，你可以下载教程[文件](https://github.com/mdn/learning-area/blob/master/css/css-layout/grids/0-starting-point.html)（你可以在线看到[效果](https://mdn.github.io/learning-area/css/css-layout/grids/0-starting-point.html)）。例子中有一个容器，容器中有一些子项。默认情况下，子项按照正常布局流自顶而下排布。在这篇文章中，我们会从这开始，对这些文件做一些改变，来了解网格是如何工作的。

```html

<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>CSS Grid starting point</title>
    <style>
        body {
            width: 90%;
            max-width: 900px;
            margin: 2em auto;
            font: .9em/1.2 Arial, Helvetica, sans-serif;
        }

        .container > div {
            border-radius: 5px;
            padding: 10px;
            background-color: rgb(207,232,220);
            border: 2px solid rgb(79,185,227);
        }
    </style>
  </head>

<body>
    <h1>Simple grid example</h1>

    <div class="container">
        <div>One</div>
        <div>Two</div>
        <div>Three</div>
        <div>Four</div>
        <div>Five</div>
        <div>Six</div>
        <div>Seven</div>
    </div>

</body>

</html>
```



首先，将容器的[`display`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/display)属性设置为`grid`来定义一个网络。与弹性盒子一样，将父容器改为网格布局后，他的直接子项会变为网格项。把下面的 css 规则加到你的文件中。

```css
.container {
    display: grid;
}

```

与弹性盒子不同的是，在定义网格后，网页并不会马上发生变化。因为`display: grid`的声明只创建了一个只有一列的网格，所以你的子项还是会像正常布局流那样从上而下一个接一个的排布。

![image-20220822112155791](image-20220822112155791.png)

为了让我们的容器看起来更像一个网格，我们要给刚定义的网格加一些列。那就让我们加三个宽度为`200px`的列。当然，这里可以用任何长度单位，包括百分比。

```css
.container {
    display: grid;
    grid-template-columns: 200px 200px 200px;
}

```

在规则里加入你的第二个声明。刷新页面后，你会看到子项们排进了新定义的网格中。

![image-20220822112501064](image-20220822112501064.png)

#### 使用 fr 单位的灵活网格

除了长度和百分比，我们也可以用`fr`这个单位来灵活地定义网格的行与列的大小。这个单位表示了可用空间的一个比例，可能有点抽像，看看下面的例子吧。

使用下面的规则来创建 3 个`1fr`的列：

```css
.container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
}

```

![image-20220822112434674](image-20220822112434674.png)

将窗口调窄（由于示例中设定了[`max-width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/max-width)，可能需要很窄），你应该能看到每一列的宽度可以会随着可用空间变小而变小。

![image-20220822112645117](image-20220822112645117.png)

`fr` 单位按比例划分了可用空间，如果没有理解，可以试着改一下数值，看看会发生什么，比如下面的代码：

```css
.container {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
}

```

![image-20220822112758002](image-20220822112758002.png)

这个定义里，第一列被分配了`2fr`可用空间，余下的两列各被分配了`1fr`的可用空间，这会使得第一列的宽度是第二第三列的两倍。另外，`fr`可以与一般的长度单位混合使用，比如`grid-template-columns: 300px 2fr 1fr`，那么第一列宽度是`300px`，剩下的两列会根据除去`300px`后的可用空间按比例分配。

> **备注：** `fr`单位分配的是*可用*空间而非*所有*空间，所以如果某一格包含的内容变多了，那么整个可用空间就会减少，可用空间是不包括那些已经确定被占用的空间的。

#### 网格间隙

使用 [`grid-column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/column-gap) 属性来定义列间隙；使用 [`grid-row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/row-gap) 来定义行间隙；使用 [`grid-gap` ](https://developer.mozilla.org/en-US/docs/Web/CSS/gap) 可以同时设定两者。

```css
.container {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    grid-gap: 20px;
}

```

![image-20220822113757639](image-20220822113757639.png)

间隙距离可以用任何长度单位包括百分比来表示，但不能使用`fr`单位。

> **备注：** `*gap`属性曾经有一个`grid-`前缀，不过后来的标准进行了修改，目的是让他们能够在不同的布局方法中都能起作用。尽管现在这个前缀不会影响语义，但为了代码的健壮性，你可以把两个属性都写上。

```css
.container {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  grid-gap: 20px;
  gap: 20px;
}

```

#### 重复构建行/列

你可以使用`repeat`来重复构建具有某些宽度配置的某些列。举个例子，如果要创建多个等宽轨道，可以用下面的方法。

```css
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

```

![image-20220822114000273](image-20220822114000273.png)

和之前一样，你仍然得到了 3 个`1fr`的列。第一个传入 repeat 函数的值（`3`）表明了后续列宽的配置要重复多少次，而第二个值（`1fr`）表示需要重复的构建配置，这个配置可以具有多个长度设定。例如`repeat(2, 2fr 1fr)`，如果你仍然不明白，可以实际测试一下效果，这相当于填入了`2fr 1fr 2fr 1fr`。

```css
.container {
    display: grid;
    grid-template-columns: repeat(2, 2fr 1fr);
    grid-gap: 20px;
}

```

![image-20220822114131384](image-20220822114131384.png)

#### 显式网格与隐式网格

到目前为止，我们定义过了列，但还没有管过行。但在这之前，我们要来理解一下显式网格和隐式网格。显式网格是我们用`grid-template-columns` 或 `grid-template-rows` 属性创建的。而隐式网格则是当有内容被放到网格外时才会生成的。显式网格与隐式网格的关系与弹性盒子的 main 和 cross 轴的关系有些类似。

隐式网格中生成的行/列大小是参数默认是`auto`，大小会根据放入的内容自动调整。当然，你也可以使用[`grid-auto-rows`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/grid-auto-rows)和[`grid-auto-columns`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/grid-auto-columns)属性手动设定隐式网格的大小。下面的例子将`grid-auto-rows`设为了`100px`，然后你可以看到那些隐式网格中的行（因为这个例子里没有设定[`grid-template-rows`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/grid-template-rows)，因此，所有行都位于隐式网格内）现在都是 100 像素高了。

译者注：简单来说，隐式网格就是为了放显式网格放不下的元素，浏览器根据已经定义的显式网格自动生成的网格部分。



```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 100px;
  grid-gap: 20px;
}

```

![image-20220822142414528](image-20220822142414528.png)

#### 方便的 minmax() 函数

100 像素高的行/列有时可能会不够用，因为时常会有比 100 像素高的内容加进去。所以，我们希望可以将其设定为至少 100 像素，而且可以跟随内容来自动拓展尺寸保证能容纳所有内容。显而易见，你很难知道网页上某个元素的尺寸在不同情况下会变成多少，一些额外的内容或者更大的字号就会导致许多能做到像素级精准的设计出现问题。所以，我们有了[`minmax`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/minmax)函数。

[`minmax`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/minmax) 函数为一个行/列的尺寸设置了取值范围。比如设定为 `minmax(100px, auto)`，那么尺寸就至少为 100 像素，并且如果内容尺寸大于 100 像素则会根据内容自动调整。在这里试一下把 `grid-auto-rows` 属性设置为`minmax`函数。

```css
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-auto-rows: minmax(100px, auto);
    grid-gap: 20px;
}

```

如果所有网格内的内容均小于 100 像素，那么看起来不会有变化，但如果在某一项中放入很长的内容或者图片，你可以看到这个格子所在的哪一行的高度变成能刚好容纳内容的高度了。注意我们修改的是`grid-auto-rows` ，因此只会作用于隐式网格。当然，这一项属性也可以应用于显示网格，更多内容可以参考[`minmax`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/minmax)页面。

#### 自动使用多列填充

现在来试试把学到的关于网格的一切，包括 repeat 与 minmax 函数，组合起来，来实现一个非常有用的功能。某些情况下，我们需要让网格自动创建很多列来填满整个容器。通过设置`grid-template-columns`属性，我们可以实现这个效果，不过这一次我们会用到[`repeat`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/repeat)函数中的一个关键字`auto-fill`来替代确定的重复次数。而函数的第二个参数，我们使用[`minmax`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/minmax)函数来设定一个行/列的最小值，以及最大值`1fr`。

```css
.container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-auto-rows: minmax(100px, auto);
  grid-gap: 20px;
}

```

![image-20220822143239545](image-20220822143239545.png)

你应该能看到形成了一个包含了许多至少 200 像素宽的列的网格，将容器填满。随着容器宽度的改变，网格会自动根据容器宽度进行调整，每一列的宽度总是大于 200 像素，并且容器总会被列填满。

### 基于线的元素放置

在定义完了网格之后，我们要把元素放入网格中。我们的网格有许多分隔线，第一条线的起始点与文档书写模式相关。在英文中，第一条列分隔线（即网格边缘线）在网格的最左边而第一条行分隔线在网格的最上面。而对于阿拉伯语，第一条列分隔线在网格的最右边，因为阿拉伯文是从右往左书写的。

我们根据这些分隔线来放置元素，通过以下属性来指定从那条线开始到哪条线结束。

- [`grid-column-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column-start)
- [`grid-column-end` ](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column-end)
- [`grid-row-start` ](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-row-start)
- [`grid-row-end` ](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-row-end)

这些属性的值均为分隔线序号，你也可以用以下缩写形式来同时指定开始与结束的线。

- [`grid-column`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/grid-column)
- [`grid-row`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/grid-row)

注意开始与结束的线的序号要使用`/`符号分开。

下载[这个文件](https://github.com/mdn/learning-area/blob/master/css/css-layout/grids/8-placement-starting-point.html)（或者查看[在线预览](https://mdn.github.io/learning-area/css/css-layout/grids/8-placement-starting-point.html)）。文件中已经定义了一个网格以及一篇简单的文章位于网格之外。你可以看到元素已经被自动放置到了我们创建的网格中。

```html
<!DOCTYPE html>
<html lang="en-us">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>CSS Grid - line-based placement starting point</title>
  <style>
      body {
          width: 90%;
          max-width: 900px;
          margin: 2em auto;
          font: .9em/1.2 Arial, Helvetica, sans-serif;
      }

      .container {
          display: grid;
          grid-template-columns: 1fr 3fr;
          grid-gap: 20px;
      }

      header,
      footer {
          border-radius: 5px;
          padding: 10px;
          background-color: rgb(207, 232, 220);
          border: 2px solid rgb(79, 185, 227);
      }

      aside {
          border-right: 1px solid #999;
      }
  </style>
</head>

<body>

<div class="container">
  <header>This is my lovely blog</header>
  <article>
    <h1>My article</h1>
    <p>Duis felis orci, pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at ultricies tellus
      laoreet sit amet. Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet orci vel, viverra
      egestas ligula. Curabitur vehicula tellus neque, ac ornare ex malesuada et. In vitae convallis lacus. Aliquam erat
      volutpat. Suspendisse ac imperdiet turpis. Aenean finibus sollicitudin eros pharetra congue. Duis ornare egestas
      augue ut luctus. Proin blandit quam nec lacus varius commodo et a urna. Ut id ornare felis, eget fermentum
      sapien.</p>

    <p>Nam vulputate diam nec tempor bibendum. Donec luctus augue eget malesuada ultrices. Phasellus turpis est, posuere
      sit amet dapibus ut, facilisis sed est. Nam id risus quis ante semper consectetur eget aliquam lorem. Vivamus
      tristique elit dolor, sed pretium metus suscipit vel. Mauris ultricies lectus sed lobortis finibus. Vivamus eu
      urna eget velit cursus viverra quis vestibulum sem. Aliquam tincidunt eget purus in interdum. Cum sociis natoque
      penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
  </article>
  <aside><h2>Other things</h2>
    <p>Nam vulputate diam nec tempor bibendum. Donec luctus augue eget malesuada ultrices. Phasellus turpis est, posuere
      sit amet dapibus ut, facilisis sed est.</p></aside>
  <footer>Contact me@mysite.com</footer>
</div>

</body>

</html>
```



接下来，尝试用定义网格线的方法将所有元素放置到网格中。将以下规则加入到你的 css 的末尾：

```css
header {
  grid-column: 1 / 3;
  grid-row: 1;
}

article {
  grid-column: 2;
  grid-row: 2;
}

aside {
  grid-column: 1;
  grid-row: 2;
}

footer {
  grid-column: 1 / 3;
  grid-row: 3;
}

```

![image-20220822144414667](image-20220822144414667.png)

> **备注：** 你也可以用`-1`来定位到最后一条列分隔线或是行分隔线，并且可以用负数来指定倒数的某一条分隔线。但是这只能用于显式网格，对于[隐式网格](https://developer.mozilla.org/zh-CN/docs/Glossary/Grid)`-1`不一定能定位到最后一条分隔线。



### 使用 grid-template-areas 属性放置元素

另一种往网格放元素的方式是用[`grid-template-areas`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/grid-template-areas)属性，并且你要命名一些元素并在属性中使用这些名字作为一个区域。

将之前基于线的元素放置代码删除（或者重新下载一份新的文件），然后加入以下 CSS 规则：

```css
.container {
  display: grid;
  grid-template-areas:
      "header header"
      "sidebar content"
      "footer footer";
  grid-template-columns: 1fr 3fr;
  grid-gap: 20px;
}

header {
  grid-area: header;
}

article {
  grid-area: content;
}

aside {
  grid-area: sidebar;
}

footer {
  grid-area: footer;
}

```

刷新页面，然后你应该能看到的元素会被放到与之前相同的地方，整个过程不需要我们指定任何分隔线序号。

![image-20220822144858776](image-20220822144858776.png)

`grid-template-areas`属性的使用规则如下：

- 你需要填满网格的每个格子
- 对于某个横跨多个格子的元素，重复写上那个元素`grid-area`属性定义的区域名字
- 所有名字只能出现在一个连续的区域，不能在不同的位置出现
- 一个连续的区域必须是一个矩形
- 使用`.`符号，让一个格子留空

你可以在文件中尽情发挥你的想象来测试各种网格排版，比如把页脚放在内容之下，或者把侧边栏一直延伸到最底。这种直观的元素放置方式很棒，你在 CSS 中看到的就是实际会出现的排版效果。

### 一个用 CSS 网格实现的网格排版框架

网格排版框架一般由 12 到 16 列的网格构成，你可以用 CSS 网格系统直接实现而不需要任何第三方的工具，毕竟这是标准定义好了的。

下载这个[初始文件](https://github.com/mdn/learning-area/blob/master/css/css-layout/grids/11-grid-system-starting-point.html)，文件中包含了一个定义了 12 列网格的容器。文件中的一些内容我们曾在前两个示例中使用过，我们暂时可以先用基于线的元素放置模式来将我们的内容放到这个 12 列的网格中。

```html
<!DOCTYPE html>
<html lang="en-us">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>CSS Grid - line-based placement starting point</title>
  <style>
      body {
          width: 90%;
          max-width: 900px;
          margin: 2em auto;
          font: .9em/1.2 Arial, Helvetica, sans-serif;
      }

      .container {
          display: grid;
          grid-template-columns: repeat(12, minmax(0, 1fr));
          grid-gap: 20px;
      }

      header,
      footer {
          border-radius: 5px;
          padding: 10px;
          background-color: rgb(207, 232, 220);
          border: 2px solid rgb(79, 185, 227);
      }

      aside {
          border-right: 1px solid #999;
      }

  </style>
</head>

<body>

<div class="container">
  <header>This is my lovely blog</header>
  <article>
    <h1>My article</h1>
    <p>Duis felis orci, pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at ultricies tellus
      laoreet sit amet. Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet orci vel, viverra
      egestas ligula. Curabitur vehicula tellus neque, ac ornare ex malesuada et. In vitae convallis lacus. Aliquam erat
      volutpat. Suspendisse ac imperdiet turpis. Aenean finibus sollicitudin eros pharetra congue. Duis ornare egestas
      augue ut luctus. Proin blandit quam nec lacus varius commodo et a urna. Ut id ornare felis, eget fermentum
      sapien.</p>

    <p>Nam vulputate diam nec tempor bibendum. Donec luctus augue eget malesuada ultrices. Phasellus turpis est, posuere
      sit amet dapibus ut, facilisis sed est. Nam id risus quis ante semper consectetur eget aliquam lorem. Vivamus
      tristique elit dolor, sed pretium metus suscipit vel. Mauris ultricies lectus sed lobortis finibus. Vivamus eu
      urna eget velit cursus viverra quis vestibulum sem. Aliquam tincidunt eget purus in interdum. Cum sociis natoque
      penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
  </article>
  <aside><h2>Other things</h2>
    <p>Nam vulputate diam nec tempor bibendum. Donec luctus augue eget malesuada ultrices. Phasellus turpis est, posuere
      sit amet dapibus ut, facilisis sed est.</p></aside>
  <footer>Contact me@mysite.com</footer>
</div>

</body>

</html>
```

```css
header {
  grid-column: 1 / 13;
  grid-row: 1;
}

article {
  grid-column: 4 / 13;
  grid-row: 2;
}

aside {
  grid-column: 1 / 4;
  grid-row: 2;
}

footer {
  grid-column: 1 / 13;
  grid-row: 3;
}

```

你可以使用[Firefox Grid Inspector](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_grid_layouts/index.html)去查看页面中的网格线，你应该能看到这 12 列的网格是如何工作的。

![image-20220822145809803](/image-20220822145809803.png)

### 小结

我们在这篇文章中接触了 CSS 网格版面的主要特性，你现在应该可以在你自己的设计中使用了。想深入了解这些内容，你可以读一读下面关于网格版面的文章，可以下面的推荐阅读里看到。

- [CSS 网格指南](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Grid_Layout#guides)
- [CSS 网格检查器：检查的你的网格版面 (en-US)](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_grid_layouts/index.html)

## 浮动

[`float`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/float) 属性最初只用于在成块的文本内浮动图像，但是现在它已成为在网页上创建多列布局的最常用工具之一。本文将阐述它的有关知识。

### 浮动的背景知识

最初，引入 [`float`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/float) 属性是为了能让 Web 开发人员实现简单的布局，包括在一列文本中浮动的图像，文字环绕在它的左边或右边。你可能在报纸版面上看到过。

但 Web 开发人员很快意识到，任何东西都可以浮动，而不仅仅是图像，所以浮动的使用范围扩大了。之前的 [fancy paragraph example](https://css-tricks.com/snippets/css/drop-caps/) 的课程展示了如何使用浮动创建一个有趣的 drop-cap（首字下沉）效果。

浮动曾被用来实现整个网站页面的布局，它使信息列得以横向排列（默认的设定则是按照这些列在源代码中出现的顺序纵向排列）。目前出现了更新更好的页面布局技术，所以使用浮动来进行页面布局应被看作[传统的布局方法](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Legacy_Layout_Methods)。

在这一章中，我们仅就浮动这一命令本身的性能展开讲解。

### 简单的例子

让我们来探讨如何使用浮动。我们将从一个非常简单的例子开始，包括在图像周围浮动一个文本块。你可以在电脑上创建新的 `index.html` 文件，并以 [简单的 HTML 模板](https://github.com/mdn/learning-area/blob/master/html/introduction-to-html/getting-started/index.html) 填充，在适当的地方插入以下代码。稍后你可以看到示例代码应该能呈现出的效果。

首先，我们写一些简单的 HTML——添加以下内容到 HTML 的`<body>`内，删除之前`<body>`里面的东西：

```html
<h1>Simple float example</h1>

<div class="box">Float</div>

<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus aliquam dolor, eu lacinia lorem placerat vulputate. Duis felis orci, pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at ultricies tellus laoreet sit amet. </p>

<p>Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet orci vel, viverra egestas ligula. Curabitur vehicula tellus neque, ac ornare ex malesuada et. In vitae convallis lacus. Aliquam erat volutpat. Suspendisse ac imperdiet turpis. Aenean finibus sollicitudin eros pharetra congue. Duis ornare egestas augue ut luctus. Proin blandit quam nec lacus varius commodo et a urna. Ut id ornare felis, eget fermentum sapien.</p>

<p>Nam vulputate diam nec tempor bibendum. Donec luctus augue eget malesuada ultrices. Phasellus turpis est, posuere sit amet dapibus ut, facilisis sed est. Nam id risus quis ante semper consectetur eget aliquam lorem. Vivamus tristique elit dolor, sed pretium metus suscipit vel. Mauris ultricies lectus sed lobortis finibus. Vivamus eu urna eget velit cursus viverra quis vestibulum sem. Aliquam tincidunt eget purus in interdum. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>

```

现在将以下 CSS 应用到您的 HTML 中（使用`<style>`元素或 `<link>` 到单独的 .css 文件——由你选择）：

```css
body {
    width: 90%;
    max-width: 900px;
    margin: 0 auto;
    font: .9em/1.2 Arial, Helvetica, sans-serif;
}

.box {
    width: 150px;
    height: 100px;
    border-radius: 5px;
    background-color: rgb(207,232,220);
    padding: 1em;
}

```

如果你现在保存并刷新，你会看到和你预期的效果差不多——图片坐落在文本的上方，且保持正常布局流。

![image-20220822150347757](image-20220822150347757.png)

#### 使盒子浮动起来

为了使盒子浮动起来，向规则 `.box` 下添加 [`float`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/float) 和 [`margin-right`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin-right) 属性：

```css
.box {
    float: left;
    margin-right: 15px;
    width: 150px;
    height: 100px;
    border-radius: 5px;
    background-color: rgb(207,232,220);
    padding: 1em;
}

```

现在，如果您保存和刷新，你会看到类似下面的东西：

![image-20220822150902315](image-20220822150902315.png)

让我们考虑一下浮动是如何工作的——浮动元素 (这个例子中的 `<div>` 元素) 会脱离正常的文档布局流，并吸附到其父容器的左边（这个例子中的 `<body>` 元素）。在正常布局中位于该浮动元素之下的内容，此时会围绕着浮动元素，填满其右侧的空间。

向右浮动的内容是一样的效果，只是反过来了——浮动元素会吸附到右边，而其他内容将从左侧环绕它。尝试将上一个例子中的浮动值改为 `right` ，再把 `margin-right` 换成 `margin-left` ，看看结果是什么。

![image-20220822151022906](image-20220822151022906.png)

#### 让浮动效果可视化

我们可以在浮动元素上应用 margin，将文字推开，但不能在文字上应用 margin 将浮动元素推走。这是因为浮动的元素脱离了正常文档流，紧随其后的元素排布在它的“后方”。你可以将示例代码进行更改，来观察到这个现象。

在紧随浮动盒子的第一段文字上添加 `special` 类，然后在你的 CSS 文件中添加如下规则，它会赋予跟随其后的段落一个背景色。

```css
.special {
  background-color: rgb(79,185,227);
  padding: 10px;
  color: #fff;
}

```

为了更清晰的看到效果，将浮动的 `margin-left` 改为 `margin` 以将周围全部空出来。如此代码效果所示，你可以看到段落的背景色处于浮动盒子之下。

![image-20220822151251972](image-20220822151251972.png)

目标元素的[行内盒子](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Visual_formatting_model#line_boxes)已被缩短，故文字会排布在浮动元素周围，但是浮动元素从正常文档流移出，故段落的盒子仍然保持全部宽度。

### 清除浮动

我们看到，一个浮动元素会被移出正常文档流，且其他元素会显示在它的下方。如果我们不想让剩余元素也受到浮动元素的影响，我们需要 *停止* 它；这是通过添加 [`clear`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/clear) 属性实现的。

在前例的 HTML 代码中，向浮动元素下方的第二个段落添加 `cleared` 类，然后向 CSS 文件中添加以下样式：

```css
.cleared {
  clear: left;
}

```

![image-20220822151827188](image-20220822151827188.png)

应该看到，第二个段落已经停止了浮动，不会再跟随浮动元素排布了。`clear` 属性接受下列值：

- `left`：停止任何活动的左浮动
- `right`：停止任何活动的右浮动
- `both`：停止任何活动的左右浮动

### 清除浮动元素周围的盒子

现在你知道了如何停止浮动元素其后元素的浮动行为。我们来看个例子，如果存在一个盒子 *同时* 包含了很高的浮动元素和一个很短的段落，会发生什么。

#### 问题所在

改变你的文档结构，使得第一个段落与浮动的盒子共同处于类名为 `wrapper` 的 [`<div>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/div) 元素之下。

```html
<div class="wrapper">
  <div class="box">Float</div>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus aliquam dolor, eu lacinia lorem placerat vulputate.</p>
</div>

```

在你的 CSS 代码中，为 `.wrapper` 类添加如下规则并重载页面：

```css
.wrapper {
  background-color: rgb(79,185,227);
  padding: 10px;
  color: #fff;
}

```

此外，将原先的 `.cleared` 类移除：

```diff
-.cleared {
-  clear: left;
-}

```

你会看到，就像示例代码一样，如果将背景色属性置于段落上，那么这个背景色将处于浮动元素之下。

![image-20220822152606432](image-20220822152606432.png)

再一次强调，这是因为浮动元素处于正常文档流之外，停止紧随其后元素的浮动并不像之前那样奏效。如果你想让盒子联合包住浮动的项目以及第一段文字，同时让紧随其后的内容从盒子中清除浮动，这就是一个问题。

有三种方法可以处理这个问题，其中的两种在所有浏览器中均可以奏效（虽然看上去有点“小技巧”），剩下的一种是可以处理问题的较新的解决方案。

#### clearfix 小技巧

传统上，这个问题通常由所谓的 "clearfix 小技巧" 解决，其过程为：先向包含浮动内容及其本身的盒子后方插入一些生成的内容，并将生成的内容清除浮动。

向示例中添加以下 CSS 代码：

```css
.wrapper::after {
  content: "";
  clear: both;
  display: block;
}

```

现在重载页面，盒子的浮动就应该清除了。这与在浮动盒子后手动添加诸如 `div` 的 HTML 元素，并设置其样式为 `clear:both` 是等效的。

![image-20220822152830012](image-20220822152830012.png)

#### 使用 overflow

一个替代的方案是将包裹元素的 [`overflow`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/overflow) 属性设置为除 `visible` 外的其他值。

移除上一节添加的 clearfix CSS 代码；在包裹元素上添加 `overflow: auto` 规则。现在，盒子应该再一次停止浮动。

```css
.wrapper {
    background-color: rgb(79,185,227);
    padding: 10px;
    color: #fff;
}
```

这个例子之所以能够生效，是因为创建了所谓的 **块格式化上下文（BFC）**。可以把它看作页面内部包含所需元素的一小块布局区域。如此设置可以让浮动元素包含在 BFC 及其背景之内。大部分情况下这种小技巧都可以奏效，但是可能会出现莫名其妙的滚动条或裁剪阴影，这是使用 overflow 带来的一些副作用。

#### display: flow-root

一个较为现代的方案是使用 `display` 属性的 `flow-root` 值。它可以无需小技巧来创建块格式化上下文（BFC），在使用上没有副作用。

从 `.wrapper` 中移除 `overflow: auto` 规则并添加 `display: flow-root`。如果你的浏览器支持该属性（[支持的浏览器列表](https://developer.mozilla.org/zh-CN/docs/Web/CSS/display#浏览器兼容性)），盒子就会停止浮动。

```css
.wrapper {
  background-color: rgb(79,185,227);
  padding: 10px;
  color: #fff;
  display: flow-root;
}

```

## 定位

定位允许你从正常的文档流布局中取出元素，并使它们具有不同的行为，例如放在另一个元素的上面，或者始终保持在浏览器视窗内的同一位置。本文解释的是定位 ([`position`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/position)) 的各种不同值，以及如何使用它们。

### 文档流

定位是一个相当复杂的话题，所以我们深入了解代码之前，让我们审视一下布局理论，并让我们了解它的工作原理。

首先，围绕元素内容添加任何内边距、边界和外边距来布置单个元素盒子——这就是[盒模型](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/The_box_model) ，我们前面看过。默认情况下，块级元素的内容宽度是其父元素的宽度的 100％，并且与其内容一样高。内联元素高宽与他们的内容高宽一样。你不能对内联元素设置宽度或高度——它们只是位于块级元素的内容中。 如果要以这种方式控制内联元素的大小，则需要将其设置为类似块级元素 `display: block;`。

这只是解释了单个元素，但是元素相互之间如何交互呢？**正常的布局流**（在布局介绍文章中提到）是将元素放置在浏览器视口内的系统。默认情况下，块级元素在视口中垂直布局——每个都将显示在上一个元素下面的新行上，并且它们的外边距将分隔开它们。

内联元素表现不一样——它们不会出现在新行上；相反，它们互相之间以及任何相邻（或被包裹）的文本内容位于同一行上，只要在父块级元素的宽度内有空间可以这样做。如果没有空间，那么溢流的文本或元素将向下移动到新行。

如果两个相邻元素都在其上设置外边距，并且两个外边距接触，则两个外边距中的较大者保留，较小的一个消失——这叫[外边距折叠](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Box_Model/Mastering_margin_collapsing), 我们之前也遇到过。

让我们来看一个简单的例子来解析这一切：

```html
<h1>Basic document flow</h1>

<p>I am a basic block level element. My adjacent block level elements sit on new lines below me.</p>

<p>By default we span 100% of the width of our parent element, and we are as tall as our child content. Our total width and height is our content + padding + border width/height.</p>

<p>We are separated by our margins. Because of margin collapsing, we are separated by the width of one of our margins, not both.</p>

<p>inline elements <span>like this one</span> and <span>this one</span> sit on the same line as one another, and adjacent text nodes, if there is space on the same line. Overflowing inline elements will <span>wrap onto a new line if possible (like this one containing text)</span>, or just go on to a new line if not, much like this image will do: <img src="https://mdn.github.io/css-examples/learn/backgrounds-borders/star.png"></p>

```

```css
body {
    width: 500px;
    margin: 0 auto;
}

p {
    background: #9aefef;
    border: 3px solid #7979c9;
    padding: 10px;
    margin: 10px;
}

span {
    background: #d37676;
    border: 1px solid #887b7b;
}

```



在我们阅读本文时，我们将多次重复这个例子，因为我们要展示不同定位选项的效果。

如果可能，我们希望你在本地计算机上跟随练习

### 介绍定位

定位的整个想法是允许我们覆盖上面描述的基本文档流行为，以产生有趣的效果。如果你想稍微改变布局中一些盒子的位置，使它们的默认布局流程位置稍微有点古怪，不舒服的感觉呢？定位是你的工具。或者，如果你想要创建一个浮动在页面其他部分顶部的 UI 元素，并且/或者始终停留在浏览器窗口内的相同位置，无论页面滚动多少？定位使这种布局工作成为可能。

有许多不同类型的定位，你可以对 HTML 元素生效。要使某个元素上的特定类型的定位，我们使用[`position`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/position)属性。

#### 静态定位

静态定位是每个元素获取的默认值——它只是意味着“将元素放入它在文档布局流中的正常位置 ——这里没有什么特别的。

为了演示这一点，并为以后的部分设置示例，首先在 HTML 中添加一个`positioned` 的 `class` 到第二个`<p>`：

```html
<p class="positioned"> ... </p>

```

现在，将以下规则添加到 CSS 的底部：

```css
.positioned {
  position: static;
  background: yellow;
}

```

如果现在保存和刷新，除了第 2 段的更新的背景颜色，根本没有差别。这很好——正如我们之前所说，静态定位是默认行为！

#### 相对定位

相对定位是我们将要看的第一个位置类型。它与静态定位非常相似，占据在正常的文档流中，但你可以修改它的最终位置，包括让它与页面上的其他元素重叠。让我们继续并更新代码中的 `position` 属性：

```css
position: relative;

```

如果你在此阶段保存并刷新，则结果根本不会发生变化。那么如何修改元素的位置呢？你需要使用[`top`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/top)，[`bottom`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/bottom)，[`left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/left)和[`right`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/right)属性，我们将在下一节中解释。

#### 介绍 top、bottom、left 和 right

[`top`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/top), [`bottom`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/bottom), [`left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/left), 和 [`right`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/right) 来精确指定要将定位元素移动到的位置。要尝试这样做，请在 CSS 中的 `.positioned` 规则中添加以下声明：

```css
top: 30px;
left: 30px;

```

> **备注：** 这些属性的值可以采用逻辑上期望的任何单位 ——px，mm，rems，％等。

如果你现在保存和刷新，你会得到一个这样的结果：

![image-20220822154620319](image-20220822154620319.png)

酷，是吗？好吧，所以这个结果这可能不是你期待的——为什么它移动到底部和右边，但我们指定顶部和左边？听起来不合逻辑，但这只是相对定位工作的方式——你需要考虑一个看不见的力，推动定位的盒子的一侧，移动它的相反方向。所以例如，如果你指定 `top: 30px;`一个力推动框的顶部，使它向下移动 30px。

#### 绝对定位

绝对定位带来了非常不同的结果。让我们尝试改变代码中的位置声明如下：

``` css
position: absolute;

```

如果你现在保存和刷新，你应该看到这样：

![image-20220822154727092](image-20220822154727092.png)

首先，请注意，定位的元素应该在文档流中的间隙不再存在——第一和第三元素已经靠在一起，就像第二个元素不再存在！好吧，在某种程度上，这是真的。绝对定位的元素不再存在于正常文档布局流中。相反，它坐在它自己的层独立于一切。这是非常有用的：这意味着我们可以创建不干扰页面上其他元素的位置的隔离的 UI 功能。例如，弹出信息框和控制菜单；翻转面板；可以在页面上的任何地方拖放的 UI 功能……

第二，注意元素的位置已经改变——这是因为[`top`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/top)，[`bottom`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/bottom)，[`left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/left)和[`right`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/right)以不同的方式在绝对定位。它们指定元素应距离每个包含元素的边的距离，而不是指定元素应该移入的方向。所以在这种情况下，我们说的绝对定位元素应该位于从“包含元素”的顶部 30px，从左边 30px。

> **备注：** 如果需要，你可以使用 [`top`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/top)，[`bottom`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/bottom)、[`left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/left) 和 [`right`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/right) 调整元素大小。尝试设置 `top: 0; bottom: 0; left: 0; right: 0;` 和 `margin: 0;` 对你定位的元素，看看会发生什么！之后再回来

> **备注：** 是的，margins 仍会影响定位的元素。然而 margin collapsing 不会。

#### 定位上下文

哪个元素是绝对定位元素的“包含元素“？这取决于绝对定位元素的父元素的 position 属性。(参见 [Identifying the containing block](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Containing_block#identifying_the_containing_block)).

如果所有的父元素都没有显式地定义 position 属性，那么所有的父元素默认情况下 position 属性都是 static。结果，绝对定位元素会被包含在**初始块容器**中。这个初始块容器有着和浏览器视口一样的尺寸，并且`<html>`元素也被包含在这个容器里面。简单来说，绝对定位元素会被放在`<html>`元素的外面，并且根据浏览器视口来定位。

绝对定位元素在 HTML 源代码中，是被放在`<body>`中的，但是在最终的布局里面，它离页面 (而不是`<body>`) 的左边界、上边界有 30px 的距离。我们可以改变**定位上下文** —— 绝对定位的元素的相对位置元素。通过设置其中一个父元素的定位属性 —— 也就是包含绝对定位元素的那个元素（如果要设置绝对定位元素的相对元素，那么这个元素一定要包含绝对定位元素）。 为了演示这一点，将以下声明添加到你的 body 规则中：

```css
position: relative;

```

应该得到以下结果：

![image-20220822155122877](image-20220822155122877.png)

定位的元素现在相对于`<body>`元素。

#### 介绍 z-index

所有这些绝对定位很有趣，但还有另一件事我们还没有考虑到 ——当元素开始重叠，什么决定哪些元素出现在其他元素的顶部？在我们已经看到的示例中，我们在定位上下文中只有一个定位的元素，它出现在顶部，因为定位的元素胜过未定位的元素。当我们有不止一个的时候呢？

尝试添加以下到你的 CSS，使第一段也是绝对定位：

```css
p:nth-of-type(1) {
  position: absolute;
  background: lime;
  top: 10px;
  right: 30px;
}

```

此时，你将看到第一段的颜色为绿色，移出文档流程，并位于原始位置上方一点。它也堆叠在原始的 `.positioned` 段落下，其中两个重叠。这是因为 `.positioned` 段落是源顺序 (HTML 标记) 中的第二个段落，并且源顺序中后定位的元素将赢得先定位的元素。

你可以更改堆叠顺序吗？是的，你可以使用[`z-index`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/z-index)属性。 “z-index”是对 z 轴的参考。你可以从源代码中的上一点回想一下，我们使用水平（x 轴）和垂直（y 轴）坐标来讨论网页，以确定像背景图像和阴影偏移之类的东西的位置。 （0,0）位于页面（或元素）的左上角，x 和 y 轴跨页面向右和向下（适合从左到右的语言，无论如何）。

网页也有一个 z 轴：一条从屏幕表面到你的脸（或者在屏幕前面你喜欢的任何其他东西）的虚线。[`z-index`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/z-index) 值影响定位元素位于该轴上的位置；正值将它们移动到堆栈上方，负值将它们向下移动到堆栈中。默认情况下，定位的元素都具有 z-index 为 auto，实际上为 0。

要更改堆叠顺序，请尝试将以下声明添加到 `p:nth-of-type(1)` 规则中：

```css
z-index: 1;

```

![image-20220822155355662](image-20220822155355662.png)

请注意，z-index 只接受无单位索引值；你不能指定你想要一个元素是 Z 轴上 23 像素—— 它不这样工作。较高的值将高于较低的值，这取决于你使用的值。使用 2 和 3 将产生与 300 和 40000 相同的效果。

#### 固定定位

还有一种类型的定位覆盖——fixed。这与绝对定位的工作方式完全相同，只有一个主要区别：绝对定位将元素固定在相对于其位置最近的祖先。（如果没有，则为初始包含它的块）而固定定位固定元素则是相对于浏览器视口本身。这意味着你可以创建固定的有用的 UI 项目，如持久导航菜单。

让我们举一个简单的例子来说明我们的意思。首先，从 CSS 中删除现有的 `p:nth-of-type(1)` 和`.positioned` 规则。

现在，更新 `body` 规则以删除`position: relative;` 声明并添加固定高度，如此：

```css
body {
  width: 500px;
  height: 1400px;
  margin: 0 auto;
}

```

现在我们要给`<h1>` 元素 `position: fixed;`，并让它坐在视口的顶部中心。将以下规则添加到 CSS：

```css
h1 {
  position: fixed;
  top: 0;
  width: 500px;
  margin: 0 auto;
  background: white;
  padding: 10px;
}

```

`top: 0;`是要使它贴在屏幕的顶部；我们然后给出标题与内容列相同的宽度，并使用可靠的老技巧 `margin: 0 auto;` 使它居中。然后我们给它一个白色背景和一些内边距，所以内容将不会在它下面可见。

![image-20220822155954597](image-20220822155954597.png)

如果你现在保存并刷新，你会看到一个有趣的小效果，标题保持固定，内容显示向上滚动并消失在其下。但是我们可以改进这一点——目前标题下面挡住一些内容的开头。这是因为定位的标题不再出现在文档流中，所以其他内容向上移动到顶部。我们要把它向下移动一点；我们可以通过在第一段设置一些顶部边距来做到这一点。添加：

```css
p:nth-of-type(1) {
  margin-top: 60px;
}

```

![image-20220822160408658](image-20220822160408658.png)

#### position: sticky

还有一个可用的位置值称为 position: sticky，比起其他位置值要新一些。它基本上是相对位置和固定位置的混合体，它允许被定位的元素表现得像相对定位一样，直到它滚动到某个阈值点（例如，从视口顶部起 10 像素）为止，此后它就变得固定了。例如，它可用于使导航栏随页面滚动直到特定点，然后粘贴在页面顶部。

```css
.positioned {
  position: sticky;
  top: 30px;
  left: 30px;
}

```

![image-20220822160556715](image-20220822160556715.png)

`position: sticky` 的另一种有趣且常用的用法，是创建一个滚动索引页面。在此页面上，不同的标题会停留在页面顶部。这样的示例的标记可能如下所示：

```css
<h1>Sticky positioning</h1>

<dl>
    <dt>A</dt>
    <dd>Apple</dd>
    <dd>Ant</dd>
    <dd>Altimeter</dd>
    <dd>Airplane</dd>
    <dt>B</dt>
    <dd>Bird</dd>
    <dd>Buzzard</dd>
    <dd>Bee</dd>
    <dd>Banana</dd>
    <dd>Beanstalk</dd>
    <dt>C</dt>
    <dd>Calculator</dd>
    <dd>Cane</dd>
    <dd>Camera</dd>
    <dd>Camel</dd>
    <dt>D</dt>
    <dd>Duck</dd>
    <dd>Dime</dd>
    <dd>Dipstick</dd>
    <dd>Drone</dd>
    <dt>E</dt>
    <dd>Egg</dd>
    <dd>Elephant</dd>
    <dd>Egret</dd>
</dl>

```

CSS 可能如下所示。在正常布局流中，`<dt>`元素将随内容滚动。当我们在`<dt>`元素上添加`position: sticky`，并将top的值设置为 0，当标题滚动到视口的顶部时，支持此属性的浏览器会将标题粘贴到那个位置。随后，每个后续标题将替换前一个标题，直到它向上滚动到该位置。

```css
body {
  width: 500px;
  height: 1400px;
  margin: 0 auto;
}

dt {
  background-color: black;
  color: white;
  padding: 10px;
  position: sticky;
  top: 0;
  left: 0;
  margin: 1em 0;
}

```

![image-20220822161143409](image-20220822161143409.png)

## 多列布局

多列布局声明提供了一种多列组织内容的方式，正如你在一些报纸中看到的那样。 这篇文章介绍怎么使用这一特性。

### 一个简单的例子

我们将学习怎么使用多列布局，通常也简写为 *multicol*。你可以从这里开始 [downloading the multicol starting point file](https://github.com/mdn/learning-area/blob/master/css/css-layout/multicol/0-starting-point.html) 然后在合适的地方加入 CSS。在这一小节的结尾，你可以看到最终代码的效果。

```html
<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Multicol starting point</title>
    <style>
        body {
            width: 90%;
            max-width: 900px;
            margin: 2em auto;
            font: .9em/1.2 Arial, Helvetica, sans-serif;
        }
    </style>
  </head>

<body>
    <div class="container">
        <h1>Simple multicol example</h1>

        <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus aliquam dolor, eu lacinia lorem placerat vulputate.
            Duis felis orci, pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at ultricies tellus
            laoreet sit amet. Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet orci vel, viverra
            egestas ligula. Curabitur vehicula tellus neque, ac ornare ex malesuada et. In vitae convallis lacus. Aliquam
            erat volutpat. Suspendisse ac imperdiet turpis. Aenean finibus sollicitudin eros pharetra congue. Duis ornare
            egestas augue ut luctus. Proin blandit quam nec lacus varius commodo et a urna. Ut id ornare felis, eget fermentum
            sapien.</p>

        <p>Nam vulputate diam nec tempor bibendum. Donec luctus augue eget malesuada ultrices. Phasellus turpis est, posuere
            sit amet dapibus ut, facilisis sed est. Nam id risus quis ante semper consectetur eget aliquam lorem. Vivamus
            tristique elit dolor, sed pretium metus suscipit vel. Mauris ultricies lectus sed lobortis finibus. Vivamus eu
            urna eget velit cursus viverra quis vestibulum sem. Aliquam tincidunt eget purus in interdum. Cum sociis natoque
            penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
    </div>
</body>

</html>
```



#### 三列布局

我们从一些很简单的 HTML 开始； 用带有类 container 的简单包装，里面是标题和一些段落。

带有 `.container` 的 `<div>` 将成为我们 `multicol` 的容器。通过这两个属性开启 `multicol column-count` 或者 `column-width`。 ·column-count· 将创建指定数量的列，所以如果你把下面的 CSS 加到样式表里让后重载入页面，你将得到 3 列：

```css
.container {
  column-count: 3;
}

```

创建的这些列具有弹性的宽度 — 由浏览器计算出每一列分配多少空间。

![image-20220822161807512](image-20220822161807512.png)

#### 设置列宽

像下面这样使用 `column-width` 更改 CSS：

```css
.container {
  column-width: 200px;
}

```

浏览器将按照你指定的宽度尽可能多的创建列；任何剩余的空间之后会被现有的列平分。 这意味着你可能无法期望得到你指定宽度，除非容器的宽度刚好可以被你指定的宽度除尽。

![image-20220822161943470](image-20220822161943470.png)

### 给多列增加样式

Multicol 创建的列无法单独的设定样式。不存在让单独某一列比其他列更大的方法，同样无法为某一特定的列设置独特的背景色、文本颜色。你有两个机会改变列的样式：

- 使用 [`column-gap`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/column-gap) 改变列间间隙。
- 用 [`column-rule`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/column-rule) 在列间加入一条分割线。

以上面的代码为例，增加 `column-gap` 属性可以更改列间间隙。

你可以尝试不同的值 — 该属性接受任何长度单位。现在再加入 `column-rule`。和你之前遇到的 [`border`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border) 属性类似， `column-rule` 是 [`column-rule-color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/column-rule-color) 和 [`column-rule-style`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/column-rule-style)的缩写，接受同 `border` 一样的单位。

```css
.container {
  column-count: 3;
  column-gap: 20px;
  column-rule: 4px dotted rgb(79, 185, 227);
}

```

![image-20220822162120385](image-20220822162120385.png)

值得一提的是这条分割线本身并不占用宽度。它置于用 `column-gap` 创建的间隙内。如果需要更多空间，你需要增加 `column-gap` 的值。

### 列与内容折断

多列布局的内容被拆成碎块。和多页媒体上的内容表现大致一样 — 比如打印网页的时候。 当你把内容放入多列布局容器内，内容被拆成碎块放进列中，内容折断（译者注：比如断词断句）使得这一效果可以实现。

有时，这种折断内容会降低阅读体验。在下面的举例中，我用 multicol 对一系列盒子布局，每一小块里有小标题和和一些文字。标题和文字可能被折断点拆开，从而降低阅读体验。

```html
<div class="container">
  <div class="card">
    <h2>I am the heading</h2>
    <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus aliquam dolor, eu lacinia lorem placerat
                vulputate. Duis felis orci, pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at ultricies
                tellus laoreet sit amet. Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet orci
                vel, viverra egestas ligula.</p>
    </div>

    <div class="card">
      <h2>I am the heading</h2>
      <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus aliquam dolor, eu lacinia lorem placerat
                vulputate. Duis felis orci, pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at ultricies
                tellus laoreet sit amet. Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet orci
                vel, viverra egestas ligula.</p>
    </div>

    <div class="card">
      <h2>I am the heading</h2>
      <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus aliquam dolor, eu lacinia lorem placerat
                vulputate. Duis felis orci, pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at ultricies
                tellus laoreet sit amet. Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet orci
                vel, viverra egestas ligula.</p>
    </div>
    <div class="card">
      <h2>I am the heading</h2>
      <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus aliquam dolor, eu lacinia lorem placerat
                vulputate. Duis felis orci, pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at ultricies
                tellus laoreet sit amet. Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet orci
                vel, viverra egestas ligula.</p>
    </div>

    <div class="card">
      <h2>I am the heading</h2>
      <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus aliquam dolor, eu lacinia lorem placerat
                vulputate. Duis felis orci, pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at ultricies
                tellus laoreet sit amet. Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet orci
                vel, viverra egestas ligula.</p>
    </div>

    <div class="card">
      <h2>I am the heading</h2>
      <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus aliquam dolor, eu lacinia lorem placerat
                vulputate. Duis felis orci, pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at ultricies
                tellus laoreet sit amet. Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet orci
                vel, viverra egestas ligula.</p>
    </div>

    <div class="card">
      <h2>I am the heading</h2>
      <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus aliquam dolor, eu lacinia lorem placerat
                vulputate. Duis felis orci, pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at ultricies
                tellus laoreet sit amet. Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet orci
                vel, viverra egestas ligula.</p>
    </div>

</div>

```

```css
.container {
  column-width: 250px;
  column-gap: 20px;
}

.card {
  background-color: rgb(207, 232, 220);
  border: 2px solid rgb(79, 185, 227);
  padding: 10px;
  margin: 0 0 1em 0;
}

```

![image-20220822162446684](image-20220822162446684.png)

#### 设置 break-inside

我们可以使用 [CSS Fragmentation](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fragmentation) 中声明的属性控制这一特性。 这份规范提供了一些属性来控制 multicol 和多页媒体中的内容拆分、折断。比如，在规则 `.card` 上添加属性[`break-inside`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/break-inside)，并设值 `avoid` 。`.card` 是标题和文本的容器，我们不想拆开这个盒子。

现阶段，增加旧属性 `page-break-inside: avoid` 能够获得更好的浏览器支持。

```css
.card {
  break-inside: avoid;
  page-break-inside: avoid;
  background-color: rgb(207,232,220);
  border: 2px solid rgb(79,185,227);
  padding: 10px;
  margin: 0 0 1em 0;
}

```

![image-20220822162551805](image-20220822162551805.png)

刷新页面，你的盒子就会呆在一起了。

### 小结

现在你知道多列布局的基本用法了，构建页面时又多了一种布局选择。

## 响应式设计

早年设计 Web 时，页面是以适配特定的屏幕大小为考量创建的。如果用户正在使用比设计者考虑到的更小或者更大的屏幕，那么结果从多余的滚动条，到过长的行和没有被合理利用的空间，不一而足。随着人们使用的屏幕尺寸的种类越来越多，出现了响应式网页设计的概念（*responsive web design，RWD*），RWD 指的是允许 Web 页面适应不同屏幕宽度因素等，进行布局和外观的调整的一系列实践。这是改变我们设计多设备网页的方式的思想，在这篇文章里，我们将会帮你理解掌握它时所需知道的主要技能。

### 历史上的网站布局

在历史上的某个时刻，设计网站时，你有两个选择：

- 你可以创建一个“液态”站点，它会拉伸以充满整个浏览器视窗；
- 或者是一个“固定宽度”站点，它有一个以像素计的固定尺寸。

这两种途径会倾向于导致它的表现只有在设计者的屏幕上才是最佳的！液态站点导致了小屏幕上的设计会挤成一团（如下所示），以及大屏幕上难以阅读的很长的行长度。

![image-20220822162758699](image-20220822162758699.png)

固定宽度站点的一个可能的后果是，在比站点更窄的屏幕上会出现一个水平滚动条（如下所示），在大屏幕上的设计边缘还会有许多空白。

随着移动 Web 在早期的功能手机上开始成为现实，希望拥抱移动端的公司普遍希望为他们的网站创建一个有着不同的网址的移动版本（大多是像*m.example.com*或者*example.mobi*这类）。这意味着一个网站需要开发两个分开的版本，而且要保持时效性。

除此以外，这些移动网站的体验经常缩水。由于移动设备变得更加强大，足以显示完整的网站，对于那些被困在移动版网站的移动端用户来说，这是很折磨人的，他们因此也没法获取他们知道在支持所有功能的桌面版网站上能找到的信息。

### 响应式设计之前的灵活布局

人们开发了许多方式，尽力解决建设网站时使用液态和固定宽度的方式所带来的弊端。2004 年，Cameron Adams 写了一篇题为《[Resolution dependent layout](https://www.themaninblue.com/writing/perspective/2004/09/21/)》的帖子，描述了一种可以创造适应多种屏幕分辨率的设计的方式。这种方式需要 JavaScript 来探测屏幕的分辨率，载入恰当的 CSS。

Zoe Mickley Gillenwater 深刻影响了[她的著作](http://zomigi.com/blog/voices-that-matter-slides-available/)，在里面描述并标准化了可变站点建立的不同方式，试图在充满屏幕和完全保持固定尺寸之间找到最佳平衡。

### 响应式设计

“响应式设计”这个词是[Ethan Marcotte 在 2010 年首度提出的](https://alistapart.com/article/responsive-web-design/)，他将其描述为三种技术的混合使用。

1. 第一个是液态网格，这早先已由 Gillenwater 进行探讨，可以在 Marcotte 的文章《[Fluid Grids](https://alistapart.com/article/fluidgrids/)》（出版于 2009 年的《A List Apart》上）中读到。
2. 第二个是[液态图像](https://unstoppablerobotninja.com/entry/fluid-images)的理念。通过使用相当简单的将设置`max-width`属性设置为`100%`的技术，图像可以在包含它们的列变得比图像原始尺寸窄的时候，缩放得更小，但总不会变得更大。这使得图像可以被缩放，以被放到一个灵活尺寸的列，而不是溢出出去，同时也不会在列宽于图像的时候，使图像变得太大以至于画质变得粗糙。
3. 第三个关键的组件是[媒体查询](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries)。媒体查询使以往 Cameron Adams 探讨过的、由 JavaScript 实现的布局类型切换，可以只使用 CSS 实现。和所有尺寸的屏幕都使用一种布局不同的是，布局是可以改变的：侧栏可以在小屏幕上重新布局，而替代用的导航栏也可以显示出来。

需要你理解的很重要的一点是**响应式 Web 设计不是单独的技术**，它是描述 Web 设计的一种方式、或者是一组最佳实践的一个词，它是用来建立可以**响应**查看内容的设备的样式的一个词。在 Marcotte's 原来的探索中，这意味着灵活网格（使用 float）和媒体查询，但是在这篇文章写就的几乎十年以后，Web 的响应式工作已经成为了默认做法。现代的 CSS 布局方式基本上就是响应式的，而且我们在 Web 平台上内置了新的东西，使得设计响应式站点变得容易。

这篇文章的余下部分会为你指出，在建立响应式站点的时候，你可能会用到的各式 Web 平台的特色功能。

### 媒介查询

响应式设计仅仅是因为媒介查询才新兴起来的。媒介查询第三级规范已经在 2009 年成为了候选推荐，这意味着它可视为准备好在浏览器中开始支持了。媒介查询允许我们运行一系列测试，例如用户的屏幕是否大于某个宽度或者某个分辨率，并将 CSS 选择性地适应用户的需要应用在样式化页面上。

例如，下面的媒体查询进行测试，以知晓当前的 Web 页面是否被展示为屏幕媒体（也就是说不是印刷文档），且视口至少有 800 像素宽。用于`.container`选择器的 CSS 将只会在这两件前提存在的情况下应用。

```css
@media screen and (min-width: 800px) {
  .container {
    margin: 1em 2em;
  }
}

```

你可以在一张样式表上加入多条媒体查询，调整整个页面或者部分页面以达到适应各式屏幕尺寸的最佳效果。媒体查询，以及样式改变时的点，被叫做*断点*（breakpoints）。

使用媒体查询时的一种通用方式是，为窄屏设备（例如移动设备）创建一个简单的单栏布局，然后检查是否是大些的屏幕，在你知道你有足够容纳的屏幕宽度的时候，开始采用一种多栏的布局。这经常被描述为**移动优先**设计。

在 MDN 文档中的[媒体查询](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries)中了解更多

### 灵活网格

响应式站点不只是在断点之间改变它们的布局，它们是建立在灵活网格上的。一个灵活网格意味着你不需要适配每个可能使用的设备尺寸，然后为其建立一个精确到像素级的适配布局。那种方式在现存有如此多种不同大小设备的前提下是不可能实现的，比如至少在台式机上，人们并不总是让他们的浏览器窗口最大化的。

使用灵活网格，你只需要加进去一个断点，在内容看起来不齐整的时候改变设计。例如如果一行随着屏幕大小增加而增长得不可读的长，或者是一个盒子在变窄时把每行的两个单词挤到一起。

早年间进行响应式设计的时候，我们唯一的实现布局的选项是使用[float](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Floats)。灵活浮动布局是这样实现的，让每个元素都有一个作为宽度的百分数，而且确保整个布局的和不会超过 100%。在他对于液态网格文章的原文中，Marcotte 详细描述了一种布局的法则，通过使用像素并把布局转化为百分数的方式设计。

```
target / context = result

```

例如如果我们的预期栏尺寸为 60 像素，而且它所在的上下文（或者容器）为 960 像素，我们在将零点二的空间移动到右边以后，用 960 去除 60，得到我们能够使用在我们的 CSS 上的值。

```css
.col {
  width: 6.25%; /* 60 / 960 = 0.0625 */
}

```

这种方式将会在今天整个 Web 上的许多地方上看到，而且它被我们的[Legacy layout methods](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Legacy_Layout_Methods)一文中的布局一节中记载。可能你将会在工作中遇到使用这种方式的站点，所以有必要理解它，即使是在你不用建立一个使用浮动基础的灵活网格的情况下。

下面的例子阐释了一个使用媒体查询和灵活网格的简单响应式设计。在窄屏幕上，布局将盒子堆叠在另一个的上面：

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>A simple float-based responsive design</title>
    <style>
      body {
        font: 1.2em Helvetica, Arial, sans-serif;
        margin: 20px;
        padding: 0;
        background-color: #eee;
      }
      .wrapper {
        max-width: 960px;
        margin: 2em auto;
      }

      .col1,
      .col2 {
        background-color: #fff;
      }

      @media screen and (min-width: 600px) {
        .col1 {
          width: 31.24999999%;
          float: left;
        }

        .col2 {
          width: 64.58333331%;
          float: right;
        }
      }
    </style>
</head>

<body>

    <div class="wrapper">
      <div class="col1">
        <p>This layout is responsive. See what happens if you make the browser window wider or narrow.</p>
      </div>
      <div class="col2">
          <p>One November night in the year 1782, so the story runs, two brothers sat over their winter fire in the little French town of Annonay, watching the grey smoke-wreaths from the hearth curl up the wide chimney. Their names were Stephen and Joseph Montgolfier, they were papermakers by trade, and were noted as possessing thoughtful minds and a deep interest in all scientific knowledge and new discovery.</p>
          <p>Before that night—a memorable night, as it was to prove—hundreds of millions of people had watched the rising smoke-wreaths of their fires without drawing any special inspiration from the fact.”</p>
      </div>

    </div>
</body>

</html>
```

![image-20220822163902379](image-20220822163902379.png)

![image-20220822163852634](image-20220822163852634.png)

### 现代布局技术

现代布局方式，例如[多栏布局](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Multiple-column_Layout)、[伸缩盒](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox)和[网格](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Grids)默认是响应式的。它们都假设你在尽力创建一个可伸缩网格，而且给了你更容易这样做的方式。

#### 多个列

这些布局方式中最老的一个是多个列，即当你指定一个`column-count`的时候，这意指你希望把你的内容分成多少列。浏览器之后会算出这些列的大小，这是一个随着屏幕尺寸变化的尺寸。

```css
.container {
  column-count: 3;
}

```

如果你却去指定`column-width`的话，你是在指定一个*最小*宽度。浏览器会尽可能多数量地创建这一宽度的列，只要它们可以恰当地放进容器里面，然后将所有列之间的剩余空间共享出去。因而列的数量会随着空间的多少而改变。

```css
.container {
  column-width: 10em;
}

```

#### 伸缩盒

在伸缩盒中，初始的行为是，弹性的物件将参照容器里面的空间的大小，缩小和分布物件之间的空间。通过更改`flex-grow`和 `flex-shrink`的值，你可以指示在物件遇到周围有更多或者更少的空间的情况下，你所期望的物件表现。

在下面的示例中，和布局专题的[Flexbox: Flexible sizing of flex items](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox#flexible_sizing_of_flex_items)中所描述的那样，使用了`flex: 1`的简写，可伸缩物件每个将会占据一份可伸缩容器中相等大小的空间。

```css
.container {
  display: flex;
}

.item {
  flex: 1;
}

```

> **备注：** 作为一个示例，我们已经重构了上面的简单响应式布局，这次我们用了伸缩盒。你可以看看我们是怎么样才不再需要使用奇怪的百分数值来计算列的尺寸的：[示例](https://mdn.github.io/css-examples/learn/rwd/flex-based-rwd.html)、[源代码](https://github.com/mdn/css-examples/blob/master/learn/rwd/flex-based-rwd.html)。



#### CSS 网格

在 CSS 网格布局中，`fr`单位许可了跨网格轨道可用空间的分布。下面的示例创建了一个有着 3 个大小为`1fr`的轨道的网格容器。这会创建三个列轨道，每个占据了容器中可用空间的一部分。你可以在[Flexible grids with the fr unit](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Grids#flexible_grids_with_the_fr_unit)下的学习布局网格专题了解更多和这一方式相关的信息。

```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}

```

> **备注：** 网格布局版本的代码要更简单，因为我们可以在.wrapper 上定义列[：示例](https://mdn.github.io/css-examples/learn/rwd/grid-based-rwd.html)，[源代码](https://github.com/mdn/css-examples/blob/master/learn/rwd/grid-based-rwd.html)。



### 响应式图像

最简单的处理响应式图像的方式是在 Marcotte 的早年的关于响应式设计的文章上所描述的那样。基本来说，你可以用一张有着所需最大尺寸的图像。然后缩放它。这仍然是今日所使用的一种方式，而且在大多数样式表里面，你在某些地方可以找到下面的 CSS：

```css
img {
  max-width: 100%:
}

```

这种方式有显然的弊端。图像有可能会显示得比它的原始尺寸小很多，以至于浪费带宽——一个移动端用户会下载几倍于他们在浏览器窗口中实际看到的大小的图像。此外，你可能不想在移动端和桌面端有相同的图像宽高比例。例如，在移动端，方形图像的表现会很好，但是在桌面端显示同样的内容则应用宽图像。或者，认识到移动端更小尺寸的图像的你也许会希望同时展示一张不同的图像，一张在小一点的屏幕上更容易理解的图像。这些东西不能简单通过缩放图像解决。

响应式图像，使用了`<picture>`元素和`<img>` `srcset`和`sizes` 特性，解决了这两个问题。你可以提供附带着“提示”（描述图像最适合的屏幕尺寸和分辨率的元数据）的多种尺寸，浏览器将会选择对设备最合适的图像，以确保用户下载尺寸适合他们使用的设备的图像。

你也可以给用于不同尺寸的图像做“艺术指导”，为不同的屏幕尺寸提供不同的图像裁切或者完全不同的图像。

你可以在 MDN 这里的学习 HTML 一节中找到详细的[响应式图像指南](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)。

[响应式图片 - 学习 Web 开发 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)

### 响应式排版

在早期的工作没有考虑的一个响应式设计的元素是响应式排版的理念。本质上讲，这描述了根据屏幕真实使用范围的多少，在媒体查询的同时改变字体大小。

在本例子中，我们想讲我们的一级标题设置为`4rem`，也就是说它将会有我们的基础字体的四倍大。这真的是个很大的标题！我们只想在大些的屏幕上有这么个超大的标题，那我们先弄个小点的标题，再使用媒体查询，在我们知道用户使用至少`1200px`的屏幕的时候，拿大些的尺寸覆写它。

```css
html {
  font-size: 1em;
}

h1 {
  font-size: 2rem;
}

@media (min-width: 1200px) {
  h1 {
    font-size: 4rem;
  }
}

```

我们已经编辑了我们在上面的响应式网格示例，让它同时包含了使用了圈出方式的响应式类型。你也可以看下随着布局变为两栏，标题是怎样转换大小的。

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>A simple float-based responsive design</title>
  <style>
      body {
          font: 1.2em Helvetica, Arial, sans-serif;
          margin: 20px;
          padding: 0;
          background-color: #eee;
      }
      .wrapper {
          max-width: 960px;
          margin: 2em auto;
      }

      .col1,
      .col2 {
          background-color: #fff;
      }

      @media screen and (min-width: 600px) {
          .col1 {
              width: 31.24999999%;
              float: left;
          }

          .col2 {
              width: 64.58333331%;
              float: right;
          }
      }
      html {
          font-size: 1em;
      }

      h1 {
          font-size: 2rem;
      }

      @media (min-width: 1200px) {
          h1 {
              font-size: 4rem;
          }
      }

  </style>
</head>

<body>

<div class="wrapper">
  <div class="col1">
    <h1>Title</h1>
    <p>This layout is responsive. See what happens if you make the browser window wider or narrow.</p>
  </div>
  <div class="col2">
    <p>One November night in the year 1782, so the story runs, two brothers sat over their winter fire in the little French town of Annonay, watching the grey smoke-wreaths from the hearth curl up the wide chimney. Their names were Stephen and Joseph Montgolfier, they were papermakers by trade, and were noted as possessing thoughtful minds and a deep interest in all scientific knowledge and new discovery.</p>
    <p>Before that night—a memorable night, as it was to prove—hundreds of millions of people had watched the rising smoke-wreaths of their fires without drawing any special inspiration from the fact.”</p>
  </div>

</div>
</body>

</html>
```

![image-20220822165349804](image-20220822165349804.png)

移动端，标题变小了：

![image-20220822165410017](image-20220822165410017.png)

正如这种排版方式展示的这样，你不需要让媒介查询只能改变页面的布局。它们也能用来调节每个元素，让它们在别的大小的屏幕上更加可用或者更具吸引力。

### 使用视口单位实现响应式排版

一个有趣的方式是使用视口单位`vw`来实现响应式排版。`1vw`等同于视口宽度的百分之一，即如果你用`vw`来设定字体大小的话，字体的大小将总是随视口的大小进行改变。

```css
h1 {
  font-size: 6vw;
}

```

问题在于，当做上面的事情的时候，因为文本总是随着视口的大小改变大小，用户失去了放缩任何使用`vw`单位的文本的能力。**所以你永远都不要只用 viewport 单位设定文本。**

这里有一个解决方法，它使用了[`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/calc)，如果你将`vw`单位加到了使用固定大小（例如`em`或者`rem`）的值组，那么文本仍然是可放缩的。基本来说，是`vw`加在了放缩后的值上。

```css
h1 {
  font-size: calc(1.5rem + 3vw);
}

```

这就是说，我们只需要指定标题的字体大小一次，而不是为移动端设定它，然后再在媒介查询中重新定义它。字体会在你增加视口大小的时候逐渐增大。

**备注：** 查看这种情况的一个编排好的示例： [示例](https://mdn.github.io/css-examples/learn/rwd/type-vw.html)，[源代码](https://github.com/mdn/css-examples/blob/master/learn/rwd/type-vw.html)。

### 视口元标签

如果你看看一张响应式页面的 HTML 源代码，你通常将会在文档的`<head>`看到下面的[`<meta>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/meta)标签。

```html
<meta name="viewport" content="width=device-width,initial-scale=1">

```

这个元标签告诉移动端浏览器，它们应该将视口宽度设定为设备的宽度，将文档放大到其预期大小的 100%，在移动端以你所希望的为移动优化的大小展示文档。

为何需要这个？因为移动端浏览器倾向于在它们的视口宽度上说谎。

这个元标签的存在，是由于原来 iPhone 发布以后，人们开始在小的手机屏幕上阅览网页，而大多数站点未对移动端做优化的缘故。移动端浏览器因此会把视口宽度设为 960 像素，并以这个宽度渲染页面，结果展示的是桌面布局的缩放版本。其他的移动端浏览器（例如谷歌安卓上的）也是这么做的。用户可以在站点中放大、移动，查看他们感兴趣的那部分，但是这看起来很不舒服。如果你不幸遇到了一个没有响应式设计的网站，今天你还会看到这种情况。

麻烦的是，你的带断点和媒介查询的响应式设计不会在移动端浏览器上像预期那样工作。如果你有个窄屏布局，在 480 像素及以下的视口宽度下生效，但是视口是按 960 像素设定的，你将不会在移动端看到你的窄屏布局。通过设定`width=device-width`，你用设备的实际宽度覆写了苹果默认的`width=960px`，然后你的媒介查询就会像预期那样生效。

**所以你应该在你的文档头部\*总是\*包含上面那行 HTML。**

和视口元标签一起，你可以使用另外几个设定，但大体说来，上面那行就是你想要使用的。

- `initial-scale`：设定了页面的初始缩放，我们设定为 1。
- `height`：特别为视口设定一个高度。
- `minimum-scale`：设定最小缩放级别。
- `maximum-scale`：设定最大缩放级别。
- `user-scalable`：如果设为`no`的话阻止缩放。

你应该避免使用`minimum-scale`、`maximum-scale`，尤其是将`user-scalable`设为`no`。用户应该有权力尽可能大或小地进行缩放，阻止这种做法会引起访问性问题。

> **备注：** 有一个 CSS @规则是被设计用来替换掉视口元标签的——[@viewport](https://developer.mozilla.org/en-US/docs/Web/CSS/@viewport)——但是浏览器对它的支持太差了。它是在 IE 和 Edge 中引入的，但自从 Chromium 内核的 Edge 发布以后，它就不再受到 Edge 浏览器支持了。



### 小结

响应式设计指的是一个响应浏览环境的网页或者应用设计。它涵盖了很多 CSS 和 HTML 的功能和技术，现在基本上就是我们默认建设网站的方式。想一下你在手机上访问的网站，遇到一个缩放的桌面版网站，或者你需要向侧边滚动来寻找东西的网站可能是相当不寻常的。这是因为 Web 已经迁移到了这种响应式设计的方式上。

响应式设计指的是一个响应浏览环境的网页或者应用设计。它涵盖了很多 CSS 和 HTML 的功能和技术，现在基本上就是我们默认建设网站的方式。想一下你在手机上访问的网站，遇到一个缩放的桌面版网站，或者你需要向侧边滚动来寻找东西的网站可能是相当不寻常的。这是因为 Web 已经迁移到了这种响应式设计的方式上。

## 媒体查询入门指南

**CSS 媒体查询**为你提供了一种应用 CSS 的方法，仅在浏览器和设备的环境与你指定的规则相匹配的时候 CSS 才会真的被应用，例如“视口宽于 480 像素”的时候。媒体查询是响应式 Web 设计的关键部分，因为它允许你按照视口的尺寸创建不同的布局，不过它也可以用来探测和你的站点运行的环境相关联的其它条件，比如用户是在使用触摸屏还是鼠标。在本节课，你将会先学习到媒体查询的语法，然后继续在一个被安排好的示例中使用它，这个示例还会告诉你一个简单的设计是可以怎么被弄成响应式的。

### 媒体查询基础

最简单的媒体查询语法看起来是像这样的：

```css
@media media-type and (media-feature-rule) {
  /* CSS rules go here */
}

```

它由以下部分组成：

- 一个媒体类型，告诉浏览器这段代码是用在什么类型的媒体上的（例如印刷品或者屏幕）；
- 一个媒体表达式，是一个被包含的 CSS 生效所需的规则或者测试；
- 一组 CSS 规则，会在测试通过且媒体类型正确的时候应用。

#### 媒体类型

你可以指定的媒体类型为：

- `all`
- `print`
- `screen`
- `speech`

下面的媒体查询将会在页面被打印的时候把 body 设定为只有 12pt 大小。当页面在浏览器中载入的时候，它将不会生效。

```css
@media print {
    body {
        font-size: 12pt;
    }
}

```

> **备注：**这里的媒体类型是和所谓的[MIME type](https://developer.mozilla.org/zh-CN/docs/Glossary/MIME_type)不同的东西。

> **备注：**媒体类型是可选的，如果你没有在媒体查询中指示一个媒体类型的话，那么媒体查询默认会设为用于全部媒体类型。

#### 媒体特征规则

在指定了类型以后，你可以用一条规则指向一种媒体特征。

##### 宽和高

为了建立响应式设计（已经广受浏览器支持），我们一般最常探测的特征是视口宽度，而且我们可以使用`min-width`、`max-width`和`width`媒体特征，在视口宽度大于或者小于某个大小——或者是恰好处于某个大小——的时候，应用 CSS。

这些特征是用来创建响应不同屏幕大小的布局的。例如，要想在视口正好是 600 像素的时候，让 body 的文本变为红色，你可能会使用下面的媒体查询。

```css
@media screen and (width: 600px) {
    body {
        color: red;
    }
}

```

在浏览器中[打开这个示例](https://mdn.github.io/css-examples/learn/media-queries/width.html)，或者[查看源代码](https://github.com/mdn/css-examples/blob/master/learn/media-queries/width.html)。

`width`（和`height`）媒体特征可以以数值范围使用，于是就有了`min-`或者`max-`的前缀，指示所给的值是最小值还是最大值。例如，要让颜色在视口窄于 400 像素的时候变成蓝色的话，可以用`max-width`：

```css
@media screen and (max-width: 800px) {
    body {
        color: blue;
    }
}

```

在浏览器中[打开示例](https://mdn.github.io/css-examples/learn/media-queries/max-width.html)，或者[查看源代码](https://github.com/mdn/css-examples/blob/master/learn/media-queries/max-width.html)。

实践中，使用最小值和最大值对响应式设计有很多的用处，所以你会很少见到`width`或`height` 单独使用的情况。

还有许多其他媒体特征可以供你测试，尽管于 4 级和 5 级媒体查询规范中引入了一些新特征，它们受浏览器支持仍然有限。在 MDN 上，每个特征都已经同浏览器支持信息一同记载下来，你可以在[使用媒体查询：媒体特征](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries#media_features)中找到一张完整的列表。

##### 朝向

一个受到良好支持的媒体特征是`orientation`，我们可以用它测得竖放（portrait mode）和横放（landscape mode）模式。要在设备处于横向的时候改变 body 文本颜色的话，可使用下面的媒体查询。

```css
@media (orientation: landscape) {
    body {
        color: rebeccapurple;
    }
}

```

在浏览器中[打开此示例](https://mdn.github.io/css-examples/learn/media-queries/orientation.html)，或者[查看源代码](https://github.com/mdn/css-examples/blob/master/learn/media-queries/orientation.html)。

标准的桌面视图是横放朝向的，在这种朝向上能够表现良好的设计，在处于竖放模式的手机或平板电脑上可能不会表现得这么好。对朝向的测试可以帮你建立一个为竖放设备优化的布局。

##### 使用指点设备

作为四级规范的一部分，`hover`媒体特征被引入了进来。这种特征意味着你可以测试用户是否能在一个元素上悬浮，这也基本就是说他们正在使用某种指点设备，因为触摸屏和键盘导航是没法实现悬浮的。

```css
@media (hover: hover) {
    body {
        color: rebeccapurple;
    }
}

```

在浏览器中[打开此示例](https://mdn.github.io/css-examples/learn/media-queries/hover.html)，或者[查看源代码](https://github.com/mdn/css-examples/blob/master/learn/media-queries/hover.html)。

如果我们知道用户不能悬浮的话，我们可以默认显示一些交互功能。对于能够悬浮的用户，我们可以选择在悬浮在链接上的时候，让这些功能可用。

还是在四级规范中，出现了`pointer`媒体特征。它可取三个值：`none`、`fine`和`coarse`。`fine`指针是类似于鼠标或者触控板的东西，它让用户可以精确指向一片小区域。`coarse`指针是你在触摸屏上的手指。`none`值意味着，用户没有指点设备，也许是他们正只使用键盘导航，或者是语音命令。

使用`pointer`可以在用户使用屏幕时进行交互时，帮你更好地设计响应这种交互的界面。例如，如果你知道用户正在用触摸屏设备交互的时候，你可以建立更大的响应区域。

### 更复杂的媒体查询

有了所有不同的可用的媒体查询，你可能想要把它们混合起来，或者建立查询列表——其中的任何一个都可以匹配生效。

#### 媒体查询中的“与”逻辑

为了混合媒体特征，你可以以与在上面使用`and`很相同的方式，用`and`来混合媒体类型和特征。例如，我们可能会想要测得`min-width`和`orientation`，而 body 的文字只会在视口至少为 400 像素宽，且设备横放时变为蓝色。

```css
@media screen and (min-width: 400px) and (orientation: landscape) {
    body {
        color: blue;
    }
}

```

#### 媒体查询中的“或”逻辑

如果你有一组查询，且要其中的任何一个都可以匹配的话，那么你可以使用逗号分开这些查询。在下面的示例中，文本会在视口至少为 400 像素宽的时候**或者**设备处于横放状态的时候变为蓝色。如果其中的任何一项成立，那么查询就匹配上了。

```css
@media screen and (min-width: 400px), screen and (orientation: landscape) {
    body {
        color: blue;
    }
}

```

#### 媒体查询中的“非”逻辑

你可以用`not`操作符让整个媒体查询失效。这就直接反转了整个媒体查询的含义。因而在下面的例子中，文本只会在朝向为竖着的时候变成蓝色。

```css
@media not all and (orientation: landscape) {
    body {
        color: blue;
    }
}

```

### 怎么选择断点

响应式设计的早期，许多设计者会尝试指向非常特定的屏幕尺寸。人们公布了流行的手机和平板的屏幕尺寸列表，以让设计者创建可以整齐地放在那些视口里面的设计。

现在有多得多的设备，以及多种多样的尺寸，让这种事变得不再可行。这也就是说，将所有的设计用在特定的尺寸上以外，一个更好的方法是在内容某种程度上开始变得混乱的时候，改变尺寸的设计。也许线太长了，或者盒子状的外侧栏开始挤在一起而难以阅读。那就是你想要使用媒体查询，将设计变得对剩余可用空间更加友好的时候。这种方式意味着，它无关使用的设备的确切大小，每个范围都被照顾到了。引入媒体查询的点就叫做**断点**。

火狐开发者工具中的[响应式设计模式](https://firefox-source-docs.mozilla.org/devtools-user/responsive_design_mode/index.html)能很好地帮助弄清楚断点应该设置在哪里。你能容易就能让视口变大和变小，然后看下可以在哪里加入媒体查询、调整设计，从而改善内容。

![A screenshot of a layout in a mobile view in Firefox DevTools.](rwd-mode.png)

### 主动学习：移动优先的响应式设计

泛泛地说，你可以采用两种方式实现响应式设计。你可以从桌面或者最宽的视图开始，然后随着视口变得越来越小，加上断点，把物件挪开；你也可以从最小的视图开始，随着视口变得越来越大，增添布局内容。第二种方式被叫做**移动优先**的响应式设计，很多时候是最值得仿效的做法。

用在最小的那个设备上的视图很多时候都是一个简单的单列内容，很像正常文本流显示的那样。这意味着，你很可能不需要为小设备做多少布局设计，合适地安排下你的源代码，默认情况下你就可以得到可读的布局。

下面的教程会领你用一个非常简单的布局熟悉这种方式。在生产站点上，你的媒体查询中可能会有更多的东西需要调整，但是它们的方法是完全一样的。

#### 教程：一个简单的移动优先布局

我们的起始点是一个 HTML 文档，上面应用了一些 CSS，为布局的各部分加入了背景颜色。

```css
* {
    box-sizing: border-box;
}

body {
    width: 90%;
    margin: 2em auto;
    font: 1em/1.3 Arial, Helvetica, sans-serif;
}

a:link,
a:visited {
    color: #333;
}

nav ul,
aside ul {
    list-style: none;
    padding: 0;
}

nav a:link,
nav a:visited {
    background-color: rgba(207, 232, 220, 0.2);
    border: 2px solid rgb(79, 185, 227);
    text-decoration: none;
    display: block;
    padding: 10px;
    color: #333;
    font-weight: bold;
}

nav a:hover {
    background-color: rgba(207, 232, 220, 0.7);
}

.related {
    background-color: rgba(79, 185, 227, 0.3);
    border: 1px solid rgb(79, 185, 227);
    padding: 10px;
}

.sidebar {
    background-color: rgba(207, 232, 220, 0.5);
    padding: 10px;
}

article {
    margin-bottom: 1em;
}

```

我们没有改变过任何布局，但是文件的源代码是以让内容可读的方式排列的。这个开头是重要的，也是能够确保内容在由屏幕阅读器读出来的时候，让其可以理解的一步。

```html
<body>
    <div class="wrapper">
      <header>
        <nav>
          <ul>
            <li><a href="">About</a></li>
            <li><a href="">Contact</a></li>
            <li><a href="">Meet the team</a></li>
            <li><a href="">Blog</a></li>
          </ul>
        </nav>
      </header>
      <main>
        <article>
          <div class="content">
            <h1>Veggies!</h1>
            <p>
              ...
            </p>
          </div>
          <aside class="related">
            <p>
              ...
            </p>
          </aside>
        </article>

        <aside class="sidebar">
          <h2>External vegetable-based links</h2>
          <ul>
            <li>
              ...
            </li>
          </ul>
        </aside>
      </main>

      <footer><p>&copy;2019</p></footer>
    </div>
  </body>

```

这个简单的布局在移动端上也能表现得很好。如果我们在开发者工具中的响应式设计模式里面查看这个布局的话，我们可以看到，它作为一个直截了当的站点移动版布局来说，表现得相当优秀。

![image-20220823140417504](image-20220823140417504.png)

从这里开始，脱拽响应式设计的窗口，让它变得变得更宽，直到你看到一行变得非常长，有足够空间把导航栏放在一个水平行里面。这是我们加入第一个媒体查询的地方。我们将会使用 em，因为这意味着，如果用户已经增加了文本的大小，断点会在行差不多也是这样长，但是视口更宽的时候产生；而文本更小的时候，视口也会更窄。

```css
@media screen and (min-width: 40em) {
    article {
        display: grid;
        grid-template-columns: 3fr 1fr;
        column-gap: 20px;
    }

    nav ul {
        display: flex;
    }

    nav li {
        flex: 1;
    }
}

```

![image-20220823140704539](image-20220823140704539.png)

让我们继续增加宽度，直到我们觉得这里有了足够多的空间来放置侧栏，再形成一列。在媒体查询中，我们会让 main 元素变成两栏网格。我们之后需要移除文章上的[`margin-bottom`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin-bottom)，让两个侧栏和彼此对齐，然后我们将会往页脚的顶部加上一个[`border`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border) 。一般来说，为了让设计看起来好看，这些小调整是你将会在每一个断点都需要做的。

```css
@media screen and (min-width: 70em) {
    main {
        display: grid;
        grid-template-columns: 3fr 1fr;
        column-gap: 20px;
    }

    article {
        margin-bottom: 0;
    }

    footer {
        border-top: 1px solid #ccc;
        margin-top: 2em;
    }
}

```

![image-20220823140849278](image-20220823140849278.png)

### 你真的需要媒体查询吗？

弹性盒、网格和多栏布局都给了你建立可伸缩的甚至是响应式组件的方式，而不需要媒体查询。这些布局方式能否在不加入媒体查询的时候实现你想要的设计，总是值得考虑的一件事。例如，你可能想要一组卡片，至少为二百像素宽，并在主文章里尽可能多地放下这些二百像素的卡片。这可以用网格布局实现，而完全不使用媒体查询。

这可以由以下代码实现：	

```html
<ul class="grid">
    <li>
        <h2>Card 1</h2>
        <p>...</p>
    </li>
    <li>
        <h2>Card 2</h2>
        <p>...</p>
    </li>
    <li>
        <h2>Card 3</h2>
        <p>...</p>
    </li>
    <li>
        <h2>Card 4</h2>
        <p>...</p>
    </li>
    <li>
        <h2>Card 5</h2>
        <p>...</p>
    </li>
</ul>

```

```css
.grid {
    list-style: none;
    margin: 0;
    padding: 0;
    display: grid;
    gap: 20px;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
}

.grid li {
    border: 1px solid #666;
    padding: 10px;
}

```

![image-20220823141132791](image-20220823141132791.png)

![image-20220823141146257](image-20220823141146257.png)

![image-20220823141159351](image-20220823141159351.png)

![image-20220823141215741](image-20220823141215741.png)



在你的浏览器里打开这个示例，让屏幕变宽变窄，看一看列轨数目的变化。这个方法里面的好事是，网格不是靠视口宽度判断的，而是可以容纳组件的宽度。对媒体查询这章节的建议就是，你可能根本不需要它！但是，实践中你会发现，由媒体查询改进的现代布局方式的恰当使用，将会产生最佳效果。

