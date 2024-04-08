---
title: 'Promise的使用与实现'
date: 2022-8-8 07:15:24
cover: false
toc_number: false
tags:
- javascript
categories: 'javascript'
typora-root-url: Promise
---
[TOC]

> 引言：
>
> Promise是ES6引入进行异步编程的新的解决方案，从语法上来说，就是一个构造函数，可以封装异步的任务，并且可以对结果进行处理。
>
> Promise最大的好处在于可以解决回调地狱的问题，并且在指定回调和错误处理方面，更加的灵活与方便。
>
> 链接：https://www.bilibili.com/video/BV1GA411x7z1
>
> 宏队列微队列部分：https://www.bilibili.com/video/BV1MJ41197Eu?p=36

**课程大纲**

- 1.`Promise`介绍和基本使用
- 2.`Promise API` 
- 3.`Promise`关键问题
- 4.`Promise`自定义封装
- 5.`async`与`await`

# 0.前置知识

## 0.1.区别实例对象和函数对象

- 实例对象

  - `new`函数产生的对象，称为实例对象， 简称对象

- 函数对象

  - 将函数作为对象使用时，简称函数对象（都是`Object`函数的实例对象）

- 先看懂语法，再看懂功能

  - 每个变量是什么数据类型
  - 返回的是什么数据类型
  - 括号的左边必然是函数，点的左边必然是对象

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
  </head>
  <body>
      <script>
          function Fn() { // Fn是函数
  
          }
          const fn = new Fn() // Fn是构造函数，fn是实例对象（简称对象）
          console.log(Fn.prototype) // Fn是函数对象
          Fn.bind({}) // Fn是函数对象
          $('#test') // JQuery函数
          $.get('/test') // JQuery函数对象
      </script>
  </body>
  </html>
  ```

  

## 0.2.两种类型的回调

- 同步回调

  - 立即执行，完全执行完了才结束，不会放入回调队列中

  - 例子：

    - 数组遍历相关的回调函数

      ```js
      const arr = [1, 3, 5]
      arr.forEach(item => {
          console.log(item) // 遍历的回调函数，是同步回调，不会放入队列，一上来就会执行
      })
      console.log('forEach()之后')
      ```

      ![image-20220510062654337](image-20220510062654337.png)

    - `Promise`的`executor`函数

- 异步回调

  - 不会立即执行，会放入回调队列中将来执行

  - 例子

    ```js
    setTimeout(() => {
        console.log('timeout callback()') // 异步回调函数，会放入队列中将来执行
    })
    console.log('setTimeout()之后')
    ```

    ![image-20220510062935873](image-20220510062935873.png)

- 如何判断是异步还是同步的呢？

  - 打印看一下输出顺序



拓展：[10张图让你彻底理解回调函数 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/326902537)

## 0.3.`JS`中`error`的处理

[Error - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)

- 错误类型

  - `Error`：所有错误的父类型

  - `ReferenceError`：引用的变量不存在

    ```js
    console.log(a) // 如果没有捕获异常，下面的代码是不会执行的
    console.log('-----')
    ```

    ![image-20220510063543381](image-20220510063543381.png)

  - `TypeError`：数据类型不正确的错误

    ```js
    let b = null
    console.log(b.xxx) // 想要读属性，点的左边应该是一个对象
    
    b.xxx() // 也是类型错误
    ```

    ![image-20220510085053940](image-20220510085053940.png)

  - `RangeError`：数据值不在其允许的范围内

    ```js
    function fn() {
        fn()
    }
    
    fn()
    
    ```

    ![image-20220510085359635](image-20220510085359635.png)

  - `SyntaxError`：语法错误

    ```js
    const c = """"
    ```

    ![image-20220510085459538](image-20220510085459538.png)

- 错误处理（如果不处理，程序就无法向下执行）

  - 捕获错误：`try...catch`

    ```js
    try {
        let d
        console.log(d.xxx)
    } catch(error) {
        console.log(error)
        console.log(error.message)
        console.log(error.stack)
    }
    console.log('出错之后')
    ```

    ![image-20220510090339611](image-20220510090339611.png)

    打断点查看`error`对象

    ![image-20220510090526693](image-20220510090526693.png)

  - 抛出错误：`throw error`

    ```js
    function doSomething() {
        if(Date.now() % 2 === 1) {
            console.log('当前日期为奇数，可以执行任务')
        } else {
            throw new Error('当前日期为偶数，无法执行')
        }
    }
    
    try {
        doSomething()
    } catch (error) {
        alert(error.message)
    }
    ```

    

- 错误对象

  - `message`属性：错误相关信息
  - `stack`属性：函数调用记录栈记录信息

# 1.`Promise`初体验

index.html

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<div class="container">
			<h2 class="page-header">Promise初体验</h2>
			<button class="btn btn-primary" id="btn">点击抽奖</button>
		</div>
		<script>
			// 生成随机数
			function rand(m, n) {
				return Math.ceil(Math.random() * (n - m + 1)) + m - 1
			}

			//    点击按钮，1s后显示是否中奖（30%概率中奖）
			//      若中奖，弹出：恭喜恭喜，奖品为10万RMB劳斯莱斯优惠券
			//      若未中奖，弹出：再接再厉

			// 获取元素对象
			const btn = document.querySelector('#btn')
			// 绑定单击事件
			btn.addEventListener('click', function() {
				//定时器
				setTimeout(() => {
					// 30%概率怎么实现
					// 1-100中，小于等于30
					// 获取1-100的一个随机数
					let n = rand(1, 100)
					// 判断
					if(n <= 30) {
						alert('恭喜恭喜，奖品为10万RMB劳斯莱斯优惠券')
					} else {
						alert('再接再厉')
					}
				},1000)
			})
		</script>
	</body>
</html>

```

## 1.1.`Promise`封装异步操作

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<div class="container">
			<h2 class="page-header">Promise初体验</h2>
			<button class="btn btn-primary" id="btn">点击抽奖</button>
		</div>
		<script>
			// 生成随机数
			function rand(m, n) {
				return Math.ceil(Math.random() * (n - m + 1)) + m - 1
			}

			//    点击按钮，1s后显示是否中奖（30%概率中奖）
			//      若中奖，弹出：恭喜恭喜，奖品为10万RMB劳斯莱斯优惠券
			//      若未中奖，弹出：再接再厉

			// 获取元素对象
			const btn = document.querySelector('#btn')
			// 绑定单击事件
			btn.addEventListener('click', function() {
				
				//定时器
				// setTimeout(() => {
				// 	// 30%概率怎么实现
				// 	// 1-100中，小于等于30
				// 	// 获取1-100的一个随机数
				// 	let n = rand(1, 100)
				// 	// 判断
				// 	if(n <= 30) {
				// 		alert('恭喜恭喜，奖品为10万RMB劳斯莱斯优惠券')
				// 	} else {
				// 		alert('再接再厉')
				// 	}
				// },1000)
				
			   
			    // Promise实现
				const p = new Promise((resolve, reject) => {
					setTimeout(() => {
						let n = rand(1, 100)
						if(n <= 30) {
							// 实际业务逻辑是，当 n <= 30时，为成功状态
							resolve() // 异步任务成功状态下，调用resolve()函数，并将p对象的状态，设置为成功
						} else {
							// 失败状态
							reject()
						}
					},1000)
				})
				console.log(p)
				p.then(() => {
					// p对象的状态为成功时，执行第一个参数作为回调函数
					alert('恭喜恭喜，奖品为10万RMB劳斯莱斯优惠券')
				}, () => {
					// p对象的状态为失败时，执行第二个参数作为回调函数
					alert('再接再厉')
				})
					
			})
		</script>
	</body>
</html>

```

如下图框选的`[[PromiseState]]`，表示的就是`Promise`对象`p`的`状态`，该状态会传递给`then`方法，不同的状态会传递给`then`方法不同的形参

![image-20220506144353326](image-20220506144353326.png)

## 1.2.获取成功/失败的结果值

**新需求：打印输出中奖的数字**

`Promise`对象用来封装一个异步操作，并可以获取其成功/失败的结果值

在实例化Promise时，封装的异步操作里面，任何定义的变量，都可以当作时结果值，传递给`resolve`和`reject`

我们可以将`n`看作是结果值，传递给`resolve`和`reject`

```js
if(n <= 30) { // 将 n <= 30 认为是成功的状态
    resolve(n)  // 将n认为是结果值
} else {
    reject(n)
}
```

对象`p`可以拿到处理成功/失败的结果，作为参数传递给`then`方法对应的成功/失败的回调函数，默认`then`方法两个回调函数的参数分别是`value`和`reason`，写成`a`和`b`也行

```js
p.then((value) => {
    alert(`恭喜恭喜，奖品为10万RMB劳斯莱斯优惠券，您的中奖数字为${value}`)
}, (reason) => {
    alert(`再接再厉，您的号码为${reason}`)
})
```

如下图框选的`[[PromiseResult]]`，表示的就是`Promise`对象`p`获取到异步操作的`结果值`，该结果值根据`状态`的不同，传递给`then`方法不同的形参

![image-20220506150130082](image-20220506150130082.png)

## 1.3.`Promise`练习

### 1.3.1.`fs`读取文件

回调函数形式

```js
const fs = require('fs')

// 回调函数形式
fs.readFile('./resource/context.txt1', (err, data) => {
	if(err) throw err
	console.log(data.toString())
})
```

Promise形式

```js
const fs = require('fs')

// Promise形式
const p = new Promise((resolve, reject) => {
	fs.readFile('./resouce/context.txt1', (err, data) => {
		if(err) reject(err)
		resolve(data)
	})
})

console.log(p)

p.then((value) => {
	console.log(value.toString())
}, (reason) => {
	console.log(reason)
})
```

### 1.3.2.`AJAX`请求

原生AJAX请求

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<div class="container">
			<h2 class="page-header">Promise封装AJAX操作</h2>
			<button class="btn btn-primary" id="btn">点击发送AJAX</button>
		</div>
		<script>
		// 接口地址：http://1.13.245.78/search/hitokoto
		const btn = document.querySelector("#btn")
		btn.addEventListener('click', function() {
			// 1.创建对象
			const xhr = new XMLHttpRequest()
			// 2.初始化
			xhr.open('GET', 'http://1.13.245.78/search/hitokoto')
			// 3.发送
			xhr.send()
			// 4.绑定事件，处理响应结果
			xhr.onreadystatechange = function() {
				if(xhr.readyState === 4) {
					// 判断响应状态码 2xx 为成功
					if(xhr.status >= 200 && xhr.status < 300) {
						// 控制台输出响应体
						console.log(xhr.response)
					} else {
						// 控制台输出响应状态码
						console.log(xhr.status)
					}
				}
			}
		})
		</script>
	</body>
</html>

```

Promise形式

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<div class="container">
			<h2 class="page-header">Promise封装AJAX操作</h2>
			<button class="btn btn-primary" id="btn">点击发送AJAX</button>
		</div>
		<script>
		// 接口地址：http://1.13.245.78/search/hitokoto
		const btn = document.querySelector("#btn")
		btn.addEventListener('click', function() {
			
			// 创建Promise对象
			const p = new Promise((resolve, reject) => {
				// 1.创建对象
				const xhr = new XMLHttpRequest()
				// 2.初始化
				xhr.open('GET', 'http://1.13.245.78/search/hitokoto')
				// 3.发送
				xhr.send()
				// 4.绑定事件，处理响应结果
				xhr.onreadystatechange = function() {
					if(xhr.readyState === 4) {
						// 判断响应状态码 2xx 为成功
						if(xhr.status >= 200 && xhr.status < 300) {
							// 控制台输出响应体
							resolve(xhr.response)
						} else {
							// 控制台输出响应状态码
							reject(xhr.status)
						}
					}
				}
			})
			
			p.then((value) => {
				console.log(value)
			}, (reason) => {
				console.log(reason)
			})
			
		})
		</script>
	</body>
</html>

```

## 1.4.`Promise`封装

### 1.4.1.`Promise`封装`fs`读取文件操作

```js
// 封装一个函数myReadFile，读取文件内容
// 参数：path
// 返回：promise对象
function myReadFile(path) {
	return new Promise((resolve, reject) => {
		require('fs').readFile(path, (err, data) => {
			if(err) reject(err)
			resolve(data.toString())
		})
	})
}
// 可以直接调用then方法，因为返回的是一个Promise对象
myReadFile('./resource/context.txt1').then((value) => {
	console.log(value)
}, (reason) => {
	console.log(reason)
})
```

当这样封装后，不需要在`readFile`后写回调函数，可以在`then`方法里写回调函数

### 1.4.2.使用`util.promisify`方法进行`promise`风格转化

上一小节中，我们是手动封装了`require('fs').readFile`方法

`node`中可以使用`util.prmisify`来达到`自动`封装的效果

官网：[util 实用工具 | Node.js API 文档 (nodejs.cn)](http://nodejs.cn/api/util.html#utilpromisifyoriginal)

> **`util.promisify(original)`**
>
> 新增于: v8.0.0
>
> - `original` `<Function>`
> - 返回: `<Function>`
>
> 
>
> 采用遵循常见的错误优先的回调风格的函数（也就是将 `(err, value) => ...` 回调作为最后一个参数），并返回一个返回 promise 的版本。



```js
// 引入util模块
const util = require('util')
// 引入fs模块
const fs = require('fs')

// 返回一个新的函数
let myReadFile = util.promisify(fs.readFile)
myReadFile('./resource/context.txt1').then(value => {
    console.log(value.toString())
})
```

作用：我们不需要每个函数都手动封装成`Promise`风格的函数

### 1.4.3.`Promise`封装`AJAX`

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>

		<script>
		// 接口地址：http://1.13.245.78/search/hitokoto
		// 封装一个函数 sendAJAX，发送GET AJAX请求
		// 参数：URL
		// 返回：Promise对象
		
		function sendAJAX(url) {
			return new Promise((resolve, reject) => {
				const xhr = new XMLHttpRequest()
				xhr.responseType = 'json'
				xhr.open('GET', url)
				xhr.send()
				// 处理结果
				xhr.onreadystatechange = function() {
					if(xhr.readyState === 4) {
						if(xhr.status >= 200 && xhr.status < 300) {
							resolve(xhr.response)
						} else {
							reject(xhr.status)
						}
					}
				}
			})
		}
		
		sendAJAX('http://1.13.245.78/search/hitokoto')
		.then(value => {
			console.log(value)
		}, reason => {
			console.log(reason)
		})
		</script>
	</body>
</html>

```



# 2.`Promise`的理解和使用

## 2.1.`Promise`是什么？

### 2.1.1.理解

- 抽象表达：

  - `Promise`是一门新的技术（ES6规范）

  - `Promise`是`JS`中进行异步编程的`新解决方案`

    - 旧解决方案是是使用回调函数

      - 什么是回调函数：[10张图让你彻底理解回调函数 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/326902537)

    - 异步操作包括哪些呢

      - `fs`文件操作

        ```js
        require('fs').readFile('./index.html',(err,data) => {})
        ```

      - 数据库操作

      - 网络请求（AJAX）

        ```js
        $.get('/server', (data) => {})
        ```

      - 定时器（setTImeout）

        ```js
        setTimeout(() => {},2000)
        ```

      

- 具体表达：

  - 从`语法`上来说，`Promise`是一个构造函数，可以通过`new`来实例化
  
    - 实例化时需要一个`函数`类型的值作为参数，并且这个函数有两个形参`resolve`、`reject`（写成`a`和`b`也可以）
  
      ```js
      const p = new Promise((resolve, reject) => {
      	// 包裹异步操作
      })
      ```
  
    - `resolve`和`reject`都是`函数`类型的数据
  
      - 当`异步任务成功`时，调用`resolve`函数，并将`Promise`对象`p`的`状态`，设置为`成功`
      - 当`异步任务失败`时，调用`reject`函数，并将`Promise`对象`p`的`状态`，设置为`失败`
      - 异步任务是成功还是失败，取决于实际业务逻辑，具体可见`2.3.1`的案例
  
    - `p.then()`
  
      - `Promise`的实例对象有一个`then`方法，这个方法执行时接收两个`函数`类型的参数
  
      - 第一个函数，是对象`p` `状态`为`成功`的回调函数
  
      - 第二个函数，是对象`p` `状态`为`失败`的回调函数
  
        ```js
        p.then(() => {
            // 成功状态后的操作
        }, () => {
            // 失败状态后的操作
        })
        ```
  
  - 从功能上来说，`Promise`对象用来封装一个异步操作，并可以获取其成功/失败的结果值
  
    - 详见`2.3.2`的案例

### 2.1.2.`Promise`对象的状态改变

- `状态`是`Promise`实例对象的一个`属性`：`[[PromiseState]]`

  ![image-20220506144353326](image-20220506144353326.png)

  - 该属性的可能值

    - `pending`：初始化的默认值，表示`未决定`

    - `resolved` / `fulfilled`：表示（异步操作的结果）`成功`
    - `rejected`：表示（异步操作的结果）`失败`

- 状态的改变
  - 异步操作`成功`，`Promise`对象状态，由`pending`变成`resolved`
  - 异步操作`失败`，`Promise`对象状态，由`pending`变成`rejected`
  - 说明：
    - `Promise`对象状态只有这两种，且一个`Promise`对象的状态，只能改变一次
    - 无论`Promise`对象状态变为`成功`还是`失败`，都会获取到异步操作的`结果数据`（前提是给`resovle`和`reject`函数传参了，否则`结果数据`为`undefined`）
    - `成功`状态获取到`结果数据`一般称为`value`，`失败`状态获取到的`结果数据`一般称为`reason`

### 2.1.3.`Promise`对象的结果值

- `结果值`是`Promise`实例对象的一个属性：`[[PromiseResult]]`，保存着`Promise`对象`成功/失败`的`结果值`

  ![image-20220506150130082](image-20220506150130082.png)

- 谁可以修改这个`结果值`呢？

  - `resolve/reject`这两个函数，是可以对实例对象中的`结果值`进行修改的

- 在后续`then`方法的回调函数中，就可以把实例对象的`结果值`取出来，然后进行相关的操作

### 2.1.4.`Promise`执行的基本流程

![image-20220507081353404](image-20220507081353404.png)

## 2.2.为什么要使用`Promise`？

### 2.2.1.指定回调函数的方式更加灵活

- 旧的：
  - 必须在异步任务前指定
- `Promise`：
  - 启动异步任务 => 返回`Promise`对象 => 给`Promise`对象绑定回调函数（甚至可以在异步任务结束后指定/多个）

### 2.2.2.支持链式调用，可以解决回调地狱的问题

- 什么是回调地狱？

  - 回调函数的嵌套调用，外部回调函数异步执行的结果，是嵌套的回调执行的条件

    ```js
    asyncFunc1(opt, (...args1) => {
        asyncFunc2(opt, (...args2) => {
            asyncFunc3(opt, (...args3) => {
                asyncFunc4(opt, (...args4) => {
                    // some operation
                })
            })
        })
    })
    ```

- 回调地狱的缺点

  - 语法上的一层层嵌套，只是最基础的
  - 不便于阅读
  - 不便于异常处理
    - 可能会写很多重复性代码
  - 控制反转问题（重点）

- 解决方案

## 2.3.如何使用`Promise`

### 2.3.1.API

#### `Promise`构造函数

- `Promise`构造函数：`Promise(executor) {}`

  - `Promise`构造函数实例化时，需要接收一个函数类型的参数，可以是箭头函数或匿名函数，该参数被称为`executor`函数

  - `executor`函数：表示执行器函数，就是`(resolve, reject) => {}`

    - 执行器函数特点：会在`Promise`内部立即同步调用，异步操作在执行器函数执行

      ```js
      const p = new Promise((resolve, reject) =>{
          console.log('aa')
      })
      
      console.log('bb')
      ```

      打印结果如下：

      ![image-20220507083113595](image-20220507083113595.png)

    - 先输出`aa`，再输出`bb`，就说明执行器函数内部的代码，和第5行的代码，是同步调用的，也就是说，执行器函数的代码，不会进入到队列中，会立即执行（后面进行封装时要注意这一点）

  - `resolve`函数：内部定义成功时，我们调用的函数，并且会修改`Promise`对象的`结果值`：`value => {}`

  - `reject`函数：内部定义失败时，我们调用的函数。并且会修改`Promise`对象的`结果值`：`reason => {}`

#### `Promise.prototype.then`方法

- `Promise.prototype.then`方法：`(onResolved, onRejected) =>{}`

  -  `then`方法有两个参数，也都是函数类型的参数，指定用于得到成功`value`的成功回调，和用于得到失败`reason`失败的回调，返回一个新的`Promise`对象
  - `onResolved`函数：成功的回调函数，并获取到`Promise`对象的`结果值`：`value => {}`
  - `onRejected`函数：失败的回调函数，并获取到`Promise`对象的`结果值`：`reason => {}`

- `then`方法的返回值：为一个新的`Promise`对象

  - 如果`then`方法的回调函数中，抛出异常，新`Promise`状态变为`rejected`，结果值`reason`为抛出的异常

    ```js
    let p = new Promise((resolve, reject) => {
        resolve('ok')
    })
    
    // 执行then方法
    let result = p.then(value => {
        throw 'Error'
    }, reason => {
        console.log(reason)
    })
    
    console.log(result)
    
    result.catch(reason => {
        return reason
    })
    ```

    ![image-20220507153130222](image-20220507153130222.png)

  - 如果`then`方法的回调函数中，返回的是非`Promise`的任意值，新`Promise`状态变为`resolved/fulfilled`，结果值`value`为返回的值

    ```js
    let p = new Promise((resolve, reject) => {
        resolve('ok')
    })
    
    // 执行then方法
    let result = p.then(value => {
        return 521
    }, reason => {
        console.log('reason为：' + reason)
    })
    
    console.log(result)
    
    ```

    ![image-20220507153255634](image-20220507153255634.png)

  - 如果`then`方法的回调函数中，返回的是另一个新的`Promise`，此`Promise`的结果就会成为新的`Promise`的结果

    ```js
    let p = new Promise((resolve, reject) => {
        resolve('ok')
    })
    
    // 执行then方法
    let result = p.then(value => {
        return new Promise((resolve, reject) => {
            resolve('success')
        })
    }, reason => {
        console.log('reason为：' + reason)
    })
    
    console.log(result)
    
    ```

    ![image-20220507153513379](image-20220507153513379.png)

  - 如果`then`方法的回调函数中，即没有抛出异常，也没有`return`，则新的`Promise`对象的结果值为`undefined`

#### `Promise.prototype.catch`方法

- `Promise.prototype.catch`方法：`(onRejected) => {}`

  - `catch`方法也是用来指定回调的，不过只能用来指定`失败`的回调

    - `catch`只是做了一个单独的封装，内部也是用`then`方法来实现的

  - `onRejected`函数：失败的回调函数，并获取到`Promise`对象的`结果值`：`reason => {}`

    ```js
    const p = new Promise((resovle, reject) => {
        reject('error')
    })
    
    p.catch(reason => {
        console.log(reason)
        return reason
    })
    ```

    打印结果如下：

    ![image-20220507085159105](image-20220507085159105.png)

  - `catch`处理过失败的`Promise`对象后，返回的是一个成功的`Promise`对象，该对象的结果值，取决于你在实际代码中返回的值。

#### `Promise.resolve`方法

- `Promise.resolve`方法：`(value) => {}`

  - `resolve`是在`Promise`实例对象上的，而不是在`Promise`的原型对象上

  - `resolve`参数：`value`可以是`成功状态`的`结果`值或`Promise`对象

    - 如果传入的参数为非`Promise`类型的对象（可以是`undefined`、`null`等等），则返回的结果为成功的`Promise`对象

      ```js
      const p = Promise.resolve('value')
      console.log(p)
      ```

      ![image-20220507090126462](image-20220507090126462.png)

    - 如果传入的参数为`Promsie`对象，则参数的结果，决定了`resolve`的结果

      - 当参数返回成功时，得到的就是`成功`的`Promise`：

        ```js
        const p = Promise.resolve(new Promise((resolve, reject) => {
            resolve(true)
        }))
        console.log(p)
        ```

        ![image-20220507091211503](image-20220507091211503.png)

      - 当参数返回失败时，得到的就是`失败`的`Promise`：

        ```js
        const p = Promise.resolve(new Promise((resolve, reject) => {
            reject('Error')
        }))
        console.log(p)
        p.catch(reason =>{
            console.log(reason)
        })
        ```

        ![image-20220507091337333](image-20220507091337333.png)

  - 返回：返回一个`成功/失败`的`Promise`对象
  - 作用：为了快速得到一个`Promise`对象，并且还能封装一个值，将这个值转化为`Promise`对象

#### `Promise.reject`方法

- `Promise.reject`方法：`(reason) => {}`

  - `reject`是在`Promise`实例对象上的，而不是在`Promise`的原型对象上

  - `reject参数`：`reason`表示失败的原因

    - 如果传入的参数为非`Promise`类型的对象，返回的是`失败`的`Promise`对象

      ```js
      const p = Promise.reject('value')
      console.log(p)
      
      p.catch(reason => {
      console.log('reason为：', reason)
      })
      ```

      ![image-20220507092446179](image-20220507092446179.png)

    - 如果传入的参数为`失败`的`Promise`对象，返回的是`失败`的`Promise`对象

      ```js
      // 定义失败的Promise对象
      let p1 = new Promise((resolve, reject) => {
          reject('Error')
      })
      
      // 处理失败的Promise对象
      p1.catch(reason => {
          return reason
      })
      
      const p2 = Promise.reject(p1) // 将失败的Promise对象传入reject
      console.log(p2) // 返回的仍是失败的Promise对象，其结果值是传入的那个Promise对象
      
      p2.catch(reason => {
          console.log('reason为：', reason)
      })
      ```

      ![image-20220507112525950](image-20220507112525950.png)

      

    - 如果传入的参数为`成功`的`Promise`对象，返回的仍然是`失败`的`Promise`对象，只不过`reason`是你传的那个`成功`的`Promise`对象

      ```js
      const p = Promise.reject(new Promise((resolve, reject) => {
          resolve('OK')
      }))
      console.log(p)
      
      p.catch(reason => {
          console.log('reason为：', reason)
      })
      ```

      

    ![image-20220507092737721](image-20220507092737721.png)

  - 返回：始终返回一个`失败`的`Promise`对象

  - 作用：为了快速的将一个值，转换成一个失败的`Promise`对象。无论这是值是非`Promise`类型，还是`成功/失败`的`Promise`类型。

#### `Promise.all`方法

- `Promise.all`方法：`(promises) => {}`

  - `promises`参数：包含`n`个`promise`的数组

  - 返回：返回一个新的`promise`，只有所有的`promise`都成功才成功，只要有一个失败了就直接失败

    - 如果数组中的每个`Promise`对象状态都是成功，`all`方法返回的是一个成功的`Promise`对象，该`Promise`对象成功的`结果值`，是每个`promise` 的`成功结果值`组成的数组

      ```js
      let p1 = new Promise((resolve, reject) => {
      resolve('OK')
      })
      let p2 = Promise.resolve('Success')
      let p3 = Promise.resolve('Oh Yeah')
      
      const result = Promise.all([p1, p2, p3])
      console.log(result)
      ```

      ![image-20220507105139821](image-20220507105139821.png)

    - 如果数组中有一个`Promise`对象状态是失败，`all`方法返回的是一个失败的`Promise`对象，该`Promise`对象失败的`结果值`，是那个失败的`Promise`对象的结果值

      ```js
      let p1 = new Promise((resolve, reject) => {
          resolve('OK')
      })
      let p2 = Promise.reject('Error') // 失败的Promise对象
      let p3 = Promise.resolve('Oh Yeah')
      
      const result = Promise.all([p1, p2, p3])
      console.log(result)
      ```

      返回的是一个失败的`Promise`对象

      ![image-20220507105917420](image-20220507105917420.png)

      注意：如果我们用链式调用的方式，使用`catch`指定了失败`Promise`对象的回调，则`all`方法返回的仍是成功的`Promise`对象

      ```js
      let p1 = new Promise((resolve, reject) => {
          resolve('OK')
      })
      let p2 = Promise.reject('Error').catch(reason => {
          return reason
      }) // 使用catch处理失败的Promise对象，返回的是一个成功的Promise对象
      let p3 = Promise.resolve('Oh Yeah')
      
      const result = Promise.all([p1, p2, p3])
      console.log(result)
      ```

      ![image-20220507110354017](image-20220507110354017.png)

      因为失败的`Promise`一旦用`catch`指定失败的`回调`，其返回值是一个成功的`Promise`对象

      所以在处理失败的`Promise`对象时，不能用链式调用的写法，要分开来写才行，这样`p2`就是一个失败的`Promise`对象了

      ```js
      let p1 = new Promise((resolve, reject) => {
          resolve('OK')
      })
      
      let p2 = Promise.reject('Error')
      p2.catch(reason => {
          return reason
      }) // 分开来写
      
      let p3 = Promise.resolve('Oh Yeah')
      
      const result = Promise.all([p1, p2, p3])
      console.log(result)
      
      result.catch(reason => {
          return reason
      })
      ```

      ![image-20220507113147000](image-20220507113147000.png)

      备注：如果有两个失败的`Promise`对象，则返回的`结果值`是优先失败的那个`Promise`对象的结果值，这里返回的是`p3`的结果值

      ```js
      let p1 = new Promise((resolve, reject) => {
          resolve('OK')
      })
      
      let p2 = Promise.reject('Error') // 失败的Promise
      p2.catch(reason => {
          return reason
      })
      
      let p3 = Promise.reject('Oh Yeah') // 失败的Promise
      p3.catch(reason => {
          return reason
      })
      
      const result = Promise.all([p1, p3, p2]) // 将p3放在前面
      console.log(result)
      
      result.catch(reason => {
          return reason
      })
      ```

      ![image-20220507113516027](image-20220507113516027.png)

#### `Promise.race`方法

- `Promise.race`方法：`(promises) => {}`

  - `promises`参数：包含`n`个`promise`的数组

  - 返回：返回一个新的`Promise`，第一个完成的`Promise`的结果状态，就是最终的结果状态

    ```js
    let p1 = new Promise((resolve, reject) => {
        resolve('OK')
    })
    
    let p2 = Promise.resolve('Success')
    
    let p3 = Promise.resolve('Oh Yeah')
    
    const result = Promise.race([p1, p2, p3])
    console.log(result)
    ```

    ![image-20220507114320619](image-20220507114320619.png)

    `p1`先完成，`race`返回的就是`p1`的状态结果

    我们给`p1`添加一个定时器

    ```js
    let p1 = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('OK')
        }, 2000)
    })
    
    let p2 = Promise.reject('Error')
    p2.catch(reason => {
        return reason
    })
    
    let p3 = Promise.resolve('Oh Yeah')
    
    const result = Promise.race([p1, p2, p3])
    console.log(result)
    
    result.catch(reason => {
        return reason
    })
    ```

    ![image-20220507114615597](image-20220507114615597.png)

    `p2`先完成，`race`返回的就是`p2`的结果

### 2.3.2`Promise`的几个关键问题

#### 如何改变`Promise`的状态

- `resolve(value)`：如果当前是`pending`，就会变成`resolved`

  ```js
  let p = new Promise((resolve, reject) => {
  	// 1.resolve函数
      resolve('OK') // pending ==> fulfilled
  })
  ```

- `reject(reason)`：如果当前是`pending`，就会变成`rejected`

  ```js
  let p = new Promise((resolve, reject) => {
  	// 2.reject函数
      resolve('Error') // pending ==> rejected
  })
  ```

- 通过`throw`抛出了异常：如果当前是`pending`，就会变成`rejected`

  ```js
  let p = new Promise((resolve, reject) => {
  	// 3.throw抛出异常
      throw 'Error' // pending ==> rejected
  })
  ```

#### 能否执行多个回调

- 如果使用`then`方法，为一个`Promise`对象指定多个成功/失败回调函数，都会调用吗？

  - 当`Promise`改变为对应状态时都会调用

    ```js
    let p = new Promise((resolve, reject) => {
        resolve('OK') // pending => fulfilled
    })
    
    // 指定回调1
    p.then(value => {
        console.log(value + '1')
    })
    // 指定回调2
    p.then(value => {
        console.log(value + '2')
    })
    ```

    结果如下：

    ![image-20220507142047652](image-20220507142047652.png)

    如果不调用`resolve`，则状态一直是`pending`，则回调函数也不会被调用

#### 改变`Promise`状态和指定回调函数谁先谁后

```js
let p = new Promise((resolve, reject) => {
    resolve('OK') // 改变状态
})

p.then(value => {
    // 指定回调
}, reason => {
    
})
```

问：`resolve('OK')`改变状态，和`value => {}`指定回调，谁先执行？

- 都有可能，正常情况下是先指定回调再改变状态，但也可以先改变状态再指定回调

  - 如何改变`Promise`状态：

    - `resolve()`
    - `reject()`
    - `throw`

  - 如何指定回调：

    - `then()`
    - `catch()`

  - 什么时候先改变状态，再指定回调？

    - 在执行器函数中，直接调用`resolve()/reject()`

    - 当执行器函数里面的任务，是同步任务的时候

      ```js
      let p = new Promise((resolve, reject) => {
          resolve('OK') // 先改变状态
      })
      
      p.then(value => {
          // 后指定回调
          console.log(value)
      }, reason => {
          
      })
      ```

    - 延迟更长时间才调用`then()`，这个例子中，我们可以延迟2秒再执行`then()`方法

      

  - 什么时候先指定回调，后改变状态？

    - 当执行器函数里面的任务，是异步任务，需要进入队列的时候

      ```js
      let p = new Promise((resolve, reject) => {
          // 后改变状态
          setTimeout(() => {
             resolve('OK') 
          }, 2000)
      })
      
      p.then(value => {
          // 先指定回调
          // 等1秒，输出value
          console.log(value)
      }, reason => {
          
      })
      ```

    - 进行文件操作、数据库操作、`AJAX`操作时，执行器函数里面的，都是异步任务

- 什么时候才能得到数据？（回调函数什么时候执行）

  - 执行器函数中，可以是同步任务，也可以是异步任务
  - 如果先指定的回调，那当状态发生改变时，回调函数就会调用，得到数据（异步任务）
  - 如果先改变状态，那当指定回调时，回调函数就会调用，得到数据（同步任务）



#### `Promise.then()`返回的新的`Promise`的结果状态，由什么决定？

- 简单表达：由`then()`指定的回调函数执行的结果决定

- 详细表达：

  - `then`方法的返回值：为一个新的`Promise`对象

    - 如果`then`方法的回调函数中，抛出异常，新`Promise`状态变为`rejected`，结果值`reason`为抛出的异常

      ```js
      let p = new Promise((resolve, reject) => {
          resolve('ok')
      })
      
      // 执行then方法
      let result = p.then(value => {
          throw 'Error'
      }, reason => {
          console.log(reason)
      })
      
      console.log(result)
      
      result.catch(reason => {
          return reason
      })
      ```

      ![image-20220507153130222](image-20220507153130222.png)

    - 如果`then`方法的回调函数中，返回的是非`Promise`的任意值，新`Promise`状态变为`resolved/fulfilled`，结果值`value`为返回的值

      ```js
      let p = new Promise((resolve, reject) => {
          resolve('ok')
      })
      
      // 执行then方法
      let result = p.then(value => {
          return 521
      }, reason => {
          console.log('reason为：' + reason)
      })
      
      console.log(result)
      
      ```

      ![image-20220507153255634](image-20220507153255634.png)

    - 如果`then`方法的回调函数中，返回的是另一个新的`Promise`，此`Promise`的结果就会成为新的`Promise`的结果

      ```js
      let p = new Promise((resolve, reject) => {
          resolve('ok')
      })
      
      // 执行then方法
      let result = p.then(value => {
          return new Promise((resolve, reject) => {
              resolve('success')
          })
      }, reason => {
          console.log('reason为：' + reason)
      })
      
      console.log(result)
      
      ```

      ![image-20220507153513379](image-20220507153513379.png)
      
    - 如果`then`方法的回调函数中，即没有抛出异常，也没有`return`，则新的`Promise`对象的结果值为`undefined`

#### `Promise`如何串联多个操作任务

- `Promise`的`then()`返回一个新的`Promise`，可以写成`then()`的链式调用

  ```js
  let p = new Promise((resolve, reject) => {
      setTimeout(() => {
          resolve('OK')
      }, 1000)
  })
  
  p.then(value => {
      console.log(value) // 延迟一秒，OK
      return new Promise((resolve, reject) => {
          resolve('success')
      })
  }).then(value => {
      console.log(value) // success
  }).then(value => {
      console.log(value) // undefined
  })
  ```

  ![image-20220507155355522](image-20220507155355522.png)

- 通过`then()`的链式调用串联多个同步/异步任务



#### `Promise`异常穿透

- 当使用`Promise`的`then`链式调用时，可以在最后指定失败的回调

  ```js
  let p = new Promise((resolve, reject) => {
      setTimeout(() => {
          reject('Error')
      }, 1000)
  })
  
  p.then(value => {
      console.log(value)
      return new Promise((resolve, reject) => {
          resolve('success')
      })
  }).then(value => {
      console.log(value)
  }).then(value => {
      console.log(value)
  }).catch(reason => {
      console.log(reason) // 1秒后 Error
  })
  ```

  ![image-20220507160049244](image-20220507160049244.png)

- 前面任何操作出现了异常，都会传到最后失败的回调中处理

  - 如果出现了多个异常，只捕获第一个异常

  ```js
  let p = new Promise((resolve, reject) => {
      setTimeout(() => {
          reject('Error')
      }, 1000)
  })
  
  p.then(value => {
      console.log(value)
      return new Promise((resolve, reject) => {
          reject('Error02')
      })
  }).then(value => {
      console.log(value)
  }).then(value => {
      console.log(value)
  }).catch(reason => {
      console.log(reason) // 1秒后 Error,不会输入Error02
  })
  ```

#### 如何中断`Promise`链

- 当使用`Promise`的链式调用时，在中间中断，不再调用后面的回调函数

- 唯一办法：

  - 在回调函数中返回一个`pendding`状态的`Promise`对象

  - `pendding`状态，意味着状态没有发生改变，也就不会执行回调函数了

  - 代码：`return new Promise((resolve, reject) => {})`

    ```js
    let p = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('OK')
        }, 1000)
    })
    
    p.then(value => {
        console.log(111) // 只会输出111
        return new Promise((resolve, reject) => {})
    }).then(value => {
        console.log(222) // 不会被调用
    }).then(value => {
        console.log(333) // 不会被调用
    })
    ```

    ![image-20220507161804408](image-20220507161804408.png)

# 3.手写`Promise`

## 3.1.定义整体结构

```
|----index.html
|----promise.js
```

`index.html`

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
		 // 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				resolve('OK')
			})
			
			p.then(value => {
				console.log(value)
			}, reason =>{
				console.log(reason)
			})
		</script>
	</body>
</html>

```

`promise.js`

```js
function Promise() {

}

```

报错信息如下，因为我们没有在构造函数`Promise`的显示原型属性上定义`then`方法，所以实例对象`p`的隐式原型属性上自然就没有该`then`方法

![image-20220507164406093](image-20220507164406093.png)

构造函数`Promise`的显示原型属性上，添加`then`方法，该`then`方法有两个形参：`onResolved`、`onRejected`

同时也给`Promise`构造函数，指定一个形参：`executor`

`promise.js`

```js
function Promise(executor) {

}

// 添加then方法
Promise.prototype.then = function(onResolved, onRejected) {

}

```

至此，基本结构搭建完毕

## 3.2.`resolve`和`reject`结构搭建

`promise.js`

```js
function Promise(executor) {
	// 执行器函数是同步调用的
    executor(resolve, reject) // 调用执行器函数时，需要传递两个参数
}

Promise.prototype.then = function(onResolved, onRejected) {

}

```

注意：在当前作用域当中，并没有`resolve`和`reject`变量

所以需要在函数内部声明，这两个变量都是函数类型的变量

`promise.js`

```js
function Promise(executor) {
	// 声明执行器函数需要的两个参数,resolve()和reject()
    // 同时这两个函数也需要传递一个参数
    
    // resolve函数
    function resolve(data) {
        
    }
    // reject函数
    function reject(data) {
        
    }
    
    executor(resolve, reject)
}

Promise.prototype.then = function(onResolved, onRejected) {

}

```

## 3.3.`resolve`和`reject`代码实现

- `resolve`函数执行完之后，有什么效果？
  - `Promise`的状态会发生改变，有`pending`变为`fulfilled`
  - 可以设置`Promise`对象的结果值
- 我们需要添加`promiseState`和`promiseResult`这两个属性

`promise.js`

```js
function Promise(executor) {
    // 添加属性并设置默认值
	this.PromiseState = 'pending'
    this.PromiseResult = null
    
    function resolve(data) {
        // 修改对象的状态 [[promiseState]]
        this.PromiseState = 'fulfilled' // 等价于resolved
        // 设置对象的结果值 [[promiseResult]]
        this.PromiseResult = data
    }

    function reject(data) {
        
    }
    
    executor(resolve, reject)
}

Promise.prototype.then = function(onResolved, onRejected) {

}

```

在`index.html`中测试看下效果

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
		 // 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				resolve('OK')
			})
			
			console.log(p)
			
			// p.then(value => {
			// 	console.log(value)
			// }, reason =>{
			// 	console.log(reason)
			// })
		</script>
	</body>
</html>

```

结果如下：

![image-20220507172528344](image-20220507172528344.png)

按道理来说，`PromiseResult`应该是`OK`，`PromiseState`应该是`fulfilled`

为什么没有变化呢？

是因为`resolve`函数中，`this`指向`window`

```js
function Promise(executor) {

	this.PromiseState = 'pending'
    this.PromiseResult = null
    // 保存实例对象的this值
    const self = this
    
    function resolve(data) {
        self.PromiseState = 'fulfilled'

        self.PromiseResult = data
    }

    function reject(data) {
        
    }
    
    executor(resolve, reject)
}

Promise.prototype.then = function(onResolved, onRejected) {

}

```

结果：

![image-20220507202336185](image-20220507202336185.png)

此时，调用`resolve`，`Promise`对象的状态和结果都发生了改变

完善一下`reject`

```js
function Promise(executor) {

	this.PromiseState = 'pending'
    this.PromiseResult = null

    const self = this
    
    function resolve(data) {
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data
    }

    function reject(data) {
        self.PromiseState = 'rejected'
        self.PromiseResult = data
    }
    
    executor(resolve, reject)
}

Promise.prototype.then = function(onResolved, onRejected) {

}

```

## 3.4.`throw`抛出异常改变状态

如果直接抛出异常，则会报错

```html
		<script>
			let p = new Promise((resolve, reject) => {

				throw 'Error'
			})
			
			console.log(p)
		</script>
```

![image-20220507202734042](image-20220507202734042.png)

正常来说，应该打印一个失败的`Promise`对象

我们使用`try catch`来处理`throw`，加在执行器函数执行的地方

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null

    const self = this

    function resolve(data) {
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data
    }

    function reject(data) {
        self.PromiseState = 'rejected'
        self.PromiseResult = data
    }

    // 处理抛出的异常
    try {
        executor(resolve, reject)
    } catch (e) {
        // 获取到异常后，修改Promise的状态为失败
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {

}


```

打印结果：

![image-20220507203149432](image-20220507203149432.png)

## 3.5.`Promise`状态只能修改一次

我们现在封装的代码，如果先调用了`resolve`，再调用`reject`，`Promise`对象的状态会改变两次

```html
		<script>
			let p = new Promise((resolve, reject) => {
                resolve('OK')
                reject('error')
			})
			
			console.log(p)
		</script>
```

最终的结果（这是错误的）：

![image-20220507203744855](image-20220507203744855.png)

那么应该怎么做，可以确保状态值更改一次呢？

应该在改变状态之前，加一层判断，判断是否已经更改过了

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null

    const self = this

    function resolve(data) {
        // 判断Promise状态是否已经更改过了，保证Promise状态只能更改一次
        if(self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data
    }

    function reject(data) {
        if(self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {

}


```

结果如下（这个是对的）：

![image-20220507204043155](image-20220507204043155.png)

## 3.6.`then`方法执行回调

此时我们封装的`then`方法，是不能执行回调的

`index.html`

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
		 // 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				resolve('OK')
			})
			
			p.then(value => {
				console.log(value)
			}, reason =>{
				console.log(reason)
			})
		</script>
	</body>
</html>

```

结果是没有打印输出的

为啥呢？因为我们还没写调用的代码！

应该在`then`方法中调用回调函数

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null

    const self = this

    function resolve(data) {
        if(self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data
    }

    function reject(data) {
        if(self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {
    // 调用回调函数
    // 这两个回调函数的执行，应该有执行条件

    // 如果成功，调用onResolved()
    // 成功的判断条件，保存在实例对象的PromiseState属性中
    if(this.PromiseState === 'fulfilled') {
        onResolved(this.PromiseResult) // 调用then方法时，是有一个value参数的，所以这里也要传入一个参数，该参数是Promise成功的结果值
    }
    
    // 如果失败，调用onRejected()
    // 失败的判断条件，保存在实例对象的PromiseState属性中
    if(this.PromiseState === 'rejected') {
        onRejected(this.PromiseResult)
    }
}

```

打印结果：

![image-20220507205644584](image-20220507205644584.png)

## 3.7.异步任务回调的执行

我们在执行器函数中定义异步任务

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
		 // 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				setTimeout(() => {
					resolve('OK')
				}, 1000)
			})
			

			p.then(value => {
				console.log(value)
			}, reason =>{
				console.log(reason)
			})
		</script>
	</body>
</html>

```

此时并没有打印输出结果

代码从上往下走，`resovle`函数并没有立即执行

再往下走，`p`的状态并没有发生变化，依旧是`pending`状态，但我们并没有对`pending`状态做任何处理 

所以，在`then`方法中我们需要对`pending`状态进行判断

```js
    // 判断pending状态
    if(this.PromiseState === 'pending') {
       // do something 
    }
```

那么，我们需要做什么操作呢？

对于异步任务来说，什么时候调用回调函数呢？应该是在状态发生改变的时候，那么什么时候状态发生改变呢？

很明显，是在调用`resovle/reject`函数的时候，

所以我们应该在`resolve/reject`函数内，调用回调函数

```js
    function resolve(data) {
        if(self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data
        
        // 调用回调函数
        // ...
    }
```

那么，怎么样才可以在`resovle`内，调用到`then`方法的回调函数呢？这两个函数是在不同的作用域内的

所以，我们在判断`pending`状态后，应该将回调函数保存下来

那么，应该保存在哪儿呢？在`then`方法外部定义一个变量吗？不！我们直接给`Promise`构造函数声明一个属性，实例化时保存在实例对象上

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null
    this.callback = {} // 回调函数保存在实例对象的callback属性上
    const self = this

    function resolve(data) {
        if(self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data
    }

    function reject(data) {
        if(self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {
    if(this.PromiseState === 'fulfilled') {
        onResolved(this.PromiseResult)
    }

    if(this.PromiseState === 'rejected') {
        onRejected(this.PromiseResult)
    }

    // 判断pending状态
    if(this.PromiseState === 'pending') {
        // 保存回调函数
        this.callback = {
            onResolved,
            onRejected
        }
    }
}


```

运行完`then`方法后，打印输出`p`：

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
		 // 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				setTimeout(() => {
					resolve('OK')
				}, 1000)
			})
		
			p.then(value => {
				console.log(value)
			}, reason =>{
				console.log(reason)
			})
            
			console.log(p)
		</script>
	</body>
</html>

```

打印结果：

![image-20220508102848816](image-20220508102848816.png)

对象`p`已经有了回调函数

之后，我们就可以在`resolve/reject`函数中，执行对应的回调函数了

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null
    this.callback = {} // 回调函数保存在实例对象的callback属性上
    const self = this

    function resolve(data) {
        if(self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data
        // 等到队列里的任务开始执行时，调用成功的回调函数
        if(self.callback.onResolved) {
            self.callback.onResolved(data)
        }

    }

    function reject(data) {
        if(self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data

        // 调用失败的回调函数
        if(self.callback.onRejected) {
            self.callback.onRejected(data)
        }
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {
    if(this.PromiseState === 'fulfilled') {
        onResolved(this.PromiseResult)
    }

    if(this.PromiseState === 'rejected') {
        onRejected(this.PromiseResult)
    }

    // 判断pending状态
    if(this.PromiseState === 'pending') {
        // 保存回调函数
        this.callback = {
            onResolved,
            onRejected
        }
    }
}


```

此时再看下打印效果，一秒后，输出结果：

![image-20220508103251580](image-20220508103251580.png)

## 3.8.指定多个回调的实现

`index.html`

`````html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
		 // 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				setTimeout(() => {
					resolve('OK')
				}, 1000)
			})
			

			p.then(value => {
				console.log(value + '1')
			}, reason =>{
				console.log(reason)
			})

			p.then(value => {
				console.log(value + '2')
			}, reason =>{
				console.log(reason)
			})
		</script>
	</body>
</html>

`````

目前我们的代码是不能够执行多个回调的，最后的`then`方法中的回调，会将之前的覆盖掉，只会执行最后一次的回调

所以我们之前那种保存回调函数的方式，需要修改一下：

将`callback`定义成数组，每次保存回调时`push`进去一个对象即可

```js
this.callbacks = [] // 回调函数保存在实例对象的callback属性上


    ...
        // 判断pending状态
    if(this.PromiseState === 'pending') {
        // 保存回调函数
        this.callbacks.push({onResolved, onRejected})
    }
```

在`then`方法后面，打印一下对象`p`

![image-20220508104251121](image-20220508104251121.png)

此时两个回调函数都被保存到了实例对象上

在`resovle/reject`函数中，重新调用下相应的回调函数

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null
    this.callbacks = [] // 回调函数保存在实例对象的callback属性上
    const self = this

    function resolve(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data
        // 调用成功的回调函数
        self.callbacks.forEach(item => {
            item.onResolved(data)
        })
    }

    function reject(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data

        // 调用失败的回调函数
        self.callbacks.forEach(item => {
            item.onRejected(data)
        })
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {
    if (this.PromiseState === 'fulfilled') {
        onResolved(this.PromiseResult)
    }

    if (this.PromiseState === 'rejected') {
        onRejected(this.PromiseResult)
    }

    // 判断pending状态
    if (this.PromiseState === 'pending') {
        // 保存回调函数
        this.callbacks.push({onResolved, onRejected})
    }
}


```

打印结果如下：

![image-20220508104703666](image-20220508104703666.png)

两次回调函数都被执行了

## 3.9.同步任务下的`then`方法返回结果实现

index.html

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
		 // 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				resolve('OK')
			})


			const res = p.then(value => {
				// console.log(value)
				return 'Hello Promise'
			}, reason =>{
				console.log(reason)
			})

			console.log(res)


		</script>
	</body>
</html>

```

目前`res`是`undefined`，因为我们在`then`方法中，并没有返回任何的值

![image-20220508110748669](image-20220508110748669.png)

所以我们在`then`方法中，返回一个`Promise`对象

```js

Promise.prototype.then = function (onResolved, onRejected) {

    return new Promise((resolve, reject) => {
        if (this.PromiseState === 'fulfilled') {
            onResolved(this.PromiseResult)
        }

        if (this.PromiseState === 'rejected') {
            onRejected(this.PromiseResult)
        }

        // 判断pending状态
        if (this.PromiseState === 'pending') {
            // 保存回调函数
            this.callbacks.push({onResolved, onRejected})
        }
    })

}
```

此时`res`的结果如下：

![image-20220508111143335](image-20220508111143335.png)

有个问题，就是`then`方法返回的`Promise`对象的状态，一直是`pending`

我们需要根据`then`方法回调函数的执行结果，来改变`then`方法返回的`Promise`对象的状态

所以要定义一个变量`result`保存回调函数执行的结果

```js
let result = onResolved(this.PromiseResult)
```

对结果进行类型判断，并对状态进行设置

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null
    this.callbacks = [] // 回调函数保存在实例对象的callback属性上
    const self = this

    function resolve(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data
        // 调用成功的回调函数
        self.callbacks.forEach(item => {
            item.onResolved(data)
        })
    }

    function reject(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data

        // 调用失败的回调函数
        self.callbacks.forEach(item => {
            item.onRejected(data)
        })
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {

    return new Promise((resolve, reject) => {
        if (this.PromiseState === 'fulfilled') {
            let result = onResolved(this.PromiseResult)
            if(result instanceof Promise) {

            } else {
                // 回调函数的结果不是Promise的实例
                // 设置then方法返回的结果对象状态为成功
                resolve(result)
            }
        }

        if (this.PromiseState === 'rejected') {
            let result = onRejected(this.PromiseResult)
        }

        // 判断pending状态
        if (this.PromiseState === 'pending') {
            // 保存回调函数
            this.callbacks.push({onResolved, onRejected})
        }
    })

}


```

打印结果如下：

![image-20220508114057606](image-20220508114057606.png)

如果`then`方法的回调函数，返回的是`Promise`类型的对象呢？

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null
    this.callbacks = []
    const self = this

    function resolve(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data
        // 调用成功的回调函数
        self.callbacks.forEach(item => {
            item.onResolved(data)
        })
    }

    function reject(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data

        // 调用失败的回调函数
        self.callbacks.forEach(item => {
            item.onRejected(data)
        })
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {
    return new Promise((resolve, reject) => {
        if (this.PromiseState === 'fulfilled') {
            let result = onResolved(this.PromiseResult)
            if (result instanceof Promise) {
                // 如果是Promise对象，则去调用then方法
                result.then(v => {
                    // 如果成功了，则整体then方法的返回结果也是成功的
                    resolve(v)
                }, r => {
                    reject(r)
                })
            } else {
                // 回调函数的结果不是Promise的实例
                // 设置then方法返回的结果对象状态为成功
                resolve(result)
            }
        }

        if (this.PromiseState === 'rejected') {
            let result = onRejected(this.PromiseResult)
        }

        if (this.PromiseState === 'pending') {
            this.callbacks.push({onResolved, onRejected})
        }
    })
}


```

`index.html`

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
		 // 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				resolve('OK')
			})


			const res = p.then(value => {
				return new Promise((resolve, reject) => {
					resolve("success")
				})
			}, reason =>{
				console.log(reason)
			})

			console.log(res)


		</script>
	</body>
</html>

```

打印结果如下：

![image-20220508185206461](image-20220508185206461.png)

如果`then`方法的回调函数，抛出了异常呢？

使用`try catch`进行包裹处理

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null
    this.callbacks = []
    const self = this

    function resolve(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data
        // 调用成功的回调函数
        self.callbacks.forEach(item => {
            item.onResolved(data)
        })
    }

    function reject(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data

        // 调用失败的回调函数
        self.callbacks.forEach(item => {
            item.onRejected(data)
        })
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {
    return new Promise((resolve, reject) => {
        if (this.PromiseState === 'fulfilled') {

            // 使用try catch进行包裹处理
            try {
            	let result = onResolved(this.PromiseResult)
                
                if (result instanceof Promise) {
                    result.then(v => {
                        resolve(v)
                    }, r => {
                        reject(r)
                    })
                } else {
                    resolve(result)
                }
            } catch(e) {
                reject(e)
            }

        }

        if (this.PromiseState === 'rejected') {
            let result = onRejected(this.PromiseResult)
        }

        if (this.PromiseState === 'pending') {
            this.callbacks.push({onResolved, onRejected})
        }
    })
}


```

`index.html`

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
		 // 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				resolve('OK')
			})


			const res = p.then(value => {
				return new Promise((resolve, reject) => {
					throw 'Error'
				})
			}, reason =>{
				console.log(reason)
			})

			console.log(res)


		</script>
	</body>
</html>

```

打印结果如下：

![image-20220508190102202](image-20220508190102202.png)

## 3.10.异步任务下的`then`方法返回结果实现

`index.html`

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
		 // 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				// 使用定时器模拟异步任务
				setTimeout(() => {
					resolve('OK')
				}, 1000)
			})


			const res = p.then(value => {
				console.log(value)
			}, reason =>{
				console.log(reason)
			})

			console.log(res)


		</script>
	</body>
</html>

```

打印结果是`pending`状态的`Promise`：

![image-20220508190707825](image-20220508190707825.png)

由于是异步任务，对象`p`在调用`then`方法时，是一个`pending`状态，目前我们自定义的代码，对于`pending`状态 操作，仅做了一个保存回调函数的操作

```js
        if (this.PromiseState === 'pending') {
            this.callbacks.push({onResolved, onRejected})
        }
```

我们需要修改一下`pending`状态下回调的代码

```js
        if (this.PromiseState === 'pending') {
            this.callbacks.push({
                onResolved: function() {
                    console.log('success1')
                },
                onRejected: function () {

                }
            })
        }
```

验证下`onResoved`函数在回调执行的时候，的确是被调用了：

![image-20220508191218611](image-20220508191218611.png)

我们真正要做的，是要执行成功的回调函数（注意`this`的指向问题）

```js
Promise.prototype.then = function (onResolved, onRejected) {

    const self = this
    return new Promise((resolve, reject) => {
        if (this.PromiseState === 'fulfilled') {

            // 使用try catch进行包裹处理
            try {
            	let result = onResolved(this.PromiseResult)
                
                if (result instanceof Promise) {
                    result.then(v => {
                        resolve(v)
                    }, r => {
                        reject(r)
                    })
                } else {
                    resolve(result)
                }
            } catch(e) {
                reject(e)
            }

        }

        if (this.PromiseState === 'rejected') {
            let result = onRejected(this.PromiseResult)
        }

        if (this.PromiseState === 'pending') {
            this.callbacks.push({
                onResolved: function() {
                    // 异步任务的pendding状态下，先调用成功的回调函数
                    onResolved(self.PromiseResult)
                },
                onRejected: function () {
                    onRejected(self.PromiseResult)
                }
            })
        }
    })
}

```



但此时返回的`Promise`对象的状态仍然是`pending`

![image-20220508191813723](image-20220508191813723.png)

和上一小节类似，要根据函数的执行结果来决定状态

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null
    this.callbacks = []
    const self = this

    function resolve(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data

        self.callbacks.forEach(item => {
            item.onResolved(data)
        })
    }

    function reject(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data

        self.callbacks.forEach(item => {
            item.onRejected(data)
        })
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {

    const self = this
    return new Promise((resolve, reject) => {
        if (this.PromiseState === 'fulfilled') {

            // 使用try catch进行包裹处理
            try {
            	let result = onResolved(this.PromiseResult)
                if (result instanceof Promise) {
                    result.then(v => {
                        resolve(v)
                    }, r => {
                        reject(r)
                    })
                } else {
                    resolve(result)
                }
            } catch(e) {
                reject(e)
            }

        }

        if (this.PromiseState === 'rejected') {
            let result = onRejected(this.PromiseResult)
        }

        if (this.PromiseState === 'pending') {
            this.callbacks.push({
                onResolved: function() {
                    // 异步任务的pendding状态下，先调用成功的回调函数
                    let result = onResolved(self.PromiseResult)
                    // 根据回调函数的执行结果来决定状态
                    if (result instanceof Promise) {
                        result.then(v => {
                            resolve(v)
                        }, r => {
                            reject(r)
                        })
                    } else {
                        resolve(result)
                    }
                },
                onRejected: function () {
                    onRejected(self.PromiseResult)
                }
            })
        }
    })
}


```

我们在`then`方法成功的回调函数中，返回一个值

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
		 // 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				// 使用定时器模拟异步任务
				setTimeout(() => {
					resolve('OK')
				}, 1000)
			})


			const res = p.then(value => {
				return 'on Yeah'
			}, reason =>{
				console.log(reason)
			})

			console.log(res)


		</script>
	</body>
</html>

```

打印结果如下：

![image-20220509064236748](image-20220509064236748.png)

完善一下`onRejected`，同时做一下异常处理

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null
    this.callbacks = []
    const self = this

    function resolve(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data

        self.callbacks.forEach(item => {
            item.onResolved(data)
        })
    }

    function reject(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data

        self.callbacks.forEach(item => {
            item.onRejected(data)
        })
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {

    const self = this
    return new Promise((resolve, reject) => {
        if (this.PromiseState === 'fulfilled') {

            // 使用try catch进行包裹处理
            try {
            	let result = onResolved(this.PromiseResult)
                
                if (result instanceof Promise) {
                    result.then(v => {
                        resolve(v)
                    }, r => {
                        reject(r)
                    })
                } else {
                    resolve(result)
                }
            } catch (e) {
                reject(e)
            }

        }

        if (this.PromiseState === 'rejected') {
            let result = onRejected(this.PromiseResult)
        }

        if (this.PromiseState === 'pending') {
            this.callbacks.push({
                onResolved: function () {
                    // 处理抛出的异常
                    try {
                        // 异步任务的pendding状态下，先调用成功的回调函数
                        let result = onResolved(self.PromiseResult)
                        // 根据回调函数的执行结果来决定状态
                        if (result instanceof Promise) {
                            result.then(v => {
                                resolve(v)
                            }, r => {
                                reject(r)
                            })
                        } else {
                            resolve(result)
                        }
                    } catch (e) {
                        reject(e)
                    }
                },
                onRejected: function () {
                    try {
                        let result = onRejected(self.PromiseResult)
                        // 根据回调函数的执行结果来决定状态
                        if (result instanceof Promise) {
                            result.then(v => {
                                resolve(v)
                            }, r => {
                                reject(r)
                            })
                        } else {
                            resolve(result) // 这里不需要改成reject(result)
                        }
                    } catch (e) {
                        reject(e)
                    }
                }
            })
        }
    })
}


```

## 3.11.`then`方法的完善与优化

- 对`rejected`状态情况进行完善

  ```js
  function Promise(executor) {
  
      this.PromiseState = 'pending'
      this.PromiseResult = null
      this.callbacks = []
      const self = this
  
      function resolve(data) {
          if (self.PromiseState !== 'pending') return
          self.PromiseState = 'fulfilled'
          self.PromiseResult = data
  
          self.callbacks.forEach(item => {
              item.onResolved(data)
          })
      }
  
      function reject(data) {
          if (self.PromiseState !== 'pending') return
          self.PromiseState = 'rejected'
          self.PromiseResult = data
  
          self.callbacks.forEach(item => {
              item.onRejected(data)
          })
      }
  
      try {
          executor(resolve, reject)
      } catch (e) {
          reject(e)
      }
  }
  
  Promise.prototype.then = function (onResolved, onRejected) {
  
      const self = this
      return new Promise((resolve, reject) => {
          if (this.PromiseState === 'fulfilled') {
              let result = onResolved(this.PromiseResult)
  
              // 使用try catch进行包裹处理
              try {
                  if (result instanceof Promise) {
                      result.then(v => {
                          resolve(v)
                      }, r => {
                          reject(r)
                      })
                  } else {
                      resolve(result)
                  }
              } catch (e) {
                  reject(e)
              }
  
          }
  
          if (this.PromiseState === 'rejected') {
              try {
                  // 对rejected的情况进行完善
                  let result = onRejected(this.PromiseResult)
                  if (result instanceof Promise) {
                      result.then(v => {
                          resolve(v)
                      }, r=> {
                          reject(r)
                      })
                  } else {
                      resolve(result)
                  }
  
              } catch (e) {
                  reject(e)
              }
          }
  
          if (this.PromiseState === 'pending') {
              this.callbacks.push({
                  onResolved: function () {
                      // 处理抛出的异常
                      try {
                          // 异步任务的pendding状态下，先调用成功的回调函数
                          let result = onResolved(self.PromiseResult)
                          // 根据回调函数的执行结果来决定状态
                          if (result instanceof Promise) {
                              result.then(v => {
                                  resolve(v)
                              }, r => {
                                  reject(r)
                              })
                          } else {
                              resolve(result)
                          }
                      } catch (e) {
                          reject(e)
                      }
                  },
                  onRejected: function () {
                      try {
                          let result = onRejected(self.PromiseResult)
                          // 根据回调函数的执行结果来决定状态
                          if (result instanceof Promise) {
                              result.then(v => {
                                  resolve(v)
                              }, r => {
                                  reject(r)
                              })
                          } else {
                              resolve(result) // 这里不需要改成reject(result)
                          }
                      } catch (e) {
                          reject(e)
                      }
                  }
              })
          }
      })
  }
  
  
  ```

- 重复代码的封装

  ```js
  function Promise(executor) {
  
      this.PromiseState = 'pending'
      this.PromiseResult = null
      this.callbacks = []
      const self = this
  
      function resolve(data) {
          if (self.PromiseState !== 'pending') return
          self.PromiseState = 'fulfilled'
          self.PromiseResult = data
  
          self.callbacks.forEach(item => {
              item.onResolved(data)
          })
      }
  
      function reject(data) {
          if (self.PromiseState !== 'pending') return
          self.PromiseState = 'rejected'
          self.PromiseResult = data
  
          self.callbacks.forEach(item => {
              item.onRejected(data)
          })
      }
  
      try {
          executor(resolve, reject)
      } catch (e) {
          reject(e)
      }
  }
  
  Promise.prototype.then = function (onResolved, onRejected) {
  
      const self = this
      return new Promise((resolve, reject) => {
          // 封装函数，注意内部this的指向问题
          function callback(type) {
              // 使用try catch进行包裹处理
              try {
                  let result = type(self.PromiseResult) // 封装复制的时候，result的定义要放在try的后面
                  if (result instanceof Promise) {
                      result.then(v => {
                          resolve(v)
                      }, r => {
                          reject(r)
                      })
                  } else {
                      resolve(result)
                  }
              } catch (e) {
                  reject(e)
              }
          }
  
          if (this.PromiseState === 'fulfilled') {
              callback(onResolved)
          }
  
          if (this.PromiseState === 'rejected') {
              callback(onRejected)
          }
  
          if (this.PromiseState === 'pending') {
              this.callbacks.push({
                  onResolved: function () {
                      callback(onResolved)
                  },
                  onRejected: function () {
                      callback(onRejected)
                  }
              })
          }
      })
  }
  
  
  ```

## 3.12.`catch`方法异常穿透与传值

`index.html`

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
			// 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				setTimeout(() => {
					reject('Error')
				}, 1000)
			})

			p.catch(reason => {
				console.warn(reason)
			})
		</script>
	</body>
</html>

```

此时会报错：

![image-20220509092748130](image-20220509092748130.png)

因为我们自定义的代码中，还没有添加`catch`方法

添加`catch`：我们在内部调用`then`方法即可

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null
    this.callbacks = []
    const self = this

    function resolve(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data

        self.callbacks.forEach(item => {
            item.onResolved(data)
        })
    }

    function reject(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data

        self.callbacks.forEach(item => {
            item.onRejected(data)
        })
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {

    const self = this
    return new Promise((resolve, reject) => {
        // 封装函数，注意内部this的指向问题
        function callback(type) {
            // 使用try catch进行包裹处理
            try {
                let result = type(self.PromiseResult) // 封装复制的时候要仔细点，result的定义不要放在try的外面
                if (result instanceof Promise) {
                    result.then(v => {
                        resolve(v)
                    }, r => {
                        reject(r)
                    })
                } else {
                    resolve(result)
                }
            } catch (e) {
                reject(e)
            }
        }

        if (this.PromiseState === 'fulfilled') {
            callback(onResolved)
        }

        if (this.PromiseState === 'rejected') {
            callback(onRejected)
        }

        if (this.PromiseState === 'pending') {
            this.callbacks.push({
                onResolved: function () {
                    callback(onResolved)
                },
                onRejected: function () {
                    callback(onRejected)
                }
            })
        }
    })
}

// 添加catch方法
Promise.prototype.catch = function(onRejected) {
    return this.then(undefined, onRejected)
}


```

`catch`方法返回的也是`Promise`对象

`index.html`

```html

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
			// 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				setTimeout(() => {
					reject('Error')
				}, 1000)
			})

			const res = p.catch(reason => {
				console.warn(reason)
			})
			
			console.log(res)
		</script>
	</body>
</html>

```

打印结果如下：

![image-20220509093323199](image-20220509093323199.png)

我们还需要实现`异常穿透`的功能

`index.html`

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
			// 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				setTimeout(() => {
					reject('Error')
				}, 1000)
			})

			p.then(value => {
				console.log(111)
			}).then(value => {
				console.log(222)
			}).then(value => {
				console.log(333)
			}).catch(reason =>{
				console.warn(reason)
			})
			
		</script>
	</body>
</html>

```

打印结果如下：

![image-20220509111212379](image-20220509111212379.png)

原因：

代码执行到`then`之前的时候，对象`p`是一个`pending`的状态，代码中我们把两个回调存起来了：

```js
        if (this.PromiseState === 'pending') {
            this.callbacks.push({
                onResolved: function () {
                    callback(onResolved)
                },
                onRejected: function () {
                    callback(onRejected)
                }
            })
        }
```



但此时，成功的回调是有的，失败的回调我们没写，所以是一个`undefined`，当状态改变完之后，一定会调用回调：

```js
        self.callbacks.forEach(item => {
            item.onRejected(data)
        })
```

而这个`item`里面，只有成功的回调，而没有失败的回调。实际调用的是就是`undefined`，就有问题了

所以我们在封装时，要允许`then`方法不传第二个回调函数，`then`方法在`return`之前，需要对`onRejected`的回调做一下判断

```js
Promise.prototype.then = function (onResolved, onRejected) {

    const self = this
    // 判断回调函数参数
    if(typeof onRejected !== 'function') {
        onRejected = reason => {
        	throw reason
        }
    }

    return new Promise((resolve, reject) => {
        function callback(type) {
            let result = type(self.PromiseResult)

            try {
                if (result instanceof Promise) {
                    result.then(v => {
                        resolve(v)
                    }, r => {
                        reject(r)
                    })
                } else {
                    resolve(result)
                }
            } catch (e) {
                reject(e)
            }
        }

        if (this.PromiseState === 'fulfilled') {
            callback(onResolved)
        }

        if (this.PromiseState === 'rejected') {
            callback(onRejected)
        }

        if (this.PromiseState === 'pending') {
            this.callbacks.push({
                onResolved: function () {
                    callback(onResolved)
                },
                onRejected: function () {
                    callback(onRejected)
                }
            })
        }
    })
}

```

当没有失败的回调时，我们自定义一个默认的回调，这个默认的回调中，抛出了异常的结果值。

这样当链式调用`then`方法，就相当于如下情况

```html
			p.then(value => {
				console.log(111)
			}, reason => {
				throw reason // 没有指定失败的回调时，相当于这种情况
			}).then(value => {
				console.log(222)
			}).then(value => {
				console.log(333)
			}).catch(reason =>{
				console.warn(reason)
			})
```

然后在`then`方法中一直抛，直到遇到`catch`方法，可以将异常处理掉

```js
Promise.prototype.catch = function(onRejected) {
    return this.then(undefined, onRejected)
}
```

打印结果如下：

![image-20220509111309652](image-20220509111309652.png)



如果异常是发生在链式调用的中间，也是可以实现异常穿透的

`index.html`

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
			// 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				setTimeout(() => {
					resolve('OK')
				}, 1000)
			})

			p.then(value => {
				console.log(111)
				throw 'error1'
			}).then(value => {
				console.log(222)
			}).then(value => {
				console.log(333)
			}).catch(reason =>{
				console.warn(reason)
			})
			
		</script>
	</body>
</html>

```

打印效果如下：

![image-20220509111552710](image-20220509111552710.png)



除了可以进行异常穿透外，还有一个特性就是`值传递`

即如下代码，也是可以可以正常的执行的

`index.html`

```html
	<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
			// 覆盖原来的Promise
		</script>
		<script>
			let p = new Promise((resolve, reject) => {
				setTimeout(() => {
					resolve('OK')
				}, 1000)
			})

			p.then()
			.then(value => {
				console.log(222)
			}).then(value => {
				console.log(333)
			}).catch(reason =>{
				console.warn(reason)
			})
			
		</script>
	</body>
</html>

```

但我们自定义的是不行的，打印结果如下：

![image-20220509111907939](image-20220509111907939.png)

原因和上面一样，所以我们也要指定默认的成功回调函数

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null
    this.callbacks = []
    const self = this

    function resolve(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data

        self.callbacks.forEach(item => {
            item.onResolved(data)
        })
    }

    function reject(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data

        self.callbacks.forEach(item => {
            item.onRejected(data)
        })
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {

    const self = this
    // 判断是否传递了第一个参数
    if(typeof onResolved !== 'function') {
        onResolved = value => value
    }

    if(typeof onRejected !== 'function') {
        onRejected = reason => {
        	throw reason
        }
    }
    return new Promise((resolve, reject) => {

        function callback(type) {

            try {
                let result = type(self.PromiseResult)
                if (result instanceof Promise) {
                    result.then(v => {
                        resolve(v)
                    }, r => {
                        reject(r)
                    })
                } else {
                    resolve(result)
                }
            } catch (e) {
                reject(e)
            }
        }

        if (this.PromiseState === 'fulfilled') {
            callback(onResolved)
        }

        if (this.PromiseState === 'rejected') {
            callback(onRejected)
        }

        if (this.PromiseState === 'pending') {
            this.callbacks.push({
                onResolved: function () {
                    callback(onResolved)
                },
                onRejected: function () {
                    callback(onRejected)
                }
            })
        }
    })
}

Promise.prototype.catch = function(onRejected) {
    return this.then(undefined, onRejected)
}


```



打印结果正常：

![image-20220509112146200](image-20220509112146200.png)



## 3.13.封装`resolve`方法

`index.html`

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
			// 覆盖原来的Promise
		</script>
		<script>
			const p = Promise.resolve('OK')
			
			console.log(p)
		</script>
	</body>
</html>

```

报错：

![image-20220509112536084](image-20220509112536084.png)

因为我们自定义的代码还没有添加呢

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null
    this.callbacks = []
    const self = this

    function resolve(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data

        self.callbacks.forEach(item => {
            item.onResolved(data)
        })
    }

    function reject(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data

        self.callbacks.forEach(item => {
            item.onRejected(data)
        })
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {

    const self = this

    if(typeof onResolved !== 'function') {
        onResolved = value => value
    }

    if(typeof onRejected !== 'function') {
        onRejected = reason => {
        	throw reason
        }
    }
    return new Promise((resolve, reject) => {

        function callback(type) {

            try {
                let result = type(self.PromiseResult)
                if (result instanceof Promise) {
                    result.then(v => {
                        resolve(v)
                    }, r => {
                        reject(r)
                    })
                } else {
                    resolve(result)
                }
            } catch (e) {
                reject(e)
            }
        }

        if (this.PromiseState === 'fulfilled') {
            callback(onResolved)
        }

        if (this.PromiseState === 'rejected') {
            callback(onRejected)
        }

        if (this.PromiseState === 'pending') {
            this.callbacks.push({
                onResolved: function () {
                    callback(onResolved)
                },
                onRejected: function () {
                    callback(onRejected)
                }
            })
        }
    })
}

Promise.prototype.catch = function(onRejected) {
    return this.then(undefined, onRejected)
}

// 添加resolve方法，注意，这个方式是属于Promise函数对象的，而不属于实例对象，所以需要注意下声明方式
Promise.resolve = function(value) {
    return new Promise((resolve, reject) => {
    
    })
}

```

测试一下结果，返回的结果的确是一个`Promise`对象

![image-20220509112928325](image-20220509112928325.png)



接下来我们根据传入的`value`来更改状态

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null
    this.callbacks = []
    const self = this

    function resolve(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data

        self.callbacks.forEach(item => {
            item.onResolved(data)
        })
    }

    function reject(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data

        self.callbacks.forEach(item => {
            item.onRejected(data)
        })
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {

    const self = this

    if(typeof onResolved !== 'function') {
        onResolved = value => value
    }

    if(typeof onRejected !== 'function') {
        onRejected = reason => {
        	throw reason
        }
    }
    return new Promise((resolve, reject) => {

        function callback(type) {

            try {
                let result = type(self.PromiseResult)
                if (result instanceof Promise) {
                    result.then(v => {
                        resolve(v)
                    }, r => {
                        reject(r)
                    })
                } else {
                    resolve(result)
                }
            } catch (e) {
                reject(e)
            }
        }

        if (this.PromiseState === 'fulfilled') {
            callback(onResolved)
        }

        if (this.PromiseState === 'rejected') {
            callback(onRejected)
        }

        if (this.PromiseState === 'pending') {
            this.callbacks.push({
                onResolved: function () {
                    callback(onResolved)
                },
                onRejected: function () {
                    callback(onRejected)
                }
            })
        }
    })
}

Promise.prototype.catch = function(onRejected) {
    return this.then(undefined, onRejected)
}


Promise.resolve = function(value) {
    return new Promise((resolve, reject) => {
        // 根据传入的value来更改状态
        if(value instanceof Promise) {
            value.then(v => {
                resolve(v)
            }, r => {
                reject(r)
            })
        } else {
            // 状态设置为成功
            resolve(value)
        }
    })
}

```

此时打印结果的状态，不再是`pending`了，并且当传入的`value`是一个`Promise`对象时，也是正常的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
			// 覆盖原来的Promise
		</script>
		<script>
			const p = Promise.resolve(new Promise((resolve, reject) => {
				reject('Error')
			}))
			
			console.log(p)
		</script>
	</body>
</html>

```

打印结果如下：

![image-20220509113539319](image-20220509113539319.png)

`resolve`的嵌套调用也是支持的

```html
	<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
			// 覆盖原来的Promise
		</script>
		<script>
			const p = Promise.resolve(Promise.resolve('Oh Yeah'))
			console.log(p)
		</script>
	</body>
</html>

```

![image-20220509113805342](image-20220509113805342.png)

## 3.14.封装`reject`方法

类似`resovle`方法的封装

```js
// ...

Promise.reject = function(reason) {
    return new Promise((resolve, reject) => {
        // 始终返回失败的Promise对象
        reject(reason)
    })
}
```

测试效果：

```html	
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
			// 覆盖原来的Promise
		</script>
		<script>
			const p = Promise.reject(Promise.reject('Oh Yeah'))
			console.log(p)
		</script>
	</body>
</html>

```

![image-20220509140815749](image-20220509140815749.png)



## 3.15.封装`all`方法

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
			// 覆盖原来的Promise
		</script>
		<script>
			let p1 = new Promise((resolve, reject) =>{
				setTimeout(() => {
					resolve('OK')
				}, 1000)
			})
			
			let p2 = Promise.resolve('Success')
			let p3 = Promise.resolve('Oh Yeah')
			
			let res = Promise.all([p1, p2, p3])
			console.log(res)
		</script>
	</body>
</html>

```

此时我们的`all`方法还没有定义，定义`all`方法：

```js
// ...

Promise.all = function(promises) {
    return new Promise((resolve, reject) => {
        // 声明变量
        let count = 0
        let arr = []

        //遍历
        for(let i = 0; i < promises.length; i++) {
            // 拿到每个promise对象
            promises[i].then(v => {
                // 得知每个Promise对象的状态都是成功
                count++
                arr[i] = v // 不能用push，否则传入的如果有异步任务的话，结果的下标会对不上
                // 判断是否都成功了
                if(count === promises.length) {
                    // 全部成功了才修改状态
                    resolve(arr)
                }
            }, r => {
                // 只要有一个失败了，就返回失败
                reject(r)
            })
        }
    })
}
```

此时看下打印结果：

![image-20220509143452356](image-20220509143452356.png)

## 3.16.封装`race`方法

新增`race`方法

```js

// ...
Promise.race = function(promises) {
    return new Promise((resolve, reject) => {
        for(let i = 0; i < promises.length; i++) {
            promises[i].then(v => {
                // 只要有一个成功，就返回成功
                resolve(v)
            }, r => {
                // 只要有一个失败了，就返回失败
                reject(r)
            })
        }
    })
}
```

测试：

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise.js">
			// 覆盖原来的Promise
		</script>
		<script>
			let p1 = new Promise((resolve, reject) =>{
				setTimeout(() => {
					resolve('OK')
				}, 1000)
			})
			
			let p2 = Promise.resolve('Success')
			let p3 = Promise.resolve('Oh Yeah')
			
			let res = Promise.race([p1, p2, p3])
			console.log(res)
		</script>
	</body>
</html>

```

结果：

![image-20220509144308120](image-20220509144308120.png)

对象`p2`先执行完，就先返回`p2`



## 3.17.`then`方法回调函数异步执行

原生实现：

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
<!-- 		<script src="./promise.js">
			// 覆盖原来的Promise
		</script> -->
		<script>
			let p1 = new Promise((resolve, reject) =>{
				resolve('OK')
				console.log(111)
			})
			
			p1.then(value => {
				console.log(222)
			})
			
			console.log(333)
		</script>
	</body>
</html>

```

打印结果：

![image-20220509144926549](image-20220509144926549.png)

自定义实现打印结果：

![image-20220509144953671](image-20220509144953671.png)

`then`方法的回调应该是异步执行的，我们给对应执行的代码添加定时器：

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null
    this.callbacks = []
    const self = this

    function resolve(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data

        // 这里的回调函数也应该是异步执行的（我们这里只是模拟，实际是在微队列中的，但我们放在宏队列中）
        setTimeout(() => {
            self.callbacks.forEach(item => {
                item.onResolved(data)
            })
        })

    }

    function reject(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data
        
        // 这里的回调函数也应该是异步执行的
        setTimeout(() => {
            self.callbacks.forEach(item => {
                item.onRejected(data)
            })
        })
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}
// ...
```

此时的结果在表现上，就和原生的一样了：

![image-20220509145555260](image-20220509145555260.png)

## 3.18.`Promise`完整实现

```js
function Promise(executor) {

    this.PromiseState = 'pending'
    this.PromiseResult = null
    this.callbacks = []
    const self = this

    function resolve(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'fulfilled'
        self.PromiseResult = data

        // 这里的回调函数也应该是异步执行的
        setTimeout(() => {
            self.callbacks.forEach(item => {
                item.onResolved(data)
            })
        })

    }

    function reject(data) {
        if (self.PromiseState !== 'pending') return
        self.PromiseState = 'rejected'
        self.PromiseResult = data

        // 这里的回调函数也应该是异步执行的
        setTimeout(() => {
            self.callbacks.forEach(item => {
                item.onRejected(data)
            })
        })
    }

    try {
        executor(resolve, reject)
    } catch (e) {
        reject(e)
    }
}

Promise.prototype.then = function (onResolved, onRejected) {

    const self = this
    if(typeof onResolved !== 'function') {
        onResolved = value => value
    }

    if(typeof onRejected !== 'function') {
        onRejected = reason => {
        	throw reason
        }
    }
    return new Promise((resolve, reject) => {

        function callback(type) {

            try {
                let result = type(self.PromiseResult)
                if (result instanceof Promise) {
                    result.then(v => {
                        resolve(v)
                    }, r => {
                        reject(r)
                    })
                } else {
                    resolve(result)
                }
            } catch (e) {
                reject(e)
            }
        }

        if (this.PromiseState === 'fulfilled') {
            // 使用定时器包裹，使得回调函数的执行变成异步
            setTimeout(() => {
                callback(onResolved)
            })
        }

        if (this.PromiseState === 'rejected') {
            // 使用定时器包裹，使得回调函数的执行变成异步
            setTimeout(() => {
                callback(onRejected)
            })
        }

        if (this.PromiseState === 'pending') {
            this.callbacks.push({
                onResolved: function () {
                    callback(onResolved)
                },
                onRejected: function () {
                    callback(onRejected)
                }
            })
        }
    })
}

Promise.prototype.catch = function(onRejected) {
    return this.then(undefined, onRejected)
}


Promise.resolve = function(value) {
    return new Promise((resolve, reject) => {
        if(value instanceof Promise) {
            value.then(v => {
                resolve(v)
            }, r => {
                reject(r)
            })
        } else {
            // 状态设置为成功
            resolve(value)
        }
    })
}

Promise.reject = function(reason) {
    return new Promise((resolve, reject) => {
        // 始终返回失败的Promise对象
        reject(reason)
    })
}

Promise.all = function(promises) {
    return new Promise((resolve, reject) => {
        // 声明变量
        let count = 0
        let arr = []

        //遍历
        for(let i = 0; i < promises.length; i++) {
            // 拿到每个promise对象
            promises[i].then(v => {
                // 得知每个Promise对象的状态都是成功
                count ++
                arr[i] = v // 不能用push，否则传入的如果有异步任务的话，结果的下标会对不上
                // 判断是否都成功了
                if(count === promises.length) {
                    // 全部成功了才修改状态
                    resolve(arr)
                }
            }, r => {
                // 只要有一个失败了，就返回失败
                reject(r)
            })
        }
    })
}

Promise.race = function(promises) {
    return new Promise((resolve, reject) => {
        for(let i = 0; i < promises.length; i++) {
            promises[i].then(v => {
                // 只要有一个成功，就返回成功
                resolve(v)
            }, r => {
                // 只要有一个失败了，就返回失败
                reject(r)
            })
        }
    })
}
```



## 3.19.`class`版本的实现

`promise_class.js`

```js
class Promise {
    // 构造方法
    constructor(executor) {
        this.PromiseState = 'pending'
        this.PromiseResult = null
        this.callbacks = []
        const self = this

        function resolve(data) {
            if (self.PromiseState !== 'pending') return
            self.PromiseState = 'fulfilled'
            self.PromiseResult = data

            // 这里的回调函数也应该是异步执行的
            setTimeout(() => {
                self.callbacks.forEach(item => {
                    item.onResolved(data)
                })
            })

        }

        function reject(data) {
            if (self.PromiseState !== 'pending') return
            self.PromiseState = 'rejected'
            self.PromiseResult = data

            // 这里的回调函数也应该是异步执行的
            setTimeout(() => {
                self.callbacks.forEach(item => {
                    item.onRejected(data)
                })
            })
        }

        try {
            executor(resolve, reject)
        } catch (e) {
            reject(e)
        }
    }

    // then方法
    then(onResolved, onRejected) {

        const self = this
        if(typeof onResolved !== 'function') {
            onResolved = value => value
        }

        if(typeof onRejected !== 'function') {
            onRejected = reason => {
                throw reason
            }
        }
        return new Promise((resolve, reject) => {

            function callback(type) {

                try {
                    let result = type(self.PromiseResult)
                    if (result instanceof Promise) {
                        result.then(v => {
                            resolve(v)
                        }, r => {
                            reject(r)
                        })
                    } else {
                        resolve(result)
                    }
                } catch (e) {
                    reject(e)
                }
            }

            if (this.PromiseState === 'fulfilled') {
                // 使用定时器包裹，使得回调函数的执行变成异步
                setTimeout(() => {
                    callback(onResolved)
                })
            }

            if (this.PromiseState === 'rejected') {
                // 使用定时器包裹，使得回调函数的执行变成异步
                setTimeout(() => {
                    callback(onRejected)
                })
            }

            if (this.PromiseState === 'pending') {
                this.callbacks.push({
                    onResolved: function () {
                        callback(onResolved)
                    },
                    onRejected: function () {
                        callback(onRejected)
                    }
                })
            }
        })
    }

    // catch方法
    catch(onRejected) {
        return this.then(undefined, onRejected)
    }

    // resolve方法，使用static声明，表明属于类，不属于对象
    static resolve(value) {
        return new Promise((resolve, reject) => {
            if(value instanceof Promise) {
                value.then(v => {
                    resolve(v)
                }, r => {
                    reject(r)
                })
            } else {
                // 状态设置为成功
                resolve(value)
            }
        })
    }

    // reject方法
    static reject(reason) {
    return new Promise((resolve, reject) => {
        reject(reason)
    })
}

    // all方法
    static all(promises) {
        return new Promise((resolve, reject) => {
            // 声明变量
            let count = 0
            let arr = []

            //遍历
            for(let i = 0; i < promises.length; i++) {
                // 拿到每个promise对象
                promises[i].then(v => {
                    // 得知每个Promise对象的状态都是成功
                    count ++
                    arr[i] = v // 不能用push，否则传入的如果有异步任务的话，结果的下标会对不上
                    // 判断是否都成功了
                    if(count === promises.length) {
                        // 全部成功了才修改状态
                        resolve(arr)
                    }
                }, r => {
                    // 只要有一个失败了，就返回失败
                    reject(r)
                })
            }
        })
    }

    // race方法
    static race(promises) {
        return new Promise((resolve, reject) => {
            for(let i = 0; i < promises.length; i++) {
                promises[i].then(v => {
                    // 只要有一个成功，就返回成功
                    resolve(v)
                }, r => {
                    // 只要有一个失败了，就返回失败
                    reject(r)
                })
            }
        })
    }

}
```

调用测试一下：

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="./promise_class.js">
			// 覆盖原来的Promise
		</script>
		<script>
			let p1 = new Promise((resolve, reject) =>{
				resolve('OK')
				console.log(111)
			})
			
			const res = p1.then(value => {
				console.log(222)
			})
			
			console.log(333)
			console.log(res)
		</script>
	</body>
</html>

```

结果正常

![image-20220509150814524](image-20220509150814524.png)

# 4.`async`与`await`

## 4.1.`mdn`文档

[async function - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)

[await - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)

## 4.2.`async`函数

- 函数的返回值为一个`Promise`对象

  ```html
  <!DOCTYPE html>
  <html>
  	<head>
  		<meta charset="utf-8">
  		<title></title>
  	</head>
  	<body>
  		<script>
  			async function main() {
  				
  			}
  			
  			let result = main()
  			
  			console.log(result)
  		</script>
  	</body>
  </html>
  
  ```

  ![image-20220509151517827](image-20220509151517827.png)

- `Promise`对象的结果由`async`函数执行的返回值决定

  - 如果返回值是一个非`Promise`类型的数据：

    - 最终的返回结果就是你返回的那个值，
    - 最终返回的状态时为成功

    ```html
    <!DOCTYPE html>
    <html>
    	<head>
    		<meta charset="utf-8">
    		<title></title>
    	</head>
    	<body>
    		<script>
    			async function main() {
    				return 'OK'
    			}
    			
    			let result = main()
    			
    			console.log(result)
    		</script>
    	</body>
    </html>
    
    ```

    ![image-20220509151830769](image-20220509151830769.png)

    

  - 如果返回值是一个`Promise`类型的对象，最终`async`函数的返回结果和该`Promise`对象返回的结果一致

    ```html	
    <!DOCTYPE html>
    <html>
    	<head>
    		<meta charset="utf-8">
    		<title></title>
    	</head>
    	<body>
    		<script>
    			async function main() {
    				return new Promise((resolve, reject) => {
    					resolve('Success')
    				})
    			}
    			
    			let result = main()
    			
    			console.log(result)
    		</script>
    	</body>
    </html>
    
    ```

    ![image-20220509152329281](image-20220509152329281.png)

  - 如果抛出了异常，最终返回的结果就是一个失败的`Promise`对象，结果值就是抛出的结果值

    ```html
    <!DOCTYPE html>
    <html>
    	<head>
    		<meta charset="utf-8">
    		<title></title>
    	</head>
    	<body>
    		<script>
    			async function main() {
    				throw 'Oh NO'
    			}
    			
    			let result = main()
    			
    			console.log(result)
    		</script>
    	</body>
    </html>
    
    ```

    ![image-20220509152606932](image-20220509152606932.png)

    报错是因为我们没有`catch`处理异常

- 这个规则，和`then`方法中成功状态回调函数的返回规则是一样的

## 4.3.`await`表达式

- `await`右侧的表达式一般为`Promise`对象，但也可以是其它的值

  - 如果表达式是`Promise`对象，`await`返回的是`Promsie`成功的值

    
  
    ```html
    <!DOCTYPE html>
    <html>
    	<head>
    		<meta charset="utf-8">
    		<title></title>
    	</head>
    	<body>
    		<script>
    			async function main() {
    				let p = new Promise((resolve, reject) => {
    					resolve('OK')
    				})
    				
    				// 右侧为promise的情况
    				let res = await p
    				console.log(res)
    			}
    			
    			main()
    		</script>
    	</body>
    </html>
    
    ```

    ![image-20220509153639670](image-20220509153639670.png)

  - 如果表达式是其它的值，直接将此值作为`await`的返回值
  
    ```html
    <!DOCTYPE html>
    <html>
    	<head>
    		<meta charset="utf-8">
    		<title></title>
    	</head>
    	<body>
    		<script>
    			async function main() {
    				let p = new Promise((resolve, reject) => {
    					resolve('OK')
    				})
    				
    				// 右侧为其他类型的数据
    				let res = await 100
    				console.log(res)
    			}
    			
    			main()
    		</script>
    	</body>
    </html>
    
    ```
  
    ![image-20220509153803614](image-20220509153803614.png)



## 4.4.注意

- `await`必须写在`async`函数中，但`async`函数中可以没有`await`

  ```html
  <!DOCTYPE html>
  <html>
  	<head>
  		<meta charset="utf-8">
  		<title></title>
  	</head>
  	<body>
  		<script>
  			await 100
  		</script>
  	</body>
  </html>
  
  ```

  ![image-20220509153325682](image-20220509153325682.png)

- 如果`await`的`Promise`对象失败了，就会抛出异常，需要使用`try catch`捕获处理

  ```html
  <!DOCTYPE html>
  <html>
  	<head>
  		<meta charset="utf-8">
  		<title></title>
  	</head>
  	<body>
  		<script>
  			async function main() {
  				let p = new Promise((resolve, reject) => {
  					reject('Error')
  				})
  				
  				// 如果Promise状态为失败，需要使用try catch来捕获异常
  				try {
  					let res = await p
  				} catch(e) {
  					console.log(e)
  				}
  			}
  			
  			main()
  		</script>
  	</body>
  </html>
  
  ```

  ![image-20220509154001990](image-20220509154001990.png)

## 4.5.`async`和`await`结合实践

需求：读取三个文件的内容，拼接后输出

`1.html`

```
行宫
元稹 〔唐代〕
```

`2.html`

```
寥落古行宫，宫花寂寞红。
```

`3.html`

```
白头宫女在，闲坐说玄宗。
```



- 纯回调函数实现

  ```js
  const fs = require('fs')
  
  fs.readFile('./resource/1.html', (err, data1) => {
      if(err) throw err
      fs.readFile('./resource/2.html', (err, data2) => {
          if(err) throw err
          fs.readFile('./resource/3.html', (err, data3) => {
              console.log(data1 + data2 + data3)
          })
      })
  })
  ```

- `async + await` 实现

  ```js
  const fs = require('fs')
  const util = require('util')
  const myReadFile = util.promisify(fs.readFile)
  
  async function main() {
      try {
          let data1 = await myReadFile('./resource/1.html')
          let data2 = await myReadFile('./resource/2.html')
          let data3 = await myReadFile('./resource/3.html')
          console.log(data1 + data2 + data3)
      } catch(e) {
          console.log(e)
      }
  }
  
  main()
  ```

  首先不需要写那么的回调函数，并且也不需要每一层都对异常进行处理

  我们故意写错第一个路径，直接用`try catch`处理异常即可，处理异常的方式变得异常灵活

  ![image-20220509155633611](image-20220509155633611.png)

  我们在`async`和`await`的使用中是看不到回调函数的（在`Promise`里面是有的），写起来非常的简洁，就像写同步代码一样（内部的执行是异步的）

## 4.6.`async`和`await`结合发送`ajax`请求

需求：刷新下页面，就发送一次请求

拿到我们之前封装成`Promise`的发送`ajax`请求的方法，并使用`await`在`async`函数中发送请求

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script>
			// http://1.13.245.78/search/hitokoto
			function sendAJAX(url) {
				return new Promise((resolve, reject) => {
					const xhr = new XMLHttpRequest()
					xhr.responseType = 'json'
					xhr.open('GET', url)
					xhr.send()
					// 处理结果
					xhr.onreadystatechange = function() {
						if(xhr.readyState === 4) {
							if(xhr.status >= 200 && xhr.status < 300) {
								resolve(xhr.response)
							} else {
								reject(xhr.status)
							}
						}
					}
				})
			}
			async function main() {
				let info = await sendAJAX('http://1.13.245.78/search/hitokoto')
				console.log(info)
			}
			main()

		</script>
	</body>
</html>

```

结果：

![image-20220509160505152](image-20220509160505152.png)

封装成`Promise`对象后，代码的书写非常的简洁

并且，将网络请求封装成`Promise`对象，已经有现成的工具库了`Axios`，这是一个基于`Promise`的`Ajax`封装的包

使用`axios`发送请求时

```js
        async categoryList() {
            let res = await reqCategoryList()
            console.log(res)
        }
```



# 5.`JS`异步之宏队列与微队列

## 5.1.原理图

![image-20220510091152445](image-20220510091152445.png)

## 5.2.队列分类

`JS`中用来存储待执行回调函数的队列包含2个不同特定的队列

异步任务会放入队列中执行

- 宏队列
  - 用来保存待执行的宏任务（回调）
  - 回调函数的种类：
    - `dom`事件回调
    - `ajax`回调
    - 定时器回调
  - 放入宏队列中的回调函数称为宏任务
- 微队列
  - 用来保存待执行的微任务（回调）
  - 回调函数的种类：
    - `Promise`回调
    - `mutation`回调
      - 监视的是标签属性的改变
  - 放入微队列中的回调函数称为微任务

## 5.3.执行顺序

- `JS`执行时会区别这2个队列

  - `JS`引擎必须先执行所有的初始化同步任务代码
    - 同步代码还没执行完时，队列里是可以先有任务的，只不过不会执行
    - 只有将同步代码全部执行完之后，才会执行队列里面的回调函数

  - 再执行队列里的代码
    - 每次准备取出第一个宏任务执行前，都要将所有的微任务一个一个取出来执行

### 微任务相比较于宏任务，优先执行

```js
setTimeout(() => { // 会立即放入宏队列
    console.log('timeout callback()')
})

Promise.resolve('ok').then(
    value => { // 会立即放入微队列
        console.log('Promise onResolved()', value) // 微队列优先执行
    }
)
```

![image-20220510093251982](image-20220510093251982.png)

### 宏任务与微任务同级之间，是按次序执行的

```js
			setTimeout(() => { // 会立即放入宏队列
				console.log('timeout callback1()')
			})
			setTimeout(() => { // 会立即放入宏队列
				console.log('timeout callback2()')
			})
			
			Promise.resolve(1).then(
				value => { // 会立即放入微队列
					console.log('Promise onResolved1()', value)
				}
			)
			
			Promise.resolve(2).then(
				value => { // 会立即放入微队列
					console.log('Promise onResolved2()', value)
				}
			)
```

![image-20220510094316043](image-20220510094316043.png)

### 前置宏任务内部如果有微任务，后置宏任务会后执行

```js
setTimeout(() => { // 会立即放入宏队列
    console.log('timeout callback1()')
    Promise.resolve(3).then( // 前置宏任务内部又有一个微任务
        value => { // 会立即放入微队列
            console.log('Promise onResolved3()', value)
        }
    )
})
setTimeout(() => { // 会立即放入宏队列
    console.log('timeout callback2()') // 后置宏任务执行时，检查到微任务还有，优先执行微任务
})

Promise.resolve(1).then(
    value => { // 会立即放入微队列
        console.log('Promise onResolved1()', value)
    }
)

Promise.resolve(2).then(
    value => { // 会立即放入微队列
        console.log('Promise onResolved2()', value)
    }
)
```

![image-20220510095535726](image-20220510095535726.png)



## 5.4.`Promise`面试题

### 面试题一

```js
setTimeout(() => {
    console.log(1)
})
Promise.resolve().then(
    value => {
        console.log(2)
    }
)
Promise.resolve().then(
    value => {
        console.log(4)
    }
)
console.log(3)
```

![image-20220510100455204](image-20220510100455204.png)

### 面试题二

`Promise`的构造器函数的执行时同步的，所以先输入`2`

```js
			setTimeout(() => {
				console.log(1)
			}, 0)
			new Promise((resolve) => {
				console.log(2)
				resolve()
			}).then(() => {
				console.log(3)
			}).then(() => {
				console.log(4)
			})
			console.log(5)
```

![image-20220510100911153](image-20220510100911153.png)

### 面试题三

`Promise`对象状态改变过一次后，后面就不会再改变了，回调函数也不再被调用，所以最后的`resovle(6)`不会有任何效果

```js
const first = () => (new Promise((resolve, reject) => {
    console.log(3)

    let p = new Promise((resolve, reject) => {
        console.log(7)
        setTimeout(() => {
            console.log(5)
            resolve(6)
        }, 0)
        resolve(1)
    })
    resolve(2)
    p.then((arg) => {
        console.log(arg)
    })
}))

first().then((arg) => {
    console.log(arg)
})

console.log(4)
```

![image-20220510102223113](image-20220510102223113.png)

### 面试题四

当`Promise`对象的`pending`状态发生改变时，其第一个`then`方法的回调函数会进入微队列最后，第二个及后面的`then`方法依次执行时，其各自的回调函数会被缓存。

被缓存的回调函数，在第一个`then`方法的回调对应的微任务被执行完，该`then`方法返回的`Promise`对象状态发生了改变时，被缓存的第二个`then`方法的回调，进入微队列的末端，等待之前的微任务执行完毕后开始执行。

```js
// 1 7 2 3 8 4 6 5 0
			// 宏队列[0]
			// 微队列[2 8 4 6 5]
			setTimeout(() => {
				console.log('0')
			}, 0)
			
			new Promise((resolve, reject) => {
				console.log('1')
				resolve()
			}).then(() => {
				console.log('2')
				new Promise((resolve, reject) => {
					console.log('3')
					resolve()
				}).then(() => {
					console.log('4')
				}).then(() => {
					console.log('5')
				})
			}).then(() => {
				console.log('6')
			})
			
			new Promise((resolve, reject) => {
				console.log('7')
				resolve()
			}).then(() => {
				console.log("8")
			})
```

![image-20220510112144540](image-20220510112144540.png)

























































