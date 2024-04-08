---
title: '电商平台Vue前台项目'
date: 2022-8-9 09:03:02
cover: false
tags:
- 案例实战
categories: '案例实战'
---



> 技术架构： `vue2 + webpack + vuex + vuerouter + axios + less`
>
> 功能模块：
>
> - 封装通用组件
> - 登录注册
> - `token`
> - 守卫
> - 购物车
> - 支付
> - 项目性能优化...



# 项目初始化及相关配置

## 项目创建

如果有成熟的项目，可以配一套自己的脚手架配置

前置条件：`node环境`

安装`vue-cli`

```bash
npm i vue-cli -D
npx vue create 项目名
```

选择`vue2`

备注：下载慢可以配置淘宝镜像，但2022年了，基本不慢

## 项目目录

项目目录及文件介绍：

- `node_modules`

  - 项目依赖文件夹

- `public`

  - 一般放置一些静态资源（图片）

  - `webpack`进行打包时，会原封不动的打包到`dist`目录

  - 该目录中新建`axios.config.js`，该文件中导出`ip`和`port`，这样无论是开发还是生产，更改环境就很方便，否则生产环境下，服务器信息就被写死在代码里了（低版本的`vue-cli`是`static`文件夹）

    `public/axios.config.js`

    ```js
    const Config= {
      ip: '1.13.**.**',
      port: '80',
    }
    ```

    `axios`中使用，`src/utils.request.js`

    ```js
    export function request(config) {
        const instance = axios.create({
            baseURL: `http://${Config.ip}:${Config.port}`,
            // timeout: `${Config.timeout}`
        })
        
        // ...
    }
    ```

- `src`

  - 源代码文件夹
  - `assets`文件夹
    - 一般也是放置静态资源（多个组件共用的静态资源）
    - `webpack`进行打包时，会把`assets`静态资源当作一个个模块，打包到`JS`文件中
  - `components`文件夹
    - 放置非路由组件（全局组件）
  - `App.vue`
    - 唯一的根组件
  - `man.js`
    - 程序的入口文件

- `babel.config.js`

  - `babel`相关的配置文件，可参阅`babel`官网

- `package.json`

  - 项目的“身份证”，记录项目叫做什么，项目中有哪些依赖，项目怎么运行

- `package-lock.json`

  - 缓存性文件

- `README.md`



## 项目的其他配置

- 配置`src`别名

  - `jsconfig.json`

    ```json
    {
        "compilerOptions": {
            "baseUrl": "./",
            "path": {
                "@/": ["src/"]
            }
        },
        "exclude": ["node_modules", "dist"]
    }
    ```

  - 新版`vue-cli`已经默认支持别名了

- 设置浏览器自动打开

  - `package.json`中的`serve`值，新增`--open`

    ```json
    "scripts": {
        "serve": ”vue-cli service serve --open“
    }
    ```

- 关闭`eslint`

  - 新建`vue.config.js`，新增

    ```js
    module.exports = {
        // 关闭eslint
        lintOnSave: false
    }
    ```



# 项目路由分析及编写

确定路由组件和非路由组件

- 路由组件
  - `Home`首页路由组件
  - `Search`路由组件
  - `Login`登录路由组件
  - `Register`注册路由组件
- 非路由组件
  - `Header`
    - 在首页、搜索页
  - `Footer`
    - 在首页、搜索页中有
    - 在注册、登录页中没有

## 非路由组件

根据静态资源，将静态资源拆分成一个个组件：资源来源：[静态页面](https://gitee.com/jch1011/shangpinhui_0415/tree/master/%E5%89%8D%E5%8F%B0%E9%A1%B9%E7%9B%AE_STUDENT%20(1)/%E4%BB%A3%E7%A0%81/%E9%9D%99%E6%80%81%E9%A1%B5%E9%9D%A2)

目录结构：

- `components`
  - `Footer`
    - `index.vue`
  - `Header`
    - `index.vue`

注意：这里为了便于掌控`dom`结构， 可以不直接复制，采用半复制的形式，也要具体看下怎么写的



新建`components/Header/index.vue`

- 定义组件

  - 复制`html`结构到`template`中

  - 复制对弈的`less`样式到`style`中，配置`lang=less`，安装`less`和`less-loader`：`npm i less less-loader`

  - 将公共组件各自需要的图片资源，保存在各自的文件夹下的`images`文件夹下

- `public`文件夹在在`index.html`中引入`reset.css`及相关的图标字体文件
- 在`App.vue`中引入组件并使用



新建`components/Footer/index.vue`，同上操作

## 路由组件

`Home`、`Search`、`Login`、`Register`

目录结构

- `pages`
  - `Home`
    - `index.vue`
  - `Search`
    - `index.vue`
  - `Login`
    - `index.vue`
  - `Register`
    - `index.vue`

- 定义各个路由组件
- 在`router`文件夹的`index.js`中，定义前端路由和路由组件的映射关系（使用懒加载的方式导入）
  - 重定向首页
- 设置相应的路由跳转
  - 登录、注册和回到首页，使用声明式导航
  - 搜索，使用编程式导航
    - 指定搜索的回调函数`goSearch`

## 非路由组件的显示与隐藏

- 使用路由元信息实现`Footer`路由的显示与隐藏
  - 登录、注册路由下，`Footer`组件是没有的
  - 首页、搜索路由下，`Footer`组件是显示的
- 配置四个路由组件的路由元信息
- 使用`v-show`配合`$route.meta.show`控制`Footer`组件的显示与隐藏

## 路由传参

- 使用对象形式进行`params`和`query`方式传参
- 配置`params`可以不传参数
- 传递`pramas`参数时，取值可以用或表达式，使用`undefined`解决`params`值为空的情况
- 重写`push`方法和`replace`方法

# 功能模块

## 首页模块

- 根据静态页面，将三级联动功能、轮播图+快报、今日推荐、热卖排行、猜你喜欢、品牌模块封装成组件
- `Home`目录下，新建三级联动组件`TypeNav`，并注册为全局组件
- 新建`ListContainer`组件（轮播图）
- 







































