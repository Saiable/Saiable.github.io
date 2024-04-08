---
title: 'node基础'
date: 2022-11-03 07:15:24
cover: false
typora-root-url: node基础
tags:
- Node.js
---



> [Node.js 简介 (nodejs.cn)](http://dev.nodejs.cn/learn)这个中文网，就整了个翻译，然后收109/半年。。。咱具体的api还是看英文吧
>
> [Usage and example | Node.js v18.12.0 Documentation (nodejs.org)](https://nodejs.org/dist/latest-v18.x/docs/api/synopsis.html)

# `Node`安装

## 下载

## 配置环境变量

## `nvm`管理多版本的`node`

[nvm文档手册 - nvm是一个nodejs的版本管理工具 (uihtm.com)](https://nvm.uihtm.com/)



# Node.js 简介

Node.js 是一个开源和跨平台的 JavaScript 运行时环境。 它几乎是任何类型项目的流行工具！

Node.js 在浏览器之外运行 V8 JavaScript 引擎（Google Chrome 的内核）。 这使得 Node.js 的性能非常好。

Node.js 应用程序在单个进程中运行，无需为每个请求创建新的线程。 Node.js 在其标准库中提供了一组异步的 I/O 原语，以防止 JavaScript 代码阻塞，通常，Node.js 中的库是使用非阻塞范式编写的，使得阻塞行为成为异常而不是常态。

当 Node.js 执行 I/O 操作时（比如从网络读取、访问数据库或文件系统），Node.js 将在响应返回时恢复操作（而不是阻塞线程和浪费 CPU 周期等待）。

这允许 Node.js 使用单个服务器处理数千个并发连接，而不会引入管理线程并发（这可能是错误的重要来源）的负担。

Node.js 具有独特的优势，因为数百万为浏览器编写 JavaScript 的前端开发者现在无需学习完全不同的语言，就可以编写除客户端代码之外的服务器端代码。

在 Node.js 中，可以毫无问题地使用新的 ECMAScript 标准，因为你不必等待所有用户更新他们的浏览器，你负责通过更改 Node.js 版本来决定使用哪个 ECMAScript 版本，你还可以通过运行带有标志的 Node.js 来启用特定的实验性功能。

## 大量的库

npm 以其简单的结构帮助 Node.js 生态系统蓬勃发展，现在 npm 仓库托管了超过 1,000,000 个开源包，你可以自由使用。

## Node.js 应用程序的示例

Node.js 中最常见的 Hello World 示例是 Web 服务器：

```js
const http = require('http')

const hostname = '127.0.0.1'
const port = 3000

const server = http.createServer((req, res) => {
  res.statusCode = 200
  res.setHeader('Content-Type', 'text/plain')
  res.end('Hello World\n')
})

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`)
})

```

启动http服务

![image-20221103203843976](image-20221103203843976.png)

浏览器访问

![image-20221103203913961](image-20221103203913961.png)

要运行此代码片段，则将其另存为 `server.js` 文件并在终端中运行 `node server.js`。（本例中是index.js）

此代码首先引入 Node.js [`http` 模块](http://nodejs.cn/api/http.html)。

Node.js 有一个很棒的[标准库](http://nodejs.cn/api/)，包括一流的网络支持。

`http` 的 `createServer()` 方法创建新的 HTTP 服务器并返回。

服务器设置为监听指定的端口和主机名。 当服务器准备好时，则回调函数被调用，在此示例中会通知我们服务器正在运行。

每当接收到新请求时，都会调用 [`request` 事件](http://nodejs.cn/api/http.html#http_event_request)，其提供两个对象：请求（[`http.IncomingMessage`](http://nodejs.cn/api/http.html#http_class_http_incomingmessage) 对象）和响应（[`http.ServerResponse`](http://nodejs.cn/api/http.html#http_class_http_serverresponse) 对象）。

这两个对象对于处理 HTTP 调用是必不可少的。

第一个提供请求的详细信息。 在这个简单的示例中，它没有被使用，但是你可以访问请求头和请求数据。

第二个用于向调用者返回数据。

在此示例中：

```js
res.statusCode = 200
```

我们将 statusCode 属性设置为 200，以指示成功响应。

我们设置了 Content-Type 标头：

```js
res.setHeader('Content-Type', 'text/plain')
```

然后我们关闭响应，将内容作为参数添加到 `end()`：

```js
res.end('Hello World\n')
```

## Node.js 框架和工具

Node.js 是一个底层平台。 为了让开发者的工作变得轻松有趣，社区在 Node.js 上构建了数千个库。

许多随着时间的推移而成为流行的选择。 以下是值得学习的部分列表：

- [**AdonisJS**](https://adonisjs.com/)：基于 TypeScript 的全功能框架，高度关注开发者的效率、稳定和信任。Adonis 是最快的 Node.js Web 框架之一。
- [**Egg.js**](https://eggjs.org/en/)：使用 Node.js 和 Koa 构建更好的企业级框架和应用程序的框架。
- [**Express**](https://expressjs.com/)：提供了最简单而强大的方式来创建 Web 服务器。它的极简主义方法、没有偏见、专注于服务器的核心功能，是其成功的关键。
- [**Fastify**](https://fastify.io/)：高度专注于以最少的开销和强大的插件架构提供最佳开发者体验的 Web 框架。Fastify 是最快的 Node.js Web 之一 构架。
- [**FeatherJS**](https://feathersjs.com/)：Feathers 是轻量级的网络框架，用于使用 JavaScript 或 TypeScript 创建实时应用程序和 REST API。在几分钟内构建原型，在几天内构建可用于生产的应用程序。
- [**Gatsby**](https://www.gatsbyjs.com/)：基于 [React](https://reactjs.org/)、由 [GraphQL](https://graphql.org/) 驱动的静态网站生成器，具有非常丰富的插件和启动器生态系统。
- [**hapi**](https://hapijs.com/)：用于构建应用程序和服务的富框架，使开发者能够专注于编写可重用的应用程序逻辑，而不是花时间搭建基础设施。
- [**koa**](http://koajs.com/)：由 Express 背后的同一个团队构建，旨在更简单、更小，建立在多年知识的基础上。新项目的诞生是为了在不破坏现有社区的情况下创建不兼容的更改。
- [**Loopback.io**](https://loopback.io/)：使构建需要复杂集成的现代应用程序变得容易。
- [**Meteor**](https://meteor.com/)：非常强大的全栈框架，为您提供同构的方法来使用 JavaScript 构建应用程序，在客户端和服务器上共享代码。曾经是提供所有功能的现成工具，现在可以与前端库 [React](https://reactjs.org/)、[Vue](https://vuejs.org/) 和 [Angular](https://angular.io/) 集成。也可用于创建移动应用程序。
- [**Micro**](https://github.com/zeit/micro)：提供了非常轻量级的服务器来创建异步的 HTTP 微服务。
- [**NestJS**](https://nestjs.com/)：基于 TypeScript 的渐进式 Node.js 框架，用于构建企业级的高效、可靠和可扩展的服务器端应用程序。
- [**Next.js**](https://nextjs.org/)：[React](https://reactjs.org/) 框架，为您提供最佳的开发者体验，包括生产所需的所有功能：混合静态和服务器渲染、TypeScript 支持、智能捆绑、路由预取等。
- [**Nx**](https://nx.dev/)：使用 NestJS、Express、[React](https://reactjs.org/)、[Angular](https://angular.io/) 等进行全栈大仓开发的工具包！Nx 有助于将您的开发从构建单个应用程序的团队扩展到多个团队协作开发多个应用程序！
- [**Remix**](https://remix.run/)：Remix 是一个全栈 Web 框架，用于为 web 构建出色的用户体验。它开箱即用，提供构建现代 web 应用程序所需的一切（包括前端和后端）并将其部署到任何基于 JavaScript 的运行时环境（包括 Node.js）。
- [**Sapper**](https://sapper.svelte.dev/)：Sapper 是用于构建各种规模的 Web 应用程序的框架，具有优美的开发体验和灵活的基于文件系统的路由。提供 SSR 等等！
- [**Socket.io**](https://socket.io/): 构建网络应用的实时通信引擎。
- [**Strapi**](https://strapi.io/)：Strapi 是灵活开源的 Headless CMS，让开发者可以自由选择他们喜欢的工具和框架，同时还允许编辑人员轻松管理和分发他们的内容。通过插件系统使管理面板和 API 可扩展，Strapi 使世界上最大的公司能够在构建精美的数字体验的同时加速内容交付。

# Node.js简史

信不信由你，Node.js 诞生才 12 年。

相比之下，JavaScript 已存在 [26 年](https://en.wikipedia.org/wiki/JavaScript#Beginnings_at_Netscape) ，而 Web 则是 [33 年](https://howoldistheinter.net/)。

12 年在技术领域并不是很长的时间，但 Node.js 似乎已经存在很久了。

在这篇文章中，我们绘制了 Node.js 历史的大图，以透视事物。

## 一点历史

JavaScript 是一门编程语言，由 Netscape 创建，作为脚本工具用于在其浏览器 [Netscape Navigator](https://en.wikipedia.org/wiki/Netscape_Navigator) 中操作网页。

Netscape 的部分商业模式是销售 Web 服务器，其中包括一个名为 Netscape LiveWire 的环境，可以使用服务器端 JavaScript 创建动态页面。 不幸的是，Netscape LiveWire 并不是很成功，服务器端 JavaScript 直到最近才流行起来，因为 Node.js 的引入。

引领 Node.js 兴起的一个关键因素是时机。 就在几年前，由于“Web 2.0”应用程序（如 Flickr、Gmail 等）向世界展示了网络上的现代体验，JavaScript 才开始被视为一门更严肃的语言。

随着许多浏览器竞相为用户提供最佳性能，JavaScript 引擎也变得相当出色。 主流浏览器背后的开发团队努力为 JavaScript 提供更好的支持，并找到使 JavaScript 运行得更快的方法。 Node.js 在引擎盖下使用的引擎 V8（也称为 Chrome V8，因为它是 Chromium 项目的开源 JavaScript 引擎），由于这场竞争而得到了显着改进。

Node.js 恰好是在正确的时间和地点构建的，但运气并不是它今天流行的唯一原因。 它为 JavaScript 服务端开发引入了很多创新思维和方法，已经帮助了很多开发者。

## 2009

- Node.js 诞生
- 第一版的 [npm](https://www.npmjs.com/) 被创建

## 2010

- [Express](https://expressjs.com/) 诞生
- [Socket.io](https://socket.io/) 诞生

## 2011

- npm 发布 1.0 版本
- 较大的公司（LinkedIn、Uber 等）开始采用 Node.js
- [hapi](https://hapi.dev/) 诞生

## 2012

- 普及速度非常快

## 2013

- 第一个使用 Node.js 的大型博客平台：[Ghost](https://ghost.org/)
- [Koa](https://koajs.com/) 诞生

## 2014

- 大分支：[io.js](https://iojs.org/) 是 Node.js 的一个主要分支，目的是引入 ES6 支持并加快推进速度

## 2015

- [Node.js 基金会](https://foundation.nodejs.org/) 诞生
- IO.js 被合并回 Node.js
- npm 引入私有模块
- Node.js 4（以前从未发布过 1、2 和 3 版本）

## 2016

- [leftpad 事件](https://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm)
- [Yarn](https://yarnpkg.com/en/) 诞生
- Node.js 6

## 2017

- npm 更加注重安全性
- Node.js 8
- HTTP/2
- V8 在其测试套件中引入了 Node.js，除了 Chrome 之外，Node.js 正式成为 JS 引擎的标杆
- 每周 30 亿次 npm 下载

## 2018

- Node.js 10
- [ES 模块](https://nodejs.org/api/esm.html) .mjs 实验支持
- Node.js 11

## 2019

- Node.js 12
- Node.js 13

## 2020

- Node.js 14
- Node.js 15

## 2021

- Node.js 16
- Node.js 17

# 如何安装 Node.js

Node.js 可以通过多种方式安装。 这篇文章重点介绍了最常见、最方便的几种。

所有主流平台的官方软件包都可以在 http://nodejs.cn/download/ 获得。

安装 Node.js 的一种非常方便的方式是通过包管理器。 对于这种情况，每种操作系统都有其自身的包管理器。

其他适用于 MacOS、Linux 和 Windows 的包管理器列出在 http://nodejs.cn/download/package-manager/。

`nvm` 是一种流行的运行 Node.js 的方式。 例如，它可以轻松地切换 Node.js 版本，也可以安装新版本用以尝试并且当出现问题时轻松地回滚。

这对于使用旧版本的 Node.js 来测试你的代码非常有用。

有关此选项的更多信息，请参阅 https://github.com/nvm-sh/nvm。

无论如何，当安装 Node.js 后，你就可以在命令行中访问 `node` 可执行程序。



# 使用 Node.js 需要了解多少 JavaScript

作为初学者，很难达到对自己的编程能力有足够信心的地步。

在学习编码时，您可能还会对 JavaScript 和 Node.js 的边界感到困惑。

在深入研究 Node.js 之前，我建议您能很好地掌握主要的 JavaScript 概念：

- 词汇结构
- 表达式
- 类型
- 类
- 变量
- 函数
- this
- 箭头函数
- 循环
- 作用域
- 数组
- 模板字面量
- 分号
- 严格模式
- ECMAScript 6、2016、2017

牢记这些概念，您就可以成为一名精通浏览器和 Node.js 的 JavaScript 开发人员。

以下概念也是理解异步编程的关键，异步编程是 Node.js 的基本组成部分之一：

- [异步编程和回调](http://nodejs.cn/learn/javascript-asynchronous-programming-and-callbacks)
- [定时器](http://nodejs.cn/learn/discover-javascript-timers)
- [Promise](http://nodejs.cn/learn/understanding-javascript-promises)
- [异步和等待](http://nodejs.cn/learn/modern-asynchronous-javascript-with-async-and-await)
- 闭包
- [事件循环](http://nodejs.cn/learn/the-nodejs-event-loop)

# Node.js 和浏览器的区别

浏览器和 Node.js 都使用 JavaScript 作为其编程语言。

构建在浏览器中运行的应用程序与构建 Node.js 应用程序完全不同。

尽管它始终是 JavaScript，但有一些关键的差异使体验完全不同。

从广泛使用 JavaScript 的前端开发人员的角度来看，Node.js 应用程序带来了巨大的优势：使用一种语言编写所有东西（前端和后端）的舒适性。

你有一个巨大的机会，因为我们知道完全、深入地学习一门编程语言是多么困难，并且通过使用同一种语言在 web 上执行你的所有工作，无论是在客户端还是在服务器上，你都处于独特的优势地位。

改变的是生态系统。

在浏览器中，您所做的大部分时间都是与 DOM 或其他 Web 平台 API（如 Cookies）进行交互。 这些当然在 Node.js 中不存在。 您没有浏览器提供的 `document`、`window` 和所有其他对象。

在浏览器中，我们没有 Node.js 通过其模块提供的所有友好的 API，比如文件系统访问功能。

另一个很大的不同是在 Node.js 中你可以控制环境。 除非您正在构建一个任何人都可以在任何地方部署的开源应用程序，否则您知道将在哪个版本的 Node.js 上运行该应用程序。 与浏览器环境（您无法奢侈地选择访问者将使用哪种浏览器）相比，这非常方便。

这意味着您可以编写您的 Node.js 版本支持的所有现代的 ES6-7-8-9 JavaScript。

由于 JavaScript 的发展速度如此之快，但浏览器的升级速度可能会有点慢，有时在 web 上你会被旧的 JavaScript / ECMAScript 版本所困扰。

你可以在将代码发布到浏览器之前使用 Babel 将代码转换为 ES5 兼容，但在 Node.js 中，你不需要它。

另一个不同之处是 Node.js 使用 CommonJS 模块系统，而在浏览器中我们开始看到正在实施的 ES Modules 标准。

在实践中，这意味着你暂时在 Node.js 中使用 `require()`，在浏览器中使用 `import`。

# V8 JavaScript 引擎

V8 是驱动 Google Chrome 的 JavaScript 引擎的名称。 这是在使用 Chrome 浏览时获取我们的 JavaScript 并执行它的东西。

V8 提供了 JavaScript 执行的运行时环境。 DOM 和其他 Web 平台 API 由浏览器提供。

很酷的是 JavaScript 引擎独立于它所在的浏览器。 这个关键特性促成了 Node.js 的兴起。 早在 2009 年，V8 就被选为驱动 Node.js 的引擎，随着 Node.js 的流行，V8 成为现在为大量使用 JavaScript 编写的服务器端代码提供驱动的引擎。

Node.js 生态系统非常庞大，这要归功于 V8，它还支持桌面应用程序，例如 Electron 等项目。

## 其他 JS 引擎

其他浏览器有自己的 JavaScript 引擎：

- Firefox 具有 [**SpiderMonkey**](https://spidermonkey.dev/)
- Safari 具有 [**JavaScriptCore**](https://developer.apple.com/documentation/javascriptcore)（也称为 Nitro）
- Edge 最初基于 [**Chakra**](https://github.com/Microsoft/ChakraCore)，但最近[使用 Chromium 和 V8 引擎重建](https://support.microsoft.com/en-us/help/4501095/download-the-new-microsoft-edge-based-on-chromium)。

还有许多其他的存在。

所有这些引擎都实现了 [ECMA ES-262 标准](https://www.ecma-international.org/publications/standards/Ecma-262.htm)，也称为 ECMAScript（JavaScript 使用的标准）。

## 追求性能

V8 是用 C++ 编写的，并且在不断改进。 它是可移植的，可以在 Mac、Windows、Linux 和其他几个系统上运行。

在此 V8 介绍中，我们将忽略 V8 的实现细节：它们可以在更权威的网站上找到（例如 [V8 官方网站](https://v8.dev/)），它们经常会从根本上随着时间的推移而变化。

V8 一直在发展，就像周围的其他 JavaScript 引擎一样，以加速 Web 和 Node.js 生态系统。

在 web 上，性能竞赛已经持续了多年，我们（作为用户和开发人员）从这场竞争中受益匪浅，因为我们年复一年地获得更快、更优化的机器。

## 编译

JavaScript 通常被认为是一门解释型语言，但是现代的 JavaScript 引擎不再只是解释 JavaScript，它们会编译它。

这从 2009 年开始发生，当时 SpiderMonkey JavaScript 编译器被添加到 Firefox 3.5 中，所有人都遵循这个想法。

JavaScript 由 V8 在内部使用即时 (JIT) 编译以加快执行速度。

这可能看起来有悖常理，但自从 2004 年 Google 地图推出以来，JavaScript 已经从一门通常执行几十行代码的语言发展为在浏览器中运行数千到数十万行代码的完整应用程序。

我们的应用程序现在可以在浏览器中运行数小时，而不仅仅是一些表单验证规则或简单的脚本。

在这个新世界中，编译 JavaScript 非常有意义，因为虽然准备好 JavaScript 可能需要更多时间，但是一旦完成，它将比纯粹的解释型代码性能更高。



# `Node.js`基本使用

















































