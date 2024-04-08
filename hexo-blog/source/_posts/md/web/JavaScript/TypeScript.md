---
title: 'TypeScript基础'
cover: false
date: 2022-7-19 19:38:20
tags:
  - TypeScript
typora-root-url: TypeScript
description: typescript基础
---



[TOC]



# 环境配置和搭建

## 什么是`TypeScript`

`TypeScript`是`JavaScript`的超集，遵循最新的`ES5/ES6`规范。`TypeScript`扩展了`JavaScript`语法

为什么要有`TS`

- `TS`更像后端语言，如`JAVA`，可以开发大型企业应用
- `TS`提供的类型系统，可以帮助我们在写代码时提供丰富的语法提示
- 在编写代码时，会对代码进行类型检查从而避免很多线上错误

> `TypeScript`不会取代`js`，两者是相互共存的
>
> 尤雨溪：我认为将类型添加到`js`本身是一个漫长的过程。让委员会设计一个类型系统是（根据`TC39`的经历来判断）不切实际的
>
> 我也是这么认为的



## 环境配置

### 全局编译`TS`文件

全局安装`typescript`对`ts`进行编译

```bash
npm i typescript -g
tsc --init # 生成tsconfig.json
```

```bash
tsc # 可以将ts文件编译成js文件
tsc --watch # 监控ts文件变化生成js文件
```

本地安装

```bash
npm i typescript -D
npx tsc --init
```

创建`tsconfig.json`，以下是默认生成的配置

```bash
npx tsc --init

Created a new tsconfig.json with:                                                                                       
                                                                                                                     TS 
  target: es2016
  module: commonjs
  strict: true
  esModuleInterop: true
  skipLibCheck: true
  forceConsistentCasingInFileNames: true


You can learn more at https://aka.ms/tsconfig

```

新建`src/1.ts`

```ts
let string:String = 'hello'
```

会根据配置文件，将其转为`js`语法

使用`tsc`指令，将文件转化为`js`语法，默认不添加文件名，会将当前目录及子目录下，所有的`ts`文件全部转为`js`文件，如果是局部安装，则使用`npx tsc`指令

![image-20220719224055435](image-20220719224055435.png)

`1.js`

```js
"use strict";
let string = 'hello';

```

但我们希望的是实时编译，使用`npx tsc --watch`指令

```bash
D:\workspace\github\code\project-workshop\code-prac\typescript>npx tsc --watch
[下午10:44:16] File change detected. Starting incremental compilation...

[下午10:44:16] Found 0 errors. Watching for file changes.

```

修改`1.ts`，是会实时编译的

```ts
let string:String = 'hello1'
let hello:String = 'hello'
```

`1.js`

```js
"use strict";
let string = 'hello1';
let hello = 'hello';

```

### `code runner + ts-node`

现在我们还希望，直接运行`ts`文件，比如打印下`string`变量，目前可行的办法是，编译成`js`后，运行`js`文件

但很麻烦，借助于`code runner`插件（需要在`vscode`插件市场搜索安装），并安装`npm install ts-node -g`，必须装在全局

`1.ts`

```ts
let string:String = 'hello1'

let hello:String = 'hello' // 选中
console.log(hello) // 选中
```

然后选择`1.ts`中的代码，右键运行`Run Code`，控制台会打印输出`hello`

同级目录下，会生成`tempCodeRunnerFile.js`，内容是选中的内容，然后借助了`ts-node`环境执行了该文件

![image-20220719225649559](image-20220719225649559.png)

无论是全局编译还是使用`code runner + ts-code`来处理`ts`文件，在我们真正写代码时，还是不能满足需求的，所以要借助构建工具

可以使用`webpack`或`rollup`

### 构建工具来处理`ts`

由于学习`ts`的过程中，并不会处理图片等资源，这里的构建工具暂不选取`webpack`，而使用`rollup`

拓展：解析`ts`的方式有两种

- `ts`插件来解析
- 通过`babel`来解析

在`rollup`中，会采用`rollup-plugin-typescript2`包，配合当前配置文件来解析`ts`

在`webpack`中，会采用`ts-loader`或者`babel-plugin-typescript`包来解析

#### `rollup`来处理`ts`

新建`rollup.config.js`

本地安装

- `rollup`
- `typescript`
- `rollup-plugin-typescript2`：连接`rollup`和`typescript`的桥梁
- `@rollup/plugin-node-resolve`：以`node`的方式导入第三方包
- `rollup-plugin-serve`：起服务相关

在根路径下，`npm init -y`初始化`package.json`

根目录下安装

```bash
npm i rollup typescript rollup-plugin-typescript2 @rollup/plugin-node-resolve rollup-plugin-serve -D
```

安装后的`package.json`

```json
{
  "name": "typescript",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@rollup/plugin-node-resolve": "^13.3.0",
    "rollup": "^2.77.0",
    "rollup-plugin-serve": "^2.0.0",
    "rollup-plugin-typescript2": "^0.32.1",
    "typescript": "^4.7.4"
  }
}

```

新建`src/index.ts`文件

配置`rollup.config.js`

```js
import {nodeResolve} from "@rollup/plugin-node-resolve"

import ts from "rollup-plugin-typescript2"
import serve from "rollup-plugin-serve"
import path from "path"

export default {
    input:'src/index.ts',
    output: {
        file: path.resolve(__dirname, 'dist/bundle.js'),
        format: 'iife', // 告诉rollup，打包后的代码是可以执行的，所以打包成立即执行函数
        // 常见的有global(弄个全局变量来接受)
        // cjs（会变成module.exports）
        // esm（会变成 import export的es6语法）
        // umd（兼容amd + commonjs，不支持es6导入）
        // rollup的配置文件，支持es6语法，它就是根据es6的语法来解析的
        sourcemap: true // ts的配置文件也得配，ts配置文件中，搜索sourceMap，取消注释即可
    },
    plugins: [
        // 1.先拿到ts文件
        nodeResolve({
            extensions: ['.js', '.ts'] // 默认解析ts文件
        }),
        // 2.根据配置文件解析
        ts({
            // 指定好ts的配置文件
            tsconfig: path.resolve(__dirname, 'tsconfig.json')
        }),
        // 3.最后提供服务
        serve({
            port: 3000, // 指定服务的端口号
            contentBase: '', // 值为空，表示指定根目录
            openPage: '/public/index.html' // 需要新建该目录和文件，并在index.html中引入`dist/bundle.js`
        })
    ]

}
```

备注：`ts`的配置文件也得配`sourceMap`，搜索`sourceMap`，取消注释即可

`package.json`中新增`script`

```json
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "rollup -cw"
  },
```

执行`npm run dev`

报错：

```bash
[!] Error: Incompatible tsconfig option. Module resolves to 'CommonJS'. This is incompatible with rollup, please use 'module: "ES2015"' or 'module: "ESNext"'.
Error: Incompatible tsconfig option. Module resolves to 'CommonJS'. This is incompatible with rollup, please use 'module: "ES2015"' or 'module: "ESNext"'.

```

将`ts`的配置文件的`module`字段的值，改为`ESNext`（默认的是`commonjs`），`target`字段由`es2016`改为`es5`

再次执行`npm run dev`

成功：

```bash
bundles src/index.ts → dist/bundle.js...
rpt2: options error TS6053: File 'D:/workspace/github/code/project-workshop/code-prac/src/index.ts' not found.
  The file is in the program because:
    Root file specified for compilation
http://localhost:3000 -> D:\workspace\github\code\project-workshop\code-prac\typescript
(!) Generated an empty chunk
index
created dist/bundle.js in 4.5s

```

打开`localhost:8080/public/index.html`，看下控制台效果

注意`index.html`中，引入`bundle.js`的路径，`rollup`会自己去找

```html
<body>
  <script src="/dist/bundle.js"></script>
</body>
```

当然也可以直接使用相对路径（推荐）

```html
<body>
  <script src="../dist/bundle.js"></script>
</body>
```



目前我们是没有写任何`ts`代码的，所以会有如上提示

在`src/index.ts`中写点内容

```ts
let str:String = "hello"
console.log(str)

```

注意要打印该变量（使用该变量），因为`rollup`默认开启了`tree-shaking`

保存后查看`dist/bundle.js`

```js
(function () {
	'use strict';

	var str = "hello";
	console.log(str);

})();
//# sourceMappingURL=bundle.js.map

```



# 基本类型

- 最基本的类型有，数字、字符、布尔
- 所有的类型都在冒号后面，`ts`的核心：一切都以安全为准
- 什么时候可以不用类型（推导）

基本演示

```ts
// 基础类型，基本演示
let num:number = 1
let str:string = 'sai'
let bool:boolean = true

```

## 数字类型

```ts
// 数字类型
// 分清小写`number`和大写`Number`的区别（`js`基础）
let num2:Number = 2 // 类，也可以当做类型
let num3:number = Number(1)
let num4:Number = new Number(1)

console.log(num2, num3, num4)
```

`bundle.js`

```js
(function () {
	'use strict';

	// 数字类型
	// 分清小写`number`和大写`Number`的区别（`js`基础）
	var num2 = 2; // 类，也可以当做类型
	var num3 = Number(1);
	var num4 = new Number(1);
	console.log(num2, num3, num4);

})();
//# sourceMappingURL=bundle.js.map

```

## 数组类型

```ts
// 数组类型，数组的概念：一类类型的集合
const arr:number[]  = [] // 声明只放数字的数组
const arr2:(number | string)[] = ['a', 1] // 联合类型，声明既可以放数字，也可以放字符串的数组（并集）
const arr3:any[] = ['', 1, {}] // 如果数组里放的内容就是不规律的
const arr4:Array<boolean> = [true, false] // 利用泛型来定义数组

```

`bundle.js`

```js
(function () {
	'use strict';

	// 数组类型，数组的概念：一类类型的集合
	var arr = []; // 声明只放数字的数组
	var arr2 = ['a', 1]; // 联合类型，声明既可以放数字，也可以放字符串的数组（并集）
	var arr3 = ['', 1, {}]; // 如果数组里放的内容就是不规律的
	var arr4 = [true, false]; // 利用泛型来定义数组
	console.log(arr, arr2, arr3, arr4);

})();
//# sourceMappingURL=bundle.js.map

```

## 元组类型

```ts
// 元组，内容固定，类型固定
const tuple:[string, boolean, number] = ['a', true, 2] // 初始化的时候，必须按照要填入数据
let r = tuple.pop() // r的类型，三种都有可能，还有可能是undefined
console.log(r)
tuple.push('bb', 1) // 在放入的时候，只能放入元组中定义的类型
// tuple[3] = 100 // 不能通过索引来更改元组

// 应用场景：数据交换（要用到泛型，后面再说）

```

`bundle.js`

```js
(function () {
	'use strict';

	// 元组，内容固定，类型固定
	var tuple = ['a', true, 2]; // 初始化的时候，必须按照要填入数据
	var r = tuple.pop(); // r的类型，三种都有可能，还有可能是undefined
	console.log(r);
	tuple.push('bb', 1); // 在放入的时候，只能放入元组中定义的类型
	// tuple[3] = 100 // 不能通过索引来更改元组
	// 应用场景：数据交换（要用到泛型，后面再说）

})();
//# sourceMappingURL=bundle.js.map

```

## 枚举类型

`ts`最终编译成的`js`是没有类型的，只是在开发时使用，分为普通枚举、异构枚举和常量枚举

- 普通枚举

  ```ts
  // 普通枚举
  enum ROLE { // 大写是规范
      USER,
      ADMIN,
      MANAGE
  }
  
  console.log(ROLE) // 值是默认加上的，可以通过USER取0，ADMIN取1
  // 同时还可以反举，通过0来取USER，2取ADMIN
  // {
  //     '0': 'USER',
  //     '1': 'ADMIN',
  //     '2': 'MANAGE',
  //     USER: 0,
  //     ADMIN: 1,
  //     MANAGE: 2
  // }
  ```

  `bundle.js`

  ```js
  (function () {
      'use strict';
  
      // 普通枚举
      var ROLE;
      (function (ROLE) {
          ROLE[ROLE["USER"] = 0] = "USER";
          ROLE[ROLE["ADMIN"] = 1] = "ADMIN";
          ROLE[ROLE["MANAGE"] = 2] = "MANAGE";
      })(ROLE || (ROLE = {}));
      console.log(ROLE); // 值是默认加上的，可以通过USER取0，ADMIN取1
      // 同时还可以反举，通过0来取USER，2取ADMIN
      // {
      //     '0': 'USER',
      //     '1': 'ADMIN',
      //     '2': 'MANAGE',
      //     USER: 0,
      //     ADMIN: 1,
      //     MANAGE: 2
      // }
  
  })();
  //# sourceMappingURL=bundle.js.map
  
  ```

- 异构枚举

  ```ts
  // 异构枚举
  enum ROLE {
      USER = 'USER', // 放字符串是不支持反举的
      ADMIN = 5,
      MANAGE // 会根据上一个的值，自动进行推断，值默认往后加一
  }
  
  console.log(ROLE)
  // { '5': 'ADMIN', '6': 'MANAGE', USER: 'USER', ADMIN: 5, MANAGE: 6 }
  
  ```

  `bundle.js`

  ```js
  (function () {
      'use strict';
  
      // 异构枚举
      var ROLE;
      (function (ROLE) {
          ROLE["USER"] = "USER";
          ROLE[ROLE["ADMIN"] = 5] = "ADMIN";
          ROLE[ROLE["MANAGE"] = 6] = "MANAGE"; // 会根据上一个的值，自动进行推断，值默认往后加一
      })(ROLE || (ROLE = {}));
      console.log(ROLE);
      // { '5': 'ADMIN', '6': 'MANAGE', USER: 'USER', ADMIN: 5, MANAGE: 6 }
  
  })();
  //# sourceMappingURL=bundle.js.map
  
  ```
  
  加上`const`后，不会生成一个对象（更简洁），没有反举了
  
  ```ts
  // 异构枚举
  const enum ROLE {
      USER = 'USER',
      ADMIN = 5,
      MANAGE
  }
  
  console.log(ROLE.USER) // USER
  
  ```
  
  `bundle.js`
  
  ```js
  (function () {
      'use strict';
  
      console.log("USER" /* ROLE.USER */); // USER
  
  })();
  //# sourceMappingURL=bundle.js.map
  
  ```

## `null`和`undefined`

`null`和`undefined`是任何类型的子类型，可以赋值给其他类型

```ts
let name:number = undefined // 默认情况下，是不能把undefined和null赋给其他人的
```

![image-20220720200619011](image-20220720200619011.png)

修改`ts`的配置文件，取消`strictNullChecks`字段的注释，设置为`false`，或者不用改这里，直接取消严格模式

由于`name`变量已经在`ts`的全局环境中定义了，所以导出当前的变量

```ts
let name:number = undefined // 默认情况下，是不能把undefined和null赋给其他人的

export {} // name属性，在ts全局下已经被声明过了，再声明就重复了。如果想要在自己的文件中也能声明，就需要加上export {}，做一个导出，表示name是当前模块的name，而不是外部的name。如果不加这个声明，ts会把所有的声明类型做一个合并。声明的作用是：防止模块间的数据共享类型。一般情况下，都会导出的
```

`bundle.js`

```js
(function () {
	'use strict';

	var name = undefined; // 默认情况下，是不能把undefined和null赋给其他人的
	console.log(name);

})();
//# sourceMappingURL=bundle.js.map

```

我们恢复对`ts`配置文件的修改，在严格模式下，`undefined`赋值给`undefined`，`null`赋值给`null`，是没有问题的

```ts
let u:undefined = undefined
let n:null = null
console.log(u, n)
```

`bundle.js`

```js
(function () {
	'use strict';

	var u = undefined;
	var n = null;
	console.log(u, n);

})();
//# sourceMappingURL=bundle.js.map

```

## `never`

表示代码无法达到终点（无法执行到），也是任何类型的子类型

- 出错

  ```ts
  // 应用场景：出错了，我希望抛个错，错误函数的类型，可以设置成never类型
  function throwError():never { // never可以赋值给void，因为它是任意类型的子类型
      throw new Error()
  }
  
  let xxx:string = throwError() // never可以赋值给任意类型
  ```

  

- 死循环

  ```ts
  function whileTrue():never { // 代码本身是不知道内部有没有死循环的，所以要明确指出，返回值就是never
      while(true) {
  
      }
  }
  ```

- 永远走不到的判断

- 做代码的完整性校验

  ```ts
  function setVal(val:string) {
      if(typeof val === 'string') {
  
      } else {
          // 这里永远走不到，因为入参已经限制死了
          // 帮我们代码做完整校验，走不到else中，val就是never
          val 
      }
  }
  ```

  

## `void`

`void`一般用来描述函数返回值，也可以描述变量

只能把`undefined`和`null`赋值给`void`

```ts
function getVoid():void { // 指定返回值为void时
    // return undefined 并且函数内部啥都不写，相当于返回undefined，undefined是可以赋值给void的，写法时兼容的
    // 那么返回null呢？可以取消严格模式，或者设置ts配置文件的`strictNullChecks`字段为false,就可以将null赋值给void，但一般不会这么写（都会在严格模式下写代码）
}
a = getVoid() // 当a的类型是void时，就知道该方法没有返回值了
```

## `object`

非原始数据，后面泛型约束，会大量使用`object`

```ts
function create(obj:object) {

}
create({})
create(function () {

})
create([])


```

## `symbol`和`bigint`

`js`本身就有的类型，并不是`ts`提供的

**`Symbol`**

```ts
let s1:symbol = Symbol(1)
let s2:symbol = Symbol(2)
console.log(s1 === s2) // false
```

无法编译成`es5`，会原样输出

`bundle.js`

```js
(function () {
	'use strict';

	var s1 = Symbol(1);
	var s2 = Symbol(2);
	console.log(s1 === s2); // false

})();
//# sourceMappingURL=bundle.js.map

```

**`bigint`**

```ts
let max = Number.MAX_SAFE_INTEGER
console.log(max + 1 === max + 2); // true 取到js中的最大值，然后相加，结果为true，很明显是有问题的
let r1:bigint = BigInt(max)
console.log(BigInt(max) + BigInt(1) === BigInt(max) + BigInt(2)) // false
```

`bundle.js`

```js
(function () {
	'use strict';

	var max = Number.MAX_SAFE_INTEGER;
	console.log(max + 1 === max + 2); // true 取到js中的最大值，然后相加，结果为true，很明显是有问题的
	BigInt(max);
	console.log(BigInt(max) + BigInt(1) === BigInt(max) + BigInt(2)); // false

})();
//# sourceMappingURL=bundle.js.map

```



# 联合类型

联合类型如果不进行赋值，在没有确定类型之前，默认会取公共方法

```ts
let numOrStr:string | number
```



![image-20220721211404171](image-20220721211404171.png)



在确定类型后，可以设置相对应的方法

```ts
numOrStr = 123
```

![image-20220721223156872](image-20220721223156872.png)

```ts
numOrStr = 'abc'
```

![image-20220721223246737](image-20220721223246737.png)

赋予类型后，可以根据上下文自动推断对应类型的方法

场景：

- 在取值的时候，也会遇到联合类型

  ```js
  const ele:HTMLElement | null = document.getElementById('app') // 真正取到了这个元素，或这个元素不存在
  ele.innerHTML = 'abc'
  ```

  直接就提示了`ele`可能为空，备注：`HTMLElement`类型是`ts`内部提供的类型

  ![image-20220721224547820](image-20220721224547820.png)

  之前我们可以通过

  ```js
  if(ele) {
      ele.innerHTML = 'abc'
  }
  ```

  或者

  ```js
  ele && (ele.innerHTML = 'abc')
  ```

  来进行判断

  但现在我们就明确知道了，`ele`一定不为空，可以使用非空断言：`!`，告诉`ts`，这个东西一定有值，后续出事我负责

  ```ts
  ele!.innerHTML = 'abc'
  
  // 另外一个例子
  let a:string | number | undefined
  a!.toString()
  ```

  上面是去除掉了空的情况，也可以直接使用`as`或`<>`强转某个类型

  强制告诉`ts`，当前这个变量，就是其中某个类型的一个

  强转要求必须在联合类型中用才行

  ```ts
  let a:string | number | undefined
  
  (<string>a).indexOf('abc')
  ```

  ![image-20220721225834606](image-20220721225834606.png)

  为了避免和`jsx`语法中的尖括号冲突，强转的语法可以用`as`来描述，这也是一种断言

  ```ts
  let a:string | number | undefined
  
  (a as string).indexOf('abc')
  ```

  可以使用双重断言，将`a`强转成`boolean`类型，但不建议这么搞

  ```js
  let a:string | number | undefined
  
  (a as any) as boolean
  ```

  双重断言：先转换成`any`，再转换成一个具体的类型。

  问题：会导致类型出问题


## 拓展

### `?`

还有一个符号是`?`，表示`aa && aa.xxx`，这个是`js`中本来就有的

```ts
const ele:HTMLElement | null = document.getElementById('app') // 真正取到了这个元素，或这个元素不存在
ele?.style // ele && ele.style 如果有ele的话，取ele得style属性
ele?.style?.color // ele && ele.style && ele.style.color 在js中，这是链判断符
```
`bundle.js`
```js
(function () {
	'use strict';

	var _a;
	var ele = document.getElementById('app'); // 真正取到了这个元素，或这个元素不存在
	ele === null || ele === void 0 ? void 0 : ele.style; // ele && ele.style 如果有ele的话，取ele得style属性
	(_a = ele === null || ele === void 0 ? void 0 : ele.style) === null || _a === void 0 ? void 0 : _a.color; // ele && ele.style && ele.style.color 在js中，这是链判断符

})();
//# sourceMappingURL=bundle.js.map

```
样例二
```js
var aa = {
  bb: {
   cc: '123'
  }
}

console.log(aa?.bb?.cc) // 123
```

### `??`

`false ?? true`的结果是多少呢？

只要第一个的值不是`null`或者`undefined`，就将第一个的值返回，否则就返回第二个值（表示排除`null`和`undefined`）

还有的操作符有：`||`、`&&`、`|`、`&`

## 字面量类型

类型的内容是固定的，已经确定好了，变量的值只能是这几个

```ts
let type: 'a' | 'b' | 'c' | 'd' = 'b'
```

但是这样写，会导致类型过于复杂（太长了），我们可以把类型单独提出来

使用`ts`中的类型别名

```ts
type IType = 'a' | 'b' | 'c' | 'd' // 类型别名
let type:IType = 'b'
let type2:IType = 'c'
```

值虽然可以写对象，但一般不这么搞

应用场景：接口的参数、状态码、下拉框的值

# 函数

## 类型

可以对函数增加类型

- 对函数的参数进行类型校验
- 对函数的返回值进行类型校验
- 也可以对函数本身进行校验（声明、参数、返回值）

有两种声明函数的方式

- 函数关键字`function name(){}`

  - 入参默认类型为`any`，返回值默认类型为`void`

  - 可以指定入参和返回值类型

    ```ts
    function sum(x:string, y:string):string { // 括号后面的表示返回值类型
        return x + y
    }
    ```

- `let myFuc = function() {}`，可以自动根据当前等号右边的内容，推断左边的内容

  ```ts
  let res = (x:number, y:number):number => {
      return x + y
  }
  ```

  `res`的类型是`(x:number, y:number) => number`，可以显示指定

  ```ts
  let res:(x:number, y:number) => number = (x:number, y:number):number => {
      return x + y
  }
  ```

  但这样写比较恶心，优化一下写法

  ```ts
  type IFn = (x: number, y: number) => number
  let res: IFn = (x: number, y: number): number => {
      return x + y
  }
  ```

  如果此时这么写了，后面函数就不需要再指定参数和返回值类型了，会自动匹配你写的函数，是否符合前面指定的要求

  ```ts
  type IFn = (x: number, y: number) => number
  let res: IFn = (x, y) => {
      return x + y
  }
  res('a', 2)
  ```

  如果入参中类型不匹配，会给出提示

  ![image-20220722063509281](image-20220722063509281.png)

- 小结：

  - 自动根据等号右边的内容，推断左边的类型（比较常用）
  - 可以指定类型，右边赋予一个可以兼容这个类型的函数

## 参数

参数可以设置不传，使用`?`（可选参数）对参数进行限制

```ts
let res = (x:number, y?:number):number => {
    return x + y
}
```

但是直接这样写，`return`的时候可能会有问题，因为`y`通过`?`进行限制，表示可传可不传

![image-20220723064245891](image-20220723064245891.png)

那怎么处理呢？给一个默认值嘛

`js`中默认值和可选参数不能一起使用

使用明确指出`y`一定不为空

```ts
let res = (x:number, y?:number):number => {
    return x + y!
}
```

或者使用`as`（一般我们都是用`as`）

```js
let res = (x:number, y?:number):number => {
    return x + (y as number)
}
```

那么剩余运算符，在`ts`中怎么用呢?

但是要指出类型

```ts
let res = (x:number, y?:number, ...args:number[]):number => {
    return x + (y as number)
}
res(1, 2, 3, 4, 5)
```

## 重载

一个方法，根据参数的不同，实现不同的功能，`ts`的目的就是根据不同的参数返回类型

需求：将数值`123`转为`[1, 2, 3]`，并将字符串`abc`转为`['a', 'b', 'c']`

```ts
function toArray(value: number | string): number[] | string [] { // 重载方法在真实方法的上方
    if(typeof value == 'string') {
        return value.split('')
    } else {
        return value.toString().split('').map(item => Number(item))
    }
}

const res = toArray('abc')
console.log(res)
```

这样写有个问题，传的是number，但是返回的可能是string数组（反之），应该限制一下（但事实上对于打包后的`js`来说，经过测试后，好像是没问题的）

`bundle.js`

```js
(function () {
    'use strict';

    function toArray(value) {
        if (typeof value == 'string') {
            return value.split('');
        }
        else {
            return value.toString().split('').map(function (item) { return Number(item); });
        }
    }
    var res = toArray('abc');
    console.log(res);

})();
//# sourceMappingURL=bundle.js.map

```

这时就要用到函数的重载

重载方法需要写法函数的上面

```ts
function toArray(value:number):number[] // number类型的toArray被treeShaking了
function toArray(value:string):string[]
function toArray(value: number | string): number[] | string [] { // 重载方法在真实方法的上方
    if(typeof value == 'string') {
        return value.split('')
    } else {
        return value.toString().split('').map(item => Number(item))
    }
}

const res = toArray('abc')
console.log(res)
```

但打包后的`js`还是原来的

`bundle.js`

```js
(function () {
    'use strict';

    function toArray(value) {
        if (typeof value == 'string') {
            return value.split('');
        }
        else {
            return value.toString().split('').map(function (item) { return Number(item); });
        }
    }
    var res = toArray('abc');
    console.log(res);

})();
//# sourceMappingURL=bundle.js.map

```

写了老半天，写了一堆空气，`○( ＾皿＾)っHiahiahia…`

`ts`的目的：为了安全，以及更好的提示



# 类

类，最早都是用构造函数来替代的，如果`es6`中的类，编译成`es5`，最终还是会编译成函数的

类有哪些特点呢？

- 实例属性、实例方法、静态属性、静态方法、原型属性、原型方法



## 实例属性、方法

```ts
class Pointer {
    
}
```

这样就声明了一个类，一般都大写

类里面有一个构造函数，当使用`new`操作符，`new Pointer`时，执行的就是这个构造函数，在构造函数中的操作，都是初始化操作

对于`ts`而言，在使用必须先声明类型，声明的变量会被增加到实例上，可以通过实例来调用该属性

```ts
class Pointer {
    
    x: number
    y: number

    constructor(x: number, y: number) {
        this.x = x
        this.y = y
    }
}

new Pointer(100, 200)
```

如果在构造函数中没有进行初始化，则需要在声明时进行初始化，否则会报错

```ts
class Pointer {
    
    x: number
    y: number

    constructor(x: number, y: number) {
    }
}

new Pointer(100, 200)
```

报错信息：提示参数没有初始化

![image-20220723072512685](image-20220723072512685.png)

在声明时进行初始化

```ts
class Pointer {
    // ts比较特殊，在使用必须先声明类型
    x: number = 1
    y: number = 2

    constructor(x: number, y: number) {
        // this.x = x
        // this.y = y
    }
}

const res = new Pointer(100, 200)
console.log(res, res.x) // Pointer {x: 1, y: 2} 1
```

看下`bundle.js`，这里是转成了`es5`了

```js
(function () {
    'use strict';

    var Pointer = /** @class */ (function () {
        function Pointer(x, y) {
            // ts比较特殊，在使用必须先声明类型
            this.x = 1;
            this.y = 2;
            // this.x = x
            // this.y = y
        }
        return Pointer;
    }());
    var res = new Pointer(100, 200);
    console.log(res, res.x); // Pointer {x: 1, y: 2} 1

})();
//# sourceMappingURL=bundle.js.map

```

在声明类型的同时初始化，就相当于在实例的构造函数中初始化了







继续上面的：

但是呢，我们一般只会在构造函数里面赋值

另外，如果我们就不想初始化，可以使用非空断言，或者取消配置文件的严格模式（不推荐）

```ts
class Pointer {
    // ts比较特殊，在使用必须先声明类型
    x!: number
    y!: number

    constructor(x: number, y: number) {
        // this.x = x
        // this.y = y
    }
}

const res = new Pointer(100, 200)
console.log(res, res.x)
```

但是一般情况下，我们还是会在构造函数中赋值的

```ts
class Pointer {
    // ts比较特殊，在使用必须先声明类型
    x: number
    y: number
    constructor(x: number, y: number) {
        this.x = x
        this.y = y
    }
}

const res = new Pointer(100, 200)
console.log(res, res.x) // Pointer {x: 100, y: 200} 100
```

构造函数它也是个函数，里面依然可以使用剩余运算符、可选参数、默认参数

## 属性修饰符

### `public`

对于类型声明，默认是由`public`关键字修饰的

上面的等价于

```ts
class Pointer {
    public x: number
    public y: number
    constructor(x: number, y: number) {
        this.x = x
        this.y = y
    }
}

const res = new Pointer(100, 200)
console.log(res, res.x) // Pointer {x: 100, y: 200} 100
```

当然也可以将传入的参数，直接放在实例上，无需再次声明。`public`是属性修饰符，`js`中是没有的

等价写法如下：

```ts
class Pointer {
    constructor(public x: number, public y: number) {
        this.x = x
        this.y = y
    }
}

const res = new Pointer(100, 200)
console.log(res, res.x) // Pointer {x: 100, y: 200} 100
```

值得注意的是，将传入的参数，直接放在实例上时，相当于已经给实例进行了初始化赋值操作，构造函数中不必再初始化了

只要在构造函数外面，声明了变量，这个变量就会被添加到实例上（等价写法，相当于在构造函数外面声明了变量）

```ts
class Pointer {
    // public x: number
    // public y: number
    constructor(public x: number, public y: number) {
        // this.x = x
        // this.y = y
    }
}

const res = new Pointer(100, 200)
console.log(res, res.x) // Pointer {x: 100, y: 200} 100
```

`bundle.js`

```js
(function () {
    'use strict';

    var Pointer = /** @class */ (function () {
        // public x: number
        // public y: number
        function Pointer(x, y) {
            this.x = x;
            this.y = y;
            // this.x = x
            // this.y = y
        }
        return Pointer;
    }());
    var res = new Pointer(100, 200);
    console.log(res, res.x); // Pointer {x: 100, y: 200} 100

})();
//# sourceMappingURL=bundle.js.map

```

### `private`

表示只有自己能访问的属性



先看一个简单继承的例子

```ts
class Animal {
    constructor(public name: string, public age: number) {

    }
}

class Cat extends Animal {
    constructor(name: string, age: number, public address: string) {
        super(name, age); // 子类继承父类的话，构造函数中，必须要调用super，相当于执行了Animal.call(this, name, age)
    }
}

let cat = new Cat('Tom', 8,  'USA')
console.log(cat) // Cat {name: 'Tom', age: 8, address: 'USA'}


export {}
```

看下`bundle.js`

```js
(function () {
    'use strict';

    /******************************************************************************
    Copyright (c) Microsoft Corporation.

    Permission to use, copy, modify, and/or distribute this software for any
    purpose with or without fee is hereby granted.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
    REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
    INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
    LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
    OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
    PERFORMANCE OF THIS SOFTWARE.
    ***************************************************************************** */
    /* global Reflect, Promise */

    var extendStatics = function(d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };

    function __extends(d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    }

    var Animal = /** @class */ (function () {
        function Animal(name, age) {
            this.name = name;
            this.age = age;
        }
        return Animal;
    }());
    var Cat = /** @class */ (function (_super) {
        __extends(Cat, _super);
        function Cat(name, age, address) {
            var _this = _super.call(this, name, age) || this;
            _this.address = address;
            return _this;
        }
        return Cat;
    }(Animal)); 
    var cat = new Cat('Tome', 8, 'USA');
    console.log(cat); // Cat {name: 'Tom', age: 8, address: 'USA'}

})();
//# sourceMappingURL=bundle.js.map

```

我们在父类和子类中构造函数中，都打印一下`name`属性

```ts
class Animal {
    constructor(public name: string, public age: number) {
        console.log(this.name) // Tom
    }
}

class Cat extends Animal {
    constructor(name: string, age: number, public address: string) {
        super(name, age);
        console.log(this.name) // Tom
    }
}

let cat = new Cat('Tom', 8,  'USA')
console.log(cat.name) // Tom


export {}
```

如果将父类的构造函数的`name`修饰符，改成`private`，子类及子类实例就不能访问了

```ts
class Animal {
    constructor(private name: string, public age: number) {
        console.log(this.name)
    }
}

class Cat extends Animal {
    constructor(name: string, age: number, public address: string) {
        super(name, age);
        console.log(this.name) // 这里无法访问
    }
}

let cat = new Cat('Tom', 8,  'USA')
console.log(cat.name)


export {}
```



![image-20220724110934800](image-20220724110934800.png)



### `protected`

表示只有自己，和自己的子孙可以访问

外界是访问不了的

- 后代的实例里，是访问不了的



将参数修饰符改为`protected`

```ts
class Animal {
    constructor(protected name: string, public age: number) {
        console.log(this.name)
    }
}

class Cat extends Animal {
    constructor(name: string, age: number, public address: string) {
        super(name, age);
        console.log(this.name)
    }
}

let cat = new Cat('Tom', 8,  'USA')
console.log(cat.name)  // 这里无法访问


export {}
```

![image-20220724111222897](image-20220724111222897.png)



补充

我们可以给构造函数添加修饰符，默认的是`public`

- `protected`
  - 可以被继承，不能被`new`
  - `new`是在实例化，调用这个构造函数，而`protected`的函数只能在类的内部被调用
- `private`
  - 不能被继承，也不能被`new`

### `readonly`

表示只读属性，在初始化完毕后，就不能修改了，有点类似于`const`

值得注意的是，在`constructor`中，表示的都是初始化操作，在`constructor`里面，是可以修改的

```ts
class Animal {
    public readonly n: number = 1

    public constructor(public name: string, public age: number) {
        console.log(this.name)
        this.n = 100  // 这里可以修改
    }
}

class Cat extends Animal {
    public constructor(name: string, age: number, public readonly address: string) {
        super(name, age);
        console.log(this.name)
        // this.n = 200 // 这里不能修改，因为对于父类而言，已经初始化完毕了
    }
}

let cat = new Cat('Tom', 8, 'USA')
console.log(cat.name)
// cat.address = 'shanghai' 编译不会通过的

export {}
```

不能修改的只是变量的引用

上例中，如果`address`是个对象，修改的是对象里面的属性，是可以的

```ts
class Animal {
    public readonly n: number = 1

    public constructor(public name: string, public age: number) {
        console.log(this.name)
        this.n = 100  // 这里可以修改
    }
}

class Cat extends Animal {
    public constructor(name: string, age: number, public readonly address: any) {
        super(name, age);
        console.log(this.name)
        // this.n = 200 // 这里不能修改，因为对于父类而言，已经初始化完毕了
    }
}

let cat = new Cat('Tom', 8, {name:'USA'})
cat.address.name = 'shanghai'
console.log(cat)

export {}
```

## 静态属性、方法

之前讲过的实例属性、方法，需要通过`new`生成实例对象来调用

静态属性、方法，通过类来调用

### 静态属性

`es6`写法

```ts
class Animal {

    public constructor(public name: string, public age: number) {

    }

    // es6中要写成属性访问器
    static get type() {
        return '哺乳动物'
    }
    
    // static types = '哺乳动物' // 静态属性，es7语法，es6是不认的
}

console.log(Animal.type)

export {}
```

`bundle.js`

```js
(function () {
    'use strict';

    var Animal = /** @class */ (function () {
        function Animal(name, age) {
            this.name = name;
            this.age = age;
        }
        Object.defineProperty(Animal, "type", {
            // static types = '哺乳动物' // 静态属性，es7语法，es6是不认的
            // es6中要写成属性访问器
            get: function () {
                return '哺乳动物';
            },
            enumerable: false,
            configurable: true
        });
        return Animal;
    }());

    console.log(Animal.type);

})();
//# sourceMappingURL=bundle.js.map

```

编译后的结果，是通过`defineProperty`来实现的

`es7`语法

```ts
class Animal {

    public constructor(public name: string, public age: number) {

    }

    // es6中要写成属性访问器
    // static get type() {
    //     return '哺乳动物'
    // }

    static type = '哺乳动物' // 静态属性，es7语法，es6是不认的
}

console.log(Animal.type)

export {}
```

`bundle.js`

```js
(function () {
    'use strict';

    var Animal = /** @class */ (function () {
        function Animal(name, age) {
            this.name = name;
            this.age = age;
        }
        // es6中要写成属性访问器
        // static get type() {
        //     return '哺乳动物'
        // }
        Animal.type = '哺乳动物'; // 静态属性，es7语法，es6是不认的
        return Animal;
    }());

    console.log(Animal.type);

})();
//# sourceMappingURL=bundle.js.map

```

### 静态方法



```ts
class Animal {

    public constructor(public name: string, public age: number) {

    }

    static type = '哺乳动物' // 静态属性，es7语法，es6是不认的

    static getName() {
        return '动物'
    }
}

console.log(Animal.type, Animal.getName()) // 哺乳动物 动物

export {}
```

`bundles.js`

```js
(function () {
    'use strict';

    var Animal = /** @class */ (function () {
        function Animal(name, age) {
            this.name = name;
            this.age = age;
        }
        Animal.getName = function () {
            return '动物';
        };

        Animal.type = '哺乳动物'; // 静态属性，es7语法，es6是不认的
        return Animal;
    }());

    console.log(Animal.type, Animal.getName());

})();
//# sourceMappingURL=bundle.js.map

```

静态方法可以被继承，可以通过子类来调用

```ts
class Animal {

    public constructor(public name: string, public age: number) {

    }

    static type = '哺乳动物' // 静态属性，es7语法，es6是不认的

    static getName() {
        return '动物'
    }
}

class Cat extends Animal {
    public constructor(name: string, age: number, public readonly address: string) {
        super(name, age);
    }
}

console.log(Cat.type, Cat.getName()) // 哺乳动物 动物

export {}
```

子类也可以拿到父类的实例属性、方法

那么是怎么实现的呢？

`bundle.js`

```js
(function () {
    'use strict';
	
    
    var extendStatics = function(d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };

    function __extends(d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    }

    var Animal = /** @class */ (function () {
        function Animal(name, age) {
            this.name = name;
            this.age = age;
        }
        Animal.getName = function () {
            return '动物';
        };
        Animal.type = '哺乳动物'; // 静态属性，es7语法，es6是不认的
        return Animal;
    }());
    var Cat = /** @class */ (function (_super) {
        __extends(Cat, _super); 
        function Cat(name, age, address) {
            var _this = _super.call(this, name, age) || this;
            _this.address = address;
            return _this;
        }
        return Cat;
    }(Animal));
    console.log(Cat.type, Cat.getName()); // 哺乳动物 动物

})();
//# sourceMappingURL=bundle.js.map

```

看下编译后的结果，看下`__extends(Cat, _super)`，它会把子类和父类都传进来，只做了一件事`extendStatics`，继承静态属性，把子类的原型对象指向父类的原型对象，这样子类就可以通过原型类查找来调用父类的属性或方法了

如果子类中，有同名方法，调用的就是自己身上的属性和方法

```ts
class Animal {

    public constructor(public name: string, public age: number) {

    }

    static type = '哺乳动物'

    static getName() {
        return '动物'
    }
}

class Cat extends Animal {
    public constructor(name: string, age: number, public readonly address: string) {
        super(name, age);
    }

    static type = '猫科动物'

    static getName() {
        return '猫'
    }
}

console.log(Cat.type, Cat.getName()) // 猫科动物 猫

export {}
```

此时，如果想要访问父类的同名属性和方法，需要在子类的同名方法中，使用`super`关键字，获取到父类，然后调用方法（构造函数和静态方法中的`super`，默认指向的都是自己的父类，在原型方法中的`super`，指向父类的原型）

```ts
class Animal {

    public constructor(public name: string, public age: number) {

    }

    static type = '哺乳动物'

    static getName() {
        return '动物'
    }
}

class Cat extends Animal {
    public constructor(name: string, age: number, public readonly address: string) {
        super(name, age);
    }

    static type = '猫科动物'

    static getName() {
        console.log(super.getName()) // 动物
        return '猫'
    }
}

console.log(Cat.type, Cat.getName()) // 猫科动物 猫

export {}
```

`bundle.js`

```js
(function () {
    'use strict';

    var extendStatics = function(d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };

    function __extends(d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    }

    var Animal = /** @class */ (function () {
        function Animal(name, age) {
            this.name = name;
            this.age = age;
        }
        Animal.getName = function () {
            return '动物';
        };
        Animal.type = '哺乳动物';
        return Animal;
    }());
    var Cat = /** @class */ (function (_super) {
        __extends(Cat, _super);
        function Cat(name, age, address) {
            var _this = _super.call(this, name, age) || this;
            _this.address = address;
            return _this;
        }
        Cat.getName = function () {
            console.log(_super.getName.call(this)); // 动物
            return '猫';
        };
        Cat.type = '猫科动物';
        return Cat;
    }(Animal));
    console.log(Cat.type, Cat.getName()); // 猫科动物 猫

})();
//# sourceMappingURL=bundle.js.map

```

## 原型属性、方法

### 原型方法

直接在类中写的方法，就是原型方法

可以通过属性访问器，定义原型属性

```ts
class Animal {

    public constructor(public name: string, public age: number) {

    }

    static type = '哺乳动物'

    static getName() {
        return '动物'
    }
}

class Cat extends Animal {
    public constructor(name: string, age: number, public readonly address: string) {
        super(name, age);
    }

    static type = '猫科动物'

    static getName() {
        console.log(super.getName()) // 动物
        return '猫'
    }

    // 原型方法
    say() {
        console.log('miao')
    }
}

console.log(Cat.type, Cat.getName()) // 猫科动物 猫

export {}
```

`bundle.js`

```js
(function () {

    var extendStatics = function(d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };

    function __extends(d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    }

    var Animal = /** @class */ (function () {
        function Animal(name, age) {
            this.name = name;
            this.age = age;
        }
        Animal.getName = function () {
            return '动物';
        };
        Animal.type = '哺乳动物';
        return Animal;
    }());
    var Cat = /** @class */ (function (_super) {
        __extends(Cat, _super);
        function Cat(name, age, address) {
            var _this = _super.call(this, name, age) || this;
            _this.address = address;
            return _this;
        }
        Cat.getName = function () {
            console.log(_super.getName.call(this)); // 动物
            return '猫';
        };
        // 原型方法
        Cat.prototype.say = function () {
            console.log('miao');
        };
        Cat.type = '猫科动物';
        return Cat;
    }(Animal));
    console.log(Cat.type, Cat.getName()); // 猫科动物 猫

})();
//# sourceMappingURL=bundle.js.map

```

### 原型属性

原型属性也能不能直接写在类中呢，我们先写一下，看下编译后的结果

```ts
class Animal {

    public constructor(public name: string, public age: number) {

    }

    static type = '哺乳动物'

    static getName() {
        return '动物'
    }
}

class Cat extends Animal {
    public constructor(name: string, age: number, public readonly address: string) {
        super(name, age);
    }

    static type = '猫科动物'

    static getName() {
        console.log(super.getName())
        return '猫'
    }
    aaaaa = 1 // es7语法，不建议使用（会作为实例方法）
    // 原型方法
    say() {
        console.log('miao')
    }
}

console.log(Cat.type, Cat.getName()) // 猫科动物 猫

export {}
```

`aaaaa`被放在了实例上

`bundle.js`

```js
(function () {
    'use strict';

    var extendStatics = function(d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };

    function __extends(d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    }

    var Animal = /** @class */ (function () {
        function Animal(name, age) {
            this.name = name;
            this.age = age;
        }
        Animal.getName = function () {
            return '动物';
        };
        Animal.type = '哺乳动物';
        return Animal;
    }());
    var Cat = /** @class */ (function (_super) {
        __extends(Cat, _super);
        function Cat(name, age, address) {
            var _this = _super.call(this, name, age) || this;
            _this.address = address;
            _this.aaaaa = 1; // es7语法，不建议使用（会作为实例方法）
            return _this;
        }
        Cat.getName = function () {
            console.log(_super.getName.call(this));
            return '猫';
        };
        // 原型方法
        Cat.prototype.say = function () {
            console.log('miao');
        };
        Cat.type = '猫科动物';
        return Cat;
    }(Animal));
    console.log(Cat.type, Cat.getName()); // 猫科动物 猫

})();
//# sourceMappingURL=bundle.js.map

```

那么怎么加原型属性呢？

使用`get`修饰符（属性访问器）

```ts
class Animal {

    public constructor(public name: string, public age: number) {

    }

    static type = '哺乳动物'

    static getName() {
        return '动物'
    }
}

class Cat extends Animal {
    public constructor(name: string, age: number, public readonly address: string) {
        super(name, age);
    }

    static type = '猫科动物'

    static getName() {
        console.log(super.getName())
        return '猫'
    }
    // aaaaa = 1 // es7语法，不建议使用（会作为实例方法）
    // 原型属性
    // 使用属性访问器
    get content() {
        return 'aaa'
    }
    set content(newVal:string) {

    }
    // 原型方法
    say() {
        console.log('miao')
    }
}

console.log(Cat.type, Cat.getName()) // 猫科动物 猫

export {}
```

可以看到编译后，给`Cat.prototype`定义了属性

```js
(function () {
    'use strict';

    /******************************************************************************
    Copyright (c) Microsoft Corporation.

    Permission to use, copy, modify, and/or distribute this software for any
    purpose with or without fee is hereby granted.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
    REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
    INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
    LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
    OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
    PERFORMANCE OF THIS SOFTWARE.
    ***************************************************************************** */
    /* global Reflect, Promise */

    var extendStatics = function(d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };

    function __extends(d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    }

    var Animal = /** @class */ (function () {
        function Animal(name, age) {
            this.name = name;
            this.age = age;
        }
        Animal.getName = function () {
            return '动物';
        };
        Animal.type = '哺乳动物';
        return Animal;
    }());
    var Cat = /** @class */ (function (_super) {
        __extends(Cat, _super);
        function Cat(name, age, address) {
            var _this = _super.call(this, name, age) || this;
            _this.address = address;
            return _this;
        }
        Cat.getName = function () {
            console.log(_super.getName.call(this));
            return '猫';
        };
        Object.defineProperty(Cat.prototype, "content", {
            // aaaaa = 1 // es7语法，不建议使用（会作为实例方法）
            // 原型属性
            // 使用属性访问器
            get: function () {
                return 'aaa';
            },
            set: function (newVal) {
            },
            enumerable: false,
            configurable: true
        });
        // 原型方法
        Cat.prototype.say = function () {
            console.log('miao');
        };
        Cat.type = '猫科动物';
        return Cat;
    }(Animal));
    console.log(Cat.type, Cat.getName()); // 猫科动物 猫

})();
//# sourceMappingURL=bundle.js.map

```

属性访问器的好处：可以访问私有属性

```ts
class Animal {

    public constructor(public name: string, public age: number) {

    }

    static type = '哺乳动物'

    static getName() {
        return '动物'
    }

    // 父类中定义原型方法
    say() {
        console.log('父')
    }
}

class Cat extends Animal {
    public constructor(name: string, age: number, public readonly address: string) {
        super(name, age);
    }

    static type = '猫科动物'

    static getName() {
        console.log(super.getName())
        return '猫'
    }

    // 私有属性
    private str: string = ''

    get content() { // 访问器上不用加修饰符
        return this.str
    }

    set content(newVal: string) {
        this.str = newVal
    }

    say() { // 原型方法中的super指向的是父类的原型
        super.say()
    }
}

let cat = new Cat('Tom', 8, 'USA')
// 直接是拿不到str的
// console.log(cat.str)
cat.content = 'abc'
console.log(cat.content) // abc
export {}
```

`bundle.js`

```js
(function () {
    'use strict';

    /******************************************************************************
    Copyright (c) Microsoft Corporation.

    Permission to use, copy, modify, and/or distribute this software for any
    purpose with or without fee is hereby granted.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
    REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
    INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
    LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
    OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
    PERFORMANCE OF THIS SOFTWARE.
    ***************************************************************************** */
    /* global Reflect, Promise */

    var extendStatics = function(d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };

    function __extends(d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    }

    var Animal = /** @class */ (function () {
        function Animal(name, age) {
            this.name = name;
            this.age = age;
        }
        Animal.getName = function () {
            return '动物';
        };
        // 父类中定义原型方法
        Animal.prototype.say = function () {
            console.log('父');
        };
        Animal.type = '哺乳动物';
        return Animal;
    }());
    var Cat = /** @class */ (function (_super) {
        __extends(Cat, _super);
        function Cat(name, age, address) {
            var _this = _super.call(this, name, age) || this;
            _this.address = address;
            // 私有属性
            _this.str = '';
            return _this;
        }
        Cat.getName = function () {
            console.log(_super.getName.call(this));
            return '猫';
        };
        Object.defineProperty(Cat.prototype, "content", {
            get: function () {
                return this.str;
            },
            set: function (newVal) {
                this.str = newVal;
            },
            enumerable: false,
            configurable: true
        });
        Cat.prototype.say = function () {
            _super.prototype.say.call(this);
        };
        Cat.type = '猫科动物';
        return Cat;
    }(Animal));
    var cat = new Cat('Tom', 8, 'USA');
    // 直接是拿不到str的
    // console.log(cat.str)
    cat.content = 'abc';
    console.log(cat.content);

})();
//# sourceMappingURL=bundle.js.map

```



### 原型方法中的`super`

原型方法中的`super`，指向的是父类原型

我们在父类中，加上个`say`方法，并在子类中调用，最后实例上调用`say`方法

```ts
class Animal {

    public constructor(public name: string, public age: number) {

    }

    static type = '哺乳动物'

    static getName() {
        return '动物'
    }

    // 父类中定义原型方法
    say() {
        console.log('父')
    }
}

class Cat extends Animal {
    public constructor(name: string, age: number, public readonly address: string) {
        super(name, age);
    }

    static type = '猫科动物'

    static getName() {
        console.log(super.getName())
        return '猫'
    }

    get content() {
        return 'aaa'
    }
    set content(newVal:string) {

    }
    say() { // 原型方法中的super指向的是父类的原型
        super.say()
    }
}

let cat = new Cat('Tom', 8,'USA')
cat.say() // 父
console.log(cat)
export {}
```

![image-20220724164421552](/image-20220724164421552.png)

`bundle.js`

```js
(function () {
    'use strict';


    var extendStatics = function(d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };

    function __extends(d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    }

    var Animal = /** @class */ (function () {
        function Animal(name, age) {
            this.name = name;
            this.age = age;
        }
        Animal.getName = function () {
            return '动物';
        };
        // 父类中定义原型方法
        Animal.prototype.say = function () {
            console.log('父');
        };
        Animal.type = '哺乳动物';
        return Animal;
    }());
    var Cat = /** @class */ (function (_super) {
        __extends(Cat, _super);
        function Cat(name, age, address) {
            var _this = _super.call(this, name, age) || this;
            _this.address = address;
            return _this;
        }
        Cat.getName = function () {
            console.log(_super.getName.call(this));
            return '猫';
        };
        Object.defineProperty(Cat.prototype, "content", {
            get: function () {
                return 'aaa';
            },
            set: function (newVal) {
            },
            enumerable: false,
            configurable: true
        });
        Cat.prototype.say = function () {
            _super.prototype.say.call(this);
        };
        Cat.type = '猫科动物';
        return Cat;
    }(Animal));
    var cat = new Cat('Tom', 8, 'USA');
    cat.say(); // 父
    console.log(cat);

})();
//# sourceMappingURL=bundle.js.map

```

# 装饰器

`es7`中的

装饰器是一个实验性语法，语法会有改动，`vue2`中刚开始用的就是装饰器，要使用这个功能，需要注释掉`ts`配置文件中的`experimentalDecorator`选项，设置为`true`

装饰器的作用，就是扩展类中的属性和方法

可以在不同的类上，增加装饰器以增加不同的功能，实现复用

```ts
function addSay1(target:any) {
    console.log('1')
}

function addSay2(target:any) {
    console.log('2')

}

function addSay3(target:any) {
    console.log('3')

}

@addSay1
@addSay2
@addSay3
class Person {

}

// 等价于addSay1(addSay2(addSay3(Person)))
```

`bundle.js`



```js
(function () {
    'use strict';

    var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r; // 反向依此执行
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    function addSay1(target) {
        console.log('1');
    }
    function addSay2(target) {
        console.log('2');
    }
    function addSay3(target) {
        console.log('3');
    }
    /** @class */ ((function () {
        function Person() {
        }
        Person = __decorate([
            addSay1,
            addSay2,
            addSay3 // 是个数组
        ], Person);
        return Person;
    })());
    // 等价于addSay1(addSay2(addSay3(Person)))

})();
//# sourceMappingURL=bundle.js.map

```

 等价于`addSay1(addSay2(addSay3(Person)))`，结果：

![image-20220724190408049](/image-20220724190408049.png)

装饰器只能修饰类，不能修饰函数，因为函数会有变量提升的问题

## 洋葱模型

如果装饰器本身返回的是个函数

```ts
function addSay1(val: string) {
    console.log(val)
    return function (target: any) {
        console.log('1')
    }
}

function addSay2(val: string) {
    console.log(val)
    return function (target: any) {
        console.log('2')
    }
}


function addSay3(val: string) {
    console.log(val)
    return function (target: any) {
        console.log('3')
    }
}


@addSay1('a1')
@addSay2('a2')
@addSay3('a3') // 这里也可以写成多层@addSay3('a3')()()，只要返回值是一个函数，类似于函数柯里化
class Person {

}
```

结果：`a1 a2 a3 3 2 1`

![image-20220724191054323](image-20220724191054323.png)

`bundle.js`

```js
(function () {
    'use strict';

    var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    function addSay1(val) {
        console.log(val);
        return function (target) {
            console.log('1');
        };
    }
    function addSay2(val) {
        console.log(val);
        return function (target) {
            console.log('2');
        };
    }
    function addSay3(val) {
        console.log(val);
        return function (target) {
            console.log('3');
        };
    }
    /** @class */ ((function () {
        function Person() {
        }
        Person = __decorate([
            addSay1('a1'),
            addSay2('a2'),
            addSay3('a3')
        ], Person);
        return Person;
    })());

})();
//# sourceMappingURL=bundle.js.map

```

## 案例

### 修饰方法

使用装饰器，给`person`新增`eat`方法

`target`参数指向的是类

```ts
function eat(target: any) { // target参数指向的是类
    target.prototype.eat = function () {
        console.log('eat')
    }
}

@eat
class Person {
    eat!: () => void // 需要在Person类中先声明下
}

let p = new Person()
p.eat() // eat

```

`bundle.js`

```js
(function () {
    'use strict';

    var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    function eat(target) {
        target.prototype.eat = function () {
            console.log('eat');
        };
    }
    var Person = /** @class */ (function () {
        function Person() {
        }
        Person = __decorate([
            eat
        ], Person);
        return Person;
    }());
    var p = new Person();
    p.eat(); // eat

})();
//# sourceMappingURL=bundle.js.map

```



### 修饰属性

`target`参数指向的是原型（可以看编译后的代码）

```ts
function toUpperCase(target:any, key:string) { // target指的是原型

}

class Person {
    @toUpperCase
    public name: string = 'sai'
}

let p = new Person()
console.log(p.name)

```

`bundle.js`

```js
(function () {
    'use strict';

    var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    function toUpperCase(target, key) {
    }
    var Person = /** @class */ (function () {
        function Person() {
            this.name = 'sai';
        }
        __decorate([
            toUpperCase
        ], Person.prototype, "name", void 0); // 指向的是原型
        return Person;
    }());
    var p = new Person();
    console.log(p.name);

})();
//# sourceMappingURL=bundle.js.map

```

现在`toUpperCase`的功能，是想实现大写，该怎么玩

我们知道代码是顺序执行的，执行到`toUpperCase`的时候，`name`还没有赋值

装饰器中，使用`Object.defineProperty`给`target`（原型）增加`get`和`set`，这样在后面修改值的时候，就可以触发更新了

```ts
function toUpperCase(target: any, key: string) { // target指的是原型
    let val: string = ''
    Object.defineProperty(target, key, {
        get() {
            return val.toUpperCase()
        },
        set(newVal: string) { //给原型对象上，赋值的时候，就会触发set
            console.log(newVal)
            val = newVal
        }
    })
}

class Person {
    @toUpperCase
    public name: string = 'sai'
}

let p = new Person()
console.log(p.name)

```

![image-20220724225645165](image-20220724225645165.png)



### 修饰静态属性

```ts
function toUpperCase(target: any, key: string) { // target指的是原型
    let val: string = ''
    Object.defineProperty(target, key, {
        get() {
            return val.toUpperCase()
        },
        set(newVal: string) { //给原型对象上，赋值的时候，就会触发set
            val = newVal
        }
    })
}

function double(num:number) {
    return function (target:any, key:string) { // target指向类
        let val:number = target[key]
        Object.defineProperty(target, key,  {
            get() {
                return val * 2
            }
        })
    }
}
class Person {
    @toUpperCase
    public name: string = 'sai'

    @double(2)
    static age:number = 18
}

let p = new Person()
console.log(p.name, Person.age) // SAI 36

```

### 修饰静态方法







































































