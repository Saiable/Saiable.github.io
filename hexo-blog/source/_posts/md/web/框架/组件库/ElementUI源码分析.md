---
title: 'ElementUI源码分析'
date: 2022-11-20 21:30:40
cover: false
tags:
- 组件库
categories: '组件库'
typora-root-url: ElementUI源码分析
---



# 初始化

新建文件夹`ElementUI`

`npm init -y`初始化空的`package.json`

`npm install element-ui -S`安装

`json`

```json
{
  "name": "elementui",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "element-ui": "^2.15.12"
  }
}
```

只装了`element-ui`（以下简称`element`），`node_modules`文件夹如下

![image-20221120180724796](image-20221120180724796.png)

# 目录结构

![image-20221120180948695](image-20221120180948695.png)

- `lib`
  - 存放`element`打包后的文件，也就是我们使用时实际依赖的文件
- `packages`
  - 存放组件相关的源代码
- `src`
  - 存放了像指令、混入、工具方法等源代码
- `types`
  - 存放了`ts`的类型声明文件
- 重点
  - `packages`
  - `types`


## `packages`文件夹

该目录下的文件夹，都是以我们使用的组件命名的

![image-20221121061533964](image-20221121061533964.png)

以`card`文件夹为例

- `index.js`

  - 导出了一个`install`方法，内容是全局注册`Card`组件

  - 这也是可以直接通过`Vue.use`注册组件的原因

  ```js
  import Card from './src/main';
  
  /* istanbul ignore next */
  Card.install = function(Vue) {
    Vue.component(Card.name, Card);
  };
  
  export default Card;
  
  ```

- `src/main.vue`

  ```vue
  <template>
    <div class="el-card" :class="shadow ? 'is-' + shadow + '-shadow' : 'is-always-shadow'">
      <div class="el-card__header" v-if="$slots.header || header">
        <slot name="header">{{ header }}</slot>
      </div>
      <div class="el-card__body" :style="bodyStyle">
        <slot></slot>
      </div>
    </div>
  </template>
  
  <script>
    export default {
      name: 'ElCard',
      props: {
        header: {},
        bodyStyle: {},
        shadow: {
          type: String
        }
      }
    };
  </script>
  
  ```

有些组件的代码，并不会存放在组件同名文件夹下，比如`el-form-item`组件，这个组件一般会与`el-form`组件一起使用，相当于`el-form`的子孙组件，这种组件的`vue`文件一般会放在祖先组件的文件夹下

![image-20221121063423818](image-20221121063423818.png)

## 案例分析

`el-input`可以搭配`el-form-item`实现表单验证

