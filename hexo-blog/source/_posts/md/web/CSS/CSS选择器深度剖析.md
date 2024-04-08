---
title: 'CSS选择器深度剖析'
date: 2022-7-9 07:28:42
cover: false
tags:
- CSS选择器
categories: 'CSS'

---



# 选择器

## 常用选择器：

- 元素选择器
- 类选择器
- id选择器

## 交集选择器：

```css
div.red{	
    color:red;
}
```

## 并集选择器：

```css
h1, span{	
    color:red;
}
```

## 关系选择器：

- 父元素：直接包含子元素的元素
- 子元素：直接被父元素包含的元素
- 祖先元素：直接或间接包含后代元素的元素
- 后代元素：直接或间接被祖先元素包含的元素
- 兄弟元素：拥有相同父元素的元素

### 子元素选择器：

```css
div.box > span{	
    color:red;
}
```

### 后代元素选择器：

```css
div.box span{	
    color:red;
}
```

### 兄弟选择器：

```css
p + span{	
    color:red;
}
```

### 选择下面所有的兄弟：

```css
p ~ span{	
    color:red;
}
```

## 属性选择器：

```css
p[title]{	
    color:red;
}
[title=abc]{	
    color:red;
}
/*以abc开头*/
[title^=abc]{	
    color:red;
}
/*以abc结尾*/
[title$=abc]{	
    color:red;
}
/*包含abc即可*/
[title*=abc]{	
    color:red;
}
```

## 伪类选择器：

```css
:root {
  --global-color: #666;
  --pane-padding: 5px 42px;
}

ul > li:first-child{	
    color:red;
}
ul > li:last-child{	
    color:red;
}
ul > li:nth-child(1){	
    color:red;
}	
ul > li:nth-child(2n){	
    color:red;
}
```

```css
ul > li:first-of-type{	
    color:red;
}
ul > li:last-of-type{	
    color:red;
}
ul > li:nth-of-type(1){	
    color:red;
}
ul > li:nth-of-type(2n){	
    color:red;
}
```

### 否定伪类：

```css
ul > li:not(:nth-child(5)){	
    color:red;
}
```

### 超链接伪类：

```css
a:link{	
    color:red;
}

a:visited{	
    color:red;
}

a:hover{	
    color:red;
}

a:active{	
    color:red;
}
```

## 伪元素选择器：

```css
/*表示第一个字母*/
p::first-letter{	
    color:red;
}

/*表示第一行*/
p::first-line{	
    color:red;
}

/*表示选中的内容*/
p::selection{	
    olor:red;}
/*元素的开始*/

p::before{	
    color:red;
}

/*元素的结束*/
p::after{	
    color:red;
}
```

## 餐厅练习（选择器练习）

[https://flukeout.github.io/](https://flukeout.github.io/)



# 选择器的权重

- 样式的冲突：当我们通过不同的选择器，选中相同的元素，并且为相同的样式设置不同的值时，此时就发生了样式的冲突
- 发生样式冲突时，应用哪个样式由选择器的权重（优先级）决定
- 选择器的权重
  - 内联样式				 1,0,0,0
  - id选择器				0,1,0,0
  - 类和伪类选择器    0,0,1,0
  - 元素和伪元素选择器            0,0,0,1
  - 通配选择器            0,0,0,0
  - 继承的样式            没有优先级
- 比较优先级时，需要将所有的选择器的优先级进行相加计算，最后优先级越高，则越优先显示（分组选择器是单独计算的）
  - 选择器的累加不会超过其最大数量级，类选择器再高，也不会超过id选择器
  - 如果优先级计算后相同，此时则优先使用靠下的样式
- 可以在某一个样式的后边添加`!important`，则此时该样式会获取到最高的优先级，甚至超过内联样式（开发中慎用）