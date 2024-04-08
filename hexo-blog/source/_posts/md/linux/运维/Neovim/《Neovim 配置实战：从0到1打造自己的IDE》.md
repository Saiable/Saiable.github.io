---
title: Neovim 配置实战：从0到1打造自己的IDE
cover: false
date: 2022-7-25 20:34:51
typora-root-url: 《Neovim 配置实战：从0到1打造自己的IDE》
---



[TOC]

源链接：[Neovim 配置实战：从0到1打造自己的IDE - 陈新_nshen - 掘金小册 (juejin.cn)](https://juejin.cn/book/7051157342770954277)

对应的github：

花了我`26.91`大洋

# 1.多年 VSCode 老粉，为什么最终转向 Neovim？

本人常年在 Windows 系统上做程序开发，虽然已经习惯使用 “VIM” 的快捷键指法好多年了，但一直使用的都是被称为宇宙第一开发工具 VSCode 下的  [VSCodeVim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FVSCodeVim%2FVim) 插件，中间曾尝试配置过几次原生的 VIM，包括各种 GUI 的版本，最终都放弃了。

主要原因一个是 VSCode 实在是太强大了，应用商店有各种插件，涵盖 Web 开发的方方面面，装上基本不用配置就非常非常好用（ 虽然在早期的 VSCode 上的有好几个 VIM 相关的插件都各有各的 bug，但后期当 VSCodeVim 被微软收编后，其他插件都停止了更新。[VSCodeVim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FVSCodeVim%2FVim) 在有了微软的投入后，也变得足够好用了）。最主要的是，我们还可以混用 VIM 的快捷键和 VSCode 的原生功能，比如  `Ctrl + Shift + p` 打开的无敌窗口调用 VSCode 的任意功能。

而当时的原生 VIM 这边配置太原始了，要在 `vimrc` 里写一堆看不懂的配置才能满足最基本使用。代码提示也不够智能，费大劲配置出来，效果还也不如 VSCode 默认配置。 而且在 Windows 上的支持也不是很好，除了在服务器上开发外，在本地做编辑器根本没有任何优势。

可是，随着  [WSL 2](https://link.juejin.cn/?target=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fwindows%2Fwsl%2F) 和  [Windows Terminal](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fterminal) 的推出，Windows 命令行也有了 Unicode 和 UTF-8 字符，GPU 加速文本渲染引擎等支持。而  [Neovim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim) 0.5.x 正式版推出后，更是内置了 LSP（[Language Server Protocol](https://link.juejin.cn/?target=https%3A%2F%2Fmicrosoft.github.io%2Flanguage-server-protocol%2F)），代码提示的体验已经跟 VSCode 看齐了，**现在的 VSCode 和原生 VIM 相比优势就不是那么明显了。**

与此同时，[Neovim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim) 在 0.5.x 版本引入了 Lua 编程语言作为编辑器的一等语言，相比于传统的 VIM 脚本 ，Lua 是一门通用的编程语言，代码更清晰，运行速度也更快，语法也更简单，即使没学过 Lua 也能猜出大概意思，使配置文件更人性化，更易看懂，没有原生 VIM 那么硬核了。

**现在众多 VIM 插件都有了基于 Lua 的原生 Neovim 版本，使得 Neovim 脱离了传统 VIM 的束缚，可以真正的称之为现代化的开发工具了。**

反而 VSCode 每月都有一次强制的更新，给人的压迫感极大，[长长的 Release Notes](https://link.juejin.cn/?target=https%3A%2F%2Fcode.visualstudio.com%2Fupdates) 中，不断地增加完全用不到的功能，你也只能被动接受，导致系统肉眼可见的越来越慢，越来越难用。而 Neovim 是以高度可定制性闻名的，你可以只配置你需要的功能，直接砍掉不喜欢的功能，或者干脆裸跑当成记事本都可以，这点上好于 VSCode 太多了。

最烦的还有 VSCode 并不会考虑到你的开发效率，使用中总有窗口弹出来，总有要你离开键盘用鼠标去点的按钮，而  Neovim 则可以天然的完全脱离鼠标，在任何窗口之间随意切换焦点，提升开发效率。

Neovim 的配置可以不断修改和改进。我觉得学会调教 Neovim 在程序开发生涯中是非常有意义的一件事，让编辑器适配你的习惯，而不是无限地追赶编辑器的更新，也是成为“ 10 倍速程序员” 必经之路。

如果你在 Google 上搜索 "Years Vim" ，会看到很多高手都已经自豪的使用 VIM 编辑器 10 年以上了，比如这篇 [VIM AFTER 15 YEARS](https://link.juejin.cn/?target=https%3A%2F%2Fstatico.github.io%2Fvim3.html) 或这篇 [Ten Years of Vim](https://link.juejin.cn/?target=https%3A%2F%2Fendler.dev%2F2018%2Ften-years-of-vim%2F) 等等，他们都会一直维护一个属于自己独一无二的配置，彼此各不相同，通过不断地调教，使之越来越适合自己，达到了“人剑合一”的境界。

这里我也展示一下自己配置的运行效果：

![features2.gif](82fd07bc9d6746be9c786009a0321b71tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

我自己已经使用 VSCode 很多年了，这次下决心转移到 Neovim，看了很多文档，参考了很多配置资料，尝试了很多插件，也走了很多弯路，终于我的 Neovim 的配置已经完全可以满足目前我对代码编辑器的需求了。所以我想写成小册，把配置方法分享出来。

回想当初我在学习的时候，如果有这个小册，真的可以节省很多时间。所以也希望能帮助到你，通过对这个小册的学习，你将可以把 Neovim 配置成你希望的样子，也许跟我的完全不同。

在章节的安排上，分为 **基建篇** 和 **代码篇**。

在 **基建篇** 中，我们会先从最基础的如何安装 Neovim 始，接着介绍配置文件位置，以及我们应该如何组织配置文件、必备的基础配置、快捷键如何设置、插件如何安装和管理。然后通过逐个介绍目前流行的插件安装方式和使用方法来补全文本编辑器所需的所有功能。

基建篇完成后你将会得到一个现代化的文本编辑器。

在 **代码篇** 中，我们会补全程序开发相关的功能，包括如何实现代码高亮，什么是内置 LSP，如何配置 Neovim 内置 LSP，代码如何补全，如何设置自定义代码段，代码格式化，UI 可否再美化加强等。之后还会专门针对前端开发和 rust 开发所必备的插件配置介绍，一步一步帮助你将手中的 Neovim 装配成 VSCode 般的开发环境。

![xmind.png](7f4e9afbfa684e25ad4c5b2b913c7623tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

本小册适合有一点 VIM 基础的使用者（至少知道怎么编辑文件和退出 VIM 😁），有志于提升开发效率与开发体验，却被网上零散过时的 VIM 配置教程困扰的同学们。

我们一起加油，早点成为 10x 程序员！

# 2.Neovim 的安装与配置架构总览



本节是第一篇，我们要先介绍一下如何在 Windows 命令行环境下安装 Neovim，然后会对配置文件结构做一个总体的规划。

在安装 Neovim 之前，首先要确保你的电脑上有 WSL 2 环境，WSL 是 Windows Subsystem for Linux 的缩写，简单来讲就是在 Windows 上运行的 Linux 子系统。WSL 2 就是 WSL 的 2.0 版本。WSL 2 的安装方法在这里就不展开说了，如有需要请参考[官方指南](https://link.juejin.cn/?target=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fwindows%2Fwsl%2Finstall)或其他教程。

我们假设您的系统已经成功安装 WSL 2，如果不确定是否安装过，可以打开 `cmd` 中运行 `wsl -l -v` 进行验证：

![wsl2.png](3d2b4880841d45579e7677ae1095fcf0tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

跟上图一致，表示安装成功，可以看到我们安装的子系统为 `Ubuntu-18.04`，也是我推荐的系统。

后边的 `VERSION 2` 表示是在 `WSL2` 环境，成功后可以继续下一步。

由于我们的整个编辑器都要在命令行下运行，所以需要的终端工具必须支持 UTF8 字符， `cmd` 是不可以的，需要安装微软的 Windows Terminal。

## 安装 Windows Terminal

Windows Terminal 是微软开源的新一代终端工具，主要功能包括多个选项卡、窗格、Unicode和 UTF-8 字符支持，GPU 加速文本渲染引擎以及自定义主题、样式和配置。

![terminal.jpg](9437fd75bdcd44069d6461a9f16fe532tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

推荐使用 [微软应用商店](https://link.juejin.cn/?target=https%3A%2F%2Fwww.microsoft.com%2Fzh-cn%2Fp%2Fwindows-terminal%2F) 进行安装。安装后可以在 `设置` 里进行对外观进行设置，比如我在 `外观` 中打开了`深色主题`，在 `配色方案中` 可以选择 `One Half Dark`，如果在之后发现有快捷键出现冲突，可以在这里的 `操作` 中 删除了与 VIM 冲突的快捷键。

在这里最重要的设置，是字体设置，要选择包含 **Nerd fonts** 的字体。因为命令行中是不支持显示图标的，比如下图的文件夹图标，如果没有 Nerd fonts 则会显示成右边类似**乱码**的样子。

![nerdfonts4.png](b9724b1008424c04b970dcd2cf1b9c0atplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

那么，什么是 Nerd fonts ？

> Nerd Fonts 是一个使用大量字体图标来解决程序员在开发过程中缺少合适字体的问题的项目。它可以从流行的字体图标库中将大量外部字体引入待开发的项目中，它支持的字体图标库包括 Font Awesome , Devicons , Octicons , and others。

简单讲，Nerd fonts 就是把各种常见的 ‘iconic fonts’，打包到你常用的字体里，这样在命令行里就支持显示这些图标了。

![nerdfonts.png](31609ce6810d4dbab0c84ce48aab6028tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

很多 `Neovim` 插件都会使用到这里的图标，必须正确安装才可以在命令行下正确显示 icons。

## 安装 Nerd fonts

Nerd fonts 本身并不是一种新的字体，而是把常用图标以打补丁的方式打到了常用字体上。

比如我在 VSCode 里最常用的是 `Fira Code` 字体，那么我就要去安装这个打了 Nerd fonts 补丁的 `FiraCode` 字体。或者你也可以到官网这里 [www.nerdfonts.com/font-downlo…](https://link.juejin.cn/?target=https%3A%2F%2Fwww.nerdfonts.com%2Ffont-downloads) 找到你喜欢的字体。

这里我找到的字体的路径为：

```txt
https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/FiraCode/Regular/complete/
```

注意要下载里边兼容 Windows 的版本，就是名为 `XXXX Windows Compatible.ttf`，下载后双击即可安装完成。



然后回到 Terminal 中点击 **设置**，**外观**，在字体选项里，选中刚才安装的带 `NF` 结尾的字体（NF：Nerd Fonts），保存。

![nerdfonts2.png](1f57f8fd18b84e9bb23eff999dcde775tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

安装过后，命令行里就支持显示这些小图标了，为了测试是否成功，可以到这个网址：[www.nerdfonts.com/cheat-sheet](https://link.juejin.cn/?target=https%3A%2F%2Fwww.nerdfonts.com%2Fcheat-sheet)

点击 `Show All Icons` 按钮，选择一个图标，点击右上角的 Copy Icon，然后粘贴到我们的 Terminal 命令行里。

![nerdfonts3.png](41dc19d7624041089a51e32d547a130etplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

看到我复制的 `github` 和 `twitter` 小图标了吗，如果可以正确显示就是成功了。 准备工作完成，可以开始安装 Neovim 了。

## 安装 Neovim

由于我的环境是 `Ubuntu-18.04`，所以要用 `apt` 安装 Neovim ，具体方法如下：

```bash
sudo add-apt-repository ppa:neovim-ppa/unstable
sudo apt-get update
sudo apt-get install neovim
```

如果你这里出现报错，找不到 `add-apt-repository` 命令，这是因为系统缺少必要的依赖包，

需要先安装下边的包：

```
sudo apt-get install software-properties-common
```

安装成功后，运行 `nvim --version` 即可输出版本信息，注意确认 `nvim` 版本必须为 **0.6** 以上。

我在编写这本小册时，显示为 `NVIM v0.7.0-dev` ，如果版本过低，说明没有成功添加 `ppa:neovim-ppa/unstable`，需要重新安装。

安装完成后可选步骤，替换默认的 vim `nvim ~/.bashrc`，添加别名：

```bash
alias vim='nvim'
alias vi='nvim'
alias v='nvim'
```

这样修改后，无论运行 vim、 vi 或 v 打开的都是 Neovim 了。安装到此也就完成了，如果你也安装成功了，那么恭喜你走完了万里长征的第一步，接下来就可以对 Neovim 进行一系列的定制了。不过在定制之前，还有一件事需要提前做好，那就是提前做好规划。

## 配置总览

虽然可以把所有配置写在一个文件里，但由于后续我们要配置很多东西，所以预先的规划是很有必要的，因为配置可能随时调整，需要随时打开、关闭某个功能的时候，尽量不要影响到其他功能。建议你在阅读时先跟着我的结构配置走，当你完成本小册的学习后，就可以根据你的需要随意调整了。

这里我先对本小册中的配置文件结构做一个总览，后续章节会逐个介绍。

整体结构：

```txt
├── LICENSE
├── README.md
├── init.lua
└── lua
    ├── autocmds.lua
    ├── basic.lua
    ├── colorscheme.lua
    ├── keybindings.lua
    ├── lsp
    │   ├── cmp.lua
    │   ├── config
    │   │   ├── bash.lua
    │   │   ├── emmet.lua
    │   │   ├── html.lua
    │   │   ├── json.lua
    │   │   ├── lua.lua
    │   │   ├── markdown.lua
    │   │   ├── pyright.lua
    │   │   ├── rust.lua
    │   │   └── ts.lua
    │   ├── formatter.lua
    │   ├── null-ls.lua
    │   ├── setup.lua
    │   └── ui.lua
    ├── plugin-config
    │   ├── bufferline.lua
    │   ├── comment.lua
    │   ├── dashboard.lua
    │   ├── gitsigns.lua
    │   ├── indent-blankline.lua
    │   ├── lualine.lua
    │   ├── nvim-autopairs.lua
    │   ├── nvim-tree.lua
    │   ├── nvim-treesitter.lua
    │   ├── project.lua
    │   ├── surround.lua
    │   ├── telescope.lua
    │   ├── toggleterm.lua
    │   ├── vimspector.lua
    │   └── which-key.lua
    ├── plugins.lua
    └── utils
        ├── fix-yank.lua
        ├── global.lua
        └── im-select.lua
```

首先 **init.lua** 是整个配置的入口文件，负责引用所有其他的模块，基本上想要打开或关闭某个插件只要在这里修改一行代码即可。

- **basic.lua：** 基础配置，是对默认配置的一个重置。

- **colorscheme.lua：** 我们安装的主题皮肤配置，在这里切换主题。

- **keybindings.lua：** 快捷键的设置，所有插件的快捷键也都会放在这里。

- **plugins.lua：** 插件安装管理，插件安装或卸载全在这里设置。

- lsp 文件夹：

   

  是对 Neovim 内置 LSP 功能的配置，包括常见编程语言与语法提示等。

  - **config** **：** 文件夹包含各种语言服务器单独的配置文件。
  - **setup.lua** **：** 内置 LSP 的配置。
  - **cmp.lua** **：** 语法自动补全补全的配置，包括各种补全源，与自定义代码段。
  - **ui.lua：** 对内置 LSP 功能增强和 UI 美化。
  - **formatter.lua：** 独立代码格式化功能。

- **plugin-config 文件夹：** 是对第三方插件的配置，未来每添加一个插件，这里就多一个配置文件。

- **utils 文件夹：** 是对常见问题的修改，包括输入法切换，针对 windows 的特殊配置等。

目前 Neovim 的默认配置还不尽人意，还需要一些基础的配置。在下一节中，我们会先介绍如何对 Neovim 做一些基础配置。

> 配置中如遇任何问题，可到 [github.com/nshen/learn…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 参考最终源码

## 补充

下载：[Nerd Fonts - Iconic font aggregator, glyphs/icons collection, & fonts patcher](https://www.nerdfonts.com/)

选择字体：Agave Nerd Font

下载下来后，在windows系统上安装，然后xshell上设置一下：

![image-20220425171043801](image-20220425171043801.png)

复制该链接上的`Icon`:https://www.nerdfonts.com/cheat-sheet

![image-20220425171122978](image-20220425171122978.png)

粘贴到终端上测试一下，没问题的话，就会显示图标了：

![image-20220425171212058](image-20220425171212058.png)

xhsell我还额外应用了主题，可能会合`neo-vim`的主题色冲突，建议使用默认的即可

![image-20220425172548567](image-20220425172548567.png)



**补充结束**

# 3.Neovim 有哪些需要关注的基础配置项？

由于历史的原因， VIM 的很多默认设置都不太合理。Neovim 出现以后，虽然对 VIM 默认配置做很多修正，但它的定位仍然是文本编辑器，对于习惯 VSCode 等现代化的开发工具的开发者来说，内置的功能是远远不够，需要为添加插件做一些修正。

同时为了配置信息的跨版本安全，我们也应该把需要的配置信息明确地列出来，作为我们的第一层配置，也是对整个配置项的一个重置。

本节将会介绍如何创建这个配置。但在开始配置之前，我们要知道 Neovim 默认配置的入口在哪里。

## 配置入口文件

Neovim 配置文件入口与 VIM 不太一样，不是 `.vimrc` 。而是保存在用户Home目录中的 `~/.config/nvim/init.lua` 文件， 也可以是用 VIM 脚本写的 `init.vim` 文件。

不过 Neovim 未来的趋势应该会是全 Lua 化了。由于`Lua` 是一种很轻巧的脚本语言，体积小，启动速度快，也更通用，最重要的是语法简单，非常容易学习，所以我这里选择使用 `init.lua` 文件，请记住根目录的这个文件，后续课程中我每次提到 **入口文件** 就是指的这个文件。

当然，如果你是一个 VIM 老用户，你会有一些属于你的 VIM 脚本配置，那么使用 `init.vim` 也是可以的，而且 Neovim 未来也并不会取消对 VIM 脚本的支持，在 `.vim` 文件里也可以任意调用 Lua 的代码，所以你可以保留在 `init.vim` 中的配置，只在后边新加的配置中增量添加 Lua 代码。

## 在 .vim 中调用 lua

如果要从 `init.vim` 里写 `Lua`代码，通常要以 lua 关键字开头，类似这样：

```vim
lua print('单行 lua')
```

多行调用，则可以写成这样：

```vim
lua <<EOF 
print('多行 lua') 
print('多行 lua') 
EOF
```

加载其他 lua 文件，可以写成：

```vim
" 加载 lua/basic.lua 文件，此行为注释 
lua require('basic')
```

由于我没有历史遗留，所以这里我使用全 Lua 编写，在 `~/.config/nvim/` 里创建全新的入口文件 `init.lua` 。

## 配置入口 init.lua

我们在 `~/.config/nvim/init.lua` 里写入如下内容：

```lua
-- 基础设置
require('basic')
```

`require` 函数在 Lua 中用于加载一个模块，而这些模块通常位于 `runtimepath` 中的 `lua/` 目录下，也就是我们的 `~/.config/nvim/lua/` 目录。

所以上边的代码，就是加载 `~/.config/nvim/lua/basic.lua` 文件（注意：require 里没有 `.lua` 扩展名）。当然也可以创建 `~/.config/nvim/lua/basic/` 目录，在目录下边创建 `init.lua` 文件也是可以成功加载的。

## 基础配置文件 basic.lua

创建对应的 `~/.config/nvim/lua/basic.lua` 文件，作为基础配置文件。

添加内容如下：

```lua
-- utf8
vim.g.encoding = "UTF-8"
vim.o.fileencoding = 'utf-8'
-- jkhl 移动时光标周围保留8行
vim.o.scrolloff = 8
vim.o.sidescrolloff = 8
-- 使用相对行号
vim.wo.number = true
vim.wo.relativenumber = true
-- 高亮所在行
vim.wo.cursorline = true
-- 显示左侧图标指示列
vim.wo.signcolumn = "yes"
-- 右侧参考线，超过表示代码太长了，考虑换行，可以不加，太丑了
--- vim.wo.colorcolumn = "80"
-- 缩进2个空格等于一个Tab
vim.o.tabstop = 2
vim.bo.tabstop = 2
vim.o.softtabstop = 2
vim.o.shiftround = true
-- >> << 时移动长度
vim.o.shiftwidth = 2
vim.bo.shiftwidth = 2
-- 空格替代tab
vim.o.expandtab = true
vim.bo.expandtab = true
-- 新行对齐当前行
vim.o.autoindent = true
vim.bo.autoindent = true
vim.o.smartindent = true
-- 搜索大小写不敏感，除非包含大写
vim.o.ignorecase = true
vim.o.smartcase = true
-- 搜索不要高亮
vim.o.hlsearch = false
-- 边输入边搜索
vim.o.incsearch = true
-- 命令行高为2，提供足够的显示空间
vim.o.cmdheight = 2
-- 当文件被外部程序修改时，自动加载
vim.o.autoread = true
vim.bo.autoread = true
-- 禁止折行
vim.wo.wrap = false
-- 光标在行首尾时<Left><Right>可以跳到下一行
vim.o.whichwrap = '<,>,[,]'
-- 允许隐藏被修改过的buffer
vim.o.hidden = true
-- 鼠标支持
vim.o.mouse = "a"
-- 禁止创建备份文件
vim.o.backup = false
vim.o.writebackup = false
vim.o.swapfile = false
-- smaller updatetime
vim.o.updatetime = 300
-- 设置 timeoutlen 为等待键盘快捷键连击时间500毫秒，可根据需要设置
vim.o.timeoutlen = 500
-- split window 从下边和右边出现
vim.o.splitbelow = true
vim.o.splitright = true
-- 自动补全不自动选中
vim.g.completeopt = "menu,menuone,noselect,noinsert"
-- 样式
vim.o.background = "dark"
vim.o.termguicolors = true
vim.opt.termguicolors = true
-- 不可见字符的显示，这里只把空格显示为一个点
vim.o.list = true
vim.o.listchars = "space:·"
-- 补全增强
vim.o.wildmenu = true
-- Dont' pass messages to |ins-completin menu|
vim.o.shortmess = vim.o.shortmess .. 'c'
-- 补全最多显示10行
vim.o.pumheight = 10
-- 永远显示 tabline
vim.o.showtabline = 2
-- 使用增强状态栏插件后不再需要 vim 的模式提示
vim.o.showmode = false


```

这里用到的分类有

- `vim.g.{name}`: 全局变量
- `vim.b.{name}`: 缓冲区变量
- `vim.w.{name}`: 窗口变量
- `vim.bo.{option}`: buffer-local 选项
- `vim.wo.{option}`: window-local 选项

这样的分类初看上去是有些混乱的，有些时候想设置一个变量，确实很难判断应该放在哪个分类里。一般来说，全部设置在 `vim.opt` 下也是可以的，例如 `vim.opt.number = true` 也是有效的，只是我们上边设置到了比较详细位置而已，具体每个变量的分类可以在 :help 文档中查看。

不管怎么说， `basic.lua` 代码中都是一些非常常用的配置，基本上大家也都是这么配置的，所以如果你是新手的话，完全可以不用考虑太多，直接拷贝到你的配置里就可以了，当然我都写了注释，你也可以根据你的习惯不断进行微调，比如你喜欢使用 TAB 还是 SPACE，缩进2个空格还是4个空格等。需要注意的是一些重点设置项，接下来我们来看下。

## 重点设置项

默认情况下，编辑器底部会以文本方式显示当前模式如： `-- INSERT --` ， `-- VISUAL --` 等。

![5.gif](b386d4d893b24b4abed50c24f789c5batplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

`vim.o.showmode = false` 表示关闭显示，这里是固定设置，因为我们后边章节会添加增强显示的插件，已经包含了其功能，如图：

![6.gif](38a601a67d084e67a7abae59fe28366ftplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

同样的， `vim.o.showtabline = 2` 也是固定设置，表示永远显示 tabline，因为后边也有对应的 tabline 插件，`vim.o.hidden = true` 在使用多个 buffer的时候是必需的，表示允许隐藏被修改过的 buffer。 否则会报 E37: No write since last change 错误，强制你保存当前buffer后才允许切换到其他的 buffer。

同样的还有 `vim.g.completeopt = "menu,menuone,noselect,noinsert"`，后边自动补全插件会用到。而 `vim.wo.signcolumn = "yes"` 会让左侧留出一列，用于符号显示，所以不建议修改。

下边两行代码用于控制不可见字符的显示。

```lua
vim.o.list = true
vim.o.listchars = "space:·"
```

我这里习惯把不可见空格显示为一个点，这样很容易看清哪里有空格，你如果不喜欢可以设置为 false 关闭。

`timeoutlen `这个参数 **非常重要**，在 VIM 快捷键中经常有多个键连敲的情况，下边代码表示键盘快捷键连击时限设为500毫秒，超过500毫秒就不认为是连续快捷键了。

```
vim.o.timeoutlen = 500
```

如果你的手速很慢经常按不出快捷键，则建议加大这个数值。如果你的手速很快，可以把时间设置得更短。我看过有些高手会设置为 300。

`:wq` 保存文件，重启后的 Neovim 就具备基础配置了。

好，到此，我们已经完成了编码需要的基础环境设置，为后续章节的配置打好了基础。

高效编码的关键是快捷键的使用，快捷键也是 VIM 的核心，那么在 Neovim 中如何配置快捷键呢？还有哪些高效的快捷键技巧呢？下一节将会介绍 Neovim 配置快捷键配置，解答上述的疑问。

> 配置中如遇任何问题，可到 [github.com/nshen/learn…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 参考最终源码

# 4.如何设置快捷键以提高开发效率？

快捷键是提高开发效率的关键。在 Neovim 中， `Normal` 模式本身就是快捷键模式，而我们在这里说的快捷键相当于是 **快捷键的快捷键**，比如把某些按键映射成其他快捷键，或者映射成几个连续的快捷键的点击用来简化操作。 又或者映射到某个内置命令上，或者以某一个字母开头，抽象出一系列常用的快捷键组合。还可以为安装的插件设置快捷的打开方式。

这里的玩法可以非常多，每个人的习惯都不同，在 `Neovim` 中，你不需要强记软件的快捷键，只要把你的习惯告诉 `Neovim` 就行了。

例如我把分屏相关的操作，都设置以 `s` 开头 (Split)，组成一系列命令， `sh` 代表水平分屏（Split Horizontally），`sv` 代表垂直分屏 (Split Vertically）， `sc` 关闭窗口 (Close)， `so` 关闭其他 (Others)。 同时我也习惯把 `Alt + h/j/k/l` 设置为在窗口之间跳转。

下图演示：

![4-1.gif](1dd0fbf36e6f4fbb8586891ce2bf5f4dtplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

这样经过简单的配置，就把窗口管理提升到了 `VSCode` 无法达到的高度，而在 `VSCode` 中想达到同样的效果，就离不开键盘和鼠标的操作了。

我甚至还设置了改变窗口比例的快捷键，这里就先不演示了。

除了可以在 `Normal` 模式下设置快捷键，其他模式也可以设置快捷键，例如下边演示一个在 `Visual` 模式下比较实用的快捷键，选中并挪动多行代码：

![4-2.gif](c20f67d37cba446497fa37496c868cedtplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

除了上述的小技巧，我们后续要安装的大量插件也都需要快捷键设置，所以本节课除了要学习如何在 `Neovim` 中设置快捷键外，还要了解如何把所有快捷键都放在一个配置文件中管理，方便我们后续查找和修改，那么我们开始吧。

## 如何在 Neovim 中设置快捷键？

在 Neovim 中使用以下方法设置快捷键：

- `vim.api.nvim_set_keymap()` 全局快捷键
- `vim.api.nvim_buf_set_keymap()` Buffer 快捷键

一般情况下，都是定义使用全局快捷键， Buffer 快捷键一般是在某些异步回调函数里指定，例如某插件初始化结束后，会有回调函数提供 Buffer，这个时候我们可以只针对这一个 Buffer 设置快捷键。

关于 Buffer 快捷键部分，我们后边课程会遇到，这里先看全局设置。

```lua
vim.api.nvim_set_keymap('模式', '按键', '映射为', 'options')
```

这里 **模式** 参数用一个字母表示，常见的有：

- **n** Normal 模式
- **i** Insert 模式
- **v** Visual 模式
- **t** Terminal 模式
- **c** Command 模式

**按键** 就是你按下的键，没什么说的。

**映射为** 可以是多个按键组合，比如 `5j` 就是连续点击`5`和`j`， 也可以是一条命令比如 `:q<CR>`，表示退出。

**options** 大部分会设置为 `{ noremap = true, silent = true }`。`noremap` 表示不会重新映射，比如你有一个映射 `A` -> `B` , 还有一个 `B` -> `C`，这个时候如果你设置 `noremap = false` 的话，表示会重新映射，那么 `A` 就会被映射为 `C`。`silent` 为 `true`，表示不会输出多余的信息。

下边我们开始实践一下。

创建 `lua/keybindings.lua` 文件，我们会统一在这个文件里设置快捷键。

在设置之前，先选定一个 Leader 键。

## Leader Key

`leader key` 是你常用的前缀，我通常设置为 `空格`。

```lua
vim.g.mapleader = " "
vim.g.maplocalleader = " "
```

后边定义快捷键看到 `<leader>` 就表示 `空格` 。

由于要设置很多快捷键，所以先保存本地变量。

```lua
local map = vim.api.nvim_set_keymap
-- 复用 opt 参数
local opt = {noremap = true, silent = true }
```

之后就可以这样映射按键了 `map('模式', '按键', '映射为', 'options')` 。

## 窗口管理快捷键映射

添加代码，实现篇首提到的窗口管理功能。

```lua
-- 取消 s 默认功能
map("n", "s", "", opt)
-- windows 分屏快捷键
map("n", "sv", ":vsp<CR>", opt)
map("n", "sh", ":sp<CR>", opt)
-- 关闭当前
map("n", "sc", "<C-w>c", opt)
-- 关闭其他
map("n", "so", "<C-w>o", opt)
-- Alt + hjkl  窗口之间跳转
map("n", "<A-h>", "<C-w>h", opt)
map("n", "<A-j>", "<C-w>j", opt)
map("n", "<A-k>", "<C-w>k", opt)
map("n", "<A-l>", "<C-w>l", opt)
```

水平分屏很常用，比如，通常在程序开发中会有跳转到定义 `gd` 快捷键(Go Definition 在后续 LSP 章节会提供)，这个可以和 `sv` 组合起来，形成 `svgd` 命令，相当于打开右侧窗口进入方法的定义。看完可以随手 `sc` 关闭掉，非常方便。

我还增加了调整窗口比例快捷键，使用 `Ctrl + 上下左右` 或者 `s,` `s.` `sj` `sk` 调整比例。

```lua
-- 左右比例控制
map("n", "<C-Left>", ":vertical resize -2<CR>", opt)
map("n", "<C-Right>", ":vertical resize +2<CR>", opt)
map("n", "s,", ":vertical resize -20<CR>", opt)
map("n", "s.", ":vertical resize +20<CR>", opt)
-- 上下比例
map("n", "sj", ":resize +10<CR>", opt)
map("n", "sk", ":resize -10<CR>", opt)
map("n", "<C-Down>", ":resize +2<CR>", opt)
map("n", "<C-Up>", ":resize -2<CR>", opt)
-- 等比例
map("n", "s=", "<C-w>=", opt)
```

顺便扩展到 `Terminal` 模式也设置一下，`Neovim` 内置的命令行要用`<C-\><C-N>` 退出，我们把它映射为 `ESC` ，并用 `leader + t` 在下边窗口打开，或 `leader + vt` 侧边窗口打开。

```lua
-- Terminal相关
map("n", "<leader>t", ":sp | terminal<CR>", opt)
map("n", "<leader>vt", ":vsp | terminal<CR>", opt)
map("t", "<Esc>", "<C-\\><C-n>", opt)
map("t", "<A-h>", [[ <C-\><C-N><C-w>h ]], opt)
map("t", "<A-j>", [[ <C-\><C-N><C-w>j ]], opt)
map("t", "<A-k>", [[ <C-\><C-N><C-w>k ]], opt)
map("t", "<A-l>", [[ <C-\><C-N><C-w>l ]], opt)
```

![4-3.gif](075e9b3d0c404215ba3e2fe8fa84b53btplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

## Visule 模式下快捷键

在 visual 模式下可以`J` `K` 上下移动代码，又增加了连续 `>` 或 `<` 缩进代码。

```lua
-- visual模式下缩进代码
map("v", "<", "<gv", opt)
map("v", ">", ">gv", opt)
-- 上下移动选中文本
map("v", "J", ":move '>+1<CR>gv-gv", opt)
map("v", "K", ":move '<-2<CR>gv-gv", opt)
```

map 的第一个参数 `v` 表示 visual 模式。

## 浏览代码快捷键

我还有小技巧，比如在浏览非常长的代码文件时，通常要用 `Ctrl+u` / `Ctrl + d` 来滚动代码，`u` 和 `p` 表示 `up翻页` 和 `down翻页`。

但是`ctrl + u` / `ctrl + d` 默认移动半屏，翻太快，一不留神就不知道翻到哪了， `j` / `k` 又移动得太慢了。这时我会设置两种不同级别的翻页距离， `Ctrl+j` / `Ctrl+k` 移动 4 行，`Ctrl+u` / `Ctrl + d` 移动 9 行

![4-4.gif](e06e164f2de242dc9cf71904b8417cf3tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

```lua
-- 上下滚动浏览
map("n", "<C-j>", "4j", opt)
map("n", "<C-k>", "4k", opt)
-- ctrl u / ctrl + d  只移动9行，默认移动半屏
map("n", "<C-u>", "9k", opt)
map("n", "<C-d>", "9j", opt)
```

为什么是 4 行和 9 行呢？因为刚好适合我，尤其是命令行全屏的时候，刚好拉开两个级别，不多不少，但你应该根据你的情况设置。

我还有一些个人的设置，你可以参考。

```lua
-- 在visual 模式里粘贴不要复制
map("v", "p", '"_dP', opt)

-- 退出
map("n", "q", ":q<CR>", opt)
map("n", "qq", ":q!<CR>", opt)
map("n", "Q", ":qa!<CR>", opt)

-- insert 模式下，跳到行首行尾
map("i", "<C-h>", "<ESC>I", opt)
map("i", "<C-l>", "<ESC>A", opt)
```

最后，别忘了在 `init.lua` 入口文件里引入 `lua/keybindings.lua`，注意不要写 `.lua`

```lua
-- 快捷键映射
require("keybindings")
```

现在 `:wq` 退出重启后，之前设置的快捷键就生效了。

后续课程中的每个插件，如果需要设置快捷键，我们都会回来在`keybindings.lua`文件里继续添加。

不要担心你的`Neovim` 和我截图中的不一样，因为你还没有安装插件，也没有安装配色，下一节课我们会学习如何给 `Neovim` 添加和配置插件。

> 配置中如遇任何问题，可到 [github.com/nshen/learn…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 参考最终源码

# 5.如何安装和管理插件？

Neovim 可以通过扩展插件来添加新功能，或修改现有功能以增强开发体验。为了安装插件，需要先安装一个插件管理器，插件管理器可以安装，升级，卸载第三方插件。

目前在 Neovim 最常见的插件管理器主要有 [vim-plug](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjunegunn%2Fvim-plug) 和 [packer.nvim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwbthomason%2Fpacker.nvim) 两个。

一个好插件管理器，最重要是常用的插件都支持。 现在 Neovim 常用插件的 github 主页上，一般都会同时有 vim-plug 和 Packer.nvim 的安装的说明。

vim-plug 的特点是使用简单，并且同时支持 Vim 和 Neovim，所有功能在一个 VIM 脚本中实现了。

而 Packer.nvim 是后起之秀，但功能更为强大，支持插件间的依赖，指定 commit 版本，Post-install/update hooks，指定分支等功能，使用全 lua 编写，是专门针对最新 Neovim v0.5.0 以上版本设计的，所以推荐使用。

本节将选用 Packer.nvim 作为插件管理器，首先我们看一下如何安装 Packer.nvim。

## 安装 Packer.nvim 插件管理器

由于 Neovim 的插件默认都是通过 Github 进行安装的，所以我们需要保证网络环境是可以联通 Github 的。

根据官网的说明，在 Terminal 终端中输入以下命令，回车，安装 packer.nvim：

```
git clone --depth 1 https://github.com/wbthomason/packer.nvim\
 ~/.local/share/nvim/site/pack/packer/start/packer.nvim
```

安装成功后，我们添加一个新的配置文件，专门用于管理插件，新建 `lua/plugins.lua` 为如下代码：

```lua
local packer = require("packer")
packer.startup(
  function(use)
   -- Packer 可以管理自己本身
   use 'wbthomason/packer.nvim'
   -- 你的插件列表...
end)
```

我们通常使用 `use 'name/repo'` 来安装插件，`name/repo` 对应`github` 的地址。例如上边代码中的 `use 'wbthomason/packer.nvim'`，对应的就是 `https://github.com/wbthomason/packer.nvim` 地址。

我们之前说过，安装插件要求你有一个稳定可联通 Github 的网络环境，如果你的网络不好，可以尝试设置第二个 config 参数，使用代理站点。

下边代码中我列出了目前常见的几个代理站点，供你尝试，但还是推荐使用 Github， 因为代理站点有些冷门的插件有可能没有同步，或者同步不及时，也有可能有并发数限制等，体验并不是很好。

```lua
local packer = require("packer")
packer.startup({
  function(use)
    -- Packer 可以管理自己本身
    use 'wbthomason/packer.nvim'
    -- 你的插件列表...
  end,
  config = {
    -- 并发数限制
    max_jobs = 16,
    -- 自定义源
    git = {
      -- default_url_format = "https://hub.fastgit.xyz/%s",
      -- default_url_format = "https://mirror.ghproxy.com/https://github.com/%s",
      -- default_url_format = "https://gitcode.net/mirrors/%s",
      -- default_url_format = "https://gitclone.com/github.com/%s",
    },
  },
})
```

`config` 中还有很多参数，具体可参考帮助文档，比较实用的还有，以浮动窗口打开安装列表：

```lua
config = {
    display = {
        open_fn = function()
            return require("packer.util").float({ border = "single" })
        end,
    },
}
```

配置完成后，`:wq` 保存文件并退出。

别忘了想要这个配置文件生效，必须在 **入口文件** 中引入才可以， 打开 `init.lua` 增加如下代码：

```lua
-- Packer 插件管理
require("plugins")
```

再次 `:wq` 后，配置生效。

配置生效后，Neovim 会增加以下命令。

- `:PackerCompile`： 每次改变插件配置时，必须运行此命令或 `PackerSync`, 重新生成编译的加载文件
- `:PackerClean` ： 清除所有不用的插件
- `:PackerInstall` ： 清除，然后安装缺失的插件
- `:PackerUpdate` ： 清除，然后更新并安装插件
- `:PackerSync` : 执行 `PackerUpdate` 后，再执行 `PackerCompile`
- `:PackerLoad` : 立刻加载 opt 插件

通过上边的说明，我们观察到 `:PackerSync` 命令包含了 `:PackerUpdate` 和`:PackerCompile`，而 `:PackerUpdate` 又包含了 `:PackerClean` 和 `:PackerInstall` 流程。

所以通常情况下，无论**安装**还是**更新**插件，我只需要下边这一条命令就够了。

```
:PackerSync
```

每次修改完 `lua/plugins.lua` 这个文件后，保存退出，重新打开并调用 `:PackerSync` 就可以了，只要你的网络可以连接到 `github`，插件就会安装成功。

安装完成， 按 `q` 退出，如图演示：

![5-1.gif](2d7b2baa9a4d48968ee08fc8190a5674tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

由于我们没有增加新的插件，所以上图显示为 `Everything already up to date!`，这是因为 `Packer` 已经检查过了，并且没有发现新的插件。

目前你的界面应该和上图类似，还是比较丑的，这是因为还没有安装主题 `colorscheme`，不要着急，我们会在下一节中详细讲解，在此之前我们先看一下插件安装在哪了。

## 安装位置

Neovim 推荐将数据存储在 **标准数据目录**下（`:h base-directories` 查看详细文档），**标准数据目录**默认是 `~/.local/share/nvim/` ，你可以通过调用 `:echo stdpath("data")` 命令查看你系统下的实际路径。

`Packer` 会将插件默认安装在 `标准数据目录/site/pack/packer/start` 中，完整目录也就是`~/.local/share/nvim/site/pack/packer/start` 目录下。

你现在可以进入这个目录，查看一下安装的插件，应该看到只安装了 `packer.nvim` 一个插件，后续安装的插件也都会出现在这个目录中。

之前我们讲了安装组件的流程为： 修改 `lua/plugins.lua` 文件，保存退出，重新打开并调用 `:PackerSync`。

其实如果你愿意的话，我们可以添加一条自动命令让每次保存 `lua/plugins.lua` 就自动安装组件。

## 添加自动安装

打开 `lua/plugins.lua` 文件，在最后添加：

```lua
-- 每次保存 plugins.lua 自动安装插件
pcall(
  vim.cmd,
  [[
    augroup packer_user_config
    autocmd!
    autocmd BufWritePost plugins.lua source <afile> | PackerSync
    augroup end
  ]]
)
```

这里的 `[[ ... ]]` 中间的部分是 VIM 脚本，因为 Neovim 还没有实现自动命令的 API，所以我们需要使用 `vim.cmd` 命令来执行这段脚本。

这段脚本的意思是 `BufWritePost` 事件时，如果改的是 `lua/plugins.lua` 文件，就自动重新加载并调用 `:PackerSync` 命令，这样就不用手动重启，可以自动安装插件了。

`pcall` 命令是一个 Lua 函数，它的作用是检查一个函数是否执行成功，如果执行成功，则返回 `true`，否则返回 `false` ，防止报错，后边遇到的时候还会再详细解释。

现在修改 `lua/plugins.lua` 后输入 `:w` 就会自动安装和更新插件了，赶快翻到下一节，一起试试吧。

> 配置中如遇任何问题，可到 [github.com/nshen/learn…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 参考最终源码

## 补充

如果`:PackerSync`提示`Failed`，手动在`/root/.local/share/nvim/site/pack/packer/start`目录下,，使用`git clone --depth 1 github路径`下载即可。

# 6.Neovim 主题配色与优秀主题推荐

本节课我们学习如何给 Neovim 设置主题配色来改变编辑器的外观，以及如何使用上一节课的 Packer.nvim 插件管理器安装第三方主题配色，什么样的主题可以被称为现代化的主题配色。 另外，我们也会介绍，如何找到合适的主题，最后我再来推荐我最喜欢的几大主题推荐, 你可以从中选择一个作为你的默认主题配色。

首先我们需要了解，Neovim 本身内置了一些主题配色，你可以通过 `:colorscheme Tab键` 命令来查看， 回车确认选中。 过程如下：

![6-1.gif](8950f36d147643b29571387a808622d8tplv-k3u1fbpfcp-zoom-in-crop-mark1304000-165061967302327.awebp)

这里列出的都是内置的 `colorscheme`，它们都保存在 `$VIMRUNTIME/colors/` 目录下。

你可以在 `Neovim` 中输入命令 `:echo $VIMRUNTIME` 来查看 `$VIMRUNTIME` 具体的路径，比如我的路径显示如下：

```
/usr/share/nvim/runtime/
```

![6-2.gif](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b47b5b326a414c56bd6047ace13fdae4~tplv-k3u1fbpfcp-zoom-in-crop-mark:1304:0:0:0.awebp?)

但通过这种方式选择的主题，在重启后就失效了。需要写入配置才可以保存，下边看一下如何写入配置。

## 配置主题

打开入口文件 `init.lua`，修改代码为：

```lua
-- 基础配置
require("basic")
-- Packer插件管理
require("plugins")
-- 快捷键映射
require("keybindings")
-- 主题设置 （新增）
require("colorscheme")
```

新建被引入的 `lua/colorscheme.lua` 文件，代码如下：

```lua
local colorscheme = "tokyonight"
local status_ok, _ = pcall(vim.cmd, "colorscheme " .. colorscheme)
if not status_ok then
  vim.notify("colorscheme " .. colorscheme .. " 没有找到！")
  return
end
```

简单解释一下，上边代码第一行，定义了一个 `colorscheme` 的变量，表示我们要设置的主题，注意其实这里我们使用的 `tokyonight` **并不存在**。

接下来的部分代码，我们又见到了 `pcall`。

```lua
local status_ok, _ = pcall(vim.cmd, "colorscheme " .. colorscheme)
```

`pcall` 在 Lua 中用于捕获错误，这句话如果不用`pcall` 的话，相当于：

```lua
vim.cmd('colorscheme '.. colorscheme)
```

Lua 语言中用 `..` 来连接两个字符串，上边已经声明了 `colorscheme` 变量也是一个字符串 `"tokyonight" `所以这里其实就等于调用 `:colorscheme tokyonight` 命令。 但如果这样直接调用命令，如果主题不存在，Neovim 就会直接崩溃报错找不到该主题，程序中也就没法知道主题是否设置成功了。

使用 `pcall` 的话就不同了，`pcall` 函数的返回的第一个参数是 `boolean` 类型表示状态，这句话的意思是，如果 `colorscheme` 执行成功，则返回 `true`，否则返回 `false`。

如果没有设置成功，我们就让它输出信息：

```lua
vim.notify("colorscheme " .. colorscheme .. " 没有找到！")
```

![6-3.png](3feb8936a6cc4f96b52b5de2f4cdd2a8tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

至此配置的部分就完成了，提示没有找到是因为 `tokyonight` 主题并不存在，如果把该值修改成已经存在的主题，比如 `ron` 就会设置成功了。

下边我们看看如何安装第三方主题。

## 安装第三方主题

打开 `lua/plugins.lua` 文件，增加 colorschemes 部分：

```lua
packer.startup({
  function(use)
    -- Packer 可以升级自己
    use("wbthomason/packer.nvim")
    --------------------- colorschemes --------------------
    -- tokyonight
    use("folke/tokyonight.nvim")
    -------------------------------------------------------

    -- 略...
})
```

`:w` 保存，如果顺利的话，会自动安装，完成后按 `q` 退出，重启后就可以看到 `tokyonight` 主题的样子了。如图：

![6-4.gif](e5a35990d60945d9b916e8c5d3970289tplv-k3u1fbpfcp-zoom-in-crop-mark1304000-16507631138653.awebp)

补充：

但通常不顺利，可以到插件目录下手动安装`git clone --depth 1 https://github.com/folke/tokyonight.nvim.git`

目录：`/root/.local/share/nvim/site/pack/packer/start`

![image-20221126150213983](image-20221126150213983.png)



通常我们都会选择专门为 Neovim 制作的第三方主题，因为它们大多都会支持基于 `TreeSitter` 的语法高亮（后续代码高亮章节会详细说明），我认为这是考量是否应该选择一个主题最基础也是重要的事。

也就是说，一个现代化的主题，必须支持 [nvim-treesitter](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-treesitter%2Fnvim-treesitter) 语法高亮。

nvim-treesitter 的官方 wiki 上列出了许多支持 Treesitter 的主题，如果你想寻找更多的主题配色，可以到 [nvim-treesitter wiki](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-treesitter%2Fnvim-treesitter%2Fwiki%2FColorschemes) 页里查看。

一个优秀的现代化主题的第二个特点，就是能支持很多流行 Lua 插件的配色。

比如刚刚安装的 [tokyonight](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffolke%2Ftokyonight.nvim) 主题，就支持非常多的 [Lua 插件](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffolke%2Ftokyonight.nvim%23plugin-support)，也是 Github 上星星最多的一款主题，我在这里强烈推荐，本书后续也将使用这款主题配色。

下边是我推荐的其他主题配色。

## 我最喜欢的主题推荐

这里是我最能找到的最喜欢的几个配色，你可以选择一款作为你的默认配色。

- tokyonight

移植自 Visual Studio Code [TokyoNight](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fenkia%2Ftokyo-night-vscode-theme) theme，我的最爱，目前 Github 上有 1.3k 星星。

![tokyonight.png](1b6b2482c1d14b6b9f34ef533a2526f0tplv-k3u1fbpfcp-zoom-in-crop-mark1304000-165061967302432.awebp)

- OceanicNext

Oceanic-Next 是受 [Oceanic Next for Sublime](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvoronianski%2Foceanic-next-color-scheme) 启发而制作的主题，但只是用到了基础色系，并不是直接移植，同时支持 Neovim 和 Vim 8，目前在 Github 上有接近1000个星星。

![oceanicNext.png](d1e2c08536324da7b90b96ab4f01bbf7tplv-k3u1fbpfcp-zoom-in-crop-mark1304000-165061967302534.awebp)

- gruvbox.nvim

是非常有名的配色 [gruvbox community](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fgruvbox-community%2Fgruvbox) 的 Lua 移植版本，支持 [treesitter](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-treesitter%2Fnvim-treesitter)。

![gruvbox.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f8ba6c15dc843bb819396890f8b4405~tplv-k3u1fbpfcp-zoom-in-crop-mark:1304:0:0:0.awebp?)

- zephyr

这是我非常非常喜欢的一款配色，作者还是中国人，可惜在某次 Treesitter 更新后就与该配色冲突了，如果你的动手能力强的话，可以参考此 [issues](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fglepnir%2Fzephyr-nvim%2Fissues%2F29) 自行修复，或者先关注，等待作者的修复吧。

![zephyr.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/641fccb5240f4b3fb5dbebb7f3e9e5ba~tplv-k3u1fbpfcp-zoom-in-crop-mark:1304:0:0:0.awebp?)

- nord

nrod 绝对可以称得上是现代化的主题配色，官网上列出了其支持非常非常多的第三方插件配色，但颜色偏素，我不是特别的喜欢。

![nord.png](3baeeb8d748f4709aff1910c74fcf53dtplv-k3u1fbpfcp-zoom-in-crop-mark1304000-165061967302538.awebp)

- onedark

onedark 这个名字不用说，任何编辑器里应该都见过，也是支持非常非常多第三方插件，以及 Treesitter 和 LSP。

![onedark.png](5e6fc8efeb404f66b1ff6fa8b997e58etplv-k3u1fbpfcp-zoom-in-crop-mark1304000-165061967302540.awebp)

- nightfox

一个插件包含多种配色 Nightfox / Nordfox / Dayfox / Dawnfox / Duskfox，支持非常多的第三方插件。并且有很多配置项，相对比较复杂。目前在 Github 上有600 多颗星星，是非常不错的选择。

![nightfox.png](d31961d706f146ed9953e49fa7dcf784tplv-k3u1fbpfcp-zoom-in-crop-mark1304000-165061967302542.awebp)

如果还是没有你喜欢的，你也可以到 Github 的 [neovim-colorscheme](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftopics%2Fneovim-colorscheme) 链接下找找你的最爱。

怎么样，选好了吗？ 要不，我们把上边推荐的所有主题一次全安装了吧？

修改 `lua/plugins.lua` 增加代码如下， 然后 `:w` 即可自动安装:

```lua
...
--------------------- colorschemes --------------------
-- tokyonight
use("folke/tokyonight.nvim")
-- OceanicNext
use("mhartington/oceanic-next")
-- gruvbox
use({ "ellisonleao/gruvbox.nvim", requires = { "rktjmp/lush.nvim" } })
-- zephyr 暂时不推荐，详见上边解释
-- use("glepnir/zephyr-nvim")
-- nord
use("shaunsingh/nord.nvim")
-- onedark
use("ful1e5/onedark.nvim")
-- nightfox
use("EdenEast/nightfox.nvim")
-------------------------------------------------------
...
```

然后找到你喜欢的样式后修改 `lua/colorscheme.lua` 内 `colorscheme` 变量的名字保存，重启后即可生效。

```lua
local colorscheme = "tokyonight"
```

下一章会开始给我们的 Neovim 装上侧边栏插件，如果没问题了就快来吧。

> 配置中如遇任何问题，可到 [github.com/nshen/learn…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 参考最终源码

# 7.如何给 Neovim 增加侧边栏文件浏览器？

本节课我们学习如何给 Neovim 增加一个侧边栏，也叫做文件浏览器，一般 IDE 默认都有，用于列出当前目录树。

可以方便地浏览目录结构，添加、删除、移动或者重命名文件，更快地打开文件。

![7-4.png](d9230327232f43f1a7f4d05f27b815d7tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

目前 [nvim-tree.lua](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkyazdani42%2Fnvim-tree.lua) 是最流行的全 Lua 编写的侧边栏插件，第一步安装，打开 `lua/plugins.lua`，增加：

```lua
packer.startup({
  function(use)
    -- Packer 可以升级自己
    use("wbthomason/packer.nvim")
    -------------------------- plugins -------------------------------------------
    -- nvim-tree (新增)，文件侧边栏
    use({ "kyazdani42/nvim-tree.lua", requires = "kyazdani42/nvim-web-devicons" })

...略
```

注意上边 `requires` 语法，表示 `nvim-tree.lua` 依赖 `nvim-web-devicons`，当安装组件的时候，两个组件都会安装。

`:w` 保存，自动安装，安装完成如图，按 `q` 退出。

![7-2.png](7e6f6aaefd514d2195b3dd442d93e47btplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

如果报错网络错误，可以重新运行 `:PackerSync` 。

插件安装完成，只表示下载成功。并不是说就可以直接使用了，每个插件都需要单独配置。

下边开始配置侧边栏。

也可到插件目录下手动安装

人家改名字了，但不影响（第一个我用新的名字，第二个还是用的老名字，都可以）

```bash
git clone --depth 1 https://github.com/nvim-tree/nvim-web-devicons.git

git clone --depth 1 https://github.com/kyazdani42/nvim-tree.lua.git
```



## 配置 nvim-tree

创建 `lua/plugin-config/nvim-tree.lua` 文件，添加如下内容：

```lua
local status, nvim_tree = pcall(require, "nvim-tree")
if not status then
    vim.notify("没有找到 nvim-tree")
  return
end
```

上边的代码相当于：

```lua
local nvim_tree = require'nvim-tree'
```

但是如果我们直接 `require` 一个插件，当这个插件不存在的时候，`Neovim` 就会崩溃，所以我这里使用 `pcall` 来捕获了错误，如果 `nvim-tree` 没有安装，我们就会直接 `return`，**不**再继续执行下边的配置。

由于我们经常会调整插件，所以应该尽量避免报错，后续的所有插件配置文件都会这么做。

继续增加代码：

```lua
local status, nvim_tree = pcall(require, "nvim-tree")
if not status then
    vim.notify("没有找到 nvim-tree")
  return
end

-- 列表操作快捷键
local list_keys = require('keybindings').nvimTreeList
nvim_tree.setup({
    -- 不显示 git 状态图标
    git = {
        enable = false,
    },
    -- project plugin 需要这样设置
    update_cwd = true,
    update_focused_file = {
        enable = true,
        update_cwd = true,
    },
    -- 隐藏 .文件 和 node_modules 文件夹
    filters = {
        dotfiles = true,
        custom = { 'node_modules' },
    },
    view = {
        -- 宽度
        width = 40,
        -- 也可以 'right'
        side = 'left',
        -- 隐藏根目录
        hide_root_folder = false,
        -- 自定义列表中快捷键
        mappings = {
            custom_only = false,
            list = list_keys,
        },
        -- 不显示行数
        number = false,
        relativenumber = false,
        -- 显示图标
        signcolumn = 'yes',
    },
    actions = {
        open_file = {
            -- 首次打开大小适配
            resize_window = true,
            -- 打开文件时关闭
            quit_on_open = true,
        },
    },
    -- wsl install -g wsl-open
    -- https://github.com/4U6U57/wsl-open/
    system_open = {
        cmd = 'wsl-open', -- mac 直接设置为 open
    },
})
-- 自动关闭
vim.cmd([[
  autocmd BufEnter * ++nested if winnr('$') == 1 && bufname() == 'NvimTree_' . tabpagenr() | quit | endif
]])
```

上边代码就是 nvim-tree 的配置，可以根据注释进行修改。这里简单解释一下，值得注意的是 `system_open` 项，如果想要在 `WSL` 中用 Windows 系统默认设置打开文件，需要使用 `Node.js` 全局安装一个 `wsl-open` 包，使用命令 `npm install -g wsl-open`，如果不需要这个功能，也可以不用安装。 如果不是 Windows 系统也就不需要安装。

nvim-tree 初始化支持很多参数，如果想知道还有哪些其他的参数，可以运行 `:h nvim-tree.setup` 调出帮助文档查看。

注意到上述代码第一行，引入了我们之前创建的 `lua/keybindings.lua`，并取出 `nvimTreeList` 变量作为快捷键设置， 那我们就看看 `keybinding` 中是如何导出这个变量的。

打开 `lua/keybindings.lua` 文件，增加如下代码：

```lua
-- 插件快捷键
local pluginKeys = {}

-- nvim-tree
map("n", "<A-n>", ":NvimTreeToggle<CR>", opt)
map("n", "<leader>n", ":NvimTreeToggle<CR>", opt)
-- 列表快捷键
pluginKeys.nvimTreeList = { 
  -- 打开文件或文件夹
  { key = {"<CR>", "o", "<2-LeftMouse>"}, action = "edit" },
  -- v分屏打开文件
  { key = "v", action = "vsplit" },
  -- h分屏打开文件
  { key = "h", action = "split" },
  -- Ignore (node_modules)
  { key = "i", action = "toggle_ignored" },
  -- Hide (dotfiles)
  { key = ".", action = "toggle_dotfiles" },
  { key = "R", action = "refresh" },
  -- 文件操作
  { key = "a", action = "create" },
  { key = "d", action = "remove" },
  { key = "r", action = "rename" },
  { key = "x", action = "cut" },
  { key = "c", action = "copy" },
  { key = "p", action = "paste" },
  { key = "y", action = "copy_name" },
  { key = "Y", action = "copy_path" },
  { key = "gy", action = "copy_absolute_path" },
  { key = "I", action = "toggle_file_info" },
  { key = "n", action = "tabnew" },
  -- 进入下一级
  { key = { "]" }, action = "cd" },
  -- 进入上一级
  { key = { "[" }, action = "dir_up" },
}





return pluginKeys
```

在上边代码中，我们首先在 Normal 模式下定义了一个`Alt + m` 的快捷键，调用 `:NvimTreeToggle<CR>` 命令，这个快捷键用来打开和关闭侧边栏。（补充：最后的配置文件中，还用了`空格键 + m`，可以回过头重新看一下第4小节）

`pluginKeys.nvimTreeList` 下则是在光标在列表中时的快捷键设置，比如用 `o` 来打开关闭文件夹，`a` 添加一个文件，`d` 删除文件等等。

代码的最后一行，我们 `return` 了一个 `lua table`， 类似 `Javascript`的 `object`，也叫关联数组。 当我们从其他文件 `require` 这个文件的时候，就会得到这个对象。

最后不要忘记在入口文件 `init.lua` 中引入配置：

```lua
-- 基础配置
require("basic")
-- Packer插件管理
require("plugins")
-- 快捷键映射
require("keybindings")
-- 主题设置
require("colorscheme")
-- 插件配置
require("plugin-config.nvim-tree")
```

重启 nvim 后，侧边栏就会生效了，使用 `Alt + m` 打开/关闭， `j/k` 上下移动， `Alt + h` / `Alt + l` 可以左右窗口跳转，演示如下：

![7-3.gif](4c9c8866ba5a45d791f382005075be25tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

注意：有的远程连接工具，如`WindTerm`它自己有`Alt + m`的快捷键，可以取消它的设置，或者设置成其他的。[windows Terminal 修改快捷键 - 简书 (jianshu.com)](https://www.jianshu.com/p/a1c067578b93)

我们这里不用`alt + m`，改成`alt +n`，并注意调整连接工具的显示大小，过大的话会有多余空行

![image-20221126153235138](image-20221126153235138.png)

超级酷的侧边栏，下一节课继续增加顶部标签栏和底部信息显示栏。

> 配置中如遇任何问题，可到 [github.com/nshen/learn…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 参考最终源码

# 8.如何给 Neovim 增加顶部标签页与底部信息显示栏？

本章介绍如何通过 [bufferline.nvim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fakinsho%2Fbufferline.nvim) 和 [lualine.nvim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-lualine%2Flualine.nvim) 插件给 Neovim 增加 **顶部标签页** 与 **底部信息显示** 栏。

首先看一下如何安装和配置 bufferline 插件。

`bufferline` 顾名思义是把 Neovim 的 `buffer` 图形化显示成类似 VSCode 中 标签页的形式，如下动图所示：

![8-2.gif](9fc23c0875884bcb8c38173b0edba40dtplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

常用 VSCode 的一定非常熟悉这个 Tab 页的概念，现在已经是代码编辑器的标配了，一个 Tab 用来表示一个打开的文件，很匹配 Neovim 中 `buffer` 的概念。

## 安装方法

第一步，打开 `lua/plugins.lua`，增加 `bufferline` 相关的代码：

```lua
packer.startup({
  function(use)
    -- Packer 可以升级自己
    use("wbthomason/packer.nvim")
    -------------------------- plugins -------------------------------------------
    -- nvim-tree
    use({ "kyazdani42/nvim-tree.lua", requires = "kyazdani42/nvim-web-devicons" })
    -- bufferline (新增)
    use({ "akinsho/bufferline.nvim", requires = { "kyazdani42/nvim-web-devicons", "moll/vim-bbye" }})

...略
```

`:w` 保存，自动安装，安装完整按 `q` 退出。 如果报错网络错误，可以重新运行 `:PackerSync` 。

这里我增加了一个 [vim-bbye](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmoll%2Fvim-bbye) 依赖，因为这个插件安装后会增加一个 `:Bdelete` 命令，相比内置的 `:bdelete`, 它删除 buffer 的同时，并不会搞乱布局 。 待会儿我们会配置 `Bdelete` 为关闭 Tab 的命令。

第二步，新建配置文件 `lua/plugin-config/bufferline.lua`，代码如下：

```lua
local status, bufferline = pcall(require, "bufferline")
if not status then
    vim.notify("没有找到 bufferline")
  return
end

-- bufferline 配置
-- https://github.com/akinsho/bufferline.nvim#configuration
bufferline.setup({
  options = {
    -- 关闭 Tab 的命令，这里使用 moll/vim-bbye 的 :Bdelete 命令
    close_command = "Bdelete! %d",
    right_mouse_command = "Bdelete! %d",
    -- 侧边栏配置
    -- 左侧让出 nvim-tree 的位置，显示文字 File Explorer
    offsets = {
      {
        filetype = "NvimTree",
        text = "File Explorer",
        highlight = "Directory",
        text_align = "left",
      },
    },
    -- 使用 nvim 内置 LSP  后续课程会配置
    diagnostics = "nvim_lsp",
    -- 可选，显示 LSP 报错图标
    ---@diagnostic disable-next-line: unused-local
    diagnostics_indicator = function(count, level, diagnostics_dict, context)
      local s = " "
      for e, n in pairs(diagnostics_dict) do
        local sym = e == "error" and " " or (e == "warning" and " " or "")
        s = s .. n .. sym
      end
      return s
    end,
  },
})
```

经过这样配置后，就基本跟 `VSCode` 中的标签页一样了，相关的说明见注释，更多的配置项可参考官网 [bufferline.nvim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fakinsho%2Fbufferline.nvim%23configuration) 配置项说明。

第三步，增加快捷键。 打开 `lua/keybindings.lua`，根据你的使用习惯增加键盘映射：

```lua
-- bufferline
-- 左右Tab切换
map("n", "<C-h>", ":BufferLineCyclePrev<CR>", opt)
map("n", "<C-l>", ":BufferLineCycleNext<CR>", opt)
-- 关闭
--"moll/vim-bbye"
map("n", "<C-w>", ":Bdelete!<CR>", opt)
map("n", "<leader>bl", ":BufferLineCloseRight<CR>", opt)
map("n", "<leader>bh", ":BufferLineCloseLeft<CR>", opt)
map("n", "<leader>bc", ":BufferLinePickClose<CR>", opt)
```

上述代码延续了我在 `VSCode` 中的使用习惯，使用 `Ctrl + h` 和 `Ctrl + l` 左右切换标签页， `Ctrl + w` 关闭当前标签页。

我又将 `bufferline` 提供的我不太常用到的命令，映射为由空格键开头， `<leader>bl` 关闭左侧标签页， `<leader>bh` 关闭右侧标签页， `<leader>bc` 选择要关闭的标签页。



**补充：**

做个笔记bufferline的快捷键要放到插件快捷键的上边，也就是你return pluginkeys这行代码的上边找个地方放

不然会报错！



最后一步，在入口文件中引入配置文件。 打开 `init.lua`，增加代码：

```lua
require("plugin-config.bufferline")
```

`:wq` 保存退出，重启后安装生效。

下面开始安装底部状态信息显示栏。

## 底部信息显示栏

底部状态栏用于显示一些额外信息，比如当前的编辑模式，光标所在的行号，列号。当前文件大小，编码格式，当前 `git` 分支等状态，如下图所示。

![8-1.png](c1097b4cce304631a5f71fdd4f4f06e5tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

我在这里选择了 [lualine.nvim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-lualine%2Flualine.nvim) 插件。

第一步安装，打开 `lua/plugins.lua`， 增加 `lualine` 相关代码：

```lua
packer.startup({
  function(use)
    -- Packer 可以升级自己
    use("wbthomason/packer.nvim")
    -------------------------- plugins -------------------------------------------
    -- nvim-tree
    use({ "kyazdani42/nvim-tree.lua", requires = "kyazdani42/nvim-web-devicons" })
    -- bufferline
    use({ "akinsho/bufferline.nvim", requires = { "kyazdani42/nvim-web-devicons", "moll/vim-bbye" }})
    -- lualine (新增)
    use({ "nvim-lualine/lualine.nvim", requires = { "kyazdani42/nvim-web-devicons" } })
    use("arkav/lualine-lsp-progress")
    ... 略
```

注意这里新增了两行，第二行是 `lualine` 的一个扩展，`:w` 保存，自动安装，安装完整按 `q` 退出。 如果报网络错误，可以重新运行 `:PackerSync` 。

第二步，新建配置文件 `lua/plugin-config/lualine.lua`，代码如下：（补充：有特殊字符，直接复制的源文件）

```lua
-- 如果找不到lualine 组件，就不继续执行
local status, lualine = pcall(require, "lualine")
if not status then
    vim.notify("没有找到 lualine")
  return
end

lualine.setup({
  options = {
    theme = "tokyonight",
    component_separators = { left = "|", right = "|" },
    -- https://github.com/ryanoasis/powerline-extra-symbols
    section_separators = { left = " ", right = "" },
  },
  extensions = { "nvim-tree", "toggleterm" },
  sections = {
    lualine_c = {
      "filename",
      {
        "lsp_progress",
        spinner_symbols = { " ", " ", " ", " ", " ", " " },
      },
    },
    lualine_x = {
      "filesize",
      {
        "fileformat",
        -- symbols = {
        --   unix = '', -- e712
        --   dos = '', -- e70f
        --   mac = '', -- e711
        -- },
        symbols = {
          unix = "LF",
          dos = "CRLF",
          mac = "CR",
        },
      },
      "encoding",
      "filetype",
    },
  },
})
```

lualine 的配置参数主要有 `options`，`extensions` 和 `sections` 三块。

`options` 用于设置样式， 其中 `theme` 设置主题配色，可以设置为 `auto`， 也可以设置为[主题列表](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-lualine%2Flualine.nvim%2Fblob%2Fmaster%2FTHEMES.md)中的一个， 我这里设置的是 `tokyonight`，是由 tokyonight 主题配色额外提供的支持。`section_separators` 设置分段分隔符`， component_separators` 设置分段中的组件分隔符。

`extensions` 用于设置 `lualine` 支持的扩展，详见[扩展列表](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-lualine%2Flualine.nvim%23extensions) 这里我们只会用到 `nvim-tree` 和 `toggleterm` 。

`sections` 用于设置不同分段，所需显示的功能模块， 分段有 6 个，分别为： `A B C X Y Z` 。

```text
+-------------------------------------------------+
| A | B | C                             X | Y | Z |
+-------------------------------------------------+
```

对应默认配置项为：

```lua
 sections = {
    lualine_a = {'mode'},
    lualine_b = {'branch', 'diff', 'diagnostics'},
    lualine_c = {'filename'},
    lualine_x = {'encoding', 'fileformat', 'filetype'},
    lualine_y = {'progress'},
    lualine_z = {'location'}
  },
```

我的配置中，修改了 `C` 的部分：

```lua
    lualine_c = {
      "filename",
      {
        "lsp_progress",
        spinner_symbols = { " ", " ", " ", " ", " ", " " },
      },
    },
```

在文件名后边增加了 `lsp_progress` 进度显示，该信息是由我们之前安装的 [arkav/lualine-lsp-progress](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Farkav%2Flualine-lsp-progress) 提供的。

我还修改了 `X` 的部分， 因为 `lualine` 默认的 `fileformat` 是用图标表示的，不是很直观，我换成了和 `VSCode` 一致的 `LF/CRLF/CR` 格式。

```lua
    lualine_x = {
      "filesize",
      {
        "fileformat",
        -- symbols = {
        --   unix = '', -- e712
        --   dos = '', -- e70f
        --   mac = '', -- e711
        -- },
        symbols = {
          unix = "LF",
          dos = "CRLF",
          mac = "CR",
        },
      },
      "encoding",
      "filetype",
    },
```

由于该插件并不需要定义快捷键，所以我们执行最后一步，在**入口文件**中引入配置文件。 打开 `init.lua`，增加代码：

```lua
require("plugin-config.lualine")
```

`:wq` 保存退出，重启后安装生效。

目前已经安装 3 个插件，完整的 `init.lua` 文件如下：

```lua
-- 基础配置
require("basic")
-- Packer插件管理
require("plugins")
-- 快捷键映射
require("keybindings")
-- 主题设置
require("colorscheme")
-- 插件配置
require("plugin-config.nvim-tree")
require("plugin-config.bufferline")
require("plugin-config.lualine")
```

除了在侧边栏树形列表中打开文件，如果你熟悉 VSCode 那么你一定经常使用 `Ctrl + p` 快捷键快速打开文件，下一节课我们会给 Neovim 增加一个同样类似的快速打开文件的功能。

> 配置中如遇任何问题，可到 [github.com/nshen/learn…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 参考最终源码

# 9.如何模糊搜索快速打开文件？

在写代码的时候，经常会想要打开一个文件，但却不记得完整的文件名，只记得部分文件名或者隐约只记得里边写过的代码。这个时候如何快速找到并打开这个文件呢？

使用之前章节中定义的`Alt + m` 打开 nvim-tree 目录树查找？不，这个时候你需要的是一个模糊查询工具。

我在使用 VSCode 的时候经常使用中内置的模糊查找 `Ctrl + p` 来查找文件，使用 `Ctrl + shift + f` 来全局查找，非常方便，我已经形成了肌肉记忆，所以这节课我们要给 Neovim 也增加这样的的功能。

如果你也跟我一样需要一个模糊查询工具，那么就跟着我一起安装 [telescope.nvim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-telescope%2Ftelescope.nvim) 插件吧。

先看一下使用 `telescope` 模糊查找文件的样子，打开窗口以后有一个输入框，随着内容的输入会实时在结果框中显示搜索结果，使用快捷键在结果框中选择，右侧会实时显示文件预览，非常酷炫。

![telescope.gif](567f9023338b4a77b6f35716516ec2c6tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

看一下安装方法，打开 `lua/plugins.lua` 文件，新增 `telescope` 相关的内容：

```lua
...
packer.startup({
  function(use)
    -- Packer 可以升级自己
    use("wbthomason/packer.nvim")
    -------------------------- plugins -------------------------------------------
    -- nvim-tree
    use({ "kyazdani42/nvim-tree.lua", requires = "kyazdani42/nvim-web-devicons" })
    -- bufferline
    use({ "akinsho/bufferline.nvim", requires = { "kyazdani42/nvim-web-devicons", "moll/vim-bbye" }})
    -- lualine
    use({ "nvim-lualine/lualine.nvim", requires = { "kyazdani42/nvim-web-devicons" } })
    use("arkav/lualine-lsp-progress")
    -- telescope （新增）
    use { 'nvim-telescope/telescope.nvim', requires = { "nvim-lua/plenary.nvim" } }
...
```

`:w` 保存，自动安装，安装完成按 `q` 退出。 如果报网络错误，可以重新运行 `:PackerSync` 。

安装完成后，需要调用 `:checkhealth telescope` 检查依赖情况，这里通常会提示 `ripgrep` 不存在，因为 `telescope` 依赖以下项目。（补充：我这边竟然两个都有了）

- [BurntSushi/ripgrep](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FBurntSushi%2Fripgrep)
- [sharkdp/fd](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsharkdp%2Ffd)

需要根据你的系统选择对应的安装方法，由于我们这里使用了 WSL2 子系统 Ubuntu 18.04，所以最简单的安装方式是在命令行中使用下列命令安装。

## 安装 repgrep

添加 `ppa` 后安装 `ripgrep` ：

```bash
sudo add-apt-repository ppa:x4121/ripgrep
sudo apt-get update
sudo apt install ripgrep
```

依次运行上边代码即可安装完成。

## 安装 fd

`fd` 的话，我找到最简单的安装方法是使用 `npm` 直接全局安装，注意 `npm` 需要 `Node.js` 环境。

```
npm install -g fd-find
```

全部安装后，可以开始配置 `Telescope` 了。

## 配置 Telescope

再次运行 `:checkhealth telescope`，如图，依赖都已经安装完成：

![9-1.png](92f2feaad2c74b19a12bdc2927bd4951tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

无需理会这里提示的 `nvim-treesitter` 没有找到，我们后边代码高亮章节才会安装。

至此，`telescope` 就安装完成了，可以运行命令 `:Telescope find_files` 打开搜索文件窗口，快速打开文件。

除此之外，还有一个常用的功能是全局查找，`:Telescope live_grep` 可以打开搜索窗口，输入内容后，结果会实时显示。

![9-2.gif](7b4be58055014d08980d51509497871dtplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

接下来将这两个常用功能定义为快捷键，打开 `lua/keybindings.lua`，根据你的使用习惯增加键盘映射。

## 快捷键配置

```lua
-- Telescope
-- 查找文件
map("n", "<C-p>", ":Telescope find_files<CR>", opt)
-- 全局搜索
map("n", "<C-f>", ":Telescope live_grep<CR>", opt)
```

这里我定义了 `Ctrl + p` 为 `:Telescope find_files`命令，和 `VSCode` 一样。 但 `Neovim` 中没办法设置 `Ctrl + shift + f` 快捷键，所以我设置了 `Ctrl + f` 为 `:Telescope live_grep` 全局查找。

默认情况下打开窗口就会进入输入模式，这个时候和在普通编辑器一样，可以按 `ESC` 键进入 `Normal` 模式，然后 `j/k` 在文件列表里上下浏览， 按 `i` 或 `a` 回到 `Insert` 模式，按 `ESC` 退出。

除了默认的快捷键以外，`Telescope` 还支持在打开的窗口中自定义快捷键，打开 `lua/keybindings.lua` 继续添加：

```lua
-- Telescope 列表中 插入模式快捷键
pluginKeys.telescopeList = {
  i = {
    -- 上下移动
    ["<C-j>"] = "move_selection_next",
    ["<C-k>"] = "move_selection_previous",
    ["<Down>"] = "move_selection_next",
    ["<Up>"] = "move_selection_previous",
    -- 历史记录
    ["<C-n>"] = "cycle_history_next",
    ["<C-p>"] = "cycle_history_prev",
    -- 关闭窗口
    ["<C-c>"] = "close",
    -- 预览窗口上下滚动
    ["<C-u>"] = "preview_scrolling_up",
    ["<C-d>"] = "preview_scrolling_down",
  },
}
```

**注意，这个要配置在`pluginKeys`的声明后面，在`return`之前**



这样在插入模式下按 `Ctrl + j` / `Ctrl +k` 就可以在文件列表中上下切换了，不再需要切回 `Normal` 模式了。

当然这个快捷键还没有生效，因为我们还没有创建 `telescope` 的配置文件。

## 配置 telescope 插件

新建配置文件 `lua/plugin-config/telescope.lua`，代码如下：

```lua
local status, telescope = pcall(require, "telescope")
if not status then
  vim.notify("没有找到 telescope")
  return
end

telescope.setup({
  defaults = {
    -- 打开弹窗后进入的初始模式，默认为 insert，也可以是 normal
    initial_mode = "insert",
    -- 窗口内快捷键
    mappings = require("keybindings").telescopeList,
  },
  pickers = {
    -- 内置 pickers 配置
    find_files = {
      -- 查找文件换皮肤，支持的参数有： dropdown, cursor, ivy
      -- theme = "dropdown", 
    }
  },
  extensions = {
     -- 扩展插件配置
  },
})
```

简单解释一下上边代码，在 `mappings` 部分引入了我们刚才在 `lua/keybindings.lua` 中定义的快捷键 `telescopeList`，这样定义才会生效。

我们可以尝试把查找文件的 picker 也就是 `Ctrl + p` 打开的窗口换一个皮肤，比如 `dropdown` 这个皮肤是把窗口垂直排列了，内置的皮肤还有 `cursor` 让窗口在光标位置打开， `ivy` 则是全屏覆盖的。建议你自己手动试试，看看喜欢哪种效果。

Telescope 非常强大，内置了很多的 pickers，比如 `:Telescope buffers` 命令可以列出打开的 buffers， `:Telescope git_files` 列出 git 文件，`:Telescope man_pages` 列出帮助等等。

你可以在命令补全里看到这些支持的 pickers。

![9-4.gif](ea6b3e7dc16d4b6cbc426df12ba36b73tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

更多内置 pickers 可以参考 [官网说明](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-telescope%2Ftelescope.nvim%23pickers)。

最后别忘了在 **入口文件** 中引入配置文件才能生效。 打开 `init.lua`，增加代码：

```lua
require("plugin-config.telescope")
```

`:wq` 保存退出，重启后安装生效。

除了内置的还可以安装第三方扩展，下边就演示一下如何安装扩展。

## Telescope 扩展安装

Telescope 支持非常多的第三方扩展，列表见下边链接：

[github.com/nvim-telesc…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-telescope%2Ftelescope.nvim%2Fwiki%2FExtensions)

下边通过一个简单的扩展，演示如何安装扩展。

要安装的扩展叫做 [telescope-env.nvim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLinArcX%2Ftelescope-env.nvim) 用于列出系统环境变量，如图：

![9-3.png](f735982ddd12419eaeda8a8e9fedac62tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

打开 `lua/plugins.lua` 文件，新增 `telescope-env.nvim` 相关的内容：

```lua
-- telescope extensions
use "LinArcX/telescope-env.nvim"
```

`:w` 保存，自动安装，安装完成后，打开 `lua/plugin-config/telescope.lua` 文件，在文件最后新增：

```lua
-- telescope extensions
pcall(telescope.load_extension, "env")
```

重启后，就可以调用 `:Telescope env` 命令，打开环境变量列表了。

Telescope 就这么多内容了，下一节课是 **基建篇** 的最后一节，我们会看看如何给 Neovim 增加一个漂亮的启动页和项目列表。

> 配置中如遇任何问题，可到 [github.com/nshen/learn…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 参考最终源码

# 10.如何自定义启动页与项目列表？

本节课会介绍如何给 Neovim 增加一个自定义启动画面，并列出常用功能，如图所示：

![10-3.png](70bf0cddda5e47d59c27e59b2164ed5etplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

当我们在命令行中输入 `nvim` 不带任何路径并敲击回车的时候，就会打开这个界面，通常我们会在这个界面中配置最常用功能，比如打开最近编辑过的文件，快速打开项目文件夹，快速修改快捷键等。

最重要的是，我们要自定一个酷酷的 Banner ，表示这是我们独一无二的版本，接下来我会教你如何定义。 首先需要安装 [dashboard-nvim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fglepnir%2Fdashboard-nvim) 插件

## 安装 dashboard-nvim 插件

修改 `lua/plugins.lua` 文件中添加 `glepnir/dashboard-nvim` 插件：

```lua
...

packer.startup({
  function(use)
    -- Packer 可以升级自己
    use("wbthomason/packer.nvim")
    -------------------------- plugins -------------------------------------------
    -- nvim-tree
    use({"kyazdani42/nvim-tree.lua", requires = "kyazdani42/nvim-web-devicons" })
    -- bufferline
    use({"akinsho/bufferline.nvim", requires = { "kyazdani42/nvim-web-devicons", "moll/vim-bbye" }})
    -- lualine
    use({"nvim-lualine/lualine.nvim", requires = { "kyazdani42/nvim-web-devicons" } })
    use("arkav/lualine-lsp-progress")
    -- telescope
    use ({"nvim-telescope/telescope.nvim", requires = { "nvim-lua/plenary.nvim" } })
    -- telescope extensions
    use "LinArcX/telescope-env.nvim"
    -- dashboard-nvim (新增)
    use("glepnir/dashboard-nvim")

...
```

`:w` 保存，自动安装，安装完整按 `q` 退出。 如果报错网络错误，可以重新运行 `:PackerSync` 。

接着第二步创建配置文件 `lua/plugin-config/dashboard.lua`，添加如下内容：

```lua
vim.g.dashboard_default_executive = "telescope"
vim.g.dashboard_custom_footer = { "https://github.com/nshen/learn-neovim-lua" }

vim.g.dashboard_custom_section = {
  a = { description = { "  Projects              " }, command = "Telescope projects" },
  b = { description = { "  Recently files        " }, command = "Telescope oldfiles" },
  c = { description = { "  Edit keybindings      " }, command = "edit ~/.config/nvim/lua/keybindings.lua" },
  d = { description = { "  Edit Projects         " }, command = "edit ~/.local/share/nvim/project_nvim/project_history", },
  -- e = { description = { "  Edit .bashrc          " }, command = "edit ~/.bashrc" },
  -- f = { description = { "  Edit init.lua         " }, command = "edit ~/.config/nvim/init.lua" },
  -- g = { description = {'  Find file          '}, command = 'Telescope find_files'},
  -- h = { description = {'  Find text          '}, command = 'Telescope live_grep'},
}

vim.g.dashboard_custom_header = {
  [[ ███╗   ██╗███████╗ ██████╗ ██╗   ██╗██╗███╗   ███╗]],
  [[ ████╗  ██║██╔════╝██╔═══██╗██║   ██║██║████╗ ████║]],
  [[ ██╔██╗ ██║█████╗  ██║   ██║██║   ██║██║██╔████╔██║]],
  [[ ██║╚██╗██║██╔══╝  ██║   ██║╚██╗ ██╔╝██║██║╚██╔╝██║]],
  [[ ██║ ╚████║███████╗╚██████╔╝ ╚████╔╝ ██║██║ ╚═╝ ██║]],
  [[ ╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═══╝  ╚═╝╚═╝     ╚═╝]],
  [[                                                   ]],
  [[                [ version : 1.0.0 ]                ]],
}
```

上述代码中 `g:dashboard_default_executive` 用于选择默认的模糊查询工具，dashboard 支持以下三种：

- [vim-clap](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fliuchengxu%2Fvim-clap)
- [fzf.vim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjunegunn%2Ffzf.vim)
- [telescope.nvim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-lua%2Ftelescope.nvim)

我们选择了上一节课刚刚安装的 `telescope.nvim`，dashboard 会使用 telescope 弹窗显示结果。

`vim.g.dashboard_custom_footer` 用于自定义底部显示的文字，我这里显示了本小册的完整的代码地址。

`vim.g.dashboard_custom_header` 是最重要的部分，用于自定义顶部显示的 ascii 图片，[官方 wiki](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fglepnir%2Fdashboard-nvim%2Fwiki%2FAscii-Header-Text) 上有很多推荐图片。



注意：`dashboard`插件目前已经使用lua重写，配置文件因而变化了，不要照抄

**更新了，别用上面的了：2022年11月27日22:00:18**

```lua

local status, db = pcall(require, "dashboard")
if not status then
  vim.notify("没有找到 dashboard")
  return
end

db.custom_footer = {
  "",
  "",
  "https://mindcons.cn     ",
}

db.custom_center = {
  {
    icon = "  ",
    desc = "Projects                            ",
    action = "Telescope projects",
  },
  {
    icon = "  ",
    desc = "Recently files                      ",
    action = "Telescope oldfiles",
  },
  {
    icon = "  ",
    desc = "Edit keybindings                    ",
    action = "edit ~/.config/nvim/lua/keybindings.lua",
  },
  {
    icon = "  ",
    desc = "Edit Projects                       ",
    action = "edit ~/.local/share/nvim/project_nvim/project_history",
  },
  -- {
  --   icon = "  ",
  --   desc = "Edit .bashrc                        ",
  --   action = "edit ~/.bashrc",
  -- },
  -- {
  --   icon = "  ",
  --   desc = "Change colorscheme                  ",
  --   action = "ChangeColorScheme",
  -- },
  -- {
  --   icon = "  ",
  --   desc = "Edit init.lua                       ",
  --   action = "edit ~/.config/nvim/init.lua",
  -- },
  -- {
  --   icon = "  ",
  --   desc = "Find file                           ",
  --   action = "Telescope find_files",
  -- },
  -- {
  --   icon = "  ",
  --   desc = "Find text                           ",
  --   action = "Telescopecope live_grep",
  -- },
}


db.custom_header = {
  [[                                                   ]],
  [[ ███╗   ██╗███████╗ ██████╗ ██╗   ██╗██╗███╗   ███╗]],
  [[ ████╗  ██║██╔════╝██╔═══██╗██║   ██║██║████╗ ████║]],
  [[ ██╔██╗ ██║█████╗  ██║   ██║██║   ██║██║██╔████╔██║]],
  [[ ██║╚██╗██║██╔══╝  ██║   ██║╚██╗ ██╔╝██║██║╚██╔╝██║]],
  [[ ██║ ╚████║███████╗╚██████╔╝ ╚████╔╝ ██║██║ ╚═╝ ██║]],
  [[ ╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═══╝  ╚═╝╚═╝     ╚═╝]],
  [[                                                   ]],
  [[                [ version : 1.0.0 ]                ]],
}

```





比如卖个萌可以设置成宝可梦：

```lua
vim.g.dashboard_custom_header = {
    [[          ▀████▀▄▄              ▄█ ]],
    [[            █▀    ▀▀▄▄▄▄▄    ▄▄▀▀█ ]],
    [[    ▄        █          ▀▀▀▀▄  ▄▀  ]],
    [[   ▄▀ ▀▄      ▀▄              ▀▄▀  ]],
    [[  ▄▀    █     █▀   ▄█▀▄      ▄█    ]],
    [[  ▀▄     ▀▄  █     ▀██▀     ██▄█   ]],
    [[   ▀▄    ▄▀ █   ▄██▄   ▄  ▄  ▀▀ █  ]],
    [[    █  ▄▀  █    ▀██▀    ▀▀ ▀▀  ▄▀  ]],
    [[   █   █  █      ▄▄           ▄▀   ]],
}
```

![10-2.png](c7b923da434a4a8889a5c11b6c471a3atplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

也可以跟我一样使用文字，你可以搜索一下 ascii 图片生成器，生成自己专属图片，我的文字是使用 [patorjk.com](https://link.juejin.cn/?target=http%3A%2F%2Fpatorjk.com%2Fsoftware%2Ftaag%2F%23p%3Ddisplay%26f%3DANSI%20Shadow%26t%3Dneovim) 生成的。进入后输入文字，然后点击左下角的 `Select & Copy` 即可复制到剪贴板。

接下来`vim.g.dashboard_custom_section` 列出常用功能， 它的基本格式为：

```lua
vim.g.dashboard_custom_section = {
  key = { description = { "图标  标题              " }, command = "命令" },
}
```

比如想要增加一条查找文件，就可以：

```lua
  f = { description = {'  Find file          '}, command = 'Telescope find_files'},
```

这里的图标需要 Nerdfont 字体支持，所以会显示成问号，复制到 Neovim 中就可以正常显示了，你可以到这个网站 [nerdfonts.com/cheat-sheet](https://link.juejin.cn/?target=https%3A%2F%2Fwww.nerdfonts.com%2Fcheat-sheet) 搜索想要的图标，并复制过来。

你可以调用任何你想要的命令，比如增加一个换肤功能，调用 `Telescope colorscheme`。

```lua
  i = { description = { "  Change Theme           "}, command = 'Telescope colorscheme'},
```

我只列举了 4 个，其中 `Telescope oldfiles` 用于打开最近编辑的文件。 `edit ~/.config/nvim/lua/keybindings.lua` 用于编辑快捷键， 因为你一定会经常调整快捷键。

```lua
  a = { description = { "  Projects              " }, command = "Telescope projects" },
  b = { description = { "  Recently files        " }, command = "Telescope oldfiles" },
  c = { description = { "  Edit keybindings      " }, command = "edit ~/.config/nvim/lua/keybindings.lua" },
  d = { description = { "  Edit Projects         " }, command = "edit ~/.local/share/nvim/project_nvim/project_history", },
```

剩下的 `Telescope projects` 并不是 telescope 内置的命令。 而是 telescope 的一个插件，需要安装 [ahmedkhalf/project.nvim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fahmedkhalf%2Fproject.nvim) 后才能使用。

（补充：记得在init.lua中导入）

## 安装 project.nvim 插件

打开 `lua/plugins.lua`，别忘了你现在已经可以用 `Ctrl + p` 模糊搜索找到它了， 在文件中添加 `ahmedkhalf/project.nvim` 插件：

```lua
-- project
use("ahmedkhalf/project.nvim")
```

`:w` 保存，自动安装，安装完整按 `q` 退出。 如果报错网络错误，可以重新运行 `:PackerSync` 。

根据 `project.nvim` 的文档，首先要确保我们之前设置的 `lua/plugin-config/nvim-tree.lua` 配置文件中有下边这一段代码：

```lua
nvim_tree.setup({
  --- 上略

  -- project plugin 需要这样设置
  update_cwd = true,
  update_focused_file = {
    enable = true,
    update_cwd = true,
  },

  -- 下略
}
```

这段代码让 `nvim-tree` 支持切换目录。 之后可以创建 `lua/plugin-config/project.lua` 配置文件：

```lua
local status, project = pcall(require, "project_nvim")
if not status then
    vim.notify("没有找到 project_nvim")
  return
end

-- nvim-tree 支持
vim.g.nvim_tree_respect_buf_cwd = 1

project.setup({
  detection_methods = { "pattern" },
  patterns = { ".git", "_darcs", ".hg", ".bzr", ".svn", "Makefile", "package.json", ".sln" },
})

local status, telescope = pcall(require, "telescope")
if not status then
  vim.notify("没有找到 telescope")
  return
end
pcall(telescope.load_extension, "projects")
```

`pcall` 的部分应该非常熟悉了，如果没有找到 `project_nvim`， 那么就不继续执行。

`detection_methods` 设置检测方式，这里设置为 `pattern`，也就是按照下边的 patterns 参数来检测，当文件夹里有这些文件时，就会被当作一个 project 文件夹，自动保存在配置文件中。

保存后，最后一步别忘了在 **入口文件** 中引入这两个配置文件：

```lua
require("plugin-config.dashboard")
require("plugin-config.project")
```

重启后 `Telescope projects` 即可生效，当我们命令行中输入 `nvim` 回车后进入启动画面，j、k 切换选项，再次回车即可执行对应命令。

![10-1.gif](c78f2231dc744f218ad60bcf702910e2tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

但有时候会发现 project 列表并不是我常用的项目列表，列出了很多没用的项目，这时候就需要手动编辑 `project_history` 列表了，但这个列表保存在哪里呢？

运行命令 `:lua print(require("project_nvim.utils.path").historyfile)` 就可以看到 `project_history` 文件的路径了。

我这里显示的是 `~/.local/share/nvim/project_nvim/project_history` 这个文件，我们可以直接手动修改这个文件，仅保存常用的项目。







好了，目前文本编辑器已经差不多了，下一节就进入 **代码篇** 了，我们会专注在代码相关的功能上。

> 配置中如遇任何问题，可到 [github.com/nshen/learn…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 参考最终源码

# 11.Neovim 语法高亮的安装与配置

我们正式进入 **代码篇** 了，本节课会为 `Neovim` 增加代码高亮功能。提到代码高亮，首先要提到的是 [Tree-sitter](https://link.juejin.cn/?target=https%3A%2F%2Ftree-sitter.github.io%2Ftree-sitter%2F) 项目， Tree-sitter 是一个解析器生成器工具和增量解析库，它可以在源文件编辑的同时高效的实时生成语法树.

接着出现的是 [nvim-treesitter](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-treesitter%2Fnvim-treesitter) 项目，`nvim-treesitter` 是 `Neovim` 下的 `Tree-sitter` 配置和抽象层，它的目标是给 `Neovim` 提供一个简单的 `Tree-sitter` 接口，并且提供多个基于 `Tree-sitter` 的基础功能模块，它可以让你在 nvim 中高效的实现 **代码高亮**，**增量选择** 等基础功能。

下图是 `nvim-treesitter` 官方提供代码高亮对比图，左侧为传统的代码高亮模式，右侧为基于 `Tree-sitter` 的代码高亮：

![nvim-treesitter.png](b9147a820eb84e2fbdab023ecf03d27ftplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

不同语言的效果截图详见官网 [Gallery](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-treesitter%2Fnvim-treesitter%2Fwiki%2FGallery) 。

`nvim-treesitter` 支持的语言非常多，常见编程语言都支持，列表见 [Supported languages](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-treesitter%2Fnvim-treesitter%23supported-languages) 。

首先看一下如何安装 `nvim-treesitter` 。

## 安装 nvim-treesitter

`nvim-treesitter` 同我们之前安装的插件没有什么不同，可以直接使用我们之前介绍的 `Packer.nvim` 安装。

修改 `lua/plugins.lua` 文件中添加 `nvim-treesitter/nvim-treesitter` 插件：

```lua
...

packer.startup({
  function(use)
    -------------------------- plugins -------------------------------------------
    .... 略

    -- treesitter （新增）
    use({ "nvim-treesitter/nvim-treesitter", run = ":TSUpdate" })
...
```

这里的 `run = ":TSUpdate"` 是 `Packer.nvim` 的一个 `Post-install hook`，表示当组件安装或更新完成时会执行 `:TSUpdate` 命令。

需要这句是因为特定的 `nvim-treesitter` 插件版本只与特定的 `language parser` 版本匹配。所以每次我们需要更新了这个插件的时候，当然我们也必须要同步更新所有已经安装的 `language parsers`。

同其他插件一样，`:w` 保存后自动安装，如图：

![11-1.gif](ffb638437139499288d8231417f5e668tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

当我们安装完插件后，注意看上图底部的状态栏，默认会自动下载安装一个 `c` 的 `parser` 。等待完成，按 q 退出。如果报网络错误，重新运行 `:PackerSync`。

`nvim-treesitter` 代码高亮之所以效果这么好，就是因为可以针对不同的语言，安装不同的 `language parser`， 下面我们看一下如何根据你的需要来安装。

## 手动安装 Language parser

你可以运行 `:TSInstallInfo` 命令查看 language parsers 列表与安装状态，如下图所示，只有 c 语言是安装好的：

![11-1.png](6b61350cb44b4ff49a605b8cbcdc4166tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

如果我们要安装指定的 `Language parser`，则我们需要调用命令：

```vim
:TSInstall <language_to_install>
```

比如我们要安装 `JavaScript` 语言，则应该调用 `:TSInstall javascript`。

当我们调用 `TSInstall` 命令的时候，插件会我们生成一个 `<language>.so` 语法文件，放在插件的 `parser` 文件夹内，比如我的系统中完整目录在：

```bash
/home/nn/.local/share/nvim/site/pack/packer/start/nvim-treesitter/parser
```

进入目录会发现我们刚安装的 `javascript.so` 和 `c.so`，每个文件只有几百 KB 大小。

![11-2.png](258f0df0ab224a46b8106cb2ab2ffdfbtplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

如果这个时候运行 `:TSInstallInfo` 则 `javascript` 也会对应打上勾勾。

对应的 `:TSUninstall <language_to_uninstall>` 命令用于卸载 language parser 。

其实我们可以不必手动安装 `language parsers` ，可以在 `nvim-treesitter` 的配置文件中指定自动安装，下边开始配置 `nvim-treesitter`。

## 配置 nvim-treesitter

创建 `lua/plugin-config/nvim-treesitter.lua` 文件。

```lua
local status, treesitter = pcall(require, "nvim-treesitter.configs")
if not status then
    vim.notify("没有找到 nvim-treesitter")
    return
end

treesitter.setup({
  -- 安装 language parser
  -- :TSInstallInfo 命令查看支持的语言
  ensure_installed = { "json", "html", "css", "vim", "lua", "javascript", "typescript", "tsx" },
  -- 启用代码高亮模块
  highlight = {
    enable = true,
    additional_vim_regex_highlighting = false,
  },
})
```

`ensure_installed` 就是自动安装 parsers，不必提前手动安装，只要这里列出，下次重启后就会自动安装，当然如果设置过多那么首次重启会卡一下，而且网络不好的话每个下载失败都会报错。

你可以和上述代码一样为`ensure_installed` 制定一个列表，也可以是直接设置为 `"all"` 或 `"maintained"` ，表示一次下载所有的 parsers。下次重启后就会下载对应的语法文件了。 这里建议你还是自定义用到的语言列表，其次是设置成 `maintained` 如果设置成 `maintained` ，那么我这里的下载量大概在 45MB 左右，给你作为参考。

`highlight` 是 `nvim-treesitter` 的语法高亮模块，设置 `enable` 为 `true` 则开启语法高亮功能，由于使用基于 `treesitter` 的语法高亮，所以将`additional_vim_regex_highlighting` 设置为 `false` 关闭 vim 的正则语法高亮。

保存后别忘了在 **入口文件** 中引入该配置文件。

```lua
-- 基础配置
require("basic")
-- Packer插件管理
require("plugins")
-- 快捷键映射
require("keybindings")
-- 主题设置
require("colorscheme")
-- 插件配置
require("plugin-config.nvim-tree")
require("plugin-config.bufferline")
require("plugin-config.lualine")
require("plugin-config.telescope")
require("plugin-config.dashboard")
require("plugin-config.project")
require("plugin-config.nvim-treesitter") -- （新增）
```

重启后，如果一切正常即可看到代码高亮效果，调用 `:TSBufToggle highlight` 命令可以切换打开关闭代码高亮功能，如图。

![11-3.gif](b2b1436bb09941eb897ede9256e0c488tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

然而这个代码高亮颜色，和我们之前安装的 `colorscheme` 支持程度有关，不同的主题配色显示会不一样，你可以在 `nvim-treesitter` 的 `wiki` 里查看不同到皮肤的显示效果，网址如下：

[github.com/nvim-treesi…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-treesitter%2Fnvim-treesitter%2Fwiki%2FColorschemes)

然而下图演示了很多网友都遇到过的一个经典的 bug ，我本来配置好好的 Neovim 环境，在某次更新插件后，突然也出现了这个 bug，后来发现很多人都遇到了这个情况，如图 ：

![11-2.gif](c907598933cc4dfea2fc32655987b3b0tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

经我查询发现，这是由于我们安装的某个 `colorscheme` 和 `treesitter` 不兼容导致的。 我之前安装的 `zephy-nvim` 配色原本是兼容的，但在某次的更新后突然出现了不兼容的状况，所以出现了上述bug。

解决办法也非常简单，直接卸载这个配色即可，卸载的办法就是在 `plugins.lua` 中把该行插件注释掉，然后保存，则会自动删除掉那个插件。

所以我还是推荐使用下载量比较大，比较流行的主题配色，通常不会出现 bug ，比如我们的 `tokyonight` 主题。如果你也出现了这种情况，试着找一找是哪个皮肤的问题。

除了代码高亮功能外，`nvim-treesitter` 还提供其他 3 个内置模块功能，可以根据你的需要添加，下边介绍增量选择模块。

## 补充

可能会提示C99Mode之类的错误，这是编译的模式问题

临时更新gcc版本

[(3条消息) centos7升级gcc 解决make时c99错误_Telda_W的博客-CSDN博客](https://blog.csdn.net/qq_23418145/article/details/121162908)

## 增量选择模块

什么是增量选择 (incremental selection) ？ 当你的光标在一个语法结点上时，可以设置一个增加键和一个减少键，敲击这两个，在表现上为不断外扩和收缩选中代码。

见图：

![11-4.gif](2fab0f9a0abe4385a20735a6b14f4255tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

如果你需要这个功能，需要打开 `lua/plugin-config/nvim-treesitter.lua` 文件，在 `highlight` 模块下方，增加如下代码：

```lua
-- 启用增量选择模块
incremental_selection = {
  enable = true,
  keymaps = {
    init_selection = "<CR>",
    node_incremental = "<CR>",
    node_decremental = "<BS>",
    scope_incremental = "<TAB>",
  },
},
```

注意到上边代码，为了减少记忆额外快捷键的负担，我将增加和减少结点的快捷键设置成了 **回车** 和 **退格** 。通过不断的按 Enter 选择区域会从里层不断外扩， Backspace 则相反不断内收。

除了增量选择模块，`nvim-treesitter` 还内置了一个比较实用的代码缩进模块，用于简单的代码缩进调整，下边介绍一下。

## 代码缩进模块

启用该模块后，可以使用 `=` 操作符对代码缩进，如图：

![11-5.gif](36c87fe145764f25bf13a2e313176468tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

在上边的演示中，我是先选中要缩进的代码，然后按 `=` 键，即可对选中代码缩进。

如果要对整个文件进行缩进，可以使用 `gg=G` 组合键，因为 `gg` 是跳到首行，`G` 是跳到尾行，`gg=G` 就是从首行一直缩进到尾行，相当于 `ggvG` 选中整个文件然后用 `=` 格式化。

如果你经常使用这个组合键，那么你可以考虑像我们之前一样，添加一个快捷键到 `lua/keybindings.lua`，这里不再详述。

想要启用代码缩进功能模块，需要打开 `lua/plugin-config/nvim-treesitter.lua` 文件，在 `incremental_selection` 模块下方，增加如下代码：

```lua
  -- 启用代码缩进模块 (=)
  indent = {
    enable = true,
  },
```

`nvim-treesitter` 还内置了一个基于 `Tree-sitter` 的代码折叠功能模块，下边介绍一下。

## 代码折叠模块

代码折叠可以使代码更清晰，更易于阅读，基于 `Tree-sitter` 的代码折叠可以精确的折叠 `{}` 中的内容。演示如下：

![11-6.gif](d426c6a54d464b3a80bf5982aec20b75tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

在上边的演示中，我使用了 `zc` 组合键来折叠 `{}` 中的内容，还可以使用 `zo` 组合键来打开对应的折叠。

如果你需要这个功能，那么打开 `lua/plugin-config/nvim-treesitter.lua`，在文件的最下方插入代码：

```lua
-- 开启 Folding 模块
vim.opt.foldmethod = "expr"
vim.opt.foldexpr = "nvim_treesitter#foldexpr()"
-- 默认不要折叠
-- https://stackoverflow.com/questions/8316139/how-to-set-the-default-to-unfolded-when-you-open-a-file
vim.opt.foldlevel = 99
```

注意这次是插入在文件的最下方，因为这个功能严格意义上不是一个模块，因为它对应的是 windows 而不是一个 buffer。

最后，你可以运行 `:TSModuleInfo` 命令来查看你的模块是否开启成功，如图：

![11-3.png](243d083c59a047b2bb680454e20d2ac6tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

`nvim-treesitter` 内置功能大概就这么多，但其 [官方 wiki ](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvim-treesitter%2Fnvim-treesitter%2Fwiki%2FExtra-modules-and-plugins)中还列出了许多第三方的功能模块和插件，你也可以去了解一下。

下一节课会介绍 Neovim 内置 LSP 的基础配置，赶快来吧。

> 配置中如遇任何问题，可到 [github.com/nshen/learn…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 参考最终源码

# 12.Neovim 内置 LSP 的基础配置

想要在 `Neovim` 中配置代码补全、代码悬停、代码提示等等功能，首先要了解什么是 LSP (Language Server Protocol) 语言服务协议?

在 LSP 出现之前，传统的 IDE 都要为其支持的每个语言实现类似的代码补全、文档提示、跳转到定义等功能，不同的 IDE 做了很多重复的工作，并且兼容性也不是很好。 LSP 的出现将编程工具解耦成了 **Language Server** 与 **Language Client** 两部分。定义了编辑器与语言服务器之间交互协议。

![12-1.png](11556d465ae2488a81ced76c51a36bd0tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

Client 专注于显示样式实现， Server 负责提供语言支持，包括常见的自动补全、跳转到定义、查找引用、悬停文档提示等功能。

而我们所说的 Neovim 内置 LSP 就是说 Neovim 内置了一套 Language Client 端的实现，这样我们就可以连接到和 VSCode 相同的第三方 language servers ，实现高质量的语法补全等功能。

下边我们就来看看如何开启 Neovim 的内置 LSP 功能。

## 开启 Neovim 内置 LSP

通过命令 `:h lsp` 查看 LSP 文档的 QUICKSTART 部分写了 4 步：

1. 安装 nvim-lspconfig
2. 安装对应 language server
3. 配置对应语言 require('lspconfig').xx.setup{…}
4. :lua print(vim.inspect(vim.lsp.buf_get_clients())) 查看 LSP 连接状态

首先第一步就是要配置客户端，之所以要安装 [nvim-lspconfig](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fneovim%2Fnvim-lspconfig) ，是因为 `nvim-lspconfig` 提供了一堆常见服务的配置方式。

第二步就是安装语言服务器，比如要安装 TypeScript Language Server，就可以到对应的 [主页](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftypescript-language-server%2Ftypescript-language-server) 上查找安装方式，发现可以用 npm 命令 `npm install -g typescript-language-server` 进行安装。

值得庆幸的是，现在有了 [nvim-lsp-installer](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwilliamboman%2Fnvim-lsp-installer) 项目，可以帮助我们管理，并自动安装 Language Server。

所以我们把这两个插件一并安装起来，打开 `lua/plugins.lua` 添加 `nvim-lspconfig` 和 `nvim-lsp-installer` 组件。

```lua
   --------------------- LSP --------------------
    use("williamboman/nvim-lsp-installer")
    -- Lspconfig
    use({ "neovim/nvim-lspconfig" })

...略
```

同其他插件一样，`:w` 保存后自动安装，如果报错网络错误，可以重新运行 `:PackerSync`。

插件安装安装完成后，我们先看一下如何用 `nvim-lsp-installer` 来安装 language servers。

## 安装 LSP Servers

我们先来看一下最简单的方式，运行 `:LspInstallInfo` 命令，会打开一个图形化界面，如图：

![12-2.png](1091ea7c9b4a4baf8c48b7e06c179beftplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

看到上图界面表示安装成功了，`Available servers` 中列出了可以安装的 servers，这时你可以使用 `j / k` 移动光标到你要安装的 server，点击键盘 `i` 安装，i 表示 install。

安装完成后会列出该 LSP Server 的版本和安装的目录等信息，过程演示如下：

![12-1.gif](cf4bb32fa64549d184d5eb98fbcd8e9ctplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

在该界面还有一些其他的快捷键，比如：

- 大写的 `X` 是卸载该 server
- `u` 是更新 server
- 大写 `U` 更新所有 servers
- `c` 检查 server 新版本
- 大写 `C` 检查所有 servers 的新版本
- `ESC` 关闭窗口
- `?` 显示其他帮助信息

几乎所有 Language Server 的管理都可以在这个界面搞定。下边 LSP 的配置部分。

## 配置 LSP Server

因为会创建很多文件，所以我们首先创建一个新的目录 `lua/lsp/` 专门存放 lsp 相关的配置，这样可以使配置文件组织更加清晰。

然后创建第一个文件 `lua/lsp/setup.lua`，内容如下：

```lua
local lsp_installer = require("nvim-lsp-installer")

-- 安装列表
-- { key: 语言 value: 配置文件 }
-- key 必须为下列网址列出的名称
-- https://github.com/williamboman/nvim-lsp-installer#available-lsps
local servers = {
  sumneko_lua = require("lsp.config.lua"), -- lua/lsp/config/lua.lua
}
-- 自动安装 Language Servers
for name, _ in pairs(servers) do
  local server_is_found, server = lsp_installer.get_server(name)
  if server_is_found then
    if not server:is_installed() then
      print("Installing " .. name)
      server:install()
    end
  end
end

lsp_installer.on_server_ready(function(server)
    local config = servers[server.name]
    if config == nil then
        return
    end
    if config.on_setup then
        config.on_setup(server)
    else
        server:setup({})
    end
end)
```

简单解释一下上述代码和配置文件的目录结构。首先我们创建了一个 `servers` 字典变量，用来存放所有的 LSP Server 的配置。

```lua
local servers = {
  sumneko_lua = require("lsp.config.lua"), -- lua/lsp/config/lua.lua
}
```

- 这里的 key `sumneko_lua` 不是随意设置的，而是 `nvim-lsp-installer` 中 lua 语言的 server name，你可以在 [这个网址](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwilliamboman%2Fnvim-lsp-installer%23available-lsps) 中查到合法的值。
- 这里的 value `require("lsp.config.lua")` 表示该 Server 对应的配置文件 `lua/lsp/config/lua.lua` 内容，这个文件需要我们自己创建，这个我们稍后创建。

接下来的这段代码，是遍历 `servers` 字典，检查每个 server 是否已经安装，如果没有安装，就调用 `install()` 方法来安装。

```lua
for name, _ in pairs(servers) do
  local server_is_found, server = lsp_installer.get_server(name)
  if server_is_found then
    if not server:is_installed() then
      print("Installing " .. name)
      server:install()
    end
  end
end
```

也就是说，如果你还没有按照之前的方法手动安装过 lua server ，那么这里会自动帮你安装上。

下边这段代码，是 `lsp_installer` 的回调函数，这个函数会在每个 LSP Server 准备好时调用。

```lua
lsp_installer.on_server_ready(function(server)
    local config = servers[server.name]
    if config == nil then
        return
    end
    if config.on_setup then
        config.on_setup(server)
    else
        server:setup({})
    end
end)
```

在回调函数中，我会先查看我们的 `servers` 字典中有没有这个 server 的配置文件，如果没有，就什么都不执行。 然后我会查看配置文件中，是否有 `on_setup` 函数，如果有，就执行这个函数，否则就用默认无配置参数。

之后我会在每个 Language Server 配置文件中导出一个 `on_setup` 函数，用于初始化该 Server，这样做是因为我发现每个 Server 初始化方法并不完全相同， 用同一套初始化流程并不能满足不同语言定制的需要，所以我将初始化方法抽离出来，让每个 Server 的配置文件来负责初始化。

我们第一个要创建的 Language Server 配置文件就是之前 require 的 lua 文件。

## 配置 Lua Server

创建文件 `lua/lsp/config/lua.lua`，内容如下：

```lua
-- https://github.com/neovim/nvim-lspconfig/blob/master/doc/server_configurations.md#sumneko_lua
local runtime_path = vim.split(package.path, ';')
table.insert(runtime_path, 'lua/?.lua')
table.insert(runtime_path, 'lua/?/init.lua')

local opts = {
    settings = {
        Lua = {
            runtime = {
                -- Tell the language server which version of Lua you're using (most likely LuaJIT in the case of Neovim)
                version = 'LuaJIT',
                -- Setup your lua path
                path = runtime_path,
            },
            diagnostics = {
                -- Get the language server to recognize the `vim` global
                globals = { 'vim' },
            },
            workspace = {
                -- Make the server aware of Neovim runtime files
                library = vim.api.nvim_get_runtime_file('', true),
                checkThirdParty = false,
            },
            -- Do not send telemetry data containing a randomized but unique identifier
            telemetry = {
                enable = false,
            },
        },
    },
    flags = {
        debounce_text_changes = 150,
    },
    on_attach = function(client, bufnr)
        -- 禁用格式化功能，交给专门插件插件处理
        client.resolved_capabilities.document_formatting = false
        client.resolved_capabilities.document_range_formatting = false

        local function buf_set_keymap(...)
            vim.api.nvim_buf_set_keymap(bufnr, ...)
        end
        -- 绑定快捷键
        require('keybindings').mapLSP(buf_set_keymap)
        -- 保存时自动格式化
        vim.cmd('autocmd BufWritePre <buffer> lua vim.lsp.buf.formatting_sync()')
    end,
}

-- 查看目录等信息
return {
    on_setup = function(server)
        server:setup(opts)
    end,
}
```

简单解释一下上述代码。先看最后 5 行代码，之前说过我们会让每个 Language Server 配置文件都导出一个 `on_setup` 函数，用于初始化该 Language Server。 这个函数会接收一个 `server` 参数， 我们通常会在这个函数中调用 `server:setup` 方法，并传入我们定制的 `opts` 参数来初始化语言服务。

在这个 `opts` 参数里通常会有两个关键项需要你来定制： `settings` 和 `on_attach`。

- `settings` 主要用来配置语言服务，我们一般会在 `nvim-lspconfig` 项目的 [服务器配置项页面](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fneovim%2Fnvim-lspconfig%2Fblob%2Fmaster%2Fdoc%2Fserver_configurations.md) 找到对应语言的示例配置。
- `on_attach` 是一个回调函数，当语言服务成功绑定到一个 buffer 上时会调用这个函数，所以通常我们会在这个函数里做一些比如快捷键绑定，自动命令，或者设置 buffer 的某些特性等操作。

上边代码 `on_attach` 中调用了 `keybindings` 文件的 `mapLSP` 方法。

```lua
`require("keybindings").mapLSP(buf_set_keymap)`
```

这样做的目的是为了把定义快捷键的代码抽离出来，都放在`lua/keybindings.lua` 这一个位置来统一管理，那么看一下都定义了哪些快捷键。

## 定义 LSP 快捷键

现在打开 `lua/keybindings.lua` 文件，在 pluginKeys 变量声明的后边添加 `mapLSP` 方法:

```lua
-- lsp 回调函数快捷键设置
pluginKeys.mapLSP = function(mapbuf)
  -- rename
  mapbuf("n", "<leader>rn", "<cmd>lua vim.lsp.buf.rename()<CR>", opt)
  -- code action
  mapbuf("n", "<leader>ca", "<cmd>lua vim.lsp.buf.code_action()<CR>", opt)
  -- go xx
  mapbuf("n", "gd", "<cmd>lua vim.lsp.buf.definition()<CR>", opt)
  mapbuf("n", "gh", "<cmd>lua vim.lsp.buf.hover()<CR>", opt)
  mapbuf("n", "gD", "<cmd>lua vim.lsp.buf.declaration()<CR>", opt)
  mapbuf("n", "gi", "<cmd>lua vim.lsp.buf.implementation()<CR>", opt)
  mapbuf("n", "gr", "<cmd>lua vim.lsp.buf.references()<CR>", opt)
  -- diagnostic
  mapbuf("n", "gp", "<cmd>lua vim.diagnostic.open_float()<CR>", opt)
  mapbuf("n", "gk", "<cmd>lua vim.diagnostic.goto_prev()<CR>", opt)
  mapbuf("n", "gj", "<cmd>lua vim.diagnostic.goto_next()<CR>", opt)
  mapbuf("n", "<leader>f", "<cmd>lua vim.lsp.buf.formatting()<CR>", opt)
  -- 没用到
  -- mapbuf('n', '<leader>q', '<cmd>lua vim.diagnostic.setloclist()<CR>', opt)
  -- mapbuf("n", "<C-k>", "<cmd>lua vim.lsp.buf.signature_help()<CR>", opt)
  -- mapbuf('n', '<space>wa', '<cmd>lua vim.lsp.buf.add_workspace_folder()<CR>', opt)
  -- mapbuf('n', '<space>wr', '<cmd>lua vim.lsp.buf.remove_workspace_folder()<CR>', opt)
  -- mapbuf('n', '<space>wl', '<cmd>lua print(vim.inspect(vim.lsp.buf.list_workspace_folders()))<CR>', opt)
  -- mapbuf('n', '<space>D', '<cmd>lua vim.lsp.buf.type_definition()<CR>', opt)
end
```

注意这里的快捷键是所有语言服务器通用的，也就是说未来添加任何语言，都会调用到这里的 mapLSP 方法。

大部分都设置为 g 开头，为方便记忆，表示 go XX，比如 `gd` 跳转到定义， 然后 `gh` 显示提示等。

建议根据你自己的习惯修改，这是我目前的配置，未来也可能随时会有修改。

最后一步，别忘了在 **入口文件** 中引入 `lua/lsp/setup.lua` 才能生效。

```lua
-- 基础配置
require("basic")
-- Packer插件管理
require("plugins")
-- 快捷键映射
require("keybindings")
-- 主题设置
require("colorscheme")
-- 插件配置
require("plugin-config.nvim-tree")
require("plugin-config.bufferline")
require("plugin-config.lualine")
require("plugin-config.telescope")
require("plugin-config.dashboard")
require("plugin-config.project")
require("plugin-config.nvim-treesitter")

-- 内置LSP (新增)
require("lsp.setup")
```

`:wq` 保存后重启，如果没有报错的话，就应该生效了，下边测试一下基本操作。

## 测试 LSP 常见功能

- `gd` 跳转到定义，可以跨文件跳转，从 lua.lua 中 `mapLSP` 关键字上点击 `gd`，可以跳转到 keybindings.lua 的方法定义处，如图。

![12-2.gif](cf8d42e048e649abad87ae3695b7ca94tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

- 随便敲代码会提示错误。

![12-3.gif](8a7c8b650b6e45aca2ed5dfd875a9282tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

注意顶部的标签页也显示了错误图标，这是因为我们之前在 `lua/plugin-config/bufferline.lua` 插件的设置中，有这么一段代码

```lua
-- 使用 nvim 内置 LSP  后续课程会配置
diagnostics = "nvim_lsp",
-- 可选，显示 LSP 报错图标
---@diagnostic disable-next-line: unused-local
diagnostics_indicator = function(count, level, diagnostics_dict, context)
    local s = " "
    for e, n in pairs(diagnostics_dict) do
    local sym = e == "error" and " " or (e == "warning" and " " or "")
    s = s .. n .. sym
    end
    return s
end,
```

- 修改变量名，用我自定义的快捷键 `<leader>rn` 修改变量名，然后回车。

![12-4.gif](e4882f8ad7904517949855b836adcf68tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

- 代码悬停，在关键字上敲击 `gh` (go hover) 显示提示。

![12-5.gif](0b46efee9ea94cb5836256252181d506tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

一切都很酷，唯独还没有 **代码自动补全** 功能，因为 Neovim 默认并没有提供自动补全框架，所以我们还需要另外配置，这将是我们下一节课的内容。

> 配置中如遇任何问题，可到 [github.com/nshen/learn…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 参考最终源码

# 13.基于 LSP 的代码补全与自定义代码段

Neovim 本身不支持代码补全，需要通过插件实现，我这里使用最流行的 [nvim-cmp](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhrsh7th%2Fnvim-cmp) 插件。

在安装自动代码补全之前，需要了解几个概念：

1. 补全引擎

   补全引擎就是为 Neovim 提供代码补全核心功能的插件，比如 [nvim-cmp](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhrsh7th%2Fnvim-cmp)。

2. 补全源

   补全源就是补全引擎需要的数据来源，最常见的来源是来自 Language Server 提供的数据，它会知道某个类有哪些属性和方法等。

3. snippet 引擎

   snippet 引擎就是自定义代码段的引擎，常见的有 `vsnip`、`luasnip` 等

三个词组一个句子，可以说：

nvim-cmp 是使用 Lua 编写的 **补全引擎** 插件。可以配置多种外部的**补全源**，支持 `vsnip`、`luasnip`、`snippy`、 `ultisnips` 4 种 **snippet 引擎** 。

## 安装补全相关插件

```lua
packer.startup({
    function(use)
        ...
        -- 补全引擎
        use("hrsh7th/nvim-cmp")
        -- snippet 引擎
        use("hrsh7th/vim-vsnip")
        -- 补全源
        use("hrsh7th/cmp-vsnip")
        use("hrsh7th/cmp-nvim-lsp") -- { name = nvim_lsp }
        use("hrsh7th/cmp-buffer") -- { name = 'buffer' },
        use("hrsh7th/cmp-path") -- { name = 'path' }
        use("hrsh7th/cmp-cmdline") -- { name = 'cmdline' }

        -- 常见编程语言代码段
        use("rafamadriz/friendly-snippets")

        ...
    end,
    ...
})
```

简单解释一下上述代码，我们好像这一次装了好多插件，其实只有 `hrsh7th/nvim-cmp` 是补全引擎插件本身，其他 `cmp-xxx` 基本都是插件补全来源，也就是说当你输入一个变量的时候，可以从多个来源显示补全的内容。

像 `hrsh7th/cmp-nvim-lsp` 就是 Neovim 内置 LSP 提供的补全内容，`hrsh7th/cmp-buffer` 补全当前 buffer 的内容， `hrsh7th/cmp-cmdline` 是命令行的补全，`hrsh7th/cmp-path` 则是用来补全路径，如果配置了这个，当输入一个路径的时候会补全路径，如图

![13-1.gif](1215c8e0d1cc418893b7fc2780393f86tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

`hrsh7th/vim-vsnip` 就是一个 snippet 引擎，也就是自定义代码段，文档中提到了 4 种，都是支持的

snippet engine

- vsnip
- luasnip
- ultisnips
- snippy

`rafamadriz/friendly-snippets` 包含了大部分常用语言的代码段，非常强大，可以到他的 github 主页查看详细内容。

不多说 `:wq` 保存后重启，如遇问题可 `:PackerSync` 再次安装。

## 配置自动补全

新建文件 `lua/lsp/cmp.lua` ，内容如下：

```lua
local cmp = require("cmp")

cmp.setup({
  -- 指定 snippet 引擎
  snippet = {
    expand = function(args)
      -- For `vsnip` users.
      vim.fn["vsnip#anonymous"](args.body)

      -- For `luasnip` users.
      -- require('luasnip').lsp_expand(args.body)

      -- For `ultisnips` users.
      -- vim.fn["UltiSnips#Anon"](args.body)

      -- For `snippy` users.
      -- require'snippy'.expand_snippet(args.body)
    end,
  },
  -- 补全源
  sources = cmp.config.sources({
    { name = "nvim_lsp" },
    -- For vsnip users.
    { name = "vsnip" },

    -- For luasnip users.
    -- { name = 'luasnip' },

    --For ultisnips users.
    -- { name = 'ultisnips' },

    -- -- For snippy users.
    -- { name = 'snippy' },
  }, { { name = "buffer" }, { name = "path" } }),

  -- 快捷键设置
  mapping = require("keybindings").cmp(cmp),
})

-- / 查找模式使用 buffer 源
cmp.setup.cmdline("/", {
  sources = {
    { name = "buffer" },
  },
})

-- : 命令行模式中使用 path 和 cmdline 源.
cmp.setup.cmdline(":", {
  sources = cmp.config.sources({
    { name = "path" },
  }, {
    { name = "cmdline" },
  }),
})
```

上述代码中，设置了 3 件事，指定了 snippet 引擎，补全来源，和设置了快捷键。

我这里选择了 `vsnip` 作为 snippet 引擎，是因为它是 `nvim-cmp` 同一个作者开发的，应该稳定性会好些，而且貌似很强大可支持 VSCode 相同代码格式。

补全来源最重要的是 `nvim_lsp`，这个是 Neovim 内置的 LSP 提供的补全内容，如果你使用了 LSP，那么这个补全源就是必须的，然后 `vsnip` 也是重要的补全来源之一，buffer 和 path 根据需要放在第二组补全源里。

快捷键的设置跟以前一样, 这里调用了 `keybindings` 的 `cmp` 方法。

打开 `lua/keybindings.lua` 在 pluginKeys 变量下边增加 `cmp` 方法：

```lua
-- nvim-cmp 自动补全
pluginKeys.cmp = function(cmp)
    return {
        -- 出现补全
        ["<A-.>"] = cmp.mapping(cmp.mapping.complete(), {"i", "c"}),
        -- 取消
        ["<A-,>"] = cmp.mapping({
            i = cmp.mapping.abort(),
            c = cmp.mapping.close()
        }),
        -- 上一个
        ["<C-k>"] = cmp.mapping.select_prev_item(),
        -- 下一个
        ["<C-j>"] = cmp.mapping.select_next_item(),
        -- 确认
        ["<CR>"] = cmp.mapping.confirm({
            select = true,
            behavior = cmp.ConfirmBehavior.Replace
        }),
        -- 如果窗口内容太多，可以滚动
        ["<C-u>"] = cmp.mapping(cmp.mapping.scroll_docs(-4), {"i", "c"}),
        ["<C-d>"] = cmp.mapping(cmp.mapping.scroll_docs(4), {"i", "c"}),
    }
end
```

上边代码主要定义了以下快捷键，你可以根据需要修改：

- `<A-.>` alt + . 出现补全弹窗
- `<A-,>` alt + , 取消补全弹窗

![13-2.gif](d6bcf9c1e1864c19aa354658eecd29d9tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

- `<C-k>` 上一个
- `<C-j>` 下一个

![13-3.gif](57104fd6e72c4c7f8e7a52cfac0f48cctplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

- `<CR>` 回车确认
- `<C-u>` 滚动上
- `<C-d>` 滚动下

如果窗口内容太多，可以用 `Ctrl + u` / `Ctrl + d `滚动，很少见，就不再演示了。

如果常用自定义代码段的话，就有一个需求是在各个预定义的参数位置快速跳转，不太好形容，看图就懂了：

![13-4.gif](b19f94ff636746f791b63cbac676ca6ftplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

`nvim-cmp` 官网的 wiki 中有一个例子，使用 `Tab` 键和 `Shift + Tab` 键兼容跳转，叫做 [Super-Tab like mapping](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhrsh7th%2Fnvim-cmp%2Fwiki%2FExample-mappings%23super-tab-like-mapping)

我不太喜欢 Tab 键有多种功能，我参考其代码增加了单独的 `<C-l>` 和 `<C-h>` 键做跳转。

你如果也需要这样的功能，可以在 `lua/keybindings.lua` 修改刚才的 cmp 函数，增加如下代码：

```lua
-- nvim-cmp 自动补全
pluginKeys.cmp = function(cmp)

  local feedkey = function(key, mode)
    vim.api.nvim_feedkeys(vim.api.nvim_replace_termcodes(key, true, true, true), mode, true)
  end

  local has_words_before = function()
    local line, col = unpack(vim.api.nvim_win_get_cursor(0))
    return col ~= 0 and vim.api.nvim_buf_get_lines(0, line - 1, line, true)[1]:sub(col, col):match("%s") == nil
  end

  return {

   ...

    -- 自定义代码段跳转到下一个参数
    ["<C-l>"] = cmp.mapping(function(_)
      if vim.fn["vsnip#available"](1) == 1 then
        feedkey("<Plug>(vsnip-expand-or-jump)", "")
      end
    end, {"i", "s"}),

    -- 自定义代码段跳转到上一个参数
    ["<C-h>"] = cmp.mapping(function()
      if vim.fn["vsnip#jumpable"](-1) == 1 then
        feedkey("<Plug>(vsnip-jump-prev)", "")
      end
    end, {"i", "s"}),

    -- Super Tab
    ["<Tab>"] = cmp.mapping(function(fallback)
      if cmp.visible() then
        cmp.select_next_item()
      elseif vim.fn["vsnip#available"](1) == 1 then
        feedkey("<Plug>(vsnip-expand-or-jump)", "")
      elseif has_words_before() then
        cmp.complete()
      else
        fallback() -- The fallback function sends a already mapped key. In this case, it's probably `<Tab>`.
      end
    end, {"i", "s"}),

    ["<S-Tab>"] = cmp.mapping(function()
      if cmp.visible() then
        cmp.select_prev_item()
      elseif vim.fn["vsnip#jumpable"](-1) == 1 then
        feedkey("<Plug>(vsnip-jump-prev)", "")
      end
    end, {"i", "s"})
    -- end of super Tab
  }
end
```

最后一步，别忘了在 **入口文件** 中引入 `lua/lsp/cmp.lua` 才能生效。

```lua
-- 基础配置
require("basic")
-- Packer插件管理
require("plugins")
-- 快捷键映射
require("keybindings")
-- 主题设置
require("colorscheme")
-- 插件配置
require("plugin-config.nvim-tree")
require("plugin-config.bufferline")
require("plugin-config.lualine")
require("plugin-config.telescope")
require("plugin-config.dashboard")
require("plugin-config.project")
require("plugin-config.nvim-treesitter")
-- 内置LSP
require("lsp.setup")
require("lsp.cmp") --  (新增)
```

`:wq` 保存后重启，如果没有报错的话，就应该生效了。

好了，自动补全也已经搞定了，可以写代码了。但是显示上还不是很完美，下节课会对目前 LSP 相关功能做一些美化，准备好就来吧。

# 14.LSP 功能增强与 UI 美化

当我们敲击了错误代码的时候，左侧会显示该行的状态，如下图：

![14-2.png](eee31ba7cf8c4e2c874faf73dedb9b8btplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

红色那行 `E` 表示错误，很好理解， 那 `W` 是什么呢？ 其实 `W` 是 Warn 的缩写，很不直观，我们把它替换成图标。

## 左列符号图标

新建文件 `lua/lsp/ui.lua` ，内容如下：

```lua
vim.diagnostic.config({
  virtual_text = true,
  signs = true,
  -- 在输入模式下也更新提示，设置为 true 也许会影响性能
  update_in_insert = true,
})
local signs = { Error = " ", Warn = " ", Hint = " ", Info = " " }
for type, icon in pairs(signs) do
  local hl = "DiagnosticSign" .. type
  vim.fn.sign_define(hl, { text = icon, texthl = hl, numhl = hl })
end
```

简单解释一下，`virtual_text` 是右侧显示的文字，`signs` 就是左侧的图标，让它们都显示出来。

默认的情况下，右侧提示文字只在切换回 normal 模式下才会更新，`update_in_insert` 可以让输入模式下也更新，但注意这里也许会影响性能。

再下边一大段的 for 循环就是定义图标了。

同时别忘了在 **入口文件** 中引入这个文件，打开 `init.lua`，加入：

```lua
-- 内置LSP
require("lsp.setup")
require("lsp.cmp")
require("lsp.ui") -- 新增
```

替换完图标后效果如下：

![14-1.png](7ab8d0cc9bed4984ad44202450d1726dtplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

这里加入一个非常重要的小提示，群里的同学问过。当一行代码很长的时候，右侧的提示文字就会显示不全，看不到提示的是什么，这个时候怎么办？ 回顾一下我们之前在 `keybindings.lua` 的 mapLSP 函数定义过这么几个快捷键。

```lua
  -- diagnostic
  mapbuf("n", "gp", "<cmd>lua vim.diagnostic.open_float()<CR>", opt)
  mapbuf("n", "gk", "<cmd>lua vim.diagnostic.goto_prev()<CR>", opt)
  mapbuf("n", "gj", "<cmd>lua vim.diagnostic.goto_next()<CR>", opt)
```

这个 `gp` 就是以弹窗的方式显示改行提示，非常实用。

![14-1.gif](4e9a404e501b4d5bb64ae765cc200c70tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

接着我们看一下自动补全的样式。

## 自动补全样式修改

默认情况下，当我们敲入字母的时候，会弹出补全弹窗，左侧列出备选内容，右侧列出备选的变量类型：

![14-2.gif](2255dea199674bdb84fd21d1ece4ed83tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

现在右侧是以文字的方式显示变量类型的，变量类型字母长度不同导致不是很美观，如果你喜欢，我们可以让右侧变量类型都以一个图标的方式显示，这样就没有对齐强迫症的问题了，也更节省空间了。

![14-3.gif](ff6ebaaf12cf4257b1e46c92c2324148tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

当然如果你觉得只有图标不是很明显，也可以图标字母同时显示。

还可以在补全弹窗里添加更多的内容显示，比如一个比较常见的改进，当我们配置了很多不同补全来源的时候，我们可以右侧增加一列显示补全源来自哪里。

最终配置的效果如下：

![14-4.gif](dd2f71ac067a4608b3559b7b6220f7fbtplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

打开 `lua/plugins.lua` 新增一个插件： [lspkind-nvim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fonsails%2Flspkind-nvim)。这个插件封装了很多常见的小图标，非常方便，不用我们手动再创建了。

```lua
packer.startup({
    function(use)
        ...
        --------------------- LSP --------------------
        -- lspconfig
        use({"neovim/nvim-lspconfig", "williamboman/nvim-lsp-installer"})
        -- 补全引擎
        use("hrsh7th/nvim-cmp")
        -- snippet 引擎
        use("hrsh7th/vim-vsnip")
        -- 补全源
        use ("hrsh7th/cmp-vsnip")
        use("hrsh7th/cmp-nvim-lsp") -- { name = nvim_lsp }
        use("hrsh7th/cmp-buffer") -- { name = 'buffer' },
        use("hrsh7th/cmp-path") -- { name = 'path' }
        use("hrsh7th/cmp-cmdline") -- { name = 'cmdline' }
        -- 常见编程语言代码段
        use("rafamadriz/friendly-snippets")
        -- ui (新增)
        use("onsails/lspkind-nvim")
        ...
    end,
    ...
})
```

`:w` 保存自动安装， 安装完毕后要添加配置信息。

打开 `lua/lsp/ui.lua`，在下边增加代码如下：

```lua
-- lspkind
local lspkind = require('lspkind')
lspkind.init({
    -- default: true
    -- with_text = true,
    -- defines how annotations are shown
    -- default: symbol
    -- options: 'text', 'text_symbol', 'symbol_text', 'symbol'
    mode = 'symbol_text',
    -- default symbol map
    -- can be either 'default' (requires nerd-fonts font) or
    -- 'codicons' for codicon preset (requires vscode-codicons font)
    --
    -- default: 'default'
    preset = 'codicons',
    -- override preset symbols
    --
    -- default: {}
    symbol_map = {
      Text = "",
      Method = "",
      Function = "",
      Constructor = "",
      Field = "ﰠ",
      Variable = "",
      Class = "ﴯ",
      Interface = "",
      Module = "",
      Property = "ﰠ",
      Unit = "塞",
      Value = "",
      Enum = "",
      Keyword = "",
      Snippet = "",
      Color = "",
      File = "",
      Reference = "",
      Folder = "",
      EnumMember = "",
      Constant = "",
      Struct = "פּ",
      Event = "",
      Operator = "",
      TypeParameter = ""
    },
})

local M ={}
-- 为 cmp.lua 提供参数格式
M.formatting = {
    format = lspkind.cmp_format({
      mode = 'symbol_text',
      --mode = 'symbol', -- show only symbol annotations

      maxwidth = 50, -- prevent the popup from showing more than provided characters (e.g 50 will not show more than 50 characters)
      -- The function below will be called before any actual modifications from lspkind
      -- so that you can provide more controls on popup customization. (See [#30](https://github.com/onsails/lspkind-nvim/pull/30))
      before = function (entry, vim_item)
        -- Source 显示提示来源
        vim_item.menu = "[" .. string.upper(entry.source.name) .. "]"
        return vim_item
      end
    })
}

return M
```

简单解释一下上述代码，首先引入刚刚安装的 `lspkind` 插件，调用 `lspkind.init` 方法初始化。

初始化参数中的 `symbol_map` 就是变量类型和其对应的自定义图标，由于图标是 Nerdfont 的，所以只在命令行中可见。

接下来我们导出一个 `M`，这在 lua 中是很常见的写法。 导出后在其他文件中就可以 `require('lsp.ui').formatting` 取到该值了。

接着我们回到 `lua/lsp/cmp.lua` 文件中，在 `cmp.setup()` 的初始化参数中添加一个 `formatting` 值，如下：

```lua
...
cmp.setup({
  -- 指定 snippet 引擎
  snippet = {...},
  -- 来源
  sources = cmp.config.sources({ ... }),
  -- 快捷键
  mapping = require("keybindings").cmp(cmp),
  -- 使用lspkind-nvim显示类型图标 (新增)
  formatting = require('lsp.ui').formatting
})
...
```

`:w` 保存重启后即可生效。下面再加一个 `indent-blankline.nvim` 插件好了。

## 配置 indent_blankline.nvim 插件

[indent_blankline.nvim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flukas-reineke%2Findent-blankline.nvim) 是什么线？看一下官网截图就明白了。

![image.png](711f6de379514183b8e8d39b7b790923tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

看到那条竖线了吗，它会随着光标的移动提醒我们在哪个上下文中。如果你需要他的话，打开 `plugins.lua`，增加插件：

```lua
    -- indent-blankline
    use("lukas-reineke/indent-blankline.nvim")
```

同之前一样 `:w` 保存即可自动安装。

安装后新建配置文件：`lua/plugin-config/indent-blankline.lua`

```lua
local status, ident_blankline = pcall(require, "indent_blankline")
if not status then
  vim.notify("没有找到 indent_blankline")
  return
end

ident_blankline.setup({
  -- 空行占位
  space_char_blankline = " ",
  -- 用 treesitter 判断上下文
  show_current_context = true,
  show_current_context_start = true,
  context_patterns = {
    "class",
    "function",
    "method",
    "element",
    "^if",
    "^while",
    "^for",
    "^object",
    "^table",
    "block",
    "arguments",
  },
  -- :echo &filetype
  filetype_exclude = {
    "dashboard",
    "packer",
    "terminal",
    "help",
    "log",
    "markdown",
    "TelescopePrompt",
    "lsp-installer",
    "lspinfo",
    "toggleterm",
  },
  -- 竖线样式
  -- char = '¦'
  -- char = '┆'
  -- char = '│'
  -- char = "⎸",
  char = "▏",
})
```

这里需要注意的是该插件会在任何界面都添加这种竖线，但是在我们之前的首页 dashboard 中就不该加入这种竖线。这个时候我们就要在 `filetype_exclude` 中排除 "dashboard" 这个界面。上边代码中我已经排除了好多界面，但如果你还在哪个不该出现竖线的窗口中看到了竖线，要怎么办呢？

方法为： 当光标在该界面内时输入 `:echo &filetype` 回车，这时下边状态栏会输出该文件的类型，把他加入到上边的 `filetype_exclude` 变量中排除就好了。

对了，要生效可别忘了在 **入口文件** 中引入：

```lua
require("plugin-config.indent-blankline")
```

重启后生效。

如果上边的修改只算小修小改，那么下边要介绍的 lspsaga.nvim 插件算是对 LSP 功能的大整修了。

## 配置 lspsaga.nvim

lspsaga.nvim 插件原地址为：

> [github.com/glepnir/lsp…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fglepnir%2Flspsaga.nvim)

但近一年插件原作者消失了，也没有维护，目前比较流行的是这个 Fork 版本：

> [github.com/tami5/lspsa…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftami5%2Flspsaga.nvim)

我们就安装这个，打开 `lua/plugins.lua` 增加插件：

```lua
packer.startup({
    function(use)
        ...
        --------------------- LSP --------------------
        -- lspconfig
        use({"neovim/nvim-lspconfig", "williamboman/nvim-lsp-installer"})
        -- 补全引擎
        use("hrsh7th/nvim-cmp")
        -- snippet 引擎
        use("hrsh7th/vim-vsnip")
        -- 补全源
        use ("hrsh7th/cmp-vsnip")
        use("hrsh7th/cmp-nvim-lsp") -- { name = nvim_lsp }
        use("hrsh7th/cmp-buffer") -- { name = 'buffer' },
        use("hrsh7th/cmp-path") -- { name = 'path' }
        use("hrsh7th/cmp-cmdline") -- { name = 'cmdline' }
        -- 常见编程语言代码段
        use("rafamadriz/friendly-snippets")
        -- ui
        use("onsails/lspkind-nvim")
        use("tami5/lspsaga.nvim" ) -- 新增
        ...
    end,
    ...
})
```

`:w` 保存自动安装，安装完毕后，打开 `lua/lsp/ui.lua` ，在 `lspkind` 配置后边加入代码：

```lua
local lspsaga = require 'lspsaga'
lspsaga.setup { -- defaults ...
  debug = false,
  use_saga_diagnostic_sign = true,
  -- diagnostic sign
  error_sign = "",
  warn_sign = "",
  hint_sign = "",
  infor_sign = "",
  diagnostic_header_icon = "   ",
  -- code action title icon
  code_action_icon = " ",
  code_action_prompt = {
    enable = true,
    sign = true,
    sign_priority = 40,
    virtual_text = true,
  },
  finder_definition_icon = "  ",
  finder_reference_icon = "  ",
  max_preview_lines = 10,
  finder_action_keys = {
    -- open = "o",
    open = "<CR>",
    vsplit = "s",
    split = "i",
    -- quit = "q",
    quit = "<ESC>",
    scroll_down = "<C-f>",
    scroll_up = "<C-b>",
  },
  code_action_keys = {
    -- quit = "q",
    quit = "<ESC>",
    exec = "<CR>",
  },
  rename_action_keys = {
    -- quit = "<C-c>",
    quit = "<ESC>",
    exec = "<CR>",
  },
  definition_preview_icon = "  ",
  border_style = "single",
  rename_prompt_prefix = "➤",
  rename_output_qflist = {
    enable = false,
    auto_open_qflist = false,
  },
  server_filetype_map = {},
  diagnostic_prefix_format = "%d. ",
  diagnostic_message_format = "%m %c",
  highlight_prefix = false,
}
```

这里基本上都是默认配置，我只修改了几个快捷键，注释的部分是原快捷键。

lspsaga 厉害之处是，安装后会有一系列新命令来替换原有功能，比如我们在之前看见过这个 rename 的操作。

![12-4.gif](e4882f8ad7904517949855b836adcf68tplv-k3u1fbpfcp-zoom-in-crop-mark1304000-165085841752924.awebp)

对比 `Lspsaga rename` 的效果：

![14-5.gif](be7fe068042e433384b0172af1d12089tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

你需要做的就是找到之前定义的快捷键，根据需要将原本的功能替换为 Lspsaga 提供的新命令。

这是我目前的设置，请参考，找到 `lua/keybindings.lua` 将之前的 mapLSP 函数替换为：

```lua
-- lsp 回调函数快捷键设置
pluginKeys.mapLSP = function(mapbuf)
  -- rename
  --[[
  Lspsaga 替换 rn
  mapbuf("n", "<leader>rn", "<cmd>lua vim.lsp.buf.rename()<CR>", opt)
  --]]
  mapbuf("n", "<leader>rn", "<cmd>Lspsaga rename<CR>", opt)
  -- code action
  --[[
  Lspsaga 替换 ca
  mapbuf("n", "<leader>ca", "<cmd>lua vim.lsp.buf.code_action()<CR>", opt)
  --]]
  mapbuf("n", "<leader>ca", "<cmd>Lspsaga code_action<CR>", opt)
  -- go xx
  --[[
    mapbuf('n', 'gd', '<cmd>Lspsaga preview_definition<CR>', opt)
  --]]
  mapbuf("n", "gd", "<cmd>lua vim.lsp.buf.definition()<CR>", opt)
  --[[
  Lspsaga 替换 gh
  mapbuf("n", "gh", "<cmd>lua vim.lsp.buf.hover()<CR>", opt)
  --]]
  mapbuf("n", "gh", "<cmd>Lspsaga hover_doc<cr>", opt)
  --[[
  Lspsaga 替换 gr
  mapbuf("n", "gr", "<cmd>lua vim.lsp.buf.references()<CR>", opt)
  --]]
  mapbuf("n", "gr", "<cmd>Lspsaga lsp_finder<CR>", opt)
  --[[
  Lspsaga 替换 gp, gj, gk
  mapbuf("n", "gp", "<cmd>lua vim.diagnostic.open_float()<CR>", opt)
  mapbuf("n", "gj", "<cmd>lua vim.diagnostic.goto_next()<CR>", opt)
  mapbuf("n", "gk", "<cmd>lua vim.diagnostic.goto_prev()<CR>", opt)
  --]]
  -- diagnostic
  mapbuf("n", "gp", "<cmd>Lspsaga show_line_diagnostics<CR>", opt)
  mapbuf("n", "gj", "<cmd>Lspsaga diagnostic_jump_next<cr>", opt)
  mapbuf("n", "gk", "<cmd>Lspsaga diagnostic_jump_prev<cr>", opt)
  mapbuf("n", "<leader>f", "<cmd>lua vim.lsp.buf.formatting()<CR>", opt)
  -- 未用
  -- mapbuf("n", "gD", "<cmd>lua vim.lsp.buf.declaration()<CR>", opt)
  -- mapbuf("n", "gi", "<cmd>lua vim.lsp.buf.implementation()<CR>", opt)
  -- mapbuf('n', '<leader>q', '<cmd>lua vim.diagnostic.setloclist()<CR>', opt)
  -- mapbuf("n", "<C-k>", "<cmd>lua vim.lsp.buf.signature_help()<CR>", opt)
  -- mapbuf('n', '<space>wa', '<cmd>lua vim.lsp.buf.add_workspace_folder()<CR>', opt)
  -- mapbuf('n', '<space>wr', '<cmd>lua vim.lsp.buf.remove_workspace_folder()<CR>', opt)
  -- mapbuf('n', '<space>wl', '<cmd>lua print(vim.inspect(vim.lsp.buf.list_workspace_folders()))<CR>', opt)
  -- mapbuf('n', '<space>D', '<cmd>lua vim.lsp.buf.type_definition()<CR>', opt)
end
```

上述代码我主要将以下 LSP 内置命令，替换成了对应了 Lspsaga 版本的命令。

- `<leader>rn`
- `<leader>ca`
- `gh`
- `gd`
- `gr`
- `gp`
- `gj`
- `gk`

下边演示一下 `gd` `gp` `gh` 的效果，篇幅所限就不过多演示了。

![14-6.gif](6447fa9aa245443ea820d674fa5cd9e6tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

当然，你也可以不替换掉命令，而是增加一条新的命令，因为 Lspsaga 还在开发中目前还不是很稳定，如果你遇到问题，可以还原成原来的命令。

美化的部分就到这了，代码改得乱糟糟的？没关系，下一节课我们会看一下如何设置专门的代码格式化插件，让你的代码更加美观。

# 15.代码格式化的两种方案

为什么我的代码格式化不管用了呢？ 记得我们在之前在 `lua/keybindings.lua` 中设置过 `<leader>f` 为快捷键呀：

```lua
  mapbuf("n", "<leader>f", "<cmd>lua vim.lsp.buf.formatting()<CR>", opt)
```

注意：

![image-20221128084851696](image-20221128084851696.png)

需要更改下方法的名称

```lua
  mapbuf("n", "<leader>f", "<cmd>lua vim.lsp.buf.format({ async = true })<CR>", opt)
```





这是因为我们使用的 Lua Language Server 并没有实现格式化功能。

> 顺便说一下，代码格式化 和 代码缩进 是不同的，在 tree-sitter 章节我们实现的代码缩进只能缩进首字母的位置 如果代码中间出现格式问题，tree-sitter 就无能为力了

如果需要添加代码格式化功能，基本上有两种方案:

- 第一种是使用专门的格式化插件；
- 第二种是给 Language Server 注入格式化功能。

先看第一种方法，我们可以安装 [formatter.nvim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmhartington%2Fformatter.nvim) 插件，Formatter.nvim 插件是很简单易用的格式化插件， 支持很多常见编程语言，例如 JavaScript、Rust、JSON、Bash、Lua、C、Ruby、Python、Golang 等等。

## 安装 Formatter.nvim

这一步别跳过

打开 `lua/plugins.lua` , 增加代码格式化组件：

```lua
    ...
    -- 代码格式化 (新增)
    use("mhartington/formatter.nvim")
    ...
```

我们以 Lua 语言为例，看看如何配置一个语言格式化功能。

第一步需要知道你使用的编程语言有哪些 Code Formatter。 像 Lua 比较常见的应该是 StyLua 或者是 lua-fmt，前端开发的话通常就是用 Prettier 来格式化。

如果不知道也没关系，可以直接到 Formatter [配置文件示例](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmhartington%2Fformatter.nvim%2Fblob%2Fmaster%2FCONFIG.md) 中搜索关键字，比如我 `Ctrl + f` 搜索 `lua` 就搜到了 stylua 的配置方法。

![15-1.png](c8ec4db29bdf4972b2a5e000c1be6afatplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

于是我们就可以去查一下 StyLua 是什么，以及如何安装 [StyLua](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FJohnnyMorganz%2FStyLua)。

`Centos`下安装`Stylua`，要先安装`Rust`，再用它的包管理器安装

[Linux 安装 Rust - 墨天轮 (modb.pro)](https://www.modb.pro/db/214854)



经过调研，我们发现 StyLua 非常简单，有固定语言风格，只提供 6 条配置项，并且可以放在项目根目录的 `.stylua.toml` 中指定。

这样我们就可以给我们的配置文件目录 `~/.config/nvim/.stylua.toml` 加上这个文件：

```toml
column_width = 120
line_endings = "Unix"
indent_type = "Spaces"
quote_style = 'AutoPreferSingle'
indent_width = 4
call_parentheses = "Always"
```

然后我们就会拥有一个统一格式的代码库了，酷。

接下来就要看一下如何安装 StyLua 了，根据 GitHub 主页介绍， Ubuntu 的话还是建议使用 cargo 安装，cargo 是 rust 语言的包管理器，安装 rust 语言后就可以使用了。

```bash
cargo install stylua
```

Mac 系统直接使用 brew 安装即可。

```bash
brew install stylua
```

安装完成运行 `stylua -V`，输出版本号表示成功。

还可以在 neovim 中运行命令：

```
:echo executable("stylua")
```

如果输出 1 表示安装成功，0 则失败。

## 配置 Formatter.nvim

接下来创建 formatter.nvim 的配置文件 `lua/lsp/formatter.lua` 输入内容：

```lua
local status, formatter = pcall(require, "formatter")
if not status then
  vim.notify("没有找到 formatter")
  return
end

formatter.setup({
  filetype = {
    lua = {
      function()
        return {
          exe = "stylua",
          args = {
            -- "--config-path "
            --   .. os.getenv("XDG_CONFIG_HOME")
            --   .. "/stylua/stylua.toml",
            "-",
          },
          stdin = true,
        }
      end,
    }
  },
})

-- format on save
vim.api.nvim_exec(
  [[
    augroup FormatAutogroup
    autocmd!
    autocmd BufWritePost *.lua FormatWrite
    augroup END
]],
  true
)
```

简单解释，代码与之前类似，先取得 formatter 组件，如果不存在则 `return` ，不继续执行。

接下来 `setup` 的参数中根据 `filetype` 不同，对应不同语言，我们这里只配置了 lua，其他编程语言也类似，直接复制 [配置文件示例](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmhartington%2Fformatter.nvim%2Fblob%2Fmaster%2FCONFIG.md) 中的代码即可。

通常需要关注的只有，两个参数：

- exe: 就是你的 Formatter 的程序，对应我们的就是 stylua。
- args: 是 Formatter 接收的参数列表，是一个 Lua table 类型，类似 JavaScript 的 Object。

我这里把 args 中的参数注释掉了，表示使用默认目录下的 `.stylua.toml` 就好，不要到系统目录找了。

接下来我们增加了一段使用了 `vim.api.nvim_exec` 调用了一段 vim 自动命令脚本，表示当我们保存文件时，会自动调用 `stylua` 格式化代码。

Neovim 会在 0.7 版本增加自动命令的 Lua API，目前 0.6 的话还是要通过调用 vim 脚本的方式实现。

最后别忘了在 **入口文件** 引入我们新增的插件：

```lua
--
...
require("lsp.setup")
require("lsp.cmp")
require("lsp.ui")
-- 新增
require("lsp.formatter")
...
```

重启之后我们可以使用新增的 `:Format` 命令来自动格式化代码了。

![15-2.gif](21f394596272493fac4cc3561f29d404tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

如果你决定使用这个插件了，那么可以考虑把之前的 `<leader>f` 快捷键配置成 `:Format` 命令就可以了。

或者你可以再考虑一下，看一下我们的第二种方案： [null-ls.nvim](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjose-elias-alvarez%2Fnull-ls.nvim) 。

## 安装 null-ls.nvim

null-ls 非常强大，可以作为一个通用 Language Server 来给编辑器注入代码补全，格式化，提示，code actions 等新功能。

简单来说就是你在编辑的同一个 buffer 时，不只可以挂一个 Language Server，还可以多挂一个通用的 null-ls Server 作为补充，这样无论我们使用哪个 Server 都可以共享 null-ls 提供的功能。

null-ls 不仅可以做为代码格式化的工具，他更像一个 Lua 语言与 Language Server 的桥梁，它可以通过注入的方式给编辑器带来更多有趣的功能呢，本章只用到了 formatting 功能，后续章节还会继续扩展。

我们先来安装，打开`lua/plugins.lua` 文件，增加代码：

```lua
    -- 代码格式化
    -- use("mhartington/formatter.nvim")
    use({ "jose-elias-alvarez/null-ls.nvim", requires = "nvim-lua/plenary.nvim" })
```

`:w` 保存自动安装，我同时注释掉 formatter.nvim 所在行，这样就卸载了 formatter.nvim， 安装成功后重启，开始配置。

## 配置 null-ls.nvim

继续添加配置文件 `lua/lsp/null-ls.lua`。

```lua
local status, null_ls = pcall(require, "null-ls")
if not status then
  vim.notify("没有找到 null-ls")
  return
end

local formatting = null_ls.builtins.formatting

null_ls.setup({
  debug = false,
  sources = {
    -- Formatting ---------------------
    --  brew install shfmt
    formatting.shfmt,
    -- StyLua
    formatting.stylua,
    -- frontend
    formatting.prettier.with({ -- 只比默认配置少了 markdown
      filetypes = {
        "javascript",
        "javascriptreact",
        "typescript",
        "typescriptreact",
        "vue",
        "css",
        "scss",
        "less",
        "html",
        "json",
        "yaml",
        "graphql",
      },
      prefer_local = "node_modules/.bin",
    }),
    -- formatting.fixjson,
    -- formatting.black.with({ extra_args = { "--fast" } }),
  },
  -- 保存自动格式化
  on_attach = function(client)
    vim.cmd([[ command! Format execute 'lua vim.lsp.buf.format({async = true})']])
    -- if client.resolved_capabilities.document_formatting then
    --   vim.cmd("autocmd BufWritePre <buffer> lua vim.lsp.buf.formatting_sync()")
    -- end
  end,
})
```

简单解释一下代码，首先查找 null-ls 插件是否存在，如果不存在则提示并 return，不再继续执行。 然后注意看下边的 `null_ls.setup` 配置中一大串代码只是在配置一个参数 `sources`， null-ls 有很多内置源，需要哪个就把哪个列在这里就好了。本节只配置了几个常见的 Formatting 源。null-ls 不只内置有 Formatting 源，还有其他共功能的源可配置，也许后续章节会涉及，本节我们专注在代码格式化功能上。

null-ls 支持的 Formatting 源非常非常的多，你可以在其 GitHub 目录中查看：

[/lua/null-ls/builtins/formatting](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjose-elias-alvarez%2Fnull-ls.nvim%2Ftree%2Fmain%2Flua%2Fnull-ls%2Fbuiltins%2Fformatting)

上述目录中所有的源，在配置文件中都在 `null_ls.builtins.formatting` 命名空间下，需要哪个列上去就好了。

最后别忘了在 **入口文件** 中引入该文件，同时注释掉 formatter 插件。

```lua
-- 内置 LSP
require("lsp.setup")
require("lsp.cmp")
require("lsp.ui")
-- require("lsp.formatter")
require("lsp.null-ls")
```

当你重启并成功安装 null-ls.nvim 后，可以运行命令 `:LspInfo` 查看绑定的 Language Server 信息。

![15-3.png](0f387a5f86924396850a43389108aa4dtplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

没错，有两个 LSP 了，null-ls 作为通用 LSP，可以在任何 filetypes 中运行。

我们可以运行 `:NullLsInfo` 查看源的激活情况，如图：

![image.png](8bc58d767fdc4f68a6a9b54171d3357ftplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

我这里显示 2 个 Active source(s) ，一个是我们刚刚配置的 stylua 源给 formatting 方法使用，还有一个 code_ation 源与本节无关，我们后续章节有机会再说。

现在篇首不可用的 format 快捷键应该已经好用了，或者直接运行命令 `:lua vim.lsp.buf.formatting_sync()` 也是可以的。

## 总结

至此，我们两种方式实现代码格式化的功能就都完成了，前一个是简单易用，后一个则是功能强大，应该用哪一种，还是由你来定。

下一节开始我会尝试配置具体的编程语言，但个人能力有限，我并不是每门语言都了解，也不太可能所有语言都照顾到。所以还是欢迎各路大佬留言分享你的配置，我会尽量参考大家的配置，最终更新到这本小册里，有意见也可以到我的 GitHub [nshen/learn-neovim-lua](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 上留言，再次谢谢大家了。

# 16.Neovim 前端开发的必要配置

这一节我们来看看如何配置前端开发环境的，应该会有非常多的东西需要安装，开始吧。

> 有小伙伴发现我已经转到 Mac OS 了，是的，因为购买小册的很多开发者都是在苹果电脑上开发的，强烈要求我使用 Mac 也配置一下， 其实 Neovim 在配置上并没有什么区别，主要还是终端上的不同，但如果你在 Mac 上遇到了什么问题，也欢迎留言告诉我，之后我也会看看是否需要补一节 Mac 环境搭建的文章。

我们先从前端语法高亮开始，还记得如何安装 Treesitter 语法高亮吗，不记得的话可以回去 [Neovim 语法高亮的安装与配置](https://juejin.cn/book/7051157342770954277/section/7071998517543174155) 复习一下。

## Tree-sitter 配置

运行 `:TSInstallInfo` 或者 `:TSModuleInfo` 查看语法安装的情况。

![16-1.png](1de6d20a6a0e47cb8c6cf39f89000cf6tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

Treesitter 有一个直接安装语法高亮的命令 `TSInstall：` 把能找到的 **前端相关** 的都装上：

```
:TSInstall css scss json html vue javascript typescript
```

记得终端挂上代理，有网络问题的不只你一个哦。

安装成功则代码高亮都没问题了，下一步配置 LSP，我们先看看是否已经安装好了，如果没有的话，就安装一下。

## html 与 cssls LSP 配置

先安装 `html` 和 `cssls`， 还记得怎么安装吗？运行 `:LspInstallInfo`，`j` / `k` 移动光标， 选中之后按 `i` 即可安装。大写的 `X` 是卸载。

![16-2.png](a829d05b58084a528e72770fd3735637tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

安装完成后进入 `lua/lsp/setup.lua` 中引入 html 和 css 的配置文件。

```lua
-- 安装列表
-- { key: 服务器名， value: 配置文件 }
-- key 必须为下列网址列出的 server name
-- https://github.com/williamboman/nvim-lsp-installer#available-lsps
local servers = {
  ...

  -- 新增
  html = require("lsp.config.html"),
  cssls = require("lsp.config.css"),
}
```

接着创建 `lua/lsp/config/html.lua` 配置文件。

```lua
return {
  on_setup = function(server)
    server:setup({
      capabilities = require("cmp_nvim_lsp").update_capabilities(vim.lsp.protocol.make_client_capabilities()),
      flags = {
        debounce_text_changes = 150,
      },
      on_attach = function(client, bufnr)
        local function buf_set_keymap(...)
          vim.api.nvim_buf_set_keymap(bufnr, ...)
        end
        -- 绑定快捷键
        require("keybindings").mapLSP(buf_set_keymap)
      end,
    })
  end,
}
```

这里与我们之前的配置类似， capabilities 参数是为了给 cmp_nvim 提供 HTML 补全能力。

保存重启后应该就没问题了，我们找一个前端工程(注意目录中要有 package.json )，创建一个 html 文件试试。

![16-3.gif](347ead4bd3e24f6f9f6be2fc6ac1914ctplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

酷，没问题，试一试代码格式化呢。

![16-4.gif](052b92c3192644d29a27ba10f630490btplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

居然出现了选项，可以输入 1 或 2 后回车进行格式化，并且格式化的样子都不同。为什么会这样呢？ 我们可以运行 `:LspInfo` 查看一下。

![16-5.png](53c419b8841143e9ae00c3b0410d69eatplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

原来我们绑定的两个 LSP ，由于 html server 本身有格式化代码能力，null-ls 又可以使用 prettier 进行格式化 HTML，所以这里出现了选项。

经常会有这种情况出现，如果你不想选择，只使用专门的 prettier 来格式化的话，那么可以在 html.lua 配置中加入。

```lua
-- 禁用格式化功能，交给专门插件插件处理
client.resolved_capabilities.document_formatting = false
client.resolved_capabilities.document_range_formatting = false
```

注意，0.8.1版本的neovim用这个方法

```lua
-- 禁用格式化功能，交给专门插件插件处理    
client.server_capabilities.documentFormattingProvider = false
client.server_capabilities.documentRangeFormattingProvider = false
```



最终配置如下：

```lua
return {
  on_setup = function(server)
    server:setup({
      capabilities = require("cmp_nvim_lsp").update_capabilities(vim.lsp.protocol.make_client_capabilities()),
      flags = {
        debounce_text_changes = 150,
      },
      on_attach = function(client, bufnr)
        -- 禁用格式化功能，交给专门插件插件处理
        -- client.resolved_capabilities.document_formatting = false
        -- client.resolved_capabilities.document_range_formatting = false
        client.server_capabilities.documentFormattingProvider = false
        client.server_capabilities.documentRangeFormattingProvider = false
        local function buf_set_keymap(...)
          vim.api.nvim_buf_set_keymap(bufnr, ...)
        end
        -- 绑定快捷键
        require("keybindings").mapLSP(buf_set_keymap)
      end,
    })
  end,
}
```



**注意：**

上面了更新了，可以直接看作者仓库`v2`分支（当前最新），看作者现在用的配置是啥样

以下两个文件只是看一下，暂时不用管

作者是提取了公共配置，新建`lsp/common-config.lua`

```lua
local M = {}

M.keyAttach = function(bufnr)
  local function buf_set_keymap(mode, lhs, rhs)
    vim.keymap.set(mode, lhs, rhs, { noremap = true, silent = true, buffer = bufnr })
  end
  -- 绑定快捷键
  require("keybindings").mapLSP(buf_set_keymap)
end

-- 禁用格式化功能，交给专门插件插件处理
M.disableFormat = function(client)
  if vim.fn.has("nvim-0.8") == 1 then
    client.server_capabilities.documentFormattingProvider = false
    client.server_capabilities.documentRangeFormattingProvider = false
  else
    client.resolved_capabilities.document_formatting = false
    client.resolved_capabilities.document_range_formatting = false
  end
end

-- M.capabilities = require("cmp_nvim_lsp").update_capabilities(vim.lsp.protocol.make_client_capabilities())
M.capabilities = require("cmp_nvim_lsp").default_capabilities()

M.flags = {
  debounce_text_changes = 150,
}

return M
```

`config/html.lua`

```lua
local M = {}

M.keyAttach = function(bufnr)
  local function buf_set_keymap(mode, lhs, rhs)
    vim.keymap.set(mode, lhs, rhs, { noremap = true, silent = true, buffer = bufnr })
  end
  -- 绑定快捷键
  require("keybindings").mapLSP(buf_set_keymap)
end

-- 禁用格式化功能，交给专门插件插件处理
M.disableFormat = function(client)
  if vim.fn.has("nvim-0.8") == 1 then
    client.server_capabilities.documentFormattingProvider = false
    client.server_capabilities.documentRangeFormattingProvider = false
  else
    client.resolved_capabilities.document_formatting = false
    client.resolved_capabilities.document_range_formatting = false
  end
end

-- M.capabilities = require("cmp_nvim_lsp").update_capabilities(vim.lsp.protocol.make_client_capabilities())
M.capabilities = require("cmp_nvim_lsp").default_capabilities()

M.flags = {
  debounce_text_changes = 150,
}

return M
```





同样的方式配置 css ， 创建 `lua/lsp/config/css.lua`。

```lua
return {
  on_setup = function(server)
    server:setup({
      capabilities = require("cmp_nvim_lsp").update_capabilities(vim.lsp.protocol.make_client_capabilities()),
      settings = {
        css = {
          validate = true,
        },
        less = {
          validate = true,
        },
        scss = {
          validate = true,
        },
      },
      flags = {
        debounce_text_changes = 150,
      },
      on_attach = function(client, bufnr)
        -- 禁用格式化功能，交给专门插件插件处理
        --- client.resolved_capabilities.document_formatting = false
        --- client.resolved_capabilities.document_range_formatting = false
        client.server_capabilities.documentFormattingProvider = false
        client.server_capabilities.documentRangeFormattingProvider = false
        local function buf_set_keymap(...)
          vim.api.nvim_buf_set_keymap(bufnr, ...)
        end
        -- 绑定快捷键
        require("keybindings").mapLSP(buf_set_keymap)
      end,
    })
  end,
}
```

创建一个 css 文件测试一下，看看代码补全和格式化效果。

![16-6.gif](5debd17f29974a748b7c5c5102536addtplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

酷，没问题，下边看一下 Emmet 的配置。

## Emmet LSP 配置

现在的 HTML 打标签有点不智能，增加 Emmet 支持，Emmet 有一套简单的语法可以快速打出 HTML 结构标签，如下图所示：

![16-7.gif](f9258b313ac845d28b3f9d12c9741f17tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

创建 `lua/lsp/config/emmet.lua` 文件如下。

```lua
return {
  on_setup = function(server)
    server:setup({})
  end,
}
```

并在 `lua/lsp/config/setup.lua` 中引入该配置：

```lua
local servers = {
  ...
  -- （新增）
  emmet_ls = require("lsp.config.emmet"),
}
```

别忘了 `:LspInstallInfo` 找到并安装 `emmetls` Language Server。

![16-8.png](5960cfc5f7084963adb5aa660cfe0ecftplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

重启即可之后生效。 接着我们要配置一下 jsonls ，让 Language Server 知道 `package.json`。

## jsonls 配置

首先在 `plugins.lua` 中增加一个插件：

```lua
-- JSON 增强
use("b0o/schemastore.nvim")
```

这是 JSON Schema Store 的插件，算是 JSON 增强插件，用于提供 JSON Schema 的支持，JSON Schema Store 包含了流行的 JSON 格式的语法提示，当然也包括我们的 `package.json`。

有兴趣的可以去官网了解，官网： schemastore.org

新建 `lua/lsp/config/json.lua` 内容如下：

```lua
return {
  on_setup = function(server)
    server:setup({
      settings = {
        json = {
          schemas = require("schemastore").json.schemas(),
        },
      },
      capabilities = require("cmp_nvim_lsp").update_capabilities(vim.lsp.protocol.make_client_capabilities()),
      flags = {
        debounce_text_changes = 150,
      },
      on_attach = function(client, _)
        -- 禁用格式化功能，交给专门插件插件处理
        --- client.resolved_capabilities.document_formatting = false
        --- client.resolved_capabilities.document_range_formatting = false
        client.server_capabilities.documentFormattingProvider = false
        client.server_capabilities.documentRangeFormattingProvider = false         
      end,
    })
  end,
}
```

注意我在 settings 中引入了之前安装的 `schemastore` 插件，这样就可以获取到 JSON Schema 了。

然后在 `lua/lsp/config/setup.lua` 中引入该配置：

```lua
local servers = {
  ...
  -- （新增）
  jsonls = require("lsp.config.json"),
}
```

重启后生效，新建一个 package.json 试试效果：

![16-9.gif](26ba566dc89044a6a8ee999b2c3d6ca6tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

最后安装的是最重要的， TypeScript Language Server。

## 配置 tsserver

首先安装 tsserver ，运行 `:LspInstallInfo`，`j` / `k` 移动光标， 选中 `tsserver` 之后按 `i` 即可安装。

安装好 Language Server，我们还要安装一个 TypeScript 增强插件，打开 `lua/plugins.lua` 增加一个插件：

```lua
use({ "jose-elias-alvarez/nvim-lsp-ts-utils", requires = "nvim-lua/plenary.nvim" })
```

`:w` 保存自动安装，安装成功后，创建 `lua/lsp/config/ts.lua` 文件，开始配置 tsserver，代码如下。

```lua
local keybindings = require("keybindings")
local ts_utils = require("nvim-lsp-ts-utils")
local opts = {
  flags = {
    debounce_text_changes = 150,
  },
  capabilities = require("cmp_nvim_lsp").update_capabilities(vim.lsp.protocol.make_client_capabilities()),
  on_attach = function(client, bufnr)
    -- 禁用格式化功能，交给专门插件插件处理
    --- client.resolved_capabilities.document_formatting = false
    --- client.resolved_capabilities.document_range_formatting = false
    client.server_capabilities.documentFormattingProvider = false
    client.server_capabilities.documentRangeFormattingProvider = false
    local function buf_set_keymap(...)
      vim.api.nvim_buf_set_keymap(bufnr, ...)
    end
    -- 绑定快捷键
    keybindings.mapLSP(buf_set_keymap)
    -- TypeScript 增强
    ts_utils.setup({
      debug = false,
      disable_commands = false,
      enable_import_on_completion = false,
      -- import all
      import_all_timeout = 5000, -- ms
      -- lower numbers = higher priority
      import_all_priorities = {
        same_file = 1, -- add to existing import statement
        local_files = 2, -- git files or files with relative path markers
        buffer_content = 3, -- loaded buffer content
        buffers = 4, -- loaded buffer names
      },
      import_all_scan_buffers = 100,
      import_all_select_source = false,
      -- if false will avoid organizing imports
      always_organize_imports = true,
      -- filter diagnostics
      filter_out_diagnostics_by_severity = {},
      filter_out_diagnostics_by_code = {},
      -- inlay hints
      auto_inlay_hints = true,
      inlay_hints_highlight = "Comment",
      -- update imports on file move
      update_imports_on_move = false,
      require_confirmation_on_move = false,
      watch_dir = nil,
    })
    -- required to fix code action ranges and filter diagnostics
    ts_utils.setup_client(client)
    -- 绑定增强插件快捷键
    keybindings.mapTsLSP(buf_set_keymap)
  end,
}

return {
  on_setup = function(server)
    server:setup(opts)
  end,
}
```

上述代码比之前长了不少，主要是多了 ts_utils 初始化，里边都是默认配置，我并没有改动，我只是在 ts_utils 初始化后调用了 `keybindings.mapTsLSP(buf_set_keymap)` 绑定了新的快捷键。

打开 `lua/keybindings.lua` ，添加 mapTsLSP 方法:

```lua
-- typescript 快捷键
pluginKeys.mapTsLSP = function(mapbuf)
  mapbuf("n", "gs", ":TSLspOrganize<CR>", opt)
  mapbuf("n", "gr", ":TSLspRenameFile<CR>", opt)
  mapbuf("n", "gi", ":TSLspImportAll<CR>", opt)
end
```

这里给我们的 TypeScript 开发增加了 3 个新功能。

我们先在 `lua/lsp/config/setup.lua` 中引入我们的 tsserver 配置文件：

```lua
tsserver = require("lsp.config.ts"),
```

经过增强，终于有了 import 相关的命令了，比如 `:TSLspOrganize` 会删除不用的 import 语句并重新排序。

先找个前端项目试一下，我故意引入了很多没用到的东西，然后敲击 gs 即可瞬间整理完毕。

![16-10.gif](b455f6f96ef3434e9fdc033d85c5d7d9tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

除了这个还有 `:TSLspRenameFile` 用于改变文件名，同时其他文件中引用该文件的文件名也会被修改。

`:TSLspImportAll` 将会导入当前文件的所有依赖，并且会自动排序。 我就不再演示了。

接下来就剩下 ESlint 和 Pretier 的配置了。

## ESLint 和 Prettier 配置

ESLint 的文字提示，和 Prettier 的格式化，我都是通过上一节介绍的 null-ls 插件来实现的。

记得我们在之前的配置中用了 null-ls 的内置代码格式化源：

```lua
local formatting = null_ls.builtins.formatting
...
-- StyLua
formatting.stylua,
```

其实 null-ls 除了内置 Formatting，还有内置很多的 Diagnostics 和 Code Actions

Diagnostic 就是类似代码行旁边的红字错误提示。

Code Action 就是这行可以触发的行为，比如有些 ESLint 错误是可以自动 Fix 的，这时候这行代码就有一个 Code Action，后边我再演示。

先打开 `lua/lsp/null-ls.lua`，改为：

```lua
local status, null_ls = pcall(require, "null-ls")
if not status then
  vim.notify("没有找到 null-ls")
  return
end

local formatting = null_ls.builtins.formatting
local diagnostics = null_ls.builtins.diagnostics
local code_actions = null_ls.builtins.code_actions

null_ls.setup({
  debug = false,
  sources = {
    -- Formatting ---------------------
    --  brew install shfmt
    formatting.shfmt,
    -- StyLua
    formatting.stylua,
    -- frontend
    formatting.prettier.with({ -- 比默认少了 markdown
      filetypes = {
        "javascript",
        "javascriptreact",
        "typescript",
        "typescriptreact",
        "vue",
        "css",
        "scss",
        "less",
        "html",
        "json",
        "yaml",
        "graphql",
      },
      extra_filetypes = { "njk" },
      prefer_local = "node_modules/.bin",
    }),
    -- Diagnostics  ---------------------
    diagnostics.eslint.with({
      prefer_local = "node_modules/.bin",
    }),
    -- code actions ---------------------
    code_actions.gitsigns,
    code_actions.eslint.with({
      prefer_local = "node_modules/.bin",
    }),
  },
  -- #{m}: message
  -- #{s}: source name (defaults to null-ls if not specified)
  -- #{c}: code (if available)
  -- 提示格式： [eslint] xxx
  diagnostics_format = "[#{s}] #{m}",
  on_attach = function(client)
    -- 自定义 :Format 命令
    vim.cmd([[ command! Format execute 'lua vim.lsp.buf.formatting()']])
  end,
})
```

注意我们上边配置的都是 `prefer_local` 也就是说要求**项目本地依赖** prettier 和 eslint，也就是说项目目录要有 `package.json` 并且 `npm install -D prettier eslint` 安装过依赖，才成功会格式化。

按照上述配置后，就应该会显示 ESLint 错误了。 我们来实验一下。

ESLint recommended 规则里有一条叫作 `no-var` 规则，就是不推荐使用 var 来声明变量。

所以我们故意用 var 来声明一个变量：

![16-11.png](98d218fd8651439d98b1106100d39aa3tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

看到右边的红字了吗，这就是 Diagostics，并且是按照我们上边代码设置的规则显示的：

```
diagnostics_format = "[#{s}] #{m}"
```

现在我们看看 Code Action 能否自动修复掉，在该行代码上敲击我们之前定义的快捷键 `<leader>ca` 就会调用 Code Action 了，请看动图演示：

![16-12.gif](0471d897dcd94fdaa2bb0904dbf76127tplv-k3u1fbpfcp-zoom-in-crop-mark1304000.awebp)

第一次运行 CA 的时候，他会提示我修复 no-var 规则，改成了 let 声明变量，然后他又发现并没有给变量 a 重新赋值过，我再一次运行 CA 的时候，他会提示我这里应该用常量。最后修复完成变成了 `const a = 10`。

Okay。全部完成了，本节比较长，如果你没有跟上的话，可以参考我 GitHub 上的代码：

[github.com/nshen/learn…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua)

欢迎点赞，或直接 Fork 我的代码，也欢迎留言分享你的配置。

下一节我会尝试配置其他编程语言 ，我了解的语言非常有限，我知道小册读者里有很多隐藏大佬，非常希望你能到 GitHub 上提出 PR 加入你熟悉的语言配置，我会更新在小册中，帮助到更多人，下节见。

# 17.NeoVim Rust开发配置与断点调试

本节我们学习如何配置 Rust 开发环境，并了解在 Neovim 中如何进行断点调试。

先快速安装一下 Rust 编程语言。

## Rust 编程语言安装

首先安装 rust，打开终端输入：

```shell
$ curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```

这个命令会下载一个脚本并自动开始安装 rustup，按照提示选择全新安装，也许会提示你输入管理员密码，安装成功会出现:

```
Rust is installed now. Great!
```

这时可以查看版本号，验证是否安装成功。

```bash
$ rustc -V
rustc 1.60.0 (7737e0b5c 2022-04-04)

$ cargo -V
cargo 1.60.0 (d1fd9fe2c 2022-03-01)
```

接下来安装 [rust-analyzer](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust-analyzer) , rust-analyzer 可以算是社区驱动的 Language Server 实现了。

MacOS 下安装比较简单，运行命令如下：

```
$ brew install rust-analyzer
```

其他系统请参考 [官方文档](https://link.juejin.cn/?target=https%3A%2F%2Frust-analyzer.github.io%2Fmanual.html%23installation) 或参考其他教程。

至此 rust 语言环境就准备完成了，可以使用 cargo 创建一个 rust 项目了，打开命令行运行：

```bash
cargo new hello-rust
cd hello-rust
cargo run
```

如果输出 `Hello, world!` 就表示成功了，可以开始配置 Neovim 的 Rust 语法高亮和代码提示了。

## Rust 语法高亮与代码提示配置

首先第一步安装基于 tree-sitter 的 rust 语法高亮。

运行 `TSInstall rust` 重启 Neovim 后，打开 `main.rs` 文件，应该可以看到语法高亮了。

接着我们配置 LSP，打开 `lua/lsp/setup.lua`，在 servers 变量中增加 rust 的配置文件，注意这里的 key 必须为 `rust_analyzer`，值为配置文件的路径，可以随意改变。

```lua
local servers = {
  sumneko_lua = require("lsp.config.lua"), -- lua/lsp/config/lua.lua
  bashls = require("lsp.config.bash"),
  pyright = require("lsp.config.pyright"),
  html = require("lsp.config.html"),
  cssls = require("lsp.config.css"),
  emmet_ls = require("lsp.config.emmet"),
  jsonls = require("lsp.config.json"),
  tsserver = require("lsp.config.ts"),
  -- 新增
  rust_analyzer = require("lsp.config.rust"),
}
```

创建对应的 LSP 配置文件 `lua/lsp/config/rust.lua`，配置如下：

```lua
local opts = {
  capabilities = require("cmp_nvim_lsp").update_capabilities(vim.lsp.protocol.make_client_capabilities()),
  flags = {
    debounce_text_changes = 150,
  },
  on_attach = function(client, bufnr)
    -- 禁用格式化功能，交给专门插件插件处理
    client.resolved_capabilities.document_formatting = false
    client.resolved_capabilities.document_range_formatting = false
    local function buf_set_keymap(...)
      vim.api.nvim_buf_set_keymap(bufnr, ...)
    end
    -- 绑定快捷键
    require("keybindings").mapLSP(buf_set_keymap)
  end,
}

return {
  on_setup = function(server)
    -- Initialize the LSP via rust-tools instead
    require("rust-tools").setup({
      -- The "server" property provided in rust-tools setup function are the
      -- settings rust-tools will provide to lspconfig during init.
      -- We merge the necessary settings from nvim-lsp-installer (server:get_default_options())
      -- with the user's own settings (opts).
      server = vim.tbl_deep_extend("force", server:get_default_options(), opts),
    })
    server:attach_buffers()
    -- Only if standalone support is needed
    require("rust-tools").start_standalone_if_required()
  end,
}
```

这里我们在返回的 on_setup 函数中引入了一个 [rust-tools](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsimrat39%2Frust-tools.nvim) 插件，这个插件是一个 Rust 增强插件，在 LSP 之上增加了更多的命令，有兴趣可以去其主页深入了解。 `vim.tbl_deep_extend` 函数可以合并两个 table，`force` 参数表示如果 key 值相同，则用第二个参数的值。 用在这里表示把默认值和我们的自定义值合并，优先使用我们的自定义 opts 的值。

别忘了在 `lua/plugins.lua` 文件中安装 rust-tools 插件，否则会报错：

```lua
-- Rust 增强
use("simrat39/rust-tools.nvim")
```

保存重启 Neovim 后，打开 main.rs 发现语法提示已经搭建好了。

![17-1.gif](/4de70a3cbd074b61ba545532168c595etplv-k3u1fbpfcp-zoom-in-crop-mark3024000.awebp)

接下来配置代码格式化。

## 代码格式化配置

现在很多项目使用 [rust-lang/rustfmt](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frust-lang%2Frustfmt) 来统一 Rust 代码风格。

我们先安装这一工具，打开命令行运行：

```bash
rustup component add rustfmt
```

运行 `rustfmt --version` 可显示版本号，表示安装成功。

![17-2.png](/29a4fa72d43c43b1af083b04b2ea0437tplv-k3u1fbpfcp-zoom-in-crop-mark3024000.awebp)

既然是主流工具，那么 null-ls 一定是支持的。

打开 `lua/lsp/null-ls.lua` 文件， 在 sources 里增加 rustfmt 。

```lua
-- rustfmt
formatting.rustfmt,
```

目前完整 `lua/lsp/null-ls.lua` 配置如下：

```lua
local status, null_ls = pcall(require, "null-ls")
if not status then
  vim.notify("没有找到 null-ls")
  return
end

local formatting = null_ls.builtins.formatting
local diagnostics = null_ls.builtins.diagnostics
local code_actions = null_ls.builtins.code_actions

null_ls.setup({
  debug = false,
  sources = {
    -- Formatting ---------------------
    --  brew install shfmt
    formatting.shfmt,
    -- StyLua
    formatting.stylua,
    -- frontend
    formatting.prettier.with({ -- 比默认少了 markdown
      filetypes = {
        "javascript",
        "javascriptreact",
        "typescript",
        "typescriptreact",
        "vue",
        "css",
        "scss",
        "less",
        "html",
        "json",
        "yaml",
        "graphql",
      },
      prefer_local = "node_modules/.bin",
    }),
    -- rustfmt
    formatting.rustfmt,
    -- Python
    -- pip install black
    -- asdf reshim python
    formatting.black.with({ extra_args = { "--fast" } }),
    -----------------------------------------------------
    -- Ruby
    -- gem install rubocop
    formatting.rubocop,
    -----------------------------------------------------
    -- Diagnostics  ---------------------
    diagnostics.eslint.with({
      prefer_local = "node_modules/.bin",
    }),
    -- code actions ---------------------
    code_actions.gitsigns,
    code_actions.eslint.with({
      prefer_local = "node_modules/.bin",
    }),
  },
  -- #{m}: message
  -- #{s}: source name (defaults to null-ls if not specified)
  -- #{c}: code (if available)
  diagnostics_format = "[#{s}] #{m}",
  on_attach = function(client)
    vim.cmd([[ command! Format execute 'lua vim.lsp.buf.formatting()']])
  end,
})
```

![17-3.gif](/a3e35fa50f3046cea3a9954ff7350720tplv-k3u1fbpfcp-zoom-in-crop-mark3024000.awebp)

注意到上述的配置中，我参考交流群里群友的讨论，也增加了 Ruby 和 Python 格式化配置。

```lua
-- Python
-- pip install black
-- asdf reshim python
formatting.black.with({ extra_args = { "--fast" } }),
-----------------------------------------------------
-- Ruby
-- gem install rubocop
formatting.rubocop,
```

也欢迎各位大佬到我们 [小册的 GitHub 代码库](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 中发PR，持续改进配置。

由此可见，其他语言也应该都是类似的方式配置代码格式化，先用该语言的**包管理器**安装专门的**格式化工具**，然后在 null-ls 里面启用即可。

本节原本打算到此就结束了，但程序开发离不开代码调试，简单的程序可以通过打 log 的方式调试，复杂的程序还是需要用打断点，用逐步运行的方式来调试的。

我一直纠结写不写断点调试相关的东西。因为不得不承认的是，Neovim 中 debug 的体验并不是很好，比如想要调试基于 Node.js 程序的话，最新版本的 VSCode 中内置了 JavaScript Debug Terminal，基本上不用配置就可以直接捕获到断点信息。而用 Neovim 调试的话，还在使用已经被微软抛弃了一年的 [vscode-node-debug2](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fvscode-node-debug2) 库来调试。

而且调试也都是要基于 VSCode 的 DAP (Debug Adapter Protocol) 协议的，所以我还是比较倾向于直接使用 VSCode 来调试程序，但如果你是个爱折腾的人，不妨也可以跟我一起了解一下在 Neovim 中如何调试程序。

## 配置 Debug 断点调试

想要在 Neovim 中打断点来调试应用程序，需要基于 DAP (Debug Adapter Protocol) 协议，这是一个跨平台的调试协议，可以在不同的平台上调试不同的程序。

在 Neovim 中基于 DAP 的插件有两个选择，一个是 [vimspector](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpuremourning%2Fvimspector) ，另一个是 [nvim-dap](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmfussenegger%2Fnvim-dap)。

vimspector 是比较老牌的调试工具，主要为 Vim 8.2 以上的版本开发，同时也兼容 Neovim 0.43 以上的版本。 而 nvim-dap 是一个比较新的调试工具，不支持 Vim，是专门为 Neovim 开发的，使用了很多 Neovim 的 API，我觉得目前还不是很完善，需要搭配几个其他的插件才能很好地使用，而且几个插件都是由不同开发者开发的，其中一个插件更新，有可能会导致其他插件的不兼容，经常需要耗费精力来调整配置。

我们这里先尝试一下 vimspector，打开 `lua/plugins.lua` 文件，添加下面的代码：

```lua
-- vimspector
use("puremourning/vimspector")
```

`:w` 后自动安装，安装完成后，重启 Neovim 后会增加许多 Vimspector 开头的命令， 如果没有 Vimspector 开头的命令， 一般是 python 3 环境的问题，可以尝试运行：

```css
sudo pip3 install --upgrade pynvim
```

正常的话会如下动图所示，我们找到 `VimspectorInstall` 命令:

![17-4.gif](/b9e9d262b13148ed947aeb57c279e617tplv-k3u1fbpfcp-zoom-in-crop-mark3024000.awebp)

上图这些就是 vimspector 支持的 debug 端适配器，在 vimspector 里适配器叫做 gadget，由于我们 debug rust 程序，所以应该安装 CodeLLDB 这个 gadget，选中 `VimspectorInstall CodeLLDB` ，回车安装。

这个命令实际上是调用的一段 python 脚本，所以需要 python3 环境支持，如果环境和网络都没有问题的话，等待一段时间如果安装成功会显示：

> Vimspector gadget installation complete!

表示安装成功，但鉴于国内的网络环境，一般不太会那么顺利，所以建议进入到 vimspector 安装目录直接调用 python 脚本进行安装，那里会有更多的报错信息。

vimspector 的安装目录默认在 `~/.local/share/nvim/site/pack/packer/start/vimspector` ，在这个目录里会有一个 `install_gadget.py` 的脚本。

如果你的网络环境比较好的话，可以挂好全局代理，一次全部安装，下次就不用再进这个目录了。

```bash
./install_gadget.py --all
```

也可以这样只安装 rust：

```bash
./install_gadget.py --enable-rust
```

如果到这里全部成功了的话，就可以开始配置 vimspector 了， 新建一个文件 `lua/dap/vimspector/init.lua`，内容为：

```lua
require("keybindings").mapVimspector()
```

vimspector 并不需要配置，只需要定义一些快捷键就可以了，这里创建的配置文件，只有一行代码，就是定义快捷键。

之所以要有这个文件，就是方便**入口文件**引用。

打开 `lua/init.lua` 添加 vimspector 配置文件的引用：

```lua
require("dap.vimspector") -- lua/dap/vimspector/init.lua
```

像这样直接引用目录的话，会自动引用目录下的 `init.lua` 文件。

然后打开 `lua/keybindings.lua` 文件，增加 vimspector 快捷键设置：

```lua
pluginKeys.mapVimspector = function()
  -- 开始
  map("n", "<leader>dd", ":call vimspector#Launch()<CR>", opt)
  -- 结束
  map("n", "<Leader>de", ":call vimspector#Reset()<CR>", opt)
  -- 继续
  map("n", "<Leader>dc", ":call vimspector#Continue()<CR>", opt)
  -- 设置断点
  map("n", "<Leader>dt", ":call vimspector#ToggleBreakpoint()<CR>", opt)
  map("n", "<Leader>dT", ":call vimspector#ClearBreakpoints()<CR>", opt)
  --  stepOver, stepOut, stepInto
  map("n", "<leader>dj", "<Plug>VimspectorStepOver", opt)
  map("n", "<leader>dk", "<Plug>VimspectorStepOut", opt)
  map("n", "<leader>dl", "<Plug>VimspectorStepInto", opt)
end
```

重启 Neovim ，如果幸运没有报错的话，就可以开始 debug 了。

打开我们之前创建的 `hello-rust` 项目，找到 main.rs ，我从 [course.rs](https://link.juejin.cn/?target=https%3A%2F%2Fcourse.rs%2Ffirst-try%2Fhello-world.html) 教程上 copy 了一段 Rust 代码，如下：

```rust
fn greet_world() {
    let southern_germany = "Grüß Gott!";
    let chinese = "世界，你好";
    let english = "World, hello";
    let regions = [southern_germany, chinese, english];
    for region in regions.iter() {
        println!("{}", &region);
    }
}

fn main() {
    greet_world();
}
```

首先我们需要 build 一下这个项目 `cargo build`，接着我们要在项目根目录创建一个 `.vimspector.json` 文件，内容如下

```json
{
  "configurations": {
    "launch": {
      "adapter": "CodeLLDB",
      "configuration": {
        "request": "launch",
        "program": "${workspaceRoot}/target/debug/hello-rust"
      },
      "breakpoints": {
        "exception": {
          "cpp_catch": "",
          "cpp_throw": "",
          "objc_catch": "",
          "objc_throw": "",
          "swift_catch": "",
          "swift_throw": ""
        }
      }
    }
  }
}
```

这个文件的 program 值指向我们刚才 build 出的 `debug/hello-rust` ，adapter 值是 CodeLLDB， breakpoints 这部分设置是默认的异常抛出处理方法，可以去掉，如果去掉的话每次debug 都会问你抛出异常如何处理。

接下来演示一下如何 debug：

1. `<leader>dt` 创建断点
2. `<leader>dd` 启动 debug
3. `<leader>dj` step over
4. `<leader>de` 结束 debug

![17-5.gif](/3a3e0884eb0a43e49cfbb9ce121864b6tplv-k3u1fbpfcp-zoom-in-crop-mark3024000.awebp)

debug 界面中小黄点是断点，黄色箭头是当前运行到的行，和其他软件的 debug 界面应该差不多。

![17-6.png](/6094e1b46f2e43bb856ffc08906e6616tplv-k3u1fbpfcp-zoom-in-crop-mark3024000.awebp)

这里就不再赘述了，接下来看一下专门为 Neovim 打造的 nvim-dap 怎么样。

## nvim-dap 配置

打开 `lua/plugins.lua` 文件，增加如下内容：

```lua
use("mfussenegger/nvim-dap")
use("theHamsta/nvim-dap-virtual-text")
use("rcarriga/nvim-dap-ui")
```

`:w` 安装完成后， 创建 `lua/dap/nvim-dap/init.lua` 文件，内容如下：

```lua
local dap = require("dap")
local dapui = require("dapui")
require("nvim-dap-virtual-text").setup({
  commented = true,
})

-- 定义各种图标

vim.fn.sign_define("DapBreakpoint", {
  text = "🛑",
  texthl = "LspDiagnosticsSignError",
  linehl = "",
  numhl = "",
})

vim.fn.sign_define("DapStopped", {
  text = "",
  texthl = "LspDiagnosticsSignInformation",
  linehl = "DiagnosticUnderlineInfo",
  numhl = "LspDiagnosticsSignInformation",
})

vim.fn.sign_define("DapBreakpointRejected", {
  text = "",
  texthl = "LspDiagnosticsSignHint",
  linehl = "",
  numhl = "",
})

dapui.setup({
  icons = { expanded = "▾", collapsed = "▸" },
  mappings = {
    -- Use a table to apply multiple mappings
    expand = { "o", "<CR>", "<2-LeftMouse>" },
    open = "o",
    remove = "d",
    edit = "e",
    repl = "r",
    toggle = "t",
  },
  sidebar = {
    -- You can change the order of elements in the sidebar
    elements = {
      -- Provide as ID strings or tables with "id" and "size" keys
      {
        id = "scopes",
        size = 0.25, -- Can be float or integer > 1
      },
      { id = "breakpoints", size = 0.25 },
      { id = "stacks", size = 0.25 },
      { id = "watches", size = 00.25 },
    },
    size = 40,
    position = "left", -- Can be "left", "right", "top", "bottom"
  },
  tray = {
    elements = { "repl" },
    size = 10,
    position = "bottom", -- Can be "left", "right", "top", "bottom"
  },
  floating = {
    max_height = nil, -- These can be integers or a float between 0 and 1.
    max_width = nil, -- Floats will be treated as percentage of your screen.
    border = "single", -- Border style. Can be "single", "double" or "rounded"
    mappings = {
      close = { "q", "<Esc>" },
    },
  },
  windows = { indent = 1 },
  render = {
    max_type_length = nil, -- Can be integer or nil.
  },
}) -- use default
dap.listeners.after.event_initialized["dapui_config"] = function()
  dapui.open()
end
dap.listeners.before.event_terminated["dapui_config"] = function()
  dapui.close()
end
dap.listeners.before.event_exited["dapui_config"] = function()
  dapui.close()
end

-- 绑定 nvim-dap 快捷键
require("keybindings").mapDAP()
```

同时在 **入口文件** init.lua 中注释掉 vimspector，增加 nvim-dap 的引用：

```lua
-- require("dap.vimspector")
require("dap.nvim-dap")
```

因为 rust-tools 正在尝试集成 Dap 调试, 所以接着我们还需要给 rust-tools 传入 Dap adapter 的配置信息。

打开 `lua/lsp/config/rust.lua`，注意看新增一行 dap 的配置：

```lua
...
return {
  on_setup = function(server)
    require("rust-tools").setup({
      server = vim.tbl_deep_extend("force", server:get_default_options(), opts),
      -- ( 新增)
      dap = require("dap.nvim-dap.rust"),
    })
    server:attach_buffers()
    require("rust-tools").start_standalone_if_required()
  end,
}
```

同时创建 `lua/dap/nvim-dap/rust.lua` 文件，内容如下：

```lua
-- 注意：这里要修改为你的绝对路径
local extension_path =
  "/Users/nn/.local/share/nvim/site/pack/packer/start/vimspector/gadgets/macos/download/CodeLLDB/v1.6.10/root/extension/"
local codelldb_path = extension_path .. "adapter/codelldb"
local liblldb_path = extension_path .. "lldb/lib/liblldb.dylib"

return {
  adapter = require("rust-tools.dap").get_codelldb_adapter(codelldb_path, liblldb_path),
}
```

这个文件提供 rust-tools 需要的适配器的路径信息，仔细看一下路径，就是我们上边用 vimspector 安装的 CodeLLDB 的路径，默认在 vimspector 插件目录下， 这个路径非常重要，需要**修改成 CodeLLDB 在你系统中的绝对路径** ，不同操作系统目录也会不同，请实际去目录中查看。

接着我们去设置快捷键，在 `lua/keybindings.lua` 中增加：

```lua
-- nvim-dap
pluginKeys.mapDAP = function()
  -- 开始
  map("n", "<leader>dd", ":RustDebuggables<CR>", opt)
  -- 结束 (dapui无法自动关闭可能是bug，手动关闭能想到的一切)
  map(
    "n",
    "<leader>de",
    ":lua require'dap'.close()<CR>"
      .. ":lua require'dap'.terminate()<CR>"
      .. ":lua require'dap.repl'.close()<CR>"
      .. ":lua require'dapui'.close()<CR>"
      .. ":lua require('dap').clear_breakpoints()<CR>"
      .. "<C-w>o<CR>",
    opt
  )
  -- 继续
  map("n", "<leader>dc", ":lua require'dap'.continue()<CR>", opt)
  -- 设置断点
  map("n", "<leader>dt", ":lua require('dap').toggle_breakpoint()<CR>", opt)
  map("n", "<leader>dT", ":lua require('dap').clear_breakpoints()<CR>", opt)
  --  stepOver, stepOut, stepInto
  map("n", "<leader>dj", ":lua require'dap'.step_over()<CR>", opt)
  map("n", "<leader>dk", ":lua require'dap'.step_out()<CR>", opt)
  map("n", "<leader>dl", ":lua require'dap'.step_into()<CR>", opt)
  -- 弹窗
  map("n", "<leader>dh", ":lua require'dapui'.eval()<CR>", opt)
end
```

方便起见，我这里设置的快捷键与 vimspector 的快捷键一模一样，增加了一个 `<leader>dh` 弹窗查看变量值，由于与vimsector 快捷键一样，我们可以用同样的方式测试一下。

1. `<leader>dt` 创建断点 （大红点）
2. `<leader>dd` 启动 debug
3. `<leader>dj` step over
4. `<leader>de` 结束 debug

![17-7.gif](/529e1cb26fa04935965cf8f759f6771dtplv-k3u1fbpfcp-zoom-in-crop-mark3024000.awebp)

Okay，本节就到此结束了，下一节是最后一节了，会对整个小册作个总结，把剩下没有讲到组件做一个简单的介绍，并把网友常问的问题进行一个整理，方便后边的同学参考，谢谢支持。

欢迎到 [小册的 GitHub 代码库](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 中发PR，持续改进配置。



# 18.结语与常见问题解答

首先恭喜你终于完成了此小册的所有配置，如果你坚持读到这里，那么你应该已经了解 Neovim 的配置原理，并且已经有了一个相对可用的开发环境了。

Neovim 是一个不断发展的开发工具，围绕其的插件也在不断更新，但它始终只是一个开发工具，不必神话它，你如果觉得实在麻烦，大可用回 `VSCode`，目前我也是两者都在使用之中。

但如果你骨子里就是一个爱折腾的人，想做那一小撮最靓的极客，那么这里只是你的第一步，你可以更加深入学习 Lua 语言的特性，苦读 Neovim 的 API 文档，寻找并尝试更多的插件，研究开源社区中其他配置版本各种各样的思路，来扩展和更新我们的版本，或者苦练手速，熟记更大量的快捷键，早日成为真正的大师。

在这里先回顾一下本小册的配置思路，我觉得是非常易懂易扩展的。

## 配置回顾

我们将 `init.lua` 作为**入口文件**，这里列出了所有用到的配置文件，如果这里没有列出来，那么一定是还没有生效的。这样当你需要添加或删除一个功能的时候，可以非常方便的这里调整。

由于脚本是从上至下顺序执行的，所以这里的引入顺序很重要。第一个引入的文件是 `basic.lua`，用于重置 Neovim 的**基础配置**，更加符合人类的使用习惯。

接着我们将所有**快捷键**的设置全部都放在 `keybindings.lua` 中，任何快捷键的调整，包含第三方插件的快捷键，都可以在这一个地方统一调整。

在这个文件中，我们先调用 `vim.api.nvim_set_keymap` 设置了**常见的快捷键**。对于不能立刻设置，需要等待**特定时机**设置的快捷键，我们在 return 的 pluginKeys Table 中定义了对应的函数，在指定的时机，任意位置都可以调用`require("keybindings).xxx()` ，这样就可以绑定对应的快捷键了。

接着我们用 `plugins.lua` **管理插件的安装卸载**，并且设置了自动命令，修改并保存此文件会自动安装对应插件。如果未来你需要**添加插件**，第一个应该想到就是到这个文件中添加。

通常每个插件对应一个配置文件，我们将**插件的配置文件**统一放在了 `plugin-config/` 文件夹中， 在这个文件夹里的文件，添加删除是常事，所以我们用 `pcall` 捕获了 `require` 插件错误，这样如果这个配置文件被引用了，但 这个插件并没安装成功，或已经被删除了，也不会让 Neovim 崩溃。

然后我们创建的单独的 `lsp/` 文件夹用于放置 **LSP 相关的的配置**，在 `lsp/setup.lua` 中，我们用 `nvim-lsp-installer` 来管理 Language Server 的安装卸载，手动加载 `lsp/confg/` 子目录的各种语言配置文件来增加不同的编程语言。

在 `lsp/cmp.lua` 中配置了**自动补全**功能，在 `lsp/formatter.lua` 中配置了专门的**代码格式化**插件，之后我们又改成了 `lsp/null-ls.lua` 来代替 LSP 的格式化方法。

最后我们又创建了 `dap/` 文件夹用于保存**断点调试**相关的配置，两个流行的插件分别在 `dap/vimspector/` 中， 和 `dap/nvim-dap/` 文件中，我们将两个工具设置了相同的一套快捷键，建议在 init.lua 中任选一种使用。



## 还有哪些没有讲到？

Neovim 是一个开放的世界，不断会有新的插件出现，我们不可能把所有的插件都研究一遍，而且大部分插件基本上不需要配置，使用默认的配置就够了。这里介绍一没有说到的插件，并提供配置文件相信你可以自己搞得定。

**nvim-autopairs** 插件可以自动补充后一半的括号，见图：

![18-4.gif](/08c35600af6644d396c05d732c993908tplv-k3u1fbpfcp-zoom-in-crop-mark3024000.awebp)

配置文件 [nvim-autopairs.lua](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua%2Fblob%2Fmain%2Flua%2Fplugin-config%2Fnvim-autopairs.lua)，在入口文件引入即可。

**Comment.nvim** 快速注释代码

![18-5.gif](/074a6ccdba1c4219a41e385b014ef5edtplv-k3u1fbpfcp-zoom-in-crop-mark3024000.awebp)

我在 `keybindings.lua` 定义了 gcc 快捷键作为行注释，gbc 快捷键作为块注释

```lua
-- 代码注释插件
-- see ./lua/plugin-config/comment.lua
pluginKeys.comment = {
  -- Normal 模式快捷键
  toggler = {
    line = "gcc", -- 行注释
    block = "gbc", -- 块注释
  },
  -- Visual 模式
  opleader = {
    line = "gc",
    bock = "gb",
  },
}
```

配置文件 [comment.lua](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua%2Fblob%2Fmain%2Flua%2Fplugin-config%2Fcomment.lua)，在入口文件引入即可。

**surround.nvim**

surround.nvim 插件会增加几个快捷键，我常用的有：

- `ds<char>`
- `cs<from><to>`
- `ys{motion}{char}`

![18-6.gif](/d61ed1e201d34834b0576d173d5e9b2dtplv-k3u1fbpfcp-zoom-in-crop-mark3024000.awebp)

配置文件 [surround.lua](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua%2Fblob%2Fmain%2Flua%2Fplugin-config%2Fsurround.lua)，在入口文件引入即可。

### 输入法自动切换

我们希望进入 Normal 模式时自动切换为英文输入法，而进入到 Insert 模式时切换回之前输入时所用的输入法。

我们可以增加一条自动命令：

```lua
local myAutoGroup = vim.api.nvim_create_augroup("myAutoGroup", { clear = true, })
local autocmd = vim.api.nvim_create_autocmd
-- 自动切换输入法
autocmd("InsertLeave", {
  group = myAutoGroup,
  callback = require("utils.im-select").macInsertLeave,
})
autocmd("InsertEnter", {
  group = myAutoGroup,
  callback = require("utils.im-select").macInsertEnter,
})
```

InserLeave 和 InsertEnter 时调用一个 im-select 脚本，这个脚本会自动切换输入法。

注意上述代码是 Mac 系统调用的 macInsertLeave / macInsertEnter , Windows 系统应改为 winInsertLeave / winInsertEnter。

`lua/utils/im-select.lua` 代码如下：

```lua
local M = {}

M.defaultIM = "com.apple.keylayout.ABC"
M.currentIM = M.defaultIM

M.macInsertLeave = function()
  M.currentIM = vim.fn.system({ "im-select" })
  vim.cmd(":silent :!im-select" .. " " .. M.defaultIM)
end

M.macInsertEnter = function()
  if M.currentIM then
    vim.cmd(":silent :!im-select" .. " " .. M.currentIM)
  else
    vim.cmd(":silent :!im-select" .. " " .. M.defaultIM)
  end
end

M.windowsInsertLeave = function()
  vim.cmd(":silent :!~/.config/nvim/im-select.exe 1033")
end

M.windowsInsertEnter = function()
  vim.cmd(":silent :!~/.config/nvim/im-select.exe 2052")
end
return M
```

注意这个脚本需要依赖 [im-select](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdaipeihust%2Fim-select)。

mac 系统安装

```bash
brew tap daipeihust/tap && brew install im-select
```

Windows 系统下载 [im-select.exe](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdaipeihust%2Fim-select%2Fraw%2Fmaster%2Fim-select-win%2Fout%2Fx86%2Fim-select.exe) 到 nvim 目录下，并且在设置中添加英语语言，具体方法为:

> Windows设置 > 时间和语言 > 语言下，找到首选语言，点 + 号添加语言，选择英语（美国），只需要基本包即可，手写识别、语音识别可以不需要。

完整代码请参考 小册 GitHub 仓库:

- [/lua/utils/im-select.lua](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua%2Fblob%2Fmain%2Flua%2Futils%2Fim-select.lua)
- [/lua/autocmds.lua](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua%2Fblob%2Fmain%2Flua%2Fautocmds.lua)

## 常见疑难问题解答

我在编写小册的过程中收到了很多反馈，以下问题是问得最多的，我将其整理出来：

### 如何卸载插件?

打开 `lua/plugins.lua` 文件，找到要卸载的插件，注释掉，`:w` 保存文件，被询问是否删除，输入 y 回车即可。

![18-1.gif](/4e3e4bcc62de4a49b1fbeb333a2c9bcctplv-k3u1fbpfcp-zoom-in-crop-mark3024000.awebp)

### 为什么插件明明安装成功了，配置文件却莫名报错找不到插件？

通常是安装插件时遇到网络错误，导致实际上并没有真正的安装成功，参考上一个问题先卸载，再重新安装。

### 插件全部安装失败，如何解决？

插件安装失败通常都是因为国内网络环境的问题，基本上有两种方式解决：

第一种就是挂全局代理，或者在代理软件上复制终端命令到系统相应位置，在 windows wsl2 挂代理有些复杂，可以到这里参考 [我的配置](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua%2Fdiscussions%2F45)。

第二种就是使用镜像站点，取消下边注释中任意一行后保存，重新安装。

```lua
  -- 自定义源
    git = {
      -- default_url_format = "https://hub.fastgit.xyz/%s",
      -- default_url_format = "https://mirror.ghproxy.com/https://github.com/%s",
      -- default_url_format = "https://gitcode.net/mirrors/%s",
      -- default_url_format = "https://gitclone.com/github.com/%s",
      -- default_url_format = "git@github.com:%s" -- 换用 git 协议
    },
```

完整代码参考： [/lua/plugins.lua#L150-L156](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua%2Fblob%2F18fe3947671088bc70a7ef75d6d2ca82c7ac0444%2Flua%2Fplugins.lua%23L150-L156)

### 总有一个插件更新失败

参考上边如何卸载插件，先卸载，再重新安装即可。

### Mac 系统没有 Alt 键，Option 键也不管用，如何设置 Command 快捷键？

在我们的配置中，Mac 系统的 Option 键对应的是 Windows 系统的 Alt 键，如果你的 Option 键没有反应，通常需要设置一下你的终端，将 Option 键设置为 Meta 键。

Item2 设置方式为 `Preference -> Profiles -> Default --> Keys --> Left Option key --> 选中 Esc+`

![18-2.png](/29c2446988a84cad857f4ddd2eb02040tplv-k3u1fbpfcp-zoom-in-crop-mark3024000.awebp)

Alacritty 设置方式参考 [我的配置文件中](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Fdotfiles%2Fblob%2Fmain%2F.alacritty.yml) `# Alt Meta key` 的部分

另外 Neovim 中 是无法识别到 Command 键的。

### windows 的 ubuntu 子系统下安装插件报错 `could not find executable "unzip" in path`?

因为缺少压缩解压软件，需要安装 zip unzip。

```bash
sudo apt-get install zip unzip
```

### 在 Windows 10 中如何将 Neovim 中的内容复制到系统剪贴板？

我们可以创建一个简单的脚本 `fix-yank.lua` 并在入口文件中引入，如下：

```lua
vim.cmd([[
augroup fix_yank
    autocmd!
    autocmd TextYankPost * if v:event.operator ==# 'y' | call system('/mnt/c/Windows/System32/clip.exe', @0) | endif
augroup END
]])
```

上述代码意思大概是每次 y 复制后把内容传给 windows 自带的 clip.exe 中，达到复制的目的。

### 在 Windows 10 中如何将系统剪切板中的内容粘贴到 Neovim 中？

可以打开 Terminal，选择 `设置 --> 操作 --> 粘贴` 设置粘贴的快捷键.

![18-3.webp](/34dce465c24747198f0272da519f41b3tplv-k3u1fbpfcp-zoom-in-crop-mark3024000.awebp)

如有更多问题欢迎留言，我会继续更新。

另外记得关注我们 [GitHub 上小册的配套代码](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnshen%2Flearn-neovim-lua) 未来代码还会持续的改进。

关注我的 [掘金个人主页](https://juejin.cn/user/1873223543167326) ，未来我也会在上边写一些 Neovim 相关的文章。

最后再次感谢支持，江湖再见！

# 从 nvim-lsp-installer 升级到 mason.nvim 

[Introducing mason.nvim · Discussion #876 · williamboman/nvim-lsp-installer · GitHub](https://github.com/williamboman/nvim-lsp-installer/discussions/876)

mason.nvim 是 nvim-lsp-installer 的下一代版本，现有的 nvim-lsp-installer 将不再维护，所以我们还是有必要升级一下的，本文将分享一下我的升级过程。

好了开始正文，最近每次我们使用 `:LspInstallInfo` 打开 **nvim-lsp-installer** 的时候都会在最上边看到两行网址。

![image.png](/a7984f06abad4a6ab1c4a469a0423c7ftplv-k3u1fbpfcp-zoom-in-crop-mark4536000.awebp)

在这个[网址中](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Fwilliamboman%2Fnvim-lsp-installer%2Fdiscussions%2F876) 作者介绍了 **mason.nvim** 项目的情况，简单来讲就是未来会用 **mason.nvim** 取代 **nvim-lsp-installer**，并且支持更多的 server 安装，不仅仅是LSP Server 还支持 DAP servers、 linters、formatters 等等超过 150 个包，100+ 种编程语言，并且升级也是非常简单的，下面就开始吧。

1. 第一步卸载所有已经安装的Lsp servers，这是因为 mason.nvim 与 nvim-lsp-installer 的文件结构不兼容。确保卸载以释放磁盘空间。建议跟我上边一样截个图先，记住都装过什么，一会儿还要再装回来。运行`:LspUninstallAll` 命令卸载。

![image.png](/5e1956478b2149dabf21b8c42d4d597atplv-k3u1fbpfcp-zoom-in-crop-mark4536000.awebp)

上图的目录就是之前安装 lsp servers 的目录，y 回车会清空这个目录。

1. 打开 `lua/plugins.lua` 替换 **nvim-lsp-installer** 插件为 **mason.nvim** 和 **mason-lspconfig.nvim**

```lua
    use({ "williamboman/mason.nvim" })
    use({ "williamboman/mason-lspconfig.nvim" })
复制代码
```

![image.png](/7c2754b162f340b894e7da85603bb1datplv-k3u1fbpfcp-zoom-in-crop-mark4536000.awebp)

保存自动安装，或者运行 `:PackerSync`

1. 找到 `lua/lsp/setup.lua` 删掉最上边的 nvim-lsp-installer 的配置部分

```lua
----------------------------------------删掉这部分
require("nvim-lsp-installer").setup({
  -- 自动安装 Language Servers
  automatic_installation = true,
})
----------------------------------------删掉这部分
复制代码
```

修改为

```lua
-- :h mason-default-settings
require("mason").setup({
  ui = {
    icons = {
      package_installed = "✓",
      package_pending = "➜",
      package_uninstalled = "✗",
    },
  },
})

-- mason-lspconfig uses the `lspconfig` server names in the APIs it exposes - not `mason.nvim` package names
-- https://github.com/williamboman/mason-lspconfig.nvim/blob/main/doc/server-mapping.md
require("mason-lspconfig").setup({
  -- 确保安装，根据需要填写
  ensure_installed = {
    "sumneko_lua",
    "tsserver",
    "cssls",
    "emmet_ls",
    "html",
    "jsonls",
  },
})
```

保存即可，mason 默认将 lsp 安装到新的位置 `~/.local/share/nvim/mason`

![image.png](/e7be2dac858d4aecad27c7eeedcb826dtplv-k3u1fbpfcp-zoom-in-crop-mark4536000.awebp)

重启！

![image.png](/331ca16e29f14ca8812d94e0fbfd6fddtplv-k3u1fbpfcp-zoom-in-crop-mark4536000.awebp)

输入命令 `:Mason` 哒哒！

![image.png](/029c7c3dde994fb19dd306b7ba8c8947tplv-k3u1fbpfcp-zoom-in-crop-mark4536000.awebp)

和之前用法基本一致，多了 1，2，3，4，5 是上边TAB快捷键，按 `2` 即可切换到 LSP，可以在这里选择需要安装的，按 `i` 进行安装。

本文结束🙏



作者：nshen
链接：https://juejin.cn/post/7154005621887631396
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# 新增

## 快捷键

### 保存文件

```lua

-- ...
-- ...

map('n', '<C-s>', ':w<CR>', opt)
map('i', '<C-s>', '<ESC>:w<CR>a', opt)
```

进入终端模式

保存当前打开过的所有buffer，下次再进来时都打开



鼠标框选

### null-ls.lua

vue文件的格式化

```lua
-- 保存自动格式化
    on_attach = function(client)
        -- vim.cmd([[ command! Format execute 'lua vim.lsp.buf.format({ async = true })']])
        --if client.resolved_capabilities.document_formatting then
        if client.server_capabilities.documentFormattingProvider then
            vim.cmd('autocmd BufWritePre <buffer> lua vim.lsp.buf.format({async = true})')
        end
    end,
```



