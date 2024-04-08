---
title: 'Vue2最佳实践'
date: 2022-8-8 07:15:24
cover: false
tags:
- Vue
categories: Vue
typora-root-url: Vue2最佳实践
---

> 本文主要是Vue2的最佳实践，Vue3特有的在单独的文章中列出

# 环境相关

## `node`环境搭建

### 单独安装`nodejs`

#### `linux`环境

下载压缩包，若是`tar.xz`，以`tar -xf filename.tar.xz`命令解压

配置环境变量：

```bash
vim /etc/profile

在最下面Ins添加两行(注意安装路径)
export NODEJS=/opt/node/node-v10.15.3-linux-x64
export PATH=$NODEJS/bin:$PATH
```

#### `windows`环境

- `win8`及以上
  - 直接去官网上下载安装：https://nodejs.org/en/
- `win7`
  - 有的`nodejs`版本不支持`win7`，在`win7`系统中执行`npm -v`时会有以下提示`This application is only supported on Windows 8.1, Windows Server 2012 R2, or higher.`
    下载`v12.16.2`及之前的版本即可：https://nodejs.org/dist/v12.16.2/
  - 建议升级系统

### `nvm`管理`node`

`NVM`是一个非常方便的`node`包管理工具，可以实现在`NodeJS` 各个不同版本之间自由的进行切换。

下面，介绍用`root`权限安装`NVM`工具。到2022年6月，`nvm`的最新版本为`v0.39`。

`vite`依赖的`node`版本 `>=` `12.0.0`

`nuxt3`依赖的`node`版本`>=` `14.16.0`

#### 安装`nvm`

下载，可以打开链接查看

```bash
wget https://github.com/nvm-sh/nvm/archive/refs/tags/v0.39.1.tar.gz
```

解压

```bash
mkdir -p /root/.nvm
tar -zxvf v0.39.1.tar.gz -C /root/.nvm
```

配置环境，打开`~/.bashrc`

```bash
vim ~/.bashrc
```

在末尾添加

```bash
# nvm path env
export NVM_DIR="$HOME/.nvm/nvm-0.39.1"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

```

保存退出并使配置生效

```bash
source ~/.bashrc
```

#### 使用`nvm`管理`node`

 列出已经安装的版本

```bash
nvm ls
```

安装指定版本`nodejs`，可以去官网看一下最新的[Node.js (nodejs.org)](https://nodejs.org/en/)

```bash
nvm install 16.14.0
```

卸载指定版本`nodejs`

```bash
nvm uninstall 16.14.0
```

切换到其他版本`nodejs`

```bash
nvm use 14.17.3
```

切换到`iojs`

```bash
nvm use iojs-v3.2.0
```

### ubuntu环境安装nvm

[ubuntu安装nvm管理node (baidu.com)](https://baijiahao.baidu.com/s?id=1742284884399786791&wfr=spider&for=pc)

[(11条消息) Ubuntu 安装 nvm_hey laosha的博客-CSDN博客](https://blog.csdn.net/geol200709/article/details/82117103)

[(11条消息) ubuntu系统添加环境变量3种方法_ubuntu添加环境变量_prz0590的博客-CSDN博客](https://blog.csdn.net/qq_34125713/article/details/128643525)

[ubuntu－设置系统环境变量 - 简书 (jianshu.com)](https://www.jianshu.com/p/12fbfa8c7489)

最后改`~/.bashrc`，使用前需要到目录下手动`. nvm.sh`运行下（已经配了环境变量，估计是杀掉了），只能在一个shell

如果nvm ls报权限问题，参看：[使用NVM安装节点v4.1 - 权限被拒绝 - VoidCC](http://cn.voidcc.com/question/p-vqtdysom-bnt.html)

或者关掉shell重新开一个即可



## `Vue/cli`脚手架

### 创建新项目

使用`nvm`装完`node`环境后，单独新建`project`文件夹安装`@vue/cli`包，然后在这文件夹下，使用`npx vue create project-name`进行每个项目的开发

- 接口文档和`UI`设计稿
- 前端项目搭建
  - `nodejs`
  - 创建新目录并进入，习惯性的`npm init -y`一下，创建一个空的`package.json`
    - 安装`vue-cli`：`npm i @vue/cli`
    - `20220511`默认安装的脚手架版本为`5.0.4`
    - 这个默认是安装在本地的，调用指令时需要使用`npx`前缀，如果是全局安装的则不需要
  - 创建`vue`项目：`npx vue create project-name`或`vue create project-name`
    - 然后选择是`vue2`还是`vue3`的项目

### 新项目技术选型

> 每个的写法（语法、配置）都不太一样

- vue2+vueRouter+vueX+elementUI/vantUI
- vue3+vueRouter+vueX+elementPlus/vantUI
- vue3+Ts+vueRouter+Pinia+elementPlus/vantUI

### 接手老项目

接手其他项目时，如果自己的`npm`版本，和创建`package-lock.json`的版本不一致，`npm i `可能会有问题。

最好是先安装`npx`，在了解接手的项目的node版本（node和npm绑定）是多少后，切换到一致的node版本，或者再尝试安装。

当然也存在node版本一致，但npm版本不一致的情况，可以新建`node`分支，在新建`node`分支上升级或降级`npm`版本，所以两者都要先了解清楚。

## 配置



### 配置代理

#### 问题描述

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

    填写该配置项后，`vue-cli`会生成一个8080的服务器（和浏览器当前页面的端口一直），并且开发的`public`目录，对应着该服务器的资源目录，`ajax`的请求路径，要修改成代理服务的

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

#### 实际应用

前端的页面是：`http://218.94.82.249:8091/#/analysisfiles`

后台接口是：`http://218.94.82.249:8093/file_handing/upload`

直接请求会报错跨域：

```js
      this.$axios
          .post("http://218.94.82.249:8093/file_handing/upload", formData, {
            "Content-type": "multipart/form-data",
          }).then()
```

`vue.config.js`配置`proxy`

```js
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    host: '0.0.0.0',
    port: 8091,
    proxy: 'http://218.94.82.249:8093'
  }
})

```

然后将请求的接口改成`8091`（也可以直接只加路径）

```js
      this.$axios
          .post("http://218.94.82.249:8091/file_handing/upload", formData, {
            "Content-type": "multipart/form-data",
          }).then()
```

如果是设置了隧道，前后端环境需要都在目标服务器上才行

### 配置`eslint`

# 前端项目目录结构

参照：[前端项目目录结构演变 - 掘金 (juejin.cn)](https://juejin.cn/post/6930533407441027079)

## 目录结构一

### 概览

```
root
	src
		main.js
		router
			router.js
			hooks.js
			permission.js
		store
			modules
				moduleA
				moduleB
					state.js
					actions.js
					mutations.js
					getters.js
				index.js
			index.js
			action-types.js
			mutation-types.js
		utils
	
```

### `src/main.js`结构

#### `vue`相关依赖

```js
import Vue from 'vue' // 引入的是node_moudules下的vue.runtime.js，去除了模板解析功能模块的（）
import App from './App'
import store from './store'
import router from './router'
```

其他依赖

```js
// serviceworker的配置文件，pwa 离线缓存，会生成manifes + sw.js
// 生产环境做缓存用的，该文件中暴露了一些钩子，也可以自定义
import './registerServiceWorker' 
```



### `src/utils`

#### `loadable.js`

[动态组件 & 异步组件](https://cn.vuejs.org/v2/guide/components-dynamic-async.html)

```js
import LoadingComponent from '@/components/loading.vue'
const loadable = (asyncFunc) => {
    // 最终切换的时候，会采用这个组件
    let component = () => ({
      // 需要加载的组件 (应该是一个 `Promise` 对象)
      component: asyncFunc(),
      // 异步组件加载时使用的组件，只是为了增加loading效果
      loading: LoadingComponent,
      // 加载失败时使用的组件，可选
      error: ErrorComponent,
      // 展示加载时组件的延时时间。默认值是 200 (毫秒)，可选
      delay: 200,
      // 如果提供了超时时间且组件加载也超时了，
      // 则使用加载失败时使用的组件。默认值是：`Infinity`，可选
      timeout: 3000
    })
    // loadable执行完毕后，返回一个组件
    return {
        render(h) { // createElement(App)
            return h(component)
        }
    }

}

// 路由切换，异步加载的loading
export default loadable
```

使用第三库的`loading`，并封装成一个公共组件

`component/loading.vue`



异步组件加载处理

#### `_debounce.js`、`_throttles.js`

防抖节流处理

##### 什么是防抖节流

函数防抖（debounce） 是指在一定时间内，在动作被连续频繁触发的情况下，动作只会被执行一次，也就是说当调用动作过n毫秒后，才会执行该动作，若在这n毫秒内又调用此动作则将重新计算执行时间，所以短时间内的连续动作永远只会触发一次。

函数节流 是指一定时间内执行的操作只执行一次，也就是说即预先设定一个执行周期，当调用动作的时刻大于等于执行周期则执行该动作，然后进入下一个新周期，一个比较形象的例子是如果将水龙头拧紧直到水是以水滴的形式流出，那你会发现每隔一段时间，就会有一滴水流出。

函数节流（throttle）与 函数防抖（debounce）都是为了限制函数的执行频次，以优化函数触发频率过高导致的响应速度跟不上触发频率，出现延迟，假死或卡顿的现象。

**区别：**

防抖是将多次执行变成最后一次执行；而节流是将多次执行变为每隔一段时间执行一次。

那么它们各自的使用场景有哪些呢？
**防抖**

- 短信验证码
- 提交表单
- resize 事件
- input 事件（当然也可以用节流，实现实时关键字查找）

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Title</title>
</head>
<body>
<p>
  请输入搜索的内容：<input type="text">
</p>
<script>
    function _debounce(fn, delay) {
        let customDelay = delay || 200;
        let timer;
        return function () {
            let _this = this;
            let args = arguments;
            if (timer) clearTimeout(timer);
            timer = setTimeout(function () {
                timer = null;
                fn.apply(_this, args);
            }, customDelay);
        };
    }

    let myinput = document.querySelector('input')
    myinput.oninput = _debounce(function () {
        console.log('发送ajax请求')
    },1000)


</script>
</body>
</html>
```

结果：输入很多次，在结束输入后，1秒钟打印（发起`ajax`请求）

![image-20220623145039201](image-20220623145039201.png)

**节流**

- scroll 事件，单位时间后计算一次滚动位置
- input 事件（上面提到过）
- 播放事件，计算进度条

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Title</title>
</head>
<body>
<div>
  <h1>我是计数器<span>0</span></h1>
  <button>点我+1</button>
</div>
<script>
    function _throttle(fn, interval) {
        let last;
        let timer;
        let custormInterval = interval || 200;
        return function () {
            let _this = this
            let args = arguments
            let now = +new Date()
            if (last && now - last < custormInterval) {
                clearTimeout(timer)
                timer = setTimeout(function () {
                    last = now
                    fn.apply(_this, args)
                }, custormInterval)
            } else {
                last = now
                fn.apply(_this, args)
            }
        }
    }

    let span = document.querySelector('span')
    let button = document.querySelector('button')
    let count = 0
    button.onclick = _throttle(function () {
        count++
        span.innerHTML = count
        console.log('执行')
    }, 1000)

</script>
</body>
</html>
```

点的再快，也只会1秒执行一次

![image-20220623162439774](image-20220623162439774.png)

如果要自定义封装，需要了解闭包和定时器

##### vue中自定义防抖节流

###### 函数封装

写在utils文件夹下

```javascript
// 防抖
export function _debounce(fn, delay) {
    let customDelay = delay || 200
    let timer
    return function () {
        let _this = this
        let args = arguments
        if (timer) clearTimeout(timer)
        timer = setTimeout(function () {
            timer = null
            fn.apply(_this, args)
        }, customDelay)
    }
}


// 节流
export function _throttle(fn, interval) {
    let last;
    let timer;
    let custormInterval = interval || 200;
    return function () {
        let _this = this
        let args = arguments
        let now = +new Date()
        if (last && now - last < custormInterval) {
            clearTimeout(timer)
            timer = setTimeout(function () {
                last = now
                fn.apply(_this, args)
            }, custormInterval)
        } else {
            last = now
            fn.apply(_this, args)
        }
    }
}
```

###### 在需要使用的组件中引用

```vue
import { _debounce } from "..."
```

###### 使用

```vue
 methods: {
    // 改变场数
    changefield: _debounce(function(_type, index, item) {
        // do something ...
    }, 200)
  }
```

##### 防抖节流的第三方库

- `lodash`

  - 防抖：https://www.lodashjs.com/docs/lodash.debounce
  - 节流：https://www.lodashjs.com/docs/lodash.throttle

- 注意：使用的时候不用再安装了，因为`vue-cli`等一些库都依赖`lodash`，之前都装过了，可以使用`npm ls lodash`查看，在 `pnpm `中使用方法是 `pnpm why lodash`

  ```
  [root@VM-4-12-centos atguigu_gmall_frontend]# npm ls lodash
  atguigu_gmall_frontend@0.1.0 /root/hh_git/code/atguigu_gmall/atguigu_gmall_frontend
  ├─┬ @vue/cli-service@5.0.6
  │ ├─┬ html-webpack-plugin@5.5.0
  │ │ ├── lodash@4.17.21 deduped
  │ │ └─┬ pretty-error@4.0.0
  │ │   ├── lodash@4.17.21 deduped
  │ │   └─┬ renderkid@3.0.0
  │ │     └── lodash@4.17.21 deduped
  │ ├─┬ portfinder@1.0.28
  │ │ └─┬ async@2.6.4
  │ │   └── lodash@4.17.21 deduped
  │ └─┬ webpack-bundle-analyzer@4.5.0
  │   └── lodash@4.17.21 deduped
  ├─┬ eslint-plugin-vue@8.7.1
  │ └─┬ vue-eslint-parser@8.3.0
  │   └── lodash@4.17.21 deduped
  └─┬ json-server@0.17.0
    ├── lodash@4.17.21
    └─┬ lowdb@1.0.0
      └── lodash@4.17.21 deduped
  ```

- 使用

  全量导入：

  ```js
  import _ from 'lodash'
  
  // ...
    methods: {
      changeIndex: _.throttle(function (index) {
        this.currentIndex = index
      }, 50)
    }
  // ...
  ```

  按需导入：

  ```js
  import throttle from 'lodash/throttle' // 底层是module.exports默认暴露的，就不用加小括号了（咋不是require咧）
  ```

  注意点：查看`node_modules`，`throttle.js`文件用到了`debounce.js`

  里面是有保存上下文`this`的，在使用的时候不能用箭头函数

  `debounce.js`

  ```js
  // ...
  function debounced() {
      var time = now(),
          isInvoking = shouldInvoke(time);
  
      lastArgs = arguments;
      lastThis = this; // 注意throttle在使用时，不能用箭头函数，否则this指向会出问题
      lastCallTime = time;
  
      if (isInvoking) {
        if (timerId === undefined) {
          return leadingEdge(lastCallTime);
        }
        if (maxing) {
          // Handle invocations in a tight loop.
          clearTimeout(timerId);
          timerId = setTimeout(timerExpired, wait);
          return invokeFunc(lastCallTime);
        }
      }
      if (timerId === undefined) {
        timerId = setTimeout(timerExpired, wait);
      }
      return result;
    }
  // ...
  ```

### `src/styles`

`/deep`的用法

### `src/router`

#### `router.js`



#### `hooks.js`

```js
impor store from '@/store'
import * as Types from '@/store/action-types'
export default {
    'clear_token': (to, from, next) => {
        // whiteList
        store.commit(Types.CLEAR_TOKEN) // 清空取消请求的token，如果只希望某个页面切换时取消请求，单独放在组件卸载的生命周期钩子里即可
        next() // vue3中支持await的写法
    },
    'login_permission': async (to, from, next) => {
        let needLogin = to.matched.some(item => item.meta.needLogin)
        if(!store.state.user.hasPermission) {
        	let isLogin = await store.dispatch(`user/${Types.VALIDATE}`) // 登录校验
            if(needLogin) {
                if(!isLogin) {
                    next('/login') // 需要登录，但没登录
                } else {
                	next() // 需要登录，的确也登录了，正常走
                }
            } else { // 不需要登录
                if(to.name == 'login') { // 访问的是登录页
                	if(!isLogin) {
                        next() // 如果没登录，正常访问登录页
                    } else {
                        next('/profile') // 如果已经登录了，访问跳转到个人中心页
                    }
                } else {
                    next() // 不需要登录，访问的是非登录页，正常放行
                }
            }
        } else { // 如果有权限
            if (to.name = '/login') {
                next('/profile') // 访问了登录页，跳转到个人中心
            } else {
                next() // 有权限，访问的是非登录页，正常放行
            }
            
        }
    },
    // 写在路由权限下面
    'menu-permission': async (to, from, next) => {
        // 这里需要对菜单权限进行处理，动态的添加路由
        if(store.state.user.hasPermission) { // 要求用户登录才能拿取菜单的权限
            if(!store.state.user.menuPermission) { // 没有菜单权限
                await store.dispatch(`user/${Types.ADD_ROUTE}`) // 路由动态加载，此时组件是异步的
                // 我希望等待组件加载完毕后，再跳转过去
                next({...to, replace: true}) //让其再重新跳转一次（组件也ok了） hack 再跳一次的时候，菜单权限是有了的
            } else {
                next()
            }
        } else { // 用户没登录
            next()
        }
    }
}
```



#### `permission.js`

```js
export default [ // 权限管理，要和后台一一对应
    {
        path: 'lesson-manager',
        component: () => import('@/views/others/lesson-manager'),
        meta: {
            auth: 'lesson' // 存放的值要和后端约定好
        }
    },
    {
        path: 'student-manager',
        component: () => import('@/views/others/student-manager'),
        meta: {
            auth: 'student'
        }
    },
    {
        path: 'points',
        component: () => import('@/views/others/points'),
        meta: {
            auth: 'points'
        }
    },
    {
        path: 'collect',
        component: () => import('@/views/others/collect'),
        meta: {
            auth: 'collect'
        }
    }
]
```



# 资源导入

## 导入静态资源

### 导入第三方`UI`库

#### `elementUI`

- `vue2`项目
- 见《`vue2`基本使用》

#### `elementPlus`

- `vue3`项目

#### `vantUI`

- 官网：https://gitee.com/vant-contrib/vant/

- 目前 Vant 官方提供了 [Vue 2 版本](https://vant-contrib.gitee.io/vant/v2)、[Vue 3 版本](https://vant-contrib.gitee.io/vant)和[微信小程序版本](http://vant-contrib.gitee.io/vant-weapp)，并由社区团队维护 [React 版本](https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2F3lang3%2Freact-vant)和[支付宝小程序版本](https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fant-move%2FVant-Aliapp)。

- 安装

  ```bash
  # Vue 3 项目，安装最新版 Vant：
  npm i vant -S
  
  # Vue 2 项目，安装 Vant 2：
  npm i vant@latest-v2 -S
  ```

- 引入

  - 自动按需引入（推荐）

    [babel-plugin-import](https://github.com/ant-design/babel-plugin-import) 是一款 babel 插件，它会在编译过程中将 import 的写法自动转换为按需引入的方式。

    ```js
    # 安装插件
    npm i babel-plugin-import -D
    // 在.babelrc 中添加配置
    // 注意：webpack 1 无需设置 libraryDirectory
    {
      "plugins": [
        ["import", {
          "libraryName": "vant",
          "libraryDirectory": "es",
          "style": true
        }]
      ]
    }
    
    // 对于使用 babel7 的用户，可以在 babel.config.js 中配置
    module.exports = {
      plugins: [
        ['import', {
          libraryName: 'vant',
          libraryDirectory: 'es',
          style: true
        }, 'vant']
      ]
    };
    // 接着你可以在代码中直接引入 Vant 组件
    // 插件会自动将代码转化为方式二中的按需引入形式
    import { Button } from 'vant';
    
    ```

    > Tips: 如果你在使用 TypeScript，可以使用 ts-import-plugin 实现按需引入。

  - 在不使用插件的情况下，可以手动引入需要的组件。

    `main.js`

    ```js
    import Button from 'vant/lib/button';
    import 'vant/lib/button/style';
    ```

  - 导入所有组件（不推荐）

    Vant 支持一次性导入所有组件，引入所有组件会增加代码包体积，因此不推荐这种做法。

    `main.js`

    ```js
    import Vue from 'vue';
    import Vant from 'vant';
    import 'vant/lib/index.css';
    
    Vue.use(Vant);
    ```

    > Tips: 配置按需引入后，将不允许直接导入所有组件。

- 可以在`App.vue`的`#app`中覆盖`vant`的样式，也可以单独写个覆盖样式的文件在`main.js`中引入

### 导入图标库

- 阿里图标字体，选好需要的字体后，可以直接要css中`@import url()`导入，并在入口文件中引入资源；商用时要注意
- `font awesome`
- 自研图标





### 导入自定义工具库



### 第三方库的自定义封装



## 导入动态资源

### 导入`scss`变量

`src/assets/common.scss`

```scss
$color: #fff;
$background: #2a3a3a;
```

无法在`main.js`入口文件中导入动态资源，如`src/assets/common.scss`中的`scss`变量，需要使用插件动态注入

`vue.config.js`

```js
const path = require('path')

module.exports = {
    pluginOptions: {
        'style-resources-loader': {
            preProcessor: 'scss'
            pattern: [path.resolve(__dirname, 'src/assets/common.scss')]
        }
    }
}
```



# `Vuex`最佳实践

目录：`root/src/store`

## `vuex`模块化编码最佳实践

### 定义模块

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

### 使用`createNamespacedHelpers`简化`map*`写法

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

### `actions`和`mutaion`s的`types`的统一管理

上一小节我们是直接提交的`action`，如果数据太多的话，不太好管理命名



-根据需求创建`action-types.js`和`mutation-types.js`

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
    // this[Types.ACTION_CATEGORYLIST]() // 注意写法
    // 加一层判断，避免每次切换路由组件时都请求一遍接口
    if(this.categoryList.length == 0) { // 如果vuex中没有数据，再去重新请求（用户刷新页面会重新请求）
        this[Types.ACTION_CATEGORYLIST]()
    }
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



# `VueRouter`最佳实践

路由不建议自动生成，但可配置性太低（如批注、钩子）

## 基本配置

见《vue2基本使用》

## 异步组件

除了首页用到的组件，其他组件都可以按需加载

```js
const routes = [
    {
        path: '/lesson',
        name: 'lesson',
        component: () => import('@/views/lesson/index.vue')
    }
]
```

异步组件未加载时，会出现空白页

虽然可以使用`prefetch`让后续页面用到的先加载，但还是不太好，一般会加个`loading`

在`router/index.js`中使用`src/utils/loadable.js`

```js
// ...
import loadable from '@/utils/loadable'

const routes = [
        {
        path: '/lesson',
        name: 'lesson',
        component: loadable(() => import('@/views/lesson/index.vue'))
    }
]
```

## 路由权限

`src/api/user.js`

```js
import axios from '@/utils/axios'

// 登录接口
export const toLogin = (data) => axios.get('/usrer/login', data)
// 验证是否通过
export const validate = () => axios.get('/user/validate')
```

`src/store/modules/user/state.js`

```js
const userState = {
    username: '',
    token: '', // jwt的方式
    hasPermission: false, // 权限有无
    
    authList: [], // 菜单权限列表
    menuPermission: false,
    
    btnPermission: ['edit', 'delete'] // 按钮权限列表
}

export default userState
```

`src/store/action-types.js`

```js
// 设置用户信息 登录需要的
export const SET_LOGIN = 'SET_TOKEN' // 默认点击登录时，会调用一个action
export const SET_USER = 'SET_USER' // 更改存储状态的用户信息 mutation
export const SET_PERMISSION = 'SET_PERMISSION' // 更改权限的 mutation
export const VALIDATE = 'VALIDATE' // 页面一刷新，校验权限的，会调用一个action
```

`src/store/modules/user/actions.js`

```js
import * as Types from '@/store/action-types.js'
import {toLogin, validate} from '@/api/user.js'
const userActions = {
    async [Types.SET_USER]({commit}, {userInfo, has}) {
        commit(Types.SET_USER, userInfo)
        commit(Types.SET_PERMISSION, has) // 标识登陆过了
    },
    
    async [Types.SET_LOGIN]({dispatch}, payload) {
        let userInfo = await toLogin(payload) // 假设后端返回的字段有username(String)/token(String)/authList(Array)[{auth:"points",name:"积分查看",path:"/profile/points"},...]
		dispatch(Types.SET_USER, {userInfo, has: true})
    },
    async [Types.VALIDATE]({commit}, payload) {
        // 此时需要看一下 用户是否登录过
        if(!localStorage.getItem('key')) return false
        
        try {
            // axios中增加token，传到后端，让后端验证去
            // 通过接口持久化vuex
            let userInfo = await validate() // 校验是否登录过
			dispatch(Types.SET_USER, {userInfo, has: true})
            return true // 返回给路由钩子

        } catch(e) {
			dispatch(Types.SET_USER, {userInfo: {}, has: false})
            return false
        }

    }
}
export default userActions
```

`src/store/modules/user/mutations.js`

```js
import * as Types from '@/store/action-types.js'
const userMutations = {
    [Types.SET_USER](state, payload) {
        state.token = payload.token
        state.username = payload.username
        state.authList = payload.authList
        // 也可以用解构赋值的写法
        
        // cookie / localStorage
        if(payload.token) { // 登录完之后，存token到localStorage中
            localStorage.setItem('token', payload.token) // 也可以用封装过的方法
        }
    },
    [Types.SET_PERMISSION](state, payload) {
        state.hasPermission = payload
    }
}
export default userActions
```

`src/router/hooks.js`

```js
impor store from '@/store'
import * as Types from '@/store/action-types'
export default {
    // ...
    'login_permission': async (to, from, next) => {
        // 用户是否需要登录才能访问的标识
        let needLogin = to.matched.some(item => item.meta.needLogin)
        // 如果vuex中有值，我就认为你当前登录了
        if(!store.state.user.hasPermission) {
            // 返回了一个isLogin字段，表示用户是否登陆过了
            // loginWhiteList 可以做一个白名单
        	let isLogin = await store.dispatch(`user/${Types.VALIDATE}`) // 登录校验
            
            if(needLogin) {
                if(!isLogin) {
                    next('/login') // 需要登录，但没登录
                } else {
                	next() // 需要登录，的确也登录了，正常走
                }
            } else { // 不需要登录
                if(to.name == 'login') { // 访问的是登录页
                	if(!isLogin) {
                        next() // 如果没登录，正常访问登录页
                    } else {
                        next('/profile') // 如果已经登录了，访问跳转到个人中心页
                    }
                } else {
                    next() // 不需要登录，访问的是非登录页，正常放行
                }
            }
        } else { // 如果有权限
            if (to.name = '/login') {
                next('/profile') // 访问了登录页，跳转到个人中心
            } else {
                next() // 有权限，访问的是非登录页，正常放行
            }
            
        }
    }
}
```

有些页面不用登录也能访问，有些页面必须需要登录

`src/router/index.js`

```js
// ...
 
const routes = [
    {
        path: 'lesson',
        name: 'lesson',
        component: loadable(() => import('@/views/lesson/index.vue')),
        meta: {
            needLogin: true // 必须要登录
        }
    }
]
```

登录页面

```vue
<script>
    import * as Types from '@/store/action-types.js'
    import FormSubmit from '@/components/form-submit'
    import {Dialog} from 'vant' // 全局引入的只能在template使用，如果要在script中使用，需要额外引入
    import {createNamespacedHelpers} from 'vuex'
    let {mapAcitons} = createNamespacedHelpers('user')
    export default {
        components: {
            FormSubmit
        },
        methods: {
            ...mapAcitons([Types.SET_LOGIN]),
            async submit(values) {
                try {
	                await this[Types.SET_LOGIN](values)
                    this.$router.push('profile')
                } catch(e) {
                    Dialog.alert({
                        title: '登录失败',
                        messgae: e.data
                    })
                }
            }
        }
    }
</script>
```

`views/profile/index.vue`

```vue
<template>
	<div class="profile">
        <vant-nav-bar title="个人中心"></vant-nav-bar>
        <div class="profil-info">
            <!-- 如果功能很多，记得用mapState -->
            <template v-if="!$store.state.user.hasPermission">
                <img src="@/assets/logo.png">
                <van-button size="small">登录</van-button>
			</template>
			<template v-else>
				<!-- 头像上传 -->
				<img src="@/assets/logo.png">
				<span>{{$store.state.user.username}}</span>
			</template>
    	</div>
    </div>
</template>
```



## 菜单权限

后端有一个根据`username`返回不同`path`的接口

后台返回权限信息的接口：

```js
validate() {
    const {ctx, app} = this
    const token = ctx.headers.authorization
    try {
        const decoded = jwt.verify(token, app.config.privateKey)
        let authList
        if(decoded.username = 'admin') {
            authList = [
                {auth: 'lesson', name: '课程管理', path: '/profile/lesson-manager'},
                {auth: 'student', name: '学员管理', path: '/profile/student-manager'}
            ]
        } else {
            authList = [
                {auth: 'points', name: '积分查看', path: '/profile/points'},
                {auth: 'collect', name: '收藏列表', path: '/profile/collect'}
            ]
        }
        ctx.body = {
            err: 0,
            data: {
                username: decoded.username
                // ....
            }
        }
    } catch(e) {
        
    }
}
```

上述返回的`path`对应前台的动态路由

我们在`views/others`文件夹中创建这四个`vue`文件：`lesson-manager.vue`、`student-manager.vue`、`points.vue`、`collect.vue`

由于是动态添加的，我们不能直接写到`router/index.js`中

新建`src/rotuer/permission.js`，该文件中专门放一些权限相关的路由

```js
export default [ // 权限管理，要和后台一一对应
    {
        path: 'lesson-manager',
        component: () => import('@/views/others/lesson-manager'),
        meta: {
            auth: 'lesson' // 存放的值要和后端约定好
        }
    },
    {
        path: 'student-manager',
        component: () => import('@/views/others/student-manager'),
        meta: {
            auth: 'student'
        }
    },
    {
        path: 'points',
        component: () => import('@/views/others/points'),
        meta: {
            auth: 'points'
        }
    },
    {
        path: 'collect',
        component: () => import('@/views/others/collect'),
        meta: {
            auth: 'collect'
        }
    }
]
```

在路由前置钩子里，还需要做一件事：根据菜单权限显示不同的动态组件

`src/router/hooks.js`

```js
impor store from '@/store'
export default {
    // ...
    // 写在路由权限下面
    'menu-permission': async (to, from, next) => {
        // 这里需要对菜单权限进行处理，动态的添加路由
        if(store.state.user.hasPermission) { // 要求用户登录才能拿取菜单的权限
            if(!store.state.user.menuPermission) { // 没有菜单权限
                await store.dispatch(`user/${Types.ADD_ROUTE}`) // 路由动态加载，此时组件是异步的
                // 我希望等待组件加载完毕后，再跳转过去
                next({...to, replace: true}) //让其再重新跳转一次（组件也ok了） hack 再跳一次的时候，菜单权限是有了的
            } else {
                next()
            }
        } else { // 用户没登录
            next()
        }
    }
}
```

`src/store/action-types.js`

```js
// ...
export const ADD_ROUTE = 'ADD_ROUTE' // 动态添加路由 action
export const SET_MENU_PERMISSION = 'SET_MENU_PERMISSION' // mutation
```

`src/store/modules/user/mutations.js`

```js
import * as Types from '@/store/action-types.js'

const userMutations = {
    //...
    [Types.SET_MENU_PERMISSION](state, payload) {
        state.menuPermission = payload
    }
}	
export default userMutations
```

`src/store/modules/user/actions.js`

```js
import * as Types from '@/store/action-types.js'
import per from '@/router/permission.js'
import router from '@/router'
const filterRouter = (authList) => { // 拿每个路由，看在不在权限列表中
    // 有很多种过滤的方式
    // 扁平化过滤，把tree展开，然后一层层过滤，性能更高一点
    
    
    // 递归过滤
    authList = authList.map(item => item.auth)
    function filter(per) {
        let result = per.filter(route => {
            if(authList.includes(route.meta.auth)) {
                if(router.children) { // 嵌套路由，一般不会超过三层
                    route.children = filter(route.children)
                }
                return route
            }
        })
        
        return result
    }
    
    return filter(per)
}
const userActions = {
    // ...
    async [Types.ADD_ROUTE]({commit, dispatch, state}, payload) {
        // 添加路由（菜单）
        // 拿到路由（菜单）的权限再去添加路由
        // 路由（菜单）的权限在vuex中
        let authList = state.authList // 服务端返回的权限
        // 根据后台提供的权限，在前台自定义的权限中，进行过滤（复杂的话可能需要递归）
        let routes = filterRouter(authList)
        // 拿到不同权限对应的动态路由路径后，将路由组件添加到`profile`中
        let route = router.options.routes.find(item => item.path == '/profile') // 可以打印router对象，它有一个options属性
        route.children = routes // 动态添加子组件
        router.addRouter([route]) // 该方法接收一个数组，动态的再向router中添加
        
        commit(Types.SET_MENUPERMISSION, true)
    }
}

export default userActions
```

`profile.vue`

```vue
<template>
	<div class="profile">
        <vant-nav-bar title="个人中心"></vant-nav-bar>
        <div class="profil-info">
            <!-- 如果功能很多，记得用mapState -->
            <template v-if="!$store.state.user.hasPermission">
                <img src="@/assets/logo.png">
                <van-button size="small">登录</van-button>
			</template>
			<template v-else>
				<!-- 头像上传 -->
				<img src="@/assets/logo.png">
				<span>{{$store.state.user.username}}</span>
			</template>
    	</div>
		
		<template  v-if="$store.state.user.menuPermission">
            <vant-tabs types="card">
                <vant-tab 
                          :title="item.name"
                          v-for="(item, index) in $store.state.user.authList"
                          :to="item.path"
                          :key="index"
                          >
                    <!-- item.path中的path，是后端返回的字段 -->
                </vant-tab>            
            </vant-tabs>
 			<!-- 可以再配置个redirect字段，让其默认展示 -->
			<router-view></router-view>
		</template>

    </div>
</template>
```



## 按钮权限

一般也是用户登录的一瞬间，把按钮权限字段，放在`vuex`中

页面中使用指令控制

`src/store/modules/user/state.js`

```js
const userState = {
    username: '',
    token: '', // jwt的方式
    hasPermission: false, // 权限有无
    authList: [], // 菜单权限列表
    menuPermission: false,
    btnPermission: ['edit', 'delete'] // 按钮权限列表，值是根据后台返回的值动态添加
}

export default userState
```

`profile.vue`

```vue
<template>
	<div class="profile">
        <vant-nav-bar title="个人中心"></vant-nav-bar>
        <div class="profil-info">
            <template v-if="!$store.state.user.hasPermission">
                <img src="@/assets/logo.png">
                <van-button size="small">登录</van-button>
			</template>
			<template v-else>
				<img src="@/assets/logo.png">
				<span>{{$store.state.user.username}}</span>
			</template>
    	</div>
		
		<template  v-if="$store.state.user.menuPermission">
            <vant-tabs types="card">
                <vant-tab 
                          :title="item.name"
                          v-for="(item, index) in $store.state.user.authList"
                          :to="item.path"
                          :key="index"
                          >
                </vant-tab>            
            </vant-tabs>
			<router-view></router-view>
		</template>
		
		<template>
			<vant-button v-has="edit">编辑</vant-button>
			<vant-button v-has='delete'>删除</vant-button>
		</template>
    </div>
</template>
```

`src/utils/directives.js`

```js
export default {
    'has': {
        inserted(el, bindings, vnode) {
            let value = bindings.value // 用户写的values值 v-has="vlaue"
            let permission = vnode.context. $store.state.user.btnPermission // 在上下文里找，上下文是当前指令所在组件的组件实例
            if(!permission.includes(value)) {
                el.parentNode.removeChild(el)
            }
        }
    }
}
```

`main.js`中引入指令

```js
// 指令
import directives from '@/utils/directives'
Object.entries(directives).forEach(([id, define]) => {
    Vue.directives(id, define)
})

// 备注：全局组件、过滤器也可以这样封装
```



# `axios`最佳实践

## 函数封装

`utils/request.js`

```js
import axios from "axios";
import Vue from "vue";
// import { Message } from 'element-ui'
// console.log(Vue.prototype.$baseURL); // 验证是否已经把属性挂载在了Vue的原型上

export function request(config) {
  //console.log('request中的router', router)
  const instance = axios.create({
    // baseURL: `http://${Config.ip}:${Config.port}`,
    baseURL: Vue.prototype.$baseURL,
    // timeout: `${Config.timeout}`
  });

  instance.interceptors.request.use(
    (config) => {
      config.headers["Content-Type"] = "application/json";
      // config.headers['Authorization'] = 'Bearer ' + localStorage.getItem('Authorization')
      // console.log(config)
      return config;
    },
    (err) => {
      console.log(err);
      Promise.reject(error);
    }
  );

  instance.interceptors.response.use(
    (res) => {
      return res.data;
    },
    (err) => {
      if (err.response) {
        switch (err.response.status) {
          case 401:
            break;
          default:
            break;
        }
      }
      console.log(err);
      Promise.reject(error);
    }
  );

  return instance(config);
}

```

`api/target.js`

```js
import { request } from "@/utils/request";

// get请求
export function getAllSpider() {
  return request({
    url: "/spider/all",
  });
}

// get请求携带parmas参数或query参数
export function getCounterByDays(nums) {
  return request({
    url: `/counter/all/days/${nums}`,
    // params: {
    //     query: params
    // }
  });
}

// post请求
export function addSpider(data) {
  return request({
    method: "post",
    url: "/spider/add",
    data,
  });
}



```



## 类封装01

### 封装

`utils/axios.js`

```js
import axios from 'axios'
import store from '@/store'
import * as Types from '@/store/actions-types.js'

class HttpRequest {
    constructor() {
        this.baseURL = process.env.NODE_ENV == 'production' ? '/' : 'http://localhost:7001'
        this.timeout = 3000
        // 需要加loading（一般很少加了，但要知道）
        this.queue = {} // 专门用来维护请求队列，页面切换用来取消请求
    }
    
    // 全局拦截器
    setInterceptor(instance, url) { // 设置全局拦截器
        instance.interceptors.request.use((config) => {
            // 开启loading，自己找个地方显示
            if(Object.keys(this.queue).length == 0) {
                // 开loading 
            }
            
            let token = localStorage.getItem('token')
            if(token) {
                // 每次请求都会携带一个权限访问服务器
                config.headers.authorization = token
            }
            
            // 可以记录请求的取消函数
            let CancelToken = axios.CancelToken
            config.cacelToken = new CancelToken((c) => { // 绑定在config上
                // c就是当前取消请求的token
                // 可以存到vuex中，页面切换的时候，组件销毁时执行
                // 涉及到vuex三连环
                store.commit(Types.SET_TOKEN, c) // 同步，将取消方法存入到vuex
                // 那么什么时候清除这些取消请求的token呢？ 在路由切换的时候（放在路由守卫中，只要你一切换路由，就认为请求跳一半了，就取消请求）
            })
            this.queue[url] = true
            return config
        })
        
        instance.interceptors.response.use((res) => {
            delete this.queue[url] // 一旦响应成功了，就删除
            if(Object.keys(this.queue).length == 0) {
                // close loading
            }
            
            if(res.data.err == 0) { //所有的响应体都有这个字段
            	return res.data.data// 这里要结合接口具体字段，可以配合switchCase状态
            }
        }, (err) => {
            delete this.queue[url]
            if(Object.keys(this.queue).length == 0) {
                // close loading
            }
            return Promise.reject(err) // 把报错抛给用户，让用户处理
        })
    }
    
    request(options) { // 通过request方法来进行请求操作
        // 每次请求可以创建一个新的实例，如果业务不复杂可以不创建实例，直接使用`axios`
        // 复杂场景下ab用的是同一个实例的话，要各自加拦截器就不好加，所以需要单独创建实例加拦截器
        let instance = axios.create()
        let config = {
            baseURL: this.baseURL,
            timeout: this.timeout,
            // ...
            ...options
        }
        this.setInterceptor(instance, config.url)
		return instance(config) // 产生的是一个`Promise`
    }
    
    get(url, data={}) { // axios.get('/xxx',{params: xxx})
        return this.request({
            url,
            method: 'get',
            ...data
        })
    }
    
    post(url, data={}) { // axios.post('/xxx', {data})
		return this.request({
        	url,
        	method: 'post',
            data
        })
    }
}

export default new HttpRequest
```

`src/store/action-types.js`

```js
// 设置token
export const SET_TOKEN = 'SET_TOKEN'
export const CLEAR_TOKEN = 'CLEAR_TOKEN'
```

`src/store/index.js`

这个功能是所有路由组件都需要的，可以放在根文件，当然也可以单独抽成一个模块

```js
import Vue from 'vue'
import Vuex from 'vuex'
import modules from './modules/index.js'
import * as Types from '@/store/actions-types'

Vue.use(Vuex)
const store = new Vuex.Store({
    state: { // 公共的状态
        tokens: []
    },
    mutations: {
        [Types.SET_TOKEN](state, token) {
            // 我们希望状态可以被追踪，但一般不会用push方法来更新，而是会用新的数组赋值（内存地址会变化）
    		// state.tokens.push(token) 
            state.tokens = [...state.tokens, token] // 存储token，后续页面切换可以让token一次执行
		},
        [Types.CLEAR_TOKEN](state) { // 一般这一步，放在actions里
            state.tokens.forEach(token => token()) // 执行所有的取消方法，都调用一下
            state.tokens = [] // 清空列表
        }
    },
    modules: {
        ...modules
    }
})

export default store

```

`src/router/hooks.js`

```js
import store from '@/store'
import * as Types from '@/store/action-types.js'
export default {
    // 此字段只是给自己看的
    'clear_token': (to, from, next) => {
        // 这里也可以做一些白名单，不管咋样都允许请求
        // whiteList
        store.commit(Types.CLEAR_TOKEN) // 清空取消请求的token，如果只希望某个页面切换时取消请求，单独放在组件卸载的生命周期钩子里即可
        next() // vue3中支持await的写法
    }
}
```

`src/router/index.js`

```js
import Vue from 'vue'
import VueRouter from 'vue-router'
import hooks from './hooks.js'

Vue.use(VueRouter)
const routes =[
    // ...
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

// 循环的是hooks对象的value
Object.values(hooks).forEach(hook => {
    router.beforeEach(hook)
})

export default router
```



### 使用

新建`src/api/home.js`文件，对应每个页面的接口文件

如果一个页面的接口有很多，可以新建`src/api/config/config.js`，该文件单独维护各个路径

`home/js`

```js
import axois from '@/utils/axios'

export const fetchSliders = () => axios.get('/api/slider')
```

`vue`的走`vuex`的开发流程：`state -> action-types -> api -> actions -> mutations`

发请求的页面

```vue
<script>
	export default {
        //...
        async mounted() {
            // 页面一开始就加载数据
            if(this.slides.length == 0 ){ // 如果vuex中没有数据，获取数据
                try {
                    await this[Types.SET_SLIDES]()
                } catch(e) { // 错误处理、或者异常处理
                    console.log(e) // 这里的异常是处理取消请求token时的报错，应该是用户用的时候自己处理，不能在封装库的时候处理
                }
            }
        }
    }
</script>
```

### 注意点

- 避免路由组件一切换就发请求，可以加一层判断

  ```js
    mounted() {
      // this[Types.ACTION_CATEGORYLIST]() // 注意写法
      // 加一层判断，避免每次切换路由组件时都请求一遍接口
      if(this.categoryList.length == 0) { // 如果vuex中没有数据，再去重新请求（用户刷新页面会重新请求）
          this[Types.ACTION_CATEGORYLIST]()
      }
    },
  ```

- 刷新页面，立刻切换到其他路由组件时，之前的请求应该取消掉

  之前我们在全局的请求拦截器中，加了`cancelToken`，相当于`xhr.abort()`

## 类封装02

### 封装



## 抽离baseURL

https://www.cnblogs.com/jdWu-d/p/12687396.html

在public目录下，新建一个文件，我命名为serverConfig.json，具体如图所示，里面配了一个baseURL。

```json
{
  "baseURL": "http://127.0.0.1:8080"
}

```

新建初始化方法`utils/init.js`

```js
import axios from "axios";
import Vue from "vue";

export async function getServerConfig() {
  return await new Promise((resolve, reject) => {
    axios
      .get("./serverConfig.json")
      .then((res) => {
        console.log("读取外部化配置文件>>>>>>>>");
        console.log(res.data); // 是否成功读取需要的配置项
        for (let key in res.data) {
          console.log(key);
          Vue.prototype["$" + key] = res.data[key];
        }
        console.log(Vue.prototype.$baseURL); // 验证是否已经把属性挂载在了Vue的原型上
        resolve();
      })
      .catch((error) => {
        console.log(error);
        reject();
      });
  });
}

```

然后，在main.js里面定义一个读取这个文件的方法，在初始化的时候读取这个文件。

```js
import {getServerConfig} from "@/utils/init.js";

new Vue({
  router,
  store,
  render: (h) => h(App),
  created() {
    getServerConfig()
  }
}).$mount("#app");

```

如果封装了`axios`，在封装的`js`文件中,读取配置

```js
import 'Vue' from 'vue';


// ...
const instance = axios.create({
    baseURL: Vue.prototype.$baseURL,
    // timeout: `${Config.timeout}`
  });
```





# 持久化最佳实践

## 登录持久化

### `localStorage`



### `cookie`



### `sessionStorage`

记录滚动条位置

### `indexDB`

# 移动端最佳实践

## `em`适配



## `rem`适配

**备注：见《移动端开发基础》**

`postcss-plugin-px2rem`

- 

`lib-flexible`

- 在页面中注入一段脚本，可获取设备`DPR`和屏幕宽度，自动计算`font-size`并添加至`html`节点属性上 

安装：

```
npm i postcss-plugin-px2rem lib-flexible
```

`main.js`中引入

```js
import 'lib/flexible' // 对应设置根的字体（这个插件也可以自己手写）
```

`vue.config.js`新增配置

```js
module.exports = {
    css: {
        loaderOptions: {
            postcss: {
                plugins: [
                    require("postcss-plugin-px2rem")({
                        rootValue: 37.5, // 表示设计稿大小 375 1rem = 37.5 ,vant里设计稿的大小是375px，可以根据实际修改
                        exclude: /node_module/
                    })
                ]
            }
        }
    }
}
```

# 组件最佳实践

## 业务组件



## 路由组件



## 公共组件



## 组件库的样式穿透

https://www.bbsmax.com/A/amd026aWJg/

scoped看起来很好用，当时在Vue项目中，当我们引入第三方组件库时(如使用element-ui)，需要在局部组件中修改第三方组件库样式，而又不想去除scoped属性造成组件之间的样式覆盖。这时我们可以通过特殊的方式**穿透scoped**

**stylus的样式穿透 使用 >>>**

```stylus
.wrapper >>> .swiper-pagination-bullet-active
   background: #fff
```

**sass和less的样式穿透 使用 /deep/**

```scss
// 语法
外层 /deep/ 第三方组件 {
	样式
}
// eg
.wrapper /deep/ .swiper-pagination-bullet-active{
	background: #fff;
}
```

`vue-cli5.0`中使用`/deep/`报错，默认安装的`sass`版本为`1.32.7`，`sass-loader`版本为`12.0.0`

报错信息：

```bash
Error: Module build failed (from ./node_modules/sass-loader/dist/cjs.js):
SassError: expected selector.
```

解决方案：

把`/deep/`写成`::v-deep`



# 控制台警告

## `Added non-passive event listener...`

在使用第三方库时，可能控制台报错如下：

```js
[Violation] Added non-passive event listener to a [scroll](https://so.csdn.net/so/search?q=scroll&spm=1001.2101.3001.7020)-blocking 'mousewheel' event. Consider marking event handler as 'passive' to make the page more responsive.
```

![img](40af32c14abc42c090960d33d2b6b508.png)

![image-20220706104041328](image-20220706104041328.png)

[违规]添加非被动事件[监听器](https://so.csdn.net/so/search?q=监听器&spm=1001.2101.3001.7020)到滚动阻塞'鼠标滚轮'事件。 考虑将事件处理程序标记为“被动”，以使页面响应更快。



**解决方案：**

**1、**npm i default-passive-events -S

2、main.js中加入：import 'default-passive-events'



原因是 Chrome51 版本以后，Chrome 增加了新的事件捕获机制－Passive Event Listeners；

Passive Event Listeners：就是告诉前页面内的事件监听器内部是否会调用preventDefault函数来阻止事件的默认行为，以便浏览器根据这个信息更好地做出决策来优化页面性能。当属性passive的值为true的时候，代表该监听器内部不会调用preventDefault函数来阻止默认滑动行为，Chrome浏览器称这类型的监听器为被动（passive）监听器。目前Chrome主要利用该特性来优化页面的滑动性能，所以Passive Event Listeners特性当前仅支持mousewheel/touch相关事件。

来源：https://blog.csdn.net/Wildness_/article/details/123190078



# 主题颜色管理



