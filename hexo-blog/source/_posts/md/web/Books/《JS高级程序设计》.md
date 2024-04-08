---
title: 《JavaScript高级程序设计（第4版）》
date: 2022-7-9 07:31:58
cover: false
tags:
- 书籍
categories: '书籍'
typora-root-url: 《JS高级程序设计》
---



**`JavaScript高级程序设计（第4版）`**

> 关于第四版出版的若干问题：https://www.zhihu.com/question/20825869
>
> 正如权威指南作者所说，最新的参考现在在网上可以轻易查到，还实时更新，不存在时效问题。他推荐的是 Mozilla 的 [MDN Web Docs](https://link.zhihu.com/?target=https%3A//wiki.developer.mozilla.org/zh-CN/) 和 Node 的 [Node.js参考文档](https://link.zhihu.com/?target=http%3A//nodejs.org/api)。



# 语言基础

## 语法

- 区分大小写
- 标识符
- 注释
- 严格模式
- 语句

## 关键字、保留字

这些词汇不能用作标识符，但现在还可以用作对象的属性名。一般来说，最好还是不要使用关键字和保留字作为标识符和属性名，以确保兼容过去和未来的 `ECMAScript` 版本。

## 变量

- `var`

  - `var`声明作用域

    - 局部变量

      ```js
      function test() { 
       var message = "hi"; // 局部变量
      } 
      test(); 
      console.log(message); // 出错！
      ```

    - 全局变量

      ```js
      function test() { 
       message = "hi"; // 全局变量
      } 
      test(); 
      console.log(message); // "hi"
      ```

      虽然可以通过省略 `var` 操作符定义全局变量，但不推荐这么做。

  - `var`声明提升

    ```js
    function foo() { 
     console.log(age); 
     var age = 26; 
    } 
    foo(); // undefined
    ```

    使用这个关键字声明的变量会自动提升到函数作用域顶部，等价于

    ```js
    function foo() { 
     var age; 
     console.log(age); 
     age = 26; 
    } 
    foo(); // undefined
    ```

    这就是所谓的“提升”（`hoist`），也就是把所有变量声明都拉到函数作用域的顶部。

    此外，反复多次使用` var` 声明同一个变量也没有问题：

    ```js
    function foo() { 
     var age = 16; 
     var age = 26; 
     var age = 36; 
     console.log(age); 
    } 
    foo(); // 36
    ```

    拓展阅读：[js变量声明底层原理分析](https://blog.csdn.net/brokenkay/article/details/107243640)

    > 等把数据结构和计算机组成原理肝完后，会整理成一个专题

## 数据类型

## 操作符

## 语句

## 函数

## 小结

# 变量、作用域与内存



# 基本引用类型



# 集合引用类型

## `Object`



## `Array`

### 操作方法

#### `concact()`：合并数组

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

#### `slice()`：截取数组

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

#### `splice()`：删除、插入或替换数组元素

- 删除：

  - 需要给 `splice()`**传 2 个参数**：要删除的第一个元素的位置和要删除的元素数量。
  - 可以从数组中删除任意多个元素，比如 `splice(0, 2)`会删除前两个元素。

- 插入

  - 需要给 `splice()`传 3 个参数：开始位置、0（要删除的元素数量）和要插入的元素，可以在数组中指定的位置插入元素。第三个参数之后还可以传第四个、第五个参数，乃至任意多个要插入的元素。
  - 比如，`splice(2, 0, "red", "green")`会从数组位置 2 开始插入字符串"`red`"和"`green`"。

- 替换（先删除，再替换）

  - `splice()`在删除元素的同时可以在指定位置插入新元素，同样要传入 3 个参数：开始位置、要删除元素的数量和要插入的任意多个元素。要插入的元素数量不一定跟删除的元素数量一致。
  - 比如，`splice(2, 1, "red", "green")`会在位置 2 删除一个元素，然后从该位置开始向数组中插入"red"和"green"。

- 我的思考：

  - 只要第二个参数不为0，就是删除元素了
  - 只要有两个以上的参数，就是插入元素了
  - 具体删了谁，插入了谁，在哪个位置插入的，看具体参数的值即可

- `splice()`方法始终返回这样一个数组，它包含从数组中被删除的元素（如果没有删除元素，则返回空数组）。

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

# 迭代器与生成器





# 对象、类与面向对象

## 理解对象

创建自定义对象的通常方式是创建 Object 的一个新实例

```js
let person = new Object();
console.dir(person)
```

这是一个没有任何属性和方法得空对象（默认有一个`[[Protoype]]`属性，可以通过`person.__proto__`获取到，指向`Object`）

![image-20220713162549927](image-20220713162549927-16577007533111.png)

- 问题：`person.__proto__`指向的`Object`，是始终指向`Object`，还是因为`Object`是构造函数呢？

  ```js
  function Person () {
      this.name = 'sai'
  }
  
  function Animal() {
      this.name = 'animal'
  }
  
  Person.prototype = Animal
  
  const p1 = new Person()
  console.dir(p1)
  ```

  ![image-20220713163207273](image-20220713163207273.png)

  上面提出问题角度就有问题，不能说`person`的`__proto__`属性，而是说成每个构造函数的实例，其默认的`__proto`属性值，是一个对象的引用，这个引用和构造函数的`prototype`属性值中保存的引用，是一致的。

  并且构造函数的`prototype`的引用，是可以被自定义修改的，以指向自定义对象

  而由于第一条的原则存在，即使`Person`的实例的隐式原型对象指向了`Animal`构造函数，在`Animal`函数对象中，也会有一个隐式原型对象指向`Object`构造函数

然后再给它添加属性和方法

```js
let person = new Object(); 
person.name = "Nicholas"; 
person.age = 29; 
person.job = "Software Engineer"; 
person.sayName = function() { 
 console.log(this.name); 
};
console.dir(person)
```

这个例子创建了一个名为 `person` 的对象，而且有三个属性（`name`、`age` 和 `job`）和一个方法（`sayName()`）。`sayName()`方法会显示 `this.name` 的值，这个属性会解析为 `person.name`。

![image-20220713164729421](image-20220713164729421.png)

### 属性的类型



### 定义多个属性



### 读取属性的特征



### 合并对象



### 对象标识及相等判断



### 增强的对象语法



### 对象解构



## 创建对象

### 概述

### 工厂模式



