---
title: 'Sass基础'
date: 2022-8-9 07:28:42
cover: false
tags:
- CSS预处理器
categories: CSS预处理器
typora-root-url: sass基础
---

[Sass常见问题 | Sass中文网](https://www.sass.hk/faq/)

[Sass: Syntactically Awesome Style Sheets (sass-lang.com)](https://sass-lang.com/)

# 基本概念

## 什么是`Sass/Scss`

[SCSS - 掘金 (juejin.cn)](https://juejin.cn/post/6945064165518082085)

`SCSS `是`Sass 3`引入新的语法，其语法完全兼容` CSS3`，并且继承了`Sass`的强大功能。

`Sass` 和`SCSS`其实是同一种东西，我们平时都称之为 Sass，两者之间不同之处有以下两点：

- `文件扩展名不同`，Sass 是以“`.sass`”后缀为扩展名，而 SCSS 是以“`.scss`”后缀为扩展名

- `语法书写方式不同`，`Sass `是以严格的`缩进式语法规则`来书写，`不带大括号({})和分号(;)`，而 `SCSS` 的语法书写和我们的` CSS 语法`书写方式非常类似。

`SASS`版本`3.0`之前的后缀名为`.sass`，而版本`3.0`之后的后缀名`.scss`。

Sass 支持两种不同的语法。两种语法可以互相加载。

## 什么是`Ruby-sass`?

[继往开来的 sass 三代编译器：ruby sass、node-sass、dart-sass - 掘金 (juejin.cn)](https://juejin.cn/post/7052193042752602148)

sass 最早是 2006 年由 ruby 开发的，作为和它 web 框架的模版引擎 haml 配套的编写 css 的语言。因为比较好用，所以前端也都在用。

sass 编译器是用 ruby 开发的，而 ruby 是一门解释型语言，所以前端开发想编译 sass 就需要在本地安装 ruby。

后来，Node.js 的出现推动了前端工程化的发展，也就是用 Node.js 来写前端用的编译打包等工具链。而 Node.js 只支持 c++ 这种编译型语言的扩展包，ruby sass 就用不了了，所以出现了 node-sass。

直到 2019 年 3 月，ruby sass 宣布不再维护，sass 最早的编译器退出历史舞台。

[Sass: Ruby Sass (sass-lang.com)](https://sass-lang.com/ruby-sass)

> Ruby Sass was the original implementation of Sass, but it reached its end of life as of 26 March 2019. It's no longer supported, and Ruby Sass users should migrate to another implementation.

## 什么是`Node-sass`？

[你还在为node-sass烦恼吗？快试试官方推荐的dart-sass - 掘金 (juejin.cn)](https://juejin.cn/post/6966763785130508296)

> Node-sass is a library that **provides binding for Node.js to LibSass**, the C++ version of the popular stylesheet preprocessor, Sass.
>
> It allows you to natively **compile .scss files to css at incredible speed and automatically via a connect middleware**.

从上面的介绍可以知道，node-sass 是一个 nodejs 环境下提供的一个 Bridge，它提供了调用 LibSass 的能力（而 LibSass 是一个 C++ 实现的样式预处理器）。

> ps: 可以看到，node-sass 并不完全是 javascript 实现的，而是借助了 C++ 的能力，毕竟编译型语言还是速度快啊。
>
> 运行时可能会有环境上的各种问题



[vue-cli 3中dart-sass替换node-sass - 掘金 (juejin.cn)](https://juejin.cn/post/6844904180948140045)

如果你使用过 sass ，应该了解多年来 node-sass 一直是 JavaScript 社区里的主流选择，它实际上只是 libsass 在 node 环境下的一个 wrapper， 编译 sass 文件的实际工作是 libsass 完成的。

在使用 node-sass 过程中遇到的很多问题实际上也是 libsass 引发的，libsass 是用 C/C++ 实现的，常见的问题是，在安装 node-sass 的过程中经常会出现安装失败的情况，又或者切换了 Node.js 版本发现 node-sass 需要重新安装才能用，如果你在 docker 中安装 node-sass 还会遇到由于缺少各种依赖导致 node-sass build 失败的情况，又或者在国内由于网络原因导致 node-sass 需要的二进制文件下载不下来而 build 失败。

现在，sass 官方已经使用 dart-sass 作为 sass 的主要实现：

> Dart Sass is the primary implementation of Sass, which means it gets new features before any other implementation. It's fast, easy to install, and it compiles to pure JavaScript which makes it easy to integrate into modern web development workflows.



[继往开来的 sass 三代编译器：ruby sass、node-sass、dart-sass - 掘金 (juejin.cn)](https://juejin.cn/post/7052193042752602148)

社区里用 c++ 实现了 sass 的编译器，叫做 LibSass，和 node 做了集成，就是 node-sass 这个包。

当然，它同样也可以和别的语言集成，比如 go、java 等。

node-sass 让我们可以在 Node.js 里通过 api 来编译 sass 代码，顺应了前端工程化的大潮流。

而且 node-sass 是用 c++ 写的，编译速度比 ruby sass 快很多。

只不过，node-sass 因为是一个 c++ 模块，所以安装的时候要和 node 版本对应，不然就会编译报错，这点比较麻烦。

在 github 可以查到 node 和 node-sass 的版本对应关系：

![image-20230104105830319](image-20230104105830319.png)

node-sass 看起来挺不错，编译速度快，支持 Node.js 调用。虽然要注意下和 node 版本的对应关系，但问题不大。

但是，node-sass 已经被标记为过时了，这意味着它也会慢慢退出历史舞台。

为什么呢？

主要是因为维护速度跟不上了。

就像 TS 是 JS 的超集一样，SASS 也是 CSS 的超集。超集意味着 TS Compiler 要支持 JS 的各种新语法，SASS 也要支持 CSS 的各种新语法，在这个基础上再迭代自己添加的那些语法。

SASS 团队的两个主要维护者感觉自己支持 CSS 新特性的速度跟不上了，而且社区出现了 dart-sass 这个对 css 新特性支持更好的 sass 编译器，随着时间的推移，CSS 新特性支持上差距越来越大。最终，在 2020 年 10 月份，node-sass 宣布了不再继续支持新特性，标记为了过时，推荐使用 dart-sass。

在 node-sass 博客上有这样一段话，展示了他们的无奈：

> 经过 Sass 核心团队的多次讨论，我们得出的结论是，是时候正式宣布 LibSass 和基于它构建的包（包括 Node Sass）已被弃用。几年来，很明显 LibSass 背后根本没有足够的工程带宽来使其与 Sass 语言的最新发展保持同步（例如，最新的新语言功能是在[2018 年 11 月](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Fsass%2Flibsass%2Freleases%2Ftag%2F3.5.5)添加的）。尽管我们希望看到这种模式发生转变，但即使是长期 LibSass 贡献者 Michael Mifsud 和 Marcel Greter 的出色工作也无法跟上CSS和 Sass语言开发的快速步伐。

就这样，node-sass 也算是推出了历史舞台，但是它对前端工程化的贡献是不可磨灭的。

我们再来看下 sass 编译器的继任者： dart-sass。

## 什么是`Dart-sass`?

Dart Sass 是 Sass 官网力推的工具，它包括了基于 Dart VM 的命令行工具，以及基于 Node 的纯 Javascript 实现。前者说的 Dart VM 就是现在很火的 Flutter 选择的编程语言 Dart 的虚拟机；而后者的出现是为了能快速与 Node 环境下现有的工作流集成，比如 webpack，gulp等。

Dart Sass的命令行工具是比 Javascript Library性能更好的，但是为了快速对接 webpack 等工具，我们目前一般通过`npm install --save-dev sass`直接使用 sass 的 Javascript Library。

改用 Dart Sass 后，不管是安装还是兼容高版本 Node 这块，都没有什么问题，总的来说，使用体验还是非常棒！

> Dart Sass 是我们对它的习惯称呼，最早它在 npm 上的确是以 dart-sass 的名字发布的，不过现在它已经更名为 sass 了。



[继往开来的 sass 三代编译器：ruby sass、node-sass、dart-sass - 掘金 (juejin.cn)](https://juejin.cn/post/7052193042752602148)

dart-sass 毫无疑问是用 dart 来写的 sass 编译器。dart 是 flutter 的编程语言，可以编译为 js，所以它提供的 npm 是 js 的，不需要像 node-sass 一样和 node 版本有绑定关系。

下载后的 npm 包可以看到 一个 sass.dart.js，这个就是用 dart 编译出来的：

![img](d43a76595a8a4ccfaf1d0d85e33afe83tplv-k3u1fbpfcp-zoom-in-crop-mark4536000.image)

因为 dart-sass 的 npm 包的编译是用 js 做的，速度上会比 node-sass 慢，但是它主要胜在对 css 的特性支持的全，而且因为是 js 包，安装很方便。

dart-sass 代表着未来，也是被官方推荐的 sass 编译器。

## 小结

介绍完了三代编译器，我们来简单做下回顾：

ruby sass 是最早的 sass 编译器，用 ruby 写的，所以不能被 node 调用，但是它是开创者，历史功绩列第一位。只是需要安装 ruby 来执行，比较麻烦。

node-sass 是顺应前端工程化潮流而出现的 node 包，是对用 c++ 实现的 sass 编译器 LibSass 的封装。因为用 c++ 编译，所以速度更快。提供了 Node.js 的 api，支撑了前端工程化的大潮流。历史功绩列第二位。只是需要 node-sass 和 node 版本的对应比较麻烦。

dart-sass 是用 dart 实现的 sass 编译器，提供的 dart-sass 的包是 js 的，由 dart 编译而来。好处是对 css 新特性支持的更全，而且也没有和 node 版本的绑定关系。

ruby sass 和 node-sass 都已经是历史，dart-sass 是 sass 编译器的未来。



css 缺少代码组织能力和动态计算能力，所以社区出现了一些 css 预处理器：sass、less、stylus。

less、stylus 的编译器都是 js 写的，最特殊的是 sass，它的三代编译器分别是 ruby、c++、dart 写的，都不是 js。（这点在工程化领域也很特殊，js 的编译器都是从 js 逐步发展到 rust、go 等别的语言，而 sass 的编译器是从别的语言慢慢切回到了编译成 js 的语言）

ruby sass、node-sass 都已经过时了，但是它们对前端工程化的贡献不可磨灭，dart-sass 代表着 sass 编译器的未来，希望它能接过前辈们的接力棒，继往开来，做的更好吧。



# 安装

## npm安装

https://blog.csdn.net/weixin_37818738/article/details/126078436

```bash
npm init -y
npm i sass
npx sass --version
```

首先要在项目目录中有两个文件夹, 一个是 scss ,一个是css. scss文件夹中存放sass文件, css文件夹中存放编译过后生成的css文件.

```bash
npx sass scss/index.scss:css/index.css
```

监听scss文件夹

```bash
npx sass -w scss:css
```

添加到`package.json`中

```json
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "sass": "npx sass -w scss:css"
  },
```

通过`npm run scss`启动监听

## vscode插件

### live sass compiler

[live sass compiler-vscode插件将scss编译为css - ZerlinM - 博客园 (cnblogs.com)](https://www.cnblogs.com/ZerlinM/p/13632254.html)

先安装两个插件，live server和 live sass compiler两个插件

然后将下面的代码复制到设置（文件---首选项----设置----打开设置json）中

```json
  "liveSassCompile.settings.formats": [
    {
      "format": "expanded",
      "extensionName": ".css",
      "savePath": "~/../css/"
    }
  ],
  "liveSassCompile.settings.excludeList": ["**/node_modules/**", ".vscode/**"],
  "liveSassCompile.settings.generateMap": false
```

这你的项目文件夹中创建一个css文件夹，

然后在vscode里点击它（如图所示）就可以监听你项目里的scss后缀的文件，

![image-20230104153241750](image-20230104153241750.png)

并自动编译成.css的文件存放在你创建的css文件夹里。

缺点：当前工作区所有的sass文件都会编译，且速度较慢

### easy scss

[小程序vscode scss自动编译插件 - 简书 (jianshu.com)](https://www.jianshu.com/p/b0f65a090215)

# 基本使用

[Sass基础教程 Sass快速入门 Sass中文手册 | Sass中文网](https://www.sass.hk/guide/)

[SCSS - 掘金 (juejin.cn)](https://juejin.cn/post/6945064165518082085#heading-25)

## 变量

`sass`使用`$`符号来标识变量

```scss
$highlight-color: #F90;
```

变量可以在`css`规则块定义之外存在。当变量定义在`css`规则块内，那么该变量只能在此规则块内使用。

```scss
$nav-color: #F90;
nav {
  $width: 100px;
  width: $width;
  color: $nav-color;
}

//编译后

nav {
  width: 100px;
  color: #F90;
}
```

`sass`的变量名可以与`css`中的属性名和选择器名称相同，包括中划线和下划线。这完全取决于个人的喜好，有些人喜欢使用中划线来分隔变量中的多个词（如`$highlight-color`），而有些人喜欢使用下划线（如`$highlight_color`）。使用中划线的方式更为普遍，这也是`compass`和本文都用的方式。

不过，`sass`并不想强迫任何人一定使用中划线或下划线，所以这两种用法相互兼容。用中划线声明的变量可以使用下划线的方式引用，反之亦然。这意味着即使`compass`选择用中划线的命名方式，这并不影响你在使用`compass`的样式中用下划线的命名方式进行引用：

```scss
$link-color: blue;
a {
  color: $link_color;
}

//编译后

a {
  color: blue;
}
```

在上例中，`$link-color`和`$link_color`其实指向的是同一个变量。实际上，在`sass`的大 多数地方，中划线命名的内容和下划线命名的内容是互通的，除了变量，也包括对混合器和Sass函数的命名。但是在`sass`中纯`css`部分不互通，比如类名、ID或属性名。

尽管变量自身提供了很多有用的地方，但是`sass`基于变量提供的更为强大的工具才是我们关注的焦点。只有当变量与`sass`的其他特性一起使用时，才能发挥其全部的潜能。接下来，我们将探讨其中一个非常重要的特性，即规则嵌套。

## 嵌套规则

```scss
#content {
  article {
    h1 { color: #333 }
    p { margin-bottom: 1.4em }
  }
  aside { background-color: #EEE }
}
```

### 父选择器的标识符&

一般情况下，`sass`在解开一个嵌套规则时就会把父选择器（`#content`）通过一个空格连接到子选择器的前边（`article`和`aside`）形成（`#content article`和`#content aside`）。这种在CSS里边被称为后代选择器，因为它选择ID为`content`的元素内所有命中选择器`article`和`aside`的元素。但在有些情况下你却不会希望`sass`使用这种后代选择器的方式生成这种连接。

最常见的一种情况是当你为链接之类的元素写`：hover`这种伪类时，你并不希望以后代选择器的方式连接。

```scss
article a {
  color: blue;
  &:hover { color: red }
}
```

编译结果

```css
article a {
  color: blue;
}
article a:hover {
  color: red;
}

```

### 群组选择器的嵌套

当`sass`解开一个群组选择器规则内嵌的规则时，它会把每一个内嵌选择器的规则都正确地解出来：

```scss
.container {
  h1, h2, h3 {margin-bottom: .8em}
}

// 编译结果
.container h1, .container h2, .container h3 {
  margin-bottom: 0.8em;
}
```

对于内嵌在群组选择器内的嵌 套规则，处理方式也一样：

```scss
nav, aside {
  a {color: blue}
}

// 编译结果
nav a, aside a {
  color: blue;
}

```

有利必有弊，你需要特别注意群组选择器的规则嵌套生成的`css`。虽然`sass`让你的样式表看上去很小，但实际生成的`css`却可能非常大，这会降低网站的速度。

### 子组合选择器和同层组合选择器：>、+和~

上边这三个组合选择器必须和其他选择器配合使用，以指定浏览器仅选择某种特定上下文中的元素。

```scss
article {
  ~ article {
    border-top: 1px dashed #ccc;
  }
  > section {
    background: #eee;
  }
  dl > {
    dt {
      color: #333;
    }
    dd {
      color: #555;
    }
  }
  nav + & {
    margin-top: 0;
  }
}


// 编译结果
article ~ article {
  border-top: 1px dashed #ccc;
}
article > section {
  background: #eee;
}
article dl > dt {
  color: #333;
}
article dl > dd {
  color: #555;
}
nav + article {
  margin-top: 0;
}
```

### 嵌套属性

在`sass`中，除了CSS选择器，属性也可以进行嵌套。尽管编写属性涉及的重复不像编写选择器那么糟糕，但是要反复写`border-style``border-width``border-color`以及`border-*`等也是非常烦人的。在`sass`中，你只需敲写一遍`border`：

```scss
nav {
  border: {
  style: solid;
  width: 1px;
  color: #ccc;
  }
}
```

嵌套属性的规则是这样的：把属性名从中划线-的地方断开，在根属性后边添加一个冒号:，紧跟一个`{ }`块，把子属性部分写在这个`{ }`块中。就像`css`选择器嵌套一样，`sass`会把你的子属性一一解开，把根属性和子属性部分通过中划线-连接起来，最后生成的效果与你手动一遍遍写的`css`样式一样，上述写法编译结果如下：

```scss
nav {
  border-style: solid;
  border-width: 1px;
  border-color: #ccc;
}
```

对于属性的缩写形式，你甚至可以像下边这样来嵌套，指明例外规则：

```scss
nav {
  border: 1px solid #ccc {
    left: 0px;
    right: 0px;
  }
}
```

这比下边这种同等样式的写法要好：

```scss
nav {
  border: 1px solid #ccc;
  border-left: 0px;
  border-right: 0px;
}
```

属性和选择器嵌套是非常伟大的特性，因为它们不仅大大减少了你的编写量，而且通过视觉上的缩进使你编写的样式结构更加清晰，更易于阅读和开发。

即便如此，随着你的样式表变得越来越大，这种写法也很难保持结构清晰。有时，处理这种大量样式的唯一方法就是把它们分拆到多个文件中。`sass`通过对`css`原有`@import`规则的改进直接支持了这一特性。

## 导入SASS文件

`css`有一个特性，即`@import`规则，它允许在一个`css`文件中导入其他`css`文件。然而，后果是只有执行到`@import`时，浏览器才会去下载其他`css`文件，这导致页面加载起来特别慢。

`sass`也有一个`@import`规则，但不同的是，`sass`的`@import`规则在生成`css`文件时就把相关文件导入进来。这意味着所有相关的样式被归纳到了同一个`css`文件中，而无需发起额外的下载请求。另外，所有在被导入文件中定义的变量和混合器（参见2.5节）均可在导入文件中使用。

使用`sass`的`@import`规则并不需要指明被导入文件的全名。你可以省略`.sass`或`.scss`文件后缀（见下图）。这样，在不修改样式表的前提下，你完全可以随意修改你或别人写的被导入的`sass`样式文件语法，在`sass`和`scss`语法之间随意切换。举例来说，`@import "sidebar";`这条命令将把`sidebar.scss`文件中所有样式添加到当前样式表中。

![img](p1.png)

本节将介绍如何使用`sass`的`@import`来处理多个`sass`文件。

首先，我们将学习编写那些被导入的`sass`文件，因为在一个大型`sass`项目中，这样的文件是你最常编写的那一类。

接着，了解集中导入`sass`文件的方法，使你的样式可重用性更高，包括声明可自定义的变量值，以及在某一个选择器范围内导入`sass`文件。

最后，介绍如何在`sass`中使用`css`原生的`@import`命令。



通常，有些`sass`文件用于导入，你并不希望为每个这样的文件单独地生成一个`css`文件。对此，`sass`用一个特殊的约定来解决。

### 使用SASS部分文件

当通过`@import`把`sass`样式分散到多个文件时，你通常只想生成少数几个`css`文件。那些专门为`@import`命令而编写的`sass`文件，并不需要生成对应的独立`css`文件，这样的`sass`文件称为局部文件。对此，`sass`有一个特殊的约定来命名这些文件。

此约定即，`sass`局部文件的文件名以下划线开头。这样，`sass`就不会在编译时单独编译这个文件输出`css`，而只把这个文件用作导入。当你`@import`一个局部文件时，还可以不写文件的全名，即省略文件名开头的下划线。

举例来说，你想导入`themes/_night-sky.scss`这个局部文件里的变量，你只需在样式表中写`@import` `"themes/night-sky";`。

局部文件可以被多个不同的文件引用。当一些样式需要在多个页面甚至多个项目中使用时，这非常有用。在这种情况下，有时需要在你的样式表中对导入的样式稍作修改，`sass`有一个功能刚好可以解决这个问题，即默认变量值。

### 默认变量值

一般情况下，你反复声明一个变量，只有最后一处声明有效且它会覆盖前边的值。举例说明：

```scss
$link-color: blue;
$link-color: red;
a {
color: $link-color;
}
```

在上边的例子中，超链接的`color`会被设置为`red`。这可能并不是你想要的结果，假如你写了一个可被他人通过`@import`导入的`sass`库文件，你可能希望导入者可以定制修改`sass`库文件中的某些值。使用`sass`的`!default`标签可以实现这个目的。

它很像`css`属性中`!important`标签的对立面，不同的是`!default`用于变量，含义是：如果这个变量被声明赋值了，那就用它声明的值，否则就用这个默认值。

```scss
$fancybox-width: 400px !default;
.fancybox {
width: $fancybox-width;
}
```

在上例中，如果用户在导入你的`sass`局部文件之前声明了一个`$fancybox-width`变量，那么你的局部文件中对`$fancybox-width`赋值`400px`的操作就无效。如果用户没有做这样的声明，则`$fancybox-width`将默认为`400px`。

接下来我们将学习嵌套导入，它允许只在某一个选择器的范围内导入`sass`局部文件。

### 嵌套导入

跟原生的`css`不同，`sass`允许`@import`命令写在`css`规则内。这种导入方式下，生成对应的`css`文件时，局部文件会被直接插入到`css`规则内导入它的地方。举例说明，有一个名为`_blue-theme.scss`的局部文件，内容如下：

```scss
aside {
  background: blue;
  color: white;
}
```

然后把它导入到一个CSS规则内，如下所示：

```scss
.blue-theme {@import "blue-theme"}

//生成的结果跟你直接在.blue-theme选择器内写_blue-theme.scss文件的内容完全一样。

.blue-theme {
  aside {
    background: blue;
    color: #fff;
  }
}
```

被导入的局部文件中定义的所有变量和混合器，也会在这个规则范围内生效。这些变量和混合器不会全局有效，这样我们就可以通过嵌套导入只对站点中某一特定区域运用某种颜色主题或其他通过变量配置的样式。

有时，可用`css`原生的`@import`机制，在浏览器中下载必需的`css`文件。`sass`也提供了几种方法来达成这种需求。

### 原生的CSS导入

由于`sass`兼容原生的`css`，所以它也支持原生的`CSS@import`。尽管通常在`sass`中使用`@import`时，`sass`会尝试找到对应的`sass`文件并导入进来，但在下列三种情况下会生成原生的`CSS@import`，尽管这会造成浏览器解析`css`时的额外下载：

- 被导入文件的名字以`.css`结尾；
- 被导入文件的名字是一个URL地址（比如http://www.sass.hk/css/css.css），由此可用谷歌字体API提供的相应服务；
- 被导入文件的名字是`CSS`的url()值。

这就是说，你不能用`sass`的`@import`直接导入一个原始的`css`文件，因为`sass`会认为你想用`css`原生的`@import`。但是，因为`sass`的语法完全兼容`css`，所以你可以把原始的`css`文件改名为`.scss`后缀，即可直接导入了。

文件导入是保证`sass`的代码可维护性和可读性的重要一环。次之但亦非常重要的就是注释了。注释可以帮助样式作者记录写`sass`的过程中的想法。在原生的`css`中，注释对于其他人是直接可见的，但`sass`提供了一种方式可在生成的`css`文件中按需抹掉相应的注释。

## 静默注释

`css`中注释的作用包括帮助你组织样式、以后你看自己的代码时明白为什么这样写，以及简单的样式说明。但是，你并不希望每个浏览网站源码的人都能看到所有注释。

`sass`另外提供了一种不同于`css`标准注释格式`/* ... */`的注释语法，即静默注释，其内容不会出现在生成的`css`文件中。静默注释的语法跟`JavaScript``Java`等类`C`的语言中单行注释的语法相同，它们以`//`开头，注释内容直到行末。

```scss
body {
  color: #333; // 这种注释内容不会出现在生成的css文件中
  padding: 0; /* 这种注释内容会出现在生成的css文件中 */
}
```

实际上，`css`的标准注释格式`/* ... */`内的注释内容亦可在生成的`css`文件中抹去。当注释出现在原生`css`不允许的地方，如在`css`属性或选择器中，`sass`将不知如何将其生成到对应`css`文件中的相应位置，于是这些注释被抹掉。

```scss
body {
  color /* 这块注释内容不会出现在生成的css中 */: #333;
  padding: 1; /* 这块注释内容也不会出现在生成的css中 */ 0;
}
```

你已经掌握了`sass`的静默注释，了解了保持`sass`条理性和可读性的最基本的三个方法：嵌套、导入和注释。现在，我们要进一步学习新特性，这样我们不但能保持条理性还能写出更好的样式。首先要介绍的内容是：使用混合器抽象你的相关样式。

## 混合器

### 混合的定义与使用

如果你的整个网站中有几处小小的样式类似（例如一致的颜色和字体），那么使用变量来统一处理这种情况是非常不错的选择。但是当你的样式变得越来越复杂，你需要大段大段的重用样式的代码，独立的变量就没办法应付这种情况了。你可以通过`sass`的混合器实现大段样式的重用。

混合器使用`@mixin`标识符定义。看上去很像其他的`CSS @`标识符，比如说`@media`或者`@font-face`。这个标识符给一大段样式赋予一个名字，这样你就可以轻易地通过引用这个名字重用这段样式。下边的这段`sass`代码，定义了一个非常简单的混合器，目的是添加跨浏览器的圆角边框。

```scss
@mixin rounded-corners {
  -moz-border-radius: 5px;
  -webkit-border-radius: 5px;
  border-radius: 5px;
}
```

然后就可以在你的样式表中通过`@include`来使用这个混合器，放在你希望的任何地方。`@include`调用会把混合器中的所有样式提取出来放在`@include`被调用的地方。如果像下边这样写：

```scss
notice {
  background-color: green;
  border: 2px solid #00aa00;
  @include rounded-corners;
}

//sass最终生成：
.notice {
  background-color: green;
  border: 2px solid #00aa00;
  -moz-border-radius: 5px;
  -webkit-border-radius: 5px;
  border-radius: 5px;
}
```

在`.notice`中的属性`border-radius``-moz-border-radius`和`-webkit-border-radius`全部来自`rounded-corners`这个混合器。这一节将介绍使用混合器来避免重复。通过使用参数，你可以使用混合器把你样式中的通用样式抽离出来，然后轻松地在其他地方重用。实际上，混合器太好用了，一不小心你可能会过度使用。大量的重用可能会导致生成的样式表过大，导致加载缓慢。所以，首先我们将讨论混合器的使用场景，避免滥用。

### 何时使用混合器

利用混合器，可以很容易地在样式表的不同地方共享样式。如果你发现自己在不停地重复一段样式，那就应该把这段样式构造成优良的混合器，尤其是这段样式本身就是一个逻辑单元，比如说是一组放在一起有意义的属性。

判断一组属性是否应该组合成一个混合器，一条经验法则就是你能否为这个混合器想出一个好的名字。如果你能找到一个很好的短名字来描述这些属性修饰的样式，比如`rounded-corners``fancy-font`或者`no-bullets`，那么往往能够构造一个合适的混合器。如果你找不到，这时候构造一个混合器可能并不合适。

混合器在某些方面跟`css`类很像。都是让你给一大段样式命名，所以在选择使用哪个的时候可能会产生疑惑。最重要的区别就是类名是在`html`文件中应用的，而混合器是在样式表中应用的。这就意味着类名具有语义化含义，而不仅仅是一种展示性的描述：用来描述`html`元素的含义而不是`html`元素的外观。而另一方面，混合器是展示性的描述，用来描述一条`css`规则应用之后会产生怎样的效果。

在之前的例子中，`.notice`是一个有语义的类名。如果一个`html`元素有一个`notice`的类名，就表明了这个`html`元素的用途：向用户展示提醒信息。`rounded-corners`混合器是展示性的，它描述了包含它的`css`规则最终的视觉样式，尤其是边框角的视觉样式。混合器和类配合使用写出整洁的`html`和`css`，因为使用语义化的类名亦可以帮你避免重复使用混合器。为了保持你的`html`和`css`的易读性和可维护性，在写样式的过程中一定要铭记二者的区别。

有时候仅仅把属性放在混合器中还远远不够，可喜的是，`sass`同样允许你把`css`规则放在混合器中。

### 混合器中的CSS规则

混合器中不仅可以包含属性，也可以包含`css`规则，包含选择器和选择器中的属性，如下代码:

```scss
@mixin no-bullets {
  list-style: none;
  li {
    list-style-image: none;
    list-style-type: none;
    margin-left: 0px;
  }
}
```

当一个包含`css`规则的混合器通过`@include`包含在一个父规则中时，在混合器中的规则最终会生成父规则中的嵌套规则。举个例子，看看下边的`sass`代码，这个例子中使用了`no-bullets`这个混合器：

```scss
ul.plain {
  color: #444;
  @include no-bullets;
}
```

`sass`的`@include`指令会将引入混合器的那行代码替换成混合器里边的内容。最终，上边的例子如下代码:

```scss
ul.plain {
  color: #444;
  list-style: none;
}
ul.plain li {
  list-style-image: none;
  list-style-type: none;
  margin-left: 0px;
}
```

混合器中的规则甚至可以使用`sass`的父选择器标识符`&`。使用起来跟不用混合器时一样，`sass`解开嵌套规则时，用父规则中的选择器替代`&`。

如果一个混合器只包含`css`规则，不包含属性，那么这个混合器就可以在文档的顶部调用，写在所有的`css`规则之外。如果你只是为自己写一些混合器，这并没有什么大的用途，但是当你使用一个类似于`Compass`的库时，你会发现，这是提供样式的好方法，原因在于你可以选择是否使用这些样式。

接下来你将学习如何通过给混合器传参数来让混合器变得更加灵活和可重用。

### 给混合器传参

混合器并不一定总得生成相同的样式。可以通过在`@include`混合器时给混合器传参，来定制混合器生成的精确样式。当`@include`混合器时，参数其实就是可以赋值给`css`属性值的变量。如果你写过`JavaScript`，这种方式跟`JavaScript`的`function`很像：

```scss
@mixin link-colors($normal, $hover, $visited) {
  color: $normal;
  &:hover { color: $hover; }
  &:visited { color: $visited; }
}
```

当混合器被`@include`时，你可以把它当作一个`css`函数来传参。如果你像下边这样写：

```scss
a {
  @include link-colors(blue, red, green);
}

//Sass最终生成的是：

a { color: blue; }
a:hover { color: red; }
a:visited { color: green; }
```

当你@include混合器时，有时候可能会很难区分每个参数是什么意思，参数之间是一个什么样的顺序。为了解决这个问题，`sass`允许通过语法`$name: value`的形式指定每个参数的值。这种形式的传参，参数顺序就不必再在乎了，只需要保证没有漏掉参数即可：

```scss
a {
    @include link-colors(
      $normal: blue,
      $visited: green,
      $hover: red
  );
}
```

尽管给混合器加参数来实现定制很好，但是有时有些参数我们没有定制的需要，这时候也需要赋值一个变量就变成很痛苦的事情了。所以`sass`允许混合器声明时给参数赋默认值。

### 默认参数值

为了在`@include`混合器时不必传入所有的参数，我们可以给参数指定一个默认值。参数默认值使用`$name: default-value`的声明形式，默认值可以是任何有效的`css`属性值，甚至是其他参数的引用，如下代码：

```scss
@mixin link-colors(
    $normal,
    $hover: $normal,
    $visited: $normal
  )
{
  color: $normal;
  &:hover { color: $hover; }
  &:visited { color: $visited; }
}
```

如果像下边这样调用：`@include link-colors(red)` `$hover`和`$visited`也会被自动赋值为`red`。

混合器只是`sass`样式重用特性中的一个。我们已经了解到混合器主要用于样式展示层的重用，如果你想重用语义化的类呢？这就涉及`sass`的另一个重要的重用特性：选择器继承。

## 选择器继承

### 使用选择器继承来精简CSS

使用`sass`的时候，最后一个减少重复的主要特性就是选择器继承。基于`Nicole Sullivan`面向对象的`css`的理念，选择器继承是说一个选择器可以继承为另一个选择器定义的所有样式。这个通过`@extend`语法实现，如下代码:

```scss
//通过选择器继承继承样式
.error {
  border: 1px solid red;
  background-color: #fdd;
}
.seriousError {
  @extend .error;
  border-width: 3px;
}

// 编译结果：
.error, .seriousError {
  border: 1px solid red;
  background-color: #fdd;
}

.seriousError {
  border-width: 3px;
}

```

在上边的代码中，`.seriousError`将会继承样式表中任何位置处为`.error`定义的所有样式。以`class="seriousError"` 修饰的`html`元素最终的展示效果**就好像**是`class="seriousError error"`。相关元素不仅会拥有一个`3px`宽的边框，而且这个边框将变成红色的，这个元素同时还会有一个浅红色的背景，因为这些都是在`.error`里边定义的样式。

`.seriousError`不仅会继承`.error`自身的所有样式，任何跟`.error`有关的组合选择器样式也会被`.seriousError`以组合选择器的形式继承，如下代码:

```scss
//.seriousError从.error继承样式
.error a{  //应用到.seriousError a
  color: red;
  font-weight: 100;
}
h1.error { //应用到hl.seriousError
  font-size: 1.2rem;
}
```

如上所示，在`class="seriousError"`的`html`元素内的超链接也会变成红色和粗体。

本节将介绍与混合器相比，哪种情况下更适合用继承。接下来在探索继承的工作细节之前，我们先了解一下继承的高级用法。最后，我们将看看使用继承可能会有哪些坑，学习如何避免这些坑。

### 何时使用继承

上文中介绍了[混合器](https://www.sass.hk/guide/)主要用于展示性样式的重用，而类名用于语义化样式的重用。因为继承是基于类的（有时是基于其他类型的选择器），所以继承应该是建立在语义化的关系上。当一个元素拥有的类（比如说`.seriousError`）表明它属于另一个类（比如说`.error`），这时使用继承再合适不过了。

这有点抽象，所以我们从几个方面来阐释一下。想象一下你正在编写一个页面，给`html`元素添加类名，你发现你的某个类（比如说`.seriousError`）另一个类（比如说`.error`）的细化。你会怎么做？

- 你可以为这两个类分别写相同的样式，但是如果有大量的重复怎么办？使用`sass`时，我们提倡的就是不要做重复的工作。
- 你可以使用一个选择器组（比如说`.error .seriousError`）给这两个选择器写相同的样式。如果.error的所有样式都在同一个地方，这种做法很好，但是如果是分散在样式表的不同地方呢？再这样做就困难多了。
- 你可以使用一个混合器为这两个类提供相同的样式，但当`.error`的样式修饰遍布样式表中各处时，这种做法面临着跟使用选择器组一样的问题。这两个类也不是恰好有相同的样式。你应该更清晰地表达这种关系。
- 综上所述你应该使用`@extend`。让`.seriousError`从`.error`继承样式，使两者之间的关系非常清晰。更重要的是无论你在样式表的哪里使用`.error .seriousError`都会继承其中的样式。

现在你已经更好地掌握了何时使用继承，以及继承有哪些突出的优点，接下来我们看看一些高级用法。

### 继承的高级用法

任何`css`规则都可以继承其他规则，几乎任何`css`规则也都可以被继承。大多数情况你可能只想对类使用继承，但是有些场合你可能想做得更多。最常用的一种高级用法是继承一个`html`元素的样式。尽管默认的浏览器样式不会被继承，因为它们不属于样式表中的样式，但是你对`html`元素添加的所有样式都会被继承。

接下来的这段代码定义了一个名为`disabled`的类，样式修饰使它看上去像一个灰掉的超链接。通过继承a这一超链接元素来实现：

```scss
.disabled {
  color: gray;
  @extend a;
}
```

假如一条样式规则继承了一个复杂的选择器，那么它只会继承这个复杂选择器命中的元素所应用的样式。举例来说， 如果`.seriousError @extend .important.error` ， 那么`.important.error` 和`h1.important.error` 的样式都会被`.seriousError`继承， 但是`.important`或者`.error下`的样式则不会被继承。这种情况下你很可能希望`.seriousError`能够分别继承`.important`或者`.error`下的样式。

如果一个选择器序列（`#main .seriousError`）`@extend`另一个选择器（`.error`），那么只有完全匹配`#main .seriousError`这个选择器的元素才会继承`.error`的样式，就像单个类名继承那样。拥有`class="seriousError"`的`#main`元素之外的元素不会受到影响。

像`#main .error`这种选择器序列是不能被继承的。这是因为从`#main .error`中继承的样式一般情况下会跟直接从`.error`中继承的样式基本一致，细微的区别往往使人迷惑。

现在你已经了解了通过继承能够做些什么事情，接下来我们将学习继承的工作细节，在生成对应`css`的时候，`sass`具体干了些什么事情。

### 继承的工作细节

跟变量和混合器不同，继承不是仅仅用`css`样式替换@extend处的代码那么简单。为了不让你对生成的`css`感觉奇怪，对这背后的工作原理有一定了解是非常重要的。

`@extend`背后最基本的想法是，如果`.seriousError @extend .error`， 那么样式表中的任何一处`.error`都用`.error .seriousError`这一选择器组进行替换。这就意味着相关样式会如预期那样应用到`.error`和`.seriousError`。当`.error`出现在复杂的选择器中，比如说`h1.error .error a`或者`#main .sidebar input.error[type="text"]`，那情况就变得复杂多了，但是不用担心，`sass`已经为你考虑到了这些。

关于`@extend`有两个要点你应该知道。

- 跟混合器相比，继承生成的`css`代码相对更少。因为继承仅仅是重复选择器，而不会重复属性，所以使用继承往往比混合器生成的`css`体积更小。如果你非常关心你站点的速度，请牢记这一点。
- 继承遵从`css`层叠的规则。当两个不同的`css`规则应用到同一个`html`元素上时，并且这两个不同的`css`规则对同一属性的修饰存在不同的值，`css`层叠规则会决定应用哪个样式。相当直观：通常权重更高的选择器胜出，如果权重相同，定义在后边的规则胜出。

混合器本身不会引起`css`层叠的问题，因为混合器把样式直接放到了`css`规则中，而继承存在样式层叠的问题。被继承的样式会保持原有定义位置和选择器权重不变。通常来说这并不会引起什么问题，但是知道这点总没有坏处。

### 使用继承的最佳实践

通常使用继承会让你的`css`美观、整洁。因为继承只会在生成`css`时复制选择器，而不会复制大段的`css`属性。但是如果你不小心，可能会让生成的`css`中包含大量的选择器复制。

避免这种情况出现的最好方法就是不要在`css`规则中使用后代选择器（比如`.foo .bar`）去继承`css`规则。如果你这么做，同时被继承的`css`规则有通过后代选择器修饰的样式，生成`css`中的选择器的数量很快就会失控：

```scss
.foo .bar { @extend .baz; }
.bip .baz { a: b; }
```

在上边的例子中，`sass`必须保证应用到.baz的样式同时也要应用到`.foo .bar`（位于class="foo"的元素内的class="bar"的元素）。例子中有一条应用到`.bip .baz`（位于class="bip"的元素内的class="baz"的元素）的`css`规则。当这条规则应用到`.foo .bar`时，可能存在三种情况，如下代码:

```html
<!-- 继承可能迅速变复杂 -->
<!-- Case 1 -->
<div class="foo">
  <div class="bip">
    <div class="bar">...</div>
  </div>
</div>
<!-- Case 2 -->
<div class="bip">
  <div class="foo">
    <div class="bar">...</div>
  </div>
</div>
<!-- Case 3 -->
<div class="foo bip">
  <div class="bar">...</div>
</div>
```

为了应付这些情况，`sass`必须生成三种选择器组合（仅仅是.bip .foo .bar不能覆盖所有情况）。如果任何一条规则里边的后代选择器再长一点，`sass`需要考虑的情况就会更多。实际上`sass`并不总是会生成所有可能的选择器组合，即使是这样，选择器的个数依然可能会变得相当大，所以如果允许，尽可能避免这种用法。

值得一提的是，只要你想，你完全可以放心地继承有后代选择器修饰规则的选择器，不管后代选择器多长，但有一个前提就是，不要用后代选择器去继承。

## 小结

本文介绍了`sass`最基本部分,你可以轻松地使用`sass`编写清晰、无冗余、语义化的`css`。对于`sass`提供的工具你已经有了一个比较深入的了解，同时也掌握了何时使用这些工具的指导原则。

变量是`sass`提供的最基本的工具。通过变量可以让独立的`css`值变得可重用，无论是在一条单独的规则范围内还是在整个样式表中。变量、混合器的命名甚至`sass`的文件名，可以互换通用`_`和`-`。同样基础的是`sass`的嵌套机制。嵌套允许`css`规则内嵌套`css`规则，减少重复编写常用的选择器，同时让样式表的结构一眼望去更加清晰。`sass`同时提供了特殊的父选择器标识符`&`，通过它可以构造出更高效的嵌套。

你也已经学到了`sass`的另一个重要特性，样式导入。通过样式导入可以把分散在多个`sass`文件中的内容合并生成到一个`css`文件，避免了项目中有大量的`css`文件通过原生的`css` `@import`带来的性能问题。通过嵌套导入和默认变量值，导入可以构建更强有力的、可定制的样式。混合器允许用户编写语义化样式的同时避免视觉层面上样式的重复。你不仅学到了如何使用混合器减少重复，同时学习到了如何使用混合器让你的`css`变得更加可维护和语义化。最后，我们学习了与混合器相辅相成的选择器继承。继承允许你声明类之间语义化的关系，通过这些关系可以保持你的`css`的整洁和可维护性。

























