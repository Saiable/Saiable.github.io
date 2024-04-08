---
title: Vue2源码解析
date: 2022-7-01 06:40:42
cover: false
tags:
  - Vue
  - 源码
categories:
  - Vue
typora-root-url: Vue2源码
---

[TOC]

# 教程一

## 大纲

**第一周**（从零手写`Vue2`部分）https://www.bilibili.com/video/BV1mR4y1w7cU

- `Vue2`响应式原理，模板编译原理，虚拟`Dom`原理，`Vue`初渲染流程
- `Vue2`中生命周期原理，`mixin`原理，依赖收集`Watcher`、`Dep`原理
- 手写`computed`及`watch`原理，异步更新原理
- 手写`Vue2`中组件渲染原理、`Vue.extend`原理，`Vue2diff`算法

> 目标：掌握`Vue2`**核心源码及核心设计思想**

**第二周**（从0手写`VueRouter`及`Vuex`）

- 掌握`HashHistory`、`BrowserHistory`及路由钩子实现原理，及`RouterView`、`RouterLink`组件实现
- 从0实现`Vuex`，彻底掌握`Vuex`设计思想

> 目标：掌握前端路由实现原理及状态管理实现原理

**第三周**

- 剖析`Vue2`源码，调试`Vue2`核心源码
- `Vue2`常见面试题解析

> 目标：掌握如何阅读框架源码，掌握`Vue`相关面试题

**第四周**（`TS`详解、掌握`TS`核心应用）

- `TS`环境搭建、基础类型、类型推导、类
- 接口、泛型、`TS`兼容性
- 类型保护、高级类型、模块命名空间等

> 目标：掌握`TS`的使用为学习`Vue3`做准备

**第五周**（`Vue3`核心讲解）

- 掌握`Vue3`核心语法及组件化开发，`Vue3`新特性和新增`API`
- `Vue3 + Vite`掌握`VueRouter4`及`Vuex4`应用，`element-plus`组件库使用
- `Vue3 + TS`后台管理系统项目实战（一）

> 目标：快速上手`Vue3`，利用`Vue3 + TS`开发项目

**第六周**（`Vue3`项目实战）

- `Vue3 + TS`后台管理系统项目实战（二）
- `Vue3 + TS`后台管理系统项目实战（三）
- 从零实现`Vite`，掌握`Vite`原理
- `Vue3`源码剖析，从零实现`Vue3`源码
- 从零搭建`Vue3`组件库

## **第一周**（从零手写`Vue2`部分）

### 使用`Rollup`搭建开发环境

不是重点，只会搭建最简单的环境方便编写`vue`代码

一般类库的打包，会用`rollup`，打包的体积相较`webpack`会更小，因为`rollup`更专注一些，主要用来打包`js`

新建文件夹`VUE2-STAGE`

```bash
npm init
# 一路回车

npm i rollup rollup-plugin-babel @babel/core @babel/preset-env -D

# 安装rollup
npm i rollup 

# 安装babel，将高级语法转换成低级语法
npm i rollup-plugin-babel

# 安装babel的核心模块
npm i @babel/core

# 安装预设(比如说怎么把let、const转换成var)
npm i @babel/preset-env
```

实操注意点：

提示`rollup-plugin-babel`不更新维护了

```bash
[root@VM-4-12-centos VUE2_STAGE]# npm i rollup rollup-plugin-babel @babel/core @babel/preset-env -D
npm WARN deprecated rollup-plugin-babel@4.4.0: This package has been deprecated and is no longer maintained. Please use @rollup/plugin-babel.
```


解决办法：

卸载`rollup-plugin-babel`：

```bash
npm uninstall rollup-plugin-babel
```

安装推荐的包

```bash
npm i @rollup/plugin-babel -D
```

安装完毕后的包信息：

```json
{
  "name": "vue2_stage",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@babel/core": "^7.18.6",
    "@babel/preset-env": "^7.18.6",
    "@rollup/plugin-babel": "^5.3.1",
    "rollup": "^2.75.7"
  }
}
```

根目录`VUE2-STAGE`新建`rollup`配置文件`rollup.config.js`

```js
// rollup 默认可以导出一个对象，作为打包的配置文件

import babel from  '@rollup/plugin-babel'
export default {
    input: './src/index.js', // 入口
    output: {
        file: './dist/vue.js', // 出口
        name: 'Vue', // 在global全局上，增添一个Vue对象，我们就可以new Vue了（global.Vue）
        format: 'umd', // options: 1.esm es6模块，相当于没有打包了 2.commonjs node中使用 3.iife 自执行函数 4.umd 兼容amd和commonjs
        sourcemap: true // 可以调试源代码
    },
    plugins: [
        // 需要新建babel的配置文件，既可以是js文件，也可以是.rc文件,
        // 这里和视频的保持一致
        babel({
            exclude: 'node_modules/**', // 排除第三方模块 ，**表示任意文件夹
            babelHelpers: 'bundled' // https://www.npmjs.com/package/@rollup/plugin-babel  搜索babelHelpers 
        }) // 所有的插件都是函数
    ]
}
```

根目录新建`.babelrc`文件

```json
{
  "presets": [
    "@babel/preset-env"
  ]
}
```

配置较少的话，也可以直接写在`rollup.config.js`中

在`package.json`中添加`npm run dev`脚本

`-c`：指定默认的配置文件

`-w`：监视文件变化

```json
// ...
  "scripts": {
    "dev": "rollup -cw"
  },
// ...
```

根目录新建打包入口文件`src/index.js`

```js
export const a = 100
export default {
    a: 1
}
```

测试能否打包

```bash
npm run dev
```

成功显示如下信息

```bash
[root@VM-4-12-centos VUE2_STAGE]# npm run dev

> vue2_stage@1.0.0 dev
> rollup -cw
rollup v2.75.7
bundles ./src/index.js → dist/vue.js...
created dist/vue.js in 304ms

[2022-06-30 17:36:35] waiting for changes...
```

可能会提示你修改`package.json`

新增字段：

```
  "type": "module"
```

根目录下会生成之前配置的目录及文件夹

```bash
[root@VM-4-12-centos VUE2_STAGE]# tree ./dist/
./dist/
|-- vue.js
`-- vue.js.map
```

`index.js`对应的打包文件

```js
(function (global, factory) {
    typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports) :
    typeof define === 'function' && define.amd ? define(['exports'], factory) :
    (global = typeof globalThis !== 'undefined' ? globalThis : global || self, factory(global.Vue = {}));
})(this, (function (exports) { 'use strict';

    var a = 100;
    var index = {
      a: 1
    };

    exports.a = a;
    exports["default"] = index;

    Object.defineProperty(exports, '__esModule', { value: true });

}));
//# sourceMappingURL=vue.js.map
```

可以新建`index.html`并引入该打包文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Title</title>
</head>
<body>
<script src="vue.js"></script>
<script>
  console.log(Vue)
</script>
</body>
</html>
```

全局上多了一个`Vue`的对象，身上的属性就是我们导出的，效果如下：

![image-20220630185136069](image-20220630185136069.png)

`index.js`中也可以设置断点，进行调试

```js
export const a = 100
debuger
export default {
    a: 1
}
```

已完成：

- [x] 1.使用`Rollup`搭建开发环境

### 初始化数据

响应式数据的核心？数据变化了，我可以监控到

监控的是什么呢？是数据的**取值**和**更改值**

监控到然后干嘛呢？更新视图

满足上面要求的数据，就是响应式数据。简单点来说，响应式数据变化可以更新视图

不考虑工程化开发，当初在`html`中我们是这么写`Vue`代码的

把所有需要的数据，都放在配置对象里

```html
<script src='vue.js'></script>
<script>
    const vm = new Vue({
        data: {
            name: 'sai',
            age: 18
        }
    })
</script>
```

> Tips：`Vue2`中没有用类的写法，因为类的方法如果有很多，就都耦合在一起了，函数的写法直接`Vue.prototype`就可以了（虽然类也可以Vue.prototype这样写，但一般不会这样搞）
> 
> ```js
> function Vue() {
> 
> }
> 
> Vue.prototype.a = function(){}
> Vue.prototype.b = function(){}
> Vue.prototype.c = function(){}
> 
> export default Vue
> ```
> 
> 并且可以将扩展的功能单独放在一个文件中，方便管理

那么现在要干嘛呢？

模拟实现`Vue`的功能

`index.js`

`options`就是用户传入的选项，拿到`options`后，肯定要处理下的

我们给原型对象上添加个`_init`方法，专门用来做初始化

```js
function Vue(options) { // options就是用户的选项
    // 拿到用户的options，做一下初始化
    this._init(options)
}

// 用于初始化操作
Vue.prototype._init = function(options) {

}

export default Vue
```

但是不能都写在`index.js`里，不然代码一多就完犊子了

新建`src/init.js`

```js
// 用于初始化操作
Vue.prototype._init = function(options) {

}
```

问题来了，这个时候`Vue`就丢失了，咋整？

可以把初始化操作，封装成函数并导出，这个函数接收一个形参

`init.js`

```js
// 就是给Vue增加_init方法的
export function initMixin(Vue) {
    // 用于初始化操作
    Vue.prototype._init = function(options) {

    }
}
```

在`index.js`就可以传入实参`Vue`使用了

```js
function Vue(options) { // options就是用户的选项
    // 拿到用户的options，做一下初始化
    this._init(options)
}

// 给Vue增加init方法
initMixin(Vue) // 扩展了init方法

export default Vue
```

`initMixin`相当于扩展了`_init`方法，后续再有逻辑，可以再`initXXX(xxx)`，就可以原型方法，扩展成一个个函数，通过函数的形式在原型上扩展功能

靠谱！！！

需要把`options`扩展到`vm`实例上，为什么不直接用呢？

- 或许扩展的第二个方法，怎么拿到`options`呢，只有通过实例来传递

看下面的代码：

`init.js`

```js
export function initMixin(Vue) {
    Vue.prototype._init = function(options) {
        this.$options = options // Vue中采取$作为自己的变量，如果传入了形如$name这样的以$开头的变量，是不会被Vue实例管理的（Vue给自己画了个界限，所有以$开头的，都认为是自己的属性）
        debugger
    }
    // Vue.prototype.xxx = function() {
        // 扩展的第二个方法，怎么拿到options呢，只有通过实例来传递
    // }
}
```

可以看到，此时`Vue`上多了`$options`属性

![image-20220702210913280](image-20220702210913280.png)

写法优化

```js
export function initMixin(Vue) {
    Vue.prototype._init = function(options) {
        const vm = this // 保留下this，不然后面一直写this，写法上有点恶心
        vm.$options = options // 将用户的选项挂载到实例上
          debugger      

    }
}
```

`this`和`vm`都指向`Vue`实例

![image-20220702211212033](image-20220702211212033.png)

挂载完`options`之后，干嘛呢？

我们不是传入了`data`这些配置项嘛，要进行初始化状态，`Vue`中的状态有很多，如`props/data/computed/watch`等等配置项，这些都是要初始化的

```js
export function initMixin(Vue) {
    Vue.prototype._init = function(options) {
        const vm = this
        vm.$options = options

        // 初始化状态 data/computed/watch等等配置项
        initState(vm)
        // 初始化状态之后，还要去编译模板、创建虚拟dom等
    }
}

function initState(vm) {
    const opts = vm.$options // 获取所有的选项
    // 拿到所有的选项之后，我们先处理`data`
    // 一项项的来处理
    // 在`data`之前处理`props`，但目前我们先只处理data
    //if(opts.props) {
    //    initProps()
    //}

    // 处理`data`
    if(opts.data) {
        initData(vm)
    }
}

function initData(vm) {
    // 代理数据
    let data = vm.$options.data // data有两种情况，对象或函数
    console.log(this) // 这里的this是undefined
    data = typeof data === 'function' ? data.call(this) : data // 对data类型进行判断后，拿到data
    debugger
}
```

![image-20220704063245372](image-20220704063245372.png)

将`initState`和`initData`这两个初始化数据的方法，单独抽出来，放到`state.js`中

```js
export function initState(vm) {
    const opts = vm.$options
    if(opts.data) {
        initData(vm)
    }
}

function initData(vm) {
    let data = vm.$options.data // data可能是函数或对象
    data = typeof data === 'function' ? data.call(vm) : data
    debugger
}
```

至此，状态初始化中的数据初始化，已经完成了第一步，拿到用户自定义配置

> 本小节技能点需完善的地方
> 
> - 浏览器控制台调试大全
> - `js`中`this`的系列问题
> - `js`中的`call`方法

下一小节，实现对象的响应式原理

### `Vue`响应式原理实现

#### 对象属性劫持

对数据进行劫持

`vue2`中采用了`defineProperty`

我们定义一个方法`obeserve`观测数据，这是一个核心模块，我们单独新建observe文件夹进行处理

`state.js`

```js
import {observe} from "./observe/index"
// ...
function initData(vm) {
    let data = vm.$options.data
    data = typeof data === 'function' ? data.call(vm) : data
    // 对数据进行劫持,vue2中采用了defineProperty
    // 定义一个方法obeserve观测数据，这是一个核心模块，我们单独新建observe文件夹进行处理
    observe(data)
}
```

新建`src/observe/index.js`

```js
export function observe(data) {
    console.log(data)
    debugger
}
```

`observe`中可以拿到`data`数据

![image-20220710111903316](image-20220710111903316.png)

##### 实现对象属性劫持

在`observe`方法中对对象类型的数据进行劫持

- 先对传入的数据类型进行判断，只对对象进行劫持
- 如果一个对象被劫持过了，那就不需要再被劫持了
  - 要判断一个对象是否被劫持过
    - 可以添加一个实例，用实例来判断是否被劫持过。
    - 在`observe`函数中新建`Observer`类，这个类是专门用来观测数据的，如果数据被观测过，那么它的实例就是这个类？？
      - 这里看不明白，可以直接先往下看，到具体代码那儿就清楚了

`observe/index.js`

```js
class Observer {
    constructor(data) {

    }
}

export function observe(data) {
    console.log(data)
    // 对data类型进行判断
    if(typeof data !== 'object' || data == null) {
        return // 只对对象进行劫持
    }

    // 如要考虑到一个对象已经被劫持的情况
    // 如果一个对象已经被劫持过了，那么就不需要再被劫持
    // 可以添加一个实例，用实例来判断是否被劫持过（应该是用实例身上的属性）
    return new Observer(data)
}
```

问题：`Object.defineProperty`只能劫持已经存在的数据，后增的或者删除的属性，是劫持不到的（为此`Vue2`单独写了一些`api`，比如说`$set`、`$delete`）

- `Observer`类型中，要遍历对象
  - 可以专门写个`walk`方法来干这件事，循环对象，对属性依此劫持
  - 拿到所有的`key`后遍历，“重新”定义属性（重新定义的话，相当于每个`key`都要遍历，这也是`Vue2`性能较差的原因）
    - 定义`defineReactive`方法，实现将某个对象数据定义成响应式
    - 该方法需要后面可以单独使用，所以写在`Observer`同级，并导出

`observer/index.js`

```js
class Observer {
    constructor(data) {
        this.walk(data)
    }

    walk(data) { // 循环对象，对属性依此劫持
        // 重新定义属性 性能差
        Object.keys(data).forEach(key => defineReactive(data, key, data[key]))
    }
}

// 向外导出该方法，供单独使用
export function defineReactive(target, key, value) { // 闭包
    Object.defineProperty(target, key, {
        get() { // 取值的时候，会执行get
            return value
        },
        set(newValue) { // 修改值的时候，会执行set
            if(value == newValue) return
            value = newValue
        }
    })
}
// ...
```

我们在使用的时候，打印下`vm`实例

`index.html`

```html
  <script src="./vue.js"></script>
  <script>
    const vm = new Vue({
        data() {
            return {
                name: 'sai',
                age: 11
            }
        }
    })
    console.log(vm)
  </script>
```

![image-20220711065304265](image-20220711065304265.png)

虽然定义了响应式，但此时`vm`实例上直接是拿不到`data`的

我们可以在`state.js`的`initData`中，在`vm`身上增加`_data`属性，将`data`赋值给`vm._data`（在观测属性之前）

`state.js`

```js
// ...
function initData(vm) {
    let data = vm.$options.data
    data = typeof data === 'function' ? data.call(vm) : data

    // 观测之前，把data放一份到vm._data身上
    vm._data = data
    observe(data)
}
```

此时`vm`身上就有了`_data`，存着`data`的响应式数据

![image-20220711065849648](image-20220711065849648.png)

思考：`vm._data=data`是在做观测数据之前存的，为啥`_data`也变成了响应式的呢？

- 直接赋值是浅拷贝，`_data`和`data`变量中存的是对象值在堆内存中的引用地址
- 原对象的值变了，但`_data`中存的引用地址没有变
- 所以即使是后做的响应式，`vm._data`自然也是响应式的了
- 观测数据之后，进行赋值也不是不可以

##### 用户用法简化

现在还有个小问题，就是取数的时候，要写成`vm._data.name`，每次都要加个`_data`，有点恶心

我们能不能直接`vm.name`去取值呢

- 当用户在`vm.name`上取值时，我们就代理到`vm._data.name`上
- 将`vm._data`用`vm`来代理
  - 依旧是做一个循环来处理
  - 自定义`proxy`方法：`proxy(vm, '_data')`，代理`vm`身上的`_data`

`state.js`

```js
// ...
function proxy(vm, target, key) {
    Object.defineProperty(vm, key, { // vm.name
        get() {
            return vm[target][key] // vm.name实际上是去vm._data.name上去取值了
        }
    })
}

function initData(vm) {
    let data = vm.$options.data
    data = typeof data === 'function' ? data.call(vm) : data

    vm._data = data

    observe(data)


    // 将vm._data用vm来代理
    for (let key in data) {
        proxy(vm, '_data', key)
    }
}
```

![image-20220711144219711](image-20220711144219711.png)

我们先写`get`方法，可以看到`vm`代理了`vm._data`，身上有了`name`和`age`属性

同样，在设置值时也要加个代理

`state.js`

```js
// ...

function proxy(vm, target, key) {
    Object.defineProperty(vm, key, { // vm.name
        get() {
            return vm[target][key] // vm.name实际上是去vm._data.name上去取值了
        },
        set(newValue) {
            vm[target][key] = newValue // 这性能的确不太好，每一个`key`都加了一层
        }
    })
}

// ...
```

![image-20220711145232926](image-20220711145232926.png)

此时写法上就可以更便捷的取值及修改值了

##### 嵌套对象属性劫持

还有个问题：上面的写法只会监测到对象的第一层，一旦传入的`data`是嵌套的，里面的属性并没有被监测到

如下所示，`address`内部属性并没有被劫持

`index.html`

```html
  <script src="./vue.js"></script>
  <script>
    const vm = new Vue({
        data() {
            return {
                name: 'sai',
                age: 11,
                address: {
                    street: 'RoadA',
                    room: 123
                }
            }
        }
    })
    console.log(vm.name)
  </script>
```

![image-20220711145822997](image-20220711145822997.png)

当初的`defineReactive`函数，入参的`value`可能是个对象

- 再次调用`observe`方法，如果`value`是个对象，会再次创建Observer实例，再次调用walk方法，劫持每个属性
- 这样就实现了对所有的对象，都进行了属性劫持
- 是个递归，性能消耗也是可以的

`observe/index.js`

```js
class Observer {
    constructor(data) {
        this.walk(data)
    }

    walk(data) {
        Object.keys(data).forEach(key => defineReactive(data, key, data[key]))
    }
}

export function defineReactive(target, key, value) { // value可能是个对象
    observe(value) // observe内部对value进行判断了，是个对象，会再次创建Observer实例，再次调用walk方法，劫持每个属性
    Object.defineProperty(target, key, {
        get() {
            return value
        },
        set(newValue) {
            if(value == newValue) return
            value = newValue
        }
    })
}

export function observe(data) {

    if(typeof data !== 'object' || data == null) {
        return
    }

    return new Observer(data)
}
```

此时不管传入的是几层，对象属性都是被劫持过了的

![image-20220711151136480](image-20220711151136480.png)

至此，对象属性劫持的`define`核心逻辑就完成了

- 循环对象，给对象用`defineReactive`方法，把属性重新定义
  - 如果值还是对象的话，需要对这个对象进行递归操作
  - 这个用户在取值和修改值时，就可以监控到
- 对象被劫持完之后，为了方便用户获取，把`data`放在了`vm._data`上
  - 再用`vm`代理`vm._data`，这样用户在取值和修改值时，只要写成`vm.name`即可

已完成：

- [x] 1.使用`Rollup`搭建开发环境
- [x] 2.`Vue`响应式原理实现，对象属性劫持，深度属性劫持

#### 数组的方法劫持

如果`data`里面还有数组呢

`index.html`

```html
  <script src="./vue.js"></script>
  <script>
    const vm = new Vue({
        data() {
            return {
                name: 'sai',
                age: 11,
                address: {
                    street: 'RoadA',
                    room: 123
                },
                hobby: [ // data中含有数组
                    'eat',
                    'drink'
                ]
            }
        }
    })
    console.log(vm.name)
  </script>
```

我们看一下打印结果

![image-20220711161920103](image-20220711161920103.png)

`defineProperty`把数组里的每个属性，都增加了`get`、`set`，虽然通过`vm.hobby[0]`取值时，的确会被监测到，但是一旦数据量大了，就很消耗内存了

并且通过下标的方式来修改值，如修改第888个数组的值，`vm.hobby[888]=123`，一般也不会有这种操作

修改数组，很少用索引来修改数组，并且内部劫持数组，会浪费性能

用户一般都是都过方法来修改数组：`push`、`shift`等等

在`observe/index.js`里的`Observer`类的构造函数中

- 对数组类型进行判断
  - 如果是数组
    - 重写数组的方法，7个变异方法（可以修改数组本身的方法）
    - 如果数组内部，还嵌套有对象，如`hobby:['eat','drink',{a:1}]`也应该对对象属性进行劫持
      - 定义`observeArray`方法，实现该功能
        - 循环传入的`data`，递归调用`observe`方法
  - 如果不是数组
    - 继续之前的逻辑，添加代理

##### 数组中的对象属性劫持

定义`observeArray`方法，对数组中的对象进行属性劫持

`observe/index.js`

```js
class Observer {
    constructor(data) {
        if(Array.isArray(data)) {
            // 这里我们可以重写数组的7个变异方法（可以修改数组本身）
            this.observeArray(data) // 递归处理数组中的对象
        } else {
            this.walk(data)
        }
    }

    walk(data) {
        Object.keys(data).forEach(key => defineReactive(data, key, data[key]))
    }

    observeArray(data) {
        data.forEach(item => observe(item)) 
    }
}

// ...
```

打印结果如下：

![image-20220711164236905](image-20220711164236905.png)

我们在`defineReactive`的函数的`get`中添加打印语句：`console.log('key', key)`

然后在样例中取数`vm.hobby[2].a`

打印结果如下：

![image-20220711165311701](image-20220711165311701.png)

表示先取了`hobby`，再取了`a`，说明数组中的对象，是可以被监控到的

##### 数组的方法劫持

如果是`vm.hobby.push['1']`，会打印了`hobby`，说明目前只能监控到`get`，无法监控到修改

所以就需要重写数组的方法

- 在传入的`data`对应的`__proto__`属性中，重写各个数组方法
  
  - 给当前数组的的原型链，重新指向新的原型（也会覆盖掉`forEach`方法，可以先注释掉`observeArray`方法的调用）
    
    `observe/index.js`
    
    ```js
    class Observer {
        constructor(data) {
            if(Array.isArray(data)) {
                // 这里我们可以重写数组的7个变异方法（可以修改数组本身）
                data.__proto__ = {
                    push() {
                        console.log('重写的push')
                    }
                }
                // this.observeArray(data) // 递归处理数组中的对象
            } else {
                this.walk(data)
            }
        }
    
        walk(data) {
            Object.keys(data).forEach(key => defineReactive(data, key, data[key]))
        }
        observeArray(data) {
            data.forEach(item => observe(item))
        }
    }
    // ...
    ```
    
    打印如下：
    
    ![image-20220712054236080](image-20220712054236080.png)

当然我们不可能直接这样重写`__proto__`，我们需要保留数组原有的特性，并且可以重写部分方法，`observe`文件夹下新建`array.js`

- 存一份原来的`Array.prototype`，该对象上定义着各种方法
  
  ```js
  let oldArrayProto = Array.prototype
  ```
  
  ![image-20220714110255721](image-20220714110255721.png)

- 以`oldArrayProto`为原型定义新的变量
  
  ```js
  let newArrayProto = Object.create(oldArrayProto)
  ```
  
  目前`newArrayProto`是一个空对象，：
  
  ![image-20220714110927390](image-20220714110927390.png)

- 定义所有的变异方法：
  
  ```js
  let methods = [
      'push',
      'pop',
      'shift',
      'unshift',
      'reverse',
      'sort',
      'splice'
  ]
  ```

- 遍历`methods`数组，给`newArrayProto`循环添加属性，这一步就是在重写
  
  ```js
  let oldArrayProto = Array.prototype
  
  let newArrayProto = Object.create(oldArrayProto)
  let methods = [
      'push',
      'pop',
      'shift',
      'unshift',
      'reverse',
      'sort',
      'splice'
  ]
  methods.forEach(method => {
      newArrayProto[method] = function (...args) { // 这里重写了数组方法
          return 'a'
      }
  })
  ```
  
  我们现在调用`newArrayProto`身上的方法，返回的都是自定义的`a`
  
  ![image-20220714112458922](image-20220714112458922.png)

- 很明显，在返回之前调用一下原来的方法就可以了
  
  - 这里要注意要，如果不改变`this`的指向，比如调用`push`方法的时候，实际上就是`oldArrayProto`这个原型对象调用了`push`方法，属性会被加到原型对象上面，样例：
    
    ```js
    let oldArrayProto = Array.prototype
    
    let newArrayProto = Object.create(oldArrayProto) 
    
    // 找到所有的变异方法
    let methods = [
        'push',
        'pop',
        'shift',
        'unshift',
        'reverse',
        'sort',
        'splice'
    ]
    
    methods.forEach(method => {
        newArrayProto[method] = function (...args) { 
            // const result = oldArrayProto[method].call(this, ...args) 
            const result = oldArrayProto[method](...args) 
    
            return result
        }
    })
    
    let data1 = ['a']
    data1.__proto__ = newArrayProto
    data1.push('b', 'c')
    
    console.log(data1)
    ```
    
    可以看到，`push`方法全都作用在了`oldArrayProto`身上了，因为方法本身就是定义在它身上的
    
    ![image-20220715091536149](image-20220715091536149.png)
  
  - 需要注意`this`指向问题，谁调的`this`应该就指向谁，所以要使用`call`方法，将`push`方法执行时的上下文，改为`data`本身
    
    ```js
    let oldArrayProto = Array.prototype
    
    let newArrayProto = Object.create(oldArrayProto) 
    
    // 找到所有的变异方法
    let methods = [
        'push',
        'pop',
        'shift',
        'unshift',
        'reverse',
        'sort',
        'splice'
    ]
    
    methods.forEach(method => {
        newArrayProto[method] = function (...args) { 
            const result = oldArrayProto[method].call(this, ...args) 
            // const result = oldArrayProto[method](...args) 
    
            return result
        }
    })
    
    let data1 = ['a']
    data1.__proto__ = newArrayProto
    data1.push('b', 'c')
    
    console.log(data1)
    ```
    
    `push`方法指定了正确的上下文：
    
    ![image-20220715091732694](image-20220715091732694.png)
  
  - 本例如下：
    
    ```js
    methods.forEach(method => {
        // arr.push(1,2,3)
        newArrayProto[method] = function (...args) { // 这里重写了数组方法
            const result = oldArrayProto[method].call(this, ...args) // 内部调用原来的方法，一般称为函数的劫持（切片编程(切面编程)：自己写个功能，把以前的功能塞进去，外面可以做一些自己的事，aop）
            return result
        }
    })
    ```

- 最后导出`newArrayProto`对象，在`observe/index.js`中导入，并将`data`的隐式原型属性指向`newArrayProto`对象

完整示例：

`observe/array.js`

```js
// 我们希望重写数组中的部分方法

let oldArrayProto = Array.prototype

// newArraryProto.__proto = oldArrayProto
export let newArrayProto = Object.create(oldArrayProto) // 以oldArryarProto对象为原型对象，新建一个newArraryProto

// 找到所有的变异方法
let methods = [
    'push',
    'pop',
    'shift',
    'unshift',
    'reverse',
    'sort',
    'splice'
] // concact slice都不会改变原数组

methods.forEach(method => {
    // arr.push(1,2,3)
    newArrayProto[method] = function (...args) { // 这里重写了数组方法
        const result = oldArrayProto[method].call(this, ...args) // 内部调用原来的方法，一般称为函数的劫持（切片编程(切面编程)：自己写个功能，把以前的功能塞进去，外面可以做一些自己的事，aop）
        console.log('method', method) // 供使用时打印
        return result
    }
})
```

`observe.index.js`

```js
import { newArrayProto } from './array'
class Observer {
    constructor(data) {
        if(Array.isArray(data)) {
            // 这里我们可以重写数组的7个变异方法（可以修改数组本身）
            data.__proto__ = newArrayProto
            // this.observeArray(data) // 递归处理数组中的对象
        } else {
            this.walk(data)
        }
    }

    walk(data) { // 循环对象，对属性依此劫持
        // 重新定义属性
        Object.keys(data).forEach(key => defineReactive(data, key, data[key]))
    }
    observeArray(data) {
        data.forEach(item => observe(item))
    }
}

// ...
```

`index.html`测试

```html
  <script src="./vue.js"></script>
  <script>
    const vm = new Vue({
        data() {
            return {
                name: 'sai',
                age: 11,
                address: {
                    street: 'RoadA',
                    room: 123
                },
                hobby: [
                    'eat',
                    'drink',
                    {
                        a: 1
                    }
                ]
            }
        }
    })
    vm.hobby.push('1')
  </script>
```

测试下，用到的是什么方法，就会打印什么方法

但是，如果追加的是一个对象，还会有问题

```html
  <script src="./vue.js"></script>
  <script>
    // ...
      vm.hobby.unshift({a:1})
  </script>
```

ps：记得取消之前的注释

```js
// ...
        if(Array.isArray(data)) {
            data.__proto__ = newArrayProto
            this.observeArray(data) // 取消这里的注释
        } else {
            this.walk(data)
        }
// ...
```

可以看到，虽然`hobby`里面的对象被劫持了，但是数组中新增的对象，并没有被劫持

因为目前我们只是拦截了变异方法，并没有对新增的属性做处理，即要对`rest`参数`args`做处理

![image-20220714140840410](image-20220714140840410.png)

我们劫持了函数之后，也要对新增的数据再次进行劫持

- 拿到`rest`参数（是个数组），根据调用的方法做不同的处理
  - `push`、`unshift`
    - 直接可以用过`rest`参数获取到
  - `splice`
    - 如果是删除操作，`splice`方法是没有第三个参数的，`args`是为

- 根据不同的方法，拿到新增的内容
  
  ```js
  methods.forEach(method => {
      newArrayProto[method] = function (...args) {
          // ...
          // 我们需要对新增的数据，再次进行劫持
          let inserted
          switch (method) {
              case 'push':
              case 'unshift': // arr.unshift(1,2,3)
                  inserted = args
                  break
              case 'splice': // arr.splice(0, 1, {a:1}, {b:2}) 只要第三个参数有值，即是新增了属性
                  inserted = args.slice(2) // [{a:1}, {b:2}]
                  break
              default:
                  break
          }
          console.log('新增的内容', inserted)
          // inserted是一个数组
          return result
      }
  })
  ```

- 对新增的内容，再次进行观测
  
  - `inserted`是一个数组，要对数组进行观测，需要拿到在`Observer`类中定义的`observeArray`方法，但不好直接拿到该方法
  
  - 在`forEach`中，我们只能拿到`this`，指向的是上下文（指向的是调用`push`方法的那个对象），可以打印下`this`，指向的就是`data`，在`index.html`中，调用的形式是`vm.hobby.push(1,2,3)`，也表明了是`data`调用的`push`
    
    - 在`Observer`类的构造函数中，在`data`上，自定义`__ob__`属性，指向`this`：`data.__ob__ = this`，这里的`this`指向的是`Observer`类的实例
    
      ```js
      class Observer {
          constructor(data) {
              data.__ob__ = this // `data`属性上再自定义`__ob__`属性，指向`Ovserver`的实例
              if(Array.isArray(data)) {
                  data.__proto__ = newArrayProto
                  this.observeArray(data)
              } else {
                  this.walk(data)
              }
          }
          // ...
      }
      ```
    
    - 那么在`forEach`中，由于`this`指向的就是`data`，可以通过`this.__ob__`拿到`Observer`的实例，然后调用`observeArray`方法
    
      - 在循环内部，就可以通过`this.__ob__.observeArray`对新增内容进行观测了
      - 这并不是一种设计上的巧妙，是没办法解决了，只能写成这样
    
      ```js
      methods.forEach(method => {
          newArrayProto[method] = function (...args) {
              // ...
              let inserted
              let ob = this.__ob__ // 指向的是Observer类的实例
              switch (method) {
                  case 'push':
                  case 'unshift':
                      inserted = args
                      break
                  case 'splice':
                      inserted = args.slice(2)
                      break
                  default:
                      break
              }
              // inserted是一个数组
              if(inserted) {
                  ob.observeArray(inserted) // 调用监测数组的方法
              }
              return result
          }
      })
      ```
    
    - 同时，另外一个好处是，也给`data`加了一个标识，如果`data`上有`__ob__`，则说明这个属性被观测过，可以借助此完善`observe`函数的判断
    
      `observe/index.js`
    
      ```js
      import { newArrayProto } from './array'
      class Observer {
          constructor(data) {
              data.__ob__ = this
              if(Array.isArray(data)) {
                  data.__proto__ = newArrayProto
                  this.observeArray(data)
              } else {
                  this.walk(data)
              }
          }
      
          walk(data) {
              Object.keys(data).forEach(key => defineReactive(data, key, data[key]))
          }
          observeArray(data) {
              data.forEach(item => observe(item))
          }
      }
      
      export function defineReactive(target, key, value) {
          observe(value) 
          Object.defineProperty(target, key, {
              get() {
                  console.log('key', key)
                  return value
              },
              set(newValue) {
                  if(value == newValue) return
                  value = newValue
              }
          })
      }
      
      export function observe(data) {
      
      // 对data类型进行判断
      if(typeof data !== 'object' || data == null) {
          return // 只对对象进行劫持
      }
      
      // 如要考虑到一个对象已经被劫持的情况
      // 如果一个对象已经被劫持过了，那么就不需要再被劫持
      // 可以添加一个实例，用实例来判断是否被劫持过（应该是用实例身上的属性）
      if(data.__ob__ instanceof Observer) {
          return data.__ob__ // 如果被代理过了，直接返回它的实例
      }
      return new Observer(data)
      
      }
      ```
    
    - 但这样写行不行呢？我们再来测试下，看下页面
    
      ![image-20220714151621487](image-20220714151621487.png)
    
      完犊子了，内存爆了！
    
      咋回事，我们是为了解决`data`是数组的情况，给`data`添加了`__ob__`自定义属性
    
      但是，如果`data`是对象，它会先加一个自定义属性`__ob__`，这是合理的，相当于增加一个标识，这一步没问题，但到了下一步，走`walk`方法，会被`data`身上的`__ob__`属性，也是对象，然后在加一个，再走`walk`，就死循环了
    
      在`data.__ob__ = this`之前打个断点，执行到`walk`时，我们进入内部，看下`data`
    
      ![image-20220714190149824](image-20220714190149824.png)
    
      再继续往下走到`observe`，添加条件断点：`key === __ob__`，不断点下一步，观察右边的调用栈，一直在增加
    
      ![image-20220714191311887](image-20220714191311887.png)
    
      那么怎么处理呢？我们希望在遍历对象的时候，不能遍历到`__ob__`这个属性，让其变成不可枚举的即可。改写原来的写法：
    
       ```js
         class Observer {
             constructor(data) {
                 // data.__ob__ = this
                 // 在data上添加属性的同时，让其变成不可枚举的
                 // 并且这种写法，也没有影响到data位数组的情况
                 Object.defineProperty(data, '__ob__', {
                     value: this,
                     enumerable: false // 将__ob__变成不可枚举（循环的时候无法获取到）
                 })
                 if(Array.isArray(data)) {
                     data.__proto__ = newArrayProto
                     this.observeArray(data)
                 } else {
                     this.walk(data)
                 }
             }
             // ...
         }
       ```
  
- 此时我们再测试一下
  
  `index.html`
  
  ```html
    <script src="./vue.js"></script>
    <script>
      const vm = new Vue({
          data() {
              return {
                  name: 'sai',
                  age: 11,
                  address: {
                      street: 'RoadA',
                      room: 123
                  },
                  hobby: [
                      'eat',
                      'drink',
                      {
                          a: 1
                      }
                  ]
              }
          }
      })
      vm.hobby.unshift({a:1})
      console.log(vm.hobby)
    </script>
  ```
  
  数组里有四项，通过数组方法新增的对象，也有了`get`和`set`
  
  ![image-20220714192439428](image-20220714192439428.png)

至此，数组的劫持，全部搞定

- 数组劫持核心，就是重写数组的方法，并且去观测数组中的每一项
  - 如果是数组的话，需要对每一项新增的属性，做一下判断，并且把数组的每一项，再进行观测

接下来就要和视图挂钩了

### 模板编译原理

当初我们需要写一个`div`并指定`id`，在里面写小胡子语法

`index.html`

```html
<body>
  <!-- 模板 -->
  <div id="app">
  	<div>
    	{{name}}    
    </div>
    <span>{{age}}</span>
  </div>

  <script src="./vue.js"></script>
  <script>
    const vm = new Vue({
        data() {
            return {
                name: 'sai',
                age: 11
            }
        }
    })
  </script>
</body>
```

我们要对这个模板进行编译，需要给配置对象，传一个`el`属性，将数据解析到`el`元素上，将`{{name}}`和`{{age}}`进行一个数据的替换

- 方案一：模板引擎
  - 每次把模板拿到，用数据来替换
  - 性能很差，需要正则匹配替换（`vue1.0`的时候，没有引入虚拟`dom`）
- 方案二：采用虚拟`dom`
  - 数据变化后，比较虚拟`dom`的差异，最后更新需要更新的地方
  - 核心就是，把模板变成`js`语法，可以通过`js`语法生成虚拟`dom`
    - 从一个东西，变成另一个东西（语法之间的转换），这是一个很典型的**语法转译**问题，如`es6 => es5`，需要先变成语法树，再重新组装代码，成为新的语法

现在我们要拿到模板

```html
<body>
  <div id="app">
  	<div>
    	{{name}}    
    </div>
    <span>{{age}}</span>
  </div>
    
  <script src="./vue.js"></script>
  <script>
    const vm = new Vue({
        data() {
            return {
                name: 'sai',
                age: 11
            }
        },
        el: "#app" // 将数据解析到el元素上
    })
  </script>
</body>
```

模板除了可以写在`el`上，也可以写在`template`上

```html
  <script src="./vue.js"></script>
  <script>
    const vm = new Vue({
        template: ``
    })
  </script>
```

或者可以用一个方法来替代：`render()`

```html
  <script src="./vue.js"></script>
  <script>
    const vm = new Vue({
        render() {
            return h('div', {})
        }
    })
  </script>
```

而我们**最终的目标**就是，把`template`语法变成`render()`函数

#### 将模板转换成`ast`语法树

状态初试完完了，就去看用户，有没有给`el`属性

- 先看配置项，有没有`el`属性

  - 如果有，`vm`原型对象上定义`$mount`函数，将`options.el`传入`$mount`方法，并实现数据的挂载
    - 有了`$mount`方法后，我们也可以不写`el`配置项，直接调用`vm.$mount("#app")`实现手动挂载

- `$mount`的功能

  - 先找到对应的元素：

    ```js
        Vue.prototype.$mount = function (el) {
            const vm = this
            el = document.querySelector(el)
        }
    ```

    返回`el`对应的`dom`元素

  - 根据配置项的进行进行不同的处理

    - 判断是否有`render`函数
      - 如果没有
        - 判断是否有`template`配置项
          - 如果没有`template`配置项，但是有`el`配置项
            - 使用`el.outerHTML`拿到模板
          - 如果有`template`配置项，就用`template`配置项

    `init.js`

    ```js
    import {initState} from "./state";
    
    export function initMixin(Vue) {
        Vue.prototype._init = function(options) {
            const vm = this
            vm.$options = $options
            initState(vm)
    
            if(options.el) { // 看是否有el配置项
                vm.$mount(options.el) // 实现数据的挂载
            }
        }
    
        Vue.prototype.$mount = function (el) {
            const vm = this
            el = document.querySelector(el)
            let ops = vm.$options
            if(!ops.render) { // 先查找render函数
                let template
                if(!ops.template && el) { // 没有template配置项，但是有el配置项
                    let template = el.outerHTML // 就用el的配置项，outHTML返回的是匹配到自身的dom元素
                } else { // 如果既有template,又有el，就用template配置项作为模板
                    if(el) {
                        template = ops.template
                    }
                }
                // 其他情况的分支考虑
                console.log(template)
            }
        }
    }
    
    
    ```

这里其他分支的细节代码就不写了，如都没有的情况应该怎么处理等

挂载`el`配置项：

`index.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport"
        content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
    <div>
        <div id="app">
            {{name}}
            {{age}}
        </div>
    </div>
<script src="./vue.js"></script>
<script>
    const vm = new Vue({
        el: '#app',
        data() {
            return {
                name: 'sai',
                age: 11,
                address: {
                    street: 'RoadA',
                    room: 123
                },
                hobby: [
                    'eat',
                    'drink',
                    {
                        a: 1
                    }
                ]
            }
        }
    })
</script>
</body>
</html>
```

结果：

![image-20221122072027640](image-20221122072027640.png)

这里可以多试试不同的情况

整体逻辑是：先找`render`函数，没写的话就找`template`配置项，再没写的话，就用外部的`html`



最终获取到`template`后，将`template`传入到自定义函数`compileToFunction`中进行渲染

`init.js`

```js
Vue.prototype.$mount = function (el) {
        const vm = this
        el = document.querySelector(el)
        let ops = vm.$options

        if(!ops.render) { // 先查找render函数
            let template
            if(!ops.template && el) { // 没有template配置项，但是有el配置项
                template = el.outerHTML // 就用el的配置项，outHTML返回的是匹配到自身的dom元素
            } else { // // 如果既有template,又有el，就用template配置项作为模板
                if(el) {
                    template = ops.template
                }
            }
            // 其他情况的分支考虑
            // console.log(template)
            // 最终如果获取到模板
            if(template) {
                // 这里需要对模板进行编译
                const render = compileToFunction(template)
                // 将编译后的结果给render函数
                ops.render = render
            }
        }
        ops.render // 有render就直接调用render
    }
```

实际开发中可以写`jsx`，它是依赖`babel`做了编译（`vue`中有对应的`jsx-plugin`插件），如果写`jsx`相当于多了一层：将`jsx`转换成`render`函数返回的`h`方法

- `script`标签引用的`vue.global.js`，这个编译过程是在浏览器运行的
- `runtime`是不包含模板编译的，整个编译打包的时候，是通过`loader`来转义`.vue`文件中的`<template></template>`
  - 只有`runtime`是不能写`template`配置项的



新建`src/compiler/index.js`，表示编译模板

`index.js`

```js
// 对模板进行编译处理
export function compileToFunction(template) {
    // 1.将template转化成ast抽象语法树

    // 2.生成render方法（返回的结果，就是虚拟dom）
    console.log(template)
    // 有了虚拟dom之后，再渲染成真实dom

}
```

`init.js`中导入

```js
import {compileToFunction} from "./compiler" // 使用@rollup/plugin-node-resolve插件，可省略index.js

// ...
```

如果想自动导入index文件，可以安装插件，`rollup`环境下安装：`npm i @rollup/plugin-node-resolve`

详细使用方式：[@rollup/plugin-node-resolve - npm (npmjs.com)](https://www.npmjs.com/package/@rollup/plugin-node-resolve)

样例：

```js
import { nodeResolve } from '@rollup/plugin-node-resolve';

export default {
  input: 'src/index.js',
  output: {
    dir: 'output',
    format: 'cjs'
  },
  plugins: [nodeResolve()]
};
```

`rollup.config.js`

```js
// rollup 默认可以导出一个对象，作为打包的配置文件
import { nodeResolve } from '@rollup/plugin-node-resolve';
import babel from  '@rollup/plugin-babel'

export default {
    input: './src/index.js', // 入口
    output: {
        file: './dist/vue.js', // 出口
        name: 'Vue', // 在global全局上，增添一个Vue对象，我们就可以new Vue了（global.Vue）
        format: 'umd', // options: 1.esm es6模块，相当于没有打包了 2.commonjs node中使用 3.iife 自执行函数 4.umd 兼容amd和commonjs
        sourcemap: true // 可以调试源代码
    },
    plugins: [
        // 需要新建babel的配置文件，既可以是js文件，也可以是.rc文件,
        // 这里和视频的保持一致
        babel({
            exclude: 'node_modules/**', // 排除第三方模块 ，**表示任意文件夹
            babelHelpers: 'bundled' // https://www.npmjs.com/package/@rollup/plugin-babel  搜索babelHelpers，不加这一行会有报错
        }), // 所有的插件都是函数
        nodeResolve()
    ]
}
```

#### 代码生成，实现虚拟`DOM`

上一节回顾：

- 把模板转换成`ast`语法树，再将`ast`语法树转换成`render`函数

对于标签而言，内容有标签名、表达式、文本、属性

```html
    <div id='app'>
        <div style='color:red' class='container'>
            {{ name }} hello world 
        </div>
        <span>
            {{ age }}
        </span>
    </div>
```

我们拿到这样的字符串文本后，需要开始解析

怎么解析呢？

要有能够匹配标签、表达式、文本、属性的能力

先来看一些正则：

`compiler/index.js`

```js
const ncname = `[a-zA-Z_][\\-\\.0-9_a-zA-Z]*` // 匹配标签名
const qnameCapture = `((?:${ncname}\\:)?${ncname})`
const startTagOpen = new RegExp(`^<${qnameCapture}`)
const endTag = new RegExp(`^<\\/${qnameCapture}[^>]*>`)
const attribute =  /^\s*([^\s"'<>\/=]+)(?:\s*(=)\s*(?:"([^"]*)"+|'([^'])'+|([^\s"'=<>`]+)))?/
const startTagClose = /^\s*(\/?)>/
const defaultTagRE = /\{\{((?:.|\r?\n)+?)\}\}/g

console.log(startTagOpen)
// 对模板进行编译处理
export function compileToFunction(template) {
    // 1.将template转化成ast抽象语法树

    // 2.生成render方法（返回的结果，就是虚拟dom）
    console.log(template)

}
```

先打印下`startTagOpen`

```js
/^<((?:[a-zA-Z_][\-\.0-9_a-zA-Z]*\:)?[a-zA-Z_][\-\.0-9_a-zA-Z]*)/
```

用可视化工具看一下，[Regexper](https://regexper.com/)

![image-20221122205447489](image-20221122205447489.png)

```html
<div>
<div:xxx> 带命名空间的标签
<_div> 自定义标签

```

`startTagOpen`匹配到的分组，是一个开始标签名



看下`endTag`

```js
/^<\/((?:[a-zA-Z_][\-\.0-9_a-zA-Z]*\:)?[a-zA-Z_][\-\.0-9_a-zA-Z]*)[^>]*>/
```

![image-20221122210031249](image-20221122210031249.png)

`Oneof`表示`任一一个`，`Noneof`表示`除了这些`，箭头表示`可跳过`

`endTag`匹配到的分组，是结束标签名



看下属性

```js
/^\s*([^\s"'<>\/=]+)(?:\s*(=)\s*(?:"([^"]*)"+|'([^']*)'+|([^\s"'=<>`]+)))?/
```

![image-20221122210514120](image-20221122210514120.png)

```
color   =  'a'
color = "a"
color=a
disabled
```

属性中的`key`是第一个分组，`value`是第三或者第四或者第五个分组



看下`startTagClose`

```js
/^\s*(\/?)>/
```

![image-20221122211350057](image-20221122211350057.png)

表示闭合标签



看下`defaultTagRE`

```js
/\{\{((?:.|\r?\n)+?)\}\}/g
```

![image-20221122211528510](image-20221122211528510.png)

表示小胡子语法对应的表达式变量



备注：`vue3`中的这一步不是用的正则，是一个一个字符来判读，如是不是`/`，是不是`<`之类来解析的，其实效果也是一样的



那么接下来怎么去解析模板呢

- 每解析一个标签，就把它从字符串中删除掉

`index.js`

```js
function parsetHTML(html) {// 每解析一个标签，就把它从字符串中删除掉
    function parseStartTag() {
        const start = html.match(startTagOpen) // 是一个数组
        console.log(start)
    }

    while(html) {
        // vue2中，html最开始一定是一个< 
        // 如果textEnd为0，说明是一个开始标签或者结束标签
        // 如果textEnd>0，说明就是文本的结束位置
        let textEnd = html.indexOf('<') // 如果索引为0，则说明是个标签，开始标签取完了，再去取尖角号，取到的是文本结束的位置
        if(textEnd == 0) {
            parseStartTag()
            break
        }
    }
}
// 对模板进行编译处理
export function compileToFunction(template) {
    // 1.将template转化成ast抽象语法树
    let ast = parsetHTML(template)
    // 2.生成render方法（返回的结果，就是虚拟dom）
    console.log(template)

}
```

`start`打印结果：

![image-20221122214247328](image-20221122214247328.png)

```js
function parsetHTML(html) {// 每解析一个标签，就把它从字符串中删除掉
    function advance(n) { // 截取
        html = html.substring(n)
    }

    function parseStartTag() {
        const start = html.match(startTagOpen) // 结果是一个数组
        console.log(start)
        if(start) {
            // 匹配到了，把结果（数组）组成一个对象
            const match = {
                tagName: start[1], // 标签名
                attrs: []
            }
            advance(start[0].length) // 根据匹配到的字符的长度，进行删除
            console.log(match)
            console.log(html)
        }
        return false // 不是开始标签，返回false
    }

    while(html) {
        // vue2中，html最开始一定是一个< 
        // 如果textEnd为0，说明是一个开始标签或者结束标签
        // 如果textEnd>0，说明就是文本的结束位置
        let textEnd = html.indexOf('<') // 如果索引为0，则说明是个标签，开始标签取完了，再去取尖角号，取到的是文本结束的位置
        if(textEnd == 0) {
            parseStartTag()
            break
        }
    }
}
// 对模板进行编译处理
export function compileToFunction(template) {
    // 1.将template转化成ast抽象语法树
    let ast = parsetHTML(template)
    // 2.生成render方法（返回的结果，就是虚拟dom）
    console.log(template)
}
```

![image-20221122215009131](image-20221122215009131.png)



开始标签匹配完了，接下来开始匹配属性

匹配过程中，只要它不是开始标签的结束，就一直匹配

```js
function parsetHTML(html) {// 每解析一个标签，就把它从字符串中删除掉
    function advance(n) { // 截取
        html = html.substring(n)
    }

    function parseStartTag() {
        const start = html.match(startTagOpen) // 结果是一个数组
        console.log(start)
        if(start) {
            // 匹配到了，把结果（数组）组成一个对象
            const match = {
                tagName: start[1], // 标签名
                attrs: []
            }
            advance(start[0].length) // 根据匹配到的字符的长度，进行删除
            // console.log(match)
            // console.log(html)
        }
        let attr
        while(!html.match(startTagClose) && (attr = html.match(attribute))) { // 如果不是开始标签的结束，就一直匹配，并且每次匹配都把匹配到的结果存起来
            advance(attr[0].length) // 每次匹配完，再把匹配过的字符去掉

        }
        console.log(html)
        return false // 不是开始标签，返回false
    }

    while(html) {
        // vue2中，html最开始一定是一个< 
        // 如果textEnd为0，说明是一个开始标签或者结束标签
        // 如果textEnd>0，说明就是文本的结束位置
        let textEnd = html.indexOf('<') // 如果索引为0，则说明是个标签，开始标签取完了，再去取尖角号，取到的是文本结束的位置
        if(textEnd == 0) {
            parseStartTag()
            break
        }
    }
}
```

匹配处理属性的结果：

![image-20221122215755848](image-20221122215755848.png)

还剩一个`>`尖角号，也需要处理（把处理方法的逻辑，放在条件判断里更合理些）

```js
 function parseStartTag() {
        const start = html.match(startTagOpen) // 结果是一个数组
        console.log(start)
        if(start) {
            // 匹配到了，把结果（数组）组成一个对象
            const match = {
                tagName: start[1], // 标签名
                attrs: []
            }
            advance(start[0].length) // 根据匹配到的字符的长度，进行删除
            // console.log(match)
            // console.log(html)
            let attr, end
            while(!(end = html.match(startTagClose)) && (attr = html.match(attribute))) { // 如果不是开始标签的结束，就一直匹配，并且每次匹配都把匹配到的结果存起来
                advance(attr[0].length) // 每次匹配完，再把匹配过的字符去掉
            }
            if(end) {
                // 如果匹配到了end，也应该删除
                advance(end[0].length)
            }
        }
        
        console.log(html)
        return false // 不是开始标签，返回false
    }
```

`>`尖角号也处理完了

![image-20221122220021712](image-20221122220021712.png)

我们需要开始标签中的属性，解析出来，并放在attrs数组中

```js
if(start) {
            // 匹配到了，把结果（数组）组成一个对象
            const match = {
                tagName: start[1], // 标签名
                attrs: []
            }
            advance(start[0].length) // 根据匹配到的字符的长度，进行删除
            // console.log(match)
            // console.log(html)
            let attr, end
            while(!(end = html.match(startTagClose)) && (attr = html.match(attribute))) { // 如果不是开始标签的结束，就一直匹配，并且每次匹配都把匹配到的结果存起来
                advance(attr[0].length) // 每次匹配完，再把匹配过的字符去掉
                match.attrs.push(
                    {
                        name:attr[1], 
                        value: attr[3] || attr[4] || attr[5] || true
                    }
                )
            }
            console.log(match)

            if(end) {
                // 如果匹配到了end，也应该删除
                advance(end[0].length)
            }
            return match
        }
```

![image-20181111100049281](image-20181111100049281.png)

第一个开始标签解析完成，继续向下解析文本内容

```js
while(html) {
        // vue2中，html最开始一定是一个< 
        // 如果textEnd为0，说明是一个开始标签或者结束标签
        // 如果textEnd>0，说明就是文本的结束位置
        let textEnd = html.indexOf('<') // 如果索引为0，则说明是个标签，开始标签取完了，再去取尖角号，取到的是文本结束的位置
        if(textEnd == 0) { 
            const startTagMatch = parseStartTag() // 开始标签的匹配结果
            if(startTagMatch) { // 解析到的开始标签
                continue
                console.log(html) // 截取完之后，可能还是开始标签
            }
            // break
        }
        if(textEnd >= 0) { // 解析到的文本
            let text = html.substring(0, textEnd) // 文本内容
            if(text) {
                advance(text.length)
                console.log(html)
            }
            break
        }
    }
```

结果：

![image-20221123085745451](image-20221123085745451.png)

该标签前面的空格内容被截取掉了



继续解析结束标签

```js
while(html) {
        // vue2中，html最开始一定是一个< 
        // 如果textEnd为0，说明是一个开始标签或者结束标签
        // 如果textEnd>0，说明就是文本的结束位置
        let textEnd = html.indexOf('<') // 如果索引为0，则说明是个标签，开始标签取完了，再去取尖角号，取到的是文本结束的位置
        if(textEnd == 0) { 
            const startTagMatch = parseStartTag() // 开始标签的匹配结果
            if(startTagMatch) { // 解析到的开始标签
                continue
                console.log(html) // 截取完之后，可能还是开始标签
            }
            //如果不是开始标签，那么就是结束标签
            let endTagMatch = html.match(endTag)
            if(endTagMatch) {
                advance(endTagMatch[0].length)
                continue
            }
        }
        if(textEnd >= 0) { // 解析到的文本
            let text = html.substring(0, textEnd) // 文本内容
            if(text) {
                advance(text.length)
            }
        }
    }
    console.log(html)
```

如果打印为空，说明`while`循环写的没问题



我们在`while`内部打个断点，看看整个流程

着重看每次循环的`html`变量以及进入的是哪个分支



如果是类似`<br />`这样的自闭合标签呢？

![image-20221123162047816](image-20221123162047816.png)

这里先留个坑，处理的时候直接就去掉了

我们在调用解析方法前，打印下获取到的`template`

![image-20221123162236809](image-20221123162236809.png)

获取到的`template`中的自闭合标签已经没有了



上面的处理，只是把字符串删除了，并没有替换文本

我们希望把文本稍作处理，需要写几个方法把各自匹配的内容，暴露出去，让外面来处理

```js
function parsetHTML(html) {
    function start(tag, attrs) {
        console.log('开始标签', tag, attrs)
    }

    function chars(text) {
        console.log('文本', text)
    }

    function end(tag) {
        console.log('结束标签', tag)
    }
    
    // ...
    while(html) {

        let textEnd = html.indexOf('<')
        if(textEnd == 0) { 
            const startTagMatch = parseStartTag()
            if(startTagMatch) {
                start(startTagMatch.tagName, startTagMatch.attrs) // 把匹配到的开始标签的内容，传出去
                continue
            }

            let endTagMatch = html.match(endTag)
            if(endTagMatch) {
                advance(endTagMatch[0].length)
                end(endTagMatch[1]) // 把匹配到的结束标签，传出去

                continue
            }
        }
        if(textEnd >= 0) {
            let text = html.substring(0, textEnd)
            if(text) {
                char(text) // 把匹配到的文本，传出去
                advance(text.length)
            }
        }
    }
    
}
```



#### 通过虚拟`DOM`生成真实`DOM`





























































































# 教程二

地址：[blog/精通 Vue 技术栈的源码原理 at main · liyongning/blog (github.com)](https://github.com/liyongning/blog/tree/main/精通 Vue 技术栈的源码原理)

## 搭建vue开发环境

### 下载及安装配置

下载链接：https://github.com/vuejs/vue

下载后，执行`npm i`安装依赖

修改`package.json`如下依赖，`scripts` 中的 `dev` 命令中添加 `--sourcemap`，这样就可以在浏览器中调试源代码时，查看当前代码在源代码中的位置：

```json
{
  "scripts": {
    "dev": "rollup -w -c scripts/config.js --sourcemap --environment TARGET:web-full-dev"
  }
}
```

### 概念扫盲

`npm run build`后的打包文件：

|                               | UMD                | CommonJS                   | ES Module          |
| ----------------------------- | ------------------ | -------------------------- | ------------------ |
| **Full**                      | vue.js             | vue.common.js              | vue.esm.js         |
| **Runtime-only**              | vue.runtime.js     | vue.runtime.common.js      | vue.runtime.esm.js |
| **Full (production)**         | vue.min.js         | vue.common.prod.js         |                    |
| **Runtime-only (production)** | vue.runtime.min.js | vue.runtime.common.prod.js |                    |

- **Full**：这是一个全量的包，包含编译器（`compiler`）和运行时（`runtime`）。
- **Compiler**：编译器，负责将模版字符串（即你编写的类 html 语法的模版代码）编译为 JavaScript 语法的 render 函数。
- **Runtime**：负责创建 Vue 实例、渲染函数、patch 虚拟 DOM 等代码，基本上除了编译器之外的代码都属于运行时代码。
- **UMD**：兼容 CommonJS 和 AMD 规范，通过 CDN 引入的 vue.js 就是 UMD 规范的代码，包含编译器和运行时。
- **CommonJS**：典型的应用比如 nodeJS，CommonsJS 规范的包是为了给 browserify 和 webpack 1 这样旧的打包器使用的。他们默认的入口文件为 `vue.runtime.common.js`。
- **ES Module**：现代 JavaScript 规范，ES Module 规范的包是给像 webpack 2 和 rollup 这样的现代打包器使用的。这些打包器默认使用仅包含运行时的 `vue.runtime.esm.js` 文件。

**运行时（Runtime）+ 编译器（Compiler） vs. 只包含运行时（Runtime-only）**

如果你需要动态编译模版（比如：将字符串模版传递给 `template` 选项，或者通过提供一个挂载元素的方式编写 html 模版），你将需要编译器，因此需要一个完整的构建包。

当你使用 `vue-loader` 或者 `vueify` 时，`*.vue` 文件中的模版在构建时会被编译为 `JavaScript` 的渲染函数。因此你不需要包含编译器的全量包，只需使用只包含运行时的包即可。

只包含运行时的包体积要比全量包的体积小 30%。因此尽量使用只包含运行时的包，如果你需要使用全量包，那么你需要进行如下配置：

**webpack**

```javascript
module.exports = {
  // ...
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    }
  }
}
```

**Rollup**

```javascript
const alias = require('rollup-plugin-alias')

rollup({
  // ...
  plugins: [
    alias({
      'vue': 'vue/dist/vue.esm.js'
    })
  ]
})
```

**Browserify**

Add to your project's `package.json`:

```json
{
  // ...
  "browser": {
    "vue": "vue/dist/vue.common.js"
  }
}
```

### 目录结构

```
├── benchmarks                  性能、基准测试
├── dist                        构建打包的输出目录
├── examples                    案例目录
├── flow                        flow 语法的类型声明
├── packages                    一些额外的包，比如：负责服务端渲染的包 vue-server-renderer、配合 vue-loader 使用的的 vue-template-compiler，还有 weex 相关的
│   ├── vue-server-renderer
│   ├── vue-template-compiler
│   ├── weex-template-compiler
│   └── weex-vue-framework
├── scripts                     所有的配置文件的存放位置，比如 rollup 的配置文件
├── src                         vue 源码目录
│   ├── compiler                编译器
│   ├── core                    运行时的核心包
│   │   ├── components          全局组件，比如 keep-alive
│   │   ├── config.js           一些默认配置项
│   │   ├── global-api          全局 API，比如熟悉的：Vue.use()、Vue.component() 等
│   │   ├── instance            Vue 实例相关的，比如 Vue 构造函数就在这个目录下
│   │   ├── observer            响应式原理
│   │   ├── util                工具方法
│   │   └── vdom                虚拟 DOM 相关，比如熟悉的 patch 算法就在这儿
│   ├── platforms               平台相关的编译器代码
│   │   ├── web
│   │   └── weex
│   ├── server                  服务端渲染相关
├── test                        测试目录
├── types                       TS 类型声明
```

## Vue初始化过程

### 目标

深入理解 Vue 的初始化过程，再也不怕 面试官 的那道面试题：`new Vue(options) `发生了什么？

### 找入口

想知道 `new Vue(options)` 都做了什么，就得先找到 Vue 的构造函数是在哪声明的，有两个办法：

- 从 rollup 配置文件中找到编译的入口，然后一步步找到 Vue 构造函数，这种方式 **费劲**
- 通过编写示例代码，然后打断点的方式，一步到位，**简单**

我们就采用第二种方式，写示例，打断点，一步到位。

- 在 `/examples` 目录下增加一个示例文件 —— `test.html`，在文件中添加如下内容：
  
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Vue 源码解读</title>
  </head>
  <body>
    <div id="app">
      {{ msg }}
    </div>
    <script src="../dist/vue.js"></script>
    <script>
      debugger
      new Vue({
        el: '#app',
        data: {
          msg: 'hello vue'
        }
      })
    </script>
  </body>
  </html>
  ```

- 在浏览器中打开控制台，然后打开 `test.html`，则会进入断点调试，然后找到 Vue 构造函数所在的文件
