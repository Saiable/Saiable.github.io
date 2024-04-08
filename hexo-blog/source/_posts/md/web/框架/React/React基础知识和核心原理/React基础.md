---
title: 'React基本使用'
date: 2023-01-12 20:30:40
cover: false
toc_number: false
tags:
- React
categories: 'React'
typora-root-url: React基础
---

# `React`简介

## 是什么

用于构建用户界面的`JavaScript`库

以前编写页面的流程

- 发送请求获取数据
- 处理数据（过滤、整理格式等）
- 操作`DOM`呈现页面



`React`核心：将数据渲染成`HTML`视图

## 谁开发的

由`Facebook`开发，且开源

- 起初由`Facebook`的软件工程师`Jordan Walke`创建
- 于2011年部署于`Facebook`的`newsfeed`
- 随后在2012年部署于`Instagram`
- 2013年5月宣布开源
- ...

## 为什么要学

- 原生`JS`操作`DOM`繁琐、效率低（`DOM-API`操作`UI`）
- 使用原生`JS`直接操作DOM，浏览器会进行大量的重绘重排
- 原生`JS`没有组件化编码方案，代码复用率低

## `React`特点

- 采用组件化模式、声明式编码，提高开发效率及组件复用率
- 在`React Native`中可以使用`React`语法进行移动端开发
- 使用虚拟`DOM`+优秀的`Diffing`算法，尽量减少与真实`DOM`的交互

## 前置知识

- 判断`this`指向
- `class`
- `ESNext`
- `npm`
- 原型与原型链
- 数组常用API
- 模块化

# `React`入门

## 官网

英文官网：https://reactjs.org/

中文官网：https://zh-hans.reactjs.org/

## `React`基本使用

相关`js`库

- `react.js`：`React`核心库
- `react-dom.js`：提供操作`DOM`的`react`扩展库
- `babel.min.js`：解析`JSX`语法代码，转为`js`代码的库
- 使用在线`JS`文件：https://reactjs.org/docs/add-react-to-a-website.html



版本变更：

https://github.com/facebook/react/blob/main/CHANGELOG.md

目前最新版本为`18.2.0 (June 14, 2022)`

本教程版本为`16.8`，有点旧了，但学个基础语法是够用的

### `HelloReact`案例

https://reactjs.org/docs/add-react-to-a-website.html

```html
<body>
    <!-- 准备容器 -->
    <div id="test"></div>
    <!-- 核心库要先引入 -->
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>

    <!-- type类型要写babel -->
    <script type="text/babel">
      // 1.创建虚拟DOM
      const VDOM = <h1>Hello, React</h1>; // 不要写引号
      // 2.渲染虚拟DOM到页面
      // ReactDOM.render(VDOM, domContainer) // React18中ReactDOM.render方法不再支持
      const domContainer = document.querySelector("#test");
      const root = ReactDOM.createRoot(domContainer);
      root.render(VDOM);
    </script>
  </body>
```

### 虚拟`DOM`的两种创建方式

方式一：`JSX`

```jsx
const VDOM = <h1>Hello, React</h1>;
```

方式二：`JS`

```js
const VDOM = React.createElement('h1', {id: 'title'}, 'Hello, React2')
```



需求：`h1`里包一个`span`，内容不变

`JSX`

```jsx
const VDOM = <h1><span>Hello, React</span></h1>;
```

`JS`

```js
const VDOM = React.createElement('h1', {id: 'title'}, React.createElement('span', {}, 'Hello, React2'))
```

四层标签嵌套，`JS`写法就很痛苦了

`JSX`作用：更流畅的创建虚拟`DOM`，就是原始`JS`创建虚拟`DOM`的语法糖

```jsx
const VDOM = (
	<h1>
        <span>Hello, React</span>
    </h1>
);
```

`babel`其实就是讲`jsx`语法转化成了`createElement`语法了

### 虚拟`DOM`与真实`DOM`

虚拟`DOM`

- 就是一般对象

- 虚拟`DOM`比较轻，真实`DOM`比较重。因为虚拟`DOM`是`React`内部在用，无需那么多的属性

- 虚拟`DOM`最终会被`React`转化为真实`DOM`，呈现在页面上

  ![image-20230112154603832](image-20230112154603832.png)





真实`DOM`

![image-20230112154745681](image-20230112154745681.png)

- `console.dir`看下真实`DOM`身上的属性，有很多很多

  ![image-20230112155151094](image-20230112155151094.png)

  

## `JSX`语法

- 全称：`JavaScript XML`
- `React`定义的一种类似于`XML`的`JS`扩展语法：`JS XML`
- 本质是`React.createElement(co)`
- 语法规则
  - 定义虚拟`DOM`时，无需引号
  - 标签中混入`JS`表达式时，要用`{}`
  - 样式的类名指定，用`className`，不能用`class`
    - `class`是`ES6`中的关键字
  - 内联样式，要用`style={{key: value}}`的形式
    - 外层的`{}`表示要写`js`表达式
    - 内层的`{}`表示一个对象
    - `key`如果是多个单词，采用小驼峰
    - `value`是字符串，要加引号
  - 只能有一个根标签
  - 标签必须闭合
  - 标签首字母
    - 小写开头：将标签转为`HTML`中的同名元素，若无同名元素，则报错
    - 大写开头：则认为是组件



# `React`面向组件编程

## 前置准备

安装`React`开发插件，edge浏览器插件市场搜索并安装：

[React Developer Tools - Microsoft Edge Addons](https://microsoftedge.microsoft.com/addons/detail/react-developer-tools/gpphkfbcpidddadnkolkpfckpihlkkil?hl=zh-CN)

![image-20230113102015048](image-20230113102015048.png)

安装成功后，打开https://www.meituan.com/，美团PC官网就是用React写的

审查元素，有两个额外的标签页：

![image-20230113102723136](image-20230113102723136.png)



## 基本理解和使用

### 函数式组件

```js
<script type="text/babel">
      // 1.创建函数式组件，组件是结构、样式等资源的集合
      function Demo() { // 首字母必须大写
        return <h2>我是用函数定义的组件（适用于简单组件的定义）</h2>; // 返回最基础的一个结构
      }

      // 2.渲染组件到页面
      const container = document.querySelector("#test");
      const root = ReactDOM.createRoot(container);
      root.render(<Demo/>); // 要写成闭合标签
    
</script>
```

`Demo`组件中，如果打印`this`，值是`undefined`，因为`babel`转化开启了严格模式

[Babel 中文网 · Babel - 下一代 JavaScript 语法的编译器 (babeljs.cn)](https://www.babeljs.cn/repl#?browsers=defaults%2C not ie 11%2C not ie_mob 11&build=&builtIns=false&corejs=3.21&spec=false&loose=false&code_lz=GYVwdgxgLglg9mABAEQKYFs4AoCUiDeiA9EYoGmZg6tqCz1oKP6g3hmDkmoJmKAUIogE6pQgdIA8ACwBMAPkCIRoHozQBSugX8VADqaAs7UCScoBC3QCN-gN7lAEP-AgBOmA4uUAB3oFVlLapWBIf_5ERogNzFSgFfjAe2qAAc0Bf6oAEPVYAA5QCo5QGW_QBDzFgBfIA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=env%2Creact%2Cstage-2&prettier=false&targets=&version=7.20.12&externalPlugins=&assumptions={})

![image-20230113110014236](image-20230113110014236.png)

执行`root.render(<Demo/>)`，发生了什么

- `React`解析组件标签，找到组件
- 发现组件是函数定义，调用该函数，将返回的虚拟`DOM`转为真实`DOM`，呈现在页面中

### 类语法



### 类式组件

```js
    <script type="text/babel">
      // 1.创建类式组件，必须要继承React.Component
      class Demo extends React.Component {
        render() { // 必须要有render函数
          return <h2>我是用类定义的组件（适用于复杂组件的定义）</h2>
        }
      }
      // 2.渲染组件到页面
      const container = document.querySelector("#test");
      const root = ReactDOM.createRoot(container);
      root.render(<Demo/>); // 这里的render和上面的render没有任何关系，只是重名
    </script>
```

`render`函数是在`Demo`的原型对象上

![image-20230113111908803](image-20230113111908803.png)

`render`函数要被调用，肯定要`new`一个实例的，`React`默认创建了组件实例

还是回到

执行`root.render(<Demo/>)`，发生了什么

这个问题：

- `React`解析组件标签，找到组件

- 发现组件是类定义，`new`出来类的实例，并通过该实例调用原型的`render`方法

  - `render`中的`this`，指向该实例，通常称之为组件实例对象或组件对象

    ![image-20230113112412717](image-20230113112412717.png)

- 将`render`返回的虚拟`DOM`转为真实`DOM`，呈现在页面中

## 组件实例三大核心属性

### `state`

- `state`是组件对象最重要的属性，值是对象（可以包含多个`key-value`的组合）
- 组件被称为“状态机”，通过更新组件的`state`来更新对应的页面显示（重新渲染组件）

注意点：

- 组件中的`render`方法中的`this`为组件实例对象
- 组件自定义的方法中，`this`为`undefined`如何解决？
  - 强制绑定`this`：通过函数对象的`bind()`
  - 箭头函数
- 状态数据，不能直接修改或更新



#### 定义`state`

在类组件的构造器里初始化`state`

```js
      class Demo extends React.Component {
        constructor(props) {
          super(props)
          this.state = {
            isHot: false
          }
        }
        render() {
          console.log(this)
          return <h2>今天天气很{this.state.isHot ? '炎热' : '凉爽'}</h2>
        }
      }
```

![image-20230113143950939](image-20230113143950939.png)

#### 事件绑定

`React`重新封装了各种事件，`onclick`对应`onClick`，其它类似

```js
return <h2 onClick={demo}>今天天气很{isHot ? '炎热' : '凉爽'}</h2> // 不要加括号


// 最外层定义demo方法，但获取不到state
function demo() {
    console.log('标题被点击了')
}
```

如果将方法定义在外层，获取不到state，可以将方法写在类里面

```js
    class Demo extends React.Component {
      constructor(props) {
        super(props)
        this.state = {
          isHot: false
        }
      }
        
      // 函数写在class里面，通过this调用
      demo() {
        console.log('标题被点击了')
          console.log(this) // undefined
      }

      render() {
        console.log(this)
        const { isHot } = this.state
        return <h2 onClick={this.demo}>今天天气很{isHot ? '炎热' : '凉爽'}</h2>
      }
    }
```

但是：

`class`类中定义的方法， 都在局部开启了严格模式

由于点击事件，不是通过实例调用，而是作为回调，直接调用，所以内部`this`为`undefined`

解决类中`this`指向问题：

```js
      constructor(props) {
        super(props)
        this.state = {
          isHot: false
        }
        this.demo = this.demo.bind(this) // 将原型上的方法挂载到自身上
      }
```



#### 修改`state`

状态不可直接更改，类似于原生小程序的`setData`，`React`中使用组件实例原型的原型上的`setState`方法，是一个合并的操作

![image-20230113154252261](image-20230113154252261.png)

```js
      demo() {
        console.log('标题被点击了')
        const {isHot} = this.state
        this.setState({
          isHot: !isHot
        })
        console.log(this)
      }
```

`state`的每次变化：

- 构造器只调用一次

- `render`函数初始化会被调用一次，`state`变化时也会重新调用（1+N次）
- `demo`回调，点几次调用几次

#### `state`的简写方式

##### 标准写法

```js
class Demo extends React.Component {
      constructor(props) {
        super(props)
        console.log('constructor')
        this.state = {
          isHot: false
        }
        this.demo = this.demo.bind(this)
      }

      demo() {
        const {isHot} = this.state
        this.setState({
          isHot: !isHot
        })
      }

      render() {
        const { isHot } = this.state
        return <h2 onClick={this.demo}>今天天气很{isHot ? '炎热' : '凉爽'}</h2>
      }
    }
```

##### 简写

- 回调函数的简写

  - 箭头函数，没有`this`，如果写了`this`则向外层作用域寻找

- 初始化状态的简写

  - 类中可以直接写赋值语句

    ```js
    class Demo {
        a = 1 // 往实例上追加a，值为1
    }
    ```

- 简写

  ```js
     class Demo extends React.Component {
        state = {
          isHot: false
        }
  
        demo = () => {
          const { isHot } = this.state
          this.setState({
            isHot: !isHot
          })
        }
  
        render() {
          const { isHot } = this.state
          return <h2 onClick={this.demo}>今天天气很{isHot ? '炎热' : '凉爽'}</h2>
        }
      }
  ```

### `props`

- 每个组件对象，都会有`props`（`properties`）的简写
- 组件标签的所有属性都保存在`props`中

#### `props`的基本使用





### `refs`与事件处理



## 收集表单数据



## 组件生命周期



## 虚拟`DOM`与`DOM Diff`算法



# `React`应用（基于`React`脚手架）



# `React Ajax`



# `React Router`



# `React` `UI`组件库



# `Redux`































































































































