---
title: 'vue-cli脚手架的应用、配置和性能优化'
date: 2022/8/9 09:03:02
cover: false
tags:
- vue-cli
typora-root-url: vue-cli脚手架的应用、配置和性能优化
---

# vue-cli中自定义配置webpack

## 加入自己的配置

![img](a6ad7a93589d4d4e8ac8f4392be971f7.png)

## 说明

[配置参考 | Vue CLI](https://cli.vuejs.org/zh/config/#devserver-proxy)

 `configureWebpack` ： 如果是对象则会合并到 `webpack` 中（相同的会覆盖），如果是函数则可以通过参数直接修改添加配置，其他配置直接写在 `module.exports` 最外层即可



# `vue add`和`npm install`区别

创建的项目依赖：

vue add 是什么方法？
1、vue add可能会改变现有的项目结构，但是npm install仅仅是安装包而不会改变项目的结构。

2、add如果你下载的库, 特别是 Ui 库, 希望对脚手架结构产生影响,那就选择
vue add xxx

3、npm如果不希望对脚手架结构产生影响, 只是单纯的使用, 比如 axios 这个插件，那就选择
npm install xxx

vue add 除了會 npm install 之外，還會幫你配置好一個範例文件。需要注意的是這個指令會更改你現有的文件內容。
特別的是使用 vue add router 或是 vue add vuex，他們雖然不是插件，但Vue CLI會幫你配置好文件，
例如 vue add router 會幫你配置 router.js 文件以及生成 About.vue 和 Home.vue 並在 App.vue 內建立了簡單的路由範例，而 vue add vuex 會幫你配置好一個 store.js 文件。

