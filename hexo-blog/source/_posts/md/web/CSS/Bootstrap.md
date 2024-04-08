---
title: 'Bootstrap'
date: 2022-8-9 07:28:42
cover: false
---

[Bootstrap中文网 (bootcss.com)](https://www.bootcss.com/)

版本：[Versions · Bootstrap v5.3 (getbootstrap.cn)](https://www.getbootstrap.cn/docs/versions/)

# V5

## 安装



# Bootstrap基础

## `box-sizing`

为了避免内边距影响盒子大小，计算盒子尺寸的方式被设置为了border-box;

```css
* {
    box-sizing: border-box;
}
```

## 流体容器 .container-fluid

流体容器，width：auto;加padding会向里缩，不会撑开盒子（盒子模型的公式）

备注：width:100%;加padding会撑开盒子

```css
.container-fluid {
    padding-right: 15px;
    padding-left: 15px;
    margin-right: auto;
    margin-left: auto;
}
```

## 固定容器 .container

固定容器的底层是`媒体查询`

```css
@media (min-width: 1200px)
.container {
    width: 1170px;
}

@media (min-width: 992px)
.container {
    width: 970px;
}
@media (min-width: 768px)
.container {
    width: 750px;
}
.container {
    padding-right: 15px;
    padding-left: 15px;
    margin-right: auto;
    margin-left: auto;
}
```

| 阈值                               | 容器的width       |
| ---------------------------------- | ----------------- |
| 大于等于1200（lg：大屏pc）         | 1170（1110+槽宽） |
| 大于等于992（md:中屏pc），小于1200 | 970（940+槽宽）   |
| 大于等于768（sm：平板），小于992   | 750（720+槽宽）   |
| 小于768（xs：移动手机）            | auto              |

小于768时，相当于又是一个流体容器

## 栅格系统

栅格使用初体验

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <style>
        .container{
            background-color:pink;
        }
        div[class|=col]{
            border:1px solid black;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-lg-10">col-lg-10</div>
        <div class="col-lg-2">col-lg-2</div>
    </div>
    <div class="row">
        <div class="col-lg-6">col-lg-6</div>
        <div class="col-lg-6">col-lg-6</div>
    </div>
    <div class="row">
        <div class="col-lg-4">col-lg-4</div>
        <div class="col-lg-8">col-lg-8</div>
    </div>
</div>
</body>
<script src="js/jquery-3.5.1.js"></script>
<script src="js/bootstrap.min.js"></script>
</html>
```

### 栅格源码_固定容器

| 源码相对路径                    | 作用                     |
| ------------------------------- | ------------------------ |
| less/variables.less             | 变量的定义               |
| less/grid.less                  | 整合在一起               |
| less/mixins/grid.less           | 定义混合                 |
| less/mixins/clearfix.less       | 解决高度塌陷             |
| less/mixins/grid-framework.less | 整个文件都是用来定义列的 |



```
less/mixins/grid.less
```

### 固定容器和流体容器的公共样式

```css
//@grid-gutter-width  槽宽
.container-fixed(@gutter: @grid-gutter-width) {
  margin-right: auto;
  margin-left: auto;
  padding-left:  floor((@gutter / 2));//一半向上取整
  padding-right: ceil((@gutter / 2));//一半向下取整
  &:extend(.clearfix all);//继承clearfix的全部
}
```

相当于

```css
//固定容器和流体容器的公共样式
margin-right: auto;
margin-left: auto;
padding-left:  15px;
padding-right:  15px;
```

### 固定容器单独额外的样式

就是三个媒体查询

```less
@media (min-width: @screen-sm-min) {
  //768px 在variables.less中定义
  width: @container-sm; //750 = 720 + 槽宽
}
@media (min-width: @screen-md-min) {
  width: @container-md;
}
@media (min-width: @screen-lg-min) {
  width: @container-lg;
}

```

如果屏幕宽度超过2000，最上面的两个样式是读到的，只不过最后被覆盖了 所以上面的3个媒体查询顺序不能变

### 栅格源码_行(row)

```less
.make-row(@gutter: @grid-gutter-width) {
  margin-left: ceil((@gutter / -2)); //负的槽宽的一半
  margin-right: floor((@gutter / -2));
  &:extend(.clearfix all);
}

```

相当于

```css
margin-left: -15px;
margin-right: -15px;

```

### 栅格源码_列（column）

第一步 .make-grid-columns()

`grid-framework.less`里面的`.make-grid-columns()`

```less
.make-grid-columns() {
  // Common styles for all sizes of grid columns, widths 1-12
  .col(@index) {
    //避免编译
    @item: ~".col-xs-@{index}, .col-sm-@{index}, .col-md-@{index}, .col-lg-@{index}";
    .col((@index + 1), @item);
    // 递归.col(1)
    // .col(2,".col-xs-@{1}, .col-sm-@{1}, .col-md-@{1}, .col-lg-@{1}")
    // less中的变量属于块级作用域
    //此时，上述有两个参数
  }
  //.col(2,".col-xs-1, .col-sm-1, .col-md-1, .col-lg-1")
  .col(@index, @list) when (@index =< @grid-columns) {
    // 2 =< 12
    @item: ~".col-xs-@{index}, .col-sm-@{index}, .col-md-@{index}, .col-lg-@{index}";
    .col((@index + 1), ~"@{list}, @{item}");
    //.col(3,".col-xs-1, .col-sm-1, .col-md-1, .col-lg-1,.col-xs-2, .col-sm-2, .col-md-2, .col-lg-2")
    //.col(4,".col-xs-1, .col-sm-1, .col-md-1, .col-lg-1,.col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3")
    //...递归调用    //index = 12
    //.col(13,str12:".col-xs-1, .col-sm-1, .col-md-1, .col-lg-1,.col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3 ...... .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12")
  }
  .col(@index, @list) when (@index > @grid-columns) {
    // 13 > 12
    //把str12当作选择器来使用
    @{list} {
      position: relative;
      min-height: 1px;
      padding-left: ceil((@grid-gutter-width / 2));
      padding-right: floor((@grid-gutter-width / 2));
    }
  }
  .col(1);
}

```

跑完这个混合的递归后，相当于:

```css
//中间就省略了
.col-xs-1,
.col-sm-1,
.col-md-1,
.col-lg-1,
.col-xs-2,
.col-sm-2,
.col-md-2,
.col-lg-2,
.col-xs-3,
.col-sm-3,
.col-md-3,
.col-lg-3 ...... .col-xs-12,
.col-sm-12,
.col-md-12,
.col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 15px;
  padding-right: 15px;
}

```

第二步`.make-grid(xs)`

```less
//移动端优先
.make-grid(@class) {
  //xs
  .float-grid-columns(@class);
  // 给12个类名，添加左浮动
  .loop-grid-columns(@grid-columns, @class, width);
  .loop-grid-columns(@grid-columns, @class, pull);
  .loop-grid-columns(@grid-columns, @class, push);
  .loop-grid-columns(@grid-columns, @class, offset);
}

```

2.1 .`float-grid-columns(xs)`

```less
.float-grid-columns(@class) {
  //xs  
  .col(@index) {    
    @item: ~".col-@{class}-@{index}";    
    .col((@index + 1), @item);    
    //.col(2,".col-xs-1")  
  }  
  .col(@index, @list) when (@index =< @grid-columns) { 
    //2 =< 12    
    @item: ~".col-@{class}-@{index}";    
    .col((@index + 1), ~"@{list}, @{item}");    
    //.col(2,".col-xs-1")    
    //递归生成    .col(13,str12:".col-xs-1,.col-xs-2,.col-xs-3,.col-xs-4, ...... , .col-xs-12,")  }  
    .col(@index, @list) when (@index > @grid-columns) { 
      // 13>12    @{list} {    //.col-xs-1,.col-xs-2,.col-xs-3,.col-xs-4, ...... , .col-xs-12      
        float: left;    
      }  
    }  
    .col(1);
  }
```

2.2 width `.loop-grid-columns(xs)`

```less
// 2.2
.loop-grid-columns(@index, @class, @type) when (@index >= 0) {
  //12 xs width   12>=0（这里是大于等于）index:12 ----> 1  
  .calc-grid-column(@index, @class, @type);  
  // next iteration  
  .loop-grid-columns((@index - 1), @class, @type);}    
  //生成类名，指定宽度
  .calc-grid-column(@index, @class, @type) when (@type = width) and (@index > 0) {
    // 12 xs @type = width   12>0（这里是大于）  
    .col-@{class}-@{index} {    
      width: percentage((@index / @grid-columns));   
       //每次调用的时候，都会生成一个.col的class类名    
       //.col-xs-12,.col-xs-12,...... ,.col-xs-1    
       //width:分别对应  12/12  11/12   ...... 1/12    
       //.col-xs-12{width:12/12}    
       //.col-xs-11{width:11/12}    
       //.col-xs-10{width:10/12}    
       // ...    
       //.col-xs-11{width:1/12}  
    }
  }
}
```

由上可知，由xs版本的，最后会有sm、md、lg版本的，里面的值其实是一样的

并且，lg之前，xs、sm、md都是已经被渲染过了的

```html
<div class="container">
  <div class="row">
    <div class="col-lg-10 col-md-6">col-lg-10</div>
    <div class="col-lg-2 col-md-6">col-lg-2</div>
  </div>
</div>

```

所以，类名写成上述代码的时候，lg屏下是10/2，而md屏下则是6/6

2.3 列排序`pull` && `push` 当index时0时，除了生成了和上面一样的，还有`.col-xs-push-0{left:auto}`和`.col-xs-pull-0{right:auto}`

```css
push.col-xs-push-12{left:12/12}
.col-xs-push-11{left:11/12}
......
.col-xs-push-1{left:1/12}
.col-xs-push-0{left:auto}

pull.col-xs-pull-12{right:12/12}
.col-xs-pull-11{right:11/12}
......

.col-xs-pull-1{right:1/12}
.col-xs-pull-0{right:auto}
```

2.4 列偏移 实际控制的是`margin-left`

```css
offset.col-xs-offset-12{right:12/12}
.col-xs-offset-11{right:11/12}
......
.col-xs-offset-1{right:1/12}
.col-xs-offset-0{right:0}
```

## 响应式工具





# V4

[下载 Bootstrap · Bootstrap v4 中文文档 v4.6 | Bootstrap 中文网 (bootcss.com)](https://v4.bootcss.com/docs/getting-started/download/)

# V3

[起步 · Bootstrap v3 中文文档 | Bootstrap 中文网 (bootcss.com)](https://v3.bootcss.com/getting-started/)

[Bootstrap3从由Less编写转成由Sass编写是出于哪些考虑？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/24741026/answer/63362486)



