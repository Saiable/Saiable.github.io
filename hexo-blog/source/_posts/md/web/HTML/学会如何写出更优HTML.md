---
title: '如何写出更优HTML'
date: 2022/8/10 09:03:02
cover: false
tags:
- HTML
categories: 'HTML'
---



# 工具层

## `Emmet`

### 安装

现代`IDE`如`webstorm`、`vscode`等，通常支持`emmet`语法

### 生成`HTML`

#### 根据`id`或类名生成标签

```html
#page>div.logo+ul#navigation>li*5>a{item $}
```

最后敲一下`tab`，`webstorm`中的生成结果

```html
<div id="page">
  <div class="logo"></div>
  <ul id="navigation">
    <li><a href="">item 1</a></li>
    <li><a href="">item 2</a></li>
    <li><a href="">item 3</a></li>
    <li><a href="">item 4</a></li>
    <li><a href="">item 5</a></li>
  </ul>
</div>
```

`emmet`默认生成的标签为`div`，生成`id`为`page`的`div`标签

```html
div#page
```

或者

```html
#page
```

编写`class`为`content`的`p`标签

```html
p.content
```

同时指定`id`为`navigation`和`class`为`nav`的`ul`标签

```html
ul#navigation.nav
```

#### 兄弟标签：`+`

```html
div+ul+bq
```

结果：

```html
<div></div>
<ul></ul>
<blockquote></blockquote>
```

#### 后代标签：`>`

```html
div.nav>ul>li
```

结果：

```html
<div class="nav">
  <ul>
    <li></li>
  </ul>
</div>
```

#### 上级元素：`^`

上级元素（`climb-up`）是什么意思呢？

在上例中，如果继续写下去，后续内容都是在`li`标签下的，如果想和`ul`平级，需要使用`^`提升一个层次

```html
div.nav>ul>li^span
```

结果：

```html
<div class="nav">
  <ul>
    <li></li>
  </ul>
  <span></span>
</div>
```

注意：层级提升支持多次

#### 重复多份：`*`

特别是无序列表，`ul`下肯定不止一个`li`

```html
ul>li*5
```

结果

```html
  <ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
  </ul>
```

#### 分组：`()`

用括号进行分组，表示一个代码块，分组内部的嵌套和层级关系，与分组外部无关

```html
div>(header>ul>li*2>a)+footer>p
```

结果：

```html
<div>
  <header>
    <ul>
      <li><a href=""></a></li>
      <li><a href=""></a></li>
    </ul>
  </header>
  <footer>
    <p></p>
  </footer>
</div>
```

如果不加分组：

```
div>header>ul>li*2>a+footer>p
```

结果：

```html
<div>
  <header>
    <ul>
      <li><a href=""></a>
        <footer>
          <p></p>
        </footer>
      </li>
      <li><a href=""></a>
        <footer>
          <p></p>
        </footer>
      </li>
    </ul>
  </header>
</div>
```

#### 属性：`[]`

```html
a[href='https://mindcons.cn' title="sai's blog"]
```

结果：

```html
<a href="https://mindcons.cn" title="sai's blog"></a>
```

也可以生成一些自定义属性：

```html
div[data-title='title' data-content='content']
```

结果：

```html
<div data-title="title" data-content="content"></div>
```

#### 编号：`$`

`$`表示一位数字，只出现一个的话，就从1开始，如果出现多个，就从0开始

```html
ul>li.item$*5
```

结果：

```html
<ul>
  <li class="item1"></li>
  <li class="item2"></li>
  <li class="item3"></li>
  <li class="item4"></li>
  <li class="item5"></li>
</ul>
```

如果想生成三位数，就要写三次`$`

```html
ul>li.item$$$*5
```

结果：

```html
<ul>
  <li class="item001"></li>
  <li class="item002"></li>
  <li class="item003"></li>
  <li class="item004"></li>
  <li class="item005"></li>
</ul>
```

可以在`$`后增加`@-`实现倒序

```html
ul>li.item$@-*5
```

结果：

```html
<ul>
  <li class="item5"></li>
  <li class="item4"></li>
  <li class="item3"></li>
  <li class="item2"></li>
  <li class="item1"></li>
</ul>
```

在`$`后增加`@N`指定开始的序号

```html
ul>li.item$@3*5
```

结果：

```html
<ul>
  <li class="item3"></li>
  <li class="item4"></li>
  <li class="item5"></li>
  <li class="item6"></li>
  <li class="item7"></li>
</ul>
```

#### 文本内容：`{}`

生成超链接一般要加上可点击的文本内容

```html
a[href='https://mindcons.cn' title="sai's blog"]{点击这里}
```

结果：

```html
<a href="https://mindcons.cn" title="sai's blog">点击这里</a>
```

#### 隐式标签

隐式标签表示`emmet`可以省略某些标签名

例如：声明一个带类的`div`，只需要输入`.item`

另外，`emmet`还会根据父标签进行判定，例如`ul>.item$*5`一样可以生成正确的结构

列出所有隐式标签名称：

```
li: 用于ul和ol中
tr: 用于table、tbody、thead和tfoot中
td: 用于tr中
option: 用于select和optgroup中

```

所有的书写，不要有空格

### 生成`CSS`

参考链接：https://wenku.baidu.com/view/3902e24f26c52cc58bd63186bceb19e8b8f6ecf7.html

### 生成长文本

`html`中输入`lorem`或者`lipsum`，即可生成长文本

还可以指定文字的个数：`lorem10`

## 常用`HTML`结构指令

- `html:5`或`!`，快速生成`HTML5`骨架结构（最后敲一下`tab`键）

# 代码层

## ` HTML` 的语义化

如果很强烈考虑兼容 `IE` 的话，那么本章节不太适合学习🐶。

参考链接：

- https://juejin.cn/search?query=%E8%AF%AD%E4%B9%89%E5%8C%96
- https://juejin.cn/post/6990572224637992996

# 资源层

- 使用图片精灵（精灵图）
  - 一张图上有多个小图（为什么叫图片精灵呢？那些小图片都是精灵，一个一个蹦出来的，所以叫图片精灵）
  - 这样就只会加载一张图片了。因为减少请求次数，页面加载会快一些





