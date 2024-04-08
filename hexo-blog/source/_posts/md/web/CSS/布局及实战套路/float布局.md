---
title: 'float布局'
date: 2022-9-1 07:28:42
cover: false
tags:
- CSS
- CSS布局
categories: 'CSS'
typora-root-url: float布局
---

# 浮动

通过浮动，可以使一个元素向其父元素的左侧，或者右侧移动（直观现象）

主要作用就是让页面中的元素可以**水平排列**，通过浮动，可以制作一些水平方向的布局

使用`float`属性，来设置元素的浮动

可选值：

- `none`：默认值，元素不浮动
- `left`：元素向左浮动
- `right`：元素向右浮动

## 单独给一个子元素设置浮动



html

```html
<div class="container">
    <div class="box1"></div>
    <div class="box2"></div>
</div>
```

css

```css
    <style>
        .box2 {
            width: 200px;
            height: 200px;

        }
        .box1 {
            width: 100px;
            height: 100px;
        /*    设置左浮动*/
            float: left;
        }
        .box1 {
            background-color: #bfa;

        }

        .box2 {
            background-color: orange;

        }
    </style>
```

初始：

![image-20211121100642842](image-20211121100642842.png)

设置浮动的效果：

`box1`会脱离文档流，`box2`会填充到之前`box1`的起始位置

![image-20211121100750890](image-20211121100750890.png)



## 给多个子元素一起设置浮动



html

```html
<div class="container">
    <div class="box1"></div>
    <div class="box2"></div>
    <div class="box3"></div>
</div>
```

css

```css
    <style>

        .box1, .box2, .box3 {
            width: 100px;
            height: 100px;
        /*    设置左浮动*/
            float: left;
        }
        .box1 {
            background-color: #bfa;

        }

        .box2 {
            background-color: orange;

        }
    </style>
```

效果：

多个设置浮动的子元素，并并排显示

![image-20211121101124317](image-20211121101124317.png)

## 浮动特点

- 子元素设置浮动后，会完全从文档流中脱离，不再占用文档流的位置（可以理解为，自己又新建了一个图层）

  - 原来子元素的位置，会被之前文档流中新的子元素，重新占据位置

  - 之前讲过的，水平布局的等式，自然不需要成立

  - 浮动的元素，不会从父元素中移除

  - 父元素中，没有浮动的块元素，始终会挡在浮动元素的上面

    - 如下，box1没有设置浮动，其他两个设置浮动

      ![image-20211121102019886](image-20211121102019886.png)

  - 在3个子元素都是浮动元素的情况下，box3不会超过同级上面的兄弟元素box2，最多是一样高，不会和box1跑一行去

    - box1/2/3都设置浮动

    - 如下，在最后，尽管第一行的margin-right还有空间，但box3是不会跑到box1的这一行的：

      ![input](input.gif)

  - 浮动目前来说，主要作用就是让页面中的元素可以水平排列，通过浮动，可以制作一些水平方向的布局

- 浮动的元素，不会覆盖文字，所以我们可以利用浮动，来设置文字环绕图片的效果

- 子元素设置浮动后，将会从文档流中脱离，从文档流中脱离后，元素的一些特点也会变化

  - 块元素：
    - 块元素不再独占一行
    - 块元素的高度和宽度都被内容撑开
  - 行内元素：
    - 宽高都是可以生效的，特点是和上面一样的
  - 脱离文档流后，不再区分块元素和行内元素

## 浮动布局问题：高度塌陷 和BFC

### 高度塌陷

在浮动布局中，父元素的高度默认是被子元素撑开的

- 当子元素浮动后，其会完全脱离文档流，
- 子元素此时将会无法撑起父元素高度，导致父元素高度丢失
- 父元素高度丢失后，剩下的子元素会自动上移，导致页面的布局混乱
- 所以，高度塌陷是浮动布局中比较常见的一个问题，这个问题必须要进行处理

### BFC

BFC（Block Formatting Context），块级格式化环境

- BFC是css中的一个隐含属性，可以为一个元素开启BFC
- 开启BFC后，该元素会变成一个独立的布局区域
- 元素开启BFC后的特点：
  -  开启BFC的元素，不会被浮动元素覆盖
  -  开启BFC的元素，子元素和父元素外边距不会重叠
  -  开启BFC的元素，可以包含浮动的元素
- 开启BFC的方式：
  - 设置元素的浮动（不推荐）
  - 将元素设置为行内块元素（不推荐）
  - 将元素的overflow设置为，一个非visible的值，一般我们用hidden即可
  - 所有开启BFC的方式，都有副作用，我们只是要找一个副作用最小的
    - 设置overflow仍然是存在副作用的

### clear

由于box1的浮动，导致box1位置上移，也就是box3受到了box1浮动的影响，位置发生了改变

可以通过clear属性，来清楚浮动元素，对当前元素所产生的的影响

clear

- 作用
  - 清楚浮动元素对当前元素所产生的影响
  - 可选值
    - left：清除左侧浮动元素对当前元素的影响
    - right：清除右侧浮动元素对当前元素的影响
    - both：清除两侧中，最大影响的那一侧

html

```html
<div class="container">
    <div class="box1"></div>
    <div class="box2"></div>
</div>
```

css

```css
    <style>
        .box1 {
            background-color: #bfa;
            width: 100px;
            height: 100px;
            float: left;
        }

        .box2 {
            background-color: orange;
            width: 500px;
            height: 100px;
            clear: both;
        }
    </style>
```

![image-20211121154806912](image-20211121154806912.png)

并不是说，box1没有浮动了，只是说，box2不再受到box1的影响了

原理：设置clear之后，浏览器会给box2自动计算一个上外边距

### 解决高度塌陷的最终方案

html

```html
<div class="container">
    <div class="box1"></div>
    <div class="box2"></div>
</div>
```

css

```css
        .container {
            border: 1px solid palevioletred;
        }
        .box1 {
            background-color: #bfa;
            width: 100px;
            height: 100px;
            float: left;
        }

        .box2 {
            clear: both;
        }
    </style>
```

虽然box1设置了浮动，但由于box2中，清除了浮动对齐的影响，所以box2还占据着原来的位置，所以父元素仍然是被撑起来的

但问题是，box2这个div，是我们自己加的，属于用结构处理表现的问题了，

现在不想加box2这个div

我们要在元素的最后，添加一个标签，只能通过html来添加吗？

不是

```css
.box1::after{
    /* 添加内容 */
	content:'';
    /* 清除其他元素浮动带来的影响 */
    clear: both;
    /* 默认是行内元素，设置为块元素 */
    display: block;
}
```



### 外边距折叠和高度塌陷的合并写法

类似上一节，解决外边距重叠的写法

给需要结局外边距折叠的父元素添加如下样式

```css
.clearfix::before {
	content:'';
    display: table;
}
```

解决外边距折叠和高度塌陷的合并写法

```css
.clearfix::before, .clearfix::after {	
    content: '';	
    display: table;	
    clear:both;
}
```

