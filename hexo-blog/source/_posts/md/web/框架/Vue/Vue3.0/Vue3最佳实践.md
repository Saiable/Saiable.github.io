---
title: 'Vue3最佳实践'
date: 2022-8-8 07:15:24
cover: false
toc_number:false
categories: Vue
typora-root-url: Vue3最佳实践
---

> 未提及项，和vue2中最佳实践保持一致
>
> 本篇也可当作：vue2项目改写成vue3注意事项

# 使用`vite`

[开始 | Vite 官方中文文档 (vitejs.dev)](https://cn.vitejs.dev/guide/)

见`vite`相关文档

# `setup`语法糖

[Vue3.2 setup语法糖、Composition API、状态库Pinia归纳总结 - 掘金 (juejin.cn)](https://juejin.cn/post/7006108454028836895#heading-13)

## 一、文件结构

Vue2中，`<template>` 标签中只能有一个根元素，在Vue3中没有此限制

```vue
<template>
  // ...
</template>

<script setup>
  // ...
</script>

<style lang="scss" scoped>
  // 支持CSS变量注入v-bind(color)
</style>
```

## 二、data

> 自动导入见vite篇

使用toRefs解构，template可直接使用

```vue
<script setup>
  import { reactive, ref, toRefs } from 'vue'

  // ref声明响应式数据，用于声明基本数据类型
  const name = ref('Jerry')
  // 修改
  name.value = 'Tom'

  // reactive声明响应式数据，用于声明引用数据类型
  const state = reactive({
    name: 'Jerry',
    sex: '男'
  })
  // 修改
  state.name = 'Tom'
  
  // 使用toRefs解构
  const {name, sex} = toRefs(state)
  // template可直接使用{{name}}、{{sex}}
</script>
```

## 三、method

```vue
<template>
  // 调用方法
  <button @click='changeName'>按钮</button>  
？》</template>

<script setup>
  import { reactive } from 'vue'

  const state = reactive({
    name: 'Jery'
  })

  // 声明method方法
  const changeName = () => {
    state.name = 'Tom'
  }  
</script>
```

## 四、computed

```vue
<script setup>
  import { computed, ref } from 'vue'

  const count = ref(1)

  // 通过computed获得doubleCount
  const doubleCount = computed(() => {
    return count.value * 2
  })
  // 获取
  console.log(doubleCount.value)
</script>
```

## 五、watch

```vue
<script setup>
  import { watch, reactive } from 'vue'

  const state = reactive({
    count: 1
  })

  // 声明方法
  const changeCount = () => {
    state.count = state.count * 2
  }

  // 监听count
  watch(
    () => state.count,
    (newVal, oldVal) => {
      console.log(state.count)
      console.log(`watch监听变化前的数据：${oldVal}`)
      console.log(`watch监听变化后的数据：${newVal}`)
    },
    {
      immediate: true, // 立即执行
      deep: true // 深度监听
    }
  )
</script>
```

## 二十一、定义组件的name

> 见vite篇

用单独的`<script>`块来定义

```vue
<script>
  export default {
    name: 'ComponentName',
  }
</script>
```

更优雅的方式，安装插件：`vite-plugin-vue-setup-extend`，就可以按以下方式定义name了

配置 `vite.config.ts`

```ts
import { defineConfig } from 'vite'
import VueSetupExtend from 'vite-plugin-vue-setup-extend'
export default defineConfig({
  plugins: [VueSetupExtend()]
})
```

使用

```vue
<script setup name="ComponentName">
  // todo
</script>
```

`vue-cli`中使用

```bash
npm i unplugin-vue-setup-extend --save-dev
```

`vue-cli`

```js
// vue.config.js
module.exports = {
  configureWebpack: {
    plugins: [
      require("unplugin-vue-setup-extend/webpack")({
        /* options */
      }),
    ],
  },
};
```

# `axios`最佳实践

## 抽离baseUrl

直接以文件的角度导入即可

`request.js`

```js
import serverConfig from "@/../public/serverConfig.js";
```

# vue3在原型上挂载(封装的方法）

## 方式一 app.config.globalProperties

在`main.js`中引入全局要使用的方法，通过`app.config.globalProperties`添加到全局中。

例一：

```js
// main.js
import { createApp } from 'vue'
import App from './App.vue'

// test 是外部引入的方法
const test = () => {
    console.log('ccccc')
    return '测试成功001'
}

const app = createApp(App)
// 添加到全局中
app.config.globalProperties.$Test = test
app.use(test)
app.use(store)
app.use(router)
app.mount('#app')

```

例二：

```ts
import session from './utlis/session'
const app = createApp(App)
/* 挂载原型 */
app.config.globalProperties.$session = session
```

根据官方文档描述
`app.config`是一个包含了 Vue 应用全局配置的对象。你可以在**应用挂载前**修改其属性，方法。
`main.js`

```
// 之前(Vue 2.x)
Vue.prototype.$http = () => { }

// 之后(Vue 3.x)
const app = Vue.createApp({ })
app.config.globalProperties.$http = () => { }
app.use(store).use(router).mount('#app');

```

在要使用的.vue文件中，

通过 getCurrentInstance 的 proxy 使用，不过 proxy 的 ts 类性中还有一个 undefined，所以使用 ts 时，类型就要自己处理了

通过 getCurrentInstance 的 appContext 使用，appContext 获取的即为 main.js 里创建的的 vue 对象.

ts写法

```js
// Home.vue
// ts写法中会使用 defineComponent，普通的写法不用在意
import { defineComponent, getCurrentInstance } from 'vue'

export default defineComponent({
    name: 'Home',
    setup() {
        // ts proxy 使用
        const { proxy }: any = getCurrentInstance()
        // js
        /* const { proxy } = getCurrentInstance() */
        console.log(proxy, proxy.$Test())
        // ts appContext 使用
        const { $Test } = getCurrentInstance().appContext.config.globalProperties
        $Test()
        /* 
        但是这种写法不行，打包之后不能正常使用
        const { ctx } = getCurrentInstance()
        ctx.$test
        */
    }
})

```

js写法

```js

import {getCurrentInstance} from 'vue'
const {proxy}=getCurrentInstance()
//get获取
//current当前应用
//instancel实例
//在组合Api内使用getCurrentInstance()返回一个对象
console.log(getCurrentInstance())//相当于vue2的this
proxy.$axios()//就可以找到我们刚才挂载的方法了
proxy.BASEURL//就可以找到我们刚才挂载的属性了

//以上就是vue3原型上挂载公共属性及方法的配置

```



## 方式二 依赖和注入（provide 和 inject）

src 文件夹下新建 symbol 文件夹并新增index.ts (或 .js) 文件

```js
// src/symbol/index.ts
// 定义对应的 symbol 并暴露出去
export const TEST_SYMBOL = Symbol('Test 测试')

```

在 `main.js` 中引入，并使用 `project` 绑定依赖

```js
// main.ts
import { createApp } from 'vue'
import App from './App.vue'
import { TEST_SYMBOL } from './symbol'
// test 是外部引入的方法
const test = () => {
    console.log('ccccc')
    return '测试成功001'
}
const app = createApp(App)
// 使用 symbol 方式
app.provide(TEST_SYMBOL, test)
// 使用自定义字符串方式
app.provide('$Test', test)
app.use(store)
app.use(router)
app.mount('#app')

```

在对应.vue文件中引入并使用

```js
import { defineComponent, inject } from 'vue'

import { TEST_SYMBOL } from '@/symbol'

export default defineComponent({
    setup() {
        // ts 中它的类型可能是个undefined
        // symbol 方式
        const $Test: (() => string) | undefined = inject(TEST_SYMBOL)
        $Test && $Test()
        // 自定义字符串方式
        const $Test2: (() => string) | undefined = inject('$Test')
        $Test2 && $Test2()
        // js
        /*
        const $Test = inject(TEST_SYMBOL)
        $Test()
        */
    }
})

```

Vue3 不推荐 方式一 在原型链上挂载一些东西这种方式，而是更建议使用 方式二 的 `provide` 和 `inject` 方式

# 格式化样式

[necolas/normalize.css: A modern alternative to CSS resets (github.com)](https://github.com/necolas/normalize.css)

```bash
npm install --save normalize.css
```

normalize.css 修复了 CSS reset 范围之外的常见桌面和移动浏览器错误。包括 HTML5 元素的显示设置、更正 font-size 预格式文本、IE9 中的 SVG 溢出以及跨浏览器和操作系统的许多与表单相关的错误。

您必须在加载任何其他CSS文件之前加载 Normalize.css文件。

`main.js`

```js
import 'normalize.css'
```

# rem适配



# vue3中给数组赋值丢失响应式的解决

由于vue3使用proxy，对于对象和数组都不能直接整个赋值。

只有push或者根据索引遍历赋值才可以保留reactive数组的响应性

```js
const arr = reactive([]);
 
const load = () => {
  const res = [2, 3, 4, 5]; //假设请求接口返回的数据
  // 方法1 失败，直接赋值丢失了响应性
  // arr = res;
    
  // 方法2 这样也是失败
  // arr.concat(res);
    
  // 方法3 可以，但是很麻烦
  res.forEach(e => {
    arr.push(e);
  });
    
  // 方法4 可以
  // arr.length = 0 // 清空原数组
  arr.push(...res)
}

```

或者

```js
const state = reactive({
	arr: []
});
...
state.arr = res
...

```

或者

这样也不会丢失响应式

原因：reactive声明的响应式对象被state代理  操作代理对象需要有代理对象的前缀，直接覆盖会丢失响应式 

```js
const state = ref([]);
...
state.value= res
...

```

# 组件动态渲染

https://blog.csdn.net/cjp1223/article/details/129621053

动态渲染如下菜单栏

![image-20230526102934110](image-20230526102934110.png)

`vue2`

```vue
data(){
	return{
	//所有的键均为 menu一级菜单所对应的id
	 iconsObj: {
        125: "el-icon-user-solid",
        103: "el-icon-turn-off",
        101: "el-icon-s-goods",
        102: "el-icon-tickets",
        145: "el-icon-monitor",
      },
	}
}
```

```vue
 <i :class="iconsObj[i.id]"></i>
```

`vue3`（该方法不行）

```vue
<style setup>
	//键也均为menu一级菜单的id
	//写法1
	let iconsObj = {
	  125: <User/>,
	  103: <Operation/>,
	  101: <GoodsFilled/>,
	  102: <Tickets/>,
	  145: <Histogram/>,
	};
	//写法2
	let iconsObj = {
	  125: 'User',
	  103: 'Operation',
	  101: 'GoodsFilled',
	  102: 'Tickets',
	  145: 'Histogram',
	};
</style>

```



```vue
<el-icon>
     <component :is='iconsObj[i.id]'/>
</el-icon>

```

## 动态渲染Vue组件的问题

跨过了Element-UI，终于来到了Element-plus。又回到了一个老问题，menu的渲染。
创建一个menu数组，利用`v-for`来渲染数组，生成menu，非常常规的操作。但是操作的过程中，出现了一个小问题，就是关于`icon`的渲染。
我们知道，在Element-plus中，渲染一个带图标的菜单项，是这么搞的：

```vue
<el-menu-item index="/mypath">
    <template #title>
        <el-icon><Odometer /></el-icon>
        <span>title</span>
    </template>
</el-menu-item>
```

`icon`图标是直接以一个组件的形式进行渲染的。
那么，当我们企图利用`v-for`进行列表渲染的时候，这个图标的组件怎么渲染出来，成了个难题。
直接用双花括号{{}}肯定是不行的，直接会把标签搞成文本。
用`v-html`也不行，它只能渲染原生的HTML标签。
WTF？

### 如何才能动态的把自定义组件渲染出来？

在`<template></template>`里面搞模版语法是行不通了。
那就只能尝试走其他的路线了。在搜索引擎愉快的与海量信息搏斗之后，找到了切入点：`render`函数。
老实说，其实早就该想到这个了，毕竟组件渲染就这么两条路嘛。奈何对`render`的使用频率太低了，选择性的搞忘记了。
那么来尝试吧。
写一个组件，通过`props`接收到图标的标签写法，然后渲染出来。

```js
//注意在vue3中，render函数中不再有参数了，h函数需要按需加载。
import { h } from 'vue';

export default{
    props: {
        //Odometer
        html: String
    },
    render(){
        return h('el-icon', null, h(this.html));
    }
}
```

果不其然没有达到效果。常用vue做开发的小伙伴肯定一眼就发现了一个问题：
用`h`函数生成虚拟DOM节点时，如果要生成的是组件，则第一个参数直接使用导入的组件即可。如果使用字符串，会原封不动的把字符串当做HTML标签渲染，而不是当作组件渲染。[(参考链接)](https://link.segmentfault.com/?enc=zA0ofOKzRkLvIT9Ku%2BzLrA%3D%3D.RNhFyTIRPWiQSo3koW%2BJTp0bpAQ6mQX%2BHgUwBIhRRdSsuZsMGsyj4Bg336P4y7orVxCAnTVa2U%2FTmN2qNJBnQNrKo40phQjCf0Nxc%2F2J1kw%3D)

修改一下：

```js
import { h } from 'vue';
import { ElIcon } from 'element-plus';

export default{
    props: {
        //Odometer
        html: String
    },
    components: {
        ElIcon
    },
    render(){
        return h(ElIcon, null, h(this.html));
    }
}
```

还是不对呀，图标名称是传过来的字符串，没法直接获取到导入的组件呀。
吓得我赶紧又翻了一下文档，在最后一行找到了这么一句话：

> 如果一个组件是用名字注册的，不能直接导入 (例如，由一个库全局注册)，可以使用 resolveComponent() 来解决这个问题。

原来如此。。。
好了，给出最终答案：

```vue
<el-menu-item :index="item.path">
    <template #title>
        <DynamicIcon :html="item.icon"></DynamicIcon>
        <span>{{item.title}}</span>
    </template>
</el-menu-item>
```

```js
//DynamicIcon
import { h, resolveComponent } from 'vue';
import { Odometer, ChatDotRound } from '@element-plus/icons-vue';

export default{
    props: {
        //Odometer
        html: String
    },
    components: {
        Odometer,
        ChatDotRound
    },
    render(){
        //ElIcon直接全局全局导入了
        const IconBox = resolveComponent('ElIcon');
        const Icon = resolveComponent(this.html);

        return h(IconBox, null, h(Icon));
    }
}
```

### 总结

最后总结一下子吧。
想要动态渲染组件，就需要利用`props`与`render`函数。
在使用`h`函数的时候，生成组件的虚拟vnode，要直接使用导入的组件。
如果只能获取一个组件名称，那么就用`resolveComponent`函数手动解析注册的组件。

# 组件库

## 使用elementPlus的图标，图标不显示

[Vue3如何使用elementPlus的图标，图标不显示](https://blog.csdn.net/weixin_45804632/article/details/129942206?spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-5-129942206-blog-123783679.235^v36^pc_relevant_default_base3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-5-129942206-blog-123783679.235^v36^pc_relevant_default_base3&utm_relevant_index=10)

下载图标库

```bash
npm install @element-plus/icons-vue
```

配置main.js

```js
//引入图标
//首先需要我们在终端下载图标库，再导入图标，再去需要引入图标的页面，如Login---->
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

```

导入和初始化

```js
//图标
import {User,Search,Position,Edit,Check} from "@element-plus/icons";
import request from "@/utils/request";
ex//图标
import {User,Search,Position,Edit,Check,Message,RefreshLeft,TurnOff,Open,Star,Delete,CirclePlusFilled,ArrowDown,RemoveFilled,FolderAdd,FolderRemove}
  from "@element-plus/icons";
import request from "@/utils/request";port default {
  setup() {
    return {
      User,
      Search,
      Position,
      Edit,
      Check,
    }
  },

```

# Pinia

[小菠萝Pinia快速入门学习 - 掘金 (juejin.cn)](https://juejin.cn/post/7231118884861689911)

[Pinia快速入门 - 掘金 (juejin.cn)](https://juejin.cn/post/7199832444836970557)

[Getting Started | Pinia (vuejs.org)](https://pinia.vuejs.org/getting-started.html)

> 直接看完前两个使用案例，实操下后，再过下官网即可

页面中可通过`store.属性名`直接使用

也可以通过在js中定义属性解构返给页面使用，但想实现`响应式`必须依赖于`storeToRefs`

可通过`$patch`批量修改state的属性，也可以指定修改哪个属性

可通过`store.$state`将整个state进行替换

通过`store.$reset()`可实现重置

通过`store.$subscribe(()=>{})`可实现监听改变

## 安装

```bash
npm install pinia
```

## 挂载

首先需要在main.js中引入pinia，然后通过导入**createPinia**方法创建pinia实例

```js
import { createPinia } from 'pinia'
import { createApp } from 'vue'
import App from './App.vue'
createApp(App).use(createPinia()).mount('#app')

```

## 定义Store

`defineStore`定义容器

参数1：是对仓库的命名，名称必须具备唯一性；

参数2：配置的选项对象，即state、getters、actions，其中state的写法必须是函数，为了避免在服务端交叉请求导致的状态数据污染，而且必须是箭头函数，为了更好的TS类型推导。

- 首先在src目录下面创建`stores`文件夹
- 然后在stores文件夹中创建`count.js`, 文件名称可以随便写。
- 然后在`stores/count.js`文件中用过**defineStore**进行定义Store

`options`x写法

```js
import { defineStore } from 'pinia'

export const useCountStore = defineStore('main', {
  state: () => ({
    count: 0,
  }),
  getters: {
    doubleCount: (state) => {
      return state.count*2
    }
  },
  actions: {
    increment() {
      this.count++
    }
  }
})

```

`composition`写法

```js
import { ref, computed } from 'vue';
import { defineStore } from 'pinia'

// Setup写法,第一个参数为id
export const useCountStore = defineStore('main', () => {
  // State
  const count  = ref(0);
  // getter
  const doubleCount = computed(() => count.value*2)
  // actions
  const increment = function(){
    count.value++
  }

  return {
    count,
    doubleCount,
    increment
  }
})

```

## 使用

```js
import { storeToRefs } from 'pinia';
import { useCountStore } from './stores/count';

export default {
  name: 'App',
  components: {},
  setup() {
    const store = useCountStore();
    const { increment } = store;
    const { count, doubleCount } = storeToRefs(store);

    return {
      count,
      doubleCount,
      increment,
    };
  },
};

```

从/stores/count.js中导入定义的useCountStore

从store中解构出increment方法

如果**直接从store中解构state会失去响应性**，也就是改了state页面上显示的state不会改变。所以需要使用**storeToRefs**方法将store中的state转为ref再进行解构，这样修改数据页面上也就会跟着变了。注意，如果使用了自动导入，可能会出错，需要手动导入`storeToRefs`方法

如果有一个`reactive`对象属性，直接使用`store.state`调用即可

## 修改`state`

**patch 函数修改state**

当需要修改state中多个数据时用$patch ，$patch函数会批量更新，此时需要传入state参数。

```js
mainStore.$patch(state=>{      
          state.count++
          state.name += '~~'
          state.arr.push(5)
})
```

**Action通过函数更改state**

在store/index.js中添加changeState方法，在组件中用store调用。

注：定义actions时不要使用箭头函数，因为箭头函数绑定外部this。使用容器中的state 时，action通过this操作；此外，还可以通过$patch修改state的数据。

```js
actions:{  
  changeState(num,str){
      this.count += num     //action通过this操作state的数据
      this.name += str
      this.arr.push(5)
      this.$patch({})
      this.$patch(state=>{})
  }
}
```

**Getters类似Vuex的计算属性**

在store/index.js的Getters函数中添加count10()方法，在组件中用store调用，getters函数接收state参数。

注：若组件中使用ts，getters使用this时，必须指定类型，否则会导致推导错误。

```js
getters:{
      count10(state){
       return state.count + 10
       }
      countOther():number{
          return this.count += 12
      }
},
```













# VueUse

VueUse is a collection of utility functions based on Composition API. 

官网：[Get Started | VueUse](https://vueuse.org/guide/)

Vueuse是一个基于Vue3的轻量级的函数式工具库，它提供了许多实用的函数和组合函数，可以帮助我们更加高效地开发Vue应用程序。

Vueuse的使用非常简单，只需要在Vue项目中安装并导入即可。

Vueuse提供了许多实用的函数，例如useMouse、useClipboard、useLocalStorage等等。这些函数可以帮助我们更加方便地处理一些常见的操作，例如获取鼠标位置、复制粘贴文本、本地存储等等。这些函数都是基于Vue3的响应式系统实现的，因此可以非常方便地与Vue组件进行集成。

除了单个函数之外，Vueuse还提供了许多组合函数，例如useFetch、useDebounce、useThrottle等等。这些组合函数可以将多个实用函数组合在一起，以实现更加复杂的功能。例如，我们可以使用useFetch函数获取远程数据，并使用useDebounce函数对用户输入进行防抖处理，以避免频繁的网络请求。

Vueuse还提供了一些与UI框架集成的函数，例如useElementUi、useAntd等等。这些函数可以帮助我们更加方便地使用这些UI框架，例如自动注册组件、自动导入样式等等。这些函数可以大大简化我们的开发流程，提高开发效率。

Vueuse是一个非常实用的工具库，可以帮助我们更加高效地开发Vue应用程序。它提供了许多实用的函数和组合函数，可以大大简化我们的开发流程。如果你正在开发Vue应用程序，不妨尝试一下Vueuse，相信它会给你带来很多帮助

```bash
npm i @vueuse/core
```

## `useLocalStorage`

> [监听localStorage - 掘金 (juejin.cn)](https://juejin.cn/post/7056045130498703374)

localStorage响应式

```vue
<script setup>
import {useLocalStorage} from '@vueuse/core'

const ref1 = useLocalStorage('test',{a:1});

ref1.value = {a:2}
watch(ref1,(val)=>{
  console.log(val);
})
</script>

```

页面上，删除localstorage的值，值会从2初始化为1，并且同时触发

1. 浏览器的`window`对象提供了`storage`的事件可以监听，`storage`的改变
2. `VueUse`的`useLocalStorage`就是靠`storage`事件,来监听`面板操作`，来`达到`保持响应式的。

# 文档生成



[vue组件库自动生成文档-生成方式对比（1） - MFYNGUFD - 博客园 (cnblogs.com)](https://www.cnblogs.com/mfyngu/p/13049965.html)



# 钩子

[浅谈：为啥vue和react都选择了Hooks🏂？ - 掘金 (juejin.cn)](https://juejin.cn/post/7066951709678895141)

> 系统运行到某一时期时，会调用被注册到该时机的回调函数。

项目、模块、页面、功能，如何高效而清晰地组织代码，这一个看似简单的命题就算写几本书也无法完全说清楚。



