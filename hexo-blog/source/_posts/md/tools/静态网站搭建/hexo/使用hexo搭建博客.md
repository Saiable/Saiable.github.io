---
title: '使用hexo搭建博客'
date: 2022/7/8 07:15:24
cover: false
typora-root-url: 使用hexo搭建博客
---



# 基于`hexo`搭建博客

https://blog.csdn.net/qq_41356250/article/details/125148095

## 准备

教程一：https://www.bilibili.com/read/cv12633102，备份链接：https://note.youdao.com/s/1MLXUHou

教程二：https://tzy1997.com/articles/hexo1601/

- 



注意事项

很多命令既可以用Windows的cmd来完成，也可以使用git bash来完成，但是部分命令会有一些问题，为避免不必要的问题，建议全部使用git bash来执行

hexo不同版本差别比较大，网上很多文章的配置信息都是基于2.x的，所以注意不要被误导

hexo有2种_config.yml文件，一个是根目录下的全局的_config.yml，一个是各个theme下的

下载并安装node.js

官网下载：https://nodejs.org/en/

安装后配置全局变量，也可以使用nvm来管理

安装后验证：node -v

下载并安装git

官网下载:  https://git-scm.com/download/win

安装后验证：git -v



命令行安装cnpm（可跳过，直接使用node默认的包管理器npm）

命令：npm install -g cnpm --registry==https://registry.npm.taobao.org

安装后验证：cnpm -v



命令行安装hexo（注意版本问题，可与教程保持一致）

命令：cnpm install -g hexo-cli

安装后验证：hexo  -v

安装`hexo-cli`

```bash
npm install -g hexo-cli
```

注意，这里可以不用全局安装（方便后面迁移）

直接

```bash
npm install hexo-cli
```

**概要及补充**

- 域名不用备案，即使备案了由于DNS指向的是国外的，云服务商也会打电话给你让你，最后我取消域名备案了

- hexo生成的页面，我是提交到了仓库的pages分支，开发目录是在master，方便统一管理

  

  ![image-20230201101427347](image-20230201101427347.png)



### 配置github

在github上创建仓库

创建：

新建一个名为你的用户名.github.io的仓库

比如说，如果你的github用户名是test，那么你就新建test.github.io的仓库（必须是你的用户名，其它名称无效），将来你的网站访问地址就是 http://test.github.io 了，是不是很方便？由此可见，每一个github账户最多只能创建一个这样可以直接使用域名访问的仓库。

注意：

注册的邮箱一定要验证，否则不会成功；

仓库名字必须是：username.github.io，其中username是你的用户名；

仓库创建成功不会立即生效，需要过一段时间，大概10-30分钟，或者更久；

创建页面如下：


创建成功后，默认会在你这个仓库里生成一些示例页面，以后你的网站所有代码都是放在这个仓库里啦。



绑定域名（这步可省略）

当然，你不绑定域名肯定也是可以的，就用默认的 xxx.github.io 来访问，如果你想更个性一点，想拥有一个属于自己的域名，那也是OK的。

首先你要注册一个域名，域名注册以前总是推荐去godaddy，现在觉得其实国内的阿里云也挺不错的，价格也不贵，毕竟是大公司，放心！

绑定域名分2种情况：带www和不带www的。

域名配置最常见有2种方式，CNAME和A记录，CNAME填写域名，A记录填写IP，由于不带www方式只能采用A记录，所以必须先ping一下你的用户名.github.io的IP，然后到你的域名DNS设置页，将A记录指向你ping出来的IP，将CNAME指向你的用户名.github.io，这样可以保证无论是否添加www都可以访问，如下：


然后到你的github项目根目录新建一个名为CNAME的文件（无后缀），里面填写你的域名，加不加www看你自己喜好，因为经测试：

如果你填写的是没有www的，比如 mygit.me，那么无论是访问 http://www.mygit.me 还是 http://mygit.me ，都会自动跳转到 http://mygit.me

如果你填写的是带www的，比如 www.mygit.me ，那么无论是访问 http://www.mygit.me 还是 http://mygit.me ，都会自动跳转到 http://www.mygit.me

如果你填写的是其它子域名，比如 abc.mygit.me，那么访问 http://abc.mygit.me 没问题，但是访问 http://mygit.me ，不会自动跳转到 http://abc.mygit.me

另外说一句，在你绑定了新域名之后，原来的你的用户名.github.io并没有失效，而是会自动跳转到你的新域名。



配置SSH免密登录

为什么要配置这个呢？因为你提交代码肯定要拥有你的github权限才可以，但是直接使用用户名和密码太不安全了，所以我们使用ssh key来解决本地和服务器的连接问题。

操作步骤：

第一步：首先打开电脑文件夹，找到C:\Users\王海洋\.ssh文件夹并删除

第二步：在C:\Users\王海洋文件夹下右键打开Git Bash Here输入命令：ssh-keygen -t rsa -C github邮件地址   生成.ssh秘钥，输入后连敲三次回车，出现下图情况代表成功


第三步：最终生成了一个新的 C:\Users\王海洋\.ssh文件夹，打开这个文件夹，找到.ssh\id_rsa.pub文件，记事本打开并复制里面的内容

第四步：打开你的github主页，进入个人设置 -> SSH and GPG keys -> New SSH key，把复制的内容粘贴进去，title随便填，保存即可，我们的公钥就添加成功了，设置好如下图：


第五步：检测是否设置成功：

输入命令：  $ ssh -T git@github.com # 注意邮箱地址不用改

如果提示Are you sure you want to continue connecting (yes/no)?，输入yes，然后会看到：

Hi liuxianan! You've successfully authenticated, but GitHub does not provide shell access.

看到这个信息说明SSH已配置成功！

第六步：此时你还需要配置：

$ git config --global user.name "liuxianan"// 你的github用户名，非昵称$ git config --global user.email  "xxx@qq.com"// 填写你的github注册邮箱 



该小节作者：https://www.bilibili.com/read/cv12633102/ 

## 初始化

### 基本构建

https://tzy1997.com/articles/hexo1602/

```
npm install -g hexo-cli
hexo init blog-demo(项目名)
cd blog-demo  //进入blog-demo文件夹
npm i
```

结构：

```bash
【node_modules】：依赖包
【scaffolds】：生成文章的一些模板
【source】：用来存放你的文章
【themes】：主题
【.npmignore】：发布时忽略的文件（可忽略）
【_config.landscape.yml】：主题的配置文件
【_config.yml】：博客的配置文件
【package.json】：项目名称、描述、版本、运行和开发等信息
```

输入hexo server或者hexo s。查看页面（`source/_posts`文件夹下需要有`md`的文章，不然就是空页面）。`-p 8081`指定端口号

### 发布

上一篇文章中，我们已经完成了对 GitHub 账户的注册以及 Github Pages 的创建，并且为 GitHub 配置了 SSH key, 我们将博客部署到 GitHub Pages 上即可。

```bash
npm install hexo-deployer-git --save
```

在blog-demo目录下的_config.yml，就是整个Hexo框架的配置文件了。可以在里面修改大部分的配置。详细可参考官方的[配置描述](https://hexo.io/zh-cn/docs/configuration)（这里建议整体过一遍）。

修改最后一行的配置，将repository修改为你自己的github项目地址即可。

```yaml
deploy:
  type: git
  # repository: git@github.com:Saiable/saiable.github.io.git
  repository: https://github.com/Saiable/saiable.github.io.git
  branch: pages # 选择仓库的其他分支，github.io选择该分支

```

注意：如果是部署到子分支上，github设置时要选择子分支

修改好配置后，运行如下命令，将代码部署到 GitHub。

```bash
hexo clean
hexo generate
hexo deploy
```

解释：

```bash
hexo clean：删除之前生成的文件，若未生成过静态文件，可忽略此命令。
hexo generate：生成静态文章，可以用hexo g缩写
hexo deploy：部署文章，可以用hexo d缩写
```

可以通过`hexo clean && hexo generate`连接

### 安装主题

https://tzy1997.com/articles/hexo1603/

[Butterfly 安裝文檔(一) 快速開始 | Butterfly](https://butterfly.js.org/posts/21cfbf15/#安裝)

基于npm安装，[hexo-theme-butterfly - npm (npmjs.com)](https://www.npmjs.com/package/hexo-theme-butterfly)

- 要先安装nodejs，再通过`npm`下载主题

  ```bash
  npm i hexo-theme-butterfly
  ```

- 主题下载到`node_moudles`文件夹后，修改站点配置文件_config.yml，把主题改为butterfly

  ```yaml
  theme: butterfly
  ```

- 如果你没有pug以及stylus的渲染器，请下载安装：

  ```bash
  npm install hexo-renderer-pug hexo-renderer-stylus --save
  ```

- 为了减少升级主题后带来的不便，请使用以下方法（建议，可以不做）。

  把主题文件夹中的 `_config.yml `复制到 Hexo 根目录里，同时重新命名为 `_config.butterfly.yml`。

  以后只需要在 `_config.butterfly.yml`进行配置就行。

  `Hexo`会自动合併主题中的`_config.yml`和 `_config.butterfly.yml`里的配置，如果存在同名配置，会使用`_config.butterfly.yml`的配置，其优先度较高。

### 配置项

#### 插入图片

如何向hexo博客中插入图片

使用相对路径的方式

众所周知，在md文件中插入图片的语法为`![]()`。

其中方括号是图片描述，圆括号是图片路径。

一般来说有三种图片路径，分别是相对路径，绝对路径和网络路径。

所谓的网络路径就是直接引用网上的图片，直接复制图片地址，放在圆括号中就完事了。

这种方式十分的方便，但是也存在一定的问题：

图片失效导致无法加载；

打开网页后要再请求加载图片；

原网站限制，如微信公众号的图片会变得不可见等。

这种方式算是有利有弊。

绝对路径是图片在计算机中的绝对位置，相对路径是相对于当前文件的路径。

由于我们的博客是要部署在网站上，部署后会生成新的文件目录，所以我们选择使用相对路径的方式。

在hexo中使用文章资源文件夹需要在config.yaml文件中更改一下配置：

post_asset_folder: true

当该配置被应用后，使用hexo new命令创建新文章时，会生成相同名字的文件夹，也就是文章资源文件夹。


由于项目会生成新的文件目录，同时会解析Markdown中的图片路径，会导致一个问题。

如在一个文件目录下，博客名为1.md，相应的存在一个1文件夹存放图片image.jpg。

在Typora编辑器中，普通的md文件使用![](1/image.jpg)能在编辑器中正常显示图片。

在hexo中，按理说应该是使用`![](image.jpg)`，但网页中却无法正常显示。

此时应该使用这样的方式来引入图片：

`{% asset_img image.jpg 这是一张图片 %}`

虽然可以正常引用图片了，但是这种引用图片的方式只有一句话能形容，wtf。



` hexo-renderer-marked`插件的安装与配置

插件hexo-renderer-marked解决了这个问题

安装： npm install hexo-renderer-marked --save   ，之后在config.yaml中更改配置即可

之后就可以在使用 `![](image.jpg)`  的方式愉快的插入图片了。

我们做了这么多都是为了方便，那么为什么不再方便一点呢。

7.3 hexo-renderer-marked插件与Typora的完美结合

如果图片数量众多的话，一张一张的放很影响效率。但是不用怕，我们有很方便的解决方法。

Typora是我非常喜欢的Markdown文本编辑器，在之前的文章中也介绍过一点。

Typora对于插入图片的支持做得非常好，在文件->偏好设置或者直接<C-,>进入设置。

复制网络路径的图片：

使用该配置后，可以直接复制网页中的图片地址，粘贴到Typora中后，会直接复制该图片到文章资源文件夹，同时自动更改路径。

如复制网络路径的图片`https://...../image.jpg`粘贴到Typora中叫文章名的文章后，图片会自动变为`![](文章名/image.jpg)`。

但我们知道部署后，文件路径是不同的，所以当我们插入完所有的图片后，我们还需要删除每个图片路径中的文件名/。不慌，也很简单。

在Typora编辑器中，使用`<C-f>`快捷键，将所有的文章名/替换为空即可删除。

然后再将博客上传，图片就会随着文章一起打包。在网页中就可以看到正常显示的图片，大功告成。 

贴上实际使用的配置

![image-20231031064326228](/image-20231031064326228.png)

![image-20231031064401052](image-20231031064401052.png)

删除路径下的`/`即可，在`typora`中可正常显示。发布后也可正常显示

#### Front-matter

https://tzy1997.com/articles/hexo1604/

`Front-matter` 是 `markdown` 文件最上方以---分隔的区域，用于指定个别档案的变数。

`Page Front-matter` 用于页面配置

```bash
---
title:【必需】页面标题
date:【必需】页面创建日期
updated:
type:【必需】标籤、分类和友情链接三个页面需要配置
comments:
description:
keywords:
top_img:【可选】页面顶部图片
mathjax:
katex:
aside:
aplayer:
highlight_shrink:
---
```



`Post Front-matter` 用于文章页配置

```bash
---
title:
date:
updated:
tags:
categories:
keywords:
description:
top_img:
comments:
cover:【可选】文章缩略图(如果没有设置top_img,文章页顶部将显示缩略图，可设为false/图片地址/留空)
toc:【可选】显示文章TOC(默认为设置中toc的enable配置)
toc_number:【可选】显示toc_number(默认为设置中toc的number配置)
toc_style_simple:【可选】显示 toc 简洁模式
copyright:
copyright_author:
copyright_author_href:
copyright_url:
copyright_info:
mathjax:
katex:
aplayer:
highlight_shrink:
aside:
---
```

#### 标签页

前往你的Hexo博客根目录，打开cmd命令窗口执行`hexo new page tags`。

在`【BlogRoot/source/】`会生成一个含有`index.md`文件的`tags`文件夹。

修改`【BlogRoot/source/tags/index.md】`，添加`type: "tags"`。

```bash
---
title: tags
date: 2022-05-29 21:42:56
type: "tags"
---
```

注意：

- `title`可以是中文
- 可以通过`top_img`指定该页的通栏图片，[必应每日壁纸-必应之美由此开始 (plmeizi.com)](https://plmeizi.com/)
  - 图片最好放在自己的cdn上
    - sm.ms，国内访问smms.app
  - 文章的图片还是放在本地吧

#### 分类页

前往你的`Hexo`博客根目录，打开`cmd`命令窗口执行`hexo new page categories`。
在`【BlogRoot/source/】`会生成一个含有`index.md`文件的`categories`文件夹。

修改`【BlogRoot/source/categories/index.md】`，添加`type: "categories"`。

```bash
---
title: categories
date: 2022-05-29 21:57:07
type: "categories"
---
```

#### 友情链接

```bash
hexo new page link
```

`source/link/index.md`

```
---
title: link
date: 2022-05-29 22:03:35
type: "link"
---
```

友情链接页面添加友链信息

前往Hexo博客目录（【BlogRoot/source/_data】）创建一个文件link.yml（如果沒有 _data 文件夹，请自行创建）。

![image-20230201144608845](image-20230201144608845.png)

```yaml
- class_name: 思维启蒙
  class_desc: 那些人、那些事
  link_list:
    - name: 吕小布
      link: https://mindcons.cn/
      avatar: https://s2.loli.net/2022/07/02/xjocPR8fnLu64KU.png
      descr: 有意识的存在
    - name: 刘未鹏
      link: http://mindhacks.cn/
      avatar: https://s2.loli.net/2022/07/26/cFoRLZe6EfYKGOX.png
      descr: 思维改变生活

- class_name: 网站
  class_desc: 值得推荐的网站
  link_list:
    - name: ECMA-262
      link: https://www.ecma-international.org/publications-and-standards/standards/ecma-262/
      avatar: https://s2.loli.net/2022/07/26/Qg59lrdFU74Ek1K.jpg
      descr: This Standard defines the ECMAScript 2022 general-purpose programming language.
 

```

class_name和class_desc支持 html 格式，如不需要，也可以留空。

如果你想设置成该站友链页的效果：https://tzy1997.com/articles/hexo1604/，请参考教程：基于[Butterfly的外挂标签引入 ](https://tzy1997.com/articles/0xiipgum/#%E6%9B%B4%E6%96%B0%E8%AE%B0%E5%BD%95)、[Butterfly 安裝文檔(三) 主題配置-1 | Butterfly](https://butterfly.js.org/posts/4aa8abbe/#標籤外掛（Tag-Plugins）)。

#### 图库

图库页面只是普通的页面，你只需要`hexo new page xxxxx`创建你的页面就行。

然后使用标签外挂 `galleryGroup`，具体用法请查看对应的内容。

```yaml
<div class="gallery-group-main">
{% galleryGroup '壁纸' '收藏的一些壁纸' '/Gallery/wallpaper' https://bu.dusays.com/2021/03/06/38a2c5cd8b44e.jpg %}
{% galleryGroup '漫威' '关于漫威的图片' '/Gallery/marvel' https://i.loli.net/2019/12/25/8t97aVlp4hgyBGu.jpg %}
{% galleryGroup 'OH MY GIRL' '关于OH MY GIRL的图片' '/Gallery/ohmygirl' https://i.loli.net/2019/12/25/hOqbQ3BIwa6KWpo.jpg %}
</div>


```

#### 相册

[Butterfly 安裝文檔(三) 主題配置-1 | Butterfly](https://butterfly.js.org/posts/4aa8abbe/#Gallery相冊)

区别于旧版的Gallery相册,新的 Gallery 相册会自动根据图片长度进行排版，书写也更加方便，与 markdown 格式一样。可根据需要插入到相应的 md。

#### 子页面

子页面也是普通的页面，你只需要hexo new page xxxxx创建你的页面就行。

然后使用标签外挂 gallery，具体用法请查看对应的内容。

```
{% gallery %}
![](https://i.loli.net/2019/12/25/Fze9jchtnyJXMHN.jpg)
![](https://i.loli.net/2019/12/25/ryLVePaqkYm4TEK.jpg)
![](https://i.loli.net/2019/12/25/gEy5Zc1Ai6VuO4N.jpg)
![](https://i.loli.net/2019/12/25/d6QHbytlSYO4FBG.jpg)
![](https://i.loli.net/2019/12/25/6nepIJ1xTgufatZ.jpg)
![](https://i.loli.net/2019/12/25/E7Jvr4eIPwUNmzq.jpg)
![](https://i.loli.net/2019/12/25/mh19anwBSWIkGlH.jpg)
![](https://i.loli.net/2019/12/25/2tu9JC8ewpBFagv.jpg)
{% endgallery %}
```

如果你想要使用 /photo/ohmygirl 这样的链接显示你的图片内容

你可以把创建好的 ohmygirl整个文件夹移到 photo文件夹里去

#### 404页面

主題內置了一个简单的404页面，可在设置中开放。

```yaml
# A simple 404 page
error_404:
  enable: true
  subtitle: 'Page Not Found'
  background: https://i.loli.net/2020/05/19/aKOcLiyPl2JQdFD.png

```

#### 语言

https://tzy1997.com/articles/hexo1605/

修改站点配置文件_config.yml，默认语言是 en 。

主题支持三种语言：

```
default(en)
zh-CN (简体中文)
zh-TW (繁体中文)
```

#### 网站资料

修改网站各种资料，例如标题、副标题和邮箱等个人资料，请修改站点配置文件_config.yml。详细参数可参考官方的[配置描述](https://hexo.io/zh-cn/docs/configuration)。

#### 导航菜单

修改主题配置文件_config.butterfly.yml。

```yaml
menu:
  Home: / || fas fa-home
  Archives: /archives/ || fas fa-archive
  Tags: /tags/ || fas fa-tags
  Categories: /categories/ || fas fa-folder-open
  List||fas fa-list:
    Music: /music/ || fas fa-music
    Movie: /movies/ || fas fa-video
  Link: /link/ || fas fa-link
  About: /about/ || fas fa-heart

```

必须是 /xxx/，后面||分开，然后写图标名。

如果不希望显示图标，图标名可不写。

v3.7.1 版本中直接默认子目录是展开的，如果你想要隐藏，后续在魔改中会提到。
若主题版本大于 v4.0.0，可以直接在子目录里添加 hide 。

```yaml
menu:
  Home: / || fas fa-home
  Archives: /archives/ || fas fa-archive
  Tags: /tags/ || fas fa-tags
  Categories: /categories/ || fas fa-folder-open
  List||fas fa-list||hide:
    Music: /music/ || fas fa-music
    Movie: /movies/ || fas fa-video
  Link: /link/ || fas fa-link
  About: /about/ || fas fa-heart

```

> 注意： 导航的文字可自行更改

例如：

```yaml
menu:
  首页: / || fas fa-home
  时间轴: /archives/ || fas fa-archive
  标签: /tags/ || fas fa-tags
  分类: /categories/ || fas fa-folder-open
  清单||fa fa-heartbeat:
    音乐: /music/ || fas fa-music
    照片: /Gallery/ || fas fa-images
    电影: /movies/ || fas fa-video
  友链: /link/ || fas fa-link
  关于: /about/ || fas fa-heart
```

#### 代码

代码块中的所有功能只适用于 Hexo 自带的代码渲染。
如果使用第三方的渲染器，不一定会有效。

**代码高亮主题**

Butterfly支持 6 种代码高亮样式：

```
darker
pale night
light
ocean
mac
mac light
```

修改主题配置文件_config.butterfly.yml。中的highlight_theme属性。

**代码复制**

修改主题配置文件_config.butterfly.yml。中的highlight_copy属性。

```yaml
highlight_copy: true
```

**代码框展开/关闭**

```yaml
highlight_shrink: true #代码框不展开，需点击 '>' 打开
```

**代码换行**

在默认情况下，Hexo 在编译的时候不会实现代码自动换行。如果你不希望在代码块的区域里有横向滚动条的话，那么你可以考虑开启这个功能。

```yaml
code_word_wrap: true
```

**代码高度限制**

> v3.7.0 及以上支持。

可配置代码高度限制，超出的部分会隐藏，并显示展开按钮。

```yaml
highlight_height_limit: false # unit: px
```

- 单位是px，直接添加数字，如 200
- 实际限制高度为highlight_height_limit + 30 px ，多增加 30px 限制，目的是避免代码高度只超出highlight_height_limit 一点时，出现展开按钮，展开没内容。
- 不适用于隐藏后的代码块（ css 设置 display: none）。

#### 社交图标

Butterfly支持[font-awesome v6](https://fontawesome.com/icons)图标。

书写格式：图标名：url || 描述性文字。

```yaml
social:
  fab fa-github: https://github.com/xxxxx || Github
  fas fa-envelope: mailto:xxxxxx@gmail.com || Email

```

#### 顶部图

如果不要显示顶部图，可直接配置 disable_top_img: true。

```yaml
配置	解释
index_img	主页的 top_img
default_top_img	默认的 top_img，当页面的 top_img 没有配置时，会显示 default_top_img
archive_img	归档页面的 top_img
tag_img	tag子页面 的 默认 top_img
tag_per_img	tag子页面的 top_img，可配置每个 tag 的 top_img
category_img	category 子页面 的 默认 top_img
category_per_img	category 子页面的 top_img，可配置每个 category 的 top_img
```

主页图：

```yaml
index_img:

# If the banner of page not setting, it will show the top_img
# 它是先渲染的default_top_img，然后再渲染了index_img，只设置index_img，而不设置default_top_img时可以看出来
# 利用它的处理方式，只设置default_top_img，避免页面重复渲染
default_top_img: https://s2.loli.net/2022/07/02/LUfbSm2HQzOIVvM.jpg
```

其它页面 （tags/categories/自建页面）和文章页的top_img，请到对应的 md 页面设置front-matter中的top_img。

#### 文章置顶

【推荐】hexo-generator-index从 v2.0.0 开始，已经支持文章置顶功能。你可以直接在文章的front-matter区域里添加sticky: 1属性来把这篇文章置顶。数值越大，置顶的优先级越大。

#### 文章封面

文章的markdown文档上，在Front-matter添加cover，并填上要显示的图片地址。如果不配置cover，可以设置显示默认的cover。

如果不想在首页显示cover，可以设置为false。

修改主题配置文件_config.butterfly.yml。

```yaml
cover:
  # 是否显示文章封面
  index_enable: true
  aside_enable: true
  archives_enable: true
  # 封面显示的位置
  # 三个值可配置 left , right , both
  position: both
  # 当没有设置cover时，默认的封面显示
  default_cover: 
```

当配置多张图片时，会随机选择一张作为cover，此时写法应为：

```yaml
default_cover:
  - https://bu.dusays.com/2022/06/05/629c5257753d1.png
  - https://bu.dusays.com/2022/05/29/62939662553c9.png
  - https://bu.dusays.com/2022/05/26/628fa0426213d.png
```

#### 文章页相关配置

##### 文章meta显示

post_meta这个属性用于显示文章的相关信息的。

修改主题配置文件_config.butterfly.yml。

```yaml
post_meta:
  page:
    date_type: both # created or updated or both 主页文章日期是创建日或者更新日或都显示
    date_format: relative # date/relative 显示日期还是相对日期
    categories: true # true or false 主页是否显示分类
    tags: true # true or false 主页是否显示标签
    label: true # true or false 显示描述性文字
  post:
    date_type: both # created or updated or both 文章页日期是创建日或者更新日或都显示
    date_format: relative # date/relative 显示日期还是相对日期
    categories: true # true or false 文章页是否显示分类
    tags: true # true or false 文章页是否显示标签
    label: true # true or false 显示描述性文字

```

##### 文章版权和协议许可

修改主题配置文件_config.butterfly.yml。

```yaml
post_copyright:
  enable: true
  decode: false
  author_href:
  license: CC BY-NC-SA 4.0
  license_url: https://creativecommons.org/licenses/by-nc-sa/4.0/
```

由于Hexo 4.1开始，默认对网址进行解码，以至于如果是中文网址，会被解码，可设置decode: true来显示中文网址。

如果有文章（例如：转载文章）不需要显示版权，可以在文章页Front-matter中单独设置。

```yaml
copyright: false
```

##### 文章打赏

```yaml
reward:
  enable: true
  QR_code:
    - img: /img/wechat.jpg
      link:
      text: wechat
    - img: /img/alipay.jpg
      link:
      text: alipay
```

##### TOC

```yaml
toc:
  post: true
  page: false
  number: true
  expand: false
  style_simple: false # for post
  
  属性	解释
post	文章页是否显示 TOC
page	普通页面是否显示 TOC
number	是否显示章节数
expand	是否展开 TOC
style_simple	简洁模式（侧边栏只显示 TOC, 只对文章页有效 ）
```

##### 相关文章推荐

相关文章推荐的原理是根据文章tags的比重来推荐。

```yaml
related_post:
  enable: true
  limit: 6 # 显示推荐文章数目
  date_type: created # or created or updated 文章日期显示创建日或者更新日

```

##### 文章锚点

开启文章锚点后，当你在文章页进行滚动时，文章链接会根据标题ID进行替换。

注意: 每替换一次，会留下一个歷史记录。所以如果一篇文章有很多锚点的话，网页的歷史记录会很多。

```yaml
# anchor
# when you scroll in post , the url will update according to header id.
anchor: true

```

##### 文章过期提醒

可设置是否显示文章过期提醒，以更新时间为基准。

```yaml
# Displays outdated notice for a post (文章过期提醒)
noticeOutdate:
  enable: true
  style: flat # style: simple/flat
  limit_day: 365 # When will it be shown
  position: top # position: top/bottom
  message_prev: It has been
  message_next: days since the last update, the content of the article may be outdated.
```

```
limit_day： 距离更新时间多少天才显示文章过期提醒。
message_prev ： 天数之前的文字。
message_next：天数之后的文字。
```

##### 文章分页按钮

```yaml
# post_pagination (分页)
# value: 1 || 2 || false
# 1: The 'next post' will link to old post
# 2: The 'next post' will link to new post
# false: disable pagination
post_pagination: false

参数	解释
post_pagination: false	关闭分页按钮
post_pagination: 1	下一篇显示的是旧文章
post_pagination: 2	下一篇显示的是新文章
```

#### 头像

```yaml
avatar:
  img: https://bu.dusays.com/2022/05/02/626f92e193879.jpg
  effect: true # 头像会一直转圈
```

#### 图片描述

可开启图片Figcaption描述文字显示，优先显示图片的title属性，然后是alt属性。

修改主题配置文件_config.butterfly.yml。

```yaml
photofigcaption: false
```

#### 文章内容复制相关配置

```yaml
# copy settings
# copyright: Add the copyright information after copied content (复制的内容后面加上版权信息)
copy:
  enable: true
  copyright:
    enable: true
    limit_count: 50

```

```
配置	解释
enable	是否开启网站复制权限
copyright	复制的内容后面加上版权信息
enable	是否开启复制版权信息添加
limit_count	字数限制，当复制文字大于这个字数限制时，将在复制的内容后面加上版权信息
```

#### Footer 设置

##### 博客年份

```yaml
footer:
  owner:
    enable: true
    since: 2018   # 站点起始时间
```

##### 页脚自定义文本

custom_text是一个给你用来在页脚自定义文本的选项。通常你可以在这里写声明文本等。支持 HTML。

修改主题配置文件_config.butterfly.yml。

本人的页脚如下，若你在配置时没有出现github徽章，请参考教程添加[Github徽标](https://tzy1997.com/articles/kfwr2gpa/)。

```yaml
custom_text: I wish you to become your own sun, no need to rely on who's light.<p><a target="_blank" href="https://hexo.io/"><img src="https://img.shields.io/badge/Frame-Hexo-blue?style=flat&logo=hexo" title="博客框架为Hexo"></a>&nbsp;<a target="_blank" href="https://butterfly.js.org/"><img src="https://img.shields.io/badge/Theme-Butterfly-6513df?style=flat&logo=bitdefender" title="主题采用butterfly"></a>&nbsp;<a target="_blank" href="https://www.jsdelivr.com/"><img src="https://img.shields.io/badge/CDN-jsDelivr-orange?style=flat&logo=jsDelivr" title="本站使用JsDelivr为静态资源提供CDN加速"></a> &nbsp;<a target="_blank" href="https://vercel.com/ "><img src="https://img.shields.io/badge/Hosted-Vervel-brightgreen?style=flat&logo=Vercel" title="本站采用双线部署，默认线路托管于Vercel"></a>&nbsp;<a target="_blank" href="https://vercel.com/ "><img src="https://img.shields.io/badge/Hosted-Coding-0cedbe?style=flat&logo=Codio" title="本站采用双线部署，联通线路托管于Coding"></a>&nbsp;<a target="_blank" href="https://github.com/"><img src="https://img.shields.io/badge/Source-Github-d021d6?style=flat&logo=GitHub" title="本站项目由Gtihub托管"></a>&nbsp;<a target="_blank" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img src="https://img.shields.io/badge/Copyright-BY--NC--SA%204.0-d42328?style=flat&logo=Claris" title="本站采用知识共享署名-非商业性使用-相同方式共享4.0国际许可协议进行许可"></a></p>
```

对于部分人需要写 ICP 的，也可以写在custom_text里。

```yaml
custom_text: <a href="icp链接"><img class="icp-icon" src="icp图片"><span>备案号：xxxxxx</span></a>

```

#### 右下角按钮

##### 简繁转换

```yaml
translate:
  enable: false
  # 默认按钮显示文字(网站是简体，应设置为'default: 繁')
  default: 繁
  # the language of website (1 - Traditional Chinese/ 2 - Simplified Chinese）
  # 网站默认语言，1: 繁体中文, 2: 简体中文
  defaultEncoding: 2
  # Time delay 延迟时间,若不在前, 要设定延迟翻译时间, 如100表示100ms,默认为0
  translateDelay: 0
  # 当文字是简体时，按钮显示的文字
  msgToTraditionalChinese: '繁'
  # 当文字是繁体时，按钮显示的文字
  msgToSimplifiedChinese: '簡'

```

##### 夜间模式

```yaml
# dark mode
darkmode:
  enable: false
  # dark 和 light 两种模式切换按钮
  button: true
  # Switch dark/light mode automatically (自動切換 dark mode和 light mode)
  # autoChangeMode: 1  Following System Settings, if the system doesn't support dark mode, it will switch dark mode between 6 pm to 6 am
  # autoChangeMode: 2  Switch dark mode between 6 pm to 6 am
  # autoChangeMode: false
  autoChangeMode: false

```

##### 阅读模式

阅读模式下会去掉除文章外的内容，避免干扰阅读。只会出现在文章页面，右下角会有阅读模式按钮。

```yaml
readmode: true
```

#### 侧边栏设置

##### 侧边排版

可自行决定哪个项目需要显示，可决定位置，也可以设置不显示侧边栏。

```yaml
aside:
  enable: true
  hide: false
  button: true
  mobile: true # 手机页面（ 显示宽度 < 768px ）是否显示aside内容
  position: right # left or right 
  card_author: # 关于博主的一些信息
    enable: true
    description:
    button:
      enable: true
      icon: fab fa-github
      text: Follow Me
      link: https://github.com/xxxxxx
  card_announcement:  # 公告信息
    enable: true
    content: This is my Blog
  card_recent_post: # 最新文章
    enable: true
    limit: 5 # if set 0 will show all
    sort: date # date or updated
    sort_order: # Don't modify the setting unless you know how it works
  card_categories: # 文章分类
    enable: true
    limit: 8 # if set 0 will show all
    expand: none # none/true/false
    sort_order: # Don't modify the setting unless you know how it works
  card_tags: # 文章标签
    enable: true
    limit: 40 # if set 0 will show all
    color: false
    sort_order: # Don't modify the setting unless you know how it works
  card_archives: # 文章归档
    enable: true
    type: monthly # yearly or monthly
    format: MMMM YYYY # eg: YYYY年MM月
    order: -1 # Sort of order. 1, asc for ascending; -1, desc for descending
    limit: 8 # if set 0 will show all
    sort_order: # Don't modify the setting unless you know how it works
  card_webinfo:  # 网站信息
    enable: true
    post_count: true
    last_push_date: true
    sort_order: # Don't modify the setting unless you know how it works

```

##### 访问人数(UV 和 PV)

详细信息请查看[busuanzi官方网站](http://busuanzi.ibruce.info/)

```yaml
busuanzi:
  site_uv: true  # 本站总访客数
  site_pv: true  # 本站总访问量 
  page_pv: true  # 本文总阅读量
```

##### 运行时间

```yaml
runtimeshow:
  enable: true
  publish_date: 6/7/2018 00:00:00  
  ##网页开通时间
  #格式: 月/日/年 时间
  #也可以写成 年/月/日 时间
```

##### 最新评论

> v3.1.0 以上支持。如果未配置任何评论，前先不要开启该功能。
> 最新评论只会在刷新时才会去读取，并不会实时变化。
> 由于 API 有 访问次数限制，为了避免调用太多，主题默认存取期限为 10 分鐘。也就是説，调用后资料会存在 localStorage 里，10分鐘内刷新网站只会去 localStorage 读取资料。 10 分鐘期限一过，刷新页面时才会去调取 API 读取新的数据。（ 3.6.0 新增了 storage 配置，可自行配置缓存时间）。

```yaml
# Aside widget - Newest Comments
newest_comments:
  enable: true
  sort_order: # Don't modify the setting unless you know how it works
  limit: 6  # 显示的数量
  storage: 10 # 设置缓存时间，单位 分钟 
  avatar: true # 是否显示头像

```

#### 网站背景

```yaml
# 图片格式 url(http://xxxxxx.com/xxx.jpg)
# 颜色（HEX值/RGB值/颜色单词/渐变色)
# 留空 不显示背景
background:
```

> 如果你的网站根目录不是’/‘，使用本地图片时，需加上你的根目录。
> 例如：网站是 https://yoursite.com/blog，引用一张img/xx.png图片，则设置background为 `url(/blog/img/xx.png)`

#### 打字效果

传送门：[activate-power-mode](https://github.com/disjukr/activate-power-mode)。

```yaml
# Typewriter Effect (打字效果)
# https://github.com/disjukr/activate-power-mode
activate_power_mode:
  enable: false
  colorful: true # open particle animation (冒光特效)
  shake: true #  open shake (抖動特效)
  mobile: false
```

#### footer 背景

```yaml
# footer是否显示图片背景(与top_img一致)
footer_bg: true
```

```
配置的值	效果
留空/false	显示默认的颜色
img链接	图片的链接，显示所配置的图片
颜色：
HEX值 - #0000FF
RGB值 - rgb(0,0,255)
颜色单词 - orange
渐变色 - linear-gradient( 135deg, #E2B0FF 10%, #9F44D3 100%)	对应的颜色
true	显示跟 top_img 一样
```

#### 背景特效

可设置每次刷新更换彩带，或者每次点击更换彩带。详细配置可查看[canvas_ribbon](https://github.com/hustcc/ribbon.js)。

静止彩带

```yaml
canvas_ribbon:
  enable: false
  size: 150
  alpha: 0.6
  zIndex: -1
  click_to_change: false  #設置是否每次點擊都更換彩带
  mobile: false # false 手機端不顯示 true 手機端顯示
```

动态彩带

```yaml
canvas_fluttering_ribbon:
  enable: true
  mobile: true # false 手机端不显示 true 手机端显示
```

`canvas_nest`

```yaml
canvas_nest:
  enable: true
  color: '0,0,255' #color of lines, default: '0,0,0'; RGB values: (R,G,B).(note: use ',' to separate.)
  opacity: 0.7 # the opacity of line (0~1), default: 0.5.
  zIndex: -1 # z-index property of the background, default: -1.
  count: 99 # the number of lines, default: 99.
  mobile: false # false 手機端不顯示 true 手機端顯示
```

#### 鼠标点击效果

烟花

```yaml
fireworks:
  enable: true
  zIndex: 9999 # -1 or 9999
  mobile: false
```

zIndex建议只在-1和9999上选。
-1 代表烟火效果在底部。
9999 代表烟火效果在前面。

爱心：

```yaml
# 点击出現爱心
click_heart:
  enable: true
  mobile: false
```

文字：

```yaml
# 点击出现文字，文字可自行修改
ClickShowText:
  enable: false
  text:
    - I
    - LOVE
    - YOU
  fontSize: 15px
  random: false # 文字随机显示
  mobile: false

```

#### 自定义字体和字体大小

##### 全局字体

```yaml
# Global font settings
# Don't modify the following settings unless you know how they work (非必要不要修改)
font:
  global-font-size:
  code-font-size:
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Lato, Roboto, "PingFang SC", "Microsoft JhengHei", "Microsoft YaHei", sans-serif
  code-font-family: consolas, Menlo, "PingFang SC", "Microsoft JhengHei", "Microsoft YaHei", sans-serif

```

##### Blog 标题字体

```yaml
# Font settings for the site title and site subtitle
# 左上角网站名字 主页居中网站名字
blog_title_font:
  font_link: https://fonts.googleapis.com/css?family=Titillium+Web&display=swap
  font-family: Titillium Web, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft JhengHei', 'Microsoft YaHei', sans-serif


```

#### 网站副标题

可设置主页中显示的网站副标题或者喜欢的座右铭。

```yaml
# Site
subtitle:
  enable: false
  # Typewriter Effect (打字效果)
  effect: true
  # loop (循環打字)
  loop: true
  # source調用第三方服務
  # source: false 關閉調用
  # source: 1  調用搏天api的隨機語錄（簡體）
  # source: 2  調用一言網的一句話（簡體）
  # source: 3  調用一句網（簡體）
  # source: 4  調用今日詩詞（簡體）
  # subtitle 會先顯示 source , 再顯示 sub 的內容
  source: false
  # 如果有英文逗號' , ',請使用轉義字元 &#44;
  # 如果有英文雙引號' " ',請使用轉義字元 &quot;
  # 開頭不允許轉義字元，如需要，請把整個句子用雙引號包住
  # 如果關閉打字效果，subtitle只會顯示sub的第一行文字
  sub:
    - 窗外有月色和雨&#44;而我在想你。
    - There is moonlight and rain outside the window, and I miss you.

```

#### 页面加载动画preloader

> 主题版本 < 5.0

当进入网页时，因为加载速度的问题，可能会导致top_img图片出现断层显示，或者网页加载不全而出现等待时间，开启preloader后，会显示加载动画，等页面加载完，加载动画会消失。

```yaml
# 加载动画 Loading Animation
preloader: true
```

> 主题版本 >= 5.0

preloader 设置更改，增加 [pace.js](https://codebyzach.github.io/pace/) 加载动画条，[pace.js原理简介](https://www.shuzhiduo.com/A/RnJW08VY5q/)

```yaml
# 加载动画 Loading Animation
preloader:
  enable: false
  # source
  # 1. fullpage-loading
  # 2. pace (progress bar)
  source: 1
  # pace theme (see https://codebyzach.github.io/pace/)
  pace_css_url:

```

#### 字数统计

安装插件：在你的博客根目录，打开cmd命令窗口执行npm install hexo-wordcount --save。
开启配置：修改主题配置文件_config.butterfly.yml中的wordcount。

```yaml
wordcount:
  enable: true
  post_wordcount: true
  min2read: true
  total_wordcount: true

```

#### 图片大图查看模式

> 只能开启一个。
> 如果你并不想为某张图片添加大图查看模式，你可以使用 html 格式引用图片，并为图片添加 no-lightbox class 名，例如：`<img src="xxxx.jpg" class="no-lightbox">`。

fancybox(推荐)

```yaml
# fancybox http://fancyapps.com/fancybox/3/
fancybox: true

```

或者是

```yaml
medium_zoom: true
```

#### Pjax

当用户点击链接，通过 ajax 更新页面需要变化的部分，然后使用 HTML5 的 pushState 修改浏览器的 URL 地址。

这样可以不用重复加载相同的资源（css/js）， 从而提升网页的加载速度。

```yaml
# Pjax [Beta]
# It may contain bugs and unstable, give feedback when you find the bugs.
# https://github.com/MoOx/pjax
pjax: 
  enable: true
  # 对于一些第三方插件，有些并不支持 pjax 。
  # 你可以把网页加入到 exclude 里，这个网页会被 pjax 排除在外。
  # 点击该网页会重新加载网站。
  exclude: 
    - /music/
    - /no-pjax/

```

> 使用 pjax 后，一些自己DIY的js可能会无效，跳转页面时需要重新调用，请参考[Pjax文档](https://github.com/MoOx/pjax)。
>
> [Hexo 集成 Pjax 实现网站无刷新加载](https://zsyyblog.com/ff9e3a96.html)

#### Inject

> v2.3.0以上支持

如想添加额外的 js/css/meta 等等东西，可以在`Inject` 里添加，head(`</body>`标签之前)， bottom(`</html>`标签之前)。

```yaml
# Inject
# Insert the code to head (before '</head>' tag) and the bottom (before '</body>' tag)
# 插入代码到头部 </head> 之前 和 底部 </body> 之前
inject:
  head:
  - <link rel="stylesheet" href="/css/custom/custom.css">
  - <link rel="stylesheet" href="/css/custom/plane_v2.css">
  bottom:
  # - <script src="xxxx"></script>

```

读取的是在`node_modules`里的

#### CDN

> 建议先ping一下cdn.jsdelivr.net，如果能ping通，可忽略此步。
> 自从jsd官方的ICP被吊销以后，很多资源都无法访问，请自行配置CDN，配置后请确认链接是否能访问。
> 为了博客能正常访问，本文列出几种解决方法（防止cdn.jsdelivr.net再次出现幺蛾子）。

**手动替换CDN**

> 注意：如果下面三种 CDN 也存在问题，可以找一找国内的一些 CDN ，如知乎、字节、饿了么等。

[常用CDN网站汇总](https://blog.csdn.net/VariatioZbw/article/details/107822562)

[Butterfly CDN链接更改指南，替换jsdelivr提升访问速度](https://blog.zhheo.com/p/790087d9.html)

[目前可用cdn整理 ](https://anzhiy.cn/posts/fe76.html)

将主题配置文件_config.butterfly.yml中的https://cdn.jsdelivr.net替换成下面任意一种CDN即可。

https://fastly.jsdelivr.net
https://testingcf.jsdelivr.net
https://gcore.jsdelivr.net

![image-20230203100446898](image-20230203100446898.png)

另外将上图中所出现的https://cdn.jsdelivr.net文件换成可用的CDN。

Valine评论相关（如果用的不是Valine，可跳过此步）：

```
node_modules\hexo-theme-butterfly\layout\includes\third-party\newest-comments\valine.pug
node_modules\hexo-theme-butterfly\layout\includes\third-party\newest-comments\leancloud.pug
```

电子时钟相关（如果未引用电子时钟，可跳过此步）：

```
node_modules\hexo-butterfly-clock\index.js
node_modules\hexo-butterfly-clock\lib\clock.css
```

其他文件也按照同样的方法修改即可。

**gulp-replace全局替换**

前往博客根目录，打开cmd命令窗口执行如下命令安装 gulp 及 gulp-replace。

```bash
npm install gulp-cli -g
npm install gulp -D
npm install --save-dev gulp-replace
```

前往博客根目录，创建文件gulpfile.js，填写以下代码。

```yaml
const gulp = require('gulp');  //如果之前有gulp相关插件，请删除此行代码
const replace = require('gulp-replace');
gulp.task('templates', async() => {
  gulp.src('public/**/*.*')
    .pipe(replace('这里填写jsd官方域名', '目标cdn地址'))
    .pipe(gulp.dest('public/')),  { overwrite: true };
});
gulp.task("default", gulp.parallel('templates'));

```

前往博客根目录，打开cmd命令窗口执行gulp。

```bash
gulp
```

#### 搜索

https://tzy1997.com/articles/hexo1607/

##### local search

```bash
npm install hexo-generator-search --save
```

修改站点配置文件`_config.yml`，添加如下代码

```yml
search:
  path: search.xml
  field: post
  content: true

```

主题中开启搜索。
在主题配置文件`_config.butterfly.yml`中修改以下内容：

```diff
local_search:
-  enable: false
+  enable: true
```

重新编译运行，即可看到效果。
前往博客根目录，打开cmd命令窗口依次执行如下命令：

```bash
hexo cl && hexo generate
hexo s -p 8000
```

实际部署时注意`CNAME`文件

经测试，现在这个插件直接就可以支持搜索文章内容了

![image-20220811195825913](image-20220811195825913.png)

第一次搜索会加载数据库，花费较长时间

##### Algolia（推荐）

> 关于 Algolia 搜索功能，这里有两种插件，一个是 hexo-algolia ，一个是 hexo-algoliasearch。第一种亲测只能对匹配文章title，不能匹配文章内容查询到结果，所以推荐第二种。下面分别对这两种插件做不同的说明

https://tzy1997.com/articles/hexo1607/

获取 `Algolia` 账号

注册 `Algolia`。https://www.algolia.com/
进入官网地址 注册，也可以直接用Github授权登录。

新建 Index。https://www.algolia.com/apps/61301LMFP2/indices

![image-20220811194142680](image-20220811194142680.png)

创建拥有一定权限的api key（如果选择第二种插件，可忽略这一步）。
进入【Settings > API Keys】。

![image-20220811194210278](image-20220811194210278.png)



![image-20220811194246448](image-20220811194246448.png)

点击【Create】，这样就得到了一个 api key。注意一下，这个key将会在下面的步骤中用到。

![image-20220811194312469](image-20220811194312469.png)

**安装依赖 && 写入配置**

方式一：`hexo-algoliasearch`（推荐）

安装 Algolia 依赖。
前往博客根目录，打开cmd命令窗口执行npm install hexo-algoliasearch --save。

```bash
npm install hexo-algoliasearch --save
```

修改站点配置文件`_config.yml`，添加如下代码：

```yaml
algolia:
  appId: "your applicationID"
  apiKey: "your Search-Only API Key"
  adminApiKey: "your Admin API Key"
  chunkSize: 50000 # 如果文章很长，可以设置大一点，不然只会搜索文章的前半部分
  indexName: "your indexName"
  fields:
    - content:strip:truncate,0,500
    - excerpt:strip
    - gallery
    - permalink
    - photos
    - slug
    - tags
    - title
```

![image-20220811194420778](image-20220811194420778.png)

【applicationID】填入图中位置的 Applicaiton ID，【apiKey】填入图中位置的 Search-Only API Key，【Admin API Key】填入图中位置的 Admin API Key，【indexName】填入前面创建的索引名称。

执行hexo algolia。（每次生成文章后都要执行一次，可以配在npm命令里，加载hexo generate后面）

前往博客根目录，打开cmd命令窗口执行hexo algolia。

```bash
hexo algolia
```

成功界面

![image-20230203103517195](image-20230203103517195.png)

可能的错误：

hexo server的时候，可能会创建db.json失败，导致上面命令提示db.json不存在，重新hexo server一下，停止、然后hexo algolia即可

![image-20230203103643231](image-20230203103643231.png)

主题中写入 Alogolia 配置项。
在主题配置文件_config.butterfly.yml中修改以下内容（靠近local_search，记得关掉local_search）：

```yaml
algolia_search:
  enable: true
  hits:
    per_page: 10
  labels:
    input_placeholder: Search for Posts
    hits_empty: "我们没有找到任何搜索结果: ${query}"
    hits_stats: "找到${hits}条结果（用时${time} ms）"

```

重新编译运行，即可看到效果。
前往博客根目录，打开cmd命令窗口依次执行如下命令：

```bash
hexo cl && hexo generate
hexo s -p 8000
```

**注意：**

此时_config.yml不能直接提交到github上了，因为有秘钥

可以抽离出`_config.custom.yml`并添加到`.gitignore`中

[配置 | Hexo](https://hexo.io/zh-cn/docs/configuration#使用代替配置文件)

可以在 hexo-cli 中使用 `--config` 参数来指定自定义配置文件的路径。

```bash
# 用 'custom.yml' 代替 '_config.yml'
$ hexo server --config custom.yml

# 使用 'custom.yml' 和 'custom2.json'，优先使用 'custom3.yml'，然后是 'custom2.json'
$ hexo generate --config custom.yml,custom2.json,custom3.yml
```

当你指定了多个配置文件以后，Hexo 会按顺序将这部分配置文件合并成一个 `_multiconfig.yml`。如果遇到重复的配置，排在后面的文件的配置会覆盖排在前面的文件的配置。这个原则适用于任意数量、任意深度的 YAML 和 JSON 文件。

同时每次启动会提交，都要同步下

但现在有个问题，每次执行`hexo algolia`都默认去`_config.yml`中找配置，也要指定配置文件

最终的`package.json`

```json
  "scripts": {
    "build": "hexo generate --config _config.yml,_config.butterfly.yml,_config.custom.yml",
    "clean": "hexo clean",
    "deploy": "hexo deploy",
    "algolia": "hexo algolia --config _config.custom.yml",
    "server": "hexo server -p 8081 --config _config.yml,_config.butterfly.yml,_config.custom.yml",
    "copy": "copy D:\\workspace\\github\\code\\saiable.github.io\\hexo-blog\\CNAME D:\\workspace\\github\\code\\saiable.github.io\\hexo-blog\\public",
    "auto": "hexo clean & npm run build & npm run algolia & npm run copy & npm run deploy"
  },
```

备注：最右边的优先级最高



开发的时候，先起一下服务，然后在另外一个窗口运行`npm run algolia`即可

添加新文章部署的时候，运行`npm run auto`即可（run algolia在generate之后）

最后把合并生成的`_multiconfig.yml`和`_config.custom.yml`添加到`.gitignore`中

```
.DS_Store
Thumbs.db
db.json
*.log
node_modules/
public/
.deploy*/
_multiconfig.yml
_config.custom.yml
```

开发的时候，搜索到结果后，点击跳转的域名不对，需要在自定义配置文件中加上url，指定你的域名

```yaml
url: https://mindcons.cn
algolia:
	...
```

虽然重复字段了，但是会被合并



另一种方式：`hexo-algolia`只支持标题，不支持内容，就不赘述了，详见https://tzy1997.com/articles/hexo1607/

#### 分享

https://tzy1997.com/articles/hexo1609/

> 注意：主题集成了三种分享功能，分别是AddThis、Sharejs、Addtoany，只能从其中选择一个分享服务商

##### AddThis

前往[AddThis 官网](https://www.addthis.com/register?next=/dashboard#tool-config)注册账号，输入下图中信息即可。

（注册不了，先跳过）



#### 在线聊天

https://tzy1997.com/articles/hexo1610/

从3.0开始，Butterfly主题内置了多种在线聊天工具。你可以选择开启一种，方便你与访客的交流。

##### 通用设置

关于这些在线聊天的工具，主题提供了一个按钮可以打开/关闭聊天窗口，这个聊天按钮将会出现在右下角里。你只需要把chat_btn打开就行。

```yaml
# Chat Button [recommend]
# It will create a button in the bottom right corner of website, and hide the origin button
chat_btn: true

```

为了不影响访客的体验，主题提供一个chat_hide_show配置，设为true后，使用工具提供的按钮时，只有向上滚动才会显示聊天按钮，向下滚动时会隐藏按钮。

修改主题配置文件_config.butterfly.yml，将chat_hide_show设置成true。

```yaml
# The origin chat button is displayed when scrolling up, and the button is hidden when scrolling down
chat_hide_show: true

```

如果使用工具自带的聊天按钮，按钮位置可能会遮挡右下角图标，请配置rightside-bottom调正右下角图标位置。

##### crisp

打开[crisp官网](https://crisp.chat/zh/)并注册账号。找到 【设置】->【网站设置】->【设置说明】，找到你的网站ID。

![image-20230203165551136](image-20230203165551136.png)

修改主题配置文件_config.butterfly.yml，将crisp设置成true。并将你的网站ID填入website_id。

```yaml
# crisp
# https://crisp.chat/en/
crisp:
  enable: true
  website_id: xxxxxxxx


```

有秘钥的都复制到自定义配置中



后面发现这样子build时会有问题，还是改回来把

```json
  "scripts": {
    "build": "hexo generate",
    "clean": "hexo clean",
    "deploy": "hexo deploy",
    "algolia": "hexo algolia",
    "server": "hexo server -p 8081",
    "copy": "copy D:\\workspace\\github\\code\\saiable.github.io\\hexo-blog\\CNAME D:\\workspace\\github\\code\\saiable.github.io\\hexo-blog\\public",
    "auto": "hexo clean & npm run build & npm run algolia & npm run copy & npm run deploy"
  },
```



##### 其他





























#### 标签语法

[Hexo+Butterfly 使用 Tab 分栏说明 | 竹山一叶 (zsyyblog.com)](https://zsyyblog.com/1f4771ba.html)

```markdown
{% tabs Unique name, [index] %}
<!-- tab [Tab caption] [@icon] -->
Any content (support inline tags too).
<!-- endtab -->
{% endtabs %}
```

# `Butterfly`主题美化





## 生成文章唯一链接（未生效）

`Hexo`的默认文章链接格式是年，月，日，标题这种格式来生成的。如果你的标题是中文的话，那你的URL链接就会包含中文。

```yml
permalink: :year/:month/:day/:title
```

前往你的`Hexo`博客根目录，打开cmd命令窗口执行`npm install hexo-abbrlink --save`。

修改站点配置文件`_config.yml`中`permalink`属性。

```diff
- permalink: :year/:month/:day/:title/
#修改为
+ permalink: post/:abbrlink.html # post为自定义前缀
+ abbrlink:
+   alg: crc32   #算法： crc16(default) and crc32
+   rep: hex     #进制： dec(default) and hex

```

如果使用的话，图片的路径就不对了

## 页面底部 footer 跳动的心

**添加图标**

编辑`BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/footer.pug`文件

将以下内容

```pug
&copy;${theme.footer.owner.since} - ${nowYear} By ${config.author}
```

改为

```pug
&copy;${theme.footer.owner.since} - ${nowYear + ' '} <i id="heartbeat" class="fa fas fa-heartbeat"></i> ${config.author}
```

将以下内容

```pug
&copy;${nowYear} By ${config.author} 
```

改为

```pug
&copy;${nowYear + ' '} <i id="heartbeat" class="fa fas fa-heartbeat"></i> ${config.author}
```

注意：上述两个地方的修改，要结合自己的实际文件，不要直接复制

**引入样式**

将以下内容添加到` <head></head>`标签内：

```yml
<link rel="stylesheet" href="https://fastly.jsdelivr.net/gh/HCLonely/images@master/others/heartbeat.min.css">

```

未防止资源失效，内容如下：

```css
/**
 * Minified by jsDelivr using clean-css v5.3.0.
 * Original file: /gh/HCLonely/images@master/others/heartbeat.css
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
#heartbeat{color:red;animation:iconAnimate 1.33s ease-in-out infinite}@-moz-keyframes iconAnimate{0%,100%{transform:scale(1)}10%,30%{transform:scale(.9)}20%,40%,60%,80%{transform:scale(1.1)}50%,70%{transform:scale(1.1)}}@-webkit-keyframes iconAnimate{0%,100%{transform:scale(1)}10%,30%{transform:scale(.9)}20%,40%,60%,80%{transform:scale(1.1)}50%,70%{transform:scale(1.1)}}@-o-keyframes iconAnimate{0%,100%{transform:scale(1)}10%,30%{transform:scale(.9)}20%,40%,60%,80%{transform:scale(1.1)}50%,70%{transform:scale(1.1)}}@keyframes iconAnimate{0%,100%{transform:scale(1)}10%,30%{transform:scale(.9)}20%,40%,60%,80%{transform:scale(1.1)}50%,70%{transform:scale(1.1)}}
/*# sourceMappingURL=/sm/7c97f3456d34ee6c17ca4a9141bef0f29c52d1ce9d85298b17f398a0de252965.map */
```

具体位置如下：

![image-20220810224105821](image-20220810224105821.png)



我们在source文件夹下新建custom文件夹，放自定义资源

![image-20230204111548743](image-20230204111548743.png)

`footer.pug`

```html
#footer-wrap
  if theme.footer.owner.enable
    - var now = new Date()
    - var nowYear = now.getFullYear()
    if theme.footer.owner.since && theme.footer.owner.since != nowYear
      //- .copyright!= `&copy;${theme.footer.owner.since} - ${nowYear} By ${config.author}`
      .copyright!= `&copy;${theme.footer.owner.since} - ${nowYear} <i id="heartbeat" class="fa fas fa-heartbeat"></i> ${config.author}`
    else
      //- .copyright!= `&copy;${nowYear} By ${config.author}`
      .copyright!= `&copy;${nowYear} <i id="heartbeat" class="fa fas fa-heartbeat"></i> ${config.author}`

  if theme.footer.copyright
    <a href="https://icp.gov.moe/?keyword=20230203" target="_blank">萌ICP备20230203号</a>
    //- .framework-info
      //- span= _p('footer.framework') + ' '
      //- a(href='https://hexo.io')= 'Hexo'
      //- span.footer-separator |
      //- span= _p('footer.theme') + ' '
      //- a(href='https://github.com/jerryc127/hexo-theme-butterfly')= 'Butterfly'

  if theme.footer.custom_text
    .footer_custom_text!=`${theme.footer.custom_text}`

<link rel="stylesheet" href="/custom/css/heartbeat.min.css" >
```



## 修改标题样式

在`BlogRoot/node_modules/hexo-theme-butterfly/source/css`文件下新建 `css` 文件，并命名为 `custom.css`( 命名按照自己喜好去命名，只需在主题配置文件`_config.butterfly.yml`中引入对应的`css`文件即可)，将以下代码复制到新建的`custom.css`中。

如果想自行修改标题样式的话，将`content: '\f0c1';`中的内容换成自己想要的即可，如要添加动画，参考`animation: avatar_turn_around 1s linear infinite;`。

```css
/* 标题样式开始 */
#article-container h1:before,
#article-container h2:before,
#article-container h3:before,
#article-container h4:before,
#article-container h5:before,
#article-container h6:before,
#post .post-outdate-notice:before,
.fontawesomeIcon,
.note:not(.no-icon)::before,
hr:before {
    display: inline-block;
    font-weight: 600;
    font-style: normal;
    font-variant: normal;
    font-family: 'Font Awesome 5 Free';
    text-rendering: auto;
    -webkit-font-smoothing: antialiased
}
#article-container h1:before,
#article-container h2:before,
#article-container h3:before,
#article-container h4:before,
#article-container h5:before,
#article-container h6:before {
    position: absolute;
    color: #f47466;
    /* 回形针 */
    content: '\f0c1';  
    line-height: 1;
    -webkit-transition: all .2s ease-out;
    -moz-transition: all .2s ease-out;
    -o-transition: all .2s ease-out;
    -ms-transition: all .2s ease-out;
    transition: all .2s ease-out;
    /* 若要使用风车效果，请去掉下面的注释 */
    /* content: '\f863'; 
    animation: avatar_turn_around 1s linear infinite; */
}
#article-container h1 {
    padding-left: 1.4rem
}

#article-container h1 code {
    font-size: 1rem
}

#article-container h1:before {
    margin-left: -1.3rem;
    top: calc(50% - .5rem);
    font-size: 1rem
}

#article-container h1:hover {
    padding-left: 1.6rem
}

#article-container h2 {
    padding-left: 1.3rem
}

#article-container h2 code {
    font-size: .9rem
}

#article-container h2:before {
    margin-left: -1.4rem;
    top: calc(50% - .45rem);
    font-size: .9rem
}

#article-container h2:hover {
    padding-left: 1.5rem
}

#article-container h3 {
    padding-left: 1.2rem
}

#article-container h3 code {
    font-size: .8rem;
    top: calc(50% - .4rem);

}

#article-container h3:before {
    margin-left: -1.2rem;
    top: calc(50% - .4rem);
    font-size: .8rem
}

#article-container h3:hover {
    padding-left: 1.4rem
}

#article-container h4 {
    padding-left: 1.1rem
}

#article-container h4 code {
    font-size: .7rem
}

#article-container h4:before {
    margin-left: -1rem;
    top: calc(50% - .35rem);
    font-size: .7rem
}

#article-container h4:hover {
    padding-left: 1.3rem
}

#article-container h5 {
    padding-left: 1rem
}

#article-container h5 code {
    font-size: .6rem
}

#article-container h5:before {
    margin-left: -.8rem;
    top: calc(50% - .3rem);
    font-size: .6rem
}

#article-container h5:hover {
    padding-left: 1.2rem
}

#article-container h6 {
    padding-left: 1rem
}

#article-container h6 code {
    font-size: .6rem
}

#article-container h6:before {
    margin-left: -.8rem;
    top: calc(50% - .3rem);
    font-size: .6rem
}

#article-container h6:hover {
    padding-left: 1.2rem
}

/* 标题样式结束 */
```

`_config.butterfly.yml`中引入

在 博客根目录的主题配置文件 `_config.butterfly.yml` 中找到` inject` 并修改，引入 css 文件即可

```yml
inject:
  head:
  - <link rel="stylesheet" href="/css/custom.css">
  bottom:
  # - <script src="xxxx"></script>

```

## 添加豆瓣插件

> 如果出现问题，请关注[hexo-douban - npm (npmjs.com)](https://www.npmjs.com/package/hexo-douban)

```
npm install hexo-douban --save
```

修改站点配置文件_config.yml，添加如下代码：

```yaml
douban:
  user: ethan_tzy
  builtin: false
  book:
    title: '腹有诗书气自华'
    quote: 'One who is filled with knowledge always behaves with elegance.'
  movie:
    title: '梦想与现实的碰撞'
    quote: 'The collision between dream and reality.'
  game:
    title: '诅咒中闪烁泪光，倾诉霜之哀伤。'
    quote: 'Tears flicker in the curse and pour out the sorrow of frost.'
  timeout: 10000
  
  douban:
  id: 267546144
  builtin: false
  item_per_page: 10
  book:
    path: booklist/index.html
    title: 'This is my book title'
    quote: 'This is my book quote'
    option:
  # movie:
  #   path: movies/index.html
  #   title: 'This is my movie title'
  #   quote: 'This is my movie quote'
  #   option:
  # game:
  #   path: games/index.html
  #   title: 'This is my game title'
  #   quote: 'This is my game quote'
  #   option:
  # song:
  #   path: songs/index.html
  #   title: 'This is my song title'
  #   quote: 'This is my song quote'
  #   option:
  timeout: 10000 
```



```
user: 你的豆瓣ID。打开豆瓣，登入账户，然后在右上角点击 ”个人主页“，这时候地址栏的URL大概是这样：https://www.douban.com/people/xxxxxx/ ，其中的”xxxxxx”就是你的个人ID了。
builtin: 是否将生成页面的功能嵌入 hexo s 和 hexo g 中，默认是 false ，另一可选项为 true 。
title: 该页面的标题。
quote: 写在页面开头的一段话,支持html语法。
timeout: 爬取数据的超时时间，默认是 10000ms，如果在使用时发现报了超时的错(ETIMEOUT)可以把这个数据设置的大一点。
如果只想显示某一个页面(比如movie)，那就把其他的配置项注释掉即可。
```





在主题配置文件_config.butterfly.yml中配置以下内容：

```yaml
# 如果你有使用hexo-douban，可配置這個
douban:
   meta: true
   movies_img: https://fastly.jsdelivr.net/gh/jerryc127/butterfly_cdn@2.1.0/top_img/movie.jpg
   books_img: https://fastly.jsdelivr.net/npm/blog-gallery@1.0.0/1/20200206161657.webp
#   games_img:

```

前往博客根目录，打开cmd命令窗口执行hexo douban。

```yaml
hexo douban
```

![image-20230210173759429](image-20230210173759429.png)



请注意，我的butterfly主题版本不是最新的，导航菜单栏格式请按照最新的格式写。

![image-20230210173828908](image-20230210173828908.png)

## 添加访客地图

略

## 添加Pixiv日榜

略

## 哔哩哔哩番剧页面插件

```bash
npm install hexo-bilibili-bangumi --save
```

修改站点配置文件_config.yml，添加如下代码：

```yaml
bangumi:
  enable: true 
  vmid: 321638084
  title: '生命不息，追番不止。'
  quote: 'Where there is life, there is life.'
  show: 1
  loading: '/img/bangumi-loading.gif'
```

```
配置说明：

enable: 是否启用
vmid: 哔哩哔哩番剧页面的 vmid(uid), 如何获取？
title: 该页面的标题
quote: 写在页面开头的一段话，支持 html 语法
show: 初始显示页面：0: 想看 , 1: 在看 , 2: 看过，默认为 1
loading: 图片加载完成前的 loading 图片
```

前往博客根目录，打开cmd命令窗口执行hexo new page bangumis。

```bash
hexo new page bangumis
```

找到 BlogRoot/source/bangumis/index.md 这个文件，修改这个文件，添加 type: "bangumis"。

```
---
title: bangumis
date: 2020-12-14 14:43:39
type: "bangumis"
---

```

防止请求次数过多插件不再自动获取番剧数据，所以请根据自己的需要在hexo generate或hexo deploy之前使用hexo bangumi -u命令更新番剧数据。
删除数据命令: hexo bangumi -d

获取 uid
登录哔哩哔哩后前往 https://space.bilibili.com/xxx，网址最后的一串数字就是 uid。





[关于图片加载相关问题 · Issue #134 · HCLonely/hexo-bilibili-bangumi (github.com)](https://github.com/HCLonely/hexo-bilibili-bangumi/issues/134)

## 添加看板娘

略

## 添加吸底音乐播放

略

## 添加贡献日历

略

## 鼠标样式

复制一下内容到`custom.css`

图片可以自己上传，

![image-20220810225621101](image-20220810225621101.png)

像素30*30

```css
body {
    cursor: url(https://bu.dusays.com/2022/05/17/6283c365d20dd.png), auto;
}

.hide-block>.hide-button.open,
.hide-inline>.hide-button.open {
    display: block
}

a,
button,
img {
    cursor: url(https://bu.dusays.com/2022/05/17/6283c376afcfc.png), auto
}

```

## 鼠标跟随效果

略

## 滚动条

透明效果

复制以下内容到`custom.css`

```css
::-webkit-scrollbar {
    width: 8px;
    height: 8px
}

::-webkit-scrollbar-track {
    border-radius: 2em;
    /* background-color: rgba(73, 177, 245, .2); */
}

::-webkit-scrollbar-thumb {
    background-color: rgb(255 255 255 / .3);
    background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.1) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.1) 75%, transparent 75%, transparent);
    border-radius: 2em
}

::-webkit-scrollbar-corner {
    background-color: transparent
}

```

## 手机侧边栏默认不展开

若主题版本大于 v4.0.0，可直接在子目录里添加 hide ：

```yaml
menu:
  Home: / || fas fa-home
  Archives: /archives/ || fas fa-archive
  Tags: /tags/ || fas fa-tags
  Categories: /categories/ || fas fa-folder-open
  List||fas fa-list||hide:
    Music: /music/ || fas fa-music
    Movie: /movies/ || fas fa-video
  Link: /link/ || fas fa-link
  About: /about/ || fas fa-heart

```

## Valine评论邮件回复提醒



## 分类磁贴

略

## 侧边栏电子时钟

略

## 更换字体

`custom.css`

```css
@font-face {
    font-family: 'mindcons';
    /* 字体名自定义即可 */
    src: url('https://fastly.jsdelivr.net/gh/tzy13755126023/BLOG_SOURCE/font/ZhuZiAWan.woff2');
    /* 字体文件路径 */
    font-display: swap;
}

body,
.gitcalendar {
    font-family: mindcons !important;
}

```

## 局部CSS优化

```css

.categoryBar-list {
    max-height: 400px;
}

.clock-row {
    overflow: hidden;
    text-overflow: ellipsis;
}

/*3s为加载动画的时间，1为加载动画的次数，ease-in-out为动画效果*/

#page-header,
#web_bg {
    -webkit-animation: imgblur 2s 1 ease-in-out;
    animation: imgblur 2s 1 ease-in-out;
}

@keyframes imgblur {
    0% {
        filter: blur(5px);
    }
    100% {
        filter: blur(0px);
    }
}

/*适配使用-webkit内核的浏览器 */

@-webkit-keyframes imgblur {
    0% {
        -webkit-filter: blur(5px);
    }
    100% {
        -webkit-filter: blur(0px);
    }
}
.table-wrap img {
    margin: .6rem auto .1rem !important;
}

/* 标签外挂 网站卡片 start */

.site-card-group img {
    margin: 0 auto .1rem !important;
}

.site-card-group .info a img {
    margin-right: 10px !important;
}

[data-theme='dark'] .site-card-group .site-card .info .title {
    color: #f0f0f0 !important;
}

[data-theme='dark'] .site-card-group .site-card .info .desc {
    color: rgba(255, 255, 255, .7) !important;
}

.site-card-group .info .desc {
    margin-top: 4px !important;
}
/* 代码块颜色 */

figure.highlight pre .addition {
    color: #00bf03 !important;
}

```

## 禁止右键及F12等事件

下面开始新的教程，如果你不需要 禁用控制台 以及 禁用一些特殊 keyCode 事件 ，可直接忽略。

修改【BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/layout.pug】，根据图中位置添加以下 pug 代码（跟 head、body同级）。

![image-20230205183438507](image-20230205183438507.png)

```html
  script.
    ((function() {var callbacks = [],timeLimit = 50,open = false;setInterval(loop, 1);return {addListener: function(fn) {callbacks.push(fn);},cancleListenr: function(fn) {callbacks = callbacks.filter(function(v) {return v !== fn;});}}
    function loop() {var startTime = new Date();debugger;if (new Date() - startTime > timeLimit) {if (!open) {callbacks.forEach(function(fn) {fn.call(null);});}open = true;window.stop();alert('你真坏，请关闭控制台！');document.body.innerHTML = "";} else {open = false;}}})()).addListener(function() {window.location.reload();});
  script.
    function toDevtools(){
      let num = 0; 
      let devtools = new Date();
      devtools.toString = function() {
        num++;
        if (num > 1) {
            alert('你真坏，请关闭控制台！')
            window.location.href = "about:blank"
            blast();
        }
      }
      console.log('', devtools);
    }
    toDevtools();
```

将以下代码复制到自定义的custom.js

```js
document.onkeydown = function (e) {
    if (123 == e.keyCode || (e.ctrlKey && e.shiftKey && (74 === e.keyCode || 73 === e.keyCode || 67 === e.keyCode)) || (e.ctrlKey && 85 === e.keyCode)) return btf.snackbarShow("你真坏，不能打开控制台喔!"), event.keyCode = 0, event.returnValue = !1, !1
};

```

重新编译运行，即可看到效果。
注意: 如果自己调试阶段，可注释第一步和第二步中的代码，再进行编译，就可以打开控制台了。部署时放开注释，编译好再丢上去就OK了

## 部分动效说明

略

## 部分页面插入视频

下载文件：[Video-DIY.zip - 蓝奏云 (lanzoui.com)](https://wwe.lanzoui.com/iNoJiww30li)

替换文件或修改文件。
如果你所使用的主题版本是 3.7.1 ，可直接下载文件，将`BlogRoot/node_modules/hexo-theme-butterfly/source/css/_layout/head.styl`替换成新下载的`head.styl`，将`BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/header/index.pug`替换成新下载的`index.pug`。
如果你所使用的主题版本跟本站（v3.7.1）有所出入，请对比一下两个文件（下载的文件和你的主题文件）之间的差异，可能需要你对`BlogRoot/node_modules/hexo-theme-butterfly/source/css/_layout/head.styl`该文件做出一些修改：

```stylus
&.not-home-page
  height: 20rem

  +maxWidth768()
    height: 14rem !important

#page-site-info
  position: absolute
  top: 10rem
  padding: 0 .5rem
  width: 100%
  z-index: 2

  +maxWidth768()
    top: 7rem !important

#post-info
  position: absolute
  ... ...

&.has-video
  position: relative 
  height: 80vh !important
  
  #page-site-info
    top: 50% !important
    margin-top: -1.425em

    +maxWidth768()
      top: 7rem !important
      margin-top: 0
    
  +maxWidth768()
    height: 14rem !important
    
&.not-top-img
  margin-bottom: .5rem
  ... ...

```

主要针对not-home-page、#page-site-info修改一些属性，并新增了一个名为has-video的类。

在自定义 css 中加入以下样式。也可以直接将这段换成style格式写进 head.styl。

```css
#index-video {
    z-index: 0;
    position: absolute;
    top: 0;
    left: 0;
    height: 80vh;
    width: 100%;
    object-fit: cover;
}
@media only screen and (max-width: 768px) {
    #index-video {
        display: none;
    }
}

@media only screen and (min-width: 768px) {
    .bg-cover {
        background-image: none !important;
    }
}


```

在想插入视频的页面，一定要有某个属性 ，可自行配置 ，如果用 type , 则`BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/header/index.pug`中则根据对应的 type 类型去写逻辑即可。
比如我的 `BlogRoot/source/comment/index.md` 配置如下：

```markdown
---
title: 留言板
type: 'comment' 
---
```

所以在`BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/header/index.pug`中的第 23 行加入 `page.type == 'comment'`

```js
- var isHomeClass = is_home() ? 'full_page' : (page.type == 'comment' || page.type == 'link' ) ? 'not-home-page has-video bg-cover' : 'not-home-page'
```

第 51 - 56 行（`if`的同级） 加入

```js
if page.type == 'comment' 
    video#index-video(autoplay='' loop='' muted='')
        source(src='你的视频地址')
if page.type == 'link' 
    video#index-video(autoplay='' loop='' muted='')
        source(src='你的视频地址')

```

## 公告栏两个小人

在【BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/widget/card_announcement.pug】下添加如下部分代码。

注意: 将代码复制到【card_announcement.pug】文件以后，不难发现会有重复的一段代码。你要做的一步操作是，**删除重复的代码（优先保留你主题版本原有的代码）**， 这里之所以没用 Diff 代码块，是因为怕删除【+】号的时候在格式上特别容易出错。

```html
if theme.aside.card_announcement.enable
  .card-widget.card-announcement
    .item-headline
      i.fas.fa-bullhorn.card-announcement-animation
      span= _p('aside.card_announcement')
    .announcement_content!= theme.aside.card_announcement.content
  .xpand(style='height:200px;')
    canvas.illo(width='800' height='800' style='max-width: 200px; max-height: 200px; touch-action: none; width: 640px; height: 640px;')
script(src='https://npm.elemecdn.com/ethan4116-blog/lib/js/other/two-people/twopeople1.js')
script(src='https://npm.elemecdn.com/ethan4116-blog/lib/js/other/two-people/zdog.dist.js')
script#rendered-js(src='https://npm.elemecdn.com/ethan4116-blog/lib/js/other/two-people/twopeople.js')
style.
 .card-widget.card-announcement {
 margin: 0;
 align-items: center;
 justify-content: center;
 text-align: center;
 }
 canvas {
 display: block;
 margin: 0 auto;
 cursor: move;
 }

```



## 星空背景和流星特效

在BlogRoot/node_modules/hexo-theme-butterfly/source/js目录下新建universe.js，输入以下代码：

```js
function dark() {window.requestAnimationFrame=window.requestAnimationFrame||window.mozRequestAnimationFrame||window.webkitRequestAnimationFrame||window.msRequestAnimationFrame;var n,e,i,h,t=.05,s=document.getElementById("universe"),o=!0,a="180,184,240",r="226,225,142",d="226,225,224",c=[];function f(){n=window.innerWidth,e=window.innerHeight,i=.216*n,s.setAttribute("width",n),s.setAttribute("height",e)}function u(){h.clearRect(0,0,n,e);for(var t=c.length,i=0;i<t;i++){var s=c[i];s.move(),s.fadeIn(),s.fadeOut(),s.draw()}}function y(){this.reset=function(){this.giant=m(3),this.comet=!this.giant&&!o&&m(10),this.x=l(0,n-10),this.y=l(0,e),this.r=l(1.1,2.6),this.dx=l(t,6*t)+(this.comet+1-1)*t*l(50,120)+2*t,this.dy=-l(t,6*t)-(this.comet+1-1)*t*l(50,120),this.fadingOut=null,this.fadingIn=!0,this.opacity=0,this.opacityTresh=l(.2,1-.4*(this.comet+1-1)),this.do=l(5e-4,.002)+.001*(this.comet+1-1)},this.fadeIn=function(){this.fadingIn&&(this.fadingIn=!(this.opacity>this.opacityTresh),this.opacity+=this.do)},this.fadeOut=function(){this.fadingOut&&(this.fadingOut=!(this.opacity<0),this.opacity-=this.do/2,(this.x>n||this.y<0)&&(this.fadingOut=!1,this.reset()))},this.draw=function(){if(h.beginPath(),this.giant)h.fillStyle="rgba("+a+","+this.opacity+")",h.arc(this.x,this.y,2,0,2*Math.PI,!1);else if(this.comet){h.fillStyle="rgba("+d+","+this.opacity+")",h.arc(this.x,this.y,1.5,0,2*Math.PI,!1);for(var t=0;t<30;t++)h.fillStyle="rgba("+d+","+(this.opacity-this.opacity/20*t)+")",h.rect(this.x-this.dx/4*t,this.y-this.dy/4*t-2,2,2),h.fill()}else h.fillStyle="rgba("+r+","+this.opacity+")",h.rect(this.x,this.y,this.r,this.r);h.closePath(),h.fill()},this.move=function(){this.x+=this.dx,this.y+=this.dy,!1===this.fadingOut&&this.reset(),(this.x>n-n/4||this.y<0)&&(this.fadingOut=!0)},setTimeout(function(){o=!1},50)}function m(t){return Math.floor(1e3*Math.random())+1<10*t}function l(t,i){return Math.random()*(i-t)+t}f(),window.addEventListener("resize",f,!1),function(){h=s.getContext("2d");for(var t=0;t<i;t++)c[t]=new y,c[t].reset();u()}(),function t(){document.getElementsByTagName('html')[0].getAttribute('data-theme')=='dark'&&u(),window.requestAnimationFrame(t)}()};
dark()

```

在BlogRoot/node_modules/hexo-theme-butterfly/source/css目录下新建universe.css，输入以下代码：

```css
/* 背景宇宙星光  */
#universe{
    display: block;
    position: fixed;
    margin: 0;
    padding: 0;
    border: 0;
    outline: 0;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: -1;
  }

```

在主题配置文件_config.butterfly.yml的inject配置项中bottom下填入：

```yaml
inject:
  bottom:
   # 星空背景
   - <canvas id="universe"></canvas>
   - <script defer src="/js/universe.js"></script>
```

在主题配置文件_config.butterfly.yml的inject配置项中head下填入：

```yaml
inject:
  head:
   ## 星空背景
   - <link rel="stylesheet" href="/css/universe.css">

```

## 樱花飘落效果

在主题配置文件_config.butterfly.yml的inject配置项中bottom下引入sakura.js即可。

```js
inject:
  bottom:
   # 樱花飘落效果
   # - <script async src="https://npm.elemecdn.com/tzy-blog/lib/js/other/sakura.js"></script>

```

不建议加

## 灯笼特效

过年的时候可以加

https://tzy1997.com/articles/Ha5487ng/

## 外挂标签

常用语法

[Butterfly 安裝文檔(三) 主題配置-1 | Butterfly](https://butterfly.js.org/posts/4aa8abbe/#標籤外掛（Tag-Plugins）)

https://tzy1997.com/articles/0xiipgum/

[Tag Plugins Plus | Akilarの糖果屋](https://akilar.top/posts/615e2dec)

如有使用了本站的外挂标签插件的读者，请确保自己的配置内容为最新。

同理，若您在使用本帖教程后，发现样式无法完全还原文档内效果，请重点排查您的其余第三方魔改css样式，例如css中是否存在**circle**、**square**等易重class名。



源码修改配置方案适用于不想应用全部外挂标签的用户，供熟悉外挂标签原理的用户自行选择装配需要的标签文件。

1. 下载资源文件：https://github.com/Akilarlxh/hexo-butterfly-tag-plugins-plus

   ```bash
   npm install hexo-butterfly-tag-plugins-plus --save
   ```

   

2. 将下载的`hexo-butterfly-tag-plugins-plus.zip`解压得到资源文件夹,下文以`[tag_plugins_file]`指代该文件夹。

3. 将`[tag_plugins_file]\lib\scripts`目录下的文件放到`[Blogroot]\themes\butterfly\scripts\tag\`文件夹内。

4. 将`[tag_plugins_file]\lib\style`目录下的文件放到`[Blogroot]\themes\butterfly\source\css\tags\`文件夹内。

5. 修改`[Blogroot]\_config.butterfly.yml`的`inject`配置项，添加`CDN`依赖项。由于`issues`写入`timeline`和`site-card`标签要用到`jquery`，请务必根据注释指示的版本**决定是否添加**

   ```yaml
   inject:
     head:
       - <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/l-lin/font-awesome-animation/dist/font-awesome-animation.min.css"  media="defer" onload="this.media='all'">  #动画标签anima的依赖
       - <script async src="https://npm.elemecdn.com/hexo-butterfly-tag-plugins-plus@latest/lib/carousel-touch.min.js"></script> #carousel相册鼠标动作的依赖
     bottom:
       - <script defer src="https://npm.elemecdn.com/jquery@latest/dist/jquery.min.js"></script>
       # 自butterfly_v3.4.0+开始，主题基本实现去jquery化，需要自己添加引用，请读者根据版本自行决定是否添加这行引用。
       - <script defer src="https://npm.elemecdn.com/hexo-theme-volantis@4.3.1/source/js/issues.js"></script>
       #数据集合标签issues的依赖
   ```

6. 考虑到hexo自带的markdown渲染插件`hexo-renderer-marked`与外挂标签语法的兼容性较差，建议您将其替换成[hexo-renderer-kramed](https://www.npmjs.com/package/hexo-renderer-kramed)

   ```bash
   npm uninstall hexo-renderer-marked --save
   npm install hexo-renderer-kramed --save
   ```

7. 外挂标签使用方案请参阅下文。

### 引用note

修改主题文件：

```yaml
note:
  # Note tag style values:
  #  - simple    bs-callout old alert style. Default.
  #  - modern    bs-callout new (v2-v3) alert style.
  #  - flat      flat callout style with background, like on Mozilla or StackOverflow.
  #  - disabled  disable all CSS styles import of note tag.
  style: flat
  icons: true
  border_radius: 3
  # Offset lighter of background in % for modern and flat styles (modern: -12 | 12; flat: -18 | 6).
  # Offset also applied to label tag variables. This option can work with disabled note tag.
  light_bg_offset: 0
```

Note标签外挂有两种用法。icons和light_bg_offset只对方法一生效。

方法一：

```
{% note [class] [no-icon] [style] %}
Any content (support inline tags too.io).
{% endnote %}
```

方法二：

```
{% note [color] [icon] [style] %}
Any content (support inline tags too.io).
{% endnote %}
```

### 上标标签 tip

语法

```
{% tip [参数，可选] %}文本内容{% endtip %}
```

示例

```
{% tip %}默认情况{% endtip %}
{% tip success %}success{% endtip %}
{% tip error %}error{% endtip %}
{% tip warning %}warning{% endtip %}
{% tip bolt %}bolt{% endtip %}
{% tip ban %}ban{% endtip %}
{% tip home %}home{% endtip %}
{% tip sync %}sync{% endtip %}
{% tip cogs %}cogs{% endtip %}
{% tip key %}key{% endtip %}
{% tip bell %}bell{% endtip %}
{% tip fa-atom %}自定义font awesome图标{% endtip %}
```



### 动态标签 anima

语法

```
{% tip [参数，可选] %}文本内容{% endtip %}
```

示例

```
{% tip warning faa-horizontal animated %}warning{% endtip %}

```



### 分栏 tab

语法

```
{% tabs Unique name, [index] %}
<!-- tab [Tab caption] [@icon] -->
Any content (support inline tags too).
<!-- endtab -->
{% endtabs %}

```

示例

```
{% tabs test4 %}
<!-- tab 第一个Tab -->
**tab名字为第一个Tab**
<!-- endtab -->

<!-- tab @fab fa-apple-pay -->
**只有图标 没有Tab名字**
<!-- endtab -->

<!-- tab 炸弹@fas fa-bomb -->
**名字+icon**
<!-- endtab -->
{% endtabs %}

```



### 时间轴 timeline

```
{% timeline 时间线标题（可选） %}
{% timenode 时间节点（标题） %}
正文内容
{% endtimenode %}
{% timenode 时间节点（标题） %}
正文内容
{% endtimenode %}
{% endtimeline %}

```

```
{% timeline %}

{% timenode 2020-07-24 [2.6.6 -> 3.0](https://github.com/volantis-x/hexo-theme-volantis/releases) %}

1. 如果有 `hexo-lazyload-image` 插件，需要删除并重新安装最新版本，设置 `lazyload.isSPA: true`。
2. 2.x 版本的 css 和 js 不适用于 3.x 版本，如果使用了 `use_cdn: true` 则需要删除。
3. 2.x 版本的 fancybox 标签在 3.x 版本中被重命名为 gallery 。
4. 2.x 版本的置顶 `top: true` 改为了 `pin: true`，并且同样适用于 `layout: page` 的页面。
5. 如果使用了 `hexo-offline` 插件，建议卸载，3.0 版本默认开启了 pjax 服务。

{% endtimenode %}

{% timenode 2020-05-15 [2.6.3 -> 2.6.6](https://github.com/volantis-x/hexo-theme-volantis/releases/tag/2.6.6) %}

不需要额外处理。

{% endtimenode %}

{% timenode 2020-04-20 [2.6.2 -> 2.6.3](https://github.com/volantis-x/hexo-theme-volantis/releases/tag/2.6.3) %}

1. 全局搜索 `seotitle` 并替换为 `seo_title`。
2. group 组件的索引规则有变，使用 group 组件的文章内，`group: group_name` 对应的组件名必须是 `group_name`。
3. group 组件的列表名优先显示文章的 `short_title` 其次是 `title`。

{% endtimenode %}

{% endtimeline %}

```

![image-20230205210606143](image-20230205210606143.png)

语法更新了：https://butterfly.js.org/posts/4aa8abbe/#timeline

```
{% timeline 2023 %}

<!-- timeline 01-30 ~ 02-01 -->

- `vue2`对象及数组数据的响应式原理

<!-- endtimeline -->

<!-- timeline 02-02 ~ 02-07 -->

- `hexo-butterfly`配置了解，优化网站视觉

<!-- endtimeline -->

{% endtimeline %}


```

## 自定义右键菜单

暂时先不弄

## 加载动画

https://akilar.top/posts/3d221bf2/

## 评论弹幕

暂略

## 自定义页脚

https://tzy1997.com/articles/hexo1617/

## 侧边栏公众号

https://tzy1997.com/articles/hexo1618/

本人用的是npm方式安装的 hexo-theme-butterfly，后续魔改时更改的文件都是【BlogRoot/node_modules/hexo-theme-butterfly】文件夹中的文件。如果你是git clone方式安装的主题，请在【BlogRoot/themes/butterfly】文件夹下修改对应的文件。



在BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/widget文件夹下新建card_wx.pug文件，
具体位置如下图：

![image-20230205214254240](image-20230205214254240.png)

```
#card-wechat.card-widget.tzy-right-widget
    #flip-wrapper
        #flip-content
            .face
            .back.face
```

注意，复制完要格式化一下（vscode里用插件）

在BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/widget/index.pug中引入上一步中创建的card_wx.pug文件。
具体位置如下图：

![image-20230205214441034](image-20230205214441034.png)

将以下代码复制到自定义的custom.css中，不会自定义css的请阅读 Hexo + Butterfly 一些常见问题 一文中关于【关于自定义的 js 和 css 文件】部分。

```css
/* 公众号 Start */

[data-theme='light'] #aside-content .card-widget#card-wechat {
    background: #49b1f5 !important;
}

#aside-content .card-widget#card-wechat {
    background: var(--card-bg);
    display: flex;
    justify-content: center;
    align-content: center;
    padding: 0;
    cursor: pointer !important;
    border: none;
    height: 110px;
}

/* 如果你设置了aside 的 mobile 为 false，记得放开下面这段注释；
   如果你设置了aside 的 mobile 为 true ，不需要改动。 */

/* @media screen and (max-width: 768px) {
    #aside-content .card-widget#card-wechat {
        display: none !important;
    }
} */

@media screen and (min-width: 1300px) {
    #aside-content .card-widget {
        margin-top: 1rem;
    }
}

#flip-wrapper {
    -webkit-perspective: 1000;
    perspective: 1000;
    position: relative;
    width: 235px;
    height: 110px;
    z-index: 1;
}

#flip-wrapper:hover #flip-content {
    -webkit-transform: rotateY(180deg);
    transform: rotateY(180deg);
}

#flip-content {
    width: 100%;
    height: 100%;
    -webkit-transform-style: preserve-3d;
    transform-style: preserve-3d;
    transition: cubic-bezier(0, 0, 0, 1.29) 0.3s;
}

.face {
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    background: url(https://img.zhheo.com/i/2022/08/31/630efc6e3e794.png) center center no-repeat;
    background-size: 100%;
}

.back.face {
    display: block;
    -webkit-transform: rotateY(180deg);
    transform: rotateY(180deg);
    box-sizing: border-box;
    background: url(https://bu.dusays.com/2022/10/30/635e9c6a228a3.png) center center no-repeat;
    background-size: 100%;
}

/* 公众号 End */


```

此段css中，你需要将`background: #49b1f5 !important`中的`#49b1f5`换成你自己的主题色，另外还需要将 https://bu.dusays.com/2022/10/30/635e9c6a228a3.png 这个图片中的二维码部分换成你自己公众号的二维码，你可以使用 [在线PS图片 工具](https://www.uupoop.com/#/)，将图中的二维码换成你公众号的二维码。

## 文章加密插件

略

## `github`徽标

### 具体步骤

https://tzy1997.com/articles/kfwr2gpa/

github徽标可以直接通过[shields.io](https://shields.io/)在线生成。
理论上可以放在页面的任何地方。教程案例是添加在页脚。
工具网站包括：
徽标生成网站:[shields](https://shields.io/)
图标查询网站:[simpleicons](https://simpleicons.org/)
html压缩网站:[htmlpack](http://tool.ggo.net/htmlpack/)
转义字符查询

具体步骤

通过shields.io在线生成。
label:标签，徽标左侧内容
message:信息，徽标右侧内容
color:色值,支持支持十六进制、rgb、rgba、hsl、hsla和 css 命名颜色。十六进制记得删除前面的#号

输入相关信息后，点击make badge即可得到徽标的URL。可以用img标签引用，写法简单。不过正式写法建议用object标签引用，写法示例如下。

```html
<!-- label=Frame，Message=Hexo，color=blue -->
https://img.shields.io/badge/Frame-Hexo-blue
<!-- 在页面上可以使用img标签来引用 -->
<img src="https://img.shields.io/badge/Frame-Hexo-blue">
<!-- 部分属性例如link需要用object标签来引用 -->
<object data="https://img.shields.io/badge/Frame-Hexo-blue?link=https://hexo.io"></object>
```

拓展写法示例

```html
<!-- 普通样式 -->
<img src="https://img.shields.io/badge/Frame-Hexo-blue">
<!-- 五种style预览 -->
<img src="https://img.shields.io/badge/Frame-Hexo-blue?logo=Hexo&style=plastic">
<img src="https://img.shields.io/badge/Frame-Hexo-blue?logo=Hexo&style=flat">
<img src="https://img.shields.io/badge/Frame-Hexo-blue?logo=Hexo&style=flat-square">
<img src="https://img.shields.io/badge/Frame-Hexo-blue?logo=Hexo&style=for-the-badge">
<img src="https://img.shields.io/badge/Frame-Hexo-blue?logo=Hexo&style=social">
<!-- 添加图标和自定义label -->
<img src="https://img.shields.io/badge/Frame-Hexo-blue?logo=Hexo&label=框架">
<!-- 添加图标和图标宽度 -->
<img src="https://img.shields.io/badge/Frame-Hexo-blue?logo=Hexo&logoWidth=30">
<!-- 图标、label、message三部分颜色自定义 -->
<img src="https://img.shields.io/badge/Frame-Hexo-blue?logo=Hexo&label=框架&logoColor=violet&labalColor=#1fd041&color=rgb(222, 31, 31)">
<!-- 给标签添加链接 -->
<object data="https://img.shields.io/badge/Frame-Hexo-blue?logo=Hexo&link=https://hexo.io/&https://hexo.io/zh-cn/docs/"></object>
<!-- 也可以通过嵌套a标签来实现添加链接 -->
<a target="_blank" href="https://hexo.io" title="框架采用Hexo"><img src="https://img.shields.io/badge/Frame-Hexo-blue"></a>

```

![image-20230202162912911](image-20230202162912911.png)



在主题配置文件_config.butterfly.yml的footer配置项中添加徽标，注意事先压缩一下，使他们只留一行。为了不至于太过紧凑，用 (空格的转义字符)隔开。

```diff
      footer:
        owner:
          enable: true
          since: 2020
-       custom_text:
+       custom_text: <p><a target="_blank" href="https://hexo.io/"><img src="https://img.shields.io/badge/Frame-Hexo-blue?style=flat&logo=hexo" title="博客框架为Hexo"></a>&nbsp;<a target="_blank" href="https://demo.jerryc.me/"><img src="https://img.shields.io/badge/Theme-Butterfly-6513df?style=flat&logo=bitdefender" title="主题采用butterfly"></a>&nbsp;<a target="_blank" href="https://metroui.org.ua/index.html "><img src="https://img.shields.io/badge/CDN-jsDelivr-orange?style=flat&logo=jsDelivr" title="本站使用JsDelivr为静态资源提供CDN加速"></a> &nbsp;<a target="_blank" href="https://vercel.com/ "><img src="https://img.shields.io/badge/Hosted-Vervel-brightgreen?style=flat&logo=Vercel" title="本站采用双线部署，默认线路托管于Vercel"></a>&nbsp;<a target="_blank" href="https://vercel.com/ "><img src="https://img.shields.io/badge/Hosted-Coding-0cedbe?style=flat&logo=Codio" title="本站采用双线部署，联通线路托管于Coding"></a>&nbsp;<a target="_blank" href="https://github.com/"><img src="https://img.shields.io/badge/Source-Github-d021d6?style=flat&logo=GitHub" title="本站项目由Gtihub托管"></a>&nbsp;<a target="_blank" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img src="https://img.shields.io/badge/Copyright-BY--NC--SA%204.0-d42328?style=flat&logo=Claris" title="本站采用知识共享署名-非商业性使用-相同方式共享4.0国际许可协议进行许可"></a></p>
        copyright: false # Copyright of theme and framework
        ICP: # Chinese ICP License
```

### 插件化写法

修改BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/footer.pug,添加页脚标签循环节：

```diff
    if theme.footer.custom_text
      .footer_custom_text!=`${theme.footer.custom_text}`
    //v3.4.0以下版本可能还有ICP的配置项。此处只要保证p和上方的if缩进平级就好。
+   p#ghbdages
+     if theme.ghbdage.enable
+       each item in theme.ghbdage.bdageitem
+         a.github-badge(target='_blank' href=url_for(item.link)  style='margin-inline:5px')
+           img(src=url_for(item.shields) title=item.message)

```

在主题配置文件_config.butterfly.yml中添加相关配置项：

```yaml
ghbdage:
  enable: true
  bdageitem:
    - link: https://hexo.io/  # 标签跳转链接
      shields: https://img.shields.io/badge/Frame-Hexo-blue?style=flat&logo=hexo #shields的API链接，填法参考本篇教程
      message: 博客框架为Hexo_v5.3.0 #鼠标悬停时显示的信息
    - link: https://demo.jerryc.me/
      shields: https://img.shields.io/badge/Theme-Butterfly-6513df?style=flat&logo=bitdefender
      message: 主题版本Butterfly_v3.4.2
    - link: https://metroui.org.ua/index.html
      shields: https://img.shields.io/badge/CDN-jsDelivr-orange?style=flat&logo=jsDelivr
      message: 本站使用JsDelivr为静态资源提供CDN加速
    - link: https://vercel.com/
      shields: https://img.shields.io/badge/Hosted-Vervel-brightgreen?style=flat&logo=Vercel
      message: 本站采用双线部署，默认线路托管于Vercel
    - link: https://vercel.com/
      shields: https://img.shields.io/badge/Hosted-Coding-0cedbe?style=flat&logo=Codio
      message: 本站采用双线部署，联通线路托管于Coding
    - link: https://github.com/
      shields: https://img.shields.io/badge/Source-Github-d021d6?style=flat&logo=GitHub
      message: 本站项目由Gtihub托管
    - link: http://creativecommons.org/licenses/by-nc-sa/4.0/
      shields: https://img.shields.io/badge/Copyright-BY--NC--SA%204.0-d42328?style=flat&logo=Claris
      message: 本站采用知识共享署名-非商业性使用-相同方式共享4.0国际许可协议进行许可
```

### 外挂标签

考虑到对shields.io的全部参数支持，外挂标签使用object标签来引用。

新建BlogRoot/node_modules/hexo-theme-butterfly/scripts/tag/ghbdage.js

```js
function bdage (args) {

  args = args.join(' ').split('||')

  let base= args[0]?args[0].split(','):''
  let right = base[0]?encodeURI(base[0].trim()):''
  let left = base[1]?encodeURI(base[1].trim()):''
  let logo = base[2]?base[2].trim():''

  let message = args[1]?args[1].split(','):''
  let color = message[0]?message[0].trim():'orange'
  let link = message[1]?message[1].trim():''
  let title = message[2]?message[2].trim():''

  let option = args[2]?args[2].trim():''

  return `<object title="${title}" standby="loading..." data="https://img.shields.io/badge/${left}-${right}-orange?logo=${logo}&color=${color}&link=${link}&${option}"></object>`
}
hexo.extend.tag.register('bdage',bdage);



```

具体用法

```markdown
{% bdage [right],[left],[logo]||[color],[link],[title]||[option] %}

```

配置参数

```
left：徽标左边的信息，必选参数。
right: 徽标右边的信息，必选参数，
logo：徽标图标，图标名称详见simpleicons，可选参数。
color：徽标右边的颜色，可选参数。
link：指向的链接，可选参数。
title：徽标的额外信息，可选参数。主要用于优化 SEO，但 object 标签不会像 a 标签一样在鼠标悬停显示 title 信息。
option：自定义参数，支持shields.io的全部API参数支持，具体参数可以参看上文中的拓展写法示例。形式为 name1=value2&name2=value2。
```

基本参数,定义徽标左右文字和图标

```
{% bdage Theme,Butterfly %}
{% bdage Frame,Hexo,hexo %}


```

信息参数，定义徽标右侧内容背景色，指向链接

```
{% bdage CDN,JsDelivr,jsDelivr||abcdef,https://metroui.org.ua/index.html,本站使用JsDelivr为静态资源提供CDN加速 %}
//如果是跨顺序省略可选参数，仍然需要写个逗号,用作分割
{% bdage Source,GitHub,GitHub||,https://github.com/ %}


```

拓展参数，支持shields的API的全部参数内容

```
{% bdage Hosted,Vercel,Vercel||brightgreen,https://vercel.com/,本站采用双线部署，默认线路托管于Vercel||style=social&logoWidth=20 %}
//如果是跨顺序省略可选参数组，仍然需要写双竖线||用作分割
{% bdage Hosted,Vercel,Vercel||||style=social&logoWidth=20&logoColor=violet %}

```

### 拓展内容-使用纯css实现仿徽标样式

```html
<div class="github-badge">
  <a style="color:#fff" href="https://hexo.io/" target="_blank" title="由 Hexo 强力驱动">
    <span class="badge-subject">
      <!-- fa图标，也支持阿里图标 -->
      <i class="fa fa-copyright"></i>
      Powered
    </span>
    <span class="badge-value bg-blue">
      Hexo
    </span>
  </a>
</div>

```

```css
/*标签整体样式*/
.github-badge {
  margin-left: 5px;
  display: inline-block;
  border-radius: 4px;
  text-shadow: none;
  color: #fff;
  line-height: 15px;
  background-color: #abbac3;
  margin-bottom: 5px;
  font-size: 12px;
}
/* 超链接下划线隐藏 */
.github-badge a {
  text-decoration: none;
}
/* 标签左侧样式 */
.github-badge .badge-subject {
  background-color: #4d4d4d;
  padding: 4px 4px 4px 6px;
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
}
/* 标签右侧样式 */
.github-badge .badge-value {
  padding: 4px 6px 4px 4px;
  border-top-right-radius: 4px;
  border-bottom-right-radius: 4px;
}
/* 标签背景色，随意自定义，渐变色也可以 */
.github-badge .bg-blue {
  background-color: #007ec6;
}

.github-badge .bg-green {
  background-color: #4dc820;
}

.github-badge .bg-orange {
  background-color: orange;
}

.github-badge .bg-gradient {
  background: linear-gradient(to right, #3ca5f6, #a86af9);
}

.github-badge .bg-violet {
  background-color: #8833d7;
}


```



## 评论系统

https://tzy1997.com/articles/hexo1611/

从3.0.0开始，开启评论需要在comments-use中填写你需要的评论，这里参照你主题版本的格式写。

支持双评论显示，只需要配置两个评论（第一个为默认显示）

```yaml
comments:
  # Up to two comments system, the first will be shown as default
  # Choose: Disqus/Disqusjs/Livere/Gitalk/Valine/Waline/Utterances/Facebook Comments/Twikoo
  use:
    # - Disqus
    # - Valine
    - Twikoo # 这里按照你主题版本的格式写
  text: true # Display the comment name next to the button
  # lazyload: The comment system will be load when comment element enters the browser's viewport.
  # If you set it to true, the comment count will be invalid
  lazyload: true
  count: true # Display comment count in post's top_img
  card_post_count: true # Display comment count in Home Page

```

```
参数	解释
use	使用的评论（请注意，最多支持两个，如果不需要请留空）
注意：双评论不能是 Disqus 和 Disqusjs 一起，由于其共用同一个 ID，会出错
text	是否显示评论服务商的名字
lazyload	是否为评论开启lazyload，开启后，只有滚动到评论位置时才会加载评论所需要的资源（开启 lazyload 后，评论数将不显示）
count	是否在文章顶部显示评论数
livere、Giscus 和 utterances 不支持评论数显示
card_post_count	是否在首页文章卡片显示评论数
gitalk、livere 、Giscus 和 utterances 不支持评论数显
```

### Twikoo（推荐）



Twikoo 是一个简洁、安全、免费的静态网站评论系统，基于腾讯云开发。

#### 特色

免费搭建（使用云开发作为评论后台，每个用户均长期享受1个免费的标准型基础版1资源套餐）
简单部署（支持一键部署、手动部署、命令行部署）



支持回复、点赞
无需额外适配，支持搭配浅色主题与深色主题使用
支持 API 调用，批量获取文章评论数、最新评论
访客在昵称栏输入 QQ 号，会自动补全 QQ 昵称和 QQ 邮箱
访客填写数字 QQ 邮箱，会使用 QQ 头像作为评论头像
支持评论框粘贴图片（可禁用）
支持插入图片（可禁用）
支持去不图床、云开发图床
支持插入表情（可禁用）
支持 Ctrl + Enter 快捷回复
评论框内容实时保存草稿，刷新不会丢失
支持 Katex 公式
支持按语言的代码高亮



隐私信息安全（通过云函数控制敏感字段（邮箱、IP、环境配置等）不会泄露）
支持 Akismet 垃圾评论检测（需自行注册 akismet.com）
支持腾讯云内容安全垃圾评论检测（需自行注册 腾讯云内容安全）
支持人工审核模式
防 XSS 注入
支持限制每个 IP 每 10 分钟最多发表多少条评



支持邮件提醒（访客和博主）
支持微信提醒（仅针对博主，基于 Server酱，需自行注册）
支持 QQ 提醒（仅针对博主，基于 Qmsg酱，需自行注册）
支持 QQ 提醒（针对博主QQ或者群，基于 go-cqhttp，需自己有服务器）



支持自定义评论框背景图片
支持自定义“博主”标识文字
支持自定义通知邮件模板
支持自定义评论框提示信息（placeholder）
支持自定义表情列表（兼容 OwO 的数据格式）
支持自定义【昵称】【邮箱】【网址】必填 / 选填
支持自定义代码高亮主题



内嵌式管理面板，通过密码登录，可方便地查看评论、隐藏评论、删除评论、修改配置
支持隐藏管理入口，通过输入暗号显示
支持从 Valine、Artalk、Disqus 导入评论



国外请求较慢
部署需要实名认证
不支持 IE



> 本站是用 Vercel + MongoDB 方案搭建 Twikoo 评论系统。
> 其他几种部署方式这里不做讲解，详情请参考：[Twikoo 文档](https://twikoo.js.org/) 。

[快速上手 | Twikoo 文档](https://twikoo.js.org/quick-start.html#vercel-部署)

#### Vercel 部署

申请 MongoDB 账号

创建免费 MongoDB 数据库，区域推荐选择 【AWS / N. Virginia (us-east-1)】，实例名自定义：db-mindcons

创建数据库用户（请记住这里的 password，后面步骤需要使用到），按步骤设置允许所有 IP（0.0.0.0/0）地址的连接（为什么？），填完信息后，点击【Finish and Close】

在 Clusters 页面点击 【Connect】，选择【Connect your appliction】，记录数据库连接字符串，请将连接字符串中的`<password>`修改为第三步中数据库密码，留着备用（将在第7步中用到）。

```
mongodb+srv://mindcons:<password>@db-mindcons.s0bqlbt.mongodb.net/?retryWrites=true&w=majority
```

申请 Vercel 账号，可以选择 Github 账号来同步

点击 此链接 将 [Twikoo](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fimaegoo%2Ftwikoo%2Ftree%2Fmain%2Fsrc%2Fserver%2Fvercel-min) 一键部署到 Vercel

点击 Create，等待 Deploy完成

进入【Settings】->【Environment Variables】，添加环境变量【MONGODB_URI】，值为第 4 步的数据库连接字符串，Environment选项需要都勾选

进入【Deployments】，然后在任意一项后面点击更多（三个点），然后点击【Redeploy】，最后点击下面的【Redeploy】

进入【Overview】，点击【Domains】下方的链接，如果环境配置正确，可以看到 “Twikoo 云函数运行正常” 的提示

Vercel Domains（包含 https:// 前缀，例如 https://xxx.vercel.app）即为您的环境 id

在主题中写入 Twikoo 配置项。
在主题配置文件_config.butterfly.yml中修改以下内容，将你的环境id填入对应位置

```yaml
# Twikoo
# https://github.com/imaegoo/twikoo
twikoo:
  envId: https://xxxxxx.vercel.app/ 
  region: 
  visitor: true
  option:

```

```
参数	解释
envId	环境id
region	环境地域，默认为 ap-shanghai，如果您的环境地域不是上海，需传此参数
visitor	是否显示文章閲读数
option	可选配置
```

> 开启 visitor 后，文章页的访问人数将改为 Twikoo 提供，而不是 不蒜子。

重新编译运行，即可看到效果，点击评论区输入框下方的齿轮状按钮，设置你的管理密码，具体配置信息这里不做讲解，按照注解进行配置即可。

[常见问题 | Twikoo 文档](https://twikoo.js.org/faq.html#如何获得管理面板的私钥文件)

[Twikoo Vercel 部署教程_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Fh411e7ZH/?vd_source=1b462828c3eae49e5645f411d81e5ea8)

如果没出现让你设置密码的界面，需要科学上网

![image-20230206073924966](image-20230206073924966.png)

【补充】Vercel绑定自己的域名：

[【Hexo博客】Twikoo评论系统的免费部署(云函数采用Vercel方式) | 百里飞洋 (meta-code.top)](https://blog.meta-code.top/2022/03/16/2022-42/)

[关于Vercel被墙导致获取Twikoo评论失败的解决方案 | 唐志远の博客 (tzy1997.com)](https://tzy1997.com/articles/hexo1614/)

(1) 给自己域名添加一个解析记录

前往自己的域名解析平台，添加一个解析记录。我用阿里云平台的云解析DNS做演示：

记录类型：CNAME-将域名指向另外一个域名
记录值：可以填twikoo，它将作为子域名地址。
解析线路：默认即可
记录值：填vercel-dns.com
TTL：默认10分钟即可

![image-20230206090447535](image-20230206090447535.png)

(2) 在Vercel添加域

前往登录Vercel：https://vercel.com/
点击右上角头像，打开Dashboard
选中自己当初创建的twikoo项目，点击进入
选择 Settings => Domains，添加域，也就是咱们刚刚给自己域名添加的那个解析记录地址

![image-20230206090519213](image-20230206090519213.png)

(3) 修改博客主题相关配置

打开电脑本地项目，找到主题配置的Twikoo部分。

把以前那个环境地址envId换成咱们的解析记录地址`https://twikoo.二级域名.域名/`



现在就不会卡了，也不会出现评论失败的情况（注意看清楚开发环境和生产环境，别调试错了）

#### 实现邮件通知

https://blog.csdn.net/weixin_58068682/article/details/122770936

> 以下教程以[QQ邮箱](http://mail.qq.com/)为例，其他邮箱可自行摸索，原理大同小异。

**开通POP3/SMTP服务**

![开通服务.png](watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQW1uZXNpYV9GdQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center.png)

按提示操作，获取的授权码后面会用到，记得留存。

**配置Twikoo**

在一个已经有评论的文章页

登录管理后台，还是需要科学上网，因为访问的是https://twikoo-saiable.vercel.app/

进入`配置管理 - 邮件通知`，按照下方提供的标准填写即可。

```
SENDER_EMAIL: <你的QQ邮箱地址>
SMTP_SERVICE: <你的邮件服务提供商>
SMTP_HOST: <自定义 SMTP 服务器地址>
SMTP_PORT: <自定义 SMTP 端口>
SMTP_SECURE: <自定义 SMTP 是否使用 TLS>
SMTP_USER: <邮件通知邮箱用户名>(需与SENDER_EMAIL一致)
SMTP_PASS: <邮件通知邮箱密码>(授权码)

```

![image-20230206105004594](image-20230206105004594.png)



#### menhera 表情样式优化

因为 twikoo 的默认宽度是 3em ， 对于 menhera-chan 等其他长宽较大的表情根本无法看清，所以将它pc端评论后的表情加载设置成300px，设屏宽小于768px的，让它继承继承父元素的 100%宽 - 30px ，30px是为了与右侧有一段细微间隔，下图可以看到手机端的时候，表情和盒子最右侧是有一定距离的。

对于设屏宽小于768px，选择 menhera-chan 表情时，宽度太小，看不清图片，所以这里将宽度调整为设备宽的 50% 宽 - 10px。其他表情保持不变，只对 menhera-chan 表情做出改善。

若你的自定义表情中有其他跟 menhera-chan表情 类似的需求，可照着下面的 css 去改写，增加对应的类或者属性即可。

将以下代码复制到custom.css即可。

```css
/* Twikoo 评论样式 */

.tk-input .el-textarea__inner {
    min-height: 120px !important;
}

#twikoo .OwO-body {
    max-width: 100% !important;
}

#twikoo .OwO .OwO-body .OwO-items:nth-child(1),
#twikoo .OwO .OwO-body .OwO-items:nth-child(4) {
    max-height: 360px !important;
}

#twikoo .OwO-items li[title|=menhera] img {
    width: 100% !important;
    margin: 5px 10px;
}

.tk-comment .tk-owo-emotion[alt*=menhera] {
    width: 300px !important;
}

.tk-comment .vemoji[alt|=menhera],
.tk-comment .tk-owo-emotion[alt*=menhera] {
    max-width: 300px !important;
    max-height: 300px !important;
    margin: 8px 1px;
    display: block !important;
}

@media screen and (max-width: 768px) {
    .tk-comment .vemoji[alt|=menhera], .tk-comment .tk-owo-emotion[alt*=menhera] {
        max-width: calc(100% - 30px) !important;
        max-height: calc(100% - 30px) !important;
    }
    .OwO .OwO-body .OwO-items-image .OwO-item[title*=menhera] {
        max-width: calc(50% - 10px);
        box-sizing: border-box;
    }
    
}

```

## 自定义右键菜单栏

https://tzy1997.com/articles/hexo1608/

在BlogRoot/node_modules/hexo-theme-butterfly/layout/includes文件夹下新建一个right-menu的文件夹，在此文件夹下新建一个index.pug文件。
具体位置如下图：

![image-20230206145902027](image-20230206145902027.png)

将以下代码复制到文件中。

```pug
#rightMenu
    .rightMenu-group.rightMenu-small
        .rightMenu-item#menu-backward
            i.fa-solid.fa-arrow-left
        .rightMenu-item#menu-forward
            i.fa-solid.fa-arrow-right
        .rightMenu-item#menu-refresh
            i.fa-solid.fa-arrow-rotate-right
        .rightMenu-item#menu-home
            i.fa-solid.fa-house
    .rightMenu-group.rightMenu-line.rightMenuOther
        a.rightMenu-item.menu-link(href='/archives/')
            i.fa-solid.fa-archive
            span='文章归档'
        a.rightMenu-item.menu-link(href='/categories/')
            i.fa-solid.fa-folder-open
            span='文章分类'
        a.rightMenu-item.menu-link(href='/tags/')
            i.fa-solid.fa-tags
            span='文章标签'
    .rightMenu-group.rightMenu-line.rightMenuNormal
        a.rightMenu-item.menu-link#menu-radompage(href='/random/index.html')
            i.fa-solid.fa-shoe-prints
            span='随便逛逛'
        .rightMenu-item#menu-translate
            i.fa-solid.fa-earth-asia
            span='繁简切换'
        .rightMenu-item#menu-darkmode
            i.fa-solid.fa-moon
            span='切换模式'
#rightmenu-mask

```

在BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/layout.pug中引入上一步中创建的index.pug文件。
具体位置如下图：

![image-20230206150208453](image-20230206150208453.png)

在BlogRoot/node_modules/hexo-theme-butterfly/source/js文件夹下新建一个rightMenu.js，将以下代码复制到文件中。

```js
var rm = {};
rm.showRightMenu = function (isTrue, x = 0, y = 0) {
    let $rightMenu = $('#rightMenu');
    $rightMenu.css('top', x + 'px').css('left', y + 'px');

    if (isTrue) {
        stopMaskScroll()
        $rightMenu.show();
    } else {
        $rightMenu.hide();
    }
};
let rmWidth = $('#rightMenu').width();
let rmHeight = $('#rightMenu').height();
rm.reloadrmSize = function () {
    rmWidth = $("#rightMenu").width();
    rmHeight = $("#rightMenu").height()
};
window.oncontextmenu = function (event) {
    if (document.body.clientWidth > 768) {
        let pageX = event.clientX + 10;	
        let pageY = event.clientY;
        let $rightMenuNormal = $(".rightMenuNormal");
        let $rightMenuOther = $(".rightMenuOther");
        let $rightMenuReadmode = $("#menu-readmode");
        $rightMenuNormal.show();
        $rightMenuOther.show();
        rm.reloadrmSize();
        if (pageX + rmWidth > window.innerWidth) {
            pageX -= rmWidth;
        }
        if (pageY + rmHeight > window.innerHeight) {
            pageY -= rmHeight;
        }
        rm.showRightMenu(true, pageY, pageX);
        $('#rightmenu-mask').attr('style', 'display: flex');
        return false;
    }
};
function removeRightMenu() {
    rm.showRightMenu(false);
    $('#rightmenu-mask').attr('style', 'display: none');
}
function stopMaskScroll() {
    if (document.getElementById("rightmenu-mask")) {
        let xscroll = document.getElementById("rightmenu-mask");
        xscroll.addEventListener("mousewheel", function (e) {
            removeRightMenu();
        }, false);
    };
    if (document.getElementById("rightMenu")) {
        let xscroll = document.getElementById("rightMenu");
        xscroll.addEventListener("mousewheel", function (e) {
            removeRightMenu();
        }, false);
    }
}
/**
 * @name:  切換模式
 */
function switchDarkMode() {
    removeRightMenu();
    const nowMode = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light'
    if (nowMode === 'light') {
        activateDarkMode();
        saveToLocal.set('theme', 'dark', 2);
        GLOBAL_CONFIG.Snackbar !== undefined && btf.snackbarShow(GLOBAL_CONFIG.Snackbar.day_to_night);
    } else {
        activateLightMode();
        saveToLocal.set('theme', 'light', 2);
        GLOBAL_CONFIG.Snackbar !== undefined && btf.snackbarShow(GLOBAL_CONFIG.Snackbar.night_to_day);
    }
    typeof utterancesTheme === 'function' && utterancesTheme();
    typeof FB === 'object' && window.loadFBComment();
    window.DISQUS && document.getElementById('disqus_thread').children.length && setTimeout(() => window.disqusReset(), 200);
};
/* eslint-disable no-undef */
document.addEventListener('DOMContentLoaded', function () {
    translateInitialization();
    document.addEventListener('pjax:complete', translateInitialization);
});
const translate = GLOBAL_CONFIG.translate;
const snackbarData = GLOBAL_CONFIG.Snackbar;
const defaultEncoding = translate.defaultEncoding; /* 網站默認語言，1: 繁體中文, 2: 簡體中文 */
const translateDelay = translate.translateDelay; /* 延遲時間,若不在前, 要設定延遲翻譯時間, 如100表示100ms,默認為0 */
const msgToTraditionalChinese = translate.msgToTraditionalChinese; /* 此處可以更改為你想要顯示的文字 */
const msgToSimplifiedChinese = translate.msgToSimplifiedChinese; /* 同上，但兩處均不建議更改 */
let currentEncoding = defaultEncoding;
const targetEncodingCookie = 'translate-chn-cht';
let targetEncoding =
    saveToLocal.get(targetEncodingCookie) === undefined
        ? defaultEncoding
        : Number(saveToLocal.get('translate-chn-cht'));
let translateButtonObject
const isSnackbar = GLOBAL_CONFIG.Snackbar !== undefined;
function translateText(txt) {
    if (txt === '' || txt == null) return '';
    if (currentEncoding === 1 && targetEncoding === 2) return Simplized(txt);
    else if (currentEncoding === 2 && targetEncoding === 1) { return Traditionalized(txt) } else return txt;
}
function translateBody(fobj) {
    let objs;
    if (typeof fobj === 'object') objs = fobj.childNodes;
    else objs = document.body.childNodes;
    for (let i = 0; i < objs.length; i++) {
        const obj = objs.item(i);
        if (
            '||BR|HR|'.indexOf('|' + obj.tagName + '|') > 0 ||
            obj === translateButtonObject
        ) { continue }
        if (obj.title !== '' && obj.title != null) { obj.title = translateText(obj.title) };
        if (obj.alt !== '' && obj.alt != null) obj.alt = translateText(obj.alt);
        if (obj.placeholder !== '' && obj.placeholder != null) obj.placeholder = translateText(obj.placeholder);
        if (
            obj.tagName === 'INPUT' &&
            obj.value !== '' &&
            obj.type !== 'text' &&
            obj.type !== 'hidden'
        ) { obj.value = translateText(obj.value) }
        if (obj.nodeType === 3) obj.data = translateText(obj.data);
        else translateBody(obj);
    }
}
function translatePage() {
    if (targetEncoding === 1) {
        currentEncoding = 1;
        targetEncoding = 2;
        saveToLocal.set(targetEncodingCookie, targetEncoding, 2);
        translateBody();
        if (isSnackbar) btf.snackbarShow(snackbarData.cht_to_chs);
    } else if (targetEncoding === 2) {
        currentEncoding = 2;
        targetEncoding = 1;
        saveToLocal.set(targetEncodingCookie, targetEncoding, 2);
        translateBody();
        if (isSnackbar) btf.snackbarShow(snackbarData.chs_to_cht);
    }
}
function JTPYStr() {
    return '万与丑专业丛东丝丢两严丧个丬丰临为丽举么义乌乐乔习乡书买乱争于亏云亘亚产亩亲亵亸亿仅从仑仓仪们价众优伙会伛伞伟传伤伥伦伧伪伫体余佣佥侠侣侥侦侧侨侩侪侬俣俦俨俩俪俭债倾偬偻偾偿傥傧储傩儿兑兖党兰关兴兹养兽冁内冈册写军农冢冯冲决况冻净凄凉凌减凑凛几凤凫凭凯击凼凿刍划刘则刚创删别刬刭刽刿剀剂剐剑剥剧劝办务劢动励劲劳势勋勐勚匀匦匮区医华协单卖卢卤卧卫却卺厂厅历厉压厌厍厕厢厣厦厨厩厮县参叆叇双发变叙叠叶号叹叽吁后吓吕吗吣吨听启吴呒呓呕呖呗员呙呛呜咏咔咙咛咝咤咴咸哌响哑哒哓哔哕哗哙哜哝哟唛唝唠唡唢唣唤唿啧啬啭啮啰啴啸喷喽喾嗫呵嗳嘘嘤嘱噜噼嚣嚯团园囱围囵国图圆圣圹场坂坏块坚坛坜坝坞坟坠垄垅垆垒垦垧垩垫垭垯垱垲垴埘埙埚埝埯堑堕塆墙壮声壳壶壸处备复够头夸夹夺奁奂奋奖奥妆妇妈妩妪妫姗姜娄娅娆娇娈娱娲娴婳婴婵婶媪嫒嫔嫱嬷孙学孪宁宝实宠审宪宫宽宾寝对寻导寿将尔尘尧尴尸尽层屃屉届属屡屦屿岁岂岖岗岘岙岚岛岭岳岽岿峃峄峡峣峤峥峦崂崃崄崭嵘嵚嵛嵝嵴巅巩巯币帅师帏帐帘帜带帧帮帱帻帼幂幞干并广庄庆庐庑库应庙庞废庼廪开异弃张弥弪弯弹强归当录彟彦彻径徕御忆忏忧忾怀态怂怃怄怅怆怜总怼怿恋恳恶恸恹恺恻恼恽悦悫悬悭悯惊惧惨惩惫惬惭惮惯愍愠愤愦愿慑慭憷懑懒懔戆戋戏戗战戬户扎扑扦执扩扪扫扬扰抚抛抟抠抡抢护报担拟拢拣拥拦拧拨择挂挚挛挜挝挞挟挠挡挢挣挤挥挦捞损捡换捣据捻掳掴掷掸掺掼揸揽揿搀搁搂搅携摄摅摆摇摈摊撄撑撵撷撸撺擞攒敌敛数斋斓斗斩断无旧时旷旸昙昼昽显晋晒晓晔晕晖暂暧札术朴机杀杂权条来杨杩杰极构枞枢枣枥枧枨枪枫枭柜柠柽栀栅标栈栉栊栋栌栎栏树栖样栾桊桠桡桢档桤桥桦桧桨桩梦梼梾检棂椁椟椠椤椭楼榄榇榈榉槚槛槟槠横樯樱橥橱橹橼檐檩欢欤欧歼殁殇残殒殓殚殡殴毁毂毕毙毡毵氇气氢氩氲汇汉污汤汹沓沟没沣沤沥沦沧沨沩沪沵泞泪泶泷泸泺泻泼泽泾洁洒洼浃浅浆浇浈浉浊测浍济浏浐浑浒浓浔浕涂涌涛涝涞涟涠涡涢涣涤润涧涨涩淀渊渌渍渎渐渑渔渖渗温游湾湿溃溅溆溇滗滚滞滟滠满滢滤滥滦滨滩滪漤潆潇潋潍潜潴澜濑濒灏灭灯灵灾灿炀炉炖炜炝点炼炽烁烂烃烛烟烦烧烨烩烫烬热焕焖焘煅煳熘爱爷牍牦牵牺犊犟状犷犸犹狈狍狝狞独狭狮狯狰狱狲猃猎猕猡猪猫猬献獭玑玙玚玛玮环现玱玺珉珏珐珑珰珲琎琏琐琼瑶瑷璇璎瓒瓮瓯电画畅畲畴疖疗疟疠疡疬疮疯疱疴痈痉痒痖痨痪痫痴瘅瘆瘗瘘瘪瘫瘾瘿癞癣癫癯皑皱皲盏盐监盖盗盘眍眦眬着睁睐睑瞒瞩矫矶矾矿砀码砖砗砚砜砺砻砾础硁硅硕硖硗硙硚确硷碍碛碜碱碹磙礼祎祢祯祷祸禀禄禅离秃秆种积称秽秾稆税稣稳穑穷窃窍窑窜窝窥窦窭竖竞笃笋笔笕笺笼笾筑筚筛筜筝筹签简箓箦箧箨箩箪箫篑篓篮篱簖籁籴类籼粜粝粤粪粮糁糇紧絷纟纠纡红纣纤纥约级纨纩纪纫纬纭纮纯纰纱纲纳纴纵纶纷纸纹纺纻纼纽纾线绀绁绂练组绅细织终绉绊绋绌绍绎经绐绑绒结绔绕绖绗绘给绚绛络绝绞统绠绡绢绣绤绥绦继绨绩绪绫绬续绮绯绰绱绲绳维绵绶绷绸绹绺绻综绽绾绿缀缁缂缃缄缅缆缇缈缉缊缋缌缍缎缏缐缑缒缓缔缕编缗缘缙缚缛缜缝缞缟缠缡缢缣缤缥缦缧缨缩缪缫缬缭缮缯缰缱缲缳缴缵罂网罗罚罢罴羁羟羡翘翙翚耢耧耸耻聂聋职聍联聩聪肃肠肤肷肾肿胀胁胆胜胧胨胪胫胶脉脍脏脐脑脓脔脚脱脶脸腊腌腘腭腻腼腽腾膑臜舆舣舰舱舻艰艳艹艺节芈芗芜芦苁苇苈苋苌苍苎苏苘苹茎茏茑茔茕茧荆荐荙荚荛荜荞荟荠荡荣荤荥荦荧荨荩荪荫荬荭荮药莅莜莱莲莳莴莶获莸莹莺莼萚萝萤营萦萧萨葱蒇蒉蒋蒌蓝蓟蓠蓣蓥蓦蔷蔹蔺蔼蕲蕴薮藁藓虏虑虚虫虬虮虽虾虿蚀蚁蚂蚕蚝蚬蛊蛎蛏蛮蛰蛱蛲蛳蛴蜕蜗蜡蝇蝈蝉蝎蝼蝾螀螨蟏衅衔补衬衮袄袅袆袜袭袯装裆裈裢裣裤裥褛褴襁襕见观觃规觅视觇览觉觊觋觌觍觎觏觐觑觞触觯詟誉誊讠计订讣认讥讦讧讨让讪讫训议讯记讱讲讳讴讵讶讷许讹论讻讼讽设访诀证诂诃评诅识诇诈诉诊诋诌词诎诏诐译诒诓诔试诖诗诘诙诚诛诜话诞诟诠诡询诣诤该详诧诨诩诪诫诬语诮误诰诱诲诳说诵诶请诸诹诺读诼诽课诿谀谁谂调谄谅谆谇谈谊谋谌谍谎谏谐谑谒谓谔谕谖谗谘谙谚谛谜谝谞谟谠谡谢谣谤谥谦谧谨谩谪谫谬谭谮谯谰谱谲谳谴谵谶谷豮贝贞负贠贡财责贤败账货质贩贪贫贬购贮贯贰贱贲贳贴贵贶贷贸费贺贻贼贽贾贿赀赁赂赃资赅赆赇赈赉赊赋赌赍赎赏赐赑赒赓赔赕赖赗赘赙赚赛赜赝赞赟赠赡赢赣赪赵赶趋趱趸跃跄跖跞践跶跷跸跹跻踊踌踪踬踯蹑蹒蹰蹿躏躜躯车轧轨轩轪轫转轭轮软轰轱轲轳轴轵轶轷轸轹轺轻轼载轾轿辀辁辂较辄辅辆辇辈辉辊辋辌辍辎辏辐辑辒输辔辕辖辗辘辙辚辞辩辫边辽达迁过迈运还这进远违连迟迩迳迹适选逊递逦逻遗遥邓邝邬邮邹邺邻郁郄郏郐郑郓郦郧郸酝酦酱酽酾酿释里鉅鉴銮錾钆钇针钉钊钋钌钍钎钏钐钑钒钓钔钕钖钗钘钙钚钛钝钞钟钠钡钢钣钤钥钦钧钨钩钪钫钬钭钮钯钰钱钲钳钴钵钶钷钸钹钺钻钼钽钾钿铀铁铂铃铄铅铆铈铉铊铋铍铎铏铐铑铒铕铗铘铙铚铛铜铝铞铟铠铡铢铣铤铥铦铧铨铪铫铬铭铮铯铰铱铲铳铴铵银铷铸铹铺铻铼铽链铿销锁锂锃锄锅锆锇锈锉锊锋锌锍锎锏锐锑锒锓锔锕锖锗错锚锜锞锟锠锡锢锣锤锥锦锨锩锫锬锭键锯锰锱锲锳锴锵锶锷锸锹锺锻锼锽锾锿镀镁镂镃镆镇镈镉镊镌镍镎镏镐镑镒镕镖镗镙镚镛镜镝镞镟镠镡镢镣镤镥镦镧镨镩镪镫镬镭镮镯镰镱镲镳镴镶长门闩闪闫闬闭问闯闰闱闲闳间闵闶闷闸闹闺闻闼闽闾闿阀阁阂阃阄阅阆阇阈阉阊阋阌阍阎阏阐阑阒阓阔阕阖阗阘阙阚阛队阳阴阵阶际陆陇陈陉陕陧陨险随隐隶隽难雏雠雳雾霁霉霭靓静靥鞑鞒鞯鞴韦韧韨韩韪韫韬韵页顶顷顸项顺须顼顽顾顿颀颁颂颃预颅领颇颈颉颊颋颌颍颎颏颐频颒颓颔颕颖颗题颙颚颛颜额颞颟颠颡颢颣颤颥颦颧风飏飐飑飒飓飔飕飖飗飘飙飚飞飨餍饤饥饦饧饨饩饪饫饬饭饮饯饰饱饲饳饴饵饶饷饸饹饺饻饼饽饾饿馀馁馂馃馄馅馆馇馈馉馊馋馌馍馎馏馐馑馒馓馔馕马驭驮驯驰驱驲驳驴驵驶驷驸驹驺驻驼驽驾驿骀骁骂骃骄骅骆骇骈骉骊骋验骍骎骏骐骑骒骓骔骕骖骗骘骙骚骛骜骝骞骟骠骡骢骣骤骥骦骧髅髋髌鬓魇魉鱼鱽鱾鱿鲀鲁鲂鲄鲅鲆鲇鲈鲉鲊鲋鲌鲍鲎鲏鲐鲑鲒鲓鲔鲕鲖鲗鲘鲙鲚鲛鲜鲝鲞鲟鲠鲡鲢鲣鲤鲥鲦鲧鲨鲩鲪鲫鲬鲭鲮鲯鲰鲱鲲鲳鲴鲵鲶鲷鲸鲹鲺鲻鲼鲽鲾鲿鳀鳁鳂鳃鳄鳅鳆鳇鳈鳉鳊鳋鳌鳍鳎鳏鳐鳑鳒鳓鳔鳕鳖鳗鳘鳙鳛鳜鳝鳞鳟鳠鳡鳢鳣鸟鸠鸡鸢鸣鸤鸥鸦鸧鸨鸩鸪鸫鸬鸭鸮鸯鸰鸱鸲鸳鸴鸵鸶鸷鸸鸹鸺鸻鸼鸽鸾鸿鹀鹁鹂鹃鹄鹅鹆鹇鹈鹉鹊鹋鹌鹍鹎鹏鹐鹑鹒鹓鹔鹕鹖鹗鹘鹚鹛鹜鹝鹞鹟鹠鹡鹢鹣鹤鹥鹦鹧鹨鹩鹪鹫鹬鹭鹯鹰鹱鹲鹳鹴鹾麦麸黄黉黡黩黪黾'
}
function FTPYStr() {
    return '萬與醜專業叢東絲丟兩嚴喪個爿豐臨為麗舉麼義烏樂喬習鄉書買亂爭於虧雲亙亞產畝親褻嚲億僅從侖倉儀們價眾優夥會傴傘偉傳傷倀倫傖偽佇體餘傭僉俠侶僥偵側僑儈儕儂俁儔儼倆儷儉債傾傯僂僨償儻儐儲儺兒兌兗黨蘭關興茲養獸囅內岡冊寫軍農塚馮衝決況凍淨淒涼淩減湊凜幾鳳鳧憑凱擊氹鑿芻劃劉則剛創刪別剗剄劊劌剴劑剮劍剝劇勸辦務勱動勵勁勞勢勳猛勩勻匭匱區醫華協單賣盧鹵臥衛卻巹廠廳曆厲壓厭厙廁廂厴廈廚廄廝縣參靉靆雙發變敘疊葉號歎嘰籲後嚇呂嗎唚噸聽啟吳嘸囈嘔嚦唄員咼嗆嗚詠哢嚨嚀噝吒噅鹹呱響啞噠嘵嗶噦嘩噲嚌噥喲嘜嗊嘮啢嗩唕喚呼嘖嗇囀齧囉嘽嘯噴嘍嚳囁嗬噯噓嚶囑嚕劈囂謔團園囪圍圇國圖圓聖壙場阪壞塊堅壇壢壩塢墳墜壟壟壚壘墾坰堊墊埡墶壋塏堖塒塤堝墊垵塹墮壪牆壯聲殼壺壼處備複夠頭誇夾奪奩奐奮獎奧妝婦媽嫵嫗媯姍薑婁婭嬈嬌孌娛媧嫻嫿嬰嬋嬸媼嬡嬪嬙嬤孫學孿寧寶實寵審憲宮寬賓寢對尋導壽將爾塵堯尷屍盡層屭屜屆屬屢屨嶼歲豈嶇崗峴嶴嵐島嶺嶽崠巋嶨嶧峽嶢嶠崢巒嶗崍嶮嶄嶸嶔崳嶁脊巔鞏巰幣帥師幃帳簾幟帶幀幫幬幘幗冪襆幹並廣莊慶廬廡庫應廟龐廢廎廩開異棄張彌弳彎彈強歸當錄彠彥徹徑徠禦憶懺憂愾懷態慫憮慪悵愴憐總懟懌戀懇惡慟懨愷惻惱惲悅愨懸慳憫驚懼慘懲憊愜慚憚慣湣慍憤憒願懾憖怵懣懶懍戇戔戲戧戰戩戶紮撲扡執擴捫掃揚擾撫拋摶摳掄搶護報擔擬攏揀擁攔擰撥擇掛摯攣掗撾撻挾撓擋撟掙擠揮撏撈損撿換搗據撚擄摑擲撣摻摜摣攬撳攙擱摟攪攜攝攄擺搖擯攤攖撐攆擷擼攛擻攢敵斂數齋斕鬥斬斷無舊時曠暘曇晝曨顯晉曬曉曄暈暉暫曖劄術樸機殺雜權條來楊榪傑極構樅樞棗櫪梘棖槍楓梟櫃檸檉梔柵標棧櫛櫳棟櫨櫟欄樹棲樣欒棬椏橈楨檔榿橋樺檜槳樁夢檮棶檢欞槨櫝槧欏橢樓欖櫬櫚櫸檟檻檳櫧橫檣櫻櫫櫥櫓櫞簷檁歡歟歐殲歿殤殘殞殮殫殯毆毀轂畢斃氈毿氌氣氫氬氳彙漢汙湯洶遝溝沒灃漚瀝淪滄渢溈滬濔濘淚澩瀧瀘濼瀉潑澤涇潔灑窪浹淺漿澆湞溮濁測澮濟瀏滻渾滸濃潯濜塗湧濤澇淶漣潿渦溳渙滌潤澗漲澀澱淵淥漬瀆漸澠漁瀋滲溫遊灣濕潰濺漵漊潷滾滯灩灄滿瀅濾濫灤濱灘澦濫瀠瀟瀲濰潛瀦瀾瀨瀕灝滅燈靈災燦煬爐燉煒熗點煉熾爍爛烴燭煙煩燒燁燴燙燼熱煥燜燾煆糊溜愛爺牘犛牽犧犢強狀獷獁猶狽麅獮獰獨狹獅獪猙獄猻獫獵獼玀豬貓蝟獻獺璣璵瑒瑪瑋環現瑲璽瑉玨琺瓏璫琿璡璉瑣瓊瑤璦璿瓔瓚甕甌電畫暢佘疇癤療瘧癘瘍鬁瘡瘋皰屙癰痙癢瘂癆瘓癇癡癉瘮瘞瘺癟癱癮癭癩癬癲臒皚皺皸盞鹽監蓋盜盤瞘眥矓著睜睞瞼瞞矚矯磯礬礦碭碼磚硨硯碸礪礱礫礎硜矽碩硤磽磑礄確鹼礙磧磣堿镟滾禮禕禰禎禱禍稟祿禪離禿稈種積稱穢穠穭稅穌穩穡窮竊竅窯竄窩窺竇窶豎競篤筍筆筧箋籠籩築篳篩簹箏籌簽簡籙簀篋籜籮簞簫簣簍籃籬籪籟糴類秈糶糲粵糞糧糝餱緊縶糸糾紆紅紂纖紇約級紈纊紀紉緯紜紘純紕紗綱納紝縱綸紛紙紋紡紵紖紐紓線紺絏紱練組紳細織終縐絆紼絀紹繹經紿綁絨結絝繞絰絎繪給絢絳絡絕絞統綆綃絹繡綌綏絛繼綈績緒綾緓續綺緋綽緔緄繩維綿綬繃綢綯綹綣綜綻綰綠綴緇緙緗緘緬纜緹緲緝縕繢緦綞緞緶線緱縋緩締縷編緡緣縉縛縟縝縫縗縞纏縭縊縑繽縹縵縲纓縮繆繅纈繚繕繒韁繾繰繯繳纘罌網羅罰罷羆羈羥羨翹翽翬耮耬聳恥聶聾職聹聯聵聰肅腸膚膁腎腫脹脅膽勝朧腖臚脛膠脈膾髒臍腦膿臠腳脫腡臉臘醃膕齶膩靦膃騰臏臢輿艤艦艙艫艱豔艸藝節羋薌蕪蘆蓯葦藶莧萇蒼苧蘇檾蘋莖蘢蔦塋煢繭荊薦薘莢蕘蓽蕎薈薺蕩榮葷滎犖熒蕁藎蓀蔭蕒葒葤藥蒞蓧萊蓮蒔萵薟獲蕕瑩鶯蓴蘀蘿螢營縈蕭薩蔥蕆蕢蔣蔞藍薊蘺蕷鎣驀薔蘞藺藹蘄蘊藪槁蘚虜慮虛蟲虯蟣雖蝦蠆蝕蟻螞蠶蠔蜆蠱蠣蟶蠻蟄蛺蟯螄蠐蛻蝸蠟蠅蟈蟬蠍螻蠑螿蟎蠨釁銜補襯袞襖嫋褘襪襲襏裝襠褌褳襝褲襇褸襤繈襴見觀覎規覓視覘覽覺覬覡覿覥覦覯覲覷觴觸觶讋譽謄訁計訂訃認譏訐訌討讓訕訖訓議訊記訒講諱謳詎訝訥許訛論訩訟諷設訪訣證詁訶評詛識詗詐訴診詆謅詞詘詔詖譯詒誆誄試詿詩詰詼誠誅詵話誕詬詮詭詢詣諍該詳詫諢詡譸誡誣語誚誤誥誘誨誑說誦誒請諸諏諾讀諑誹課諉諛誰諗調諂諒諄誶談誼謀諶諜謊諫諧謔謁謂諤諭諼讒諮諳諺諦謎諞諝謨讜謖謝謠謗諡謙謐謹謾謫譾謬譚譖譙讕譜譎讞譴譫讖穀豶貝貞負貟貢財責賢敗賬貨質販貪貧貶購貯貫貳賤賁貰貼貴貺貸貿費賀貽賊贄賈賄貲賃賂贓資賅贐賕賑賚賒賦賭齎贖賞賜贔賙賡賠賧賴賵贅賻賺賽賾贗讚贇贈贍贏贛赬趙趕趨趲躉躍蹌蹠躒踐躂蹺蹕躚躋踴躊蹤躓躑躡蹣躕躥躪躦軀車軋軌軒軑軔轉軛輪軟轟軲軻轤軸軹軼軤軫轢軺輕軾載輊轎輈輇輅較輒輔輛輦輩輝輥輞輬輟輜輳輻輯轀輸轡轅轄輾轆轍轔辭辯辮邊遼達遷過邁運還這進遠違連遲邇逕跡適選遜遞邐邏遺遙鄧鄺鄔郵鄒鄴鄰鬱郤郟鄶鄭鄆酈鄖鄲醞醱醬釅釃釀釋裏钜鑒鑾鏨釓釔針釘釗釙釕釷釺釧釤鈒釩釣鍆釹鍚釵鈃鈣鈈鈦鈍鈔鍾鈉鋇鋼鈑鈐鑰欽鈞鎢鉤鈧鈁鈥鈄鈕鈀鈺錢鉦鉗鈷缽鈳鉕鈽鈸鉞鑽鉬鉭鉀鈿鈾鐵鉑鈴鑠鉛鉚鈰鉉鉈鉍鈹鐸鉶銬銠鉺銪鋏鋣鐃銍鐺銅鋁銱銦鎧鍘銖銑鋌銩銛鏵銓鉿銚鉻銘錚銫鉸銥鏟銃鐋銨銀銣鑄鐒鋪鋙錸鋱鏈鏗銷鎖鋰鋥鋤鍋鋯鋨鏽銼鋝鋒鋅鋶鐦鐧銳銻鋃鋟鋦錒錆鍺錯錨錡錁錕錩錫錮鑼錘錐錦鍁錈錇錟錠鍵鋸錳錙鍥鍈鍇鏘鍶鍔鍤鍬鍾鍛鎪鍠鍰鎄鍍鎂鏤鎡鏌鎮鎛鎘鑷鐫鎳鎿鎦鎬鎊鎰鎔鏢鏜鏍鏰鏞鏡鏑鏃鏇鏐鐔钁鐐鏷鑥鐓鑭鐠鑹鏹鐙鑊鐳鐶鐲鐮鐿鑔鑣鑞鑲長門閂閃閆閈閉問闖閏闈閑閎間閔閌悶閘鬧閨聞闥閩閭闓閥閣閡閫鬮閱閬闍閾閹閶鬩閿閽閻閼闡闌闃闠闊闋闔闐闒闕闞闤隊陽陰陣階際陸隴陳陘陝隉隕險隨隱隸雋難雛讎靂霧霽黴靄靚靜靨韃鞽韉韝韋韌韍韓韙韞韜韻頁頂頃頇項順須頊頑顧頓頎頒頌頏預顱領頗頸頡頰頲頜潁熲頦頤頻頮頹頷頴穎顆題顒顎顓顏額顳顢顛顙顥纇顫顬顰顴風颺颭颮颯颶颸颼颻飀飄飆飆飛饗饜飣饑飥餳飩餼飪飫飭飯飲餞飾飽飼飿飴餌饒餉餄餎餃餏餅餑餖餓餘餒餕餜餛餡館餷饋餶餿饞饁饃餺餾饈饉饅饊饌饢馬馭馱馴馳驅馹駁驢駔駛駟駙駒騶駐駝駑駕驛駘驍罵駰驕驊駱駭駢驫驪騁驗騂駸駿騏騎騍騅騌驌驂騙騭騤騷騖驁騮騫騸驃騾驄驏驟驥驦驤髏髖髕鬢魘魎魚魛魢魷魨魯魴魺鮁鮃鯰鱸鮋鮓鮒鮊鮑鱟鮍鮐鮭鮚鮳鮪鮞鮦鰂鮜鱠鱭鮫鮮鮺鯗鱘鯁鱺鰱鰹鯉鰣鰷鯀鯊鯇鮶鯽鯒鯖鯪鯕鯫鯡鯤鯧鯝鯢鯰鯛鯨鯵鯴鯔鱝鰈鰏鱨鯷鰮鰃鰓鱷鰍鰒鰉鰁鱂鯿鰠鼇鰭鰨鰥鰩鰟鰜鰳鰾鱈鱉鰻鰵鱅鰼鱖鱔鱗鱒鱯鱤鱧鱣鳥鳩雞鳶鳴鳲鷗鴉鶬鴇鴆鴣鶇鸕鴨鴞鴦鴒鴟鴝鴛鴬鴕鷥鷙鴯鴰鵂鴴鵃鴿鸞鴻鵐鵓鸝鵑鵠鵝鵒鷳鵜鵡鵲鶓鵪鶤鵯鵬鵮鶉鶊鵷鷫鶘鶡鶚鶻鶿鶥鶩鷊鷂鶲鶹鶺鷁鶼鶴鷖鸚鷓鷚鷯鷦鷲鷸鷺鸇鷹鸌鸏鸛鸘鹺麥麩黃黌黶黷黲黽'
}
function Traditionalized(cc) {
    let str = '';
    const ss = JTPYStr();
    const tt = FTPYStr();
    for (let i = 0; i < cc.length; i++) {
        if (cc.charCodeAt(i) > 10000 && ss.indexOf(cc.charAt(i)) !== -1) { str += tt.charAt(ss.indexOf(cc.charAt(i))) } else str += cc.charAt(i)
    };
    return str;
}
function Simplized(cc) {
    let str = '';
    const ss = JTPYStr();
    const tt = FTPYStr();
    for (let i = 0; i < cc.length; i++) {
        if (cc.charCodeAt(i) > 10000 && tt.indexOf(cc.charAt(i)) !== -1) { str += ss.charAt(tt.indexOf(cc.charAt(i))) } else str += cc.charAt(i)
    }
    return str;
}
function translateInitialization() {
    translateButtonObject = document.getElementById('menu-translate');
    if (translateButtonObject) {
        if (currentEncoding !== targetEncoding) {
            setTimeout(translateBody, translateDelay);
        }
        translateButtonObject.addEventListener('click', translatePage, false);
    }
}
$('#menu-backward').on('click', function () { window.history.back(); });
$('#menu-forward').on('click', function () { window.history.forward(); });
$('#menu-refresh').on('click', function () { window.location.reload(); });
$('#menu-darkmode').on('click', function () { switchDarkMode() });
$('#menu-home').on('click', function () { window.location.href = window.location.origin; });
/* 简体繁体切换 */
$('#menu-translate').on('click', function () {
    removeRightMenu();
    translateInitialization();
});
$(".menu-link").on("click", function () {
    removeRightMenu()
});
$("#rightmenu-mask").on("click", function () { removeRightMenu() });
$("#rightmenu-mask").contextmenu(function () {
    removeRightMenu();
    return false;
});

```

在BlogRoot/node_modules/hexo-theme-butterfly/source/css文件夹下新建一个rightMenu.css，将以下代码复制到文件中。

```css
#rightMenu {
    display: none;
    position: fixed;
    padding: 0 .25rem;
    width: 9rem;
    height: fit-content;
    top: 10%;
    left: 10%;
    background-color: rgba(238, 255, 255, .85);
    -webkit-backdrop-filter: blur(20px);
    backdrop-filter: blur(20px);
    color: #363636;
    border-radius: 12px;
    z-index: 99994;
    border: #e3e8f7;
    user-select: none;
    box-shadow: rgba(0, 0, 0, .05);
}

#rightMenu a {
    color: #363636;
}

#rightMenu .rightMenu-group {
    padding: .35rem .3rem;
    transition: .3s
}

#rightMenu .rightMenu-line {
    border-top: 1px dashed #4259ef23
}

#rightMenu .rightMenu-group.rightMenu-small {
    display: flex;
    justify-content: space-between
}

#rightMenu .rightMenu-group .rightMenu-item {
    border-radius: 8px;
    transition: .3s;
    cursor: pointer
}

#rightMenu .rightMenu-line .rightMenu-item {
    margin: .25rem 0;
    padding: .25rem 0
}

#rightMenu .rightMenu-group.rightMenu-line .rightMenu-item {
    display: flex
}

#rightMenu .rightMenu-group .rightMenu-item:hover {
    background-color: #6f42c1;
    color: #fff;
}

#rightMenu .rightMenu-group .rightMenu-item:active {
    transform: scale(.97)
}

#rightMenu .rightMenu-group .rightMenu-item i {
    display: inline-block;
    text-align: center;
    line-height: 1.5rem;
    width: 1.5rem;
    padding: 0 .25rem
}

#rightMenu .rightMenu-line .rightMenu-item i {
    margin: 0 .25rem
}

#rightMenu .rightMenu-group .rightMenu-item span {
    line-height: 1.5rem
}

.rightMenu-small .rightMenu-item {
    width: 30px;
    height: 30px;
    line-height: 30px
}

#rightmenu-mask {
    position: fixed;
    width: 100vw;
    height: 100vh;
    background: 0 0;
    top: 0;
    left: 0;
    display: none;
    z-index: 101;
    margin: 0 !important;
    z-index: 99993
}

```

在主题配置文件_config.butterfly.yml中引入Jquery、rightMenu.js和rightMenu.css。

```yaml
inject:
  head:
    - <link rel="stylesheet" href="/css/rightMenu.css">
  bottom:
    - <script defer src="https://npm.elemecdn.com/jquery@latest/dist/jquery.min.js"></script>
    - <script defer data-pjax src="/js/rightMenu.js"></script>

```

> 需要注意的是，如果点击繁简切换，切换模式，出现了错误，请检查下主题的这两个功能是否开启。在主题配置文件_config.butterfly.yml中搜索translate和darkmode，将enable设置为true，在重新编译运行。

### 扩展

这个章节将讲述如何去扩展右键的功能。如果想在自定义右键上新增一个打印页面的功能。该如何去实现呢？

增加DOM。（为了描述的更清晰，将沿用上面提到过的代码，+表示在此基础上新增的代码。）
在BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/right-menu/index.pug中新加如下代码：

```html
#rightMenu
    .rightMenu-group.rightMenu-small
        .rightMenu-item#menu-backward
            i.fa-solid.fa-arrow-left
        .rightMenu-item#menu-forward
            i.fa-solid.fa-arrow-right
        .rightMenu-item#menu-refresh
            i.fa-solid.fa-arrow-rotate-right
        .rightMenu-item#menu-home
            i.fa-solid.fa-house
    .rightMenu-group.rightMenu-line.rightMenuOther
        a.rightMenu-item.menu-link(href='/archives/')
            i.fa-solid.fa-archive
            span='文章归档'
        a.rightMenu-item.menu-link(href='/categories/')
            i.fa-solid.fa-folder-open
            span='文章分类'
        a.rightMenu-item.menu-link(href='/tags/')
            i.fa-solid.fa-tags
            span='文章标签'
    .rightMenu-group.rightMenu-line.rightMenuNormal
        a.rightMenu-item.menu-link#menu-radompage(href='/random/index.html')
            i.fa-solid.fa-shoe-prints
            span='随便逛逛'
        .rightMenu-item#menu-translate
            i.fa-solid.fa-earth-asia
            span='繁简切换'
        .rightMenu-item#menu-darkmode
            i.fa-solid.fa-moon
            span='切换模式'
+       .rightMenu-item#menu-print
+           i.fa-solid.fa-print.fa-fw
+           span='打印页面'
#rightmenu-mask
```

有兴趣的同学可以按下F12 打开控制台，找到Elements，并找到#rightMenu的盒子，你会发现新增的pug语法最终会被编译成：

```html
<div class="rightMenu-item" id="menu-print">
    <i class="fa-solid fa-print fa-fw"></i>
    <span>打印頁面</span>
</div>

```

记住这个id为menu-print的属性，下面将会用到。

在BlogRoot/node_modules/hexo-theme-butterfly/source/js/rightMenu.js中写入实现方法。

```js
$('#menu-translate').on('click', function () {
    removeRightMenu();
    translateInitialization();
});
$(".menu-link").on("click", function () {
    removeRightMenu()
});
+   $("#menu-print").on("click", function () {
+       removeRightMenu();
+       window.print();
+   });
$("#rightmenu-mask").on("click", function () { removeRightMenu() });
$("#rightmenu-mask").contextmenu(function () {
    removeRightMenu();
    return false;
});

```

不难发现，新增的代码实际上是在id为menu-print的盒子上绑了一个点击事件，后面的方法则是触发点击事件后要执行的过程。

### 推荐阅读

参考方向	教程原贴
ZHHEO	[Butterfly 魔改：自定义右键菜单](https://blog.zhheo.com/p/5e931b65.html)
LYX	[博客自定义右键菜单升级版](https://yisous.xyz/posts/11eb4aac/)



## 侧边滚动栏设置成猫咪

> 没什么要求，但必须引入 Jquery。

步骤

制作一个盛放内容的盒子，在BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/head.pug最后一行加入如下代码：

```pug
#myscoll
```

其实随便放在哪里都行，像我放在了BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/right-menu/index.pug的末尾（如果用了自定义右键功能的话，可以放在这里）。

在BlogRoot/node_modules/hexo-theme-butterfly/source/js文件夹下新建一个cat.js，将以下代码复制到文件中。

```js
if (document.body.clientWidth > 992) {
    function getBasicInfo() {
        /* 窗口高度 */
        var ViewH = $(window).height();
        /* document高度 */
        var DocH = $("body")[0].scrollHeight;
        /* 滚动的高度 */
        var ScrollTop = $(window).scrollTop();
        /* 可滚动的高度 */
        var S_V = DocH - ViewH;
        var Band_H = ScrollTop / (DocH - ViewH) * 100;
        return {
            ViewH: ViewH,
            DocH: DocH,
            ScrollTop: ScrollTop,
            Band_H: Band_H,
            S_V: S_V
        }
    };
    function show(basicInfo) {
        if (basicInfo.ScrollTop > 0.001) {
            $(".neko").css('display', 'block');
        } else {
            $(".neko").css('display', 'none');
        }
    }
    (function ($) {
        $.fn.nekoScroll = function (option) {
            var defaultSetting = {
                top: '0',
                scroWidth: 6 + 'px',
                z_index: 9999,
                zoom: 0.9,
                borderRadius: 5 + 'px',
                right: 60 + 'px',
                nekoImg: "https://bu.dusays.com/2022/07/20/62d812db74be9.png",
                hoverMsg: "喵喵喵~",
                color: "#6f42c1",
                during: 500,
                blog_body: "body",
            };
            var setting = $.extend(defaultSetting, option);
            var getThis = this.prop("className") !== "" ? "." + this.prop("className") : this.prop("id") !== "" ? "#" +
                this.prop("id") : this.prop("nodeName");
            if ($(".neko").length == 0) {
                this.after("<div class=\"neko\" id=" + setting.nekoname + " data-msg=\"" + setting.hoverMsg + "\"></div>");
            }
            let basicInfo = getBasicInfo();
            $(getThis)
                .css({
                    'position': 'fixed',
                    'width': setting.scroWidth,
                    'top': setting.top,
                    'height': basicInfo.Band_H * setting.zoom * basicInfo.ViewH * 0.01 + 'px',
                    'z-index': setting.z_index,
                    'background-color': setting.bgcolor,
                    "border-radius": setting.borderRadius,
                    'right': setting.right,
                    'background-image': 'url(' + setting.scImg + ')',
                    'background-image': '-webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.1) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.1) 75%, transparent 75%, transparent)', 'border-radius': '2em',
                    'background-size': 'contain'
                });
            $("#" + setting.nekoname)
                .css({
                    'position': 'fixed',
                    'top': basicInfo.Band_H * setting.zoom * basicInfo.ViewH * 0.01 - 50 + 'px',
                    'z-index': setting.z_index * 10,
                    'right': setting.right,
                    'background-image': 'url(' + setting.nekoImg + ')',
                });
            show(getBasicInfo());
            $(window)
                .scroll(function () {
                    let basicInfo = getBasicInfo();
                    show(basicInfo);
                    $(getThis)
                        .css({
                            'position': 'fixed',
                            'width': setting.scroWidth,
                            'top': setting.top,
                            'height': basicInfo.Band_H * setting.zoom * basicInfo.ViewH * 0.01 + 'px',
                            'z-index': setting.z_index,
                            'background-color': setting.bgcolor,
                            "border-radius": setting.borderRadius,
                            'right': setting.right,
                            'background-image': 'url(' + setting.scImg + ')',
                            'background-image': '-webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.1) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.1) 75%, transparent 75%, transparent)', 'border-radius': '2em',
                            'background-size': 'contain'
                        });
                    $("#" + setting.nekoname)
                        .css({
                            'position': 'fixed',
                            'top': basicInfo.Band_H * setting.zoom * basicInfo.ViewH * 0.01 - 50 + 'px',
                            'z-index': setting.z_index * 10,
                            'right': setting.right,
                            'background-image': 'url(' + setting.nekoImg + ')',
                        });
                    if (basicInfo.ScrollTop == basicInfo.S_V) {
                        $("#" + setting.nekoname)
                            .addClass("showMsg")
                    } else {
                        $("#" + setting.nekoname)
                            .removeClass("showMsg");
                        $("#" + setting.nekoname)
                            .attr("data-msg", setting.hoverMsg);
                    }
                });
            this.click(function (e) {
                btf.scrollToDest(0, 500)
            });
            $("#" + setting.nekoname)
                .click(function () {
                    btf.scrollToDest(0, 500)
                });
            return this;
        }
    })(jQuery);

    $(document).ready(function () {
        //部分自定义
        $("#myscoll").nekoScroll({
            bgcolor: 'rgb(0 0 0 / .5)', //背景颜色，没有绳子背景图片时有效
            borderRadius: '2em',
            zoom: 0.9
        }
        );
        //自定义（去掉以下注释，并注释掉其他的查看效果）
        /*
        $("#myscoll").nekoScroll({
            nekoname:'neko1', //nekoname，相当于id
            nekoImg:'img/猫咪.png', //neko的背景图片
            scImg:"img/绳1.png", //绳子的背景图片
            bgcolor:'#1e90ff', //背景颜色，没有绳子背景图片时有效
            zoom:0.9, //绳子长度的缩放值
            hoverMsg:'你好~喵', //鼠标浮动到neko上方的对话框信息
            right:'100px', //距离页面右边的距离
            fontFamily:'楷体', //对话框字体
            fontSize:'14px', //对话框字体的大小
            color:'#1e90ff', //对话框字体颜色
            scroWidth:'8px', //绳子的宽度
            z_index:100, //不用解释了吧
            during:1200, //从顶部到底部滑动的时长
        });
        */
    })
}

```

在BlogRoot/node_modules/hexo-theme-butterfly/source/css文件夹下新建一个cat.css，将以下代码复制到文件中。当然你也可以选择不新建 css 文件，复制代码到custom.css也行，总之有地方引入就行。（我是所有的自定义内容，尽量放在一个文件夹下：source/custom/...）

```css

body::-webkit-scrollbar {
    width: 0;
}

.neko {
    width: 64px;
    height: 64px;
    background-image: url("https://bu.dusays.com/2022/07/20/62d812db74be9.png");
    position: absolute;
    right: 32px;
    background-repeat: no-repeat;
    background-size: contain;
    transform: translateX(50%);
    cursor: pointer;
    font-family: tzy;
    font-weight: 600;
    font-size: 16px;
    color: #6f42c1;
    display: none;
}

.neko::after {
    display: none;
    width: 100px;
    height: 100px;
    background-image: url("https://bu.dusays.com/2022/07/20/62d812d95e6f5.png");
    background-size: contain;
    z-index: 9999;
    position: absolute;
    right: 50%;
    text-align: center;
    line-height: 100px;
    top: -115%;

}

.neko.showMsg::after {
    content: attr(data-msg);
    display: block;
    overflow: hidden;
    text-overflow: ellipsis;
}

.neko:hover::after {
    content: attr(data-msg);
    display: block;
    overflow: hidden;
    text-overflow: ellipsis;
}

.neko.fontColor::after {
    color: #333;
}

/**
 * @description: 滚动条样式  跟猫二选一
 */
@media screen and (max-width:992px) {
    ::-webkit-scrollbar {
        width: 8px !important;
        height: 8px !important
    }

    ::-webkit-scrollbar-track {
        border-radius: 2em;
    }

    ::-webkit-scrollbar-thumb {
        background-color: rgb(255 255 255 / .3);
        background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.1) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.1) 75%, transparent 75%, transparent);
        border-radius: 2em
    }

    ::-webkit-scrollbar-corner {
        background-color: transparent
    }
}

```

在主题配置文件_config.butterfly.yml中引入cat.js和cat.css。

```yaml
inject:
  head:
    - <link rel="stylesheet" href="/css/cat.css">
  bottom:
    - <script defer src="https://npm.elemecdn.com/jquery@latest/dist/jquery.min.js"></script>
    - <script defer data-pjax src="/js/cat.js"></script>

```

最后重新编译运行即可看见效果。

如果你大致看懂了`cat.js`，可以针对自己站点去做出一些设置，例如滚动到某个位置，加一些提示语等等。

## 首页加载添加移入动画

https://tzy1997.com/articles/hexo1615/

在BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/header文件夹下新建一个plane.pug文件

具体位置如下图：

![image-20230207084412291](image-20230207084412291.png)

将以下代码复制到文件中。

```pug
#drone
  .container
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .trigger
    .monitor
      .opening
        .camera.o-x
          .camera.o-y
            .camera.o-z
              .awing
                .stars
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                  .star
                .fly.o-x
                  .fly.o-y
                    .fly.o-z
                      .free_bounce
                        .free_rotate
                          .body
                            .cockpit
                              .under
                              .back
                              .left
                              .right
                              .edge_left
                              .edge_right
                              .boosts
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                                .boost
                            .wing_left
                              .under
                              .back
                              .left
                              .right
                            .wing_right
                              .under
                              .back
                              .left
                              .right  

```

在BlogRoot/node_modules/hexo-theme-butterfly/layout/includes/header/index.pug中引入上一步中创建的plane.pug文件。

```pug
!=partial('includes/header/plane', {}, {cache: true})
```

跟#site-info、#scroll-down同级。
具体位置如下图：

![image-20230207084639400](image-20230207084639400.png)

在主题配置文件_config.butterfly.yml中引入plane.css。

```yaml
inject:
  head:
    - <link rel="stylesheet" href="https://npm.elemecdn.com/ethan4116-blog/lib/css/plane_v2.css">
```

最后重新编译运行即可看见效果。

**BUG 反馈**

关于下方有横向滚动条的 bug , 如下图所示

![image-20230207084739659](image-20230207084739659.png)

为了及时解决这个 bug , 你可以在自定义的 css 中加入下面这个样式即可。

```css
#drone .container {
    overflow: hidden;
}
```



生成的dom结构太冗余了，不加了



























