---
title: JavaScript从基础到进阶
date: 2022-09-16 09:58:44
cover: false
tags:
- javascript
categories: 'javascript'
typora-root-url: js从基础到进阶
---



# 了解前端与准备

## 前端发展史：全面拥抱大前端时代

### `web1.0`时代：静态网页

- 1989年，在欧洲粒子物理实验室`Tim Berners—Lee`（伯纳斯·李）提出：个人计算机上访问大量的科研文献，并建议在文档中链接其他文档=>“**WEB原型**”
- 1994年，万维网(`W3C`) 成立，网景推出了第一版`Navigator`浏览器, `HTML`也发布了第二代版本，`TIM`的好基友也设计了`CSS`...所以我们把1994年称为“**前端历史的起点**”
  - `H5C3`去官网看：[Tutorials and Courses - W3C](https://www.w3.org/2002/03/tutorials.html)
- 1995年，网景工程师`Brendan Eich`花 了10天时间设计了`JavaScript`语言, 1996年微软发布了`JScript` (和`JS`有一些差异)，同时拉开了`Navigator和Internet Explorer` 浏览器大战的序幕(到2002年`IE`完胜，占据全世界96%的市场份额)。
  - 后期浏览器兼容性问题的起源
- 为了让各大浏览器统一编程规范，1997年6月`ECMA` (欧洲计算机制造联合会)以`JavaScript`语言为基础制定了`ECMAScript`标准规范`ECMA-262`，从此浏览器厂商都是按照这个规范来开发自己的浏览器产品。
- 1999年12月`ES3`发布，到2011年6月`ES5`发 布(2007年 的`ES4`夭折:改动太大)，`ES3`占据了10年历程， 也是`JS`语言的基础。2015年6月`ES6`发布 (但是由于之后规定每年发布一个新的版本，所以后改名`ES2015`: `let、 const、 Arrow function、 Class、 Module、Promise、Iterator、 Generator、 Set、 Map、 async、 Symbol、 Proxy`.... )，2016年6月对2015版本增强的2016版本发布，此后相继有`ES2017`、`ES2018`...
- 同样`HTML`也在2014年10月发布了第五代版本，2011年`CSS`也发布了第三代版本，此时前端基础的技术栈就稳固下来。

### `web2.0`时代：动态网页的崛起

1995年之前，`JS`只用来做一些简单的`DOM`修改，`WEB` 页面都是静态的(显示静态文本和图片)，为了让`WEB`页面更具备活力(例如:动态展示数据)，1995年`PHP`诞生， 1996年`JSP`诞生，1996 年`ASP`诞生，2002年`ASP.NET`诞生...这些服务器端页面技术实现了`WEB`页面的动态化，从此`WEB2.0`时代到来。



#### 服务端渲染

- 服务器接收到请求后
  - 1.找到需要访问的资源文件
  - 2.从数据库中基于`SQL`语句，查询出需要的数据
- 数据库存放的是数据
- 服务器渲染:把页面代码和数据结合在一起，生成有结构样式和数据的页面，把渲染完成的页面返回给客户端浏览器
- 前端开发：(网页制作)
  - 写页面和样式
- 后台开发:
  - 1.会写数据绑定的代码
  - 2.操作数据库
  - 3.操作服务器
  - 4.数据结构和算法
  - 5.服务器分布式(缓存和并发)
  - ..

- 弊端
  - 1.服务器承受压力过大
  - 2.同步非异步刷新
    - 页面中某一个数据想要更改，只能重新刷新整个页面(全局刷新)
  - 3.不利于团队协作开发
    - 后台开发的任务量过大(网页制作任务量少) ，代码过于臃肿，两种角色很难实现同时任务开发

### `AJAX`时代

> 详见《Ajax&Axios》

[ `AJAX`时代: 前后端分离的雏形，异步渲染大显神通]

在Web最初发展的阶段，前端页面要想获取后台信息需要刷新整个页面，这是很糟糕的用户体验。`Google`分 别在`2004`年和`2005`年先后发布了两款重量级的Web产品: `Gmail`和`Google Map`。 
这两款`Web`产品都大量使用了`AJAX`技术，不需要刷新页面就可以使得前端与服务器进行网络通信，所以`AJAX`是一项革命性的技术，颠覆了用户体验。

到2013年/2014年，随着移动端`H5`的崛起，高性能的WEB体验是重中之重，国内大部分项目都已经改为“前后端分离”模式，这也奠定了前端开发二分天下的局面。导致到后期，跨域策略请求方案(`JSONP、 IFRAME、 CORS、DOMAIN、POXY、SCOKET`... )以及FETCH等 新通信方案不断的崛起。

#### 客户端渲染

- 服务器一般有多个
  - `WEB`服务器：
    - 接受客户端请求，把找到的静态资源文件返回给客户端
  - 数据服务器：
    - 客户端基于`AJAX ( JSONP、CROSS、 WEBPACK PROXY... )`或者`FETCH`，向数据服务器发送请求
    - 数据服务器操作数据库并向客户端返回数据
    - 客户端获取数据后，基于模板字符串等手段，把数据拼成需要展示的结构，放到容器中
  - 资源服务器
    - 一般放图片资源
- 前端工程师
  - 1.写页面`H5/CSS3`
  - 2.写人机交互`js`及框架插件
  - 3.数据请求和绑定`ajax`....
  - 4.操作系统`linux`
- 后台
  - 1.业务逻辑处理
  - 2.数据处理(数据库)
  - 3.数据结构和算法(服务器负载均衡)
  - 4.操作系统

### `App`

#### 原生`APP` ( `Native App` )

`object-c / java-native /swift`

优势:

- 1.性能好
- 2.功能强大(可以调用手机软件硬件)

弊端:

- 1.不能跨平台，成本大
- 2.不能同步



#### Web App ( H5页面)

响应式布局开发

> 浏览器
>
> > 网址
> >
> > > `HTML5`页面
> > >
> > > - 优势
> > >   - 1.跨平台
> > >   - 2.及时更新
> > > - 弊端:
> > >   - 1.性能相对不好
> > >   - 2.功能没有那么强大



#### `Hybrid`混合`APP`开发（99.99999%）

> `Native App`壳子（安卓/`IOS`写壳子）
>
> > `webview` (`webkit`内核)
> >
> > 通过`JSBridge`，可以调用壳子的方法
> >
> > > `H5`
> > >
> > > 壳子都不用原生（安卓/`IOS`）写了
> > >
> > > - `React-Native`
> > > - `Flutter`
> > >   - `Dart`语言
> > > - `uni-app`
> > >   - 一套代码，啥平台都有

#### `NODE`崛起

[ `NODE`崛起:` JS`成为最热门全栈开发技术] I

2009年，`Ryan`利 用`Chrome`的`V8`引擎打造了基于事件循环的异步I/0框架-`Node.js`诞生。

`NODE`特点：基于事件循环的异步I/0框架，能够提高1/0吞吐量;单线程运行，能够避免了多线程变量同步的问题；使得`JS`可以编写后台代码，前后端编程语言统一。
2010年1月，`NPM`作为`Node. js`的包管理系统首次发布。前`NPM` 具有40万左右的模块，是世界上最大的包模块管理系统。



#### 前端未来发展预估

- A：小程序是企业产品的重要组成部分
- B： `IOS`和安卓开发逐步被淘汰
- C： `VR/AI`最终转为B端(`JS`，尤其是`webGL`、`canvas`、`three. js`等是`3D`虚拟交互的主要实现技术)
- D：`H5`游戏/小游戏的热度会提高(白鹭`JS`引擎)
- E：`NODE.JS`还会迎来下一个高潮
- ...

大前端时代已经到来!



### 当下前端开发的技术体系

#### 第一阶段: `HTML (5) + CSS (3) `

技术要点：`HTML5`、`CSS3`、响应式布局(`rem/flex/@media`等)、`Hybrid`混合`APP`开发、微信二次开发、小程序开发、`ReactNative`开发、`Flutter`、`uni-app`...
特殊说明:	

- `Hybrid`、微信开发、小程序开发、`React Native`开发等，这些都需要有`JS`和框架编程的基础;	
- `H5`不仅仅是标签，还需要掌握常用的`API`以及`video`和`audio`等,例如：`locaIstorage`、`webscoket`、`getCurrentPosition`等;

书籍：

- 《`HTML5`》秘籍

- 《`CSS`权威指南》
- 《图解`CSS3`》
- 《`React Native`》入门与实战
- ...

#### 第二阶段: JS包括ES6核心原理

JS堆栈内存、闭包作用域、浏览器词法解析(v8渲染机制原理)、面向对象和THIS处理(主要是独立封装组件和插件，研究常用类库的源码) ;

ES6基础语法(包括class 类的继承封装和多态)、ES6中 的Promise (及Promise A+规范)、Generator生 成器函数等深入用法;

同步异步编程(包括运行机制和微任务、宏任务，以及实战应用)

常用的编程思想和设计模式:函数的防抖和节流、柯理化函数、惰性函数、单例设计模式、发布订阅模式、Promise设计模式等

DOM性能优化(重排和重绘的优化)、DOM事件

前端编程常规算法:去重、冒泡排序、插入排序、快速排序、递归等

书籍：

- 《JavaScript权威指南》
- 《你不知道的JavaScript》
- 《JavaScript高级程序设计》
- 《ES6标准入门》

#### 第三阶段: AJAX和HTTP

技术要点: ajax原理、ajax异步解决方案(promise)、axios; (包括自己封装promise版ajax库)、fetch及封装处理、jquery中的ajax操作和库的封装等

跨域解决方案及实现原理: jsonp、 cors、 webpack proxy (scoket.io)、document. domain、window. name+ iframe、postMessage 等

HTTP报文(常用的响应请求头实战应用技巧)、HTTP (TCP) 传输流程(包括三次握手四次挥手及TCP底层协议)、HTTP1和HTTP2的 区别、HTTP和HTTPS的区别等

特殊说明: HTTP是目前优秀公司重点考察的知识点，因为传统前端代码优化，性能上提高较小，HTTP相关优化手段是性能提高的重要方法(例如: 304缓 存、DNS缓存、减少HTTP传输次数和大小、HTTPS的加密等)，这块是一个重点!

书籍：

- 《图解HTTP》
- ...



#### 第四阶段:框架开发

技术要点:目前市场上的项目大部分都是框架开发的，所以框架学习非常的重要，目前主流框架是vue、react、 angular， angular现在 用的越来越少（国内），一般都是老项目使用这个技术在维护(angular1. 0版本居多)

vue全家桶: vue (MWVM实 现的原理以及一些语法实现的原理)、vue- router (HASH路由实现的原理)、vuex (掌握原理)、axios、 vue-cli (需要能够修改脚手架的webpack配置项)、iview/vux/vue element等常用框架的使用等

react全家桶: create-react-app (能够修改webpack的配置项)、react (掌握虚拟DOM渲染原理，掌握DOM-DIFF原理，掌握INDEX索引对比机制，掌握MVC实现的原理)、react-dom/react-native、 react-router、 react-redux/dva/mobx (掌握原理， 自己可以基于原生JS写一套类似的插件、发现里面的一些不足点)、antd (最好可以自己封装一些基础的组件)等

书籍：

- 《React学习手册》
- 《深入浅出React Redux》
- ...

#### 第五阶段:辅助技能

技术要点

Webpack:掌握常用的脚手架使用和修改，会一些基础的webpack搭建

Git: 熟练掌握团队协作开发中代码版本管控技项，熟悉常用的操作命令

Node:掌握基础的API、掌握express/koa/egg等框架、可以编写伪API,可以基于node做跨域处理等，有精力的同学可以研究一下数据库操作等（使用Sequelize ORM框架）

Canvas:一些公司要求会可视化，需要掌握canvas/webGI/d3等,这个对于数学结构、算法等有一定的要求;这方面不好的，可以先掌握一些基础的操作,掌握echarts的用法等;

书籍：

- 《了不起的Node.js》
- 《HTML5游戏开发案例教程》
- 《精通Git》
- 《Linux基础学习篇》

## 推荐的学习方式

- 温故而知新,可以为师矣:笔记+复习
- 知其然而知其所以然:深挖底层原理
- 学而不思则罔 ,思而不学则殆
- 实战很重要:薪资和你敲过的代码成正比
- 多读书:致其知、 诚其意、正其心、修其身，然后家齐 ,国治,而后天下平
- 学习，学前端，什么比较重要呢？是编程（思想）比较重要？基础知识比较重要？还是原理比较重要？还是实战比较重要？都重要。确实也是都重要，但是自己不要把它们区分开，因为都是相辅相成的。只有你的基础知识扎实，你才能够玩得懂源码（原理）；只有基础知识扎实，原理玩透了，你慢慢才能养成编程思想；编程思想再不断去练习，你才能够去做出案例。这是一个相辅相成的过程，只有案例做多了，你才有组件、插件封装的思想，才能够有写底层、写核心，给别人用的这样一个能力；在练习这个能力的时候，又是不断的在巩固基础知识和深入理解的过程。
- 那么什么样才是基础知识扎实呢？
  - 笔记+复习，每天抽出两到三小时
  - 随便给两个点，都可以在三句话之内，不牵强的 说出它们之间的关联（要有整个知识脉络的体系）


## 前端开发需要掌握的IDE

VSCODE

常用插件

- 汉化（看个人）
- 代码格式化：Beautify（shift + alt + F）
- Live Server

常见设置

- File > preference > Settigngs
  - Word Wrap

常用快捷键

- 感叹号!，生成HTML骨架
- EMMET语法
- 格式化代码：shift + alt + F

## 笔记工具

markdown格式，使用typora免费版

## 浏览器内核和控制台

### 常用浏览器

- webkit内核(V8引擎)

  - 谷歌Chrome

  + Safari
  + Opera >=V14
  + 国产浏览器
  + 手机浏览器
  + ...

- Gecko

  - 火狐Firefpx 

- Presto

  - Opera <V14

- Trident

  + IE

  + IE EDGE开始采用双内核(其中包含chrome迷你)



## 谷歌浏览器的控制台(F12/Fn+F12)

- Elements:查看结构样式，可以修改这些内容
- Console:查看输出结果和报错信息，是JS调试的利器
- Sources:查看项目源码
- Network:查看当前网站所有资源的请求信息(包括和服务器传输的HTTP报文信息)、加载时间等(根据加载时间进行项目优化)
- Application: 查看当前网站的数据存储和资源文件(可以盗图)



# JS概览
按照相关的JS语法，去操作页面中的元素，有时还要操作浏览器里面的一些功能
- ECMAScript3/5/6...: JS的语法规范(变量、数据类型、操作语句等等)
- DOM (document object model) :文档对象模型，提供- -些JS的属性和方法，用来操作页面中的DOM元素
- BOM (browser object model) !浏览器对象模型，提供一些JS的属性和方法，用来操作浏览器的

书籍推荐：https://www.aliyundrive.com/s/f8JS7ExEh7o

- 《JavaScript高级程序设计》（第四版）
- 《你不知道的JavaScript》（三卷）
- 《JavaScript权威指南》
- 《ES6标准入门》

## 变量和命名规范

> - 多种定义方式：var / let / const / function / import / class / Symbol()
> - 严谨的命名规范:区分大小写 / 驼峰命名 / 关键字保留字

### 变量

变量：可变的量，在编程语言中，变量其实就是 一个名字，用来存储和代表不同值的东西

变量本身是没有意义的，**有意义的是变量对应的那个值**

ECMAScript 变量是松散类型的，意思是变量可以用于保存任何类型的数据。每个变量只不过是一个用于保存任意值的命名占位符。有 3 个关键字可以声明变量：var、const 和 let。其中，var 在ECMAScript 的所有版本中都可以使用，而 const 和 let 只能在 ECMAScript 6 及更晚的版本中使用。

```js
// ES3
var a = 12
a = 13
console.log(a)

// ES6
let b = 100
b = 200 // 这两种声明方式有啥区别呢  后面讲完变量提升后，再说

const c = 1000
c = 2000 // 报错，const创建的变量存储的值，是不允许被修改的（可以理解为const创建的是常量）

// 创建函数，也相当于在创建变量
function fn() {}

// 创建类，也相当于创建变量
class A {}

// ES6的模块导入也可以创建变量
import B from './B.js'

// Symbol创建唯一值
let n = Symbol(100)

```

#### `var`

```js
// 初始化，默认值为undefined
var message;
```

**声明作用域**：使用 var 操作符定义的变量会成为包含它的函数的局部变量。比如，使用 var在一个函数内部定义一个变量，就意味着该变量将在函数退出时被销毁：

```js
function test() { 
 var message = "hi"; // 局部变量
} 
test(); 
console.log(message); // 出错！
```

不过，在函数内定义变量时省略 var 操作符，可以创建一个全局变量：

```js
function test() { 
 message = "hi"; // 全局变量
} 
test(); 
console.log(message); // "hi"
```

虽然可以通过省略 var 操作符定义全局变量，但不推荐这么做。在局部作用域中定义的全局变量很难维护，也会造成困惑。

**var 声明提升**

使用 var 时，下面的代码不会报错。这是因为使用这个关键字声明的变量会自动提升到函数作用域顶部：

```js
function foo() { 
 console.log(age); 
 var age = 26; 
} 
foo(); // undefined
```

之所以不会报错，是因为 ECMAScript 运行时把它看成等价于如下代码：

```js
function foo() { 
 var age; 
 console.log(age); 
 age = 26; 
} 
foo(); // undefined
```

这就是所谓的“提升”（hoist），也就是把所有变量声明都拉到函数作用域的顶部。此外，反复多次

使用 var 声明同一个变量也没有问题：

```js
function foo() { 
 var age = 16; 
 var age = 26; 
 var age = 36; 
 console.log(age); 
} 
foo(); // 36
```

#### `let`

let 跟 var 的作用差不多，但有着非常重要的区别。最明显的区别是，let 声明的范围是块作用域，而 var 声明的范围是函数作用域。

```js
 // var关键字没有块级作用域，只有函数作用域
  if (true) {
    var name = "Matt";
    debugger;
    console.log(name); // Matt
    
  }
  console.log(name); // Matt，在方括号外面仍可以访问
```

![image-20221216092309932](image-20221216092309932.png)

```js
  if (true) {
    let age = 26;
    debugger;
    console.log(age); // 26
  }
  // console.log(age); // Uncaught ReferenceError: age is not defined

```

`age`之所以不能在if块外部被引用,看下图就知道了

- let声明在变量在在Block里，额外开辟了一块堆内存
- 而if块外部只能访问Local和Global

![image-20221215192214871](image-20221215192214871.png)

执行上下文中，一直的作用域对象有

- Block
  - `let`可创建
- `Local`
- `Global`

![image-20221215192510220](image-20221215192510220.png)

let 不允许同一个块作用域中出现冗余声明。

```js
  let repeat;
  // let repeat; // Uncaught SyntaxError: Identifier 'repeat' has already been declared
```



##### 暂时性死区

let 与 var 的另一个重要的区别，就是 let 声明的变量不会在作用域中被提升。

```js
// name 会被提升
console.log(name); // undefined 
var name = 'Matt';
```

相当于

```js
// name 会被提升
var name;
console.log(name); // undefined 
name = 'Matt';
```

从《你不知道的JavaScript》中，可以知道JS代码执行前存在编译阶段，而var关键字声明的标识符，会在代码执行前，被先处理一下，定义到作用域上。

所谓的变量提升，是js代码存在编译阶段做了一些处理的表现形式

```js
// age 不会被提升
console.log(age); // ReferenceError：age 没有定义
let age = 26;
```

《JS高程第4版中文版》：在解析代码时，JavaScript 引擎也会注意出现在块后面的 let 声明，只不过在此之前不能以任何方式来引用未声明的变量。在 let 声明之前的执行瞬间被称为“暂时性死区”（temporal dead zone），在此阶段引用任何后面才声明的变量都会抛出ReferenceError。

When parsing the code, JavaScript engines will still be aware of the let declarations that appear later in a block, but these variables will be unable to be referenced in any way before the actual declaration occurs. The segment of execution that occurs before the declaration is referred to as the “temporal dead zone,” and any attempted references to these variables will throw a ReferenceError.



简单理解就是JS引擎在编译的时候，对let关键字不做处理，编译完代码执行的时候，作用域里没有age这个变量，自然是报`age没有定义`

上面的理解正确吗？我们调试下不同情况的声明

> 新建index.html，js代码通过scirpt标签写在html内部

- 情况一，使用`var`声明关键字并赋值，注意：断点是在前面

  ```html
      <script>
        debugger;
        var age2 = 13;
      </script>
  ```

  执行到断点时：`Scope`是空的，`age2`已经经过编译被挂到`Global`上了，默认值为`undefined`，符合之前的认知

  ![image-20221216100722267](image-20221216100722267.png)

  断点继续往下走，是赋值操作，值变为13；`Scope`无新增作用域

- 情况二，使用`let`关键字声明并赋值

  ```html
      <script>
        debugger;
        let age = 60;
        // var age2 = 13;
      </script>
  ```

  执行到断点时：新增了`Script`作用域，里面有一个属性age，值为`undefined`

  ![image-20221216102233760](image-20221216102233760.png)

  断点继续往下走：`Script`中的age值变成了60，`Global`无新增属性（age没被挂载到`Global`上）

- 情况三，在函数里面使用`var`关键字

  ```html
      <script>
        function test() {
          debugger;
          var age2 = 13;
        }
        test()
      </script>
  ```

  执行到断点时：在test函数执行栈中，对应的函数作用域里，发生了同情况一一样的事情，只不过对于此时的`age2`而言，它是挂载到当前执行栈的`Local`上的

  ![image-20221216105651340](image-20221216105651340.png)

- 情况四：在函数里面使用`let`关键字

  ```html
      <script>
  
        function test() {
          debugger;
          let age = 60;
          // var age2 = 13;
        }
        test()
      </script>
  ```

  执行到断点时，情况好像和var一样，断点继续往下走，值变为`60`

  ![image-20221216103256948](image-20221216103256948.png)

- 区别呢？？区别在于我们在非函数的方括号中使用的时候

  - var

    ```html
        <script>
          if (true) {
            debugger;
            // var age = 60;
            var age2 = 13;
            console.log(age);
          }
        </script>
    ```

    ![image-20221216104655000](image-20221216104655000.png)

  - let

    ```html
        <script>
          if (true) {
            debugger;
            let age = 60;
            // var age2 = 13;
            console.log(age);
          }
        </script>
    ```

    ![image-20221216104748889](image-20221216104748889.png)

    可以看到，`let`关键字如果被声明在了非函数的语句块中，编译器会新建个`Block`作用域，把对应的变量放在里面

**var和let比较**

- var关键字定义的变量，存储在作用`Scope`对象中的`Global`对象或`Local`变量对象中（距离最近的父级作用域），并且会被编译器先挂载；而`let`也是这样，但额外一点是，如果`let`被声明在了非函数语句块中，编译器在对应的当前`Scope`上新开启一个`Block`对象用来存储变量。
- 对于`var`，变量提升其实就是编译器会把对应的标识符，挂载到最近的父级作用域上（对应情况一和情况三），并且非函数语句块没有作用域；而对于`let`是不会有挂载最近的父级作用域上这个操作的，并且`let`遇到非函数语句块时，反而会新增一个`Block`作用域
- 作用域是分块的，已知的作用域有
  - `Scope`
    - `Global`
      - 全局作用域，一般写代码的最外层，js代码执行时产生
    - `Local`
      - 函数执行，入栈时产生
      - 直接访问不到`Global`，但是函数里有一个`this`属性，指向`Global`
      - 非函数语句块里的同一个执行栈中，`Local`变量对象在方括号内外都是可以访问的，表现为`var`没有块级作用域（对应上文的if的例子）；
    - `Block`
      - 执行`let`关键字在非函数语句块中声明变量时产生
    - `Script`
      - `html`中引入`script`时产生
    - ......



再来看看对于暂时性死区的理解

> 简单理解就是JS引擎在编译的时候，对let关键字不做处理（不会向var关键字那样，把变量挂载到最近的父级作用域上），编译完代码执行的时候，当前作用域对象里没有age这个变量，自然是报`age没有定义`

对应情况一

![image-20221216100722267](image-20221216100722267.png)

```js
      debugger; // 编译阶段结束，age2已经被挂载到最近的父级作用域Global上，值默认为undefined
      console.log(age2) // undefined
      var age2 = 13;
```

对应情况二

![image-20221216102233760](image-20221216102233760.png)

```js
      debugger;
 // 虽然编译阶段age仍像var那样被提升了，但注意，人家var是被提到了距离最近的父级作用域上`Global`
// 但是let声明的关键字是提升到了`Script`作用域里，与`Global`作用域平级
// console.log(age)语句，查找age时，是在Global的作用域链里查找的，自然是找不到的
      console.log(age) // Uncaught ReferenceError: Cannot access 'age' before initialization
	
      let age = 60;
```

对应情况三

```js
      function test() {
        debugger;
        console.log(age2) // undefined

        var age2 = 13;
      }
      test()
```

![image-20221216113306051](image-20221216113306051.png)

对应情况四

```js
      function test() {
        debugger;
        console.log(age) // Uncaught ReferenceError: Cannot access 'age' before initialization

        let age = 60;
      }
      test()
```

![image-20221216113533900](image-20221216113533900.png)

这里可能会问了，情况二访问不到，是因为变量放在了`Script`作用域里，但这里`Local`作用域里，命名就有age，为啥还会访问不到呢？

应该这样说，是可以访问的，但js引擎检测到你要访问的变量，是通过`let`关键字声明的，强制不让你访问，给你报个错`Cannot access 'age' before initialization`，这就是所谓的暂时性死区

那么js引擎咋知道这个变量时`let`关键字声明的呢？因为代码执行前先执行了编译阶段呀





##### 全局声明









#### `const`



小结：

- 不使用`var`
  - 限制自己只使用 let 和 const，有助于提升代码质量，因为变量有了明确的作用域、声明位置，以及不变的值。
- `const`优先、`let`次之
  - 使用 const 声明可以让浏览器运行时强制保持变量不变，也可以让静态代码分析工具提前发现不合法的赋值操作。因此，很多开发者认为应该优先使用 const 来声明变量，只在提前知道未来会有修改时，再使用 let。这样可以让开发者更有信心地推断某些变量的值永远不会变，同时也能迅速发现因意外赋值导致的非预期行为。

### 命名规范

- 严格区分大小写
- 使用数字、字母、下划线、$，数字不能作为开头
- 使用驼峰命名法:首字母小写，其余每-一个有意义单词的首字母都要大写(命名尽可能语义化明显，使用英文单词)
- 不能使用关键字和保留字，当下有特殊含义的是关键字，未来可能会成为关键字的叫做保留字

- [代码规范参考](https://juejin.cn/post/6844903714164047879)
- 免测产品的第一步，是良好的编码习惯

## 数据类型

### 基本数据类型

> - 基本数据类型(值类型) ：数字number、字符串string、 布尔boolean、null、 undefined
>
> - 引用数据类型：object (数组、对象、正则... )、function
> - Symbol：唯一值

**基本数据类型**

- 数字number
  - 常规数字
  - NaN
-  字符串string
  - 所有用单引号、双引号、反引号包起来的，都是字符串
- 布尔boolean
  - true
  - false
- 空对象指针null
- 未定义undef ined

**引用数据类型**

- 对象数据类型object

  + {} 普通对象
  + [] 数组对象.

  + `/^[+-]?(\d|([1-9]\d+))(\.\d+)?$/` 正则对象

  + Math 数学函数对象
  + 日期对象
  + ...

- 函数数据类型function

#### 数字number

- 常规数字

- 

- NaN：not a number，不是一个数，但它属于数字类型

  ```js
  // isNaN([val])
  console.log(isNaN(10)) // false
  console.log(isNaN('AA')) // true, 1.Number('AA') => NaN, 2.isNaN(NaN) => true
  console.log(isNaN('10')) // false, 1.Number('10') => 10, 2.isNaN(10) => false
  console.log(isNaN(NaN)) // true
  ```

  - NaN和任何值(包括自己)都不相等: `NaN!=NaN`，所以我们不能用相等的方式判断是否是有效数字
  - isNaN：检测一个值是否为非有效数字，如果不是有效数字返回TRUE，反之是有效数字返回FALSE
  - 在使用isNaN进行检测的时候，首先会验证检测的值是否为数字类型，如果不是，**先基于Number()**这个方法，把值转换为数字类型，然后再检测

- 把其它类型值转换为数字类型

  > Number( [val] )
  >
  > parseInt([val]) / parseFloat([val],[进制])
  >
  > ==进行比较时比较时，可能要出现把其他类型值转换成数字

- 浏览器内置的V8引擎底层转换规则

  - 把字符串转换为数字，只要字符串中包含任意一个非有效数字字符(第一个点除外)结果都是NaN，空字符串会变为数字零

    ```js
    console.log(Number('12.5')) // 12.5
    console.log(Number('12.5px')) // NaN
    console.log(Number('12.4.5')) // NaN
    console.log(Number(011)) // 11
    console.log(Number('')) // 0
    ```

  - 把布尔转换成数字

    true 转换为 1，false 转换为 0

    ```js
    console.log(Number(true)) // 1
    console.log(Number(false)) // 0
    console.log(isNaN(true)) // false
    console.log(isNaN(false)) // false
    ```

  - null和undefined转为数字

    null返回 0，undefined返回 NaN

    ```js
    console.log(Number(null)) // 0
    console.log(Number(undefined)) // NaN
    console.log(isNaN(null)) // false
    console.log(isNaN(undefined)) // true
    ```

  - 把引用数据类型转为数字

    - 是先把它基于toString方法转换为字符串，然后再将字符串转为数字

    ```js
    console.log(({name: 'sai'}).toString()) // [object Object]
    console.log(Number({name: 'sai'})) // NaN
    console.log(Number({})) // NaN
    
    console.log([].toString()) // '', 空字符串
    console.log(Number([])) // 0
    
    console.log([12].toString()) // '12',
    console.log(Number([12])) // 12
    
    console.log([12, 34].toString()) // '12,34'
    console.log(Number([12, 34])) // NaN
    ```

- parseInt和parseFloat是额外提供的，不同于V8引擎的转换规则

  - 字符串：对于字符串`12.5px`，如果仍然想获得其中的数字，可以使用parseInt和parseFloat方法，它是从左到右依次查找有效数字字符，直到遇到非有效数字字符，停止查找(不管后面是否还有数字，都不在找了)，把找到的当做数字返回

    ```js
    console.log(Number('12.5px')) // NaN
    console.log(parseInt('12.5px')) // 12
    console.log(parseFloat('12.5px')) // 12.5
    console.log(parseFloat('width:12.5px')) // NaN，一开始就是非有效数字字符，停止查找
    ```

  - 布尔

    ```js
    console.log(parseInt(true)) // NaN，会先转为字符串'true'
    console.log(parseInt(false)) // NaN
    console.log(parseFloat(false)) // NaN
    console.log(parseFloat(false)) // NaN
    ```

  - null和undefined

    ```js
    console.log(parseInt(null)) // NaN
    console.log(parseFloat(null)) // NaN
    console.log(parseInt(undefined)) // NaN
    console.log(parseFloat(undefined)) // NaN
    ```

  - 引用数据类型

    ```js
    console.log(parseInt({})) // NaN
    console.log(parseInt({name: 'sai'})) // NaN
    console.log(parseInt([])) // NaN
    console.log(parseInt([12])) // 12
    console.log(parseInt([12,34])) // 12
    
    console.log(parseFloat({})) // NaN
    console.log(parseFloat({name: 'sai'})) // NaN
    console.log(parseFloat([])) // NaN
    console.log(parseFloat([12])) // 12
    console.log(parseFloat([12,34])) // 12
    ```


#### 字符串string

所有用单引号、双引号、反引号(撇 ES6模板字符串)包起来的都是字符串

- 把其它类型值转换为字符串类型

  > [val].toString()
  >
  > 字符串拼接
  
- toString()

  ```js
  // console.log(12.toString()) // An identifier or keyword cannot immediately follow a numeric literal.
  
  let a = 12
  console.log(a.toString()) // '12'
  
  console.log((NaN).toString()) // 'NaN'
  
  console.log((true).toString()) // 'true'
  
  // console.log((null).torString()) // 有toString方法，但是禁止使用   Uncaught TypeError: Cannot read properties of null (reading 'torString')
  // console.log((undefined).toString()) // 同上
  
  console.log([].toString()) // ''
  console.log([12, 34].toString()) // '12,34'
  
  console.log(/^$/.toString()) // '/^$/'
  
  console.log(({ name: 'sai' }).toString()) // '[object Object]' 因为Object.prototype.toString方法不是用来转换字符串的，而是用来转换数据类型的
  
  ```

- 字符串拼接

  四则运算法则中，除加法之外，其余都是数学计算，只有加法可能存在字符串拼接（一旦遇到字符串， 则不是数学运算，而是字符串拼接）

  ```js
  console.log('10' + 10) // 1010
  console.log('10' - 10) // Number('10') - 10 = 0
  console.log('10px' - 10) // Number('10px') - 10 = NaN
  ```

- 面试题

  ```js
  let a = 10 + null + true + [] + undefined + 'sai' + null + [] + 10 + false
  console.log(a) // 11undefinedsainull10false
  
  /*
  10 + null = 10 + Number(null) = 10 + 0 = 10
  10 + true = 10 + Number(true) = 10 + 1 = 11
  11 + [] = 11 + '' = '11' // 空数组变为数字，先要经历变为空字符串，遇到字符串，啥都别想了，直接变为字符串拼接
  '11' + undefined = '11undefined'
  '11undefined' + 'sai' = '11undefinedsai'
  '11undefinedsai' + null = '11undefinedsainull'
  '11undefinedsainull + [] = '11undefinedsainull'
  '11undefinedsainull' + 10 = '11undefinedsainull10'
  '11undefinedsainull10' + false = '11undefinedsainull10false'
  */
  
  
  ```



#### 布尔boolean

只有两个值：true / false

- 把其它类型值转换为布尔类型：只有0、NaN、''、null、undefined 五个值转换为FALSE，其余都转换为TRUE（而且没有任何的特殊情况，空对象转换成布尔值也是true）

  > Boolean([val])
  >
  > ! / !!
  >
  > 条件判断

- Boolean([val])

  ```js
  console.log(Boolean(0)) // false
  console.log(Boolean(NaN)) // false
  console.log(Boolean(null)) // false
  console.log(Boolean(undefined)) // false
  console.log(Boolean('')) // false
  console.log(Boolean('sai')) // true
  console.log(Boolean(-1)) // true
  console.log(Boolean([]))  // true
  console.log(Boolean([12])) // true
  console.log(Boolean([12, 34])) // true
  console.log(Boolean({})) // true
  console.log(Boolean({ name: 'sai' })) // true
  ```

- !：取反(先转为布尔，然后取反)
  !!： 取反再取反，只相当于转换为布尔<=> Boolean

  ```js
  console.log(!1) // false
  console.log(!!1) // true
  ```

- 如果条件只是一个值，不是== / === /!= / >= 等这些比较，是要把这个值先转换为布尔类型，然后验证真假

  ```js
  if (1) { // Boolean(1)
      console.log('true') // true
  }
  
  if ('3px' + 3) {
      console.log('true') // true
  }
  
  if ('3px' - 3) { // NaN
      console.log('false') // 不会输出
  }
  ```




#### null & undefined

null和undefined都代表的是没有



- null: 意料之中(一般都是开始不知道值，我们手动先设置为null, 后期再给予赋值操作)

  - 一 般最好用null 作为初始的空值，因为零不是空值，他在栈内存中有自己的存储空间(占了位置)

    ```js
    let num = null // null是不占据空间的
    // let num = 0 // 0是占据空间的
    
    // ...
    num = 12
    ```

- undefined: 意料之外(不是我能决定的)

  - 创建一一个变量没有赋值，默认值是undefined

    ```js
    let num
    ```

#### `symbol` 唯一值

- 目的为了创建唯一值，不能被`new`

  ```js
  let a1 = Symbol('AA')
  let a2 = Symbol('AA')
  console.log(a1 === a2) // false
  ```

- 常见的3种应用场景：

  - 给对象设置唯一值的属性名

    - 字符串
    - `Symbol`类型
    - `Map`新的数据结构，可以允许属性名是对象

    ```js
    
    let obj = {
        n: 10,
        10: 100,
        true: 200,
        [Symbol('AA')]: 300
    }
    console.log(obj[Symbol('AA')]) // undefined, 两次创建的Symbol不一样
    
    let key = Symbol('BB')
    let obj2 = {
        n: 10,
        10: 100,
        true: 200,
        [key]: 300 
    }
    console.log(obj2[key]) // 300
    
    let obj3 = {
        n: 10,
        10: 100,
        true: 200,
        [Symbol('AA')]: 300,
        [Symbol('AA')]: 600
    }
    
    console.log(obj3) // { '10': 100, n: 10, true: 200, [Symbol(AA)]: 300, [Symbol(AA)]: 600 } 重写call方法时，会使用这种用法
    ```

  - `Symbol`身上的一些方法，如`Symbol.asyncIterator/iterator/hasInstance/toPrimitive/toStringTag...`是某些`JS`底层实现的机制，了解这些机制对我们应用`JS`有很大帮助。

    ![image-20220828124447129](image-20220828124447129.png)

  - `Redux`做公共状态管理的时候，会对派发的行为标识做管理，可以基于`Symbol`类型的值，保证行为的唯一性

#### `bigint` 大数

- 前端发展过程中，用来弥补`JS`已有的数据类型缺陷

  - `JS`中最大安全数

    ```js
    console.log(Number.MAX_SAFE_INTEGER) // 9007 1992 5474 0991
    ```

  - `JS`中最小安全数

    ```js
    console.log(Number.MIN_SAFE_INTEGER) // -9007 1992 5474 0991
    ```

  - 值超过安全数后，进行运算或者访问时，结果会不准确

    ```js
    console.log(Number.MAX_SAFE_INTEGER + 2) // 9007 1992 5474 0992
    ```

- 应用场景：客户端如果拿到这样的数，再进行计算，肯定是不行的了

  - 解决方案

    - 1.服务器返回给客户端的大数，按字符串的格式返回

    - 2.客户端将其变为`bigint`类型，然后按照`bigint`进行运算

      ```js
      console.log(BigInt('90071992547409912434234') + BigInt(12345)) // 90071992547409912446579n
      ```

    - 3.最后把运算过的结果变为字符串，再传递给服务器即可

      ```js
      console.log((90071992547409912446579n).toString()) // 90071992547409912446579
      ```

### 对象数据类型

#### 普通对象

> {[key]: [value], ...} 任何一个对象都是由零到多组键值对(属性名:属性值)组成的(并且属性名不能重复)

- 定义对象

  ```js
  let person = {
      name: 'sai',
      age: 18,
      height: '185CM',
      weight: '80KG',
      1: 100
  }
  ```

- 获取属性名对应的属性值

  ```js
  // 获取属性名对应的属性值
  // 对象.属性名
  // 对象[属性名] 属性名是数字或者字符串格式的
  // 如果当前属性名不存在，默认的属性值是undefined
  // 如果属性名是数字，则不能使用点的方式获取属性值
  
  console.log(person.name) // sai
  console.log(person['age']) // 18
  console.log(person.sex) // undefined
  console.log(person[1]) // 100
  // console.log(person.1) // Uncaught SyntaxError: missing ) after argument list 
  ```

  - 变量和属性名的区别

- 设置属性名属性值

  ```js
  // 设置属性名属性值
  // 属性名不能重复，如果属性名已经存在，不属于新增属于修改属性值
  
  person.GF = 'igo'
  person.name = 'akira'
  console.log(person['GF']) // igo
  console.log(person['name']) // akira
  ```

- 删除属性

  ```js
  console.log(person) // {1: 100, name: 'akira', age: 18, height: '185CM', weight: '80KG', GF: 'igo'}
  // 删除属性
  // 真删除：把属性彻底干掉
  delete person[1]
  // 假删除：属性还在，值为空
  person.weight = null
  console.log(person) // {name: 'akira', age: 18, height: '185CM', weight: null, GF: 'igo'}
  ```

##### 变量名和属性名区别

```js
var name = 10;
var obj = {
    name: 'sai',
    [12]: 120,
    true: 'true123',
    null: 'null123',
    undefined: 'undefined123'
}

// 获取obj这个对象的name属性对应的值
console.log(obj.name) // sai

// 一个对象的属性名只有两种格式：数字或者字符串
console.log(obj['name']) // sai
// console.log(obj.12) // 报错
console.log(obj[12], obj.true, obj.null, obj['undefined']) // 12 'true123' 'null123' 'undefined123'，就当做是数字或者字符串就可以了

console.log(obj[name]) // 等价于obj[10]，结果为undefined
```

值与变量

```js
'age' 值，代表本身
age 变量，代表它存储的值

console.log(obj[name]) // 输出name变量存储的值，等价于obj[10]，结果为undefined

function fn() {
    var a = 100
    return a // 把变量a存储的值返回，return 100
}

// 通过点获取时，只能是ojb.属性名，obj.name
console.log(obj.name)
// 通过中括号获取时，中括号里的内容加上引号才代表属性名，否则是变量
console.log(obj['name'], obj[name])
    
```

要理解的一个事实是，操作一个对象只有两种方式（不考虑使用方法操作）

- 使用点的形式、使用中括号的形式
- 这两种操作符只能跟属性名
  - 对于点，不加引号的就是属性名，纯数字的属性名无法操作
  - 对于中括号，加引号的就是属性名，同时可以操作数字；不加引号，获取的则是变量存储的值（需要做一步转化）
  - obj.key相当于obj['key']

```js
var obj = {
    name: 'sai'
}

var name2 = 'sai2'
var obj2 = {
    // 属性名：属性值（属性值是变量，也是把变量存储的值拿过来，做属性值）
    name2: name2,
    //name2, // ES6的语法糖（合并属性和属性值的写法）
    age: 1 === 1 ? 100 : 20 // 属性值只能放值，这里最终放的也是这个表达式的值
}

```

##### for in 循环

用来循环遍历对象的键值对的（continue和break同样适用）

```js
var obj = {
    name: 'sai',
    age: 18,
    friends: 'hikaru, akira',
    1: 20,
    null: 30,
    [3]: 40
}

// for(var 变量 in 对象)
// 对象中有多少组键值对，循环就执行几次（除非break）结束
for( var key in obj) {
    // 每一次循环时，key变量存储的值是当前对象的属性名
    // 获取属性值：obj[属性名] => obj[key]
    console.log(key) // 打印对象所有的属性名
    // 不能通过obj.key的形式获取，获取的结果是undefined
    console.log(`属性名是${key}，属性值是${obj[key]}`)

    // for in 循环遍历时，会有一个优先级，优先遍历数字类型的属性名，并按照从小到大的顺序
}
```



#### 特殊对象

##### 数组

数组是特殊的对象数据类型

- 属性名是数字，从0开始逐级递增（索引）
- 多了一个length属性

```js
let arr = [12, 'haha', true, 13]
console.log(arr)
```

![image-20220922053400732](image-20220922053400732.png)



- 我们中括号中设置的是属性值，它的属性名是默认生成的数字，从零开始递增，而且这个数字代表每一项的位置，我们把其成为“索引”=>从零开始，连续递
  增，代表每一-项位置的数字属性名

- 天生默认-一个属性名length ，存储数组的长度

  ```js
  let arr = [12, 'haha', true, 13]
  console.log(arr)
  console.log(arr.length) // 4
  console.log(arr['length']) // 4
  console.log(arr[1]) // haha
  console.log(arr[arr.length - 1]) // 13
  // 向数组末尾追加内容
  arr[arr.length] = 100
  console.log(arr) // [12, 'haha', true, 13, 100]
  ```

#### 元素对象

`let box = document. getElementById('box');`
通过方法获取的元素是对象数据类型的值
`console.log(typeof box); //=>"object"`
基于`.dir`可以看到一个对象的详细信息

- id:操作元素的ID值
- className:获取或者操作元素的CLASS样式类的值
- innerHTML:获取或者操作的元素的内容(可以识别标签)
- innerText:和innerHTML 的区别是不能识别标签
- style:操作元素的**行内样式**，属性值也是一个对象（CSSStyleDeclaration）
- tagName:获取元素的标签名(一般大写)

实际学习的时候，每次都打印输出一下，对比每个元素（h1、div）都有什么属性及有哪些不同的地方，不断的夯实基础；这部分没有什么系统的理论，每次用到的时候，打印输出一下，然后对比已经掌握的进行学习



![image-20221008222740822](image-20221008222740822.png)

```js
box.style.backgroundColor = 'red'
// 修改的是堆内存中的值(只要堆内存中的值被修改,浏览器会基于DOM映射机制把页面中的元素进行重新渲染)

let AA = box.style;
AA.backgroundColor = 'blue'; // 修改堆中的信息,有效果

let BB = box.style.backgroundColor;
BB = 'green'; // 修改不是堆中信息,不起作用

```

基础知识没什么好说的，背下来记熟了，脑子里面有东西了，慢慢的自己就能悟透了

#### 对象的自定义属性

可以通过`ojb.property = value`把需要保存的数据，存储在全局对象上，并通过`this`或其他方式获取到（视具体实现）

在写多行表格数据展开显示时，尤其有用

## 数据类型堆栈底层机制

```js

let a = 12;
let b = a;
b = 13;
console.log(a); // 12

let n = {
    name: 'sai'
};
let m = n;
m.name = 'sai2'
console.log(n.name); // sai2

```

浏览器想要执行JS代码:

1.从电脑内存中分配出一块内存，用来执行代码(栈内存=>Stack)

- 执行代码、存储变量和基本类型值
- js中的赋值，是关联引用模式，而不是拷贝模式

2.分配一个主线程用来自上而下执行js代码



`let a = 12;`

1. 创建变量a，放到当前栈内存变量存储区域中

2. 创建一个值12 ,把它存储到当前栈内存值区域中（简单的基本类型值是这样存储的,复杂的引用类型值不是这样做的）

   复杂值(引用类型值)的存储,又分成了三个步骤:	

   1. 在内存中分配出一块新内存,用来存储引用类型值(堆内存=>heap) =>内存有一个16进制地址
   2. 把对象中的键值对(属性名:属性值)依次存储到堆内存中
   3. 把堆内存地址和变量关联起来

3. =为赋值，其实赋值是让变量和值相互关联的过程



基本类型：按值操作(直接操作的是值) ,所以也叫作值类型

引用类型：操作的是堆内存的地址(按引用地址操作的)

练习：

```js
let n = [10, 20]; // 0x100
let m = n; // 0x100
let x = m; // 0x100
m[0] = 100; // [100, 20] 0x100
x = [30, 40]; // 0x200
x[0] = 200; // [200, 40] 0x200
m = x; // 0x200
m[1] = 300; // [200, 300] 0x200
n[2] = 400; // [100, 20, 400]
console.log(n, m, x) // [100, 20, 400], [200, 300], [200, 300]
```

## 数据类型检测

> - typeof [val]: 用来检测数据类型的运算符 
> - instanceof :用来检测当前实例是否率属于某个类
> - constructor :基于构造函数检测数据类型(也是基于类的方式)
> - object.prototype.toString.call() :检测数据类型最好的办法

### `typeof`

在浏览器（计算机）底层，基于数据类型的二进制值进行检测

基于typeof检测出来的结果：

1.首先是一个字符串

2.字符串中包含对应的类型

```js
console.log(typeof 1) // 'number'
let a = NaN
console.log(typeof a) // 检测值，'number'
console.log(typeof 'a') // 'string'
console.log(typeof undefined) // 'undefined'
console.log(typeof function () { }) // 'function'

console.log(typeof null) // 'object'
console.log(typeof []) // 'object'
console.log(typeof {}) // 'object'
console.log(typeof /^/) // 'object'
```

局限性

1.`typeof null => "object"`，但是null并不是对象

2.基于typeof无法细分出当前值是普通对象还是数组对象等，因为只要是对象数据类型，返回的结果都是"object"

```js
console.log(typeof typeof typeof []) // 'string'，注意用引号区分出字符串
```

因为typeof检测的结果都是字符串，所以只要两个及以上同时检测，最后结果必然是"string"

### `instanceof`

一开始并不是用来检测数据类型的，而是用来检测当前实例是否属于某个类的



### `constructor`



### `Object.prototype.toString.call`

## 流程控制

### 判断

> 条件成立做什么?不成立做什么?
>
> - if/else if/else
> - 三元运算符
> - switch case

#### 三元运算符

三元运算符:简单IF/ELSE的特殊处理方式

条件?条件成立处理的事情:不成立处理的事情;

1.如果处理的事情比较多，我们用括号包起来，每一-件事情用逗号分隔

2.如果不需要处理事情，可以使用null/undefined占位

#### switch case

> 1.每一-种CASE情况结束后最好都加上break
>
> 2.default等价于else，以上都不成立干的事情
>
> 3.每一种case情况的比较用的都是===绝对相等

```js
let a = 10
switch (a) {
    case 10:
        console.log(10) // 10
        break
    case 11:
        console.log(11)
        break
    default:
        console.log(12)
}
```

没加break的影响：不管后面的条件成不成立，都会被执行，直到遇到break为止

```js
let a = 10
switch (a) {
    case 10:
        console.log(10) // 10
    case 11:
        console.log(11) // 11
    default:
        console.log(12) // 12
}
```

应用场景，不加break可以实现变量在某些值的情况下做相同的事情：

```js
let a = 10
switch (a) {
    case 10:
    case 11:
        console.log('10, 11') // 不加break可以实现变量在某些值的情况下做相同的事情
    default:
        console.log(12)
}
```

#### == VS ===

==:相等(如果左右两边数据值类型不同，是默认先转换为相同的类型，然后比较)
'5'==5 =>TRUE
===:绝对相等(如果类型不一一样，肯定不相等)
'5'===5 =>FALSE

项目中为了保证业务的严谨，推荐使用===

### 循环

> 重复做某些事情就是循环
>
> - for循环
> - for in循环
> - for of循环( ES6新增)
> - while循环
> - do while循环

1.创建循环初始值

2.设置(验证)循环执行的条件

3.条件成立执行循环体中的内容

4.当前循环结束执行步长累计操作

循环体中的两个关键词

- continue: 结束当前这轮循环(continue后面的代码不再执行)，继续执行下一轮循环
- break: 强制结束整个循环( break后面代码也不再执行)，而且整个循环啥也不干直接结束

```js
for (var i = 0; i < 10; i++) {
    if (i > 2) {
        i += 2
        continue
    }
    if (i >= 6) {
        i--
        break
    }
    i++
    console.log(i) // 1 3
}
console.log(i) // 10

```

## 函数的基础概念

>函数就是一个方法或者一个功能体，函数就是把实现某个功能的代码放到一-起进行封装，以后想要操作实现这个功能，只需要把函数执行即可=>“封装”: 减少页面中的冗余代码，提高代码重复使用率(低耦合高内聚)

### 函数的创建

```js
//=>ES5老方式
function [函数名]([形参变量1]...){
    //函数体:基于JS完成需要实现的功能，
    return [处理后的结果];
}

[函数名]([实参1]....);

```

### 函数参数

```js
// 求两个数的和， 算完和后乘以10，然后在除以2...
// =>sum是函数名，代表这个函数，
// =>n/m是形参，是变量，用来存储执行函数时传递的实参
function sum(n, m) {
    let result=n+m;
    result *= 10;
    result /= 2;
    console. log(result);
}

console. log(sum);
sum(10, 20);|

//形参的细节
//创建函数的时候我们设置了形参变量，但如果执行的时候并没有给传递对应的实参值，那么形参变量默认的值是: undefined

```

### 函数返回值

```js
// 函数执行的时候，函数体内部创建的变量我们是无法获取和操作的，如果要想获取内部的信息，我们需要基于RETURN返回值机制，把信息返回才可以
// RETURN的一定是值:此处是把RESULT变量存储的值返回给外面
// 没有写RETURN，函数默认返回值是undefined

```

### 匿名函数

```js
//匿名函数之函数表达式:把一个匿名函数本身作为值赋值给其它东西，这种函数一般不是手动触发执行，而且靠其它程序驱动触发执行(例如:触发某个事件的时候把它执行等)
document. body. onclick = function () {}
setTimeout( function(){}, 1000); //=>设置定时器，1000MS后执行匿名函数

//匿名函数之自执行函数:创建完-一个匿名函数，紧接着就把当前函数加小括号执行
(function(n){
	n=>100
})(100);
```

### 函数的底层运行机制

```js
// 创建函数
function fn(n, m) {
    var res = null
    res = n + m
    return res
}

// 执行函数
var AA = fn(10, 20)
console.log(AA)
```

创建函数，开辟的堆内存中存储的是函数体中的代码，但是是按照字符串存储的

执行函数，先把fn函数执行，再把执行后的返回结果和变量AA关联在一起，函数的返回值只看return，有return，后面是啥返回值就是啥，没有就是undefined

每一次函数执行的目的，都是把函数体中的代码（先从字符串变为代码）执行 => 形成一个全新的私有内存栈（[JS编译过程，VO，AO ](https://www.jianshu.com/p/edb2be5866eb)）

**`JS`函数运行机制**

首先关于整个生命周期，最重要的是要了解它的编译过程。

1. 发现有代码调用了一个函数
2. 在执行这个function之前，创建一个执行上下文（execution context），也可以叫执行环境。
3. 进入创建阶段（VO创建）
    a. 初始化作用域链（scope chain）
    b. 创建变量函数（variable object / VO）
    c. 创建参数对象（arguments object，传进来的参数）,检查上下文，初始化其名字和值，以及建立引用对象的拷贝。
    d. 扫描上下文中的函数声明
    e. 为每一个扫描到的函数声明在VO中创建一个属性，命名为函数的名字，指向了存储空间中的对应函数。
    f. 如果函数名称已经存在了，这个引用指针将被重写为新的这一个。
    g. 扫描上下文中的变量声明
    h. 为每一个扫描到的变量声明在VO中创建一个属性，命名为变量的名字，初始化值为undefined。
    i. 如果变量名在内存中已经存在了，就跳过。
    j. 决定上下文中this的指向。
4. 执行阶段（VO => AO）
    a. 执行/解释上下文中的function，为变量赋值
    b. 代码按行执行

就我个人理解，他们的相应概念和包含内容如下。

scope ：变量/函数起作用的区域
 scope chain : 保证对执行环境有权访问的所有变量和函数的有序访问。相当于VO + [scope]
 我们可以将作用域定义为一套规则，用来管理引擎如何在当前作用域以及嵌套的子作用域中根据标识符名称进行变量查找，作用域链是这套规则的具体实现。

execution context  = {VO, this, [scope]}



函数的每次执行，都会形成一个全新的私有栈内存

每个私有栈内存都会有变量存储、值存储对应的内存空间



**案例解析**

选项卡

```html

<body>
    <button value="按钮1">按钮1</button>
    <button value="按钮2">按钮2</button>
    <button value="按钮3">按钮3</button>
    <button value="按钮4">按钮4</button>
    <button value="按钮5">按钮5</button>
</body>
<script>
    var btnList = document.getElementsByTagName('button')
    for (var i = 0; i < btnList.length; i++) {
        btnList[i].onclick = function() {
            console.log(i)
        }
    }
</script>

```

点击的回调函数执行时，每个函数对应保存i都是5，因为for循环已经执行完毕了：给每个`button`对象向，添加点击事件的回调，而当我们真正去点击时，函数开始执行，此时`i`的值是5

可以每次循环时，自定义一个`myIndex`属性，记录每次`i`的值

```js
    var btnList = document.getElementsByTagName('button')
    for (var i = 0; i < btnList.length; i++) {
        btnList[i].myIndex = i
        btnList[i].onclick = function() {
            console.log(this.myIndex)
        }
    }
```

### 函数的arguments

任意数求和：

- 传递实参的个数不定
- 传递的值是否为有效数字不定

把传递的有效数字进行相加求和

箭头函数

arguments：函数内置的实参集合

- 类数组集合，集合中存储所有函数执行时，传递的实参信息
- 不论是否设置形参，arguments都存在
- 不论是否传递实参，arguments都存在

- arguments.callee：存储的是当前函数本身（一般不用，JS严格模式下禁止使用这些属性）

```js
function sum() {
    console.log(arguments)
    let total = null
    for (let i = 0; i < arguments.length; i++) {
        // 获取的每一项，都要先转换成数字
        let item = Number(arguments[i])
        // 非有效数字不加
        if (isNaN(item)) {
            continue
        }
        total += item;
    }
    return total
}

let total = sum(1, 3, '5a')
console.log(total)
// arguements.callee指向函数自身，严格模式下禁止使用
```

![image-20221212210134110](image-20221212210134110.png)

### 箭头函数

见`ES6~11`小节



## 正则表达式

### 正则表达式是干什么的

> regular expression: RegExp
>
> 用来处理字符串的规则
>
> - 只能处理字符串
> - 它是一个规则：可以验证字符串是否符合某个规则（test），也可以把字符串中符合规则的内容捕获到（exec/match...）

```js
let str = "good good study, day day up!";
// 正则就是用来指定规则
// 规则：是否包含连续的数字
let reg = /\d+/;
console.log(reg.test(reg)) // false

str = "2023-02-12"
// 捕获符合正则的内容
console.log(reg.exec(str)); // [ '2023', index: 0, input: '2023-02-12', groups: undefined ]
// input存的是原始字符串
```

### 编写正则表达式

创建方式有两种

- 字面量方式（两个斜杠之间包起来的，都是用来描述规则的元字符）

  ```js
  let reg = /\d+/;
  ```

- 构造函数模式创建

  ```js
  // 两个参数：元字符字符串  修饰符字符串
  let reg = new RegExp("\\d+"); // 字符串需要转义
  ```

正则表达式是由两部分组成：

- 元字符

  - 用来定义规则的

  - 常用的元字符

    **量词元字符**，设置出现的次数

    ```js
    *   零次到多次
    +   一次到多次
    ？  零次或者一次
    {n} 出现n次，n为0或正整数
    {n,} 出现n到多次
    {n,m} 出现n次到m次（包含n,m）
    ```

    **特殊元字符**，单个或者组合在一起，代表特殊的含义

    ```js
    \  转义字符：普通字符 ==> 特殊字符 ==>  普通字符
    .  除\n（换行符）以外的任意字符
    ^  以哪一个元字符作为开始
    $  以哪一个元字符作为结束
    \n  换行符
    \d  0~9之间的数字
    \D  非0~9之间的数字（\d和\D意思相反）
    \N  非换行符，就是.
    \w  数字、字母、下划线中的任意一个字符
    \W  非数字、字母、下划线中的任意一个字符
    \s  一个空白字符（包括空格、制表符、换页符等）
    \t  一个制表符（Tab键：四个空格）
    \b  匹配一个单词的边界
    
    x|y  x或者y中的一个字符
    [xyz]  x或者y或者z中的一个字符
    [^xy]  除了x/y以外的字符
    [a-z]  指定a-z这个范围内中的任意字符，[0-9a-zA-Z_] === \w
    [^a-z]  上一个的取反
    ()    正则中的分组符号
    (?:)  只匹配不捕获
    (?=)  正向预查
    (?!)  负向预查
    ```

    **普通元字符**，代表本身含义

    ```js
    /mindcons/  此正则匹配的就是mindcons
    ```

- 修饰符

  - 常用的修饰符：`img`

    ```js
    i => ignoreCase  忽略单词大小写匹配
    m => multiline   可以进行多行匹配
    g => global      全局匹配
    
    
    /A/.test('lalala'); // false
    /A/i.test('lalala'); //true
    ```

    

只要掌握上面两个东西，就掌握正则了



### 元字符剖析

#### `^ $` 开始和结尾

```js
let reg = /^\d/;
console.log(reg.test('mindcons')); // false
console.log(reg.test('mindcons2023')); // false
console.log(reg.test('2023mindcons')); // true

let reg1 = /\d$/;
console.log(reg1.test('mindcons')); // false
console.log(reg1.test('mindcons2023')); // true
console.log(reg1.test('2023mindcons')); // false

// 两个都不加，字符串中包含符合规则的内容即可
let reg2 = /\d+/;
// 两个都加，字符串只能是和规则一致的内容（如下：只能是数字）
let reg3 = /^\d+$/;
// 验证手机号（11位，第一个数字是1）
let reg4 = /^1\d{10}$/;
```

#### `\` 转义

```js
// .不是小数点，是除了\n外的任意字符
let reg = /^2.3$/;
console.log(reg.test('2.3')); // true
console.log(reg.test('2@3')); // true
console.log(reg.test('23')); // false

// 基于转义字符，让其只能代表小数点
let reg1 = /^2\.3$/;
console.log(reg1.test('2.3')); // true
console.log(reg1.test('2@3')); // false

let str = "\\d"; // 字符串中一个\也有特殊含义
console.log(str); // \d
let reg2 = /^\d$/; // \d代表0-9之间的任意数字
console.log(reg2.test(str)); // false
let reg3 = /^\\d$/;
console.log(reg3.test(str)); // true


```

#### `x|y` 或

```js
let reg = /^18|29$/;
console.log(reg.test("18")); // true
console.log(reg.test("29")); // true
console.log(reg.test("129")); // true
console.log(reg.test("189")); // true
console.log(reg.test("1829")); // true
console.log(reg.test("829")); // true
console.log(reg.test("182")); // true

// 直接x|y会有很多情况，一般会伴随着小括号，进行分组，因为小括号能改变处理的优先级
// 只能是18或29中的一个了
let reg1 = /^(18|29)$/;
console.log(reg1.test("18")); // true
console.log(reg1.test("29")); // true
console.log(reg1.test("129")); // false
```

#### `[]`

```js
// 1.中括号中出现的字符，一般都代表本身的含义
let reg = /^[@+]$/;
console.log(reg.test("@")); // true
console.log(reg.test("+")); // true
console.log(reg.test("@@")); // false
console.log(reg.test("@+")); // false

// 2.\d在中括号中还是0-9
let reg1 = /^[\d]$/;
console.log(reg1.test("d")); // false
console.log(reg1.test("\\")); // false
console.log(reg1.test("9")); // true
let reg2 = /^[\\d]$/; // 转义
console.log(reg2.test("d")); // true
console.log(reg2.test("\\")); // true
console.log(reg2.test("9")); // false

// 3.中括号中不存在多位数
let reg3 = /^[18]$/;
console.log(reg2.test("1")); // true
console.log(reg2.test("8")); // true
console.log(reg2.test("18")); // false
let reg4 = /^[10-29]$/; // 不是10-29，代表1或者0-2或者9
let reg5 = /^[(10-29)]$/; // 括号在[]中没有分组的含义
let reg5 = /^[\(10-29\)]$/; // \在[]中转义(还是(自身))
```

#### 元字符及其含义完整列表

自查

### 常用正则表达式

#### 验证是否为有效数字

```js
/**
 * 0
 * 1
 * 12
 * 12.5
 * 12.0
 * -1
 * -12.5
 * 09
 * +9
 * 规则分析
 * 1.可能出现 + - 号，也可能不出现
 * 2.一位0-9都可以，多位首位不能为0
 * 3.小数部分，可能有可能没有，一旦有，后面必须有小数点+数字
 * 
 * 书写技巧：按位写
 * 1.(+|-)?   [+-]?
 * 2.(\d|([1-9]\d+))
 * 3.(\.\d+)?
 */

let reg = /^(+|-)?(\d|([1-9]\d+))(\.\d+)?$/;
```

#### 验证密码

数字、字母或下划线，6-16位

```js
let val = userPassInp.value,
    reg = /\w{6,16}/;

let flag = reg.test(val);
// ...
```

#### 验证真实姓名

```js
/**
 * 1.汉字
 * 第一个字符到最后一个字符的Unicode编码  * /^[\u4E00-\u9FA5]$/
 * 2.名字长度2-10位
 * 3.可能有译名 ·汉字
 * 
 */
let reg = /^[\u4E00-\u9FA5]{2,10}(·[\u4E00-\u9FA5]{2,10}){0,2}$/;
```

#### 验证邮箱

```js
// 逆向分析
let reg = /^\w+((-\w+)|(\.\w+))*@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;
// mindcons@foxmail.com

// \w+((-\w+)|(\.\w+))*
// 开头是数字、字母、下划线（一到多位）
// 还可以是 -数字字母下划线  或者 .数字字母下划线（整体0到多位）
// => 邮箱的名字由“数字、字母、下划线、-、.”几部分组成，但是- / .不能连续出现也不能作为开始


// [A-Za-z0-9]+
// @后面紧跟：数字字母（一到多位）foxmail

// ((\.|-)[A-Za-z0-9]+)*
// xxx.com.cn  对多域名邮箱的匹配.com
// sai@google-mail-office.com  对企业域名的匹配


// \.[A-Za-z0-9]+
// xxx.com  xxx.cn 匹配的是最后的域名
```

#### 验证身份证号码

```js
// 二代身份证18位、最后一位可能是X
// let reg = /^\d{17}(\d|X)$/; // 一般不这么写，因为里面还有很多特殊的意义


// 前六位：省市县 130828 0开头北京、3开头江苏
// 中间八位：年月日
// 最后四位：
//   最后一位：X或数字
//   倒数第二位：偶数 女、奇数 男
//   其余是依托已有数字，经过算法算出来的

// 小括号的第二个作用：分组捕获，不仅可以把大正则匹配到的信息捕获到，还可以单独捕获到每个小分组的内容
let reg = /^(\d{6})(\d{4})(\d{2})(\d{2})\d{2}(\d)(\d|X)$/;
res = reg.exec("130828199012040617")
console.log(res)
// 捕获结果是一个数组，包含每个小分组单独获取的内容

/**
 * [
  '130828199012040617',
  '130828', // 省市县
  '1990', // 年
  '12', // 月
  '04', // 日
  '1', // 性别
  '7', 
  index: 0,
  input: '130828199012040617',
  groups: undefined
]
 */
```

### 两种创建正则方式的区别

构造函数中传递的是字符串，需要转义`\`

```js
let reg = /\d+/g;

reg = new RegExp("\\d+", "g") // 构造函数创建，传递两个字符串参数：元字符 修饰符
```

正则表达式中的部分内容，是变量存储的值（变量存的值是正则的一部分）

```js
let type = "sai";
reg = /^@"+type+"@$/; // 这种方式不行，/之间代表的都是元字符
console.log(reg.test("@sai@")) // false
console.log(reg.test('@"""typeeeee"@')) // true

// 如果正则中，要包含某个变量的值，则不能使用字面量的形式创建
// 使用构造函数拼接，因为参数是字符串
reg = new RegExp("^@"+type+"@$")
console.log(reg.test("@sai@")) // true
```

### 正则捕获

#### 实现正则捕获的方法

- 正则`RegExp.prototype`上的方法
  - `exec`
  - `test`
- 字符串`String.prototype`上的方法
  - `replace`
  - `match`
  - `splite`
  - ...

#### 前提

当前正则要和字符串匹配，如果不匹配，结果是null

```js
let str = "sai2019mind2020cons2021";

let reg = /^\d+$/;

// 实现正则捕获的前提：当前正则要和字符串匹配，如果不匹配，结果是null
console.log(reg.test(str)) // false
console.log(reg.exec(str)) // null
```

#### `exec`捕获结果

1.捕获的结果是`null`或者一个数组

第一项：本次捕获到的内容

其余项：对应小分组本次单独捕获的内容

`index`：当前捕获内容在字符串中的起始索引

`input`：原始字符串

```js
let str = "sai2019mind2020cons2021";

// 捕获所有数字
let reg = /\d+/;

console.log(reg.exec(str)) 
```

```json
[
  '2019',
  index: 3,
  input: 'sai2019mind2020cons2021',
  groups: undefined
]
```

2.每执行一次`exec`，只能捕获到一个符合正则规则的。但是默认情况下，无论执行多少次，获取的结果永远是匹配到的第一个，其余的获取不到

```js
let str = "sai2019mind2020cons2021";

// 捕获所有数字
let reg = /\d+/;

console.log(reg.exec(str)) ;
console.log(reg.exec(str)) ;
console.log(reg.exec(str)) ; // 结果都是一样的
```

上述特点称为：正则捕获的懒惰性

原因：下一小节

#### `exec`捕获原理（懒惰性）

`lastIndex`：

当前正则下一次匹配的起始索引位置，默认为0，表示匹配捕获是从索引为零的位置开始找

第一次匹配完成，`lastIndex`没有改变，所以下一次`exec`依然是从字符串最开始找，找到的永远是第一个匹配到的

`exec`捕获懒惰性的原因：默认情况下`lastIndex`的值不会修改（其他的捕获方法也是一样的），这是正则捕获本身的机制

```js
let str = "sai2019mind2020cons2021";
let reg = /\d+/;

console.log(reg.lastIndex) // 0
```

直接手动修改是不行的`reg.lastIndex = 7`

```js
let str = "sai2019mind2020cons2021";
let reg = /\d+/g; // 加一个g的修饰符，正则处理机制内容会自己修改lastIndex

console.log(reg.lastIndex); // 0
console.log(reg.exec(str)); // ["2019"...]
console.log(reg.lastIndex); // 7
console.log(reg.exec(str)); // ["2020"...]
console.log(reg.lastIndex); // 15
console.log(reg.exec(str)); // ["2021"...]
console.log(reg.lastIndex); // 23
console.log(reg.exec(str)); // null // 当全部捕获后，再次捕获的结果是null，lastIndex值回归到0
console.log(reg.lastIndex); // 0
console.log(reg.exec(str)); // ["2019"...] 
```

写法注意：

条件判断中的`test`，会先改了一次`lastIndex`

```js
let str = "sai2019mind2020cons2021";
let reg =/\d+/g;
if(reg.test(str)) {
    console.log(reg.lastIndex); // 7
    console.log(reg.exec(str)); // ["2020"...]
}
```

解决办法：

```js
// 单独拿一份
let str = "sai2019mind2020cons2021";
let reg =/\d+/g;
let reg_cond =/\d+/g;
if(reg_cond.test(str)) {
    console.log(reg.lastIndex); // 0
    console.log(reg.exec(str)); // ["2019"...]
}
```

#### `exec`方法封装

编写一个方法`execAll`，执行一次捕获所有的匹配结果

```js
~function () {
  function execAll(str = "") {
    // 确保正则是加了g
    if(!this.global) return this.exec(str); // 没有加g，只捕获一次
    // this: RegExp的实例
    let arr = [], // arr存储捕获的所有内容
      res = this.exec(str); // res存储每次捕获的内容

    while (res) {
      // 把每次捕获的内容存在arr中
      arr.push(res[0]);
      // 只要捕获的内容不为null，就继续捕获下去
      res = this.exec(str);
    }
    return arr.length === 0 ? null : arr;

  }
  RegExp.prototype.execAll = execAll;
}()

let reg = /\d+/g; // 浏览器控制台打印一下reg，如果加了g，则global属性为true
let str = "sai2019mind2020cons2021";
console.log(reg.execAll(str)) // [ '2019', '2020', '2021' ]
```

字符串方法中，`match`方法可以实现执行一次捕获所有匹配结果（效果同上，如果不加`g`，只返回一个捕获结果，若没有匹配到，则返回`null`）

上述方法其实就是`mathc`的原理

```js
let reg = /\d+/g;
console.log("sai2019mind2020cons2021".match(reg)) // [ '2019', '2020', '2021' ]
```

#### 分组捕获和分组引用





```js
let reg = /^(\d{6})(\d{4})(\d{2})(\d{2})\d{2}(\d)(\d|X)$/;
res = reg.exec("130828199012040617")
console.log(res)
// 捕获结果是一个数组，包含每个小分组单独获取的内容

/**
 * [
  '130828199012040617',
  '130828', // 省市县
  '1990', // 年
  '12', // 月
  '04', // 日
  '1', // 性别
  '7', 
  index: 0,
  input: '130828199012040617',
  groups: undefined
]
 */
```







### 应用场景









# ES6+

[GitHub - lukehoban/es6features: Overview of ECMAScript 6 features](https://github.com/lukehoban/es6features)

教程来源：https://www.bilibili.com/video/BV1uK411H7on

## 变量及作用域

### let变量声明及其作用域

1.变量不能重复声明

2.块级作用域 全局，函数，eval

3.不存在变量提升

4.不影响作用域链

**let实践练习**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .item{
            width: 100px;
            height: 50px;
            border: solid 1px #0077AA;
            float: left;
            margin-left: 10px;
        }
    </style>
</head>
<body>
<div class="container">
    <h2 class="page-header">点击切换颜色</h2>
    <div class="item"></div>
    <div class="item"></div>
    <div class="item"></div>
    <script>
        //获取item对象
        let items = document.getElementsByClassName("item");
        //遍历并绑定事件
        for(let i=0;i<items.length;i++){
            items[i].onclick=function(){
                items[i].style.background = 'pink';
            }
        }
    </script>
</div>
</body>
</html>
```

### const常量声明

1.一定要赋初始值

2.一般常量使用大写（潜规则）

3.常量的值不能修改

4.块级作用域

5.对于数组和对象的元素的修改，不算做对常量的修改，不会报错

## 解构赋值

`ES6`允许按照一定的模式从数组或对象中提取值，对变量进行赋值，这被称为解构赋值

### 数组的解构

```js
const F4 = ['a','b','c','d'];
let [a1,a2,a3,a4] = F4;
console.log(a1,a2,a3,a4) // a b c d
```

### 对象的解构

```js
// 对象的解构
const person = {
    name : '小明',
    age : 10,
    run : function() {
       console.log("我可以跑步");
    }
};
let {name,age,run} = person;
run(); // 我可以跑步
```

#### 对象解构赋值的连续写法

```js
let obj = {
    a: {
        b: {
            c: 1
        }
    }
}

let $oute = {
    query: {
        id: 0001,
        title: 'hello'
    }
}

const {a} = obj
console.log('a', a) // {b: {c: 1}}

const {a: {b}} = obj
console.log('b', b) // {c: 1}

const {a: {b: {c}}} = obj
console.log('c', c) // 1
```

连续结构赋值的同时，重命名属性值

```js
const {a: {b: data}} = obj
console.log('data', data) // {c: 1}
```

通过连续结构赋值的写法，是无法获取到外层属性值的，比如此时a是无法获取到的：

```js
const {a: {b: data}} = obj
console.log('a', a)
```



## 模板字符串

`ES6`引入新的声明字符串的方式，类似于占位符

```
` `, ' ', " "
```

1.声明

2.内容中可以直接出现换行符

3.变量拼接

```
// ${}
let name = 'xiaoming'
let result = `${name} is running`
```

## 对象的简化写法

`ES6`允许在大括号里面，直接写入变量和函数，作为对象的属性和方法。这样的书写更加简洁。

```js
let name = 'xiaoming';
let change = function() {
  console.log('we can change you~');
}
const school = {
    name,
    change,
    improve(){
        console.log('we can improve you~');
    }
}
```

## 箭头函数

### 箭头函数以及声明特点

`ES6`允许使用箭头`=>`定义函数

```js
let fn = (a,b) => {
    return a + b;
}
let result = fn(1,2);
```

1.`this`是静态的，`this`始终指向函数声明时所在作用域下的`this`的值

```js
function getName() {
  console.log(this.name);
}
let getName2 = () => {
  console.log(this.name)
}
//设置window对象的name属性
window.name = '小明';
const person = {
    name:'xiaoming'
}

//直接调用
getName();//小明
getName2();//小明

//call方法调用
getName.call(person)//xiaoming
getName2.call(person)//小明  this始终指向函数声明时所在作用域下的this的值
```

call方法补充

```js
var person = {
    fullName: function() {
        return this.firstName + " " + this.lastName;
    }
}
var person1 = {
    firstName:"Bill",
    lastName: "Gates",
}
var person2 = {
    firstName:"Steve",
    lastName: "Jobs",
}
person.fullName.call(person1);  // 将返回 "Bill Gates"
```

2.不能作为构造函数实例化对象

3.不能使用`arguments`变量

```js
    // 没有arguments
    let argFunc = () => {
        console.log(arguments) // 可以打印，但并没有值
    }
    argFunc(1, 2, 3, 4)
```

并没有获取到实参

![image-20221212214757106](image-20221212214757106.png)

4.箭头函数的简写

- 参数

  ```js
  1.省略小括号，当形参有且只有一个的时候
  
  
  ```

  

- 返回值

  ```js
  // 省略花括号，当代码体只有一条语句的时候，此时return可以省略，而且语句的执行结果就是函数的返回值
  
  // 普通函数
  function sum(n, m) {
      return n + m
  }
  // 改写成箭头函数
  let sumA = (n, m) => {
      return n + m
  }
  
  // 如果函数体中只有一行return，可以省略return和大括号，一行搞定
  let sumB = (n, m) => n + m
  
  // 函数中返回函数（柯里化函数）
  function fn(n) {
      return function (m) {
          return n + m
      }
  }
  
  // 柯里化函数改写成箭头函数
  let fn1 = (n) => (m) => n + m
  ```

  

### 箭头函数的实践和应用场景

`pass`

### 函数参数的默认值

`ES6`允许给函数参数赋值初始值

1.形参初始值 具有默认值的参数，一般要靠后（潜规则）

```js
// 函数形参默认值
function add(a, b, c = 10) {
    return a + b + c;
}
let result = add(1, 2)

let sum = (n = 0, m = 0) => n + m
```

2.与解构赋值相结合

```js
// 与解构赋值相结合
function connect({ host = "127.0.0.1", username, password, port }) {
    console.log(host, username, password, port);
}
connect({
    username: 'root',
    password: 'root',
    port: 3306
})
```

### `rest`参数

`ES6`引入`rest`参数（剩余运算符），用户获取函数的实参，用来代替arguments

```js
    // ES5获取实参的方式
    function date() {
        console.log(arguments);
    }
    date('a', 'b', 'c'); // Arguments(3) ['a', 'b', 'c', callee: ƒ, Symbol(Symbol.iterator): ƒ]

    // 箭头没有arguments（箭头函数的arguments始终是一个空类数组对象）
    let argFunc = () => {
        console.log(arguments) // 可以打印，但并没有值
    }
    argFunc(1, 2, 3, 4)

    // rest参数
    function date02(...args) {
        console.log(args); // 结果是数组，可以使用数组的一些api，filer some every map等
    }
    date02('d', 'e', 'f'); // [ 'd', 'e', 'f' ]
```

`rest`参数必须要放到参数的最后

```js
    // `rest`参数必须要放到参数的最后
    function fn(a, b, ...args) {
        console.log(a, b, args)
    }
    fn(1, 2, 3, 4, 5); //1 2 [ 3, 4, 5 ]

    // args参数任意数求和
    let sumArgs = (...args) => eval(args.join('+'))
    console.log(`sumArgs: ${sumArgs(1, 2, 3, 4, 5)}`)
```

## 扩展运算符

`...`

- `扩展运算符能将`数组`转化为逗号分隔的`参数序列

```js

//声明一个数组
const boys = ['aa','bb','cc'];
// => 'aa','bb','cc'

//声明一个函数
function chunwan(){
    console.log(arguments);
}
chunwan(boys);// Arguments [Array(3), callee: ƒ, Symbol(Symbol.iterator): ƒ]
chunwan(...boys);//Arguments(3) ["aa", "bb", "cc", callee: ƒ, Symbol(Symbol.iterator): ƒ]     chunwan('aa','bb','cc);
```

### 扩展运算符的运用

1.数组的合并

```js
//普通的数组合并
const array1 = ['aa','bb'];
const array2 = ['cc','dd'];
const array3 = array1.concat(array2);
console.log(array3);// (4) ["aa", "bb", "cc", "dd"]

const array4 = [...array1,...array2];
console.log(array4);//(4) ["aa", "bb", "cc", "dd"]
```

2.数组的克隆

```js
const testa = ['A','B','C'];
const testCopy = [...testa];

console.log(testa,testCopy,testa === testCopy); //(3) ["A", "B", "C"] (3) ["A", "B", "C"] false
```

3.将伪数组转为真正的数组

```js
const divs = document.querySelectorAll("div");
console.log(divs);/deList(3) [div, div, div]

const divArr = [...divs];
console.log(divArr);//(3) [div, div, div]
```

## Symbol的介绍与 应用

1.Symbol的值是唯一的，用来解决命名冲突的问题

2.Symbol值不能与其他数据进行运算

3.Symbol定义的对象属性不能使用for...in循环遍历，但是可以使用Reflect.ownKeys来获取对象的所键名

```
//创建Symbol
let s = Symbol();
console.log(s, typeof s); //Symbol() "symbol"

let s2 = Symbol('aa');
let s3 = Symbol('aa');
console.log(s2,s3,s2 == s3);//Symbol(aa) Symbol(aa) false

//Symbole.for创建
let s4 = Symbol.for('aa');
console.log(s4,typeof s4);//Symbol(aa) "symbol"
let s5 = Symbol.for('aa');
console.log(s4 == s5);// true

//不能与其他数据进行运算
let result = s + 100;//test.js:17 Uncaught TypeError: Cannot convert a Symbol value to a number
```

JS数据类型记忆：USONB

```
U:undefined
S:String Symbol
O:object
N:number null
B:boolean
```

### 对象添加Symbol类型的属性[¶](#symbol_1)

添加方式一：

```
//向对象添加方法 up down
let game = {
    down:function () {
        console.log('aa');
    },
    up:function(){
        console.log('cc');
    },
    name : 'bb'
}
//不能直接给对象添加up或down，因为不确定game对象中是否已经存在相同值
// game.up =function () {
//
// }
//声明一个对象
let methods = {
    up:Symbol(),
    down:Symbol()
};
//给game扩展方法
game[methods.up] = function () {
    console.log('我可以改变形状');
}
game[methods.down] = function () {
    console.log('我可以快速下降');
}
console.log(game)
// {
//     down: [Function: down],
//     up: [Function: up],
//     name: 'bb',
//     [Symbol()]: [Function],
//     [Symbol()]: [Function]
// }
```

添加方式二：

```
let youxi = {
    name:'狼人杀',
    [Symbol('say')]:function () {
        console.log('我可以发言');
    },
    [Symbol('zibao')]:function () {
        console.log('我可以自爆');
    }
}
console.log(youxi);
//{
//   name: '狼人杀',
//   [Symbol(say)]: [Function: [say]],
//   [Symbol(zibao)]: [Function: [zibao]]
// }
```

### Symbol的内置属性[¶](#symbol_2)

除了定义自己使用的Symbol值意外，ES6还提供了11个内置的Symbol值，指向语言内部使用的方法 这些属性都是Symbol的属性，而Symbol又是对象的属性，都是用来控制，对象在`特定场景`下的表现

Symbol.hasInstance|当其他对象使用instanceof运算符，判断是否为该对象的实例时，会调用这个方法 Symbol.isConcatSpreadable|对象的Symbol.isConcatSpreadable属性等于的是一个布尔值，表示该对象用于Array.prototype.concat(),是否可以展开

```
//hasInstance
class Person{
    static [Symbol.hasInstance](param){
        console.log(param)//会把参数传递进来
        console.log('我被用来检测类型了');
        return true;//可以自定义返回值
    }
}
let o ={
    name:'test'
};
console.log(o instanceof Person);
//{name: "test"}name: "test"__proto__: Object
//test.js:4 我被用来检测类型了
//test.js:11 true
const arr = [1,2,3];
const arr2 = [4,5,6];

console.log(arr.concat(arr2));//(6) [1, 2, 3, 4, 5, 6]

arr2[Symbol.isConcatSpreadable] = false;
console.log(arr.concat(arr2));(4) [1, 2, 3, Array(3)]
```

### 迭代器介绍[¶](#_9)

迭代器是一种接口，为各种不同的数据结构提供统一的访问机制。任何数据结构只要部署Iterator接口，就可以完成遍历操作。 （Iterator接口本质就是对象的一个属性，就是Symbol.Iterator)

1) ES6创造了一种新的遍历命令for...of循环，Iterator接口主要提供for...of消费

2) 原生具有iterator接口的数据（可用for of遍历）

```
a) Array

b) Arguments

c) Set

d) Map

e) String

f) TypedArray

g) NodeList
```

3) 工作原理

a) 创建一个指针对象，指向当前数据结构的起始位置

b) 第一次调用对象的next方法，指针自动指向数据结构的第一个成员

c) 接下来不断调用next方法，指针一直往后移动，直到指向最后一个成员

```
（Iterator接口本质就是对象的一个属性，就是Symbol.Iterator)
```

`注意`需要自定义遍历数据的时候，要想到迭代器

### 自定义迭代器[¶](#_10)

```
const banji = {
    name:"终极一班",
    stus:[
        'xiaoing',
        'xiaoning',
        'xiaotian',
        'knigth'
    ],
    [Symbol.iterator](){
        //索引变量
        let index = 0;

        let _this = this;
        return {
            next:function () {
                if(index < _this.stus.length){
                    const result = {value:_this.stus[index],done:false};
                    index++;
                    return result;
                }else{
                    return {value: undefined,done: true};
                }
            }
        }
    }
}
//遍历这个对象
for(let v of banji){
    console.log(v);
}
// xiaoing
// xiaoning
// xiaotian
// knigth
```

### 生成器函数声明与调用[¶](#_11)

```
//定义生成器函数
function * gen() {
    // console.log(111);
    yield 'aaa';
    // console.log(222);
    yield 'bbb';
    // console.log(333);
    yield 'ccc';
    // console.log(444);
}

let iterator = gen();
//生成器函数通过next()调用
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());

// { value: 'aaa', done: false }
// { value: 'bbb', done: false }
// { value: 'ccc', done: false }
// { value: undefined, done: true }


//遍历
for(let v of gen()){
    console.log(v);
}
```

### 生成器函数的参数传递[¶](#_12)

```
function * gen(arg) {
    console.log(arg);
    let one = yield 111;
    console.log(one);
    let two = yield 222;
    console.log(two);
    let three = yield 333;
    console.log(three);
}
//执行获取迭代器对象
let iterator = gen('AAA');
console.log(iterator.next())
//next()方法可以传入实参
console.log(iterator.next('BBB'));
console.log(iterator.next('CCC'));
console.log(iterator.next('DDD'));
```

### 生成器函数实例[¶](#_13)

常见的异步操作有：

异步编程 文件操作 网络操作（ajax,request） 数据库操作

```
//1s后控制台输出111,2s后控制台输出222,3s后控制台输出333
//回调地狱
setTimeout(() =>{
    console.log(111);
    setTimeout(() => {
        console.log(222);
        setTimeout(() => {
            console.log(333);
        },3000)
    },2000)
},1000)
```

使用生成器函数解决

```
// 异步编程  文件操作  网络操作（ajax,request）  数据库操作

//1s后控制台输出111,2s后控制台输出222,3s后控制台输出333
//回调地狱
// setTimeout(() =>{
//     console.log(111);
//     setTimeout(() => {
//         console.log(222);
//         setTimeout(() => {
//             console.log(333);
//         },3000)
//     },2000)
// },1000)

function one() {
    setTimeout(() =>{
        console.log(111);
        iterator.next();
    },1000)
}

function two() {
    setTimeout(() => {
        console.log(222);
        iterator.next();
    },2000)
}

function three() {
    setTimeout(() => {
        console.log(333);
        iterator.next();
    },3000)
}

function * gen() {
    yield one();
    yield two();
    yield three();
}

//调用生成器函数
let iterator = gen();
iterator.next();
```

### 生成器函数实例2[¶](#2)

```
//模拟获取  用户数据  订单数据  商品数据
function getUsers(){
    setTimeout(() => {
        let data = '用户数据';
        iterator.next(data);
    },1000)
}
function getOrders() {
    setTimeout(() => {
        let data = '订单数据';
        iterator.next(data);

    },1000)
}
function getGoods() {
    setTimeout(() => {
        let data = '商品数据';
        iterator.next(data);
    },1000)
}

function * gen() {
    let users = yield getUsers();
    console.log(users);

    let orders = yield getOrders();
    console.log(orders);

    let goods = yield getGoods();
    console.log(goods);
}

let iterator = gen();
iterator.next();
```

## Promise

> 手写Promise见《Promise》篇

### Promise介绍与基本使用

Promise是ES6引入的异步编程的新解决方案。

语法上Promise是一个构造函数，用来封装异步操作并且可以获取其成功或者失败的结果

```
//实例化Promise对象
const p = new Promise(function (resolve,reject) {
    setTimeout(() =>{
        // let data = '数据库中的用户数据';
        // resolve(data);

        let err = '数据读取失败';
        reject(err);
    },1000);
})
//调用Promise对象的then方法
p.then(function (value) {
    console.log(value);
},function (reason) {
    console.log(reason);//数据读取失败
})
```

### Promise封装读取文件

普通方法调用

```
//引入fs模块
const fs = require('fs');

//调用方法读取文件
fs.readFile('为学.md',(err,data) => {
    if(err) throw err;
    console.log(data.toString())
});
// 为学
// 天下事有难易乎？
// 为之，则难者亦易矣，
// 不为，则易者亦难矣
```

使用Promise封装调用

```
const p = new Promise(function (resolve,reject) {
    fs.readFile('为学.mdaa',(err,data) => {
        if(err) reject(err);
        resolve(data);
    })
});

p.then(function (value) {
    console.log(value.toString());
},function (reason) {
    console.log('读取失败');
})
//读取失败
```

### 使用Promise封装ajax请求

需要放在html里面

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<script>
    const p = new Promise(function (resolve,reject) {
        //1.创建对象
        const xhr = new XMLHttpRequest();
        //2.初始化
        xhr.open('GET','https://api.apiopen.top/getJoke');
        //3.发送
        xhr.send();
        //4.绑定事件，处理响应结果
        xhr.onreadystatechange = function () {
            //判断
            if(xhr.readyState === 4){
                //判断响应状态码 200 ~ 299
                if(xhr.status >= 200 && xhr.status < 300){
                    //表示成功
                    resolve(xhr.response);
                }else {
                    //如果失败
                    reject(xhr.status);
                }

            }
        }
    });
    p.then(function (value) {
        console.log(value);
    },function (reason) {
        console.error(reason);
    })
</script>
</body>
</html>
```

### Promise.prototype.then方法

then方法的返回值

```
//创建Proise对象
const p = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('用户数据')
        // reject('出错啦');
    },1000);
});

//调用then方法 then方法  then方法的返回结果是Promise对象，对象状态是由回调函数的执行结果决定的
//1.如果回调函数中，返回的结果是非Promise类型的属性，状态为成功，返回值为对象的成功的值（undefined）
const result = p.then((value)=> {
    console.log(value);
    //1.非promise类型的属性
    // return 'iloveyou';
    //2.是Promise对象
    // return new Promise((resolve,reject) => {
    //     // resolve('ok');
    //     reject('error');
    // });
    //3.抛出错误
    // throw '出错啦';
},(reason)=>{
    console.warn(reason);
});

console.log(result)
```

链式调用

```
p.then(value => {

}).then(value => {

})
```

### Promise实践练习

```
//引入fs模块
const fs = require('fs');

fs.readFile('为学.md',(err,data1 )=> {
    fs.readFile('插秧诗.md',(err,data2) => {
        fs.readFile('观书有感.md',(err,data3) => {
            let result = data1 + '\r\n' + data2 + '\r\n' + data3 + '\r\n';
            // console.log(result);
        })
    })
})

//使用Promise实现
const p = new Promise((resolve,reject) => {
    fs.readFile('为学.md',(err,data) => {
        resolve(data);
    });
});

p.then(value => {
    // console.log(value.toString())
    return new Promise((resolve,reject) => {
        fs.readFile('插秧诗.md',(err,data) => {
            resolve([value,data]);
        });
    })
}).then(value => {
    return new Promise((resolve,reject) => {
        fs.readFile('观书有感.md',(err,data) => {
            //压入
            value.push(data);
            resolve(value.join('\r\n'));
        });
    })
}).then(value => {
    console.log(value);
})
/*
为学
天下事有难易乎？
为之，则难者亦易矣，
不为，则易者亦难矣
插秧诗
手把青秧插满田，低头便见水中天。
六清净方为道，退步原来是向前。
观书有感二首
其一
半亩方塘一鉴开，天光云影共徘徊。
问渠那得清如许？为有源头活水来。
其二
昨夜江边春水生，艨艟巨舰一毛轻。
向来枉费推移力，此日中流自在行。*/
```

### Promise对象catch方法

```
const p = new Promise((resolve,reject) => {
    setTimeout(() => {
        //设置p对象的状态为失败
        reject('出错啦');
    },1000);
});

//p.then((value) => {
//
//},(reason) => {
//    console.error(reason);
//});

//相当于是一种语法糖
p.catch((reason) => {
    console.warn(reason)
});
```



## await

## 集合

### 集合介绍与API[¶](#api)

```
//声明一个集合
let s = new Set();
console.log(s);//Set {}

let s1 = new Set(['a','b','c','b','d','e','a']);
console.log(s1);//Set {"a", "b", "c", "d", "e"}

//元素个数
console.log(s1.size);//5

//添加新元素
s1.add('f');
console.log(s1);

//删除元素
s1.delete('a');
console.log(s1);//Set {"b", "c", "d", "e", "f"}

//检测
console.log(s1.has('a'));//false
console.log(s1.has('b'));//true

//循环遍历集合元素
for(let v of s1){
    console.log(v);
}
```

### 集合实践[¶](#_14)

```
let arr1 = [1,2,3,4,5,4,3,2,1];

//1.数组去重
//let result = [...new Set(arr)];
//console.log(result);//[1, 2, 3, 4, 5]

//2.交集
let arr2 = [4,5,6,5,6];
//let result2 = [...new Set(arr)].filter(item => {
//    let s2 = new Set(arr2);//4 5 6
//    if(s2.has(item)){
//        return true;//如果为真，表示既在数组一，也在数组二；
//    }else{
//        return false;
//    }
//});

//简写
//let result2 = [...new Set(arr)].filter(item => new Set(arr2).has(item));
//console.log(result2)//4 5

//3.并集
//let union = [...new Set([...arr,...arr2])];
//console.log(union);//[1, 2, 3, 4, 5, 6]

//4.差集，谁是主体，求出来的结果是不一样的
let diff = [...new Set(arr1)].filter(item => !(new Set(arr2).has(item)));
console.log(diff);//[1, 2, 3]  这里是1对2求差集，表示1里面有，而2里面没有的
```

### Map的介绍与API[¶](#mapapi)

ES提供了Map数据结构。它类似于对象，也是键值对的集合，但是“键”的范围不限于字符串，各种类型的值（包括对象）都可以当作键。Map也实现了iterator接口，所以可以使用`扩展运算符`和`for of`进行遍历。

Map的属性和方法：

```
1)size 返回Map的元素的个数

2)set 增加一个新元素，返回当前Map

3)get 返回键名对象的键值

4)has 检测Map中是否包含某个元素，返回boolean值

5)clear 清空集合，返回undefined
//声明Map
let m = new Map();

console.log(m);//Map {}

//添加元素
m.set('name','xiaoming');
m.set('change',function () {
    console.log('我可以改变你');
});

console.log(m);//Map { 'name' => 'xiaoming', 'change' => [Function] }
```

### class类[¶](#class)

ES6提供了更接近传语言的写法，引入了Class（类）这个概念，作为对象的模板；

通过class关键字，可以定义类。基本上，ES6的class可以看做只是一个语法糖，它的绝大部分功能，ES5都可以做到，新的class写法只是让对象原型的写法更加清晰、更像面向对象编程的语法而已

```
1) class声明类

2） constructor定义构造函数初始化

3) extends继承父类

4) super调用父级构造方法

5) static定义静态方法和属性

6)父类方法可以重写
```

ES5 实例化对象的写法

```
//手机
function Phone(brand, price){
    this.brand = brand;
    this.price = price;
}

//添加方法
Phone.prototype.call = function() {
  console.log('我可以打电话');
};

//实例化对象
let HUAWEI = new Phone('HUAWEI','2999');
HUAWEI.call();
console.log(HUAWEI);
```1
ES6的写法
```javascript
class Phone{
    //构造方法 名字不能修改
    constructor(brand, price){
        this.brand = brand;
        this.price = price;
    }


    //方法必须使用该语法，不能使用ES5的对象完整形式
    call(){
        console.log('我可以打电话');
    }
}

let onePlus = new Phone("1+", 1999);
console.log(onePlus);
```

### class静态成员[¶](#class_1)

函数对象的属性，是属于类的，并不属于实例对象的属性，这样的属性称为`静态成员`

```
function Phone(){

}
Phone.name = '手机';
Phone.change = function () {
    console.log('我可以改变世界');
}

let nokia = new Phone();
//console.log(nokia.name);//undefined
//nokia.change();//Uncaught TypeError: nokia.change is not a function

Phone.prototype.size = '5.5inch';
console.log(nokia.size);//5.5inch
class Phone{
    //静态属性
    static name = '手机';
    static change(){
        console.log('我可以改变世界');
    }
}

let nokia = new Phone();
console.log(nokia.name);//undefined
console.log(Phone.change);
//ƒ change(){
//        console.log('我可以改变世界');
//}
```

### ES6-ES5构造函数继承[¶](#es6-es5)

ES5构造函数继承

```
//手机
function Phone(brand, price) {
    this.brand = brand;
    this.price = price;
}
Phone.prototype.call = function () {
    console.log('我可以打电话');
}

//智能手机
function SmartPhone(brand,price,color,size){
    Phone.call(this,brand,price);
    this.color = color;
    this.size = size;
}

//设置子级构造函数的原型
SmartPhone.prototype = new Phone;
//做一下校正
SmartPhone.prototype.constructor = SmartPhone;

//声明子类的方法
SmartPhone.prototype.photo = function () {
    console.log('我可以拍照片');
}
SmartPhone.prototype.playGame = function () {
    console.log('我可以打游戏');
}
const chuizi = new SmartPhone('锤子',2499,'黑色','5.5inch');
console.log(chuizi)
// SmartPhone
//     brand: "锤子"
//     color: "黑色"
//     price: 2499
//     size: "5.5inch"
//     __proto__: Phone
```

### ES6-class的类继承[¶](#es6-class)

ES6继承

```
class Phone{
    //构造方法
    constructor(brand,price) {
        this.brand = brand;
        this.price = price;
    }
    //父类的成员属性
    call(){
        console.log('我可以打电话！')
    }
}
class SmartPhone extends Phone{
    //构造方法
    constructor(brand,price,color,size) {
        super(brand,price);//Phone.call(this,brand,price);
        this.color = color;
        this.size = size;
    }

    photo(){
        console.log('拍照片');
    }
    playGame(){
        console.log('玩游戏')
    }
}

const xiaomi = new SmartPhone('小米',799,'黑色','4.7inch');
console.log(xiaomi)
// SmartPhone {brand: "小米", price: 799, color: "黑色", size: "4.7inch"}
//     brand: "小米"
//     color: "黑色"
//     price: 799
//     size: "4.7inch"
//     __proto__: Phone
```

### 子类对父类方法的重写[¶](#_15)

```
class Phone{
    //构造方法
    constructor(brand,price) {
        this.brand = brand;
        this.price = price;
    }
    //父类的成员属性
    call(){
        console.log('我可以打电话！')
    }
}
class SmartPhone extends Phone{
    //构造方法
    constructor(brand,price,color,size) {
        super(brand,price);//Phone.call(this,brand,price);
        this.color = color;
        this.size = size;
    }

    photo(){
        console.log('拍照片');
    }
    playGame(){
        console.log('玩游戏')
    }
    call() {
        // super() 子类中不能直接调用父类的同名方法，只能重写
        console.log('我可以视频通话');
    }
}

const xiaomi = new SmartPhone('小米',799,'黑色','4.7inch');
console.log(xiaomi)
// SmartPhone {brand: "小米", price: 799, color: "黑色", size: "4.7inch"}
//     brand: "小米"
//     color: "黑色"
//     price: 799
//     size: "4.7inch"
//     __proto__: Phone
xiaomi.call();//我可以视频通话+
```

### class中getter和setter的设置[¶](#classgettersetter)

```
//get 和 set
class Phone {

    //对属性进行读取时，将会调用该方法
    //通常是对动态的属性进行封装
    get price(){
        console.log('价格属性被读取了');
        return 'iloveyou';
    }

    //对属性进行设置时，将会调用该方法
    //可以添加更多的控制和判断
    set price(newVal){
        console.log('价格属性被修改了');
    }
}

//实例化对象
let s = new Phone();
console.log(s.price);
//价格属性被读取了
//iloveyou  get中的返回值，将会被读取到


s.price = 'free';//价格属性被修改了
```

### ES6的数值扩展[¶](#es6)

### ES6的对象方法扩展[¶](#es6_1)

### 模块化介绍、优势及产品[¶](#_16)

CommonJs => NodeJs、Browserify

### 浏览器使用ES6模块化引入模块[¶](#es6_2)

m1.js

```
export let school = 'sgg';

export function teach() {
    console.log('we can teach you');
}
```

test.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<script type="module">
    //引入m1.js
    import * as m1 from './m1.js';
    console.log(m1)
    // Module
    // school: (...)
    // teach: (...)
    // Symbol(Symbol.toStringTag): "Module"
    // get school: ƒ ()
    // set school: ƒ ()
    // get teach: ƒ ()
    // set teach: ƒ ()
</script>
</body>

</html>
```

### ES6模块暴露数据语法汇总[¶](#es6_3)

```
//分别暴露
export let school = 'sgg';

export function teach() {
    console.log('we can teach you');
}
//统一暴露
let school = 'sgg';

function teach() {
    console.log('we can teach you');
}

export {school,teach};
//默认暴露
export default {
    school: 'sgg',
    teach: function () {
        console.log('we can teach you');
    }
}
```

这种暴露数据的方法，在调用时需要多加一层default

```
m1.default.change();
```

### ES6引入模块数据语法汇总[¶](#es6_4)

```
<script type="module">
    //1.通用的导入方式
    import * as m1 from './m1.js';

    //2.解构赋值
    import {school,teach} from './m1.js';
    import {school as school2,teach as teach2} from './m2.js';

    //3.简便形式，针对默认暴露
    import m1 from'./m1.js';
    console.log(m1)
</script>
```

### 浏览器使用ES6模块二[¶](#es6_5)

入口文件app.js

```
//入口文件

//模块引入
import * as m1 from './m1.js';
import * as m2 from './m2.js';
import * as m3 from './m3.js';
```

引入入口文件

```
<script src="app.js" type="module"></script>
```

# JS常用API

## Math常用方法

### 绝对值方法

`Math.abs()`

> 获取绝对值，绝对值永远是正数或者零

```js
console.log(Math.abs(-12.5)) // 12.5
console.log(Math.abs(12)) // 12
console.log(Math.abs(0)) // 0

// 传递的不是数字类型的值，先基于Number()转换为数字类型再处理
console.log(Math.abs('-1')) // 1
console.log(Math.abs('-1px')) // NaN
console.log(Math.abs(true)) // 1
```

### 舍入方法

`Math.ceil()`

> 方法始终向上舍入为最接近的整数

```js
console.log(Math.ceil(25.1)) // 26
console.log(Math.ceil(25.9)) // 26
console.log(Math.ceil(-25.9)) // -25
console.log(Math.ceil(-25.1)) // -25
```

`Math.floor()`

> 方法始终向下舍入为最接近的整数

```js
console.log(Math.floor(25.1)) // 25
console.log(Math.floor(25.9)) // 25
console.log(Math.floor(-25.9)) // -26
console.log(Math.floor(-25.1)) // -26
```

`Math.round()`

> 方法执行四舍五入

```js
console.log(Math.round(25.1)) // 25
console.log(Math.round(25.5)) // 26，正数里是进一位
console.log(Math.round(25.9)) // 26

console.log(Math.round(-25.9)) // -26
console.log(Math.round(-25.5)) // -25，负数里是舍去的
console.log(Math.round(-25.1)) // -25
```

`Math.fround()`

> 方法返回数值最接近的单精度（32 位）浮点值表示

### 最值方法

min()和 max()方法用于确定一组数值中的最小值和最大值

- 输入必须是一个个的值的形式
- 不能直接求数组的最值，可以用扩展操作符展开

```js
let max = Math.max(3, 54, 32, 16)
let min = Math.min(3, 54, 32, 16)
console.log(max, min) // 54, 3

let arr = [3, 54, 32, 16]
console.log(Math.max(arr)) // NaN
console.log(Math.max(...arr)) // 54

```

### 随机数方法

`Math.random()`

> 方法返回一个 0~1 范围内的随机数，其中包含 0 但不包含

基于如下公式使用 Math.random()从一组整数中

随机选择一个数：

```js
number = Math.floor(Math.random() * total_number_of_choices + first_possible_value) 
```

如果想从 1~10 范围内随机选择一个数，代码就是这样的：

```js
let num = Math.floor(Math.random() * 10 + 1);
```

如果想选择一个 2~10 范围内的值，则代码就

要写成这样：

```js
let num = Math.floor(Math.random() * 9 + 2); 
```

封装成函数

```js
function selectFrom(lowerValue, upperValue) { 
 let choices = upperValue - lowerValue + 1; 
 return Math.floor(Math.random() * choices + lowerValue); 
} 
let num = selectFrom(2,10); 
console.log(num); // 2~10 范围内的值，其中包含 2 和 10
```

应用，取数组的随机项

```js
let colors = ["red", "green", "blue", "yellow", "black", "purple", "brown"]; 
let color = colors[selectFrom(0, colors.length-1)];
```

> `Math.random()`方法在这里出于演示目的是没有问题的。如果是为了加密而需要生成随机数（传给生成器的输入需要较高的不确定性），那么建议使用 `window.crypto. getRandomValues()`。

```js
var array = new Uint32Array(10);
window.crypto.getRandomValues(array);

console.log("Your lucky numbers:");
for (var i = 0; i < array.length; i++) {
    console.log(array[i]);
}
```

### 其他

![image-20221114203722124](image-20221114203722124.png)



## Array常用方法

- 方法的作用和含义
- 方法的实参（类型和含义）
- 方法的返回值

### 栈方法

- `push()`

  > `push()`方法接收任意数量的参数，并将它们添加到数组末尾，返回数组的最新长度
  >
  > `@params`：多个任意类型
  >
  > `@return`：新增数组后的长度
  
  ```js
  let colors = new Array(); // 创建一个数组
  let count = colors.push("red", "green"); // 推入两项
  alert(count); // 2 
  count = colors.push("black"); // 再推入一项
  alert(count); // 3	
  ```
  
  基于原生JS，也可以向末尾追加内容，但效率不如直接提供的push方法
  
  ```js
  arr[arr.length] = newValue
  ```

- `pop()`

  > pop()方法用于删除数组的最后一项，同时减少数组的 length 值，返回被删除的项

  ```js
  let item = colors.pop(); // 取得最后一项
  alert(item); // black 
  alert(colors.length); // 2
  ```
  
  `arr.length--`，也可以实现删除数组最后一项
  
  ```js
  let arr = [12, 34, 56, 78]
  arr.length--
  console.log(arr) // [12, 34, 56]
  ```

### 队列方法

有了在数据末尾添加数据的 `push()`方法，所以要模拟队列就差一个从数组开头取得数据的方法了

- `shift()`

  > 它会删除数组的第一项并返回它，然后数组长度减 1

  ```js
  let colors = new Array(); // 创建一个数组
  let count = colors.push("red", "green"); // 推入两项
  alert(count); // 2 
  count = colors.push("black"); // 再推入一项
  alert(count); // 3 
  
  let item = colors.shift(); // 取得第一项
  alert(item); // red 
  alert(colors.length); // 2
  ```

- `unshift()`

  > 在数组开头添加任意多个值，然后返回新的数组长度

  ```js
  let colors = new Array(); // 创建一个数组
  let count = colors.unshift("red", "green"); // 从数组开头推入两项
  alert(count); // 2 
  count = colors.unshift("black"); // 再推入一项
  alert(count); // 3 
  
  let item = colors.pop(); // 取得最后一项
  alert(item); // green 
  alert(colors.length); // 2
  ```

  

### `concact()`：合并数组

- 可以在现有数组全部元素基础上创建一个新数组。

- 它首先会创建一个当前数组的副本，然后再把它的参数添加到副本末尾，最后返回这个新构建的数组。

  - 如果传入一个或多个数组，则 `concat()`会把这些数组的每一项都添加到结果数组。
  - 如果参数不是数组，则直接把它们添加到结果数组末尾。

  ```js
  let colors = ["red", "green", "blue"]; 
  let colors2 = colors.concat("yellow", ["black", "brown"]); 
  console.log(colors); // ["red", "green","blue"] 
  console.log(colors2); // ["red", "green", "blue", "yellow", "black", "brown"]
  ```

- 打平数组

- 操作不影响原始数组

### 操作方法

- `slice()`：截取数组

  - 创建一个包含原有数组中一个或多个元素的新数组


  - 可以接收一个或两个参数：返回元素的开始索引和结束索引。

    - 如果只有一个参数，则 `slice()`会返回该索引到数组末尾的所有元素。
    - 如果有两个参数，则 `slice()`返回从开始索引到结束索引对应的所有元素，其中不包含结束索引对应的元素（左闭右开）。

    ```js
    let colors = ["red", "green", "blue", "yellow", "purple"]; 
    let colors2 = colors.slice(1); 
    let colors3 = colors.slice(1, 4); 
    alert(colors2); // green,blue,yellow,purple 
    alert(colors3); // green,blue,yellow
    ```


  - 如果 `slice()`的参数有负值，那么就以数值长度加上这个负值的结果确定位置。

    - 比如，在包含 5 个元素的数组上调用 `slice(-2,-1`)，就相当于调用 slice(3,4)。
    - 如果结束位置小于开始位置，则返回空数组。


  - 操作不影响原始数组


- `splice()`：删除、插入或替换数组元素

  - 删除：

    - 需要给 `splice()`**传 2 个参数**：要删除的第一个元素的位置和要删除的元素数量。

    - 可以从数组中删除任意多个元素，比如 `splice(0, 2)`会删除前两个元素。

    - 清空数组

      ```js
      let arr = [12, 34, 56, 78]
      let res = arr.splice(0) // 没有第二个参数，默认是数组的长度
      
      console.log(arr, res) // [], [12, 34, 56, 78]
      ```

    - 删除第一项和最后一项

      ```js
      let arr = [12, 34, 56, 78]
      arr.splice(arr.length - 1)
      arr.splice(0, 1)
      
      console.log(arr) // [34, 56]
      ```

  - 插入

    > 需要给 `splice()`传 3 个参数：开始位置、0（要删除的元素数量）和要插入的元素，可以在数组中指定的位置插入元素。
    >
    > 第三个参数之后还可以传第四个、第五个参数，乃至任意多个要插入的元素。

    比如，`splice(2, 0, "red", "green")`会从数组位置 2 开始插入字符串"`red`"和"`green`"。

    向数组末尾/开头追加

    ```js
    let arr = [12, 34, 56, 78]
    arr.splice(arr.length, 0, 'AA')
    
    console.log(arr) // [12, 34, 56, 78, 'AA']
    
    arr.splice(0, 0, 'BB')
    console.log(arr) // ['BB', 12, 34, 56, 78, 'AA']
    ```

  - 替换（先删除，再替换）

    > `splice()`在删除元素的同时可以在指定位置插入新元素，同样要传入 3 个参数：开始位置、要删除元素的数量和要插入的任意多个元素。
    >
    > 要插入的元素数量不一定跟删除的元素数量一致。

    比如，`splice(2, 1, "red", "green")`会在位置 2 删除一个元素，然后从该位置开始向数组中插入"red"和"green"。

  - 我的思考：

    - 只要第二个参数不为0，就是删除元素了
    - 只要有两个以上的参数，就是插入元素了
    - 具体删了谁，插入了谁，在哪个位置插入的，看具体参数的值即可


  - 返回值

    > `splice()`方法始终返回这样一个数组，它包含从数组中被删除的元素（如果没有删除元素，则返回空数组）。

    ```js
    let colors = ["red", "green", "blue"]; 
    let removed = colors.splice(0,1); // 删除第一项
    console.log(colors); // green,blue 
    console.log(removed); // red，只有一个元素的数组
    
    removed = colors.splice(1, 0, "yellow", "orange"); // 在位置 1 插入两个元素，原来在位置1的blue被挤后面去了
    console.log(colors); // green,yellow,orange,blue 
    console.log(removed); // 空数组
    
    removed = colors.splice(1, 1, "red", "purple"); // 插入两个值，删除一个元素
    console.log(colors); // green,red,purple,orange,blue 
    console.log(removed); // yellow，只有一个元素的数组
    ```

  - 操作会影响到原数组


### `delete`

`delete`方法，把数组当做普通对象，确实可以删除某一项内容，但是不会影响数组本身的数据结构特点（`length`长度不会跟着改变），真实项目中杜绝使用

```js
let arr = [12, 34, 56, 78]
delete arr[0]
console.log(arr)
```

![image-20221115060441857](image-20221115060441857.png)

## Object常用方法

### `Object.create()`

> 方法用于创建一个新对象，使用现有的对象来作为新创建对象的原型（prototype）。

```js
const person = {
  isHuman: false,
  printIntroduction: function() {
    console.log(`My name is ${this.name}. Am I human? ${this.isHuman}`);
  }
};

const me = Object.create(person);

me.name = 'Matthew'; // "name" is a property set on "me", but not on "person"
me.isHuman = true; // inherited properties can be overwritten

me.printIntroduction();
// expected output: "My name is Matthew. Am I human? true"

```

我们可以在新建对象后打印`me`对象，看一下：

```js
const person = {
  isHuman: false,
  printIntroduction: function() {
    console.log(`My name is ${this.name}. Am I human? ${this.isHuman}`);
  }
};

const me = Object.create(person);
console.dir(me)
```

在没有添加属性之前，`me`对象就是一个以`person`对象为原型的空对象

![image-20220714091058110](image-20220714091058110.png)

也可以在`me`对象上重写`person`身上的方法，并不会覆盖原型对象上的方法

### `Object.entries`

> 遍历对象的，将`key-value`的形式，转换成二维数组

![image-20220629110203985](/image-20220629110203985.png)

### `Object.keys()`

### `Object.values`

### `Object.assign()`

https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/assign

#### 语法

```js
Object.assign(target, ...sources) 
```

- 参数

  - `target`

    目标对象，接收源对象属性的对象，也是修改后的返回值。

  - `sources`

    源对象，包含将被合并的属性。

- 返回值

  - 目标对象，即函数的返回值是合并后的`target`

#### 描述

如果目标对象与源对象具有相同的 [key](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)，则目标对象中的属性将被源对象中的属性覆盖，后面的源对象的属性将类似地覆盖前面的源对象的属性。

`Object.assign` 方法只会拷贝源对象 *可枚举的* 和 *自身的* 属性到目标对象。该方法使用源对象的 `[[Get]]` 和目标对象的 `[[Set]]`，它会调用 [getters](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Functions/get) 和 [setters](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Functions/set)。故它分配属性，而不仅仅是复制或定义新的属性。如果合并源包含 getters，这可能使其不适合将新属性合并到原型中。

为了将属性定义（包括其可枚举性）复制到原型，应使用 [`Object.getOwnPropertyDescriptor()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyDescriptor) 和 [`Object.defineProperty()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)，基本类型 [`String`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String) 和 [`Symbol`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Symbol) 的属性会被复制。

如果赋值期间出错，例如如果属性不可写，则会抛出 [`TypeError`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/TypeError)；如果在抛出异常之前添加了任何属性，则会修改 `target` 对象（译者注：换句话说，`Object.assign()` 没有“回滚”之前赋值的概念，它是一个尽力而为、可能只会完成部分复制的方法）。

> **备注：** `Object.assign()` 不会在 `source` 对象值为 [`null`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/null) 或 [`undefined`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/undefined) 时抛出错误。

#### 示例

##### 复制对象

```js
const obj = { a: 1 };
const copy = Object.assign({}, obj);
console.log(copy); // { a: 1 }

```

##### 深拷贝问题

针对[深拷贝 (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/Deep_copy), 需要使用其他办法，因为 `Object.assign()` 只复制属性值。

假如源对象是一个对象的引用，它仅仅会复制其引用值。

```js
function test() {
  'use strict';

  let obj1 = { a: 0 , b: { c: 0}};
  let obj2 = Object.assign({}, obj1);
  console.log(JSON.stringify(obj2)); // { "a": 0, "b": { "c": 0}}

  obj1.a = 1;
  console.log(JSON.stringify(obj1)); // { "a": 1, "b": { "c": 0}}
  console.log(JSON.stringify(obj2)); // { "a": 0, "b": { "c": 0}}

  obj2.a = 2;
  console.log(JSON.stringify(obj1)); // { "a": 1, "b": { "c": 0}}
  console.log(JSON.stringify(obj2)); // { "a": 2, "b": { "c": 0}}

  obj2.b.c = 3;
  console.log(JSON.stringify(obj1)); // { "a": 1, "b": { "c": 3}}
  console.log(JSON.stringify(obj2)); // { "a": 2, "b": { "c": 3}}

  // Deep Clone
  obj1 = { a: 0 , b: { c: 0}};
  let obj3 = JSON.parse(JSON.stringify(obj1));
  obj1.a = 4;
  obj1.b.c = 4;
  console.log(JSON.stringify(obj3)); // { "a": 0, "b": { "c": 0}}
}

test();

```

##### 合并对象

```js
const o1 = { a: 1 };
const o2 = { b: 2 };
const o3 = { c: 3 };

const obj = Object.assign(o1, o2, o3);
console.log(obj); // { a: 1, b: 2, c: 3 }
console.log(o1);  // { a: 1, b: 2, c: 3 }, target object itself is changed.
console.log(o1 === obj) // true
```

##### 合并具有相同属性的对象

```js
const o1 = { a: 1, b: 1, c: 1 };
const o2 = { b: 2, c: 2 };
const o3 = { c: 3 };

const obj = Object.assign({}, o1, o2, o3);
console.log(obj); // { a: 1, b: 2, c: 3 }

```

属性会被后续参数中具有相同属性的其他对象覆盖。

##### 拷贝 `Symbol` 类型属性

```js
const o1 = { a: 1 };
const o2 = { [Symbol('foo')]: 2 };

const obj = Object.assign({}, o1, o2);
console.log(obj); // { a : 1, [Symbol("foo")]: 2 } (cf. bug 1207182 on Firefox)
Object.getOwnPropertySymbols(obj); // [Symbol(foo)]

```

##### 原型链上的属性和不可枚举属性不能被复制

```js
const obj = Object.create({ foo: 1 }, { // foo is on obj's prototype chain.
  bar: {
    value: 2  // bar is a non-enumerable property.
  },
  baz: {
    value: 3,
    enumerable: true  // baz is an own enumerable property.
  }
});

console.log(obj) // {baz: 3, bar: 2} 另外：{foo: 1}在obj的原型链上

const copy = Object.assign({}, obj);
console.log(copy); // { baz: 3 }
```

##### 基本类型会被包装为对象

```js
const v1 = 'abc';
const v2 = true;
const v3 = 10;
const v4 = Symbol('foo');

const obj = Object.assign({}, v1, null, v2, undefined, v3, v4);
// Primitives will be wrapped, null and undefined will be ignored.
// Note, only string wrappers can have own enumerable properties.
console.log(obj); // { "0": "a", "1": "b", "2": "c" }

```

##### 异常会打断后续拷贝任务

```js
const target = Object.defineProperty({}, 'foo', {
  value: 1,
  writable: false
}); // target.foo is a read-only property

Object.assign(target, { bar: 2 }, { foo2: 3, foo: 3, foo3: 3 }, { baz: 4 });
// TypeError: "foo" is read-only
// The Exception is thrown when assigning target.foo

console.log(target.bar);  // 2, the first source was copied successfully.
console.log(target.foo2); // 3, the first property of the second source was copied successfully.
console.log(target.foo);  // 1, exception is thrown here.
console.log(target.foo3); // undefined, assign method has finished, foo3 will not be copied.
console.log(target.baz);  // undefined, the third source will not be copied either.

```

![image-20221114205656441](image-20221114205656441.png)

##### 拷贝访问器

如果源对象里有`getter`，正常情况下会返回`getters`的值

现在希望把`getters`的访问器属性也整到目标对象中，定义了`completeAssign`方法

```js
const obj = {
  foo: 1,
  get bar() {
    return 2;
  }
};

let copy1 = Object.assign({}, obj);
console.log(copy1);
// { foo: 1, bar: 2 }
// The value of copy.bar is obj.bar's getter's return value.

// This is an assign function that copies full descriptors
function completeAssign(target, ...sources) {
  sources.forEach(source => {
    let descriptors = Object.keys(source).reduce((descriptors, key) => {
      descriptors[key] = Object.getOwnPropertyDescriptor(source, key);
      return descriptors;
    }, {});

    // By default, Object.assign copies enumerable Symbols, too
    Object.getOwnPropertySymbols(source).forEach(sym => {
      let descriptor = Object.getOwnPropertyDescriptor(source, sym);
      if (descriptor.enumerable) {
        descriptors[sym] = descriptor;
      }
    });
    Object.defineProperties(target, descriptors);
  });
  return target;
}

copy2 = completeAssign({}, obj);
console.log(copy2);
// { foo:1, get bar() { return 2 } }

```

#### 参见

- [Polyfill of `Object.assign` in `core-js`](https://github.com/zloirock/core-js#ecmascript-object)
- [`Object.defineProperties()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperties)
- [属性的可枚举性和所有权](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Enumerability_and_ownership_of_properties)
- [构造字面量对象时使用展开语法](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Spread_syntax#构造字面量对象时使用展开语法)

## Date常用方法

Date对象用于处理日期和时间。

创建Date对象的语法：

```
var myDate=new Date()
```

注释：Date 对象会自动把当前日期和时间保存为其初始值。

date对象获取时间日期的方法如下：

```js
// 获取当前日期时间
var myDate = new Date();
myDate.toLocaleDateString();                //获取当前日期
var mytime=myDate.toLocaleTimeString();     //获取当前时间
myDate.toLocaleString( );                   //获取日期与时间
 
myDate.getYear();                //获取当前年份(2位)
myDate.getFullYear();            //获取完整的年份(4位,1970-????)
myDate.getMonth();               //获取当前月份(0-11,0代表1月)
myDate.getDate();                //获取当前日(1-31)
myDate.getDay();                 //获取当前星期X(0-6,0代表星期天)
myDate.getTime();                //获取当前时间(从1970.1.1开始的毫秒数)
myDate.getHours();               //获取当前小时数(0-23)
myDate.getMinutes();             //获取当前分钟数(0-59)
myDate.getSeconds();             //获取当前秒数(0-59)
myDate.getMilliseconds();        //获取当前毫秒数(0-999)

// 获取当前日期时间
function getDatetime() {
    var now = new Date();
    var year = now.getFullYear();       
    var month = now.getMonth() + 1;     
    var day = now.getDate();            
    var hh = now.getHours();            
    var mm = now.getMinutes();          
    var ss = now.getSeconds();          
    var clock = year + "-";
    if (month < 10)
        clock += "0";
    clock += month + "-";
    if (day < 10)
        clock += "0";
    clock += day + " ";
    if (hh < 10)
        clock += "0";
    clock += hh + ":";
    if (mm < 10) clock += '0';
    clock += mm + ":";
    if (ss < 10) clock += '0';
    clock += ss;
    return clock;}

// 获取当前日期时间
function timestampToTime(timestamp) {
    var date = new Date(timestamp);
    var Y = date.getFullYear() + '-';
    var M = (date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1) + '-';
    var D = date.getDate() < 10 ? '0' + date.getDate() : date.getDate() + ' ';
    var hh = date.getHours() < 10 ? '0' + date.getHours() : date.getHours() + ':';
    var mm = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes() + ':';
    var ss = date.getSeconds() < 10 ? '0' + date.getDate() : date.getSeconds() ;
    return Y + M + D + hh + mm + ss;}
```



踩过这个坑，还有下一个坑等着你，这一路就是给自己填坑，坑填多了，也就习惯了，直到这一路平坦了，也就无怨无悔了。

转载 ： https://www.cnblogs.com/xiaofeilin/p/14468107.html

 

\-------------------------------------------------------------------------



```
  onConfirm(date) {
      const date1 = this.timestampToTime(date);
      console.log(date1);
      this.text = ` ${date1} `;
    },
    onSubmit(values) {
      console.log("submit", values);
    },
    onClickLeft() {
      this.$router.push({
        path: "/home/index",
      });
    },
    // 获取当前日期时间
    timestampToTime(timestamp) {
      var date = new Date(timestamp);
      var Y = date.getFullYear() + "-";
      var M =
        (date.getMonth() + 1 < 10
          ? "0" + (date.getMonth() + 1)
          : date.getMonth() + 1) + "-";
      var D = date.getDate() < 10 ? "0" + date.getDate() : date.getDate() + " ";
      var text = " ";
      var hh =
        date.getHours() < 10 ? "0" + date.getHours() : date.getHours() + ":";
      var mm =
        date.getMinutes() < 10
          ? "0" + date.getMinutes()
          : date.getMinutes() + ":";
      var ss =
        date.getSeconds() < 10 ? "0" + date.getDate() : date.getSeconds();
      return Y + M + D + text + hh + mm + ss;
    }
```

![image-20221114205956862](image-20221114205956862.png) 



```
onConfirm(date) {
      var now = new Date();
      var Today = now.getDate();

      const date2 = date.getDate(); //签到的时间
      if (Today != date2) {
        Toast.fail("请选择今天日期,签到！");
      } else {
        const date1 = this.timestampToTime(date);
        this.text = ` ${date1} `;
        Toast.success("签到成功");
      }
    },
```



# 案例训练

## 数据类型

```js
let a = {
    n: 1
};
let b = a;
a.x = a = {
    n: 2
};
console.log(a.x); // undefined
console.log(b) // {n: 1, x: {n: 2}}
```

操作符的优先级：[js运算符优先级 ](https://www.cnblogs.com/liyongquan/p/9359523.html)

![堆栈内存图01](2022年9月24日.png)

- 成员访问的优先级为18，赋值的优先级为3

```js
var a = 'abc' + 123 + 456;
var b = '456' - '123';
var c = 100 + true + 21.2 + null + undefined + "Tencent" + [] + null + 9 + false;
console.log(a, b, c)
```

## 判断逻辑

### 判断数字正负

```js
const myinput = document.querySelector('.myinput'),
    btn = document.querySelector('.calc'),
    res = document.querySelector('.value')


// const inputValue = Number(myinput.value)

const validateNumber = function validateNumber() {
        const inputValue = myinput.value
        if(inputValue === '') {
            res.innerHTML = '请输入'
            return
        }
    
        const numberValue = Number(inputValue)
        // if(String(numberValue) === 'NaN') {
        //     res.innerHTML = `输入为：${inputValue}，请输入有效数字`
    
        // } else if(numberValue === 0) {
        //     res.innerHTML = `输入为：${inputValue}`
        // } else {
        //     res.innerHTML = numberValue > 0 ? `结果为：${numberValue}，正数` : `结果为：${numberValue}，负数`
        // }
        if(!isNaN(numberValue)) {
            if(numberValue === 0) {
                    res.innerHTML = `输入为：${inputValue}`
            } else {
                res.innerHTML = numberValue > 0 ? `结果为：${numberValue}，正数` : `结果为：${numberValue}，负数`
            }
        } else {
            res.innerHTML = `输入为：${inputValue}，请输入有效数字`
        }
}
btn.addEventListener('click', validateNumber)

myinput.addEventListener('keydown', function(event) {
    if(event.keyCode === 13) {
        validateNumber()
    }
})

```





```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>判断数字输入正负</title>
    <link rel="stylesheet" href="./style.css">
</head>

<body>
    <h1>判断数字输入正负</h1>
    <div class="container">
        <input type="text" class="myinput">
        <button class="calc">点击计算</button>
        <div class="value">结果为：</div>
    </div>
    <script src="./index.js"></script>
</body>

</html>
```



```css
* {
    box-sizing: border-box;
}

body {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    height: 100vh;
    margin: 0;
    overflow: hidden;
}

.myinput {
    width: 200px;
    height: 38px;
    padding: 0 6px;
    border-radius: 6px;
    border: 1px solid rgb(99, 99, 99);
    outline: none;
    letter-spacing: 1px;
    font-size: 18px;

}

input.myinput:focus {
    outline: 1px solid rgb(71, 197, 255);
}

button.calc {
    width: 80px;
    height: 38px;
    border-radius: 10px;
    border: 1px solid grey;
    cursor: pointer;
}

div.value {
    width: 290px;
    height: 200px;
    margin-top: 10px;

}
```

### 奇偶判定

判断输入的数字是偶数还是奇数

偶数条件:能被2整除(或者除以2余数为0 => N%2是取余数)

### 成绩判定

根据输入的分数,判定成绩等级

说明: 90分及以上“优秀”80分及以 上"中等”70分及以 上”及格”70分以下”不及格”

### 年终奖发放判定

某个公司要给员工发年终奖,为了奖励老员工,所以工作时间越长,发的越多,规则如下:

工作满0年，发月薪的1倍月薪年终奖,如果月薪大于8000 ,那么就是发1.2倍
工作满1年，发月薪的1.5倍月薪年终奖,如果月薪大于10000 ,那么就是发1.7倍
工作满2年甚至更多，发月薪的3倍月薪年终奖,如果月薪大于12000,那么就是发3.2倍
编写JS程序,当用户输入自己的工作年限和薪资后,计算并且输出应得的年终奖~~

### 加油优惠

一个加油站为了鼓励车主多加油,所以加的多有优惠。

92号汽油，每升6元;如果大于等于20升,那么每升5.9元.
97号汽油，每升7元;如果大于等于30升,那么每升6.95元
编写JS程序,用户输入自己的汽油编号,然后输入自己加多少升,计算并且输出应付价格~~

### 奇偶行变色

同时，鼠标滑过的时候，实现变色

```js
let ulEle = document.querySelector('.container'),
    liEle = document.querySelectorAll('.item')

for(let i = 0; i < liEle.length; i++) {
    let liItem = liEle[i]
    liItem.style.backgroundColor = i % 2 === 0 ? '#ddd' : '#fff' // 初始化背景颜色
    // let currentBgc = liItem.style.backgroundColor // 记录初始背景颜色
    // 使用自定义属性，存储背景颜色
    // 自定义属性编程思想：前期把一些值存储到元素的自定义属性上，后期需要用到的时候，直接从属性上获取到这些值即可
    liItem.myOriginBg = liItem.style.backgroundColor

    liItem.onmouseover = function() { // 鼠标滑过改变背景颜色
        this.style.backgroundColor = 'lightblue'
    }

    liItem.onmouseout = function() { // 鼠标移出恢复背景颜色
        this.style.backgroundColor = this.myOriginBg
    }
}
```



```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>奇偶行变色</title>
    <link rel="stylesheet" href="./style.css">
</head>

<body>
    <h1>奇偶行变色</h1>
    <ul class="container">
        <li class="item">我是item001</li>
        <li class="item">我是item002</li>
        <li class="item">我是item003</li>
        <li class="item">我是item004</li>
        <li class="item">我是item005</li>
    </ul>
    <script src="./index.js"></script>
</body>

</html>
```



```css
* {
    box-sizing: border-box;
}

body {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    height: 100vh;
    margin: 0;
    overflow: hidden;
}

ul.container {
    width: 500px;
    height: 300px;
    border: 1px solid skyblue;
}

li.item {
    width: 100%;
    height: 50px;
    list-style: none;
    border-bottom: 1px dashed grey;
    line-height: 50px;
}

li.item:first-child {
    margin-top: 10px;
}

li.item:last-child {
    border-bottom: none;
}

/* 真实项目css实现更方便一点，为了练习使用js实现 */
/* li.item:nth-child(2n) {
    background-color: rgb(100, 100, 100);
}

li.item:hover {
    background-color: rgb(56, 63, 70);
} */
```



## 选项卡案例

拥有active选中样式类的显示

- 循环li时，使用var声明i时的解决方案：

  - 增加自定义属性

    ```js
    for(var i = 0; i <navList.length; i++) {
    	navList[i].myIndex = i
        navList.onclick = function() {
            changeTab(this.myIndex)
        }
    }
    ```

  - 使用闭包

    ```js
    for(var i = 0; i <navList.length; i++) {
        navList[i].onclick = (function(i) {
            return function() {
                changeTab(i)
            }
        })(i)
    }
    ```

- 当然了，可以使用let关键字，有自己的块级作用域

## 扩展题

1.浏览器常用的输出方式，除了 `console.log`还有哪些 ?

2.`< script >`标签放到页面头部和尾部的区别，以及解决办法?



---
title: js底层核心概念
date: 2022-10-14 05:58:44
cover: false
tags:
- javascript
categories: 'javascript'
typora-root-url: js底层核心概念
---

# JS核心概念

## 数据结构

### 栈

一种遵从先进后出（LIFO）原则的有序集合；

新添加的或待删除的都保存在栈的末尾，称作栈顶，另一端为栈底。

在栈里，新元素都靠近栈顶，旧元素都接近栈底。

栈知识对原有数据的一次封装而已。

而封装的结果是：并不关心其内部的元素是什么，只是去操作栈顶元素，这样的话，在编码中会更可控一些。

定义一个栈

```js
```

### 队列

与上相反，一种遵循先进先出（FIFO）原则的一组有序的项；

队列在尾部添加新元素，并从头部移除元素。

最新添加的元素必须排在队列的末尾。例如日常生活中的购物排队。

与栈类比，栈仅能操作其头部，队列则首尾均能操作，但仅能在头部出尾部进

定义一个队列

```js
```

### 链表

存储有序的元素集合，但不同于数组，链表中的元素在内存中并不是连续放置的；

每个元素有一个存储本身的节点和一个指向下一个元素的引用（指针/链接）组成

### 集合

由一组无序且唯一（即不能重复）的项组成；

这个数据结构使用了与有限集合相同的数学概念，但引用在计算机科学的数据结构中。

### 字典

以[键，值]对为数据形态的数据结构，其中键名用来查询特定元素，类似于JS中的Object

### 散列

根据关键码（Key Value）直接进行访问的数据结构；

它通过把关键码值映射到表中的一个位置来访问记录，以加快查找的速度；

这个映射函数叫做散列函数，存放记录的数组叫做散列表

### 树

表示一对多关系

由n（n>=1）个有限节点组成一个具有层次关系的集合；

把它叫做“树”是因为它看起来像一颗倒挂的树，基本呈一对多关系，树也可以看做是图的特殊形式

### 图

表示多对多关系

图是网络结构的抽象模型；

图是一组由边连接的节点（顶点）

任何二元关系都可以用图来表示，常见的比如：道路图、关系图、呈现多对多关系

## 堆栈内存

浏览器想要执行JS代码:

1.从电脑内存中分配出一块内存，用来执行代码(栈内存=>Stack)

- 执行代码、存储变量和基本类型值
- js中的赋值，是关联引用模式，而不是拷贝模式

2.分配一个主线程用来自上而下执行js代码

### 栈内存

栈（stack）中主要存放一些基本类型的变量和对象的引用，（包含池，池存放常量）；

其优势是存取速度比堆要快，并且栈内的数据可以共享；

但缺点是存在栈中的数据大小与生存期必须是确定的，缺乏灵活性；

先进后出，后进先出原则，所以push优于unshift

### 堆内存

堆（heap）用于复杂数据类型（引用类型）分配空间，例如数组对象、object对象;

它是运行时动态分配内存的，因此存取速度较慢

## 数据类型内存机制

js的数据类型主要分为两种：基本类型值和引用类型值

### 基本数据类型

基本类型值有6种：undefined、null、boolean、number、string、symbol。

这六种数据类型是按值访问的，是存放在栈内存中的简单数据段，数据大小确定，内存空间大小可以分配。

基本类型值的复制是值的传递，赋值以后二者再无关联，修改其中一个不会影响另一个。

### 引用数据类型

引用类型值：6中基本类型值以外的数据类型，都可以看作是引用类型值；

比如array，object等，是保存在堆内存中对象。

js不允许直接访问堆内存中的位置，也就是说不能直接操作对象的内存空间。

在操作对象时，实际是在操作对象的引用而不是实际的对象，是按地址访问的。

直接传递引用类型值的时候，传递的知识引用，二者指向同一块内存，所以修改其中一个，必然会引起另一个变量的变化。

在日常的使用中，我们把对象赋值给一个变量时，通常希望得到的是一个跟原对象无关的的副本，修改新的变量不影响原对象，因此就有了浅拷贝和深拷贝

### 内存角度分析变量声明及定义

`let a = 12;`

1. 创建变量a，放到当前栈内存变量存储区域中

2. 创建一个值12 ,把它存储到当前栈内存值区域中（简单的基本类型值是这样存储的,复杂的引用类型值不是这样做的）

   复杂值(引用类型值)的存储,又分成了三个步骤，`let obj = {name: 'sai'}`:	

   1. 在内存中分配出一块新内存,用来存储引用类型值(堆内存=>heap) =>内存有一个16进制地址
   2. 把对象中的键值对(属性名:属性值)依次存储到堆内存中
   3. 把堆内存地址和变量关联起来

3. =为赋值，其实赋值是让变量和值相互关联的过程

## 作用域与作用域链

对于几乎所有的编程语言来说，最基本的功能之一，就是储存变量当中的值并且能在之后对这个值进行访问和修改。这种能力的引入，是程序的状态存在的基础。

但是，能力的引入需要我们解决几个问题，例如：变量存储在哪里？以何种形式存储？需要读取和修改变量的时候，以什么方式获取到这个变量？

很明显，为了解决这些问题，我们需要一套设计良好的规则来存储变量，并且之后可以方便的找到这些变量。与此同时，整套完整规则的设计就会衍生出额外规则概念。而作用域，就是这套规则下衍生出来的概念。

### 作用域

链接：https://juejin.cn/post/7152863269353422855

我们可以把作用域理解为上面讲到的这套规则下的限定范围。作用域的职责是，在这段限定范围中根据这套设计好的规则存储所声明的变量，并且提供修改该变量的支持。在变量的访问权限安全上，作用域还承担着保护当前作用域内的变量不被外部作用域访问的权限保护作用。

通过类比，我们可以把作用域想象成一个气泡。在这个气泡里所声明的变量成员被包含在其中。每个气泡都配备有一位有原则的管家，将所有的成员管理起来，并针对他们声明的位置和要求对它们提供保护。当气泡中代码语句想要访问和修改变量成员时，管家会结合变量成员的要求关联对应访问和修改操作。

随着ECMAScript标准的不断发展和完善，JavaScript目前存在着四种作用域类型：

- 全局作用域（Global Scope）: JavaScript语言环境的最顶级作用域，在语言环境初始化时创建。
- 模块作用域（Module Scope）: 由ECMAScript模块标准（ES Module）引入，在解析ECMAScript模块时创建。
- 函数作用域（Function Scope）: 在函数声明`function() {}`或者`() => {}`时创建。
  - 可人为创建
- 块级作用域（Block Scope）: 由ECMAScript2015的变量声明标识符`let`和`const`引入，在使用这两者进行变量声明时，根据最近的一对花括号`{}`创建。
  - 可人为创建

```js
/* 全局作用域 start，JavaScript语言环境初始化时就被创建 */
/* 模块作用域 start，作为ES Module解析和执行时被创建 */
let name = 'Wu';

{
  /* 块级作用域 start，const进行变量声明在最近的花括号{}内创建 */
  const prefix = Hardy;
  name = prefix + name;
  /* 块级作用域 end */
}

export function sayMyName(myName) {
  /* 函数作用域 start，函数声明时自动创建，初始化默认包含函数的形参变量 */
  if (!myName) {
    /* 块级作用域 start */
    const noNameAnswer = 'Sorry!';
    console.log(noNameAnswer);
    return;
    /* 块级作用域 end */
  }
  const wordPrifix = 'Hi! My Name is ';
  const answer = wordPrifix + myName + '.';
  console.log(answer);
  /* 函数作用域 end */
}
/* 模块作用域 end */
/* 全局作用域 end */

```

### 作用域的嵌套

作用域在使用上具有嵌套特征。一个作用域能够在自身内部创建一个新作用域从而形成内部和外部作用域的嵌套关系。

全局作用域作为JavaScript的初始作用域，是所有其他作用域最外层的作用域。另外，每一个ES Module都具有模块自己的顶级作用域（top-level scope），模块中的顶级作用域变量和函数都包含在这个模块顶级作用域中，而模块作用域的外部作用域是全局作用域。而函数作用域和块级作用域则相对比较灵活，可以相互嵌套。

### 作用域的一些实现细节

在JavaScript中，每一个函数、代码块`{...}`以及`script`脚本被运行前，都会有一个相对应的称为**词法环境（Lexical Environment）** 的内部关联对象被创建。

词法环境由两部分组成：

- **环境记录（Environment Record）**：一个存储所有局部变量作为其属性（包括一些执行上下文信息，例如`this`的值）的对象。
- **外部词法环境引用（Outer）**：对外部词法环境的引用，以此关联外部词法环境。

代码执行的过程中，每一个局部变量和局部函数的声明，都会作为一个属性字段被添加到环境记录中，后续对变量和函数的读取则通过对应标识符在环境记录中进行查找。	

根据上面的概念，我们可以通过下面的对象结构理解词法环境：

```js
  lexicalEnvironment = {
    environmentRecord: {
      <identifier>: <value>,
      <identifier>: <value>,
    },
    outer: <Reference to the parent lexical environment>,
  }

```

再来通过下面的代码例子来理解词法环境：

```js
/*  当前模块运行时，模块的词法环境被创建，  
moduleLexicalEnvironment = {    
	environmentRecord: {      
		name: <uninitialized>,      
		sayName: <reference to function object>,    
	},    
	outer: <globalLexicalEnvironment>,  
	}
    */

let name = 'Hardy';
/*  变量声明和赋值，修改环境记录的字段属性值，  
moduleLexicalEnvironment = {    
	environmentRecord: {      
        name: 'Hardy',      
        sayName: <reference to function object>,    
	},    
	outer: <globalLexicalEnvironment>,  
    }
    */

function sayName(myName) {
  /*    执行函数时，函数的词法环境被创建，    
  functionLexicalEnvironment = {      
  	environmentRecord = {        
  		myName: 'Hardy',      
    },      
    outer: <moduleLexicalEnvironment>,    
    }  
    */
  /* 通过读取环境记录的对应标识符字段属性值获取myName的变量值 */
  console.log(myName);
}

sayName(); // Hardy

```

我们来分析下上面的代码例子。

根据声明提前的特性，变量`name`和函数`sayName`都会在模块的词法环境创建时被添加在环境记录中。但是，由于`let`的暂时性死区特性，变量`name`在自身声明和初始化赋值之前处于不可引用和未初始化状态。函数的声明则不同，除了声明提前外还会初始化函数的引用。这就是我们可以在函数执行声明语句前调用函数的原因。另外，函数的词法环境在被创建时，对应函数的参数会被初始化在环境记录中，并且会被赋值上调用函数时的所传值或者函数参数的默认值。

在`outer`引用方面，模块词法环境`moduleLexicalEnvironment`的`outer`引用指向JavaScript最外部的全局词法环境`globalLexicalEnvironment`，而函数词法环境`functionLexicalEnvironment`的`outer`引用指向外部的模块词法环境`moduleLexicalEnvironment`。

我们可以看出，词法环境是JavaScript对作用域概念的内部技术实现。它是JavaScript引擎创建一个执行上下文时，创建用来存储变量和函数声明的环境。代码执行过程中，通过它访问到存储在其内部的变量和函数。在代码执行完毕后，执行上下文会从堆栈中被销毁回收，而词法环境也会根据情况的被销毁（如果词法环境被其他外部的词法环境所引用，则不会被销毁回收，例如闭包）。

### 作用域链

作用域可以嵌套，嵌套在内部的作用域可以访问外部的作用域所声明的变量和函数。通过上面词法环境的介绍，我们大概清楚，作用域的这种嵌套关系是通过词法环境的外部词法环境引用`outer`来关联实现的。这种词法环境的外部引用的关联关系，构建了一条单向的词法环境的链条。这就是我们常说的作用域链。

本质上，作用域链是JavaScript引擎给所执行代码维护的一条词法环境链条。代码执行中对外部作用域的变量的引用，通过这一条链条进行变量的查找、读取、修改。

代码执行中对某个变量的访问大致如下：

- 当代码要访问一个变量时，首先会搜索当前内部词法环境。如果搜索成功，就返回对一个变量值或变量引用，结束搜索。如果搜索不到，则通过`outer`引用继续搜索外部词法环境，以此类推，直到全局词法环境。
- 如果在任何地方都找不到这个变量，那么在严格模式下就会报错。

根据上面的概念，我们来看看下面的例子：

```js
let phrase = 'Hello';

function sayHello(name) {
  /*    函数的作用域链,    functionLexicalEnvironment{ name: 'Hardy' } ==outer==>    moduleLexicalEnvironment{ phrase: 'Hello' } ==outer==>    globalLexicalEnvironment        变量name从当前functionLexicalEnvironment中查找到并获取，    变量phrase沿作用域链查找，从moduleLexicalEnvironment中查找到并获取  */
  console.log(`${phrase}, ${name}!`);
}

sayHello('Hardy'); // Hello, Hardy!

```

上面例子中，函数`sayHello`在内部引用了`name`和`phrase`两个变量，函数被调用的执行时会创建`functionLexicalEnvironment > moduleLexicalEnvironment > globalLexicalEnvironment`的作用域链。

其中，变量`name`作为函数参数属于当前函数作用域的局部变量，变量可以直接从当前函数的词法环境`functionLexicalEnvironment`中查找到并返回相关信息。而变量`phrase`属于外部作用域中声明的变量，存储在外部的模块词法环境`moduleLexicalEnvironment`中。函数`sayHello`引用变量`phrase`，会首先从在自身函数词法环境`functionLexicalEnvironment`中进行查找，查找不到后，会沿外部词法环境引用`outer`找到模块词法环境`moduleLexicalEnvironment`，并从中继续进行变量的查找，查找到了并返回变量的相关信息。

值得注意的是`console.log()`是全局内置对象`console`上的方法，对该方法的调用需要引用`console`。这个变量的引用会沿作用域链一直查找到全局词法环境`globalLexicalEnvironment`中，从中查找到并返回相关变量信息。

变量标识符解析和引用的过程就是沿作用域链迭代查找变量是否在作用域链节点中并返回变量相关信息的过程。



### 相关优化

综合上面的标识符的解析过程和作用域以及作用域链的关系，我们可以了解到，变量标识符解析的性能是和变量标识符所处在作用域链中的位置是息息相关的。变量标识符所出的作用域节点越靠近整个作用域链的前端，则需要沿作用域链迭代查找的次数就越少，变量标识符解析的速度就会越快，性能就越好。

这种标识符解析性能的规律，让我们可以得出以下使用变量的优化点：

- 对于频繁引用的外部作用域的变量，可以根据情况在当前作用域内声明赋值为局部变量后使用。
- 减少作用域增强`with`语句的使用。

外部作用域变量标识符的多次引用，会造成执行过程中的标识符解析沿作用域链查找的频繁执行，这种查找在第一次解析引用时是必须的，但是后续解析引用却是重复的。将外部作用域变量通过在当前作用域内声明赋值为局部变量，可以优化后续查找的需要经过的作用域链节点个数，得到一定的性能提升。

`with`语句可以在当前作用域链前端临时添加一个词法环境，从而在位置构建和使用新的作用域链。但是这方式问题也很显而易见：作用域链被加长了，除了被添加到前端的词法环境中的存储的变量外，其他变量的标识符解析性能都会变差。因此，我们应该减少`with`语句的使用。

### 总结

随着JavaScript语言的发展，语言中的作用域的种类也变得丰富起来，不再局限于函数作用域作为最小变量声明范围来使用，而是可以基于更小范围的跨级作用域来管理我们的变量引用范围。变量的管理变得更加的灵活、安全。

作用域链是作用域链嵌套的结构产物，所有变量标识符的解析和引用会沿着作用域链进行查找。而词法环境，是JavaScript对于作用域的内部技术实现。深入了解词法环境后，也让我们更清楚代码在解析变量标识符时的内部执行过程。也根据这个过程，我们大概总结出了两点关于作用域和变量使用的性能优化点。

作用域的使用作为每一位JavaScript开发人员的必修课，了解得深入才能在使用它的时候不再迷茫。它就像空气，存在于JavaScript的许多地方，值得我们去好好了解。

## 变量生命周期

定义一个变量到这个变量被回收发生了什么
变量和内存之间的关系，是由三个部分组成：变量名、内存绑定和内存地址

## 上下文

执行上下文

- 代码执行时，创建上下文
- 所有代码执行完成后，销毁上下文	
- 每一个上下文，都有一个相关联的变量对象（VO：Variable Object）
- 当前上下文中，定义的变量和对象都存储在VO上

全局上下文

- GO(Global Object)，浏览器环境下，就是window对象，GO是特殊的VO

- var关键字声明变量，存储在GO上（给GO对象添加属性），即

  ```js
  var a;
  console.log(window.a) // undefined
  ```

- function关键字声明函数，存储在GO上

  ```js
  var a;
  console.log(window.a)
  function aFunc() {
      console.log(a)
  }
  aFunc()	
  ```

- js代码执行之前，浏览器首先会默认把所有带var和function关键字的变量，进行提前声明或定义(存储在GO上)

- 关联this到GO(window)

- JS线程全局上下文维护着当前一次执行过程（宏任务）中，产生的微任务队列，在宏任务执行完后，会执行所有的微任务，之后GUI渲染线程才会进行渲染

函数上下文

- 见函数底层执行机制 > 函数的执行

## 变量提升，函数提升、浏览器解析变量的机制



## JS预解析

1.当浏览器加载html页面的时候，浏览器tab页的renderer进程下，开启JS线程，JS线程会先提供一个全局JS代码执行的环境

 - JS线程开启栈空间，栈空间中开辟全局执行上下文（全局上下文开始执行一次宏任务，并维护着微任务队列）

2.预解析（变量提升，浏览器的加载机制）

在当前的作用域（上下文）中，js代码执行之前，JS线程首先会默认把所有带var和function关键字的变量，进行提前声明或定义
- 对于变量只是进行了变量的提前声明
	```js
	var num = 1;
	// 理解声明和定义
	// 声明（declare）： var num ==> 告诉浏览器，在全局作用域中有一个num的变量了（在GO上，新增属性num，默认属性值为undefined），声明：对于变量，就是把变量添加到当前上下文的变量对象上
	// 定义（defined）：num = 1; ==>给变量赋值（进行值关联），定义：定于变量，就是把当前上下文的变量对象对应的属性，关联值或者内存地址
	
	// console.log(number) // Uncaught ReferenceError: number is not defined
	console.log(num) // undefined，这里打断点，会看到全局window对象上，已经有num属性了，值为undefined
	var num = 1;
	console.log(num) // 1
	```
	
	
	
- 对于函数是提前声明并且定义（将函数代码以字段串的形式存储起来）

  ```js
  console.log(fn) // 打印出函数体，由于函数提升机制，此时GO（window)对象上，已经有fn属性了，值为代码块字符串
  function fn() {
      console.log('fn')
  }
  console.log(fn) // 打印出函数体（实际打印的就是window.fn，值为代码块字符串）
  ```

- 变量和函数重名时

  - 提升阶段：变量只是提前声明了，函数是声明并且定义了
  - 执行阶段：变量开始定义赋值，函数不进行赋值

  ```js
  console.log(afn) // afn(){console.log(4)}
  function afn() {
  	console.log(2)
  }
  console.log(afn) // afn(){console.log(4)}  
  
  var afn;
  console.log(afn) // afn(){console.log(4)}
  
  var afn = 3 
  console.log(afn) // 3
  
  function afn() {
  	console.log(4)
  }
  
  console.log(afn) // 3
  ```

- 函数表达式的调用，必须写到函数表达式的下面

  ```js
  fun() // 声明定义函数之前调用， Uncaught TypeError: fun is not a function
  
  var fun = function() {
  	console.log(22)
  }
  ```

  相当于

  ```js
  var fun;
  fun(); // Uncaught TypeError: fun is not a function
  fun = function() {
  	console.log(22)
  }
  ```

- 预解析（变量提升和函数提升）只会发生在当前上下文中。

  例如：开始只会对全局上下文中的变量和函数进行预解析，因为一开始就创建了全局上下文；只有函数执行的时候，才会创建函数上下文，才会对函数上下文中的变量和函数进行预解析

  ```js
  var a = 10;
  function afn() {
      console.log(a) // undefined
      var a = 11
      console.log(a) // 11
  }
  afn()
  console.log(a) // 10
  ```

  相当于

  ```js
  var a = 10 // GO全局对象window上的属性
  function fn() {
  	var a; // 私有上下文对象AO上的属性，属性值为undefined
  	console.log(a) // undefined
  	var a = 11
  	console.log(a) // 11
  } // 出栈后，私有上下文销毁
  fn() // 进栈
  console.log(a) // 10
  ```

## 函数底层执行机制

>  1.函数的创建

每一个上下文都有一个相关联的`VO`，当前上下文中，声明的变量和对象存储在`VO`上

创建对象时，会在堆内存中开辟一块空间来存储对象的值

函数对象被创建时，存储的键值对有
- `this`
- `prototype`

函数对象除了在堆内存中存储键值对，还会存储两部分东西
- 创建函数时的声明作用域`[[Scopes]]`：
  - 函数在哪个上下文中创建，其`[[Scopes]]`就关联谁
  
	- 函数定义中使用到了哪个变量或对象，[[Scopes]]就会把该变量或者对象所有的`VO`添加到`[[Scopes]]`中，这个机制也是let关键字形成块级作用域的根本原因
	
	- `[[Scopes]]`中存储的应该是，实际用到的变量所在的上下文对应的变量对象
	
	  ```js
	  function aFunc() {
	      var a = 1
	      console.log(a)
	      console.log(this)
	  }
	  aFunc()
	  console.dir(aFunc) // [[Scopes]]有一个值，指向当前上下文的GO，即window对象
	  
	  
	  function bFunc() {
	      var b = 1, c =2;
	      function bInnnerFunc() {
	          // return // [[Scopes]]只有一个值，指向window对象
	          return b // [[Scopes]][0]为bFunc私有上下文的AO对象，{b: 1}，[[Scopes]][1]指向window对象
	          // return b + c // [[Scopes]][0]为bFunc私有上下文的AO对象，{b: 1, c: 2}，[[Scopes]][1]指向window对象
	      }
	      console.dir(bInnnerFunc) // [[Scopes]]有两个值，[[Scopes]][0]指向bFunc执行上下文的VO对象（更准确点，是bFunc私有上下文的AO对象，见下一部分），这是一个闭包;[[Scopes]][1]指向window
	  }
	  
	  bFunc()
	  ```
	
	  

- 函数字符串：把函数体中的代码，以字符串的形式存储起来

     - 如果是循环4个标签，for循环是以var声明的i，按照直观上，每次click的回调函数打印的值应该不一样。事实上都是4，代码首先会循环4次，然后每次都讲i加1，for方法体的函数，仅执行了创建的过程，onclick关联的函数，此时是以字符串的形式保存在堆内存中（保存了4份），并且循环结束时，i的值已经变成了4。当我们点击元素时，onclick关联的回调函数，进栈开始执行，沿着[[Scopes]]作用域链找到GO（window）上的i值为4。

       ```js
       var myBtn = document.querySelectorAll('.myBtn')
       for(var i = 0; i < myBtn.length; i++) {
           myBtn[i].onclick = function() {
               console.log(i)
           }
       }
       console.log(i)
       
       // 将回调函数定义成具名函数，方便查看作用域链（设置断点查看）
       var myBtn = document.querySelectorAll('.myBtn')
       for(var a = 0; a < myBtn.length; a++) { //定义成a，查看是在window属性的第一个
           let innerFunc = function innerFunc() {
               console.log(a, window.a, a === window.a)
               console.dir(innerFunc)
           }
           myBtn[a].onclick = innerFunc // 不能加括号，否则就直接执行了
       }
       ```

> 函数的执行


		2.1.创建私有上下文
			- 进栈：函数一旦执行，就会创建一个全新的私有上下文（函数上下文）
				- 函数的每次执行，都是重新形成一个私有的上下文，和之前产生的上下文没有必然的联系
				- 函数的代码都是在私有上下文中执行的
			- 函数进栈执行时，会创建一个全新私有变量对象（AO: Active Object）
				- 这里区分开VO，AO是VO的一个分支
				- 在私有上下文中创建的变量和对象，都会存储在AO中，例如形参、变量提升和函数中定义的变量
				- 私有变量对象不能被外部访问，但可以通过return语句返回
		2.2.完成初始化操作
		函数进栈后，正式开始执行前，会进行5步的初始化操作
			- 初始化作用域链([[Scopes]])
				- 根据函数代码中实际使用到的变量，关联变量所在上下文的变量对象，作为作用域链中的每一个值
			- 初始化this
				- this的基本概念
					在js中，this是一个关键字，它会被自动定义在js所有函数的作用域中，《JS高程》在函数一章中指出：定义一个函数会获得this和prototype两个属性，而this很特殊在于this可以用作声明指向某个对象？？
				this在运行时绑定的，并不是在编写时绑定的，她的上下文取决于函数调用时的各种条件。this的绑定和函数声明的位置没有任何关系，只取决于函数的调用方式
				- this到底是什么 
					当一个函数被调用时，会创建一个活动记录（私有上下文）。这个记录会包含函数在哪里被调用（调用栈）、函数的调用方式、传入的参数等信息。this就是这个记录的一个属性，会在函数执行的过程中用到
				- 函数绑定方式
					this的绑定规则和函数的调用方式有着重大联系
					- 普通函数调用
					```js
					function foo () {
						console.log(this.a)
					}
	
					var a = 2
					foo() // 2，相当于window.foo()
					```
					- new方式调用
					```js
					
					```
				- 箭头函数没有这一步
				js采用的是词法作用域（静态作用域），也就是说函数的作用域（可以访问到的变量），在函数定义的时候就确定了
				与之相反的是动态作用域，即函数的作用域在函数调用时才确定
				下面的例子，很好的说明JS是一个静态作用域的语言，如果函数的作用域是在运行时确定的，运行aFoo函数是，从aFoo函数内部没有找到局部变量value后，会从调用函数的作用域，也就是aBar函数内部查找value变量，那么应该会打印2
				JS引擎底层的实现为：函数在定义时，会把其所属环境（全局环境）的变量生成一个变量对象，放入函数的scope属性中。调用函数时，会生成执行环境（上下文）并创建一个作用域链，即先把函数scope属性中的变量对象放到作用域链中，再利用函数参数和内部变量，生成一个活动对象，并放入作用域链的前端。
				```js
				var aValue = 1
				function aFoo() {
					console.log(aValue)
				}
				function aBar() {
					var aValue = 2
					aFoo()
				}
	
				aBar() // 1
				```
				this关键字是JS中的动态作用域机制，是为了在JS中加入动态作用域而做的努力，因为this指向的对象实在函数调用时绑定的。
				在任何函数中，this的指向都不是静态的。它总是在你调用一个函数，但尚未执行函数内部代码前被指定。即this的指向与函数被调用的方式（语法）有关
				
				```js
				var o = {
					a: 10,
					b: {
						fn: function() {
							console.log(this)
						}
					}
				}
	
				o.b.fn() // this指向对象b，{fn: f}
	
				var j = o.b.fn
				j() // this指向window
				```
				可以看到，函数内部的this指向，和其调用方式有关，和函数本身的定义方式无关
				绑定规则
				- 1.构造绑定：通过new关键字调用构造函数。此时会生成一个实例对象，并且this指向这个实例对象。这种方式实际上是new的底层实现修改了this指向
				```js
				var savedThis;
				function Constr() {
					savedThis = this;
				}
	
				var inst = new Constr()
	
				console.log(savedThis === inst) // true
				```
				2.显示绑定：apply()、call()、bind()三个方法改变函数的调用对象（this对象）
				3.隐式绑定：某个上下文对象中调用函数。比如使用obj.foo()这样的语法来调用函数，函数foo中的this绑定到obj对象
				```js
				var o = {
					a: 10,
					b: {
						fn: function() {
							console.log(this.a) // undefined，this指向b对象
						}
					}
				}
	
				o.b.fn()
	
				// 事件处理函数
				function doPrint() {
					console.log(this)
				}
				doPrint() // 全局对象 window
				var myBtn = document.querySelector('.myBtn')
				myBtn.onclick = doPrint
				myBtn.onclick() // 元素对象button
				```
				4.默认绑定：不符合上述三种情况，在一个函数中使用了this，但是没有为this绑定对象。这种情况下，严格模式this绑定到undefined，非严格模式下this绑定到全局对象（GO）（Node环境中的global，浏览器环境的window）
				```js
				var o = {
					a: 10,
					b: {
						fn: function() {
							console.log(this.a) // undefined
							console.log(this) // window
						}
					}
				}
	
				var j = o.b.fn
				j() // window
				```
				对于3、4两点，可以用一个简单的规则去判断：当一个函数被调用时，应该立马看()左边的部分
					- 如果()左边是一个引用，那么函数的this指向这个引用所属的对象（隐式绑定）
					- 否则this指向的就是全局对象或者undefined（默认绑定）
					- 上面的代码中，fn是一个引用，属于b这个对象，所以this指向b；j不是引用，所以this指向window
			- 初始化arguments？？
				- 箭头函数没有这一步
			- 形参赋值
			- 变量提升：var关键字声明的变量会提前声明，function关键字声明的函数会提前
	3.代码执行
		将堆内存中存储的代码字符串，从上往下顺序执行
		- 变量按作用域链查找
	4.出栈释放或保留
		- 正常情况下，代码执行完成后，私有上下文出栈被回收
		- 特殊情况
			- 如果当前私有上下文执行完成之后的某个东西（变量或对象），被执行上下文以外的东西占用，则当前私有上下文就不会出栈释放，也就是形成了不被销毁的上下文（闭包）
		- 还有一种情况：上下文没被占用，但是要紧接着被用一次，这样没有用完之前是不能释放的，用完再释放。这样就形成了一个临时不被释放的上下文
		- 函数每次执行都是重新形成给全新的私有上下文，正常情况下，函数执行完就会出栈私有上下文被释放，但是如果不能被释放（闭包），就会一直被保存在内存中，当到达栈内存的极限时就会出现栈内存溢出

理清上述概念的先后顺序




## let、const和块级作用域

块级作用域
	- JS中没有块级作用域

let定义变量

 - let关键字定义的变量，在代码执行时，会在栈内存再形成一个块级上下文，这个块级上下文也有一个与之关联的VO对象，当代码执行到函数定义时，由于用到了变量a，就会把变量对象{a: 0}，添加到innerFunc的[[Scopes]]

   ```js
   var amyBtn = document.querySelectorAll('.myBtn')
   for(let a = 0; a < amyBtn.length; a++) {
   	let innerFunc = function innerFunc() {
   		console.dir(innerFunc)
   		console.log(a)
   	}
   	amyBtn[a].onclick = innerFunc // 不能加括号，否则就直接执行了
   }
   ```

   - let关键字声明的变量，在谷歌浏览器断点调试的作用域中，被称为“代码块”
     const定义常量
     const关键字声明的变量，在谷歌浏览器断点调试的作用域中，被称为“脚本”
     const关键字声明的变量，绑定了第一次定义的值的内存地址与该变量的关联关系，当尝试绑定其他内存地址时无法生效
     对于由若干内存片段组成的非连续内存数据（对象、数组），只有第一处是有变量与内存的强绑定关系，对象内部属性值仍然可以修改
     Object.freeze()

箭头函数

## 堆栈内存及函数底层处理机制

链接：https://www.jianshu.com/p/edb2be5866eb





# JS运行机制

链接：https://juejin.cn/post/6844904050543034376

本文大致分为以下这样的步骤来帮助我们由广入深更加清晰的了解JS运行机制

- 首先我们要了解进程和线程的概念
- 其次我们要知道浏览器的进程线程常识
- 再然后通过Event Loop、宏任务(macrotask)微任务(microtask)来看浏览器的几个线程间是怎样配合的
- 再然后通过例子来印证我们的猜想
- 最后提下NodeJS的运行机制

## 进程与线程

### 什么是进程

我们都知道，`CPU`是计算机的核心，承担所有的计算任务

官网说法，`进程`是`CPU`资源分配的最小单位

字面意思就是进行中的程序，我将它理解为一个可以独立运行且拥有自己的资源空间的任务程序

`进程`包括运行中的程序和程序所使用到的内存和系统资源

`CPU`可以有很多进程，我们的电脑每打开一个软件就会产生一个或多个`进程`，为什么电脑运行的软件多就会卡，是因为`CPU`给每个`进程`分配资源空间，但是一个`CPU`一共就那么多资源，分出去越多，越卡，每个`进程`之间是相互独立的，`CPU`在运行一个`进程`时，其他的进程处于非运行状态，`CPU`使用 [时间片轮转调度算法](https://link.juejin.cn?target=) 来实现同时运行多个`进程`

### 什么是线程

`线程`是`CPU`调度的最小单位

`线程`是建立在`进程`的基础上的一次程序运行单位，通俗点解释`线程`就是程序中的一个执行流，一个`进程`可以有多个`线程`

一个`进程`中只有一个执行流称作`单线程`，即程序执行时，所走的程序路径按照连续顺序排下来，前面的必须处理好，后面的才会执行

一个`进程`中有多个执行流称作`多线程`，即在一个程序中可以同时运行多个不同的`线程`来执行不同的任务， 也就是说允许单个程序创建多个并行执行的`线程`来完成各自的任务

### 进程和线程的区别

进程是操作系统分配资源的最小单位，线程是程序执行的最小单位

一个进程由一个或多个线程组成，线程可以理解为是一个进程中代码的不同执行路线

进程之间相互独立，但同一进程下的各个线程间共享程序的内存空间(包括代码段、数据集、堆等)及一些进程级的资源(如打开文件和信号)

调度和切换：线程上下文切换比进程上下文切换要快得多

### 多进程和多线程

多进程：多进程指的是在同一个时间里，同一个计算机系统中如果允许两个或两个以上的进程处于运行状态。多进程带来的好处是明显的，比如大家可以在网易云听歌的同时打开编辑器敲代码，编辑器和网易云的进程之间不会相互干扰

多线程：多线程是指程序中包含多个执行流，即在一个程序中可以同时运行多个不同的线程来执行不同的任务，也就是说允许单个程序创建多个并行执行的线程来完成各自的任务

## JS为什么是单线程

JS的单线程，与它的用途有关。作为浏览器脚本语言，JavaScript的主要用途是与用户互动，以及操作DOM。这决定了它只能是单线程，否则会带来很复杂的同步问题。比如，假定JavaScript同时有两个线程，一个线程在某个DOM节点上添加内容，另一个线程删除了这个节点，这时浏览器应该以哪个线程为准？

还有人说js还有Worker线程，对的，为了利用多核CPU的计算能力，HTML5提出Web Worker标准，允许JavaScript脚本创建多个线程，但是子线程是完 全受主线程控制的，而且不得操作DOM

所以，这个标准并没有改变JavaScript是单线程的本质

了解了进程和线程之后，接下来看看浏览器解析，浏览器之间也是有些许差距的，不过大致是差不多的，下文我们皆用市场占有比例最大的Chrome为例

## 浏览器

### 浏览器是多进程的

作为前端，免不了和浏览器打交道，浏览器是多进程的，拿Chrome来说，我们每打开一个Tab页就会产生一个进程，我们使用Chrome打开很多标签页不关，电脑会越来越卡，不说其他，首先就很耗CPU

### 浏览器包含哪些进程

- Browser进程
  - 浏览器的主进程(负责协调、主控)，该进程只有一个
  - 负责浏览器界面显示，与用户交互。如前进，后退等
  - 负责各个页面的管理，创建和销毁其他进程
  - 将渲染(Renderer)进程得到的内存中的Bitmap(位图)，绘制到用户界面上
  - 网络资源的管理，下载等
- 第三方插件进程
  - 每种类型的插件对应一个进程，当使用该插件时才创建
- GPU进程
  - 该进程也只有一个，用于3D绘制等等
- 渲染进程(重)
  - 即通常所说的浏览器内核(Renderer进程，内部是多线程)
  - 每个Tab页面都有一个渲染进程，互不影响
  - 主要作用为页面渲染，脚本执行，事件处理等

### 为什么浏览器要多进程

我们假设浏览器是单进程，那么某个Tab页崩溃了，就影响了整个浏览器，体验有多差

同理如果插件崩溃了也会影响整个浏览器

当然多进程还有其它的诸多优势，不过多阐述

浏览器进程有很多，每个进程又有很多线程，都会占用内存

这也意味着内存等资源消耗会很大，有点拿空间换时间的意思

到此可不只是为了让我们理解为何Chrome运行时间长了电脑会卡，哈哈，第一个重点来了

### 简述渲染进程Renderer(重)

页面的渲染，JS的执行，事件的循环，都在渲染进程内执行，所以我们要重点了解渲染进程

渲染进程是多线程的，我们来看渲染进程的一些常用较为主要的线程

### 渲染进程Renderer的主要线程

#### GUI渲染线程

- 负责渲染浏览器界面，解析HTML，CSS，构建DOM树和RenderObject树，布局和绘制等
  - 解析html代码(HTML代码本质是字符串)转化为浏览器认识的节点，生成DOM树，也就是DOM Tree
  - 解析css，生成CSSOM(CSS规则树)
  - 把DOM Tree 和CSSOM结合，生成Rendering Tree(渲染树)
- 当我们修改了一些元素的颜色或者背景色，页面就会重绘(Repaint)
- 当我们修改元素的尺寸，页面就会回流(Reflow)
- 当页面需要Repaing和Reflow时GUI线程执行，绘制页面
- 回流(Reflow)比重绘(Repaint)的成本要高，我们要尽量避免Reflow和Repaint
- GUI渲染线程与JS引擎线程是互斥的
  - 当JS引擎执行时GUI线程会被挂起(相当于被冻结了)
  - GUI更新会被保存在一个队列中等到JS引擎空闲时立即被执行

#### JS引擎线程

- JS引擎线程就是JS内核，负责处理Javascript脚本程序(例如V8引擎)
- JS引擎线程负责解析Javascript脚本，运行代码
- JS引擎一直等待着任务队列中任务的到来，然后加以处理
  - 浏览器同时只能有一个JS引擎线程在运行JS程序，所以js是单线程运行的
  - 一个Tab页(renderer进程)中无论什么时候都只有一个JS线程在运行JS程序
- GUI渲染线程与JS引擎线程是互斥的，js引擎线程会阻塞GUI渲染线程
  - 就是我们常遇到的JS执行时间过长，造成页面的渲染不连贯，导致页面渲染加载阻塞(就是加载慢)
  - 例如浏览器渲染的时候遇到`<script>`标签，就会停止GUI的渲染，然后js引擎线程开始工作，执行里面的js代码，等js执行完毕，js引擎线程停止工作，GUI继续渲染下面的内容。所以如果js执行时间太长就会造成页面卡顿的情况

#### 事件触发线程

- 属于浏览器而不是JS引擎，用来控制事件循环，并且管理着一个事件队列(task queue)
- 当js执行碰到事件绑定和一些异步操作(如setTimeOut，也可来自浏览器内核的其他线程，如鼠标点击、AJAX异步请求等)，会走事件触发线程将对应的事件添加到对应的线程中(比如定时器操作，便把定时器事件添加到定时器线程)，等异步事件有了结果，便把他们的回调操作添加到事件队列，等待js引擎线程空闲时来处理。
- 当对应的事件符合触发条件被触发时，该线程会把事件添加到待处理队列的队尾，等待JS引擎的处理
- 因为JS是单线程，所以这些待处理队列中的事件都得排队等待JS引擎处理

#### 定时触发器线程

- `setInterval`与`setTimeout`所在线程
- 浏览器定时计数器并不是由JavaScript引擎计数的(因为JavaScript引擎是单线程的，如果处于阻塞线程状态就会影响记计时的准确)
- 通过单独线程来计时并触发定时(计时完毕后，添加到事件触发线程的事件队列中，等待JS引擎空闲后执行)，这个线程就是定时触发器线程，也叫定时器线程
- W3C在HTML标准中规定，规定要求`setTimeout`中低于4ms的时间间隔算为4ms

#### 异步http请求线程

- 在XMLHttpRequest在连接后是通过浏览器新开一个线程请求
- 将检测到状态变更时，如果设置有回调函数，异步线程就产生状态变更事件，将这个回调再放入事件队列中再由JavaScript引擎执行
- 简单说就是当执行到一个http异步请求时，就把异步请求事件添加到异步请求线程，等收到响应(准确来说应该是http状态变化)，再把回调函数添加到事件队列，等待js引擎线程来执行

了解了上面这些基础后，接下来我们开始进入今天的正题

## 事件循环(Event Loop)初探

首先要知道，JS分为同步任务和异步任务

同步任务都在主线程(这里的主线程就是JS引擎线程)上执行，会形成一个`执行栈`

主线程之外，事件触发线程管理着一个`任务队列`，只要异步任务有了运行结果，就在`任务队列`之中放一个事件回调

一旦`执行栈`中的所有同步任务执行完毕(也就是JS引擎线程空闲了)，系统就会读取`任务队列`，将可运行的异步任务(任务队列中的事件回调，只要任务队列中有事件回调，就说明可以执行)添加到执行栈中，开始执行

我们来看一段简单的代码

```javascript
let setTimeoutCallBack = function() {
  console.log('我是定时器回调');
};
let httpCallback = function() {
  console.log('我是http请求回调');
}

// 同步任务
console.log('我是同步任务1');

// 异步定时任务
setTimeout(setTimeoutCallBack,1000);

// 异步http请求任务
ajax.get('/info',httpCallback);

// 同步任务
console.log('我是同步任务2');
复制代码
```

上述代码执行过程

JS是按照顺序从上往下依次执行的，可以先理解为这段代码时的执行环境就是主线程，也就是也就是当前执行栈

首先，执行`console.log('我是同步任务1')`

接着，执行到`setTimeout`时，会移交给`定时器线程`，通知`定时器线程` 1s 后将 `setTimeoutCallBack` 这个回调交给`事件触发线程`处理，在 1s 后`事件触发线程`会收到 `setTimeoutCallBack` 这个回调并把它加入到`事件触发线程`所管理的事件队列中等待执行

接着，执行http请求，会移交给`异步http请求线程`发送网络请求，请求成功后将 `httpCallback` 这个回调交由事件触发线程处理，`事件触发线程`收到 `httpCallback` 这个回调后把它加入到`事件触发线程`所管理的事件队列中等待执行

再接着执行`console.log('我是同步任务2')`

至此主线程执行栈中执行完毕，`JS引擎线程`已经空闲，开始向`事件触发线程`发起询问，询问`事件触发线程`的事件队列中是否有需要执行的回调函数，如果有将事件队列中的回调事件加入执行栈中，开始执行回调，如果事件队列中没有回调，`JS引擎线程`会一直发起询问，直到有为止

到了这里我们发现，浏览器上的所有线程的工作都很单一且独立，非常符合单一原则

定时触发线程只管理定时器且只关注定时不关心结果，定时结束就把回调扔给事件触发线程

异步http请求线程只管理http请求同样不关心结果，请求结束把回调扔给事件触发线程

事件触发线程只关心异步回调入事件队列

而我们JS引擎线程只会执行执行栈中的事件，执行栈中的代码执行完毕，就会读取事件队列中的事件并添加到执行栈中继续执行，这样反反复复就是我们所谓的**事件循环(Event Loop)**

![img](16fb7acab03b35fatplv-t2oaga2asx-zoom-in-crop-mark4536000.awebp)

首先，执行栈开始顺序执行

判断是否为同步，异步则进入异步线程，最终事件回调给事件触发线程的任务队列等待执行，同步继续执行

执行栈空，询问任务队列中是否有事件回调

任务队列中有事件回调则把回调加入执行栈末尾继续从第一步开始执行

任务队列中没有事件回调则不停发起询问

## 宏任务(macrotask) & 微任务(microtask)

### 宏任务(macrotask)

在ECMAScript中，`macrotask`也被称为`task`

我们可以将每次执行栈执行的代码当做是一个宏任务(包括每次从事件队列中获取一个事件回调并放到执行栈中执行)， 每一个宏任务会从头到尾执行完毕，不会执行其他

由于`JS引擎线程`和`GUI渲染线程`是互斥的关系，浏览器为了能够使`宏任务`和`DOM任务`有序的进行，会在一个`宏任务`执行结果后，在下一个`宏任务`执行前，`GUI渲染线程`开始工作，对页面进行渲染

```
宏任务 -> GUI渲染 -> 宏任务 -> ...
```

常见的宏任务

- 主代码块
- setTimeout
- setInterval
- setImmediate ()-Node
- requestAnimationFrame ()-浏览器

### 微任务(microtask)

ES6新引入了Promise标准，同时浏览器实现上多了一个`microtask`微任务概念，在ECMAScript中，`microtask`也被称为`jobs`

我们已经知道`宏任务`结束后，会执行渲染，然后执行下一个`宏任务`， 而微任务可以理解成在当前`宏任务`执行后立即执行的任务

当一个`宏任务`执行完，会在渲染前，将执行期间所产生的所有`微任务`都执行完

```
宏任务 -> 微任务 -> GUI渲染 -> 宏任务 -> ...
```

常见微任务

- process.nextTick ()-Node
- Promise.then()
- catch
- finally
- Object.observe
- MutationObserver

### 简单区分宏任务与微任务

看了上述宏任务微任务的解释你可能还不太清楚，没关系，往下看，先记住那些常见的宏微任务即可

我们通过几个例子来看，这几个例子思路来自掘金`云中君`的文章参考链接【14】，通过渲染背景颜色来区分宏任务和微任务，很直观，我觉得很有意思，所以这里也用这种例子

找一个空白的页面，在console中输入以下代码

```js
document.body.style = 'background:black';
document.body.style = 'background:red';
document.body.style = 'background:blue';
document.body.style = 'background:pink';
```

![img](16fb7c7576f1e3b1tplv-t2oaga2asx-zoom-in-crop-mark4536000.awebp)

我们看到上面动图背景直接渲染了粉红色，根据上文里讲浏览器会先执行完一个宏任务，再执行当前执行栈的所有微任务，然后移交GUI渲染，上面四行代码均属于同一次宏任务，全部执行完才会执行渲染，渲染时`GUI线程`会将所有UI改动优化合并，所以视觉上，只会看到页面变成粉红色

再接着看

```js
document.body.style = 'background:blue';
setTimeout(()=>{
    document.body.style = 'background:black'
},200)
```

![img](16fb7c81efff6db0tplv-t2oaga2asx-zoom-in-crop-mark4536000.awebp)

上述代码中，页面会先卡一下蓝色，再变成黑色背景，页面上写的是200毫秒，大家可以把它当成0毫秒，因为0毫秒的话由于浏览器渲染太快，录屏不好捕捉，我又没啥录屏慢放的工具，大家可以自行测试的，结果也是一样，最安全的方法是写一个`index.html`文件，在这个文件中插入上面的js脚本，然后浏览器打开，谷歌下使用控制台中`performance`功能查看一帧一帧的加载最为恰当，不过这样录屏不好录所以。。。

回归正题，之所以会卡一下蓝色，是因为以上代码属于两次`宏任务`，第一次`宏任务`执行的代码是将背景变成蓝色，然后触发渲染，将页面变成蓝色，再触发第二次宏任务将背景变成黑色

再来看

```js
document.body.style = 'background:blue'
console.log(1);
Promise.resolve().then(()=>{
    console.log(2);
    document.body.style = 'background:pink'
});
console.log(3);
```

![img](16fb7c909570edd9tplv-t2oaga2asx-zoom-in-crop-mark4536000.awebp)

控制台输出 1 3 2 , 是因为 promise 对象的 then 方法的回调函数是异步执行，所以 2 最后输出

页面的背景色直接变成粉色，没有经过蓝色的阶段，是因为，我们在宏任务中将背景设置为蓝色，但在进行渲染前执行了微任务， 在微任务中将背景变成了粉色，然后才执行的渲染

### 微任务宏任务注意点

- 浏览器会先执行一个宏任务，紧接着执行当前执行栈产生的微任务，再进行渲染，然后再执行下一个宏任务
- 微任务和宏任务不在一个任务队列，不在一个任务队列
  - 例如`setTimeout`是一个宏任务，它的事件回调在宏任务队列，`Promise.then()`是一个微任务，它的事件回调在微任务队列，二者并不是一个任务队列
  - 以Chrome 为例，有关渲染的都是在渲染进程中执行，渲染进程中的任务（DOM树构建，js解析…等等）需要主线程执行的任务都会在主线程中执行，而浏览器维护了一套事件循环机制，主线程上的任务都会放到消息队列中执行，主线程会循环消息队列，并从头部取出任务进行执行，如果执行过程中产生其他任务需要主线程执行的，渲染进程中的其他线程会把该任务塞入到消息队列的尾部，消息队列中的任务都是宏任务
  - 微任务是如何产生的呢？当执行到script脚本的时候，js引擎会为全局创建一个执行上下文，在该执行上下文中维护了一个微任务队列，当遇到微任务，就会把微任务回调放在微队列中，当所有的js代码执行完毕，在退出全局上下文之前引擎会去检查该队列，有回调就执行，没有就退出执行上下文，这也就是为什么微任务要早于宏任务，也是大家常说的，每个宏任务都有一个微任务队列（由于定时器是浏览器的API，所以定时器是宏任务，在js中遇到定时器会也是放入到浏览器的队列中）

此时，你可能还很迷惑，没关系，请接着往下看

### 图解宏任务和微任务

![img](16fb7adf5afc036dtplv-t2oaga2asx-zoom-in-crop-mark4536000.awebp)

首先执行一个宏任务，执行结束后判断是否存在微任务

有微任务先执行所有的微任务，再渲染，没有微任务则直接渲染

然后再接着执行下一个宏任务

## 图解完整的Event Loop

![img](16fb7ae3b678f1eatplv-t2oaga2asx-zoom-in-crop-mark4536000.awebp)

首先，整体的script(作为第一个宏任务)开始执行的时候，会把所有代码分为`同步任务`、`异步任务`两部分

同步任务会直接进入主线程依次执行

异步任务会再分为宏任务和微任务

宏任务进入到Event Table中，并在里面注册回调函数，每当指定的事件完成时，Event Table会将这个函数移到Event Queue中

微任务也会进入到另一个Event Table中，并在里面注册回调函数，每当指定的事件完成时，Event Table会将这个函数移到Event Queue中

当主线程内的任务执行完毕，主线程为空时，会检查微任务的Event Queue，如果有任务，就全部执行，如果没有就执行下一个宏任务

上述过程会不断重复，这就是Event Loop，比较完整的事件循环

## 关于Promise

`new Promise(() => {}).then()` ，我们来看这样一个Promise代码

前面的 `new Promise()` 这一部分是一个构造函数，这是一个同步任务

后面的 `.then()` 才是一个异步微任务，这一点是非常重要的

```js
new Promise((resolve) => {
	console.log(1)
  resolve()
}).then(()=>{
	console.log(2)
})
console.log(3)
```

上面代码输出`1 3 2`

## 关于 async/await 函数

async/await本质上还是基于Promise的一些封装，而Promise是属于微任务的一种

所以在使用await关键字与Promise.then效果类似

```js
setTimeout(() => console.log(4))

async function test() {
  console.log(1)
  await Promise.resolve()
  console.log(3)
}

test()

console.log(2)
```

上述代码输出`1 2 3 4`

可以理解为，`await` 以前的代码，相当于与 `new Promise` 的同步代码，`await` 以后的代码相当于 `Promise.then`的异步

## 举栗印证

首先给大家来一个比较直观的动图

![img](16fb7d0f356a33a4tplv-t2oaga2asx-zoom-in-crop-mark4536000.awebp)



之所以放这个动图，就是为了向大家推荐这篇好文，动图录屏自参考链接【1】

极力推荐大家看看这篇帖子，非常nice，分步动画生动且直观，有时间的话可以自己去体验下

不过在看这个帖子之前你要先了解下运行机制会更好读懂些

接下来这个来自网上随意找的一个比较简单的面试题，求输出结果

```js
function test() {
  console.log(1)
  setTimeout(function () { 	// timer1
    console.log(2)
  }, 1000)
}

test();

setTimeout(function () { 		// timer2
  console.log(3)
})

new Promise(function (resolve) {
  console.log(4)
  setTimeout(function () { 	// timer3
    console.log(5)
  }, 100)
  resolve()
}).then(function () {
  setTimeout(function () { 	// timer4
    console.log(6)
  }, 0)
  console.log(7)
})

console.log(8)
```

结合我们上述的JS运行机制再来看这道题就简单明了的多了

JS是顺序从上而下执行

执行到test()，test方法为同步，直接执行，`console.log(1)`打印1

test方法中setTimeout为异步宏任务，回调我们把它记做timer1放入宏任务队列

接着执行，test方法下面有一个setTimeout为异步宏任务，回调我们把它记做timer2放入宏任务队列

接着执行promise，new Promise是同步任务，直接执行，打印4

new Promise里面的setTimeout是异步宏任务，回调我们记做timer3放到宏任务队列

Promise.then是微任务，放到微任务队列

console.log(8)是同步任务，直接执行，打印8

主线程任务执行完毕，检查微任务队列中有Promise.then

开始执行微任务，发现有setTimeout是异步宏任务，记做timer4放到宏任务队列

微任务队列中的console.log(7)是同步任务，直接执行，打印7

微任务执行完毕，第一次循环结束

检查宏任务队列，里面有timer1、timer2、timer3、timer4，四个定时器宏任务，按照定时器延迟时间得到可以执行的顺序，即Event Queue：timer2、timer4、timer3、timer1，依次拿出放入执行栈末尾执行 **(插播一条：浏览器 event loop 的 Macrotask queue，就是宏任务队列在每次循环中只会读取一个任务)**

执行timer2，console.log(3)为同步任务，直接执行，打印3

检查没有微任务，第二次Event Loop结束

执行timer4，console.log(6)为同步任务，直接执行，打印6

检查没有微任务，第三次Event Loop结束

执行timer3，console.log(5)同步任务，直接执行，打印5

检查没有微任务，第四次Event Loop结束

执行timer1，console.log(2)同步任务，直接执行，打印2

检查没有微任务，也没有宏任务，第五次Event Loop结束

结果：1，4，8，7，3，6，5，2

## 提一下NodeJS中的运行机制

上面的一切都是针对于浏览器的EventLoop

虽然NodeJS中的JavaScript运行环境也是V8，也是单线程，但是，还是有一些与浏览器中的表现是不一样的

其实nodejs与浏览器的区别，就是nodejs的宏任务分好几种类型，而这好几种又有不同的任务队列，而不同的任务队列又有顺序区别，而微任务是穿插在每一种宏任务之间的

在node环境下，process.nextTick的优先级高于Promise，可以简单理解为在宏任务结束后会先执行微任务队列中的nextTickQueue部分，然后才会执行微任务中的Promise部分

![img](16fb7aed8db21b8dtplv-t2oaga2asx-zoom-in-crop-mark4536000.awebp)

上图来自NodeJS官网

如上图所示，nodejs的宏任务分好几种类型，我们只简单介绍大体内容了解，不详细解释，不然又是啰哩啰嗦一大篇

NodeJS的Event Loop相对比较麻烦

```
Node会先执行所有类型为 timers 的 MacroTask，然后执行所有的 MicroTask(NextTick例外)

进入 poll 阶段，执行几乎所有 MacroTask，然后执行所有的 MicroTask

再执行所有类型为 check 的 MacroTask，然后执行所有的 MicroTask

再执行所有类型为 close callbacks 的 MacroTask，然后执行所有的 MicroTask

至此，完成一个 Tick，回到 timers 阶段

……

如此反复，无穷无尽……
```

反观浏览器中Event Loop就比较容易理解

```
先执行一个 MacroTask，然后执行所有的 MicroTask

再执行一个 MacroTask，然后执行所有的 MicroTask

……

如此反复，无穷无尽……
```

好了，关于Node中各个类型阶段的解析，这里就不过多说明了，自己查阅资料吧，这里就是简单提一下，NodeJS的Event Loop解释起来比浏览器这繁杂，这里就只做个对比

# JS工具库

## jQuery



## Vue

见Vue篇

## React

见React篇













































































































