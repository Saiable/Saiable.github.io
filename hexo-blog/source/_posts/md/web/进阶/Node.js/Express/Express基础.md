---
title: 'Express基础'
date: 2023-01-07 09:03:02
cover: false
tags:
- Express
categories: Express
---

[Vue+Express+Mysql 全栈初体验 - 掘金 (juejin.cn)](https://juejin.cn/post/6844903853704347655#heading-0)



# `Express`是什么

`Express`是一个快速、简单、极简的`Node.js web`应用开发框架。通过它，可以轻松的构建各种`web`应用。例如

- 接口服务
- 传统的web网站
- 开发工具集成等
- ...

Express本身是极简的，仅仅提供了web开发的基础功能，但是它通过中间件的方式继承了许许多多的外部插件来处理http请求

- `body-parse`：解析`HTTP`请求体
- `compression`：压缩`HTTP`响应
- `cookie-parser`：解析`cookie`数据
- `cors`：处理跨域资源请求
- `morgan`：`HTTP`请求日志记录
- ...
- 



`Express`中间件的特性固然强大，但是它所提供的灵活性是一把双刃剑。

- 它让`Express`本身变得更加灵活和简单
- 缺点在于虽然有一些中间件包可以解决几乎所有问题和需求，但是挑选合适的包有时也会成为一个挑战
  - 由此延伸出的另外的问题时，如果没有选择合适的包，在某些问题的处理上，就会有很多坑，需要付出额外的时间和精力
  - 因此对于不用场景下中间件的选择和认知，是要有的

`Express`不对`Node.js`已有的特性进行二次抽象，只是在它之上扩展了`web`应用所需的基本功能

- 内部使用的还是`http`模块
- 请求对象继承自`http.IncomingMessage`
- 响应对象继承自`http.ServerResponse`
- ...



有很多流行框架基于`Express`

- `LoopBack`：高度可扩展的开源`Node.js`框架，用于快速创建动态的端到端`REST API`
- `Sails`：用于`Node.js`的`MVC`框架，用于构建使用的，可用于生产的应用程序
- `NestJs`：一个渐进式的`Node.js`框架，用于在`TypeScript`和`JavaScript`之上构建高效，可扩展的企业级服务器端应用程序
- ...



`Express`的开发作者是知名的开源项目创建者和写作者`TJ Holowaychuk`

- Github: https://github.com/tj
- Express、commander、ejs、co、Koa...



`Express`特性



# `Express`特性

- 简单易学
- 丰富的基础API特性，以及常见的HTTP辅助程序，例如重定向、缓存等
- 强大的路由功能
- 灵活的中间件
- 高性能





