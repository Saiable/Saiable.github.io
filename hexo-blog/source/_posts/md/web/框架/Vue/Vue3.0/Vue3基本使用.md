---
title: 'Vue3基本使用'
date: 2022-7-25 20:30:40
cover: false
toc_number: false
tags:
- Vue3
categories: Vue
typora-root-url: Vue3基本使用
---



> 本文承接《Vue2基本使用》

# 8.`Vue3`

## 8.1.`Vue3`快速上手

### 8.1.1.`Vue3`简介

- 2020年9月18日，`Vue.js`发布3.0版本，代号：`One Piece`（海贼王）
- 耗时2年多，<span style="color:red">2600+次提交、[30+个RFC](https://github.com/vuejs/rfcs)、600+次PR、99位贡献者</span>
- `github`上的`tags`地址：https://github.com/vuejs/core/tree/v3.2.36

### 8.1.2.`Vue3`带来了什么

#### 8.1.2.1.性能的提升

- 打包大小减少`41%`
- 初次渲染快`55%`，更新渲染快`133%`
- 内存减少`54%`
- ...

#### 8.1.2.2.源码的升级

- 使用`Proxy`代替`defineProperty`实现响应式
- 重写虚拟`dom`的实现和`tree-shaking`
- ...

#### 8.1.2.3.拥抱`TypeScript`

- `Vue3`可以更好的支持`tree-shaking`

#### 8.1.2.4.新特性

- `Composition API`（组合式`API`）
  - `setup`配置
  - `ref`和`reactive`
  - `watch`和`watchEffect`
  - `provide`和`inject`
  - ...
- 新的内置组件
  - `Fragment`
  - `Teleport`
  - `Suspense`
- 其他改变
  - 新的生命周期钩子
  - `data`选项应始终被声明为一个函数
  - 移除`keyCode`支持作为`v-on`的修饰符
  - ...

## 8.2.创建`Vue3`工程

### 8.2.1.使用`vue-cli`创建

官方文档：https://cli.vuejs.org/zh/guide/creating-a-project.html#vue-create

```bash
## 查看@vue/cli版本，确保@vue/cli版本在4.5.0以上
vue --version
# 或者
vue -V

## 安装或升级@vue/cli
npm install @vue/cli -g
## 或者
npm install @vue/cli -D

## 创建
vue create vue3_project
## 或者
npx vue create vue3_project

## 启动
cd vue_project3
npm run serve
```



### 8.2.2.使用`vite`创建

官方文档：https://v3.cn.vuejs.org/guide/installation.html#vite

什么是`vite`？新一代前端构建工具

优势：

- 开发环境中，无需打包操作，可快速的冷启动

- 轻量快速的热重载（`HMR`）

- 真正的按需编译，不再等待整个应用编译完成

- 传统构建与`vite`构建对比图

  <img src="bundler.37740380.png" alt="基于打包器的开发服务器" style="zoom:30%;" />

  <img src="esm.3070012d.png" alt="基于 ESM 的开发服务器" style="zoom:35%;" />

  



```bash
# npm 6.x
npm init vite@latest my-vue-app --template vue

# npm 7+, 需要额外的双横线：
npm init vite@latest my-vue-app -- --template vue

cd my-vue-app
npm install
npm run dev

```

### 8.2.3.分析工程结构

分析的是`vue-cli`方式创建的目录结构

#### `src/main.js`

```js
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')

```

- `import { createApp } from 'vue'`

  - 引入的不再是`Vue`构造函数了，而是一个名为`createApp`的工厂函数（无需通过`new`关键字调用）

- `createApp(App).mount('#app')`

  ```js
  const app = createApp(App)
  console.log(app)
  
  app.mount('#app')
  ```

  - 创建应用实例对象，`app`类似于`vue2`中的`vm`，但`app`比`vm`更轻

    ![image-20220607054736154](image-20220607054736154.png)

    

  - 注意，并不兼容之前的`new Vue`的写法，`import Vue from 'vue'`时，`Vue`时`undefined`

#### `App.vue`

- `template`中可以没有根标签

### 8.2.4.安装`vue3`对应的开发者工具

直接去官网：https://devtools.vuejs.org/guide/installation.html

## 8.3.常用`Composition API`

官方文档：

### 8.3.1.拉开序幕的`setup`

- 理解：`Vue3`中的一个新的配置项，值为一个函数

- `setup`是所有`Composition API`（组合`API`）表演的舞台

- 组件中所用到的：数据，方法等等，均要配置在`setup`中

- `setup`函数的两种返回值

  - 若返回一个对象，则对象中的属性、方法，在模板中均可以直接使用。（重点关注）

    ```js
    <template>
    	<h1>我是App组件</h1>
    	<h2>姓名： {{name}}</h2>
    	<h2>姓名： {{age}}</h2>
    	<button @click="sayHello">click</button>
    </template>
    
    <script>
    	export default {
    		name: 'App',
    		setup() {
    			let name = 'sai'
    			let age = 18
    			
    			function sayHello() {
    				alert(`你好呀，${name},今年我${age}岁了`)
    			}
    			
    			return {
    				name,
    				age,
    				sayHello
    			}
    		}
    
    	}
    </script>
    
    <style>
    
    </style>
    
    ```

    ![image-20220607064823164](image-20220607064823164.png)

  - 若返回一个渲染函数，则可以自定义渲染内容（了解）

    - 模板里的内容会被渲染函数的返回内容覆盖

    ```vue
    <template>
        <!-- 内容会被覆盖 -->
    	<h1>我是App组件</h1>
    </template>
    
    <script>
    	import {h} from 'vue'
    	export default {
    		name: 'App',
    		setup() {
    			// return () => {
    			// 	return h('h1', 'sai')
    			// }
    
    			// 简写
    			return () => h('h1', 'sai')
    		}
    
    	}
    </script>
    
    <style>
    
    </style>
    
    ```

    

- 注意点：

  - 尽量不要和`vue2.x`配置混用
    - `vue2.x`配置（`data`、`methods`、`computed`...）中可以访问到`setup`中的属性和方法
    - 但在`setup`中不能访问到`vue2.x`配置（`data`、`methods`、`computed`...）
    - 如果有重名，`setup`优先
  - `setup`不能是一个`async`函数，因为返回值不再是`return`的对象，而是`promise`，模板中看不到对象中的属性（后期学到了`Suspence`，其实是可以的）

### 8.3.2.`ref`函数

`vue2`中的`ref`是一个标签属性，`vue3`中多了一个同名的函数

#### 8.3.2.1`ref`函数处理基本数据类型

```vue
<template>
  <h1>我是App组件</h1>
  <h2>姓名：{{name}}</h2>
  <h2>年龄：{{age}}</h2>
  <button @click="modifyInfo">修改信息</button>
</template>

<script>
export default {
  name: 'App',
  setup() {
    let name = 'sai'
    let age = 18

    function modifyInfo() {
      name = 'sai_change'
      age = 19
      console.log(name, age)
    }

    return {
      name,
      age,
      modifyInfo
    }
  }

}
</script>

<style>

</style>

```

这个案例中，我们修改了数据，但是页面上并没有更新



![image-20220607090829602](image-20220607090829602.png)

因为`vue`并没有监视到数据的变化，上述方式定义的数据并不是响应式数据

如何把普通的数据，变成一个能被`vue`监测到的响应式数据呢？

借助`ref`函数

```vue
<script>
import {ref} from 'vue'
export default {
  name: 'App',
  setup() {
    let name = ref('sai')
    let age = ref(18)

    function modifyInfo() {
      name = 'sai_change'
      age = 19
      console.log(name, age)
    }

    return {
      name,
      age,
      modifyInfo
    }
  }

}
</script>
```

那么直接能这样改吗？不能！！！上述代码执行后，点击修改按钮页面仍然没有变化

为啥咧？因为我们改的地方不对！！

我们先注释掉修改的两行代码，直接打印被`ref`包裹的`name`和`age`

![image-20220607092144979](image-20220607092144979.png)

- `RefImpl`：`Refenrence Implement`（引用的实现），表示一个引用实现对象

- `RefImpl`对象也是通过`Object.defineProperty`实现数据响应式的

  - 类比于`vue2`的`_data`身上的属性，为了便于读写，给了`vm`一份属性
  - `RefImpl`对象的原型对象上定义着`getter`和`setter`，然后又给了`RefImpl`对象一份属性

- 读写数据会根据原型链查找`getter`和`setter`

  - 读数据

    ```vue
      <h2>姓名：{{name}}</h2>
      <h2>年龄：{{age}}</h2>
    ```

    插值语法中，不用写成`name.value`和`age.value`，`vue`在解析模板读取数据时，如果变量是一个`RefImpl`引用实现对象，则会自动读取其`value`的属性值

    - 读数据，会调用引用实现对象的原型对象的`getter`

  - 写数据

    ```vue
    <script>
    import {ref} from 'vue'
    export default {
      name: 'App',
      setup() {
        let name = ref('sai')
        let age = ref(18)
    
        function modifyInfo() {
          name.value = 'sai_change'
          age.value = 19
          console.log(name, age)
        }
    
        return {
          name,
          age,
          modifyInfo
        }
      }
    
    }
    </script>
    ```

    - 写数据，会调用引用实现对象的原型对象的`setter`

    - `setter`内部封装更新页面的逻辑

    - 此时页面更新了

      ![image-20220607094215557](image-20220607094215557.png)

#### 8.3.2.2.`ref`函数处理对象数据类型

先梳理一下`ref`函数处理基本数据类型的逻辑

- 通过`ref`函数包裹基本数据类型，返回一个引用实现对象，可以通过`value`属性，取得包裹的数据的值
- 响应式实现方式，通过`Object.defineProperty`在其原型对象上定义`getter`和`setter`



按照类似的逻辑，`ref`函数处理对象类型的数据，也应该是这样的

- 使用`ref`包裹对象类型的数据

  ```vue
  <template>
    <h1>我是App组件</h1>
    <h2>姓名： {{person.name}}</h2>
    <h2>年龄： {{person.age}}</h2>
    <button @click="modifyInfo">修改信息</button>
  </template>
  
  <script>
  import {ref} from 'vue'
  export default {
    name: 'App',
    setup() {
  
      let person = ref({
        name: 'sai',
        age: 18
      })
  
      function modifyInfo() {
      }
  
      return {
        person,
        modifyInfo
      }
    }
  
  }
  </script>
  ```

  ![image-20220607100950658](image-20220607100950658.png)

- 根据`vue2`的经验，`vue3`应该会对对象的每个属性，都设置`getter`和`setter`，所以我们修改`age`属性时，应该是`person.value.age.value=19`

  ```vue
  <template>
    <h1>我是App组件</h1>
    <h2>姓名： {{person.name}}</h2>
    <h2>年龄： {{person.age}}</h2>
    <button @click="modifyInfo">修改信息</button>
  </template>
  
  <script>
  import {ref} from 'vue'
  export default {
    name: 'App',
    setup() {
  
      let person = ref({
        name: 'sai',
        age: 18
      })
  
      function modifyInfo() {
          // 修改数据
          person.value.name.value = 'sai_modify'
          person.value.age.value = 19
      }
  
      return {
        person,
        modifyInfo
      }
    }
  
  }
  </script>
  ```

  但是，此时修改不了

  ![image-20220607101141197](image-20220607101141197.png)

- 为啥咧

  - 打印下`person`引用实现对象，以及`value`属性

    ```js
        function modifyInfo() {
          // 修改数据
          // person.value.name.value = 'sai_modify'
          // person.value.age.value = 19
          console.log(person)
          console.log(person.value)
        }
    ```

    ![image-20220607101407849](image-20220607101407849.png)

  - 可以看到，`ref`函数处理对象数据类型，用的是`ES6`中的`Proxy`，关于`Proxy`下一小节详细讲解

#### 8.3.2.3.小结：`ref`函数

- 作用：定义一个响应式的数据
- 语法：`const xxx = ref(initValue)`
  - 创建一个包含响应式数据的引用对象（`reference`对象）
  - `JS`中操作数据：`xxx.value`
  - 模板中读取数据，不需要`.value`，直接`<div>{{xxx}}</div>`
- 备注：
  - 接收的数据可以是基本数据类型，也可以是对象数据类型
  - 基本数据类型：响应式依然靠的是`Object.defineProperty`的`get`与`set`
  - 对象数据类型：内部`求助`了`Vue3`中的一个新函数——`reactive`函数

### 8.3.3.`reactive`函数

将源对象交给`reactive`处理，返回的是一个代理对象

#### 8.3.3.1.返回的是`Proxy`对象

```vue
<template>
  <h1>我是App组件</h1>
  <h2>姓名： {{person.name}}</h2>
  <h2>年龄： {{person.age}}</h2>
  <button @click="modifyInfo">修改信息</button>
</template>

<script>
import {reactive} from 'vue'

export default {
  name: 'App',
  setup() {
    let person = reactive({
      name: 'sai',
      age: 18
    })
    function modifyInfo() {
      console.log(person) // 这里不用.value，直接使用即可
    }
    return {
      person,
      modifyInfo
    }
  }
}
</script>

```

![image-20220607110312006](image-20220607110312006.png)

将源数据改成了`Proxy`类型的对象

#### 8.3.3.2.修改对象数据类型

此时可以直接修改对象类型的数据了

```vue
<template>
  <h1>我是App组件</h1>
  <h2>姓名： {{person.name}}</h2>
  <h2>年龄： {{person.age}}</h2>
  <button @click="modifyInfo">修改信息</button>
</template>

<script>
import {reactive} from 'vue'

export default {
  name: 'App',
  setup() {
    let person = reactive({
      name: 'sai',
      age: 18
    })
    function modifyInfo() {
      // 修改数据
      person.name = 'sai_modify'
      person.age = 19
      console.log(person)
    }
    return {
      person,
      modifyInfo
    }
  }
}
</script>

```

![image-20220607111003887](image-20220607111003887.png)

#### 8.3.3.3.修改嵌套的对象数据

即使对象嵌套的很深，`reactive`函数也可以监测到其变化：

```vue
<template>
  <h1>我是App组件</h1>
  <h2>姓名： {{person.name}}</h2>
  <h2>年龄： {{person.age}}</h2>
  <h2>测试数据： {{person.a.b.c}}</h2>
  <button @click="modifyInfo">修改信息</button>
</template>

<script>
import {reactive} from 'vue'

export default {
  name: 'App',
  setup() {
    let person = reactive({
      name: 'sai',
      age: 18,
      a: {
        b: {
          c: 'test'
        }
      }
    })

    function modifyInfo() {
      person.name = 'sai_modify'
      person.age = 19
      person.a.b.c = 'test_modify'
      console.log(person)

    }
    return {
      person,
      modifyInfo
    }
  }

}
</script>
```

![image-20220607111533470](image-20220607111533470.png)



#### 8.3.3.4.修改数组数据类型

被`reactive`包裹的数组，可以直接通过索引来修改数组类型的数据

```vue
<template>
  <h1>我是App组件</h1>
  <h2>爱好：{{hobby}}</h2>
  <button @click="modifyInfo">修改信息</button>
</template>

<script>
    import {reactive} from 'vue'

    export default {
        name: 'App',
        setup() {
            let hobby = reactive(['eat','drink'])

            function modifyInfo() {
                hobby[0] = 'sleep'
                console.log(hobby)

            }
            return {
                hobby,
                modifyInfo
            }
        }

    }
</script>
```

修改后的效果：

![image-20220617065538228](image-20220617065538228.png)

#### 小结：`reactive`函数

- 作用：定义一个对象类型的响应式数据（基本数据类型不要用它，要用`ref`函数）
- 语法：`const 代理对象 =  reactive(源对象)`，接收一个对象（或数组），返回一个代理对象（`Proxy`的实例对象，简称`Proxy`对象）
- `reactive`定义的响应式数据是`深层次的`
- 内部基于`ES6`的`Proxy`实现，通过代理对象操作源对象的内部数据

### 8.3.4.`Vue3`中的响应式原理

#### 8.3.4.1.`Vue2`的响应式

- 实现原理：

  - 对象类型：通过`Object.defineProperty()`对属性的读取、修改进行拦截（数据劫持）

    ```js
    Object.defineProperty(data, 'count', {
      get() {},
      set() {}
    })
    ```

  - 数组类型：通过重写更新数组的一系列方法来进行拦截。（对数组的变更方法进行了包裹）

- 存在问题：

  - 对象类型：新增属性、删除属性，界面不会更新

    - 新增的属性，要通过`this.$set`或`Vue.set`才会变成响应式的

      ```js
      this.$set(this.person, 'sex', '女')
      ```

    - 删除的属性，要通过`this.$delete`或`Vue.delete`才会变成响应式的

      ```js
      this.$delete(this.person, 'name')
      ```

  - 数组类型：直接通过下标修改数组，界面不会自动更新

    - 要通过`this.$set`或`Vue.set`才会变成响应式的

      ```js
      this.$set(this.person.hobby, 0, '逛街')
      ```

    - 或者调用`splice`方法

      ```js
      this.person.hobby.splice(0, 1, '逛街')
      ```

#### 8.3.4.2.`Vue3`的响应式

- 实现原理：
  - 通过`Proxy`（代理）：拦截对象中任意属性的变化，包括：属性值的读写、属性的添加、删除等
  - 通过`Reflect`（反射）：对被代理对象的属性进行操作
  - `MDN`文档中描述的`Proxy`和`Reflect`
    - `Proxy`：https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy
    - `Refelct`：https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Reflect
- 验证对象的操作
- 验证数组的操作
- 模拟`Vue2`的响应式
- 模拟`Vue3`的响应式
  - 验证`Proxy`基本语法
    - 读取：`get`
    - 修改和新增：`set`
    - 删除：`deleteProperty`
  - 验证`Reflect`基本语法
    - 获取属性值
    - 修改属性值
    - 删除属性
    - `ECMA`正在尝试把`Object`上的方法，移植到`Reflect`身上
      - `Obeject.defineProperty`
        - 基本使用
        - 一旦有异常就会挂掉，除非用`try catch`捕获到
      - `Reflect.defineProperty`
        - 基本使用
        - 会有布尔类型的返回值，异常处理比较方便
        - 对于框架封装来说，使用`Reflect`相对会好一点
  - 使用`Reflect`配合`Proxy`

### 8.3.5.`reactive`对比`ref`

- 从定义数据角度对比
  - `ref`用来定义：基本数据类型
  - `reactive`用来定义：对象（或数组）类型数据
  - 备注：`ref`也可以用来定义对象（或数组）类型数据，它内部会自动通过`reactive`转为代理对象
- 从原理角度对比
  - `ref`通过`Object.defineProperty()`的`get`与`set`来实现响应式（数据劫持）
  - `reactive`通过使用`Proxy`来实现响应式（数据劫持），并通过`Reflect`操作源对象内部的数据
- 从使用角度对比
  - `ref`定义的数据：操作数据需要`.value`，读取数据时模板中直接读取不需要`.value`

### 8.3.6.`setup`的两个注意点

#### 8.3.6.1.`setup`执行的时机

- 在`beforeCreate`之前执行一次，`this`是`undefined`


#### 8.3.6.2.`setup`的参数

##### 参数验证

```js
set(a, b, c) {
    console.log(a, b, c)
}
```

图片

##### `props`参数

值为对象，包含：组件外部传递过来，且在组件内部声明接收了的属性

- `vue2`中的`props`

  - 如果使用`props`接收了，传的数据挂载在`vc`实例上

  - 如果没有使用`props`接收，传的数据挂载在`$attrs`上 

- `vue3`中的`props`

  `App.vue`

  ```vue
  <template>
  	<Demo msg='hello' addredd='beijing'/>
  </template>
  <script>
  	import Demo from './components/Demo'
      export default {
          name: 'App',
          components: {
              Demo
          }
      }
  </script>
  ```

  

  `Demo.vue`

  ```js
  export default {
      props: ['msg', 'address'],
      set(props) {
          console.log(props)// 会把接收到的所有props的值，整理成`Proxy`类型的对象
      }
  }
  ```

##### `context`参数

- 上下文对象，身上有三个属性使我们关心的

- `attrs`

  - `vue2`的`$attrs`
    - 父组件给子组件传了数据，子组件如果没有使用`props`接收，则会放在`this.$attrs`对象上
  - `vue3`的`attrs`
    - 如果没有使用`props`接收到的数据，会放在`attrs`属性上，相当于`vue2`的`this.$attrs`

- `emit`

  - 如果给子组件绑定了自定义事件，`vue3`中需要使用`emits`数组配置项，在子组件中来接收命名，否则控制台会有警告

- `slots`

  - `vue2`中的插槽
    - 子组件的对象标签中，写了新的标签内容，会以虚拟`dom`的形式，挂载在父组件的`$slot`属性上（不论子组件有没有使用插槽来接收）

  - `vue3`中的插槽
    - 子组件的对象标签中，写了新的标签内容，会以虚拟`dom`的形式，`slots`属性上（不论子组件有没有使用插槽来接收）
    - `vue3`中的具名插槽的写法，请使用`v-slot:name`，不要使用`vue2`的`slot="name"`这种写法

#### 小结：`setup`的两个注意点

- `setup`执行的时机

  - 在`beforeCreate`之前执行一次，`this`是`undefined`

- `setup`的参数

  - `props`参数：值为对象，包含：组件外部传递过来，且组件内部声明接收了的属性

  - `context`参数：上下文对象

    - `attrs`：值为对象，包含：组件外部传递过来，但没有在`props`配置中声明的属性，相当于`this.$attrs`
    - `slot`：收到的插槽内容，相当于`this.$slots`

    - `emit`：分发自定义事件的函数，相当于`this.$emit`

### 8.3.7.计算属性与监视

#### 8.3.7.1.`computed`函数

- 与`vue2.x`中`computed`配置功能一致

- 写法：

  ```vue
  <template>
  	<h2>
          {{person.fullName}}
      </h2>
  </template>
  <script>
  	import {reactive, computed} from 'vue'
      export default {
          setup() {
              // 数据
              let person = reactive({
                  firstName: '张',
                  lastName: '三'
              })
              
              // 计算属性简写
              // 注意可以直接给Proxy类型的person对象上，添加计算属性，也是响应式的
              person.fullName1 = computed(() => { 
                  return person.firstName + '-' + person.lastName
              })
  
              // 计算属性完整写法
              person.fullName2 = computed({
                  get() {
                      return person.firstName + '-' + person.lastName
                  },
                  set(value) {
                      const nameArr = value.split('-')
                      person.firstName = nameArr[0]
                      person.lastName = nameArr[1]
                  }
              })
              
              return {
                  person            }
      	}  
  }
  </script>
  
  ```

计算属性返回的时是ref对象，如果要转换成reactive对象，参考如下：

```js
import { computed, ref } from 'vue';

const myRef = ref({ count: 0 });

const myComputed = computed(() => {
  return myRef;
});


```

`ref`转换成`reactive`

```js
import { reactive, toRefs } from 'vue';

const myReactiveData = reactive(toRefs(myComputed.value));
console.log(myReactiveData.count); // Reactive: This will be reactive, no need to use .value.
```

子组件接受父组件传值后，如果自己想存一份并设置为响应式，可以使用如下代码：

```js
const props = defineProps(["item", "index"])
// 深拷贝一份
const localItem = computed(() => {
  return JSON.parse(JSON.stringify(props.item))
})
// 将ref转换为reactive
const reactiveLocalItem = reactive(localItem.value)
```



#### 8.3.7.2.`watch`函数

- 与`vue2.x`中`watch`配置功能一致，接收三个参数

  - 监视的是谁
  - 监视的回调
  - 监视的配置

- 两个注意点

  - 监视`reactive`定义的响应式数据时，`oldValue`无法正确获取、强制开启了深度监视（`deep`配置失效）
  - 监视`reactive`定义的响应式数据中某个属性时，`deep`配置有效

- 监视`ref`定义的响应式数据

  写监视的对象时，监视的应该是一个结构，而不是具体的值

  - 如果是基本数据类型，不需要添加`.value`；
  - 如果使用`ref`包裹了对象类型数据，监视时需要添加`.value`
    - `RefImp`对象的`value`此时不再是一个具体的值，而是一个`Proxy`对象，再怎么修改这个对象里面的值，这个对象的内存地址也不会变，自然也就监视不到变化了
    - 所以真正的要监视的，应该是通过`.value`获取到的`Proxy`对象
    - 或者也可以不加`.value`，但是要添加深度监视配置项

  ```js
  watch(sum, (newValue, oldValue) => {
      console.log('sum变化了', newVlaue, oldValue)
  }, {immediate: true})
  ```

- 监视多个`ref`定义的响应式数据

  ```js
  watch([sum, msg], (newValue, oldValue) => {
      console.log('sum或msg变化了', newValue, oldValue)
  })
  ```

  输出的也是数组：

  ![image-20220618143803425](image-20220618143803425.png)

- 监视`reactive`定义的响应式数据

  - 若`watch`监视的是`reactive`定义的响应式数据，则无法正确获得`oldValue`，`newValue`和`oldValue`都是`Proxy`类型的对象

    ![image-20220618144135227](image-20220618144135227.png)

    如果一定要获取`oldValue`，则用`ref`定义源数据

  - 若`watch`监视的是`reactive`定义的响应式数据，则强制开启了深度监视（默认开启了），并且关闭不再生效

    ```js
    watch(person, (newValue, oldValue) => {
        console.log('person变化了', newValue, oldValue)
    },{immediate: true, deep: false}) // 此处的deep配置不再奏效
    ```

- 监视`reactive`定义的响应式数据中的某个属性，第一个参数要写成一个函数，此时的`deep`配置项是有效的

  ```js
  watch(() => person.age, (newValue, oldValue) => {
      console.log('preson的age变化了', newValue, oldValue)
  }) 
  ```

  一般监视的属性是一个对象时，才会开启深度监视（获取不到`oldValue`）

  ```js
  watch(() => person.job, (newValue, oldValue) => {
      console.log('preson的job变化了', newValue, oldValue)
  }, {immediate: true, deep: true}) // job中还有salary属性，可以开启深度监视
  ```

- 监视`reactive`定义的响应式数据中的某些属性

  ```js
  watch([() => person.job, () => person.name], (newValue, oldValue) => {
      console.log('preson的job或name变化了', newValue, oldValue)
  }, {immediate: true, deep: true})
  ```



#### 8.3.7.3.`watchEffect`函数

- `watch`的套路是：既要指明监视的属性，也要指明监视的回调

- `watchEffect`的套路是，不用指明监视的是哪个属性，监视的回调中用到哪个属性，那就监视哪个属性

- `watchEffect`有点像`computed`：

  - 但`computed`注重计算出来的值（回调函数的返回值），所以必须要写返回值

  - 而`watchEffect`更注重的是过程（回调函数的函数体），多以不用写返回值

    ```js
    // watchEffect所指定的回调中，用到的数据只要发生了变化，则直接重新执行回调
    watchEffect(() => {
        const x1 = sum.value
        const x2 = person.age
        console.log('watchEffect配置的回调执行了')
    })
    ```

    

### 8.3.8.生命周期

- `vue3`中可以继续使用`vue2`中的生命周期钩子，但有两个被更名：
  - `beforeDestroy`改名为`beforeUnmount`
  - `destroyed`改名为`unmounted`
- `vue3`中也提供了`Compsition API`形式的生命周期钩子，与`vue2`中钩子的对应关系如下：
  - `beforeCreate`===>`setup()`
  - `created`===>`setup()`
  - `beforeMount`===>`onBeforeMount`
  - `mounted`===>`onMounted`
  - `beforeUpdate`===>`onBeforeUpdate`
  - `updated`===>`onUpdated`
  - `beforeUnmount`===>`onBeforeUnmount`
  - `unmounted`===>`onUnmounted`
  - 备注：使用时需要引入

### 8.3.9.自定义`hook`函数

- 什么是`hook`
  - 本质是一个函数，把`setup`函数中使用的`Composition API`进行了封装
  - 类似`vue2`中的`mixin`
- 自定义`hook`的优势
  - 复用代码，让`setup`中的逻辑更清楚易懂

定义`hook`

`hook/usePoint.js`

```js
import {reactive, onMounted, onBeforeUnmount} from 'vue'

export default function() {
    let point = reactive({
        x: 0,
        y: 0
    })
    
    function savePoint(event) {
        point.x = event.pageX
        point.y = event.pageY
        console.log(event.pageX, event.pageY)
    }
    
    onMounted(() => {
        window.addEventListener('click', savePoint)
    })
    
    onBeforeUnmount(() => {
        window.removeEventListener('click', savePoint)
    })
    
    return point
}
```

使用`hook`

```vue
<template>
	<h2>
        当前点击鼠标时的坐标为：x：{{point.x}}，y：{{point.y}}
    </h2>
</template>
<script>
	import userPoint from '../hooks/usePoint'
    export default {
        setup() {
            const point = usePoint()
            return {
                point
            }
        }
    }
</script>
```



### 8.3.10.`toRef`

使用`reactive`包裹深层次对象，在使用时需要写多个点，很麻烦，可以用`toRef`来替代这个操作

```vue
<template>
	<!-- 此时不需要person.name -->
	<h2>{{name}}</h2>
</template>
<script>
	import {reactive, toRef} from 'vue'
    export default {
        setup() {
            let person = {
                name: 'sai',
                age:18,
                job: {
                    j1: {
                        salary: 30
                    }
                }
            }
            
            const name = toRef(person, 'name') // 返回的是一个引用实现对象，其value指向person.name，如果使用ref(person, 'name')，则是复制创建了一个新的引用实现对象，不存在引用关系了
            const salary = toRef(person.job.j1, 'salary') // 第一个参数，传递一个对象
            return {
                person, 
                name, // 需要单独使用的属性
                salary // 简写形式，等价于salary: toRef(person.job.j1, 'salary')
            }
        }
    }
</script>
```

小结：

- 作用，创建一个`ref`对象，其`value`值指向另一个对象中的某个属性

- 语法：`const name = toRef(person, 'name')`

- 应用：要将响应式对象中的某个属性，单独提供给外部使用时

- 扩展：`toRefs`与`toRef`功能一致，但可以批量创建多个`ref`对象，语法：`toRefs(person)`

  ```js
  const x = toRefs(person)
  console.log(x)
  ```

  ![image-20220620064618982](image-20220620064618982.png)

  返回值是一个对象，`return`的时候需要解构赋值

  返回对象的`key`，是源对象的`key`，

  - 若源对象`key`是基本数据类型，则`key`对应的属性值，是一个引用实现对象，模板中使用时不用加`.value`进行调用，
  - 若源对象`key`的值仍是一个对象，则`key`对应的属性值，是一个`Proxy`实例对象

  ```js
  return {
      ...toRefs(person)
  }
  ```


###   8.3.11.`toRefs`

toRefs函数的作用是将响应式对象中的所有属性转换为单独的响应式数据，对象成为普通对象，并且值是关联的。在这个过程中toRefs会做以下两件事：

- 把一个响应式对象转换成普通对象
- 对该普通对象的每个属性都做一次ref操作，这样每个属性都是响应式的

说明：

- reactive 对象取出的所有属性值都是非响应式的，而利用 toRefs 可以将一个响应式 reactive 对象的所有原始属性转换为响应式的 ref 属性。
- reactive的响应式功能是赋值给对象，如果展开对象，会让数丢失响应的能力
- 使用toRefs可以保证对象展开的每个属性都是响应式的

应用场景：

- 展开响应式对象时，想使用响应式对象中的多个或者所有属性做为响应式数据。
- 当函数返回响应式对象时，toRefs非常有用，这样消费组件就可以在不丢失响应式的情况下对返回的对象进行分解使用。-
  

```vue
<template>
    <h2>姓名：{{name}}</h2>
    <h2>年龄：{{age}}</h2>
    <h2>地址：{{addr.province}}-{{addr.city}}</h2>
    <button @click="name='zhangsan'">修改名字</button>
</template>
<script>
    import { reactive, toRefs } from 'vue'
    export default {
        setup() {
            const user = reactive({
                name: '张三',
                age: 19,
                addr: {
                    province: '河南',
                    city: '郑州'
                }
            })
            return {
                ...toRefs(user)
            }
        }
    }
</script>

```







## 8.4.其它`Composition API`

### 8.4.1.`shallowReactive`和`shallowRef`

- `shallowReactive`：只处理对象最外层属性的响应式（浅响应式）

- `shallowRef`：只处理基本数据类型的响应式，不进行对象的响应式处理

  - 传的是基本类型，和`ref`一样

  - 传的是对象类型数据，就不再求助于`reactive`了，就不再是响应式了

    ![image-20220620071743944](image-20220620071743944.png)

- 什么时候使用

  - 如果有一个对象数据，结构比较深，但变化时只是外层属性变化，使用`shallowReactive`
  - 如果有一个对象数据，后续功能不会修改该对象中的属性，而是生成新的对象来替换，使用`shallowRef`

### 8.4.2.`readonly`与`shallowReadonly`

- `readonly`：让一个响应式数据变为只读的（深只读）

  - `readonly`是一个函数，接收响应式数据作为参数

    ```js
    setup() {
        let person = reactive({
            name: 'sai',
            age: 18,
            job: {
                j1: {
                    salary: 30
                }
            }
        })
        person = readonly(person)
        return {
            ...toRefs(person)
        }
    }
    ```

    

- `shallowReadonly`：让一个响应式数据变为只读的（浅只读）

  ```js
  person = shallowReadonly(person)
  ```

  上述例子中，若使用`shallowReadonly`函数进行处理，则第一层数据不允许修改，但是里面的`salary`还是可以修改的

  对于`ref`包裹的响应式数据，没有必要用`shallowReadonly`，因为基本数据类型始终就是一层

- 应用场景：不希望数据被修改时

  - `person`的数据不是自己定义的，用的是别人的组件，接收的时候可以用`readonly`限制一下，防止误操作


### 8.4.3.`toRaw`与`markRaw`

- `toRaw`

  - 作用：将一个由`reactive`生成的响应式对象，变成普通对象（不能处理`ref`定义的响应式数据）

    ```js
    let person = reactive({
        name: 'sai',
        age: 18
    })
    
    function showRawPerson() {
        const p = toRaw(person)
        console.log(p)
    }
    ```

  - 应用场景：用于读取响应式对象对应的普通对象，对这个普通对象的所有操作，不会引起页面更新

- `makeRaw`

  - 作用：标记一个对象，使其永远不会再成为响应式对象
    - 但是对于数据的更改仍然是生效的，只是`vue`不再做响应式处理了
  - 应用场景：
    - 有些值不应被设置为响应式的，例如复杂的第三方类库等
    - 当渲染具有不可变数据源的大列表时，跳过响应式转换可以提高性能

### 8.4.4.`customRef`

- 作用：创建一个自定义的`ref`，并对其依赖项跟踪和更新触发，进行显示控制

  - 读数据找`get()`，写数据找`set()`
  - 在关键的地方调用`track`和`trigger`

- 实现防抖效果

  ```vue
  <template>
  	<input type="text" v-model="keyword">
  	<h3>
          {{keyword}}
      </h3>
  </template>
  <script>
  	import {ref, customRef} from 'vue'
      export default {
          name: 'Demo',
          setup() {
              // let keyword = ref('hello') // 使用vue准备好的内置的ref
              // 自定义一个myRef
              function myRef(value, delay) {
                  let timer
                  // 通过customRef去实现自定义
                  return customRef((track, trigger) => {
                  	return {
                          get() {
                              track() // 告诉vue这个value值是需要被“追踪”的
                              return value
                          },
                          set(newValue) {
                              clearTimeout(timer)
                              timer = setTimeout(() => {
  								value = newValue	
                                  trigger() // 告诉vue去更新页面
                              }, delay)
                          }
                      }
                  })
              }
              
              let keyword = myRef('hello', 500)
              return {
                  keyword
              }
          }
      }
  </script>
  ```

### 8.4.5.`provide`与`inject`

![image-20220620163000601](image-20220620163000601.png)

- 作用：实现**祖组件**与**后代组件**间通信

  - 虽然也可以用来父子组件通信，但那样直接用`props`即可

- 套路：父组件有一个`provide`选项来提供数据，后代组件有一个`inject`选项来开始使用这些数据

- 具体写法：

  - 1.祖先组件中

    ```js
    import {provide} from 'vue'
    ...
    setup() {
        ...
        let person = reactive({
            name: 'sai',
            age: 18
        })
        provide('person', person)
    }
    ```

  - 2.孙子组件中

    ```js
    import {inject} from 'vue'
    
    setup() {
        ...
        const person = inject('person')
        return {person}
    }
    ```

    

### 8.4.6.响应式数据的判断

- `isRef`：检查一个值，是否为一个`ref`对象
- `isReactive`：检查一个对象，是否是由`reactive`创建的响应式代理
- `isReadonly`：检查一个对象，是否是由`readonly`创建的只读代理
- `isProxy`：检查一个对象，是否是由`reactive`或者`readonly`方法创建的代理

## 8.5.`Composition API`的优势

### 8.5.1.`Options API`存在的问题

使用传统`Options API`，新增或者修改一个需求，就需要分别在`data`、`methods`、`computed`里修改

![image-20220620164219772](image-20220620164219772.png)

如果一个组件里的功能特别多

- 一个功能的数据、方法、计算属性都是拆散的
- 每个配置项里堆积了不同功能的代码
- 维护某一个功能代码时，就需要打开一个庞大的`data`找啊找，然后再打开一个庞大的`method`找啊找，可能还要去`computed`、`watch`、生命周期钩子里不断的查找修改

### 8.5.2.`Composition API`的优势

我们可以更加优雅的组织我们的代码，函数。让相关功能的代码更加有序的组织在一起

![image-20220620165208346](image-20220620165208346.png)

![image-20220620164953100](image-20220620164953100.png)

![image-20220620165019824](image-20220620165019824.png)

## 8.6.新的组件

### 8.6.1.`Fragment`

- 在`vue2`中，组件必须有一个根标签

- 在`vue3`中，组件可以没有根标签，内部会将多个标签包含在一个`Fragment`虚拟元素中

  - 好处：减少标签层级，减小内存占用

  ![image-20220620170100495](image-20220620170100495.png)

### 8.6.2.`Teleport`

- `Teleport`是一种能够将我们的**组件`html`结构**移动到指定位置的技术

- 后代组件中，直接显示的弹窗，会被包裹在`dom`结构内，即使可以使用定位，但组件嵌套一多，写起来也麻烦

  - `移动位置`可写的值：
    - `body`
      - 组件的嵌套再多，渲染的`dom`结构，也是直接在`body`下的
    - `css`选择器

  ```vue
  <teleport to='移动位置'>
  	<div v-if='isShow' class='mask'>
          <div class='dialog'>
              <h3>
                  我是一个弹窗
              </h3>
              <button @click='isShow=false'>
                  关闭弹窗
              </button>
          </div>
      </div>
  </teleport>
  ```

  

### 8.6.3.`Suspense`

- 等待异步组件时渲染一些后备内容，获得更好地用户体验

  - `Suspense`底层是用插槽实现的
    - `v-slot:defalut`
      - 用于放置本应该展示的组件
    - `v-slot:fallback`
      - 组件未加载时，展示的内容

- 使用步骤：

  - 1.异步引入组件

    ```js
    import {defineAsyncComponent} from 'vue'
    // import Child from './components/Child.vue' // 静态引入（同步引入）
    const Child = defineAsyncComponent(() => import('./components/Child.vue')) // 动态引入（异步引入）
    ```

  - 2.使用`Suspence`包裹组件，并配置好`default`与`fallback`

    `App.vue`

    ```vue
    <template>
    	<div class='app'>
            <h3>
            	我是App组件    
        	</h3>
            <Suspence>
        		<template v-slot:default>
    				<Child/>
    			</template>
    			<template v-slot:fallback>
    				<h3>
                        加载中...
                    </h3>
    			</template>
        	</Suspence>
        </div>
    </template>
    ```

    - 同步引入情况下，会等到所有的组件引入加载完，才会展示
    - 异步引入情况下，被设置成异步引入的组件，不会阻塞整个页面的加载

  - 之前说`setup`不能返回`Promise`，那是因为没有讲到这里，其实是可以的

    `Child.vue`

    ```vue
    <template>
    	<div class="child">
    		<h3>我是Child组件</h3>
    		{{sum}}
    	</div>
    </template>
    
    <script>
    	import {ref} from 'vue'
    	export default {
    		name: 'Child',
    		setup() {
    			let sum = ref(0)
    			return new Promise((resolve, reject) => {
    				setTimeout(() => {
    					resolve(sum)
    				}, 1000)
    			})
    		}
    	}
    </script>
    ```

    或者写成`async`形式

    ```vue
    <template>
    	<div class="child">
    		<h3>我是Child组件</h3>
    		{{sum}}
    	</div>
    </template>
    
    <script>
    	import {ref} from 'vue'
    	export default {
    		name: 'Child',
    		async setup() {
    			let sum = ref(0)
    			let p = new Promise((resolve, reject) => {
    				setTimeout(() => {
    					resolve(sum)
    				}, 1000)
    			})
                return await p
    		}
    	}
    </script>
    ```

    可以配合`Suspence`使用

## 8.7.其他

### 8.7.1.全局`API`的转移

- `vue2`有许多全局`API`和配置

  - 例如：注册全局组件、注册全局指令等

    ```js
    // 注册全局组件
    Vue.component('MyButton', {
        data: () => ({
            count: 0
        }),
        template: `<button @click="count++>Clicked {{count}} times.</button>`
    })
    
    // 注册全局指令
    Vue.directive('focus', {
        inserted: el => el.focus()
    })
    ```

- `vue3`中对这些`API`做出了调整

  - 将全局的`API`，即`Vue.xxx`调整到应用实例`app`上

    | 2.x全局API（Vue）        | 3.x实例API（app）           |
    | ------------------------ | --------------------------- |
    | Vue.config.xxx           | app.config.xxx              |
    | Vue.config.productionTip | 移除                        |
    | Vue.component            | app.component               |
    | Vue.directive            | app.directive               |
    | Vue.mixin                | app.mixin                   |
    | Vue.use                  | app.use                     |
    | Vue.prototype            | app.config.globalProperties |



## 8.7.2.其他改变

- `data`选项应始终被声明为一个函数

- 过度类名的更改

  - `vue2`的写法

    ```css
    .v-enter, .v-leave-to {
        opacity: 0;
    }
    .v-leave, .v-enter-to {
        opacity: 1;
    }
    ```

  - `vue3`的写法

    ```js
    .v-enter-from, .v-leave-to {
        opacity: 0;
    }
    .v-leave-from, .v-enter-to {
        opacity: 1;
    }
    ```

- 移除`keyCode`作为`v-on`的修饰符，同时也不再支持`config.keyCodes`

- 移除`v-on.native`修饰符

  - 父组件中绑定事件

    ```vue
    <my-component 
                  v-on:close = "handleComponentEvent"
                  v-on:click = "handleNativeClickEvent"
                  />
    ```

  - 子组件中声明自定义事件

    ```vue
    <script>
    	export default {
            emits: ['close'] // 没指定的，会认为是原生事件
        }
    </script>
    ```

- 移除过滤器（`filter`）state.regisstate.registerState.passportterState.passport

  - 过滤器虽然看起来很方便，但它需要一个自定义语法，打破大括号内表达式“只是JavaScript”的假设，这不仅有学习成本，而且有实现成本
  - 建议用方法调用或计算属性去替换过滤器

- 其他



# vue3中路由

```vue
import { useRouter } from 'vue-router'
 
setup(){
    const $router = useRouter();
    function turnToLogin(){
        //对象$router.push()可以向history对象添加新纪录
        $router.push('/login');
    }
    return {
        turnToLogin
    }
}
```

# vue3中的父子组件

## 父传子

[和Vue3和解的Day11--父子组件通信 - 掘金 (juejin.cn)](https://juejin.cn/post/7198806651561623608)

子组件通过props接收父组件传递的参数，props接受参数也有两种写法: **数组**或者**对象**

### 子组件中定义`props`接收props传参

#### options api中的写法

```vue
<template>
  <div>
    <h2>{{ title }}</h2>
    <h2>{{ info }}</h2>
  </div>
</template>

<script>
  export default {
    props: ["title", "info"]
  }
</script>

```

通过隐式定义规定类型

```vue
  props: {
    title: "",
    info: {}
  }
```

通过type类型规定类型

```vue
  props: {
    title: {
      type: String,
      default: "默认值"
    },
    info: {
      type: Object,
      default: {}
    }
  }

```

props校验参数可传

```vue
      propsA: {
        validator(value) {
          return ['success', 'error'].includes(value)
        }
      },

```

当`type`为`Obejct | Array`的时候。`default`参数最好是写成工厂函数。

- 如果是对象类型，当子组件重复被使用，对象变量指向的都是同一个内存地址，当父组件更改变量的时候，其他调用的父组件也会跟着改变。
- 如果是函数类型，变量是`return`出去的，每次调用都会重新拷贝一个新的变量，调用的父组件之间不会相互影响。

```js
      propB: {
          type: Function,
          default() {
              return 'Default function'
          }
      }

```

#### setup函数中的写法

如果是**setup函数**的形式，props 必须以 `props` 选项的方式声明，props 对象会作为 `setup()` 函数的第一个参数被传入

```vue
<script>
export default {
  props: ['title', "info"],
  setup(props) {
    console.log(props);
  }
}
</script>

```

#### setup语法糖中的写法

```vue
<script setup>

const props = defineProps(["title", "info"])

console.log(props);

</script>

```



### 父组件定义数据传输props参数

```vue
<son :title="title" :info="info"></son>
        
 // data中定义
 title: "Father标题",
 info: { name: "小白" }
```

传递对象

```vue
<son :title="title" :info="info"></son>

  data() {
    return {
      title: "Father标题",
      info:{
        name: "小白"
      }
    }
  },

```







```js
<script setup>

const props = defineProps(["title", "info"])

console.log(props);

</script>

```



### 父组件传输非props参数

当我们向一个组件传递某个属性，该属性并没有定义对应的`props`或者`$emit`时，就会被称之为**非props的Attribute**，常见的包括`class`、`id`、等等。

[和Vue3和解的Day12--父子组件通信 - 掘金 (juejin.cn)](https://juejin.cn/post/7199086162991988794)

父组件在子组件调用时，定义了`class`类

```vue
<son class="box" :title="title"></son>
```

如果子组件只有一个节点，则会自动绑定

```vue
<template>
    <h2>{{ title }}</h2>
</template>

```

其最终渲染的结构如下：

![image-20230803153517721](image-20230803153517721.png)

如果子组件有多个节点的时候，父组件不能再自动绑定attribute，需要我们手动绑定

父组件

```vue
<son class="box" set="set" :title="title" :message="message"></son>
```

子组件`title`变量上绑定`attribute`，此时父组件传递的所有选择器都会绑定到`title`这个变量的节点上

```vue
<template>
    <h2 v-bind="$attrs">{{ title }}</h2>
    <h2>{{ message }}</h2>
</template>

```

当我不想要继承根节点的时候，可以使用`inheritAttrs: false`设置，可以从`$attrs`中获取所有的`attribute`

手动绑定的attribute，即使在设置了不继承之后，依旧会被绑定在指定位置，这个属性对手动绑定的不生效。

```vue
<template>
    <h2>{{ title }}</h2>
</template>

<script>
export default {
  inheritAttrs: false,
  props: ['title', "message"],
}
</script>

```

## 子传父

首先明确一点，子组件不能直接给父组件传参，需要我们在子组件上绑定一个方法，在**选项式中通过`$emit`方法给父组件传递一个方法，在父组件中通过调用这个方法实现参数传递**

### options api中的写法

子组件

```vue
<template>
    <h2>{{ counter }}</h2>
    <button @click="addCounter">+1</button>
</template>

<script>
export default {
  props: ["counter"],
  methods: {
    addCounter() {
      this.$emit("increment")
    }
  }
}
</script>

```

父组件

```vue
<template>
  <div>
    <son :counter="counter" @increment="increment"></son>
  </div>
</template>

<script>
import Son from './Son.vue';
export default {
  data() {
    return {
      counter: 10
    }
  },
  components: { Son },
  methods: {
    increment() {
      this.counter++
    }
  }
}
</script>

```

上例是最基本的子组件中的方法，在父组件引用子组件之后可以触发方法。子组件中的交互，需要修改数据，但数据来自父组件，怎么处理？

- 一种是如上，通过$emit在子组件身上提交一个方法，然后父组件中触发这个方法并调用该方法的回调，该回调中修改了父组件中的数据（同时该数据也被传递给了子组件，即可实现子组件变更props数据）
- 第二种是通过定义`data`额外接受一次`props`，子组件基于`data`渲染



子组件向父组件传递方法时，那么如何传递我们想要传递的参数呢？

子组件

```vue

<template>
  <button @click="transmit">传递参数的类型</button>
</template>

<script>
export default {
  methods: {
    transmit() {
      this.$emit("transmit", 10)
      this.$emit("transmit", "字符串")
      this.$emit("transmit", [1, 2])
      this.$emit("transmit", { name: "小白" })
    }
  }
}
</script>

```

父组件

```vue
<template>
  <div>
    <son @transmit="transmit"></son>
  </div>
</template>

<script>
import Son from './Son.vue';
export default {
  components: { Son },
  methods: {
    transmit(params) {
      console.log(params);
    }
  }
}
</script>

```

通过$emit传递的四个方法，都成功将参数传递过去了，并且四个参数类型都不相同。

后面的传参并不会覆盖前面传递的参数，但是并不建议这样做

![image-20230803154738838](image-20230803154738838.png)

### setup函数中的写法

 `setup`接收的第一个参数是 `props` **setup 接收的第二个参数就是context, context是一个对象，里面包含了emit**, 我们就是利用这个参数进行子组件向父组件传参

子组件

```vue
<template>
  <h2>{{ counter }}</h2>
  <button @click="addCouter">+1</button>
</template>

<script>
export default {

  props: ["counter"],
  emits: ['addCouter'],
  setup(props, context) {
    const addCouter = () => {
      context.emit('addCouter')
    }

    return {
      addCouter
    }
  }
}
</script>

```

父组件

```vue
<template>
  <div>
    <son :counter="counter" @addCouter="addCouter"></son>
  </div>
</template>

<script>
import { ref } from 'vue';
import Son from './Son.vue';
export default {
  components: { Son },
  setup() {
    const counter = ref(10)
    const addCouter = () => {
      counter.value++
    }

    return {
      counter,
      addCouter
    }
  }
}
</script>

```

这里要注意的一点就是在vue3的组合式中需要我们额外将需要传递的方法定义在emits数组中。上面也说过context是一个对象，我们也可以采用解构的写法来写emit传参

在方法中传递方法和参数的时候，直接emit()即可。

```vue
<script>
export default {
  props: ["counter"],
  emits: ['addCouter'],
  setup(props, { emit }) {
    const addCouter = () => {
      emit('addCouter')
    }

    return {
      addCouter
    }
  }
}
</script>

```

传参方式和上述一致

### setup语法糖中的写法

在父组件中引用调用子组件的方法和变量和之前是没有变化的，但是子组件会有引入新的官方提供的新方法

子组件

```vue
<template>
  <h2>{{ counter }}</h2>
  <button @click="addCouterClick">+1</button>
</template>

<script setup>

// const props = defineProps(["counter"])
const props = defineProps({
  counter: Number
})

const emits = defineEmits(["addCounter"])

const addCouterClick = () => {
  emits("addCounter")
}

</script>

```

## 祖孙组件通信

[和Vue3和解的Day15--非父子组件通信 - 掘金 (juejin.cn)](https://juejin.cn/post/7200366809424396346)

为什么需要非父子组件传参，我们可以想象一下，我们有5个组件是逐级引用的，那么我们需要props沿着组件引用定义传参，那么此刻的场面会相当混乱，也不利于我们后期维护代码。

官方提供了`provide`和`inject`来帮助我们**解决多层props嵌套**的问题。一个父组件相对于其所有的后代组件，会作为**依赖提供者**。任何后代的组件树，无论层级有多深，都可以**注入**由父组件提供给整条链路的依赖。

比如下面这张图，我们想要给DeepChild传递参数就可以使用`provide`和`inject`这两个方法

![image-20230803160613774](image-20230803160613774.png)

### 基本使用

先说一个组件的引用结构：App.vue -> Home.vue -> HomeContent.vue

**组合式中的provide需要引入才能使用**

> `provide(/* 注入名 */ 'message', /* 值 */ 'hello!')`

`App.vue`

```vue
<template>
  <div>
    <home></home>
</div>
</template>

<script setup>
import Home from './Home.vue';
import { ref, provide } from 'vue';

const name = ref("小白")
provide("name", name)
</script>

```

`HomeContent.vue`

```vue
<template>
  <div>
    <h2>{{ name }}</h2>
</div>
</template>

<script setup>

import { inject } from 'vue';
const name = inject("name")


</script>

```

此时我们数据会正常显示，以下说一些补充知识点。

**注入默认值**

```vue
const name = inject("name" , "默认值")
```

 **提供方改变数据**

`App.vue`

```vue
<template>
  <div>
    <home></home>
    <button @click="changeClick">点击切换</button>
</div>
</template>

<script setup>
import Home from './Home.vue';
import { ref, provide } from 'vue';

const name = ref("小白")
provide("name", name)

const changeClick = () => name.value = "小刚"

</script>

```

**provide传递一个对象**

`App.vue`

```js
const name = ref("小白")
const age = ref(18)
provide("user", {
  name,
  age
})

```

`HomeContent.vue`

```vue
    <h2>{{ user.name }}</h2>
    <h2>{{ user.age }}</h2>

<script setup>

import { inject } from 'vue';
const user = inject("user")


```

也可以解构后使用

```js
const {name, age} = inject('user')
```

### 底层原理

[和Vue3和解的Day18--非父子组件通信 - 掘金 (juejin.cn)](https://juejin.cn/post/7201314551576264765)

`provide` 和 `inject` 的实现原理其实是利用了 Vue3 中新的响应式系统和依赖注入机制。

首先，当一个组件使用 `provide` 来提供数据时，Vue3 会将这些数据包装成一个 reactive 对象，同时将它们添加到当前组件的 provide 实例属性中。这样，子孙组件就可以通过 `inject` 来访问这些数据了。

具体来说，当一个组件使用 `provide` 来提供数据时，Vue3 会将这些数据存储在组件实例的 `_provided` 属性中，同时将 `_provided` 属性添加到当前组件的依赖项（deps）中。这样，当数据发生变化时，所有依赖它的子孙组件都会被通知更新。

另外，当一个组件使用 `inject` 来注入数据时，Vue3 会在组件实例的 `setup` 钩子中创建一个 `inject` 函数，该函数会在当前组件的依赖项中添加 `_provided` 属性，并返回其对应的值。这样，子孙组件就可以在模板或组件逻辑中通过 `this.xxx` 访问这些数据了。

需要注意的是，由于 `provide` 和 `inject` 是基于 Vue3 的响应式系统和依赖注入机制实现的，因此它们仅在 Vue3 中有效，而在 Vue2 或其它框架中并不适用。



