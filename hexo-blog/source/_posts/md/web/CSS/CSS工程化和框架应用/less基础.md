---
title: 'Less基础'
date: 2022-8-9 07:28:42
cover: false
typora-root-url: less基础
tags:
- CSS预处理器
categories: CSS预处理器
---

# `Less`

[Less 快速入门 | Less.js 中文文档 - Less 中文网 (bootcss.com)](https://less.bootcss.com/)

[Less 入门教程 - 开发文档 ](https://www.wenjiangs.com/doc/less-mixins)

## 安装

### 脚手架中安装

`vue3-cli`在配置项中可以直接选中less语言或者sass语言，2里面还得安装

- 一、安装开发依赖，安装如果有问题，可以指定版本的less-loader

  ```
  npm install less less-loader --save-dev
  ```

- 二、打开 ` build / webpack.base.conf.js` ，配置`rule`属性

  ```
       {
          test: /\.less$/,
          loader: "style-loader!css-loader!less-loader"
        }
  ```

- 三：在组件页面内部用` lang='less'`

  ```css
  <style scoped lang='less'>
  .a{
      .b{}
  }
   
  </style>
  ```



如果使用的是`vue-cli5`

- 此时自己下载的`vue-cli`，用到`webpack`的版本为`5`版本（`node_modules`文件夹找`webapck`文件夹，查看`package.json`文件），这个时候装`less-loader`是没有问题的，因为默认安装的是最新版的`less-loader`，新版本是为了迎合`webpakc5`
- 如果`vue-cli`用的`webpack`为`4`版本，则要`less-loader`版本降级以兼容`webpack4`
  - 查看所有版本：`npm view less-loader versions`
  - 试一下不那么新的版本：`npm i less-loader@7.0.0 -D` 
    - `8`及以上的版本就是为`webpack4`服务的了

### 浏览器环境安装

去`github`上，下载，然后`html`文件中导入`dist`目录下的`less.min.js`，引入的`less`文件的`rel`属性为`stylesheet/less`，并使用`liveServer`打开即可

```html
    <!-- 导入less -->
    <link rel="stylesheet/less" href="css/index.less"></link>
    <script src="css/less.min.js"></script>
```

### vscode插件

可以在vscode中，安装less插件

配置



## 基本使用

- 使用态样式语言，属于`css`预处理器范围，它扩展了`css`语言

  - 增加了变量、`Mixin`、函数等特性，使`css`更易维护和扩展

  - `less`既可以在客户端上运行，也可以借助`node`在服务器上运行

    - 在 `Node.js` 环境中使用 `Less` ：

```
      npm install -g less
      > lessc styles.less styles.css
```

      在浏览器环境中使用 `Less` ：
    
      ```html
      <link rel="stylesheet/less" type="text/css" href="styles.less" />
      <script src="//cdnjs.cloudflare.com/ajax/libs/less.js/3.11.1/less.min.js" ></script>
      ```

### `less`中的注释

- 以`//`开头的注释，不会被编译到`css`中
- 以`/* */`包裹的注释会被编译到`css`中

### `less`中的变量

使用`@`来声明一个变量：`@pink: pink`

#### 变量的使用场合

主要为以下几种：

- 值变量

  ```less
  // 定义变量
  @color-white: white;
  @color-danger: #bd362f;
  
  .btn-danger {
      color: @color-white;
      background-color: @color-danger; // 使用变量
  }
  ```

- 选择器变量

  作为选择器和属性名：`@{变量名}`的形式，一般用的很少，不会把选择器和属性名定义成变量的

  ```less
  @display: display; // 定义属性名变量
  @selector: .btn; // 定义选择器变量
  @{selector} { //使用变量
      @{display}: inline-block;
  }
  ```

  ```less
  @sleName: container;
  
  .@{sleName} {
    color: #fff;
  }
  
  #@{sleName} {
    color: #fff;
  }
  
  .top-@{sleName} {
    color: #fff;
  }
  ```

- 属性名变量

  ```less
  @bg: background-color;
  
  .container {
    @{bg}: red;
  }
  ```

- URL 变量

  文件的 URL 也可以作为一个变量，便于文件结构变化后修改文件路径。

  ```less
  @util: "../util"
  
  .container {
    background-image: src("@{util}/a.png");
  }
  ```

- 声明变量

  声明变量可以表示一段样式，类似于 Mixins（后续教程会提到），使用变量时需在后面加上 `()`。

  ```less
  @bg: {background-color:red};
  
  .container {
    @bg();
  }
  ```

- 变量运算

  变量可以通过加减乘除等算法输出运算后的值。

  > 1. 加减运算时以第一个数据的单位为准
  > 2. 乘除运算注意保持单位的一致

  ```less
  @width: 20px;
  
  .container {
    width: @width/2;
  }
  ```




#### 变量的延迟加载

```less
@height:300px;
@font_size:12px;
.textarea {
	width:@width;
	height:@height;
	font-size:@font_size;
}
@width:5000px; // 定义在最后，也可以被读取到
```

同一变量名称定义多次时，只会使用最后一次在作用域中定义的变量。

```less
@var: 0;
.class {
    @var: 1;
    .brass {
        @var: 2;
        three: @var; // 结果不是2，是3，要等当前作用域全部读取完才会加载
        @var: 3;
    }
    one: @var; // 1
}
```

#### 小结

我们可以创建一个配置文件单独声明变量，利于我们维护代码。

类似于如下代码：

```less
@default-color          : @theme-color;
@success-color          : #34BFA3;
@warning-color          : #FFE57F;
@error-color            : #F4516C;
@disabled-color         : #DEE2E6;
@selected-color         : fade(@default-color, 90%);
@tooltip-color          : #fff;
@subsidiary-color       : #80848f;
@rate-star-color        : #f5a623;
```

### `less`中的嵌套规则

- 基本嵌套使用

  ```less
  .outer {
      .inner {
          
      }
  }
  ```

- `&`的使用（伪类、伪元素）

  ```less
      .inner {
          &:hover {
              // .inner:hover，如果不加&，编译后会多一个空格
              // 添加了&表示选取当前元素
          } 
          &:focus {
              
          }
      }
  ```

- 媒体查询

  ```less
  // 定义变量为一个字符串
  @min-1024: ~"(min-width: 1024px)";
  
  .element {
  
      // 在媒体查询处使用该变量
      @media @min-1024 {
          color: skyblue;
      }
  }
  ```

### `less`运算

在`less`中可以进行加减乘除的运算

css中的`calc()`运算是在运行时计算的

```less
.container {
  width: (100 + 100px);
}
```

编译结果

```css
.container {
  width: 200px;
}
```

如果运算的单位是一致的，那么只要有一个带单位即可

### `less`避免编译

```less
.container {
  width: calc(100px + 200px);
}
```

有的less编译器会直接编译结果，但我想交给浏览器去计算

使用`~`语法实现避免编译

```less
.container {
  width: ~"calc(100px + 200px)";
}
```

### `less`中的继承

性能比混合高

灵活度比混合低



这个小节我们会介绍 Less 中的一个伪类，这个伪类一般与我们需要复用的样式所结合使用，但是这个伪类与我们平常使用的CSS 伪类比如 `:hover` 等不太一样，它可以与这些伪类结合使用，一定要加以区分。

#### 什么是继承？

> Extend is a Less pseudo-class which merges the selector it is put on with ones that match what it references.——官方定义

> 慕课解释：
>
> 1. Extend 是 Less 语法中的一个伪类，它可以继承所匹配的全部样式。
> 2. Extend 是为了解决样式表中重复的样式，这一点与其它语言中的继承功能相似。
> 3. Extend 主要用于复用重复的样式类，可附加在选择器上或放置到样式集中。

#### 语法详情

首先，我们先来看一个继承的代码例子，目的是先来大体了解一下 less 中继承的使用方式，让我们大体有个总体的印象，后面会详细讲解它的语法格式。

```less
.nav {
  &:extend(.line);
  background: blue;
}

.line {
  color: red;
}
```

在上面的样式表中，extend 会把 `nav` 的选择器应用到 `.line` 样式类上，`nav` 原本定义的样式保持不变。

```css
.nav {
  background: blue;
}
.line,
.nav {
  color: red;
}

```

**代码解释**：我们可以看到输出的代码中并没有 `:extend()` 这个伪类，在编译的过程中这个伪类会被删除掉，从而使原代码块保持原样，这一点与 `:hover` 那些伪类并不相同。

Less 中的继承有 2 种使用方法，分别为在**选择器**中使用，和在**样式集**中使用，2 种方式都是把需要继承的选择器名称写入 `:extend()` 的括号来实现继承的。

#### 附加在选择器上使用

Extend 可直接附加在选择器上使用。

**语法格式**

```less
<selector>:extend(<extendSelector>) { }
```

```less
.b{
  color: red;
}

.a:extend(.b) {
  background: blue;
}
```

CSS 输出代码：

```css
.a,.b {
  color: red;
}
  
.a {
  background: blue;
}
```

#### 在样式集中使用

Extend 也可以放到样式集中使用，但注意在使用时需在前面加上 `&`符号。

**语法格式**

```less
<selector> {
  &:extend(<extendSelector>);
}
```

```less
.a {
  &:extend(.b);
}

.b {
  color: red;
}
```

CSS 输出代码：

```css
.b,.a {
  color: red;
}
```

#### 继承多个样式类

```less
.nav {
  &:extend(.line, .b);
  background: blue;
}

.line {
  color: red;
}

.b {
  font-size: 18px;
}

```

CSS 输出代码：

```css
.nav {
  background: blue;
}
.line,
.nav {
  color: red;
}
.b,
.nav {
  font-size: 18px;
}

```

#### 继承中的`all`关键字

当继承嵌套结构的样式时，如果想要同时继承嵌套结构内的样式，需要在样式名加上`all`关键字。

```less
.a {
  &:extend(.b all);
}

.b {
  color: red;
  .c {
    background: #8a2be2;
  }
}
```

输出代码：

```css
.a,.b { 
  color: red;
}
  
.a .c, .b .c {
  background: #8a2be2;
}
```

我们再对比下不加 ‘all’ 关键字输出的代码：

```css
.b,
.a {
  color: red;
}

.b .c {
  background: #8a2be2;
}
```

#### Tips

1. 选择器可以包含多个伪类，但是 `:extend()` 必须位于末位。

   ```less
   div:hover:extend(span)
   ```

2. 选择器和 `:extend()` 之间是允许有空格。

   ```less
   div :extend(span)
   ```

3. 选择器可以多次继承。

   ```less
   .color {
     color: red;
   }
   
   .bg-color {
     background: green;
   }
   
   //  与 div:hover:extend(.color, .bg-color) 等效
   div:hover:extend(.color):extend(.bg-color)
   ```

4. 如果一个规则集包含多个选择器，其中任何一个选择器都可以具有 `:extend()` 。

   ```less
   .content:extend(.color), .image:extend(.bg-color) {
     color: red
   }
   ```

5. `:extend()` 可以匹配嵌套选择器。

   ```less
   div {
     img {
       width: 10px;
     }
   }
   
   .class:extend(div img) {
     height: 20px;
   }
   ```

6. `:extend()` 中所继承的选择器名称不能是变量，以下示例均为错误示范。

   ```less
   .content {
     color: blue;
   }
   
   .class:extend(@{selector}) {} // 找不到匹配项
   
   @selector: .content;
   ```

7. `:extend()` 并没有重复检测，请勿重复定义。比如以下代码中只用继承 `.success-info` 或者 `span` 即可，以下写法编译时并不会帮我们把重复的选择器删除掉。

   ```less
   .success-info,
   span {
     color: green;
   }
   
   .success:extend(.success-info, span) {}
   ```

   CSS输出代码

   ```css
   .success-info,
   span,
   .success,
   .success {
     color: green;
   }
   
   ```

#### 使用场景总结

- 利用重复代码

  通过继承我们可以创建出不同的基础样式，比如背景颜色、字体大小等：

  ```less
  .info-font {
    font-size: 28px;
  }
  
  .content {
    &:extend(.info-font)
  }
  ```

- 减小 CSS 代码体积

  在平时我们引用重复的代码可能会这样写，比如直接将 `.a` 的样式粘贴到 `.b` 中，然后代码将成了下面这样：

  ```css
  .a{
    color: #fff;
  }
  
  .b{
    color: #fff;
  }
  ```

  `:extend()` 已经帮助我们选择了一种高效利用样式的方式，通过选择器名称进行共用，从而帮助我们减少了 CSS 代码的体积：

  ```css
  .a, .b{
    color: #fff;
  }
  ```

#### 小结

本章节介绍了 Less 有关继承的使用方式，使用继承的第一步需要我们声明一个继承的样式，通常来讲这个样式是复用性较强的一段的 CSS 的代码，需要我们具有将重复出现的 CSS 代码抽离出来，比如布局方式、字体颜色大小等，灵活的运用可以帮助我们提高 CSS 代码的可维护性。

### `less`中的混合

>  混合就是将一系列属性，从一个规则集中引入到另一个规则集的方法
>
> 混合的定义在less规则中有明确的规定，使用 . 的形式来定义

#### 普通混合

可以直接写类名

`.sp-comm`也会被编译到`css`中

```less
.sp-comm {
    background: url("../images/comm-spr.png") no-repeat;
    background-size: 393px 200px;
}
//更多按钮箭头处理
.comm-more-arrow {
    display: inline-block;
    margin-left: 5px;
    width: 15px;
    height: 15px;
    .sp-comm; // 这里直接写类名即可
    background-position: -213px -126px;

}
```

#### 不带输出的混合

从上面的示例代码中，我们可以看到定义的 Mixins 也被编译到了输出的代码中，但是某些情况下这些样式造成不必要的重复。此时我们可以在定义 Mixins 时在类的名称后加上 “()” ，这样 Mixins 所定义的样式就不会编译到输出的代码中了。

加括号，不会被编译到`css`中

#### 带参数的混合

当 Mixins 同时包含多个参数时，多个参数之间使用 `;` 或者 `,` 分隔。建议使用 `;` ，因为在 Less 中逗号有两种含义：代表 Mixins 参数分隔符或 CSS 列表分隔符。

如果使用 `,` 作为分隔符，就不能使用含有 `,` 的属性值作为参数。此外，如果参数之间有一个 `;` 作为分隔符，编译器则会认为 `,` 属于属性值的一部分。

```less
.sp-comm(@w, @h) {
    background: url("../images/comm-spr.png") no-repeat;
    background-size: @w @h;
}

//更多按钮箭头处理
.comm-more-arrow {
    display: inline-block;
    margin-left: 5px;
    width: 15px;
    height: 15px;
    background-position: -213px -126px;

    .common1 {
        .sp-comm(100px, 200px);
    }

    .common2 {
        .sp-comm(200px, 300px)
    }
}
```

#### 带参数并且有默认值的混合

```less
.sp-comm(@w:10px, @h:20px) {
    background: url("../images/comm-spr.png") no-repeat;
    background-size: @w @h;
}
```

#### 参数顺序

Mixins 中的参数可以不按照特定的顺序定义，可以直接使用其参数名称进行定义。

- 输入代码

```less
.mixin(@color: black; @margin: 10px; @padding: 20px) {
  color: @color;
  margin: @margin;
  padding: @padding;
}

.primary {
  .mixin(@margin: 20px; @color: #33acfe);
}

.success {
  // 第一个参数未填写参数名称，所以代表的是 @color
  // 第二个参数名称为 @padding ，所以说 @margin 参数未传入会取默认值
  .mixin(#efca44; @padding: 40px);
}
```

- 输出代码

```css
.primary {
  color: #33acfe;
  margin: 20px;
  padding: 20px;
}

.success {
  color: #efca44;
  margin: 10px;
  padding: 40px;
}
```

#### 命名参数

```less
.sp-comm(@w:10px, @h:20px) {
    background: url("../images/comm-spr.png") no-repeat;
    background-size: @w @h;
}


.common1 {
    .sp-comm(@w:100px); // 指定实参
}
```

#### 匹配模式

画三角形

`index.less`

```less
@import url('./triangle.less');

#wrap{
    .arrow {
        .triangle(red, 40px);
    }
}
```

`triangle.less`

```less
.triangle(@color, @width) {
    width: 0px;
    height: 0px;
    border-width: @width;
    border-style: dashed solid dashed dashed;
    border-color: transparent @color transparent transparent;
    overflow: hidden;
}

```

如果还想抽离箭头的指向，如果还是加参数，就有点拉了，

可以用匹配模式

```less
.triangle(Bottom, @color, @width) {
    width: 0px;
    height: 0px;
    border-width: @width;
    border-style: solid dashed dashed dashed;
    border-color: @color transparent transparent transparent;
    overflow: hidden;
}

.triangle(Left, @color, @width) {
    width: 0px;
    height: 0px;
    border-width: @width;
    border-style: dashed solid dashed dashed;
    border-color: transparent @color transparent transparent;
    overflow: hidden;
}

.triangle(Top, @color, @width) {
    width: 0px;
    height: 0px;
    border-width: @width;
    border-style: dashed dashed solid dashed;
    border-color: transparent transparent @color transparent;
    overflow: hidden;
}

.triangle(Right, @color, @width) {
    width: 0px;
    height: 0px;
    border-width: @width;
    border-style: dashed dashed dashed solid;
    border-color: transparent transparent transparent @color;
    overflow: hidden;
}
```

可以进一步抽离公共样式

定义一个同名混合，使用`@_`来实现默认调用

除了`@_`参数，其它参数要对应上

```less
.triangle(@_, @color, @width) {
    width: 0px;
    height: 0px;
    overflow: hidden;
}

.triangle(Bottom, @color, @width) {
    border-width: @width;
    border-style: solid dashed dashed dashed;
    border-color: @color transparent transparent transparent;
}

.triangle(Left, @color, @width) {
    border-width: @width;
    border-style: dashed solid dashed dashed;
    border-color: transparent @color transparent transparent;
}

.triangle(Top, @color, @width) {
    border-width: @width;
    border-style: dashed dashed solid dashed;
    border-color: transparent transparent @color transparent;
}

.triangle(Right, @color, @width) {
    border-width: @width;
    border-style: dashed dashed dashed solid;
    border-color: transparent transparent transparent @color;
}
```

使用

```less
    .arrow {
        .triangle(Top, red, 40px);
    }
```



#### `arguments`变量

```less
.border(@a, @b, @c) {
  border: @arguments;
}

.container {
  .border(1px, solid, black);
}

```

编译后的css

```css
.container {
  border: 1px solid black;
}

```

#### 剩余参数

如果想要接收可变数量的参数，我们可以使用 `...` 代表其余的参数。

```less
.mixin(...)         // 匹配第 0-N 个参数
.mixin(@a: 1; ...)  // 匹配第 0-N 个参数
.mixin(@a; ...)     // 匹配第 1-N 个参数
.mixin(@a; @rest...) {
   // @rest 表示在 @a 后的所有参数
   // @arguments 表示所有参数
}
```

- 示例代码

```less
.box-shadow(@rest...) {
  box-shadow: @rest;
}

button {
  .box-shadow(2px; 5px; 1px; #000);
}
```

- 输出代码

```css
button {
  box-shadow: 2px 5px 1px #000;
}
```

#### 命名空间

Mixins 同其他逻辑语言一样，Less 中也有命名空间的概念。

我们可以创建一个类或者 ID 选择器作为一个命名空间，这样我们可以把定义的 Mixins 放在下面，避免与引入的其他文件造成冲突：

```less
.namespace { //命名空间
  .bg {
    color: red;
  }
}
```

**代码解释**：.namespace 就是一个命名空间。

在引用 `.bg` 样式时，我们可以使用以下几种方式：

```less
.namespace > .bg;
.namespace > .bg();
.namespace .bg;
.namespace .bg();
.namespace.bg;
.namespace.bg();
```

**代码解释**：以上几种写法是等效的。

下面看一个完整的例子：

- 输入代码：

```less
.namesapce {
  .bg() {
    color: red;
  }
}

.content {
  .namesapce>.bg();//调用
}
```

- 输出代码：

```css
.content {
  color: red;
}
```

#### 混合函数

##### 什么是混合函数？

> Return variables or mixins from mixins 。——官方定义

> 慕课解释： Mixins 可以作为一个函数使用返回参数或者一个新的 Mixins 。

在混合函数，返回的参数可以当作变量使用，但是返回 Mixins 时比较抽象，大家要多加练习理解。

##### 语法详情

Mixins 不仅可以对样式表进行复用，它也可以看作是一个函数。

类似于 JS 等编程语言中函数，它也具有函数的诸多特征，比如传入参数、返回参数等。

比如我们需要声明一个函数返回 `@width`、`@height` 两个变量，我们可以这样定义一个 Mixins 。

```less
.return() {
  @width:  80%;
  @height: 20px;
}
```

然后我们在使用这两个参数的样式表中引入 `.mixins()` 即可。

```less
.callback {
  .return();
  width:  @width;
  height: @height;
}
```

编译后的结果如下：

```less
.callback {
  width:  80%;
  height: 20px;
}
```

##### 使用场景

混合函数可以对传入参数进行处理后返回，封装判断、循环及计算逻辑，从而达到复用的效果。

##### 返回参数

混合函数可对传入参数进行计算处理。

- 输入代码

```less
.img(@line, @row) {
  @width: ((@row+ @line) / 2);
}

img {
  .img(20px, 50px); // 引入 mixin
  width: @width;    // 使用返回值（@width）
}
```

- 输出代码

```css
img {
  width: 35px;
}
```

##### 返回 Mixins

混合函数可以返回一个 Mixins 并引入使用。

- 输入代码

```less
.return-mixins(@color; @size) { 
  .mixins() { //返回 mixins
    background: @color;
    font-size: @size;
  }
}

#id {
  .return-mixins(red; 28px);
  .mixins(); //引用返回的 mixins
}
```

- 输出代码

```css
#id {
  background: red;
  font-size: 28px;
}
```

##### 小结

1. 在 Mixins 中定义的变量和混合函数是仅对调用方来说是可见的。比如说下面的用法就是错误的：

```less
.a {
  .b(@color) {
    color: @color;
  }
}

.c {
  // 此处会报错，因为 .b() 是属于 .a 的作用域，所以 .c 不能直接调用 .b()
  .b(#fff);
}
```

1. 如果调用方的作用域中，包含相同名称的变量（包括由另一个混合函数定义的变量），则保留原本定义的变量。从父作用域所继承的变量则会被覆盖重写。

- 输入代码

```less
  @width: 300px; // 父作用域变量会被覆盖

  .a() {
    @width: 100px;
  }

  .b {
    .a();
    @width: 200px; // 调用方作用域中的变量需在 mixins 之后才不会被 mixins 中的变量覆盖。
    width: @width;
  }
```

- 输出代码

```css
.b {
  width: 200px;
}
```



### 将规则集传递到混合

在上一个小节中我们学习了混合函数相关的语法特性，或者说是具有返回值的函数。

在 Less 中，我们可以把一个规则集当作一个 mixins 来使用，但是要注意区别两者之间的不同之处。

#### 什么是规则集？

> Allow wrapping of a css block, defined in a mixin 。——官方定义

> 慕课解释：把一个值为规则集的变量作为 Mixins 使用。

#### 语法详情

变量不仅可以作为一个值或路径，也可以是一组 css 属性、嵌套的规则集、媒体声明或存储在变量中的任何其他内容。

当变量是一个规则集合时，我们可以把这个变量看作是一个特殊定义方式的 Mixins 。比如：

```less
@mixins: { background: red; };

img {
  @mixins(); 
}
```

`@mixins` 变量作用此时和 Mixins 是一样的，注意变量后也需要加 “()” 。

编译后：

```css
img {
  background: red;
}
```

#### 使用场景

使用场景主要用于定义一个样式属性不定的 Mixins ，它可以在媒体查询或非支持的浏览器类名中封装一段属性值。规则集可以传递给 Mixins，以便 Mixins 可以包装内容。

比如 `.ie()` 已经定义了媒体查询根类，这样我们就可以使用 Mixins 来封装一段代码。

- 输入代码

```less
.ie(@rules) {
  @media screen and (min-width: 1200) {
    @rules();
  }
  html.lt-ie9 & {
    @rules();
  }
}

div {
  background-color: blue;

  .ie({
    background-color: red;
  });
}

```

- 输出代码

```css
div {
  background-color: blue;
}
@media screen and (min-width: 1200) {
  div {
    background-color: red;
  }
}
html.lt-ie9 div {
  background-color: red;
}

```

#### 示例

##### 返回 Mixins

变量所包含的规则集中也允许含有 Mixins 并将其返回。

- 输入代码

```less
@return: {
  .mixin() {
    background-color: red;
  }
};

.callback {
  @return ();
  .mixin();
}

```

- 输出代码

```css
.callback {
  background-color: red;
}
```

#### 小结

变量的 css 规则集作用域有以下两个特点：

1. 规则集内可以使用调用者内定义的变量和混合。
2. 外部同名的变量优先级高于调用者内部定义的同名变量。

- 输入代码：

```less
@params: #fff;

@data: {
  color: @params;
};

#id {
  @data();
  @params: red;
}

```

- 输出代码

```css
#id {
  color: #fff; // 将会使用外部全局变量
}
```

#### 对比

定义变量时值为 css 规则集（以下简称变量）时这个变量可以看作是一个 Mixins 。但是它与 Mixins 又有什么区别哪？主要有以下几点：

1. 定义的形式不同，Mixins 可以作为一个 ID 选择器或者是类选择器为 demo 节点增加样式，简单来说就是 Mixins 可以出现在编译后的代码中，而变量不能。
2. 作为混合函数时使用范围不同，Mixins 可以返回 Mixins 或变量，而变量只能返回 Mixins 。

```less
  @detached-ruleset: { 
      @color:blue; // @color 属于私有变量
  };

  .caller {
      @detached-ruleset();
      color: @color; // syntax error
  }
```

### 样式导入（Import Styles）

在上一个小节中，有关混合（mixins）的知识已经全部讲解完毕。

在软件工程中代码的拆分机制，可以帮助我们增强代码的可维护性，同样在 Less 中也提供了这种导入导出机制，帮助我们进行样式的拆分。

#### 语法定义

> Import styles from other style sheets——官方定义

> 慕课解释：通过导入指令引入其他样式表的内容 。

导出并不需要特殊的语法，但是导入需要我们使用 `@import` 语法并加上文件名称。此外导入机制仅编译我们用到的代码，并不会编译多余的代码。

#### 语法详情

类似于原生 CSS 语法的导入指令，在 Less 中我们也是通过 `@import` 指令引入其他样式表。

比如引入`base.less`文件：

```less
@import 'base.less';
```

有一点与原生语法不同的是，在 CSS 中 `@import` 规则必须位于所有其他类型的规则之前。但是 Less 可以将 `@import` 语句放在任意位置。

```less
.apple {
  background: red;
}

@import "base.less";
```

> **TIPS**：注意，在这里 Less 中虽然允许我们将导入指令写在任意位置，个人建议同 CSS 语法一样在文件头部导入文件，便于我们快速查阅导入文件的列表并进行修改。

也可以加`url`，这是`CSS`中导入的规则

```less
// @import "./triangle.less";

@import url('./triangle.less');
```

#### 导入文件类型

除了可以引入.less 文件，还可以引导不同类型的文件。

根据导入文件类型的不同，`@import` 语句可能会出现以下几种情形：

1. 如果文件扩展名为 `.css`，该文件将被视为 CSS 文件，`@import` 语句引入规则保持不变。
2. 如果文件扩展名为除 `.css` 和 `.less` 以外的拓展名，`@import` 语句将会将其拓展名视为 `.less` 并将其引入。
3. 文件无扩展名时，`@import` 语句将会默认添加 `.less` 拓展名并引入。

```less
@import "foo";      // 引入 foo.less
@import "foo.js";  // foo.js 会被当作 less 文件引入
@import "foo.css";  // 规则不变
```

#### 使用场景

`@import` 可以帮助我们形成一个个的文件模块，使用文件模块有以下几个优点：

- 提高代码复用性
- 提高代码可维护性

所以说我们可以把复用性较强语法，比如全局变量、mixins 等可以单独提取出来放到一个文件（模块）中。例如我们新建一个 `mixins.less` :

```less
// mixins.less
.mixins1() {
  color: red;
}

.mixins2() {
  color: blue;
}

// componenets.less
@import 'mixins.less'

.color {
    .mixins1();
}
```

### 导入配置（Import Options）

上一个小节中我们学习到了如何提取样式并进行导入，但是在某些情况下我们可能需要对导入的样式文件有一些需求，比如标识一个文件的类型。我们就需要对导入文件进行配置（拓展）从而让编译机制可以识别我们的需求。

#### 语法定义

> Less offers several extensions to the CSS @import CSS at-rule to provide more flexibility over what you can do with external files. ——官方定义

> 慕课解释：Less 为 @import 规则提供了多种拓展，提高了处理外部文件的灵活性 。

#### 语法详情

在上一个章节的中，我们了解到 `@import` 语句默认仅处理拓展名为 `.css`、`.less` 的两类文件。

导入配置可以帮助我们修改 `@import` 默认的行为。

语法：

```less
 @import (keyword) "filename"`
```

`keyword` 的值有以下几种：

- `reference` : 使用 Less 文件但是不输出它；

  使用 `@import(reference)` 导入外部文件，如果没有使用引用的样式，导入的样式将不会添加到编译输出中。

  ```less
  @import (reference) "foo.less"
  ```

- `inline` : 在输出中包含源文件，但不对其进行处理；

  当 CSS 文件可能不兼容时，我们使用此选项。

  因为尽管 Less 已经支持大多数已知的标准 CSS ，但在某些地方它不支持注释，并且不修改 CSS 就不支持所有已知的 CSS hack。

  ```less
  @import (inline) "not-less-compatible.css"
  ```

- `less` : 无论拓展名为什么，都视为 Less 文件；

  使用 `@import (less)` 可以忽略引入文件的拓展名，并将其视为 less 文件。

  ```less
  @import (less) "foo.css"; // 等价于 @import "foo.less"
  ```

- `css` : 无论拓展名为什么，都视为 CSS 文件；

  同 less 配置选项类似，将文件视为 css 文件。

  ```less
  @import (css) "foo.less";// 等价于 @import "foo.css"
  ```

- `once` : 仅引入一次文件 （默认行为）；

  `@import` 语句的默认行为。这意味着该文件仅导入一次，该文件的后续导入语句将被忽略。

  ```less
  @import (once) "foo.less";
  @import (once) "foo.less"; // 该语句将被忽略
  ```

- `multiple` : 多次引入文件；

  使用 `@import (multiple)` 可以多次引入名称相同的文件。这是与 `@import (once)` 行为相反的一个选项。

  - 输入代码：

  ```less
  // foo.less
  .a {
    color: green;
  }
  // main.less
  @import (multiple) "foo.less";
  @import (multiple) "foo.less";
  ```

  - 输出代码：

  ```css
  .a {
    color: green;
  }
  
  .a {
    color: green;
  }
  ```

- `optional` : 找不到文件时停止编译。

  使用 `@import (optional)` 仅在文件存在时才允许导入。如果没有配置可选关键字 `less` ，则在导入找不到的文件时会抛出`FileError`并停止编译。

  ```less
  @import (optional) "foo.less"
  ```

`@import` 语句中可以包含多个配置选项，但必须使用 `,` 分隔开。比如：

```less
@import (optional, reference) "foo.less"
```

#### 使用场景

导入配置适用于修改 `@import` 的默认行为，比如引入特定的样式等。

### 混合守卫（Mixin Guards）

前面的章节中我们已经学习了 mixin 的各种用法，可以说 mixin 是 Less 中的一等公民。为什么这么说哪？因为在 Less 中有关逻辑判断几乎都是通过 mixin 去实现的。例如我们这个章节学习的条件判断就是与 mixin 结合所实现的，让我们一块来了解一下。

#### 语法定义

> Conditional mixins——官方定义

> 慕课解释：根据条件进行判断。

#### 语法详情

在 Mixins 的使用条件需要匹配一个值或算法时，我们可以使用 Less 的条件判断。

与 Java 、Python 等函数式编程语言的条件判断一样，不过语法形式略有差异。

为了与 CSS 原生语言语法形式保持一致，在 Less 中是通过守卫函数的形式而不是 `if/else` ，与 `@media` 的用法类似。我们先来看一段包含条件判断的 Mixins ：

```less
.bg (@color; @width) when (@width >= 50%) {
  background-color: black;
}

.bg (@color; @width) {
  color: @color;
}
```

`when` 关键字引入了守卫机制（条件判断），下面让我们来调用定义好的 Mixins ：

```less
.container1 {
  .bg(red; 40%);
}

.container2 {
  .bg(red; 60%);
}
```

输出代码如下：

```css
.container1 {
  color: red;
}

.container2 {
  background-color: black;
  color: red;
}
```

#### 使用场景

混合守卫适用于 mixins 需要匹配值、运算式、范围的场景，避免 mixin 出现调用错误。

#### 条件判断运算符

条件判断的运算符包含以下几个：

- `>`
- `>=`
- `=`
- `<`
- `=<`

此外，`true` 这个关键字是唯一代表条件为真的值。所以以下的两个 Mixins 是等价的：

此外，`true` 这个关键字是唯一代表条件为真的值。所以以下的两个 Mixins 是等价的：

```less
.truth (@a) when (@a) { ... }
.truth (@a) when (@a = true) { ... }
```

其他的值代表条件都为假：

```less
.a {
  .truth(10); // 10 与 true 不相等，所以不会有任何输出
}
```

我们也可以对两个变量进行比较：

```less
.max (@a; @b) when (@a > @b) { width: @a }
.max (@a; @b) when (@a < @b) { width: @b }
```

#### 条件逻辑运算符

当 Mixins 的判断条件含有两个及两个以上时，我们可以使用逻辑运算符将条件进行关联。

使用 `and` 关键字对两个条件取并集：

```less
.mixin1 (@color) when (iscolor(@color)) and (@color = red) { ... }
```

我们可以使用 `,` 运算符来模拟 `or` 运算符，只要有一个条件为真就可以匹配。

```less
.mixin2 (@width) when (@width > 20%), (@width < 80%) { ... }
```

使用 `not` 关键字代表否定条件：

```less
.mixin3 (@width) when not (@b > 10%) { ... }
```

#### 类型检查函数

我们可以使用 Less 提供的类型检查函数对变量进行判断：

```less
.mixin1 (@color) when (iscolor(@color)) { ... }
.mixin2 (@url) when (isurl(@url)) { ... }
```

主要有以下几种基础的类型检查函数：

- `iscolor`
- `isnumber`
- `isstring`
- `iskeyword`
- `isurl`

如果要检查某个值是否除作为数字外还包含在特定单位中，还可以使用：

- `ispixel`
- `ispercentage`
- `isem`
- `isunit`

#### default()函数

default() 函数可根据已创建的 Mixins 条件来形成该条件的补集。

```less
.mixin (@width) when (@width > 10%) { ...  }
.mixin (@width) when (default()) { ... } // default()等价于 @width <= 10%
```

#### 小结

本章节介绍了混合守卫，在 Less 中我们可以使用混合守卫（即 when函数）代替 `if` ， 如果需要使用 `else` 即需要使用到 default() 函数创建多个 mixins 进行匹配。

### CSS守卫（CSS Guards）

在上一个章节中我们学习了混合守卫，但是在某些场景下我们不只是需要对 Mixin 进行条件判断，css 的样式类也是需要进行条件判断的，此时我们就需要使用到 CSS 守卫了。注意，该语法是在 v1.5.0 版本之后添加的，建议大家跟我下载同样的版本进行学习。

#### 语法定义

> 官方定义： “if”'s around selectors.

> 慕课解释： 类似与 Mixins 守卫，在选择器中使用类似于 “if” 的判断语句。

#### 方法详情

`Guards` 也可以应用于css选择器，它是用于声明 mixin 然后立即调用它的语法糖。

例如，在 v1.5.0 之前我们只能这样写去定义一个 CSS 守卫：

```less
.style() when (@select = true) {
  button {
    color: white;
  }
}

.style();
```

但是现在我们可以直接在选择器上应用 `guard` ，例如：

```less
button when (@select = true) {
  color: white;
}
```

我们还可以通过将其与 `&` 功能结合使用来实现对多个 `guard` 进行分组。也就是说我们可以同时对多个样式类进行条件判断。

```less
& when (@select = true) {
  button {
    color: white;
  }
  span {
    color: blue;
  }
}
```

#### 小结

本章节我们介绍了 CSS 守卫，CSS 守卫本质上是对混合守卫封装的一个语法糖，让选择器使用 Guards 更加方便，使用场景及其他用法可参考混合守卫。

### 循环（Loops）

在编程中我们最常用的逻辑处理除了条件判断之外，其次就是循环了。在上一个小节中我们已经学习了条件判断，这个小节我们具体学习一下循环，在其他的编程语言中我们都是通过 for 循环的结构去实现的循环结构。但是在 Less 中并没有这么一种语法，而是通过自身调用从而实现的循环递归。同时我们需要运用之前我们学习到的条件判断从而跳出循环。

#### 语法定义

> 官方定义： Creating loops .

> 慕课解释： 创建循环。

#### 方法详情

在 Less 中，我们可以通过 mixins 结合 guard 函数自身调用从而达到类似于 for 循环的效果，创建各种循环迭代结构。

例如：

```less
@list:a,b;

.for(@counter) when (@counter < length(@List)+1) {
  .background-@{counter} {
    background-image: url("./images/@{extract(@list,@counter)}.png")
  }
  .for(@counter+1)
}

.for(1)
```

上述的代码中，`.for` 通过 `when()` 函数控制 `@counter` 参数并调用自身，达到了类似于循环的效果，每一次循环都会返回一个结果。

输出代码如下：

```css
.background-1 {
    background-image: url("./images/a.png")
}

.background-@{counter} {
    background-image: url("./images/b.png")
}
```

#### 使用场景

循环主要用于动态创建多个样式类或多个属性值。

#### 示例

我们来使用递归循环创建一个 CSS 网格类：

- 输入代码：

```less
.generate-columns(@n, @i: 1) when (@i =< @n) {
  .column-@{i} {
    width: (@i * 100% / @n);
  }
  .generate-columns(@n, (@i + 1));
}

.generate-columns(4);
```

`.generate-columns` 一共循环了 4 次，每一次循环都会创建一个 `.column-@{i}` 类及其对应的样式类。当然我们也可以通过这种方式生成多个属性值相同的样式类。

- 输出代码

```less
.column-1 {
  width: 25%;
}
.column-2 {
  width: 50%;
}
.column-3 {
  width: 75%;
}
.column-4 {
  width: 100%;
}
```

#### 小结

本章节我们介绍了 Less 中的循环，循环（loops）其实是 minxin 和 guard 结合的一种语法。在循环之前我们可以创建一个列表保存需要循环的数据，合理的结合使用可以达到循环迭代的效果。

### 合并（Merge）

从这个小节开始我们开始学习有关属性操作有关的语法，本章节我们主要介绍属性合并的使用方法。属性合并主要为了解决引入 mixins 时存在两个同样的属性值冲突时的处理方式。

默认情况下两个属性值会同时编译到目标样式类中，如果需要将属性值进行合并整合就需要用到我们本章节学习的知识。

#### 语法定义

> 官方定义： Combine properties .

> 慕课解释： 合并属性值 。

#### 方法详情

合并功能允许将多个属性中的值合并到一个属性的列表中，值用 `,` 或者空格分隔开。

#### 使用场景

合并（merge）主要应用于列表属性的整合，比如 `box-showdow`、`transfrom` 等属性。

#### 示例

##### 逗号分隔

使用合并功能之前需定义一个 mixin 并在需要合并的属性后加上 `+` ，然后在引入 minxin 后在被合并的属性后也加上 `+` 。

- 输入代码

```less
.mixin() {
  box-shadow+: 0 0 10px #333;
}

div {
  .mixin();
  box-shadow+: 0 0 20px black;
}
```

- 输出代码

```css
div {
  box-shadow: 0 0 10px #333, 0 0 20px black;
}
```

##### 空格分隔

使用步骤同逗号分隔，将属性后的符号改为 `+_` 即可。

- 输入代码

```less
.mixin() {
  transform+_: scale(2);
}

div {
  .mixin();
  transform+_: rotate(15deg);
}
```

- 输出代码

```css
div {
  transform: scale(2) rotate(15deg);
}
```

#### 小结

本章节我们介绍了合并，合并主要用于相同属性的合并联接，为了避免任何意外的联接，合并要求在每个联接的属性声明上使用显式的 `+` 或 `+_` 标志。

### 父选择器（Parent Selectors）

上一个章节中我们学习了属性的合并，这个章节我们学习一个有关选择器的操作 —— 父选择器。

其功能与其名称相同，就是用符号代表其父选择器。

#### 语法定义

> 官方定义： Referencing parent selectors with `&` 。

> 慕课解释： 用 `＆` 符号引用父选择器。

#### 语法详情

在嵌套结构中 `&` 表示父选择器。比如：

```less
a {
  color: blue;
  &:hover {
    color: green;
  }
}
```

在上述代码中，`:hover` 前面加上了 `&` 符号，编译后则等同于 `a:hover` 。

输出代码如下：

```css
a {
  color: blue;
}

a:hover {
  color: green;
}
```

嵌套结构中默认编译规则为 `.parentSelector .childSelector` ，即父选择器和子选择器之间使用空格分隔开的。

所以在未添加 `&` 的情况下， `:hover` 输出的样式选择器会是 `a :hover` ， 这与我们预期的结果是不一致的。

#### 使用场景

使用 `&` 运算符可以满足我们使用默认规则以外的其他方式组合嵌套的需求，在修改类或伪类并应用于现有选择器时最常用。

#### 示例

##### 多个 `&` 组合

我们可以使用多个 `&` 运算符并使用其他运算符连接起来，便于重复引用父选择器而无需重复其名称。

- 输入代码

```less
.link {
  & , & {
    color: red;
  }

  && {
    color: blue;
  }

  &, &ish {
    color: cyan;
  }
}
```

- 输出代码

```css
.link , .link {
  color: red;
}

.link.link {
  color: blue;
}

.link, .linkish {
  color: cyan;
}
```

#### 更改选择器顺序

在某些情况下我们需要将选择器放在继承的（父）选择器之前。 此时可以通过将 `&` 运算符放在当前选择器后面来完成。

- 输入代码

```less
.header {
  border-radius: 5px;
  .no-borderradius & {
    background-image: url('images/button-background.png');
  }
}
```

- 输出代码

```css
.header {
  border-radius: 5px;
}

.no-borderradius .header {
  background-image: url('images/button-background.png');
}
```

#### 排列组合

`&` 运算符可用于生成逗号分隔列表中选择器的所有可能的排列组合。

- 输入代码

```less
p, a, ul, li {
  border-top: 2px dotted #366;
  & + & {
    border-top: 0;
  }
}
```

将会输出所有可能的 `16` 中排列组合。

- 输出代码

```css
p,
a,
ul,
li {
  border-top: 2px dotted #366;
}
p + p,
p + a,
p + ul,
p + li,
a + p,
a + a,
a + ul,
a + li,
ul + p,
ul + a,
ul + ul,
ul + li,
li + p,
li + a,
li + ul,
li + li {
  border-top: 0;
}
```

#### Tips

在嵌套结构中，`&` 运算符代表所有父选择器，而不仅仅是最接近的父选择器，比如：

- 输入代码

```less
.grand {
  .parent {
    & > & {
      color: red;
    }
  }
}
```

上述代码中的 `&` 运算符不仅仅指的是 `.parent` 这个父选择器，而是 `.grand .parent` 。

- 输出代码

```css
.grand .parent > .grand .parent {
  color: red;
}
```

#### 小结

这个章节我们介绍了父选择器的使用，父选择器就是用 `&` 符号去表示所在区域的父选择器，是一种父选择器的替代写法，可以组合出多种使用方法。

### 杂项函数(1)

从本章开始，我们开始学习 Less 内置函数有关的知识，Less 中内置的函数可以帮助我们解决很多计算或者判断的问题。

对于函数的学习我建议可以现大致浏览一下有哪些函数以及他们对应的功能和用途。

等到我们用到的时候可以回过头来翻阅函数的参数以及详细的用法，具体使用的场景可以帮助我们快速理解函数的用途。

#### 杂项函数简介

杂项函数主要用于处理图片路径、颜色等途径。

#### color 函数

> 函数用途： 用于解析颜色，将颜色值的字符串处理为可以使用的颜色值。

参数： `string` 指定颜色值的字符串
返回值： `color` 颜色值
语法： `color(param: string) => value`

- 输入代码

```less
.color {
  color: color("#fff");
}
```

- 输出代码

```css
.color {
  color: #fff;
}
```

####  image-size 函数

> 函数用途： 用于获取图片文件的尺寸。

参数： `string` 获取尺寸的文件
返回值： 尺寸（图片长和宽）
语法： `url(path:string) => value`

- 输入代码

```less
.img {
  background:url("file.png");
  background-repeat:no-repeat;
  background-size: image-size("file.png");
}
```

- 输出代码

```css
.img {
  background:url("file.png");
  background-repeat:no-repeat;
  background-size: 10px 10px;
}
```

#### image-width 函数

> 函数用途： 获取图片文件宽度。

参数： `string` 获取尺寸的宽度
返回值： 宽度（单位为 `px` ）
语法： `image-width(path: string) => value`

- 输入代码

```less
.img {
  width: image-width("file.png");
}
```

- 输出代码

```css
.img {
  width: 10px;
}
```

####  image-height 函数

> 函数用途： 获取图片文件长度。

参数： `string` 获取尺寸的长度
返回值： 长度（单位为 `px` ）
语法： `image-height(path: string) => value`

- 输入代码

```less
.img {
  height: image-height("file.png");
}
```

- 输出代码

```css
.img {
  height: 10px;
}
```

#### convert 函数

> 函数用途： 单位转换

第一个参数包含一个带单位的数字，第二个参数包含一个单位。

如果两个单位兼容，则进行单位转换。如果它们不兼容，则第一个参数将按原样返回。

支持转换的单位如下：

- lengths(长度单位): `m`, `cm`, `mm`, `in`, `pt` , `pc`
- time(时间单位): `s` , `ms`
- angle(角度单位): `rad` , `deg` , `grad` , `turn`

参数：

- `number` : 含有单位的浮点数。
- `identifier`, `string` 或者 `escaped value`: 单位 。

返回值： `number`

- 输入代码

```less
.convert {
  time: convert(9s, "ms");
  lenght: convert(14cm, mm);
  unkow: convert(8, mm); // 无法转换返回原值
}
```

- 输出代码

```css
.convert {
  time: 9000ms;
  lenght: 140mm;
  unkow: 8; // 无法转换返回原值
}
```

#### data-uri 函数

> 函数用途： 将内联资源转换为 base64 或者 text/html 格式 。

参数：

- `mimetype` ： mime 类型字符串（可选）。
- `url` ： 内联文件的路径。

如果没有 `mimetype` ，`data-uri` 函数将从文件名后缀中猜测出来。 文本和svg文件编码为 utf-8，其他所有文件编码为 base64。

如果提供了mimetype，且 mimetype 参数以 base64 结尾，则该函数将使用 base64 转换图片。 例如，`image / jpeg; base64`被编码为 `base64` ，而 `text / html` 被编码为 `utf-8` 。

> 如果ieCompat选项打开，资源过大，或者在浏览器中使用该功该函数则会回退为url()。

- 输入代码

```less
.img {
  // 1
  background: data-uri('../data/image.jpg');
  // 2
  background: data-uri('image/jpeg;base64', '../data/image.jpg');
  // 3
  background: data-uri('image/svg+xml;charset=UTF-8', 'image.svg');
}
```

- 输出代码

```css
.img {
  // 1
  background: url('data:image/jpeg;base64,bm90IGFjdHVhbGx5IGEganBlZyBmaWxlCg==');
  // 2
  background: url('data:image/jpeg;base64,bm90IGFjdHVhbGx5IGEganBlZyBmaWxlCg==');
  // 3
  background: url("data:image/svg+xml;charset=UTF-8,%3Csvg%3E%3Ccircle%20r%3D%229%22%2F%3E%3C%2Fsvg%3E");
}
```

### 杂项函数(2)

该章节的函数主要用于单位的修改以及某个含有单位值的单位获取。

#### default 函数

> 函数用途： 仅在混合守卫的条件中使用，当无其他 mixin 匹配时返回 `true` ，反之则返回 `false` 。

在 Mixins 中我们可以通过 `default()` 函数结合其他函数对 Mixins 进行保护。

- 输入代码

```less
.x {
  .m(red) {
    case: darkred;
  }
  .m(@x) when (iscolor(@x)) and (default()) {
    default-color: @x;
  }
  .m("foo") {
    case: I am "foo";
  }
  .m(@x) when (isstring(@x)) and (default()) {
    default-string: and I am the default;
  }

  &-blue {
    .m(red);
  }
  &-green {
    .m(green);
  }
  &-foo {
    .m("foo");
  }
  &-baz {
    .m("baz");
  }
}

```

- 输出代码

```css
.x-blue {
  case: darkred;
}

.x-green {
  default-color: #008000;
}

.x-foo {
  case: I am 'foo';
}

.x-baz {
  default-string: and I am the default;
}
```

#### unit 函数

> 函数用途： 更改或删除尺寸的单位。

参数：

- `dimension`: 填入一个数值，带单位或者不带
- `unit`:（可选参数） 填入需要转换的单位，如果未传入，则移除数值的单位。

语法： `unit(dimension, ?unit) => value`

- 输入代码

```less
.unit {
  width: unit(5px, rem);
  height: unit(50px)
}
```

- 输出代码

```css
.unit {
  width: 5rem;
  height: 50
}
```

#### get-unit 函数

> 函数用途： 返回数值的单位。如果参数包含带单位的数字，则该函数返回其单位。不带单位的参数将导致返回一个空值。

参数：带或不带单位的数字。
语法：`get-unit(dimension) => value`

- 输入代码

```less
.get-unit {
  unit: get-unit(5px)
}
```

- 输出代码

```css
.get-unit {
  unit: px
}
```

### 字符串函数

#### 字符串函数简介

字符串函数主要用于字符串的转码、替换、格式化等方面，可以帮助我们快速简便的处理字符串。

#### escape 函数

> 函数用途： 将URL编码应用于在输入字符串中找到的特殊字符。

**tips:**

- 以下这些字符不会参与编码：`,` , `/` , `?` , `@` , `&` , `+` , `'` , `~` , `!` , `$`
- 常见的编码字符： `<space>` , `#` , `^` , `(` , `)` , `{` , `}` , `|` , `:` , `>` , `<` , `;` , `]` , `[`, `=`

参数： `string` 需要转义的字符串。
返回值： 转义后的字符串，未带引号。
语法： `escape(param) => value`

- 输入代码

```less
.escape {
  string: escape('a=1')
}
```

- 输出代码

```css
.escape {
  string: a%3D1
}
```

#### e 函数

> 函数用途： CSS转义，替换为~"value"语法。

该函数可将字符串去除引号并返回。它可用于将输出无效的 CSS 值转换为 CSS 语法，或转换 Less 不能识别的专有语法。

参数：`string` 需要转义的字符。
返回值： `string` 去除引号后的转义字符。
语法： `e(param) => value`

- 输入代码

```less
.img {
  filter: e("ms:alwaysHasItsOwnSyntax.For.Stuff()");
}
```

- 输出代码

```css
.img {
  filter: ms:alwaysHasItsOwnSyntax.For.Stuff();
}
```

**tips:**

该函数还接受含 `~` 、`""` 的值和数字作为参数。其他类型的参数会报错。

#### % format 函数

> 函数用途： 格式化字符

第一个参数是带有占位符的字符串。所有占位符开始百分号 `%` 后跟字母 `s`，`S` ，`d` ，`D` ，`a` ，或`A` 。其余参数包含替换占位符的表达式。如果需要输出百分比符号，请用另一个百分比将其转义 `%%` 。

如果需要将特殊字符转义为 `utf-8` 转义码，请使用大写占位符。该函数将转义除以外的所有特殊字符 `()'~!`。空格编码为 `%20` 。小写占位符保留原样的特殊字符。

占位符：

1. `d`，`D` ，`a` ，`A` 可以通过任何种类的参数（颜色，号码，转义值，表达式，…）的替换。如果将它们与字符串结合使用，则将使用整个字符串-包括引号。但是，引号按原样放置在字符串中，不能用“/”或类似符号进行转义。
2. `s` ，`S` 可以用任何表达式替换。如果将它与字符串一起使用，则仅使用字符串值-省略引号。

参数：

- `string` ： 带占位符字符串。
- `anything`* : 用于替换占位符的值。

返回值：格式化后的字符串。

语法： `%(string, anything) => value`

- 输入代码：

```less
.format {
  format-a-d: %("repetitions: %a file: %d", 1 + 2, "directory/file.less");
  format-a-d-upper: %('repetitions: %A file: %D', 1 + 2, "directory/file.less");
  format-s: %("repetitions: %s file: %s", 1 + 2, "directory/file.less");
  format-s-upper: %('repetitions: %S file: %S', 1 + 2, "directory/file.less");
}
```

- 输出代码：

```css
.format {
  format-a-d: "repetitions: 3 file: "directory/file.less"";
  format-a-d-upper: "repetitions: 3 file: %22directory%2Ffile.less%22";
  format-s: "repetitions: 3 file: directory/file.less";
  format-s-upper: "repetitions: 3 file: directory%2Ffile.less";
}
```



#### replace 函数

> 函数作用： 替换字符串中的文本.

参数：

- `string` ：被替换的字符。
- `pattern`： 需搜索的字符串或正则表达式。
- `replacement`： 用于替换匹配模式的字符串。
- `flags`：（可选）正则表达式标志。

返回值： 替换后的字符串。
语法： `replace(string, pattern, replacement, ?flags) => value`

- 输入代码：

```less
.replace {
  value: replace("Hello, Mars?", "Mars?", "Earth!");
}
```

- 输出代码：

```less
.replace {
  value: "Hello, Earth!";
}
```

### 列表函数

在 Less 中一个变量也可表示一个列表，列表用 `,` 分隔开， 类似于其他语言中的数组，该章节的函数就是为了操作列表所产生的，比如返回列表长度、获取指定元素的等。

####  length 函数

> 函数作用：返回值列表中的元素个数。

参数：`list` 用逗号或空格分隔的值列表。

返回值： 列表中元素的整数。
语法： `length(list) => value`

- 输入代码

```less
@list: "banana", "tomato", "potato", "peach";

.fruit {
  number: length(@list);
}
```

- 输出代码

```css
.fruit {
  number: 4;
}
```

#### extract 函数

参数：

- `list` 用逗号或空格分隔的值列表。
- `index` 一个整数，它指定要返回的列表元素的位置。

返回值：列表中指定位置的值。
语法： `extract(list) => value`

- 输入代码

```less
@list: apple, pear, coconut, orange;

.get-fruit {
  value: extract(@list, 3);
}
```

- 输出代码

```css
.get-fruit {
  value: coconut;
}
```

### 数学函数(1)

#### 数学函数简介

数学函数主要用于数组的处理，比如数字的取整四舍五入、三角函数等数学运算。

#### ceil 函数

> 函数作用：取整，将浮点数向下舍入到下一个整数。

参数： `number` 浮点数。
返回值： 整数。
语法： `ceil(number) => value`

- 输入代码

```less
.ceil {
  rows: ceil(2.3);
}
```

- 输出代码

```css
.ceil {
  rows: 3;
}
```

#### floor 函数

> 函数作用：取整，将浮点数向上舍入到上一个整数。

参数： `number` 浮点数。

返回值： 整数。
语法： `floor(number) => value`

- 输入代码

```less
.floor {
  rows: floor(2.8);
}
```

- 输出代码

```css
.floor {
  rows: 2;
}
```

#### percentage 函数

> 函数作用：将浮点数转换为百分比字符串。

参数：`number` 浮点数。

返回值： `string` 百分比字符串。
语法：`percentage(number) => value`

- 输入代码

```less
.container {
  width: percentage(0.5);
}
```

- 输出代码

```css
.container {
  width: 50%;
}
```

#### round 函数

> 函数作用： 按需舍入。遵循四舍五入。

参数：

- `number`：浮点数。
- `decimalPlaces`：（可选）要舍入的小数位数。默认为 `0`。

返回值： `number`
语法： `round(number) => value`

- 输入代码

```less
.round {
  rows: round(1.67);
  rows: round(1.67, 1);
}
```

- 输出代码

```css
.round {
  rows: 2;
  rows: 1.7;
}
```

#### sqrt 函数

> 函数作用：计算数字的平方根。保持单位不变。

参数：`number` 浮点数。

返回值： `number`
语法： `sqrt(number) => value`

- 输入代码

```less
.img {
  width: sqrt(25px);
}
```

- 输出代码

```css
.img {
  width: 5px;
}
```

#### abs 函数

> 函数作用：计算数字的绝对值。保持单位不变。

参数：`number` 浮点数。

返回值： `number`
语法： `abs`

- 输入代码

```less
.container {
  width: abs(25px);
  height: abs(-18.6%);
}
```

- 输出代码

```css
.container {
  width: 25px;
  height: 18.6%;
}
```

#### abs 函数

> 函数作用：计算数字的绝对值。保持单位不变。

参数：`number` 浮点数。

返回值： `number`
语法： `abs`

- 输入代码

```less
.container {
  width: abs(25px);
  height: abs(-18.6%);
}
```

- 输出代码

```css
.container {
  width: 25px;
  height: 18.6%;
}
```

#### asin 函数

> 函数作用：计算反正弦函数

返回以弧度表示的数字，例如 `-π/2` 和之间的数字 `π/2`。

参数：`number` [-1, 1]间隔中的浮点数。

返回值： `number`
语法： `asin(number) => value`

- 输入代码

```less
.animation {
  rotate: asin(-0.8414709848078965);
}
```

- 输出代码

```css
.animation {
  rotate: -1rad;
}
```

#### cos 函数

> 函数作用：计算余弦函数。

假定数字的弧度不带单位。

参数：`number` 浮点数。

返回值： `number`
语法： `cos(number) => value`

- 输入代码

```less
.cos {
  number: cos(1);
}
```

- 输出代码

```css
.cos {
  number: 0.5403023058681398;
}
```

### 数学函数(2)

该章节函数包括三角函数及 π 值获取的函数等。

#### acos 函数

> 函数作用：计算反余弦（余弦的倒数）函数。

返回以弧度为单位的数字，例如 `0` 到 `π` 之间的数字。

参数：`number` 从[-1，1]间隔开始的浮点数。

返回值： `number`
语法： `acos(number) => value`

- 输入代码

```less
.animation {
  rotate: acos(0.5403023058681398);
}
```

- 输出代码

```css
.animation {
  rotate: 1rad;
}
```

#### tan 函数

> 函数作用：计算切线函数。

假定数字的弧度不带单位。

参数：`number` 浮点数。

返回值： `number`
语法： `tan(number) => value`

- 输入代码

```less
.table {
  rows: tan(1deg);
}
```

- 输出代码

```css
.table {
  rows: 0.017455064928217585;
}
```

#### atan 函数

> 函数作用：计算反正切（反正切）函数。

返回以弧度表示的数字，例如`-π/2`和之间的数字`π/2`。

参数：`number` 浮点数。

返回值： number
语法： `atan(number) => value`

- 输入代码

```less
.animation {
  rotate: atan(0);
}
```

- 输出代码

```css
.animation {
  rotate: 0rad;
}
```

#### pi 函数

> 函数作用：返回 π 值

参数： `none`

返回值： `number`
语法： `pi() => value`

- 输入代码

```less
@width: 5px;
.pi {
  height: 2*pi()*@width;
}
```

- 输出代码

```css
.pi {
  height: 31.41592653589793;
}
```

#### pow 函数

> 函数作用：返回提高到第二个参数的幂的第一个参数的值。

返回值的尺寸与第一个参数的尺寸相同，而第二个参数的尺寸将被忽略。

参数：

- `number`：`base` 浮点数。
- `number`：`指数` 浮点数。

返回值： `number`
语法： `pow(number, number) => value`

- 输入代码

```less
.pow {
  border: pow(0px, 0cm);
}
```

- 输出代码

```css
.pow {
  border: 1px;
}
```

#### mod 函数

> 函数作用：返回第一个参数模数第二个参数的值。

返回值的尺寸与第一个参数的尺寸相同，而第二个参数的尺寸将被忽略。该功能还可以处理负数和浮点数。

参数：

- `number`：一个浮点数。
- `number`：一个浮点数。

返回值： `number`
语法： `mod(number, number) => value`

- 输入代码

```less
.mod {
  height: mod(11px, 6cm);
}
```

- 输出代码

```css
.mod {
  height: 5px;
}
```

#### min函数

> 函数作用：返回一个或多个值中的最小值。

参数：`value1, ..., valueN` 一个或多个要比较的值。

返回：`最小值`。
语法： `min(number,...) => value`

- 输入代码

```less
.grid {
  rows: min(5, 10);
}
```

- 输出代码

```css
.grid {
  rows: 5;
}
```

#### max 函数

> 函数：返回一个或多个值中的最大值。

参数：`value1, ..., valueN` 一个或多个要比较的值。

返回：`最大值`。
语法： `max(number,...) => value`

- 输入代码

```less
.grid {
  rows: max(5, 10);
}
```

- 输出代码

```css
.grid {
  rows: 10;
}
```

# `Less`应用

## 栅格





 
