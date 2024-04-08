---
title: 'Vant UI'
date: 2022-12-16 07:15:24
cover: false
tags:
- Vant
typora-root-url: VantUI
---



[快速上手 - Vant 4 (gitee.io)](https://vant-contrib.gitee.io/vant/#/zh-CN/quickstart)



# 安装

下载

```bash
# Vue 3 项目，安装最新版 Vant
npm i vant

# Vue 2 项目，安装 Vant 2
npm i vant@latest-v2

```

## 按需引入组件样式

在基于 `vite`、`webpack` 或 `vue-cli` 的项目中使用 Vant 时，可以使用 [unplugin-vue-components](https://github.com/antfu/unplugin-vue-components) 插件，它可以自动引入组件，并按需引入组件的样式。

相比于常规用法，这种方式可以按需引入组件的 CSS 样式，从而减少一部分代码体积，但使用起来会变得繁琐一些。如果业务对 CSS 的体积要求不是特别极致，我们推荐使用更简便的常规用法。

### 安装插件

```bash
# 通过 npm 安装
npm i unplugin-vue-components -D

# 通过 yarn 安装
yarn add unplugin-vue-components -D

# 通过 pnpm 安装
pnpm add unplugin-vue-components -D
```

### 配置插件

如果是基于 `vite` 的项目，在 `vite.config.js` 文件中配置插件：

```js
import vue from '@vitejs/plugin-vue';
import Components from 'unplugin-vue-components/vite';
import { VantResolver } from 'unplugin-vue-components/resolvers';

export default {
  plugins: [
    vue(),
    Components({
      resolvers: [VantResolver()],
    }),
  ],
};
```

如果是基于 `vue-cli` 的项目，在 `vue.config.js` 文件中配置插件：

```js
const { VantResolver } = require('unplugin-vue-components/resolvers');
const ComponentsPlugin = require('unplugin-vue-components/webpack');

module.exports = {
  configureWebpack: {
    plugins: [
      ComponentsPlugin({
        resolvers: [VantResolver()],
      }),
    ],
  },
};
```

如果是基于 `webpack` 的项目，在 `webpack.config.js` 文件中配置插件：

```js
const { VantResolver } = require('unplugin-vue-components/resolvers');
const ComponentsPlugin = require('unplugin-vue-components/webpack');

module.exports = {
  plugins: [
    ComponentsPlugin({
      resolvers: [VantResolver()],
    }),
  ],
};
```

### 使用组件

完成以上两步，就可以直接在模板中使用 Vant 组件了，`unplugin-vue-components` 会解析模板并自动注册对应的组件。

```html
<template>
  <van-button type="primary" />
</template>
```

### 引入函数组件的样式

Vant 中有个别组件是以函数的形式提供的，包括 `Toast`，`Dialog`，`Notify` 和 `ImagePreview` 组件。在使用函数组件时，`unplugin-vue-components` 无法自动引入对应的样式，因此需要手动引入样式。

```js
// Toast
import { showToast } from 'vant';
import 'vant/es/toast/style';

// Dialog
import { showDialog } from 'vant';
import 'vant/es/dialog/style';

// Notify
import { showNotify } from 'vant';
import 'vant/es/notify/style';

// ImagePreview
import { showImagePreview } from 'vant';
import 'vant/es/image-preview/style';
```

你可以在项目的入口文件或公共模块中引入以上组件的样式，这样在业务代码中使用组件时，便不再需要重复引入样式了。