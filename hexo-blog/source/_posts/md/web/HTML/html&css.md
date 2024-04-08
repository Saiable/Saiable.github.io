---
title: 'html&cs'
date: 2022-8-9 07:28:42
cover: false
---

[TOC]



# CSS

## CSS工程化

原文链接：https://mp.weixin.qq.com/s/ghTj7uREeYrsbZhdEvWc1A

大家好，我是皮汤。最近业务调整，组内开启了前端工程化方面的基建，我主要负责 CSS 技术选型这一块，针对目前业界主流的几套方案进行了比较完善的调研与比较，分享给大家。

目前整个 CSS 工具链、工程化领域的主要方案如下：

![css01](html&css.assets/css01.webp)

而我们技术选型的标准如下：

- 开发速度快
- 开发体验友好
- 调试体验友好
- 可维护性友好
- 扩展性友好
- 可协作性友好
- 体积小
- 有最佳实践指导

目前主要需要对比的三套方案：

- Less/Sass + PostCSS 的纯 CSS c侧方案
- styled-components / emotion 的纯 CSS-in-JS 侧方案
- TailwindCSS 的以写辅助类为主的 HTML 侧方案

### 纯 CSS 侧方案

#### 介绍与优点

![lessgit](html&css.assets/lessgit.webp)

> 维护状态：一般

> Star 数：16.7K

> 支持框架：无框架限制

> 项目地址：https://github.com/less/less.js

Less/Sass + PostCSS 这种方案在目前主流的组件库和企业级项目中使用很广，如 ant-design 等

它们的主要作用如下：

- 为 CSS 添加了类似 JS 的特性，你也可以使用变量、mixin，写判断等
- 引入了模块化的概念，可以在一个 less 文件中导入另外一个 less 文件进行使用
- 兼容标准，可以快速使用 CSS 新特性，兼容浏览器 CSS 差异等

这类工具能够与主流的工程化工具一起使用，如 Webpack，提供对应的 loader 如 sass-loader，然后就可以在 React/Vue 项目中建 `.scss` 文件，写 sass 语法，并导入到 React 组件中生效。

比如我写一个组件在响应式各个断点下的展示情况的 sass 代码：

```less
.component {

  width: 300px;

  @media (min-width: 768px) {

    width: 600px;

    @media  (min-resolution: 192dpi) {

      background-image: url(/img/retina2x.png);

    }

  }

  @media (min-width: 1280px) {

    width: 800px;

  }

}
```

或导入一些用于标准化浏览器差异的代码：

```less
@import "normalize.css"; 



// component 相关的其他代码
```

#### 不足

这类方案的一个主要问题就是，只是对 CSS 本身进行了增强，但是在帮助开发者如何写更好的 CSS、更高效、可维护的 CSS 方面并没有提供任何建议。

- 你依然需要自己定义 CSS 类、id，并且思考如何去用这些类、id 进行组合去描述 HTML 的样式
- 你依然可能会写很多冗余的 Less/Sass 代码，然后造成项目的负担，在可维护性方面也有巨大问题

#### 优化

- 可以引入 CSS 设计规范：BEM 规范，来辅助用户在整个网页的 HTML 骨架以及对应的类上进行设计
- 可以引入 CSS Modules，将 CSS 文件进行 “作用域” 限制，确保在之后维护时，修改一个内容不会引起全局中其他样式的效果

BEM 规范

B （Block）、E（Element）、M（Modifier），具体就是通过块、元素、行为来定义所有的可视化功能。

拿设计一个 Button 为例：

```less
/* Block */

.btn {}



/* 依赖于 Block 的 Element */

.btn__price {}



/* 修改 Block 风格的 Modifier */

.btn--orange {}

.btn--big {}
```

遵循上述规范的一个真实的 Button：

```less
<a class="btn btn--big btn--orange" href="#">

  <span class="btn__price">$3</span>

  <span class="btn__text">BIG BUTTON</span>

</a>
```

可以获得如下的效果：

![css03](html&css.assets/css03.webp)

##### CSS Modules

CSS Modules 主要为 CSS 添加局部作用域和模块依赖，使得 CSS 也能具有组件化。

一个例子如下：

```less
import React from 'react';

import style from './App.css';



export default () => {

  return (

    <h1 className={style.title}>

      Hello World

    </h1>

  );

};
.title {

  composes: className;

  color: red;

}
```

上述经过编译会变成如下 hash 字符串：

```less
<h1 class="_3zyde4l1yATCOkgn-DBWEL">

  Hello World

</h1>
._3zyde4l1yATCOkgn-DBWEL {

  color: red;

}
```

CSS Modules 可以与普通 CSS、Less、Sass 等结合使用。

### 纯 JS 侧方案

#### 介绍与优点

![lessgit02](html&css.assets/lessgit02.webp)

> 维护状态：一般

> Star 数：35.2K

> 支持框架：React ，通过社区支持 Vue 等框架

> 项目地址：https://github.com/styled-components/styled-components

使用 JS 的模板字符串函数，在 JS 里面写 CSS 代码，这带来了两个认知的改变：

- 不是在根据 HTML，然后去写 CSS，而是站在组件设计的角度，为组件写 CSS，然后应用组件的组合思想搭建大应用
- 自动提供类似 CSS Modules 的体验，不用担心样式的全局污染问题

同时带来了很多 JS 侧才有的各种功能特性，可以让开发者用开发 JS 的方式开发 CSS，如编辑器自动补全、Lint、编译压缩等。

比如我写一个按钮：

```react
const Button = styled.button`

  /* Adapt the colors based on primary prop */

  background: ${props => props.primary ? "palevioletred" : "white"};

  color: ${props => props.primary ? "white" : "palevioletred"};



  font-size: 1em;

  margin: 1em;

  padding: 0.25em 1em;

  border: 2px solid palevioletred;

  border-radius: 3px;

`;



render(

  <div>

    <Button>Normal</Button>

    <Button primary>Primary</Button>

  </div>

);
```

可以获得如下效果：

![图片](html&css.assets/640-16406007345883)

还可以扩展样式：

```react
// The Button from the last section without the interpolations

const Button = styled.button`

  color: palevioletred;

  font-size: 1em;

  margin: 1em;

  padding: 0.25em 1em;

  border: 2px solid palevioletred;

  border-radius: 3px;

`;



// A new component based on Button, but with some override styles

const TomatoButton = styled(Button)`

  color: tomato;

  border-color: tomato;

`;



render(

  <div>

    <Button>Normal Button</Button>

    <TomatoButton>Tomato Button</TomatoButton>

  </div>

);
```

可以获得如下效果：

![button02](html&css.assets/button02.webp)

#### 不足

虽然这类方案提供了在 JS 中写 CSS，充分利用 JS 的插值、组合等特性，然后应用 React 组件等组合思想，将组件与 CSS 进行细粒度绑定，让 CSS 跟随着组件一同进行组件化开发，同时提供和组件类似的模块化特性，相比 Less/Sass 这一套，可以复用 JS 社区的最佳实践等。

但是它仍然有一些不足：

- 仍然是是对 CSS 增强，提供非常大的灵活性，开发者仍然需要考虑如何去组织自己的 CSS
- 没有给出一套 “有观点” 的最佳实践做法
- 在上层也缺乏基于 styled-components 进行复用的物料库可进行参考设计和使用，导致在初始化使用时开发速度较低
- 在 JS 中写 CSS，势必带来一些本属于 JS 的限制，如 TS 下，需要对 Styled 的组件进行类型注释
- 官方维护的内容只兼容 React 框架，Vue 和其他框架都由社区提供支持

整体来说不太符合团队协作使用，需要人为总结最佳实践和规范等。

#### 优化

- 寻求一套写 CSS 的最佳实践和团队协作规范
- 能够拥有大量的物料库或辅助类等，提高开发效率，快速完成应用开发

### 偏向 HTML 侧方案

#### 介绍与优点

![git03](html&css.assets/git03.webp)

> 维护状态：积极

> Star 数：48.9K

> 支持框架：React、Vue、Svelte 等主流框架

> 项目地址：https://github.com/tailwindlabs/tailwindcss

典型的是 TailwindCSS，一个辅助类优先的 CSS 框架，提供如 `flex` 、`pt-4` 、`text-center` 、`rotate-90` 这样实用的类名，然后基于这些底层的辅助类向上组合构建任何网站，而且只需要专注于为 HTML 设置类名即可。

一个比较形象的例子可以参考如下代码：

```vue
<button class="btn btn--secondary">Decline</button>

<button class="btn btn--primary">Accept</button>
```

上述代码应用 BEM 风格的类名设计，然后设计两个按钮，而这两个类名类似主流组件库里面的 Button 的不同状态的设计，而这两个类又是由更加基础的 TailwindCSS 辅助类组成：

```css
.btn {

  @apply text-base font-medium rounded-lg p-3;

}



.btn--primary {

  @apply bg-rose-500 text-white;

}



.btn--secondary {

  @apply bg-gray-100 text-black;

}
```

上面的辅助类包含以下几类：

- 设置文本相关：`text-base` 、`font-medium` 、`text-white` 、`text-black`
- 设置背景相关的：`bg-rose-500` 、`bg-gray-100`
- 设置间距相关的：`p-3`
- 设置边角相关的：`rounded-lg`

通过 Tailwind 提供的 `@apply` 方法来对这些辅助类进行组合构建更上层的样式类。

上述的最终效果展示如下：

![css04](html&css.assets/css04.webp)

可以看到 TailwindCSS 将我们开发网站的过程抽象成为使用 Figma 等设计软件设计界面的过程，同时提供了一套用于设计的规范，相当于内置最佳实践，如颜色、阴影、字体相关的内容，一个很形象的图片可以说明这一点：

![css05](html&css.assets/css05.webp)

TailwindCSS 为我们规划了一个元素可以设置的属性，并且为每个属性给定了一组可以设置的值，这些属性+属性值组合成一个有机的设计系统，非常便于团队协作与共识，让我们开发网站就像做设计一样简单、快速，但是整体风格又能保持一致。

TailwindCSS 同时也能与主流组件库如 React、Vue、Svelte 结合，融入基于组件的 CSS 设计思想，但又只需要修改 HTML 上的类名，如我们设计一个食谱组件：

```vue
// Recipes.js

import Nav from './Nav.js'

import NavItem from './NavItem.js'

import List from './List.js'

import ListItem from './ListItem.js'



export default function Recipes({ recipes }) {

  return (

    <div className="divide-y divide-gray-100">

      <Nav>

        <NavItem href="/featured" isActive>Featured</NavItem>

        <NavItem href="/popular">Popular</NavItem>

        <NavItem href="/recent">Recent</NavItem>

      </Nav>

      <List>

        {recipes.map((recipe) => (

          <ListItem key={recipe.id} recipe={recipe} />

        ))}

      </List>

    </div>

  )

}



// Nav.js

export default function Nav({ children }) {

  return (

    <nav className="p-4">

      <ul className="flex space-x-2">

        {children}

      </ul>

    </nav>

  )

}



// NavItem.js

export default function NavItem({ href, isActive, children }) {

  return (

    <li>

      <a

        href={href}

        className={`block px-4 py-2 rounded-md ${isActive ? 'bg-amber-100 text-amber-700' : ''}`}

      >

        {children}

      </a>

    </li>

  )

}



// List.js

export default function List({ children }) {

  return (

    <ul className="divide-y divide-gray-100">

      {children}

    </ul>

  )

}



//ListItem.js

export default function ListItem({ recipe }) {

  return (

    <article className="p-4 flex space-x-4">

      <img src={recipe.image} alt="" className="flex-none w-18 h-18 rounded-lg object-cover bg-gray-100" width="144" height="144" />

      <div className="min-w-0 relative flex-auto sm:pr-20 lg:pr-0 xl:pr-20">

        <h2 className="text-lg font-semibold text-black mb-0.5">

          {recipe.title}

        </h2>

        <dl className="flex flex-wrap text-sm font-medium whitespace-pre">

          <div>

            <dt className="sr-only">Time</dt>

            <dd>

              <abbr title={`${recipe.time} minutes`}>{recipe.time}m</abbr>

            </dd>

          </div>

          <div>

            <dt className="sr-only">Difficulty</dt>

            <dd> · {recipe.difficulty}</dd>

          </div>

          <div>

            <dt className="sr-only">Servings</dt>

            <dd> · {recipe.servings} servings</dd>

          </div>

          <div className="flex-none w-full mt-0.5 font-normal">

            <dt className="inline">By</dt>{' '}

            <dd className="inline text-black">{recipe.author}</dd>

          </div>

          <div class="absolute top-0 right-0 rounded-full bg-amber-50 text-amber-900 px-2 py-0.5 hidden sm:flex lg:hidden xl:flex items-center space-x-1">

            <dt className="text-amber-500">

              <span className="sr-only">Rating</span>

              <svg width="16" height="20" fill="currentColor">

                <path d="M7.05 3.691c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.372 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.539 1.118l-2.8-2.034a1 1 0 00-1.176 0l-2.8 2.034c-.783.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.363-1.118L.98 9.483c-.784-.57-.381-1.81.587-1.81H5.03a1 1 0 00.95-.69L7.05 3.69z" />

              </svg>

            </dt>

            <dd>{recipe.rating}</dd>

          </div>

        </dl>

      </div>

    </article>

  )

}
```

上述食谱的效果如下：

![button03](html&css.assets/button03.webp)

可以看到我们无需写一行 CSS，而是在 HTML 里面应用各种辅助类，结合 React 的组件化设计，既可以轻松完成一个非常现代化且好看的食谱组件。

除了上面的特性，TailwindCSS 在响应式、新特性支持、Dark Mode、自定义配置、自定义新的辅助类、IDE 方面也提供非常优秀的支持，除此之外还有基于 TailwindCSS 构建的物料库 Tailwind UI ，提供各种各样成熟、好看、可用于生产的物料库：

![UI](html&css.assets/UI.webp)

因为需要自定的 CSS 不多，而需要自定义的 CSS 可以定义为可复用的辅助类，所以在可维护性方面也是极好的。

#### 不足

- 因为要引入一个额外的运行时，TailwindCSS 辅助类到 CSS 的编译过程，而随着组件越来越多，需要编译的工作量也会变大，所以速度会有影响
- 过于底层，相当于给了用于设计的最基础的指标，但是如果我们想要快速设计网站，那么可能还需要一致的、更加上层的组件库
- 相当于引入了一套框架，具有一定的学习成本和使用成本

#### 优化

- Tailwind 2.0 支持 **JIT**[1]，可以大大提升编译速度，可以考虑引入
- 基于 TailwindCSS，设计一套符合自身风格的上层组件库、物料库，便于更加快速开发
- 提前探索、学习和总结一套教程与开发最佳实践
- 探索 styled-components 等结合 TailwindCSS 的开发方式

# 文档流（normal flow）

- 文档流

  - 网页是一个多层结构，一层摞着一层

  - 通过css可以为每一层设置样式

  - 作为用户只能看到最顶上的一层

  - 这些层中，最底下的一层称为文档流，文档流是网页的基础
    - 我们所创建的元素默认都是在文档流中进行排列


- 对于元素主要有连个状态：
  - 在文档流中
  - 不在文档流中（脱离文档流）

## 块元素与行内元素


- 元素在文档流中有什么特点：
  - 块元素
    - 块元素会在页面上独占一行（自上向下垂直排列）
    - 默认宽度是父元素的全部（会把父元素撑满）
    - 默认高度是被内容撑开（子元素）
    - 块级元素占据其父元素（容器）的整个水平空间，垂直空间等于其内容高度，因此创建了一个“块”。

  - 行内元素
    - 行内元素不会独占页面的一行，只占自身的大小
    - 行内元素在页面中，自左向右水平排列，如果一行中不能容下所有的行内元素，则元素会换到第二行继续自左向右排列（书写习惯一致）
    - 行内元素的默认宽度和高度都是被内容撑开
    - 一个行内元素只占据它对应标签的边框所包含的空间。

  - 块级元素与行内元素有几个关键区别：

    - 格式
      - 默认情况下，块级元素会新起一行。

    - 内容模型
      - 一般块级元素可以包含行内元素和其他块级元素。这种结构上的包含继承区别可以使块级元素创建比行内元素更”大型“的结构。

## 盒子模型

### 概述

当对一个文档进行布局（lay out）的时候，浏览器的渲染引擎会根据标准之一的 **CSS 基础框盒模型**（**CSS basic box model**），将所有元素表示为一个个矩形的盒子（box）。CSS 决定这些盒子的大小、位置以及属性（例如颜色、背景、边框尺寸…）。

每个盒子由四个部分（或称*区域*）组成，其效用由它们各自的边界（Edge）所定义（原文：defined by their respective edges，可能意指容纳、包含、限制等）。如图，与盒子的四个组成区域相对应，每个盒子有四个边界：*内容边界* *Content edge*、*内边距边界* *Padding Edge*、*边框边界* *Border Edge*、*外边框边界* *Margin Edge*。

![CSS Box model](html&css.assets/boxmodel-(3).png)

**内容区域 content area** ，由内容边界限制，容纳着元素的“真实”内容，例如文本、图像，或是一个视频播放器。它的尺寸为内容宽度（或称 *content-box 宽度*）和内容高度（或称 *content-box 高度*）。它通常含有一个背景颜色（默认颜色为透明）或背景图像。

如果 [`box-sizing`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/box-sizing) 为 `content-box`（默认），则内容区域的大小可明确地通过 [`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width)、[`min-width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/min-width)、[`max-width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/max-width)、[`height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/height)、[`min-height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/min-height)，和 [`max-height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/max-height) 控制。

**内边距区域 padding area** 由内边距边界限制，扩展自内容区域，负责延伸内容区域的背景，填充元素中内容与边框的间距。它的尺寸是 *padding-box 宽度* 和 *padding-box 高度*。

内边距的粗细可以由 [`padding-top`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding-top)、[`padding-right`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding-right)、[`padding-bottom`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding-bottom)、[`padding-left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding-left)，和简写属性 [`padding`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding) 控制。

**边框区域 border area** 由边框边界限制，扩展自内边距区域，是容纳边框的区域。其尺寸为 *border-box 宽度* 和 *border-box 高度*。

边框的粗细由 [`border-width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-width) 和简写的 [`border`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border) 属性控制。如果 [`box-sizing`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/box-sizing) 属性被设为 `border-box`，那么边框区域的大小可明确地通过 [`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width)、[`min-width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/min-width), [`max-width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/max-width)、[`height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/height)、[`min-height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/min-height)，和 [`max-height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/max-height) 属性控制。假如框盒上设有背景（[`background-color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-color) 或 [`background-image`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-image)），背景将会一直延伸至边框的外沿（默认为在边框下层延伸，边框会盖在背景上）。此默认表现可通过 CSS 属性 [`background-clip`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-clip) 来改变。

**外边距区域 margin area** 由外边距边界限制，用空白区域扩展边框区域，以分开相邻的元素。它的尺寸为 *margin-box 宽度* 和 *margin-box 高度*。

外边距区域的大小由 [`margin-top`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin-top)、[`margin-right`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin-right)、[`margin-bottom`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin-bottom)、[`margin-left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin-left)，和简写属性 [`margin`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin) 控制。在发生[外边距合并](https://developer.mozilla.org/en-US/CSS/margin_collapsing)的情况下，由于盒之间共享外边距，外边距不容易弄清楚。

最后，请注意，除[可替换元素](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Replaced_element)外，对于行内元素来说，尽管内容周围存在内边距与边框，但其占用空间（每一行文字的高度）则由 [`line-height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/line-height) 属性决定，即使边框和内边距仍会显示在内容周围。





- 内容区(content)，元素中的所有子元素和文本内容都是在内容区中排列
  - 内容区的大小，由width和height两个属性来设置
- 边框(border)，边框属于盒子边缘，出了盒子都是盒子的外部
  - 边框的大小会影响到整个盒子的大小
    - 要设置边框，至少要设置三个样式：`border-width`、`border-color`、`border-style	`
- 盒子模型、盒模型、框模型(box-model)
  - css将页面中的所有元素设置为了一个矩形的盒子
  - 每一个盒子都有以下几个组成部分
    - 内容区(content)
    - 内边距(padding)
    - 边框(border)
    - 外边距(margin)

### 盒子模型-边框

边框

- 边框的宽度：`border-width`
  - 默认值，一般都是3个像素
  - 可以用来指定4个方向的边框的宽度
    - 四个值：上 右 下 左
    - 三个值：上 左右 下
    - 两个值：上下 左右
    - 一个值：上下左右
  - border-xxx-width
    - xxx可以是：top right bottom left
- 边框的颜色：`border-color`
  - 用来指定边框的颜色，同样可以分别指定四个边的边框颜色，使用方式同上
- 边框的样式：`border-style`
  - solid 表示实线
  - dotted 表示虚线
  - dashed 虚线
  - double 双线
  - 可以分别指定四个边的边框样式，使用方式同上
- 合并的 写法
  - `border:1px solid red`

### 盒子模型-内边距

盒子模型图示：

![image-20211121065016351](html&css.assets/image-20211121065016351.png)

内边距：内容区和边框之间的距高

一共有4个方向的内边距：

- padding-top
- padding-right
- padding-bottom
- padding-left

内边距的设置，会影响盒子的大小

背景颜色，会延伸到内边距

盒子可见框的大小，有内容区、内边距和边框共同决定，计算的时候要一起计算

### 盒子模型-外边距

外边距不会影响盒子可见框的大小，但是外边距会影响盒子的位置

一共有四个方向的外边距

- margin-top：上外边距，设置一个正直，元素会向下移动
- margin-right：右外边距，默认情况下，设置margin-right不会产生任何效果
- margin-left：左外边距，设置一个正直，元素会向右移动
- margin-bottom：下外边距，设置一个正直，它下边的元素，会向下移动

元素在页面中，自动排列的顺序是从左到右，所以默认情况下，如果我们设置的是，左外边距和上外边距，会移动元素自身，而设置右外边距和下外边距，元素不会移动

margin也可以设置负值，此时元素会向相反的方向移动

margin的简写属性：

同时设置4个方向的margin值

```css
margin:100px;
```

margin虽然不会影响盒子的可见大小，但是会影响实际的大小（实际占用网页空间的大小）

### 盒子模型-水平方向的布局

元素的水平方向的布局

元素在其父元素中水平方向的位置，由以下几个属性共同决定：

- margin-left
- border-left
- padding-left
- width
- padding-right
- border-right
- margin-right

一个元素在器父元素中，水平布局必须要满足以下等式

margin-left + border-left + padding-left + width + padding-right + border-right + margin-right = 其父元素内容区的宽度（必须满足）

如下实例

html

```html
<div class="outer">
    <div class="inner">
        
    </div>
</div>
```

css

```css
.outer {
    width: 800px;
    height: 200px;
    border: 1px solid red;
}

.inner {
    width: 200px;
    height:200px;
    background-color: #bfa;
}
```

等式如下：

```
0 + 0 + 0 + 200 + 0 + 0 + 600 = 800
```

以上等式必须满足，如果相加结果使得等式不成立，则称为过渡约束，则等式会自动调整

inner中的调整情况：

- 如果这七个值没有为auto的情况，则浏览器会自动调整margin-right的值，以使等式满足（如上的例子）

- 如果某个值为auto，则会自动调整为auto的那个值，以使等式成立

  - width是auto的一员，且只有width设置了，其他属性未设置：width会直接调整到最大

    - 如果将一个宽度和一个外边距都设置为auto，宽度会调整到最大，设置为auto的外边距默认为0
    - 如果将一个宽度和两个外边距都设置为auto，宽度会调整到最大，设置为auto的外边距默认为0

  - width为auto，margin-right设置为200px，其他属性未设置：width会自动调整为600px（800 - 200）

  - width为auto，margin-right和margin-left分别都设置为200px，其他属性为设置：width会自动调整为400px

  - width的值默认就是auto

    - 块元素中，子元素的宽度时父元素的100%，这个100%其实不是值，值是auto

  - width是固定值

    - 如果两个外边距都是auto，则外边距的值会平分

      ```css
      //根据以上原理，设置水平居中
      .inner {
          width:100px;
          margin:0 auto;
      }
      ```

- 如果宽度设置为1000px，则会自动调整margin-right的值为-200px

### 盒子模型-垂直方向的布局

1.父元素不设置高度，默认情况下，高度被子元素撑开；
2.子元素超过父元素高度，子元素从父元素中溢出；

- 可以使用overflow属性，来设置父元素如何处理溢出的子元素
- 可选值：
  - visible：默认值 子元素会从父元素溢出，在父元素外部显示
  - hidden：溢出内容被裁剪不显示
  - scroll：生成两个滚动条，查看完整的内容
    - auto 根据需要生成

```css
.outer{	
    width:200px;	
    height:200px;
}
.inner{	
    width:200px;	
    height:400px;
}
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210131081821683.png)
使用overflow在父元素中处理溢出；

```css
.outer{	
    width:200px;	
    height:200px;	
    overflow:visible;
    /*visible hidden scroll auto*/	
    /*overflow-x overflow-y*/
}
.inner{	
    width:200px;	
    height:400px;
}
```

### 盒子模型-外边距的折叠

#### 外边距折叠现象

html

```html
<body>
    <div class="box1"></div>
    <div class="box2"></div>
</body>
```

css

```css
    <style>
        .box1, .box2 {
            width: 200px;
            height: 200px;

        }
        .box1 {
            background-color: #bfa;
        /*    设置一个下外边距*/
            margin-bottom: 100px;
        }
        .box2 {
            background-color: orange;
        /*    设置一个上外边距*/
            margin-top: 100px;
        }

    </style>
```

![image-20211121092502370](html&css.assets/image-20211121092502370.png)

相邻的、垂直外边距会发生重叠现象
1.相邻（挨着）
2.垂直（margin-bottom  margin-top）

##### 兄弟元素

- 两者都是正值，取较大值；
- 一正一负，取两者和；
- 两者都是负值，取绝对值较大值；

兄弟元素之间的外边距折叠，对于开发是有利的，不需要处理；

##### 父子元素

父子元素间的相邻（上）外边距，子元素会传递给父元素；
现象：给子元素设置一个上外边距后，父元素被挤下来了；

html

```html
<body>
<div class="box1">
    <div class="box2"></div>
</div>

</body>
```

css

```css
    <style>
        .box1 {
            width: 200px;
            height: 200px;

        }
        .box2 {
            width: 100px;
            height: 100px;
        }
        .box1 {
            background-color: #bfa;

        }

        .box2 {
            background-color: orange;
            /*    设置一个上外边距*/
            margin-top: 100px;
        }


    </style>
```

现象：父子元素的上外边距，子元素会传递给父元素，所以上图中，父元素也会有一个上外边距



![image-20211121093207101](html&css.assets/image-20211121093207101.png)

#### 外边距折叠的处理

父子元素的外边距折叠，会影响到页面的布局，必须进行处理

##### 处理方式一

计算一下，不用子元素的margin-top，用padding-top;

##### 处理方式二

用border-top，使父子元素不相邻；

##### 处理方式三

使用伪元素

## 行内元素的盒模型

- 行内元素不支持设置宽度和高度
- 行内元素可以设置padding、border、margin
  - 垂直方向不会影响元素的布局

### display

用来设置元素显示的类型

- inline：行内元素；
- block ：块元素；
- inline-block：行内块元素；
  - 既可以设置宽高，也不会独占一行；
- table：表格；
- none：隐藏一个元素； 

### visibility

- visible：默认值，正常显示；
- hidden：隐藏不显示，但依然占据页面的位置； 

## 盒子的大小

默认情况下，盒子可见框的大小，由内容区、内边距和边框共同决定

box-sizing：用来设置盒子尺寸的计算方式

可选值：

- content-box：默认值，宽度和高度设置内容区的大小
- border-box：高度和宽度用来设置整个盒子的大小，width和height指的是内容区和内边距和边框的大小

## 轮廓、阴影和圆角

- box-shadow：用来设置元素的阴影效果，阴影不会影响页面布局

  - 第一个值：水平偏移量
  - 第二个值：垂直偏移量
  - 第三个值：模糊半径
  - 第四个值：阴影颜色

- outline：用来设置元素的轮廓线，用法和border一样

  - 轮廓和边框不同的是，轮廓不会影响到可见框的大小

- border-radius：用来同时设置4个方向的圆角

  - 设置：

    - 四个值：左上 右上 右下 左下
    - 三个值：左上 右上/左下 右下
    - 两个值：左上/右下 右上/左上

  - border-xxx-yyy-radius：xxx的取值为top/bottom，yyy的取值为left/right

    - 可以设置两个值

  - 将元素设置为圆形

    ```css
    border-radius: 50%
    ```

# 布局

## Flex布局

flex（弹性盒）是CSS中的一种布局手段，它主要用来代替浮动来完成页面的布局

flex可以让元素具有弹性，让元素跟随页面的大小而改变

#### 弹性容器

```
要使用弹性盒，必须先将一个元素设置为弹性容器

我们通过`display`来设置弹性容器
    display: flex // 设置为块级弹性容器
    display: inline flex //设置为行内的弹性容器
```

#### 弹性元素

```
弹性容器的子元素是弹性元素（弹性项）
一个元素可以同时是弹性容器和弹性元素
```

### 弹性容器的样式

#### `flex-direction`

| 可选值         | 作用                     | 主轴     |
| -------------- | ------------------------ | -------- |
| row（默认值）  | 弹性元素在容器中水平排列 | 自左向右 |
| row-reverse    | 弹性元素在容器中水平排列 | 自右向左 |
| column         | 弹性元素在容器中纵向排列 | 自上而下 |
| column-reverse | 弹性元素在容器中纵向排列 | 自下而上 |



`主轴`：弹性元素的排列方向称为主轴 `辅轴`：与主轴垂直的轴称为辅轴

#### `flex-wrap`

| 可选值       | 作用                   |
| ------------ | ---------------------- |
| nowrap       | 默认值，元素不换行     |
| wrap         | 设置弹性元素自动换行   |
| wrap-reverse | 元素沿辅轴方向反向换行 |



#### `flex-flow`

direction和wrap的简写属性

#### `justify-content`

如何分配主轴上的空白空间（主轴上的元素如何排列）

只要是justify开头的，描述的都是主轴上的属性

| 值            | 解释                                                         |
| ------------- | ------------------------------------------------------------ |
| flex-start    | 子元素沿着主轴的起边排列，如果有空白，则会在每一行的最右侧，主轴是从左往右的，起边就在最左侧那一列 |
| flex-end      | 子元素沿着主轴的终边排列，如果有空白，则会在每一行的最左侧，主轴是从左往右的，终边就在最右侧那一列 |
| center        | 子元素居中排列，如果有空白，会全部分布在两边                 |
| space-around  | 如果有空白，会平均分布在子元素左右两侧                       |
| space-evenly  | 如果有空白，则会均匀分配在元素左右两边                       |
| space-between | 如果有空白，均匀分布在子元素中间，左右两边不会留有空白       |



#### `align-items`：

#### 当有两行以上的元素时，控制元素在辅轴上如何对齐

只要是align开头的，描述的都是辅轴上的属性

| 值         | 解释                                                         |
| ---------- | ------------------------------------------------------------ |
| stretch    | 默认值，将同一行的子元素的长度设置为相同值，确保在同一条水平线上 |
| flex-start | 元素不会拉伸，不同行都会沿着各自辅轴起边对齐                 |
| flex-end   | 元素不会拉伸，不同行都会沿着各自辅轴终边对齐                 |
| center     | 元素不会拉伸，在所在行居中对齐                               |
| baseline   | 元素不会拉伸，沿着基线对齐                                   |



#### `align-content`

当有两行以上的元素时，控制辅轴空白空间的分布

| 值            | 解释                                                   |
| ------------- | ------------------------------------------------------ |
| flex-start    | 元素沿着辅轴的起边排列，空白在下面                     |
| flex-end      | 元素沿着辅轴的终边排列，空白在上面                     |
| center        | 让上下的空白相等，元素在中间                           |
| space-around  | 如果有空白，会平均分布在子元素上下两侧                 |
| space-evenly  | 如果有空白，则会均匀分配在元素上下两边                 |
| space-between | 如果有空白，均匀分布在子元素中间，上下两边不会留有空白 |



#### 水平垂直居中

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <style>
            .box1{
                width: 500px;
                height: 500px;
                border: 1px solid red;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .box2{
                width:50px;
                height: 50px;
                background-color: #1BC4FB;
            }
        </style>
    </head>
    <body>
        <div class="box1">
            <div class="box2"></div>
        </div>
    </body>
</html>
```

### 弹性元素的样式

#### `align-self`

用来覆盖当前弹性元素上的`align-items`

#### `flex-grow`

指定弹性元素的伸展系数,弹性元素的默认值是flex-grow:0

```
当父元素有多余空间时，子元素如何伸展
    可以直接给每个子元素设置flex-grow:1，即按相同比例分配子元素长度
    也可以给各子元素设置不同的flex-grow值:
        将以父元素的总长度为基准，按给定比例分配各子元素长度
        flex-grow值越大，子元素长度就越长
```

#### `flex-shrink`

指定弹性元素的伸缩系数，弹性元素的默认值是flex-shrink:1

```
当父元素空间不足以容纳所有的子元素时，如何对子元素进行收缩
    若设置flex-shink:0；则不会进行收缩
        此时可以给弹性容器设置flex-wrap:wrap;设置弹性元素自动换行
    也可以给各子元素设置不同的flex-shrink值:
        将以父元素的总长度为基准，按给定比例分配各子元素长度
        flex-shrink值越大，缩小的长度就越多
```

#### `flex-basis`

元素的基础长度

```
指定的是元素在主轴上的基础长度
    如果主轴是横向的，则该值指定的是元素的宽度
    如果主轴是纵向的，则该值指定的是元素的高度
```

| 值     | 解释                                   |
| ------ | -------------------------------------- |
| auto   | 默认值，表示参考元素自身的宽度或者高度 |
| 具体值 | 如果传递了一个值，则以该值为准         |



#### `flex`

简写属性：`flex: 1 1 auto`，分别对应增长系数、缩减系数、基础长度，顺序不能错

| 值     | 增长系数 | 缩减系数 | 基础长度 |
| ------ | -------- | -------- | -------- |
| inital | 0        | 1        | auto     |
| auto   | 1        | 1        | auto     |
| none   | 0        | 0        | auto     |



#### `order`

影响元素的排列顺序，最小的值排在最前面

## Grid布局

视频教程：[css grid布局，手把手教你grid布局，包你学会，史上最全面详细的课程_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Bk4y197xm)

对应笔记：[ 图解CSS布局（一）- Grid布局_小丞同学-CSDN博客_css grid布局](https://blog.csdn.net/m0_50855872/article/details/116571697)

### Grid布局简介

![image-20211229211217206](html&css.assets/image-20211229211217206.png)



![image-20211229211239491](html&css.assets/image-20211229211239491.png)



![image-20211229211432115](html&css.assets/image-20211229211432115.png)

![image-20211229211405923](html&css.assets/image-20211229211405923.png)

![image-20211229211516304](html&css.assets/image-20211229211516304.png)

![image-20211229211729362](html&css.assets/image-20211229211729362.png)

### 容器属性

![image-20211229211834442](html&css.assets/image-20211229211834442.png)

![image-20211229211912760](html&css.assets/image-20211229211912760.png)

![image-20211229212539887](html&css.assets/image-20211229212539887.png)

![image-20211229212634270](html&css.assets/image-20211229212634270.png)

![image-20211229212746534](html&css.assets/image-20211229212746534.png)

![image-20211229212930365](html&css.assets/image-20211229212930365.png)

![image-20211229213039867](html&css.assets/image-20211229213039867.png)

![image-20211229213129020](html&css.assets/image-20211229213129020.png)

![image-20211229213345726](html&css.assets/image-20211229213345726.png)



![image-20211229213510828](html&css.assets/image-20211229213510828.png)

![image-20211229214610877](html&css.assets/image-20211229214610877.png)

![image-20211229214623718](html&css.assets/image-20211229214623718.png)





![image-20211229215230459](html&css.assets/image-20211229215230459.png)

![image-20211229215549466](html&css.assets/image-20211229215549466.png)



![image-20211229215615298](html&css.assets/image-20211229215615298.png)

![image-20211229220011440](html&css.assets/image-20211229220011440.png)

![image-20211229220110375](html&css.assets/image-20211229220110375.png)

![image-20211229220310990](html&css.assets/image-20211229220310990.png)



![image-20211229220324191](html&css.assets/image-20211229220324191.png)

![image-20211229220703269](html&css.assets/image-20211229220703269.png)

![image-20211229220813151](html&css.assets/image-20211229220813151.png)

![image-20211229220900615](html&css.assets/image-20211229220900615.png)

![image-20211229221058243](html&css.assets/image-20211229221058243.png)

![image-20211229221218092](html&css.assets/image-20211229221218092.png)

![image-20211229221310218](html&css.assets/image-20211229221310218.png)





# 字体介绍 

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206191407492.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

## 引入自定义字体

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206191723870.png)

```html
<!DOCTYPE html><html>	<head>		<meta charset="utf-8">		<title></title>		<style type="text/css">			@font-face {				font-family:myfont;				src: url(FZPTYJW.TTF) format("truetype");			}			p{				color: red;				font-size: 40px;				font-family: "myfont";			}		</style>	</head>	<body>		<p>今天天气不错，hello</p>	</body></html>
```

## 图标字体

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206195718297.png)

### fontawesome使用步骤

![在这里插入图片描述](https://img-blog.csdnimg.cn/2021020620043628.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### 通过伪元素来设置图标字体

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206201621163.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### iconfont使用步骤

[https://www.iconfont.cn/](https://www.iconfont.cn/)

[资源链接](https://www.iconfont.cn/collections/detail?spm=a313x.7781069.1998910419.dc64b3430&cid=29085)

![在这里插入图片描述](html&css.assets/20210206204053428.png)



添加到项目后，选择“下载至本地”

```html
<!DOCTYPE html><html lang="zh"><head>	
    <meta charset="UTF-8">	
    <meta name="viewport" content="width=device-width, initial-scale=1.0">	
    <meta http-equiv="X-UA-Compatible" content="ie=edge">	
    <title></title>	
    <link rel="stylesheet" type="text/css" href="iconfont.css"/>	
    <style type="text/css">		
        .iconfont{			
            font-size: 40px;			
            color: red;		
        }		
        p::before{			
            content: '\e7be';			
            font-family: 'iconfont';			
            font-size: 50px;		
        }		
        .icon-xianxingtanghulu{			
            font-size: 60px;		
        }	
    </style>
    </head>
    <body>	
        <span class="iconfont">&#xe7bd;</span>	
        <p class="iconfont">hello</p>	
        <i class="iconfont icon-xianxingtanghulu"></i>
    </body>
</html>
```

### vue3中使用element plus

直接安装的，没指定版本，

```
    "@element-plus/icons": "0.0.11",
    "element-plus": "^1.2.0-beta.3",
    "vue": "^3.0.0",
```

>1.main.js中导入，并挂载
>
>2.在需要使用的组件中，挂载对应的组件，具体使用哪个图标，

1.main.js中导入，并挂载

main.js

```javascript
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/css/global.css'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

createApp(App).use(store).use(router).use(ElementPlus).mount('#app')

```



## 字体相关样式

### 行高介绍

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206204553921.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### 简写属性

```css
font: bold italic 50px/2 微软雅黑, 'Times New Roman', Times, serif;//不写不等于没有，浏览器会自动渲染默认值；
```

## 文本相关样式

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206205150357.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206205636486.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

## 其他文本样式

### textdecoration

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206210156230.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### white-space

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206210625684.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206210615303.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)



# 表格与表单

# 过渡、动画和变行属性

## `transition`过渡属性

- 通过过渡可以指定一个属性发生变化时的切换方式

- 通过过渡可以创建一些非常好的效果，提升用户体验

  - `transition-property`：指定要执行过渡的属性

    - 多个属性使用逗号隔开
    - 如果所有属性都需要过渡，则使用all关键字
    - 大部分属性都支持过渡效果，注意过度时，必须是从一个有效数值，向另一个有效数值进行过渡

  - `transition-duration`：指定过渡效果的持续时间

    - 时间单位：s和ms

  - `transition-timing-function`：指定过渡的时序函数

  - 可选值：

    - `ease`：默认值，慢速开始，先加速再减速

    - `linear`：匀速运动

    - `ease-in`：加速运动

    - `ease-out`：减速运动

    - `ease-in-out`：先加速后减速

    - `cubic-bezier()`：来指定时序函数

      - https://cubic-bezier.com 本质是贝塞尔曲线

        ![image-20211229195434815](html&css.assets/image-20211229195434815.png)

    - steps()：分步骤执行过渡效果

      - steps(2)：分两步
      - steps(2, end)：在`transition-duration`的时间结束时执行过渡（默认值）
      - steps(2, start)：在`transition-duration`的时间开始时执行过渡

  - transition：可以同时设置过渡相关的所有属性，只有一个要求，如果要写延迟，则两个时间中第一个是持续时间

    - `transition: 2s margin-left 1s`

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title></title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .box1 {
            width: 400px;
            height: 400px;
            background-color: #BBFFAA;
        }

        .box1 div {
            width: 50px;
            height: 50px;
        }

        .box2 {
            background-color: skyblue;
            /* transition-property: width,height; */
            transition-property: all;
            transition-duration: 2s;
            /* transition-timing-function: ease; */
            transition-timing-function: steps(2, starts);
        }

        .box3 {
            background-color: orange;
            transition-property: all;
            transition-duration: 2s;
            transition-timing-function: cubic-bezier(.19, 1.24, .82, -0.58);
        }

        .box1:hover div {
            /* width: 100px;				height: 100px; */
            margin-left: 350px;
        }
    </style>
</head>

<body>
    <div class="box1">
        <div class="box2"></div>
        <div class="box3"></div>
    </div>
</body>

</html>
```

### `transition`练习

```html
<!DOCTYPE html>
<html>
 
<head>
    <meta charset="utf-8">
    <title></title>
    <style>
        .box {
            width: 96px;
            height: 194px;
            background-image: url("mitu.png");
            background-position: 0, 0;
            transition: 0.8s steps(4);
        }

        .box:hover {
            background-position: -378px 0;
        }
    </style>
</head>

<body>
    <div class="box"></div>
</body>

</html>
```

## `keyframes`动画属性

动画和过渡类似，都是可以实现一些动态的效果

不同的是过渡需要在某个属性发生变化时才会触发，动画可以自动触发动态效果

设置动画效果，必须先要设置一个关键帧，关键帧设置了动画执行的每一个步骤

```css
@keyframes test {
	/* from表示动画的开始位置，也可以使用0% */
    from {
        magin-left: 0;
    }
	/* to表示动画的结束位置，也可以使用100% */
    to {
        margin-left: 700px;
    }
}

.box2 {
    background-color: #bfa;
    
    /* 设置box2的动画 */
    /* animation-name： 要对当前元素生效的关键帧的名字 */
    animation-name: test;
    
    /* animation-duration： 动画的执行时间 */
    animation-duration: 4s;
    
    /* animation-delay： 动画的延时 */
    animation-delay: 2s;
    
    /* animation-timing-function： 动画的时序函数 */
    animation-timing-function：ease-in-out;
    
    /* animation-iteration-count： 动画执行的次数 */
    animation-iteration-count：infinite;
    
    /* animation-direction： 指定动画运动的方向 
    可选值：
    	normal  默认值  从from向to运行，每次都是这样
    	reverse  从to向from运行，每次都是这样
    	alternate  从from向to运行，重复执行动画时反向执行
    	alternate-reverse
    */
    animation-direction：normal;
    
    /* animation-play-state： 动画的执行状态
    可选值：
    	running  默认值，动画执行
   		paused  动画暂停
    */
    animation-play-state：paused;
    
    /* animation-fill-mode： 动画的填充模式 
    可选值：
    	none  默认值，动画执行完毕后，元素回到原来位置
    	forwards  动画执行完毕，元素会停止在动画结束的位置
    	backwards  动画延时等待时，元素就会处于开始位置
    	both  结合了forwards和backwards
    */
    animation-fill-mode：both;
}
```

对于动画的使用，还可以自定义类名

```css
.come {
    animation: 1s test linear;
}

```

然后在自定元素上添加类名即可

这样写的好处是，对于一个元素，添加不同的类名，可以实现不同动画之前的切换

### `keyframes`练习

#### 奔跑的少年

![在这里插入图片描述](html&css.assets/20210222221120834.png)

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title></title>
    <style>
        .box1 {
            width: 91px;
            height: 91px;
            margin: 0 auto;
            background-image: url(sprite01.png);
            animation: run 1s steps(6) infinite;
        }

        /* 创建关键帧 */
        @keyframes run {
            from {
                background-position: 0, 0;
            }

            to {
                background-position: -551px;
            }
        }
    </style>
</head>

<body>
    <div class="box1"></div>
</body>

</html>
```

![](html&css.assets/run.gif)

#### 小球落下

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title></title>
    <style>
        .box1 {
            height: 500px;
            margin: 50 auto;
            overflow: hidden;
            border-bottom: 10px solid black;
        }

        .box2 {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background-color: #BBFFAA;
            animation: ball 2s forwards ease-in alternate;
        }

        /* 创建小球落下的动画 */
        @keyframes ball {
            from {
                margin-top: 0;
            }

            20%,
            60%,
            to {
                margin-top: 400px;
                animation-timing-function: ease-in;
            }

            40% {
                margin-top: 100px;
            }

            80% {
                margin-top: 200px;
            }
        }
    </style>
</head>

<body>
    <div class="box1">
        <div class="box2"></div>
    </div>
</body>

</html>
```

![](html&css.assets/ball.gif)

## `transform`变形属性

变形就是指通过`CSS`来改变元素的形状或位置

- 变形不会影响到页面的布局

- `transform`用来设置元素的变形效果

  - 平移：
    - `translateX()` 沿着X轴方向平移
    - `translateY()` 沿着Y轴方向平移
    - `translateZ()` 沿着Z轴方向平移

- 利用`transform`，设置水平居中

  ```css
  .box3 {
      background-color: orange;
      position: absolute;
      left: 50%;
      top: 50%;
      transform: translateX(-50%);
  }
  ```

  

### `transform`练习

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title></title>
    <style type="text/css">
        body {
            background-color: #CCCCCC;
        }

        .box1 {
            width: 250px;
            height: 400px;
            background-color: white;
            margin: 20px auto;
            transition: all .3s;
        }

        .box1:hover {
            transform: translate(-2px, -3px);
            box-shadow: 2px 2px 10px rgba(0, 0, 0, .3);
        }
    </style>
</head>

<body>
    <div class="box1"> </div>
</body>

</html>
```

鼠标hover时的效果：

![image-20211230185040274](html&css.assets/image-20211230185040274.png)

### z轴平移

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222224706487.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222224806422.png)

### 旋转介绍

```html
<!DOCTYPE html><html>	<head>		<meta charset="utf-8">		<title></title>		<style type="text/css">			html{				/* perspective: 800px; */			}			body{				border:1px solid red;			}			.box1{				width: 200px;				height: 200px;				background-color: #BBFFAA;				margin: 50px auto;				transition: 2s;			}			body:hover .box1{				/* transform: rotateY(180deg) translateY(100px); */				transform: rotateY(180deg);				/* 是否显示元素的背面 */				backface-visibility: hidden;			}		</style>	</head>	<body>		<div class="box1">			<img src="./54.布局作业/01/img/0102.webp" >		</div>	</body></html>
```

#### 旋转练习--钟表

```html
<!DOCTYPE html><html>	<head>		<meta charset="utf-8">		<title></title>		<style type="text/css">			* {				margin: 0;				padding: 0;			}			.block{				width: 500px;				height: 500px;				margin: 0 auto;				margin-top: 100px;				border-radius: 50%;				border: 10px solid black;				position: relative;			}			.block > div{				position: absolute;				top: 0;				left:0;				bottom: 0;				right:0;				margin: auto;			}			/* 设置时针 */			.hour-wrapper{				height: 70%;				width: 70%;				animation: run 7200s linear infinite;			}			.min-wrapper{				height: 80%;				width: 80%;				animation: run 600s steps(60) infinite;			}			.sec-wrapper{				height: 90%;				width: 90%;				animation: run 10s steps(60) infinite;			}			.hour{				height: 50%;				width: 6px;				background-color: black;				margin: 0 auto;			}			.min{				height: 50%;				width: 4px;				background-color: black;				margin: 0 auto;			}			.sec{				height: 50%;				width: 2px;				background-color: black;				margin: 0 auto;			}			/* 旋转的关键帧 */			@keyframes run {				from {					transform: rotateZ(0);				}				to {					transform: rotateZ(360deg);				}			}		</style>	</head>	<body>		<!-- 创建表容器 -->		<div class="block">			<!-- 创建时针 -->			<div class="hour-wrapper">				<div class="hour"></div>			</div>			<!-- 创建分针 -->			<div class="min-wrapper">				<div class="min"></div>			</div>			<!-- 创建秒针 -->			<div class="sec-wrapper">				<div class="sec"></div>			</div>		</div>	</body></html>
```

### 3d旋转

```html
<!DOCTYPE html><html>	<head>		<meta charset="utf-8">		<title></title>		<style>			html{				perspective: 800px;			}			.cube{				width: 200px;				height: 200px;				margin: 100px auto;				transform-style: preserve-3d;				transform: rotateX(45deg) rotateZ(45deg);				animation: rotate 20s infinite linear;			}			.cube > div{				width: 200px;				height: 200px;				opacity: 0.8;				position: absolute;				/* 设置3d变形效果 */			}			img{				vertical-align: top;			}			.box1{				transform: rotateY(90deg) translateZ(100px);			}			.box2{				transform: rotateY(-90deg) translateZ(100px);			}			.box3{				transform: rotateX(90deg) translateZ(100px);			}			.box4{				transform: rotateX(-90deg) translateZ(100px);			}			.box5{				transform: rotateY(180deg) translateZ(100px);			}			.box6{				transform: rotateY(0deg) translateZ(100px);			}			@keyframes rotate{				from{					transform: rotateX(0) rotateZ(0);				}				to{					transform: rotateX(1turn) rotateZ(1turn);				}			}		</style>	</head>	<body>		<!-- 创建一个外部容器 -->		<div class="cube">			<!-- 引入图片 -->			<div class="box1"><img src="../img/laopo01.png" alt=""></div>			<div class="box2"><img src="../img/laopo02.png" alt=""></div>			<div class="box3"><img src="../img/laopo03.png" alt=""></div>			<div class="box4"><img src="../img/laopo04.png" alt=""></div>			<div class="box5"><img src="../img/laopo05.png" alt=""></div>			<div class="box6"><img src="../img/laopo06.png" alt=""></div>					</div>	</body></html>
```



### 一、弹性容器的样式

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210223234313434.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210223234544914.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210224195243588.png)


![在这里插入图片描述](https://img-blog.csdnimg.cn/20210223235135676.png)

```html
<!DOCTYPE html><html>	<head>		<meta charset="utf-8">		<title></title>		<style>			*{				margin: 0;				padding: 0;			}			ul{				width: 800px;				border: 10px solid red;				/*设置ul为弹性容器 */				display: flex;				/* 设置排列的方向 */				/* flex-direction: row; */				/* 设置弹性元素是否自动换行 */				/* flex-wrap: wrap; */				/* 简写属性 */				/* flex-flow: column nowrap; */								/* 如何分主轴上的空白空间					flex-start:沿着主轴的起边排列；					flex-end:沿着主轴的终边排列；					center:居中排列；					space-around:空白分布到元素两侧；					space-between:空白分布元素中间；					space-evenly:空白分布在元素的单侧；				 */				/* justify-content: space-evenly;					针对主轴上的布局				 */								/* 				 stretch  默认值，让元素的长度相同（行与行之间的高度）				 flex-start  沿着辅轴的起边对齐				 flex-end  沿着辅轴的终边对齐				 center   居中对齐				 baseline  基线对齐				 */				align-items: stretch;								/* 				辅轴中间的空白对齐方式； 				 */				align-content: flex-end;											}			li{				width:200px;				height: 100px;				background-color: #bfa;				font-size: 50px;				text-align: center;				line-height: 100px;				list-style: none;				/* 设置缩减系数 */				flex-shrink: 0;			}			li:nth-child(1){				align-self: stretch;				/* 用来覆盖当前元素的align-items */			}			li:nth-child(2){				background-color: pink;			}			li:nth-child(3){				background-color: orange;			}		</style>	</head>	<body>		<ul>			<li>1</li>			<li>2</li>			<li>3</li>		</ul>	</body></html>
```

### 二、弹性元素的样式

```html
<!DOCTYPE html><html>	<head>		<meta charset="utf-8">		<title></title>		<style>			*{				margin: 0;				padding: 0;			}			ul{				width: 800px;				border: 10px solid red;				/*设置ul为弹性容器 */				display: flex;															}			li{				width:200px;				height: 100px;				background-color: #bfa;				font-size: 50px;				text-align: center;				line-height: 100px;				list-style: none;				/* 弹性增长系数 */				/* flex-grow: 1; */				/* 				 设置的缩减系数					计算的方式比较复杂，是根缩减系数和大小决定				 */				flex-shrink: 1;								/* 				元素基础长度					如果主轴是横向的，则指定的是元素的宽度					如果主轴是纵向的，则指定的是元素的高度					默认值，auto表示参考的是元素自身的宽度或者高度				 */				flex-basis: 100px;								/* flex可以设置弹性元素的样式 					flex 增长 缩减 基础					initial :0 1 auto;					auto :1 1 auto;					none : 0 0 auto;弹性元素没有弹性				*/				flex:1 1 auto; 							}			li:nth-child(1){				/* 决定元素的排列顺序 */				order: 3;			}			li:nth-child(2){				background-color: pink;				/* flex-grow: 2; */			}			li:nth-child(3){				background-color: orange;				/* flex-grow: 3; */			}		</style>	</head>	<body>		<ul>			<li>1</li>			<li>2</li>			<li>3</li>		</ul>	</body></html>
```

### 三、淘宝手机导航练习

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210224205602502.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

```html
<!DOCTYPE html><html lang="zh"><head>	<meta charset="UTF-8">	<meta name="viewport" content="width=device-width, initial-scale=1.0">	<meta http-equiv="X-UA-Compatible" content="ie=edge">	<title></title>	<style>		.nav{			width: 100%		}		/* 设置每一行的容器 */		.nav-inner{			/* 设置为弹性容器 */			display: flex;			justify-content: space-around;		}		.item{			/* flex:auto; */			width: 18%;			text-align: center;		}		.item img{			width: 100%;		}		.item a{			color: #333;			text-decoration: none;			font-size: 16px;		}				</style></head><body>	<!-- 创建一个外部容器 -->	<nav class="nav">		<div class="nav-inner">			<div class="item"><a href="#"><img src="taobaoImage/01.png" alt=""><span>天猫</span></a></div>			<div class="item"><a href="#"><img src="taobaoImage/02.png" alt=""><span>今日爆款</span></a></div>			<div class="item"><a href="#"><img src="taobaoImage/03.png" alt=""><span>天猫国际</span></a></div>			<div class="item"><a href="#"><img src="taobaoImage/04.png" alt=""><span>饿了么</span></a></div>			<div class="item"><a href="#"><img src="taobaoImage/05.png" alt=""><span>天猫超市</span></a></div>		</div>		<div class="nav-inner">			<div class="item"><a href="#"><img src="taobaoImage/06.png" alt=""><span>充值中心</span></a></div>			<div class="item"><a href="#"><img src="taobaoImage/07.png" alt=""><span>机票酒店</span></a></div>			<div class="item"><a href="#"><img src="taobaoImage/08.png" alt=""><span>金币庄园</span></a></div>			<div class="item"><a href="#"><img src="taobaoImage/09.png" alt=""><span>阿里拍卖</span></a></div>			<div class="item"><a href="#"><img src="taobaoImage/10.png" alt=""><span>淘宝吃货</span></a></div>					</div>	</nav></body></html>
```



### 一、像素、视口介绍

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210224210946994.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210224211542822.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210224214927283.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210224220210413.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021022422055355.png)

### 二、手机页面练习

```html
<!DOCTYPE html><html lang="zh"><head>	<meta charset="UTF-8">	<meta name="viewport" content="width=device-width, initial-scale=1.0">	<meta http-equiv="X-UA-Compatible" content="ie=edge">	<title></title>	<link rel="stylesheet" type="text/css" href="css/style.css"/>	<link rel="stylesheet" href="77.图标字体/fa/css/all.css"></head><body>	<!-- 创建头部容器 -->	<header class="top-bar">		<div class="menu-btn"><a href="#"><i class="fas fa-stream"></i></a></div>		<h1 class="logo"><a href="#">爱学习</a></h1>		<div class="search-btn"><a href="#"><i class="fas fa-search"></i></a></div>	</header>	<!-- 创建banner -->	<div class="banner"><a href="#"><img src="mobileprac/banner.png" ></a></div>	<!-- 菜单 -->	<nav class="menu">		<a href="#" class="course"><i class="fas fa-book"></i>我的课程</a>		<a href="#" class="star"><i class="fas fa-cut"></i>明星讲师</a>		<a href="#" class="sub"><i class="fas fa-globe"></i>我的订阅</a>		<a href="#" class="download"><i class="fas fa-envelope"></i>我的下载</a>	</nav>	<!-- 课程列表 -->	<div class="course-list">		<!-- 列表标题 -->		<div class="title">			<h2>最新课程</h2>			<a href="#" class="more">更多+</a>		</div>		<!-- 列表容器 -->		<div class="item-list">			<div class="item">				<!-- 封面 -->				<div class="cover"><img src="mobileprac/pic01.jpg" alt=""></div>				<!-- 小标题 -->				<h3 class="course-title">摄影课程</h3>				<!-- 用户信息 -->				<div class="user-info">					<div class="avatar"><img src="mobileprac/user-image.jpg" alt=""></div>					<div class="nickname">令狐冲</div>				</div>			</div>		</div>	</div></body></html>
```

```css
// 使用的是less*{	margin: 0;	padding: 0;}@total-width:750;.w{	width: 693/40rem;	margin: 0 auto;}html{	// 设置rem比值	font-size: 100vw/@total-width * 40;	background-color: #eff0f4;}a{	text-decoration: none;}// 设置头部.top-bar:extend(.w){	display: flex;	height: 175/40rem;	line-height: 175/40rem;	// 设置对齐方式	justify-content: space-between;	// 设置辅轴的对齐方式	align-items: center;	a{		color: #24253d;		font-size: 50/40rem;		i{			color: #999;			font-size: 40/40rem;		}	}}// 设置banner.banner:extend(.w){	overflow: hidden;	img{		width: 100%;	}}// 设置中间菜单.menu:extend(.w){	// 确定元素的高度	height: 329/40rem;		// 设置弹性元素	display: flex;	// 设置框的大小	// 设置换行	flex-flow:row wrap; 	justify-content: space-between;	align-content: space-around;	a{		width: 327/40rem;		height: 104/40rem;		line-height: 104/40rem;		color: white;		border-radius: 10/40rem;		i{			margin: 0 20/40rem 0 38/40rem;		}	}	.course{		background-color: #f97053;	}	.star{		background-color: #cd6efe;	}	.sub{		background-color: #fe4479;	}	.download{		background-color: #1bc4fb;	}}// 设置课程列表.course-list:extend(.w){	height: 394/40rem;	display: flex;	flex-flow: column;	justify-content: space-between;	margin-bottom: 46px/40rem;	.title{		display: flex;		justify-content: space-between;		align-items: center;		h2{			font-size: 33/40rem;			color: #24253D;			border-left: 2/40rem solid #3a84ff;			padding-left: 4/40rem;		}		a{			font-size: 28/40rem;			color: #656565;		}	}}// 设置item.item{	width: 320/40rem;	height: 350/40rem;	background-color: #fff;	box-shadow: 0 0 10px/40rem rgba(0,0,0,.3);	overflow: hidden;	border-radius: 10/40rem;	padding: 0 22/40rem;	display: flex;	flex-flow: column;	justify-content: space-evenly;	.cover{		overflow: hidden;		// padding-top: 15/40rem;	}	img{		width: 100%;		vertical-align: top;	}	.course-title{		font-size: 32/40rem;		color: #24253D;	}	.user-info{		display: flex;		align-items: center;	}	.avatar{		width: 42/40rem;		height: 42/40rem;		border-radius: 50%;		overflow: hidden;	}	.nickname{		font-size: 24/40rem;		color: #969693;	}}
```



### 一、媒体查询介绍

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210227074630439.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### 二、语法

```html
		<style type="text/css">			@media only screen and (min-width:500px) and (max-width:700px) {				body{					background-color: #bfa;				}			}		</style>
```

### 三、练习：响应式导航条

```html
<!DOCTYPE html><html>	<head>		<meta charset="utf-8">		<title></title>		<link rel="stylesheet" type="text/css" href="../54.布局作业/01/reset.css" />		<link rel="stylesheet" type="text/css" href="../77.图标字体/fa/css/all.css" />		<link rel="stylesheet" href="style.css">	</head>	<body>		<!-- 		 响应式设计的网页：			移动端优先；			渐进增强；		 -->		<div class="topbar-wrapper">			<!-- 外部容器 -->			<div class="top-bar">				<!-- 左侧的菜单栏 -->				<div class="left-menu">					<!-- 创建菜单图标 -->					<ul class="menu-icon">						<li></li>						<li></li>						<li></li>					</ul>					<!-- 创建菜单 -->					<ul class="nav">						<li><a href="#">手机</a></li>						<li><a href="#">美容仪器</a></li>						<li><a href="#">配件</a></li>						<li><a href="#">服务支撑</a></li>						<li><a href="#">企业网站</a></li>						<li>							<a href=""><i class="fas fa-search"></i></a>							<span>搜索 Meitu.com</span>						</li>					</ul>				</div>				<!-- logo -->				<h1 class="logo">					<a href="#">美图手机</a>				</h1>				<!-- 用户信息 -->				<div class="user-info">					<a href="#">						<i class="fa fa-user"></i>					</a>				</div>			</div>		</div>	</body></html>
```

```css
a{	text-decoration: none;	color: #fff;	&:hover{		color: rgb(197,196,196);	}}.topbar-wrapper{	background-color: #000000;}// 导航条外部容器.top-bar{	max-width: 1200px;	margin: 0 auto;	height: 48px;	background-color: #000000;	padding: 0 14px;	display: flex;	align-items: center;	justify-content: space-between;}.left-menu{	// position: relative;	&:hover{		.nav{			display: block;		}	}	.nav{		display: none;		position: absolute;		top: 48px;		background-color: #000;		left:0;		right:0;		bottom: 0;		padding-top: 60px;		li{			width: 80%;			margin: 0 auto;			border-bottom: 1px solid #4e4e4e;			a{				display: block;				line-height: 44px;				font-size: 14px;			}			&:last-child a{				display: inline-block;				margin-right: 6px;			}			span{				color: #fff;				font-size: 14px;			}		}	}	.menu-icon{		// background-color: #bfa;		width: 18px;		height: 48px;		position: relative;		li{			width: 18px;			height: 1px;			background-color: #fff;			position: absolute;			// 修改变形原点			transform-origin: left center;			transition: all 0.5s;		}		li:nth-child(1){			top: 18px;		}		li:nth-child(2){			top: 24px;		}		li:nth-child(3){			top: 30px;		}		&:hover{			li:nth-child(1){				// 向下旋转				transform: rotateZ(40deg);						}			li:nth-child(2){				opacity: 0;			}			li:nth-child(3){				transform: rotateZ(-40deg);			}		}	}}// 设置logo.logo{	a{		display: block;		width: 122px;		height: 32px;		background-image: url(images/dff63979.sprites-index@2x.png);		background-size: 400px 400px;		text-indent: -9999px;	}}// 设置媒体查询@media only screen {	// 断点768px	@media (min-width: 768px){		.left-menu{			order: 2;			// 显示菜单			flex: auto;			.nav{				display: flex;				position: static;				padding: 0;				justify-content: space-around;				li{					width: auto;					border-bottom: none;					margin: 0;					a{						line-height: 48px;											}					span{						display: none;					}				}			}			// 隐藏菜单图标			.menu-icon{				display: none;			}					}		.logo{			order: 1;		}		.user-info{			order: 3;		}	}}
```







# 媒体查询

## 响应式布局

网页可以根据不同的设备，或窗口大小呈现出不同的效果

使用响应式布局，可以使一个网页适用于所有设备

响应式布局的关键就是，媒体查询

通过媒体查询，可以为不同的设备，或不同的状态分别设置样式

## 媒体查询简介

使用媒体查询

```
语法：@media 查询规则（）
媒体类型：
    all 所有设备
    print 打印设备
    screen 带屏幕的设备
    speech 屏幕阅读器

可以在媒体查询类型前面加一个only，表示只有
@media only screen{
    background-color: red;
}
```

## 媒体特性

```
width  视口的宽度
height 视口的高度

min-width 视口的最小宽度（视口大于指定宽度时生效）
max-width 视口的最大宽度（视口小于指定宽度时生效）
@media(min-width: 500px){
    body{
        background-color:red;    
    }
}
```

一般常用的断点

| 范围     | 使用屏幕 | 设置             |
| -------- | -------- | ---------------- |
| 小于768  | 超小屏幕 | max-width=768px  |
| 大于768  | 小屏幕   | min-width=768px  |
| 大于992  | 中型屏幕 | min-width=992px  |
| 大于1200 | 大于屏幕 | min-width=1200px |



```
@media(min-width:500px) and (max-width: 700px){
    body{
        background-color: red;   
    }
}
```













