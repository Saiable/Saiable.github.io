---
title: 'Neovim IDE 搭建系列'
cover: false
---





> 来源链接：[Neovim IDE 搭建系列（01） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/469355805)

# **Neovim IDE 搭建系列（01）**

## **前言**

我是一名 Python 开发者，最早的时候使用 Pycharm 进行开发，后来大概使用了一年多的 vscode，由于受不了 vscode 以及 Pycharm 的卡顿，所以在不久前我转到了 neovim 阵营。

得益于 LSP 以及 DAP 的加持，目前 neovim 的编码体验已经不输于 vscode 了，高效的全键盘操作能够让你的思维不会因为寻找鼠标而中断，这也是我热爱 neovim 最重要的一个原因。

鉴于目前这部分中文资料较少，所以在此想对加入 neovim 大家庭而又畏惧繁琐配置的朋友提供一份快速搭建的指南，如果您觉得这个系列对您有帮助，不妨点个关注 ～

预计在未来一周内将会全部更新完毕，感谢阅读。



## **配置范围**

个人平常会使用的语言如下，如果你也使用这些语言，那么是完全可以用 neovim 进行开发的：

- Python3
- Golang
- Lua
- NodeJs
- HTML
- CSS
- JavaScript
- TypeScript
- Vue



## **拟定目录**

配置过程大概分为以下几个步骤：

- 基本配置
- 美化配置
- 编辑配置
- 功能配置
- LSP 配置
- DAP 配置
- 其他配置

刚好 7 天，一天一个板块，目前我的插件数量是 68，没做任何优化，在 16 年的老电脑上启动时间大约 100 毫秒，比 vscode 快了很多倍。



## **准备工作**

在开始之前，需要确保安装以下一些外部依赖：

- neovim（至少大于 0.5 版本）
- python3 以及 pip3
- tar、curl、git、gzip、wget
- gcc 以及 g++ （用于 [nvim-treesitter](https://link.zhihu.com/?target=https%3A//github.com/nvim-treesitter/nvim-treesitter) 的依赖安装）
- nerd font（正确显示图标）
- node 以及 npm（用于 LSP 服务，可选）
- [fd](https://link.zhihu.com/?target=https%3A//github.com/sharkdp/fd) 以及 [ripgrep](https://link.zhihu.com/?target=https%3A//github.com/BurntSushi/ripgrep) （用于 telescope 模糊查找）
- [sed](https://link.zhihu.com/?target=https%3A//www.gnu.org/software/sed/) （用于 [nvim-spectre](https://link.zhihu.com/?target=https%3A//github.com/nvim-pack/nvim-spectre) 的全局字符串替换）

由于我使用的是 Linux （manjaro），所以安装它们都非常简单，推荐 windows 用户在 WSL 下安装，这样会省掉很多繁琐的步骤。



## **配置目录**

neovim 现在支持 vimscript 和 lua 这 2 种语言书写配置，个人使用纯 lua 语言，它能够更加方便的管理多个插件。

neovim 的配置文件放在 ~/.config/nvim/init.lua 中，可按照下面的目录结构创建相关目录：

```text
/home/askfiy/.config/nvim
├── init.lua
├── ftplugin/
├── lint/
├── lua/
│   ├── basic/
│   │   ├── config.lua
│   │   ├── keybinds.lua
│   │   ├── plugins.lua
│   │   └── settings.lua
│   ├── conf/
│   ├── dap/
│   └── lsp/
└── snippet/
```

目录说明：

- ftplugin：存放不同文件类型的缩进规则文件
- lint：存放各种语言的代码检查规范配置文件，如 pylint 等
- basic：存放基本配置项文件
- conf：存放插件相关配置文件
- dap：存放 DAP 相关配置文件
- lsp：存放 LSP 相关配置文件
- snippet：存放代码片段相关文件

文件说明：

- init.lua：配置入口文件
- config.lua：存放用户自定义配置的文件
- keybinds.lua：存放键位绑定的文件
- plugins.lua：存放依赖插件的文件
- settings.lua：存放 neovim 基本配置项的文件



## **部分功能展示**

目录树、重做树、大纲预览、各种终端：



![img](https://pic2.zhimg.com/80/v2-d104657704ebf761f2951d9ea66ad325_720w.jpg)



语法提示、代码补全、工作区诊断、问题跳转：



![img](https://pic2.zhimg.com/v2-23eb7d98dc634fb0ee10ec4466d3a441_b.jpg)





代码调试：



![img](https://pic3.zhimg.com/v2-d459614e95c11981576edf6c34f425d6_b.jpg)





代码快速格式化：



![img](https://pic4.zhimg.com/v2-de9eb320a3caefb82a83513d6c5609d7_b.jpg)





自定义代码片段（和 vscode 一样的配置方式，很方便）：



![img](https://pic2.zhimg.com/80/v2-491c52672e7f02abefba1343e3603e5d_720w.jpg)



tabnine 和 git copilot 等 AI 代码补全：



![img](https://pic1.zhimg.com/v2-ab2936e0768ffc2d0101580b61658928_b.jpg)





快速跳转到词、行、列：



![img](https://pic2.zhimg.com/v2-c0f6b00645bf4ee32c8df643c03c3f95_b.jpg)





项目模糊查找、文件查找、标签查找：



![img](https://pic1.zhimg.com/v2-d0da4a2695f374f68d14897e18eb5d04_b.jpg)





各种漂亮的主题：



![img](https://pic2.zhimg.com/80/v2-fa635dcc7a4bf866ad9b4db958939f89_720w.jpg)

![img](https://pic1.zhimg.com/80/v2-0036431adf0b423290c43c0c73a7d2e0_720w.jpg)

# **Neovim IDE 搭建系列（02）**

## **安装 neovim**

为了和大家一样从头开始配置 neovim，我特意准备了一个 Ubuntu 的虚拟机。

首先第一步是安装 neovim，Ubuntu 如果用 apt 安装 neovim 其实版本是非常低的，所以我们从 neovim 官网直接安装最新版本的 neovim。

跳转到 neovim 稳定版本下载页面：[点我跳转](https://link.zhihu.com/?target=https%3A//github.com/neovim/neovim/releases/latest)



![img](https://pic4.zhimg.com/80/v2-589a950b18f52c587c0f799bf7099297_720w.jpg)



复制出链接地址，然后使用 wget 下载：

```text
$ cd ~
$ wget https://github.com/neovim/neovim/releases/download/v0.6.1/nvim-linux64.tar.gz
```

下载完成后安装：

```text
$ sudo tar -xvf ~/nvim-linux64.tar.gz -C /usr/local/
```

将 neovim 添加至环境变量：

```text
$ vi ~/.bashrc
```

粘贴以下内容：

```text
export PATH=/usr/local/nvim-linux64/bin:$PATH
```

退出 vi，然后刷新配置：

```text
$ source ~/.bashrc
```

输入 nvim，应该可以看见主界面了：



![img](https://pic3.zhimg.com/80/v2-ed9ac28972505a148459da5b4fd09ea6_720w.jpg)







## **创建目录**

创建 neovim 配置目录，直接复制粘贴：

```text
$ mkdir -p ~/.config/nvim/{ftplugin,lint,lua,snippet}
$ mkdir -p ~/.config/nvim/lua/{basic,conf,dap,lsp}
$ touch ~/.config/nvim/init.lua
$ touch ~/.config/nvim/lua/basic/config.lua
$ touch ~/.config/nvim/lua/basic/keybinds.lua
$ touch ~/.config/nvim/lua/basic/plugins.lua
$ touch ~/.config/nvim/lua/basic/settings.lua
```

最终目录结构如下所示：

```text
/home/askfiy/.config/nvim/
├── ftplugin
├── init.lua
├── lint
├── lua
│   ├── basic
│   │   ├── config.lua
│   │   ├── keybinds.lua
│   │   ├── plugins.lua
│   │   └── settings.lua
│   ├── conf
│   ├── dap
│   └── lsp
└── snippet
```

每个目录、文件的功能及用途可参照本系列第一篇的介绍，这里不再重复说明。



## **init.lua**

在 Lua 中，通过 require 方法，可以导入其它模块。

而 init.lua 是整个配置的入口文件，当 neovim 启动时会自动加载该文件。

所以我们需要在 init.lua 中导入 lua/basic 目录下的 4 个 Lua 文件，复制粘贴以下代码到 init.lua 文件中：

```text
$ nvim ~/.config/nvim/init.lua 

-- 加载配置项  
require("basic.settings")
require("basic.keybinds")
require("basic.config")
require("basic.plugins")
```





## **基础设置**

neovim 的基础设置如下，打开 lua/basic/settings.lua 填入以下内容：

```text
$ nvim ~/.config/nvim/lua/basic/settings.lua 

-- 设定各种文本的字符编码
vim.o.encoding = "utf-8"
-- 设定在无操作时，交换文件刷写到磁盘的等待毫秒数（默认为 4000）
vim.o.updatetime = 100
-- 设定等待按键时长的毫秒数
vim.o.timeoutlen = 500
-- 是否在屏幕最后一行显示命令
vim.o.showcmd = true
-- 是否允许缓冲区未保存时就切换
vim.o.hidden = true
-- 是否开启 xterm 兼容的终端 24 位色彩支持
vim.o.termguicolors = true
-- 是否高亮当前文本行
vim.o.cursorline = true
-- 是否开启语法高亮
vim.o.syntax = "enable"
-- 是否显示绝对行号
vim.o.number = true
-- 是否显示相对行号
vim.o.relativenumber = true
-- 设定光标上下两侧最少保留的屏幕行数
vim.o.scrolloff = 10
-- 是否支持鼠标操作
vim.o.mouse = "a"
-- 是否启用系统剪切板
vim.o.clipboard = "unnamedplus"
-- 是否开启备份文件
vim.o.backup = false
-- 是否开启交换文件
vim.o.swapfile = false
-- 是否特殊显示空格等字符
vim.o.list = true
-- 是否开启自动缩进
vim.o.autoindent = true
-- 设定自动缩进的策略为 plugin
vim.o.filetype = "plugin"
-- 是否开启高亮搜索
vim.o.hlsearch = true
-- 是否在插入括号时短暂跳转到另一半括号上
vim.o.showmatch = true
-- 是否开启命令行补全
vim.o.wildmenu = true
-- 是否在搜索时忽略大小写
vim.o.ignorecase = true
-- 是否开启在搜索时如果有大写字母，则关闭忽略大小写的选项
vim.o.smartcase = true
-- 是否开启单词拼写检查
vim.o.spell = true
-- 设定单词拼写检查的语言
vim.o.spelllang = "en_us,cjk"
-- 是否开启代码折叠
vim.o.foldenable = true
-- 指定代码折叠的策略是按照缩进进行的
vim.o.foldmethod = "indent"
-- 指定代码折叠的最高层级为 100
vim.o.foldlevel = 100
```

注意，若想让 neovim 共享系统剪切板，还需要下载一个插件：

```text
$ sudo apt install xsel
```

具体各个配置项的作用可通过 help 命令查询，如 :h hidden：



![img](https://pic1.zhimg.com/80/v2-328539cbe53eff72394d0a110490ca48_720w.jpg)









## **键位设置**

个人不太喜欢将默认的键位做太多更改，所以对默认键位只做了非常简单的配置：

```text
$ nvim ~/.config/nvim/lua/basic/keybinds.lua 

-- leader 键设置为空格                                    
vim.g.mapleader = " "    
    
-- 默认的键位设置函数太长了，所以这里将它们重新引用一下
vim.keybinds = {    
    gmap = vim.api.nvim_set_keymap,    
    bmap = vim.api.nvim_buf_set_keymap,    
    dgmap = vim.api.nvim_del_keymap,    
    dbmap = vim.api.nvim_buf_del_keymap,    
    opts = {noremap = true, silent = true}    
}    
    
-- 插入模下 jj 退出插入模式    
vim.keybinds.gmap("i", "jj", "<Esc>", vim.keybinds.opts)    
    
-- 用 H 和 L 代替 ^ 与 $    
vim.keybinds.gmap("n", "H", "^", vim.keybinds.opts)    
vim.keybinds.gmap("v", "H", "^", vim.keybinds.opts)    
vim.keybinds.gmap("n", "L", "$", vim.keybinds.opts)    
vim.keybinds.gmap("v", "L", "$", vim.keybinds.opts)    
    
-- 将 C-u 和 C-d 调整为上下滑动 10 行而不是半页    
vim.keybinds.gmap("n", "<C-u>", "10k", vim.keybinds.opts)    
vim.keybinds.gmap("n", "<C-d>", "10j", vim.keybinds.opts)    
    
-- 插入模式下的上下左右移动    
vim.keybinds.gmap("i", "<A-k>", "<up>", vim.keybinds.opts)    
vim.keybinds.gmap("i", "<A-j>", "<down>", vim.keybinds.opts)    
vim.keybinds.gmap("i", "<A-h>", "<left>", vim.keybinds.opts)    
vim.keybinds.gmap("i", "<A-l>", "<right>", vim.keybinds.opts)    
    
-- 修改分屏大小    
vim.keybinds.gmap("n", "<C-up>", "<cmd>res +1<CR>", vim.keybinds.opts)    
vim.keybinds.gmap("n", "<C-down>", "<cmd>res -1<CR>", vim.keybinds.opts)    
vim.keybinds.gmap("n", "<C-left>", "<cmd>vertical resize-1<CR>", vim.keybinds.opts)    
vim.keybinds.gmap("n", "<C-right>", "<cmd>vertical resize+1<CR>", vim.keybinds.opts)    
    
-- 正常模式下按 ESC 取消高亮显示    
vim.keybinds.gmap("n", "<ESC>", ":nohlsearch<CR>", vim.keybinds.opts)    
    
-- 通过 leader cs 切换拼写检查    
vim.keybinds.gmap("n", "<leader>cs", "<cmd>set spell!<CR>", vim.keybinds.opts)   
```





## **输入法设置**

个人使用的是 Fcitx 框架，所以直接可以自己写一个函数让 neovim 在退出插入模式时切换到英文输入法。

打开 lua/basic/config.lua，填入以下内容

```text
$ nvim ~/.config/nvim/lua/basic/config.lua 

-- 自动切换输入法（Fcitx 框架）
vim.g.FcitxToggleInput = function()
    local input_status = tonumber(vim.fn.system("fcitx-remote"))
    if input_status == 2 then
        vim.fn.system("fcitx-remote -c")
    end
end

vim.cmd("autocmd InsertLeave * call FcitxToggleInput()")
```

如果是 Windows 或者 Mac 平台，可以搜索 [im-select](https://link.zhihu.com/?target=https%3A//github.com/daipeihust/im-select) 并安装，而后自行寻找其它教程配置，这里不再举例。





## **ftplugin 配置**

不同类型的文件有不同的缩进规则，比如在 Python 中缩进是 4 个空格，而在 Golang 中是 1 个 tab。

基础设置时，我们在 lua/basic/settings.lua 中配置了这样的一个选项：

```text
-- 自动缩进的策略为 plugin
vim.o.filetype = "plugin"
```

接下来需要在 ~/.config/nvim/ftplugin 目录中新建不同语言的缩进规则文件，如图所示：



![img](https://pic1.zhimg.com/80/v2-c545beb17a5ba7653020d512ab2b7bdc_720w.jpg)



然后根据语言的缩进规则来书写不同的内容，以 go.lua 为例：

```text
-- 是否将 tab 替换为 space
vim.bo.expandtab = false
-- 换行或 >> << 缩进时的 space 数量    
vim.bo.shiftwidth = 4    
-- 一个 tab 占用几个 space    
vim.bo.tabstop = 4    
-- tab 和 space 的混合，和上面 2 个设置成相同即可    
vim.bo.softtabstop = 4   
```

同理，在 Lua 中的缩进规则是 4 个空格，那么 lua.lua 文件的内容就是下面这样：

```text
vim.bo.expandtab = true                     
vim.bo.shiftwidth = 4
vim.bo.tabstop = 4                     
vim.bo.softtabstop = 4 
-- 取消自动注释，当前行是 -- 注释时，按下 CR 或者 o 默认会自动注释下一行，所以这里取消了
vim.opt_local.formatoptions = vim.opt_local.formatoptions - {"c", "r", "o"}
```

除此之外，我们也可以为不同语言设置不同的空格以及回车样式，但是要确保 lua/basic/settings.lua 中的 list 配置项是打开的：

```text
-- 是否特殊显示空格等字符
vim.o.list = true
```

比如我想让 Golang 中的空格表现为 ⋅，回车表现为 ↴，那么就可以在 go.lua 中加入下面 2 行代码：

```text
vim.opt.listchars:append("space:⋅")
vim.opt.listchars:append("eol:↴")
```

在编辑 Golang 文件时，你会发现它们生效了：



![img](https://pic1.zhimg.com/80/v2-fc0f89fef8f1fd1c8f2241ae2cea9630_720w.jpg)





## **本章节的话**

如果你之前使用过 vimscript 但对 Lua 并不熟悉的话，可以参照 [在 neovim 中使用 Lua](https://link.zhihu.com/?target=https%3A//github.com/glepnir/nvim-lua-guide-zh) 这份教程。

今后的配置不会很繁琐，能用 Lua 写的代码就会尽量用 Lua 来写，不会涉及太多深层次的东西。

ok，那么基础配置已经搞定了，后面会做一些美化让 neovim 看起来更酷一些。

如果您觉得对你有所帮助，烦请动动发财的小手，点波喜欢吧～