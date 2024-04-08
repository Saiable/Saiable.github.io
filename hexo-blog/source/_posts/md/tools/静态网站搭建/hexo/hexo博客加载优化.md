---
title: 'hexo博客加载优化'
date: 2023/02/08 07:15:24
cover: false
typora-root-url: hexo博客加载优化
---

# 概览

|    资源类型     | 文件大小 |                         情景                         | 加载时间 |                           处理方式                           |          前置准备          |
| :-------------: | -------- | :--------------------------------------------------: | -------- | :----------------------------------------------------------: | :------------------------: |
| `woff2`字体文件 | 5M+      |   一：放在`source`目录下，直接访问托管的github网站   | 20s+     | 可以托管在国内的gitee上，但它会莫名封掉不让访问。并且`hexo`有部分应用依赖`github`。不考虑托管在国内 |             无             |
|                 |          | 二：文件挂到七牛云存储上，https://s.qiniu.com/QVNJNf |          |                             cdn                              | 1.备案域名<br />2.域名证书 |
|      图片       | 大图     |                例如：toc_img和底部图                 |          | 图片格式转为webp，工具：[XnConvert](http://www.downza.cn/soft/212929.html) |                            |
|                 | 小图     |                   例如自定义鼠标图                   |          | 资源文件直接放在github托管的网站上，在source目录下<br />css中的可以通过相对路径引用，配置文件可以直接通过域名访问 |                            |
|                 |          |                                                      |          |                                                              |                            |

# 字体图标

默认走的是jsdelivr

![image-20230208204129705](image-20230208204129705.png)



# 图片



## 小图

小图还是别放免费图床了，完全属于负优化了，当然如果找到了serverResponse比较快的图床，还是可以的（如果付费图床自己做了cdn，还是放图床上吧）

![image-20230208142736554](image-20230208142736554.png)

放图床上

![image-20230208144250418](image-20230208144250418.png)

放github上

![image-20230208144112258](image-20230208144112258.png)

放七牛云上

![image-20230208144503840](image-20230208144503840.png)

对比可以看到，虽然七牛云的contentDownload最快，但由于是外链，有个200多ms的Queueing队列调度时间（这个是本站程序决定的），并且七牛云等待serverResponse的时间并不比github快

资源跨域图

![image-20230208145129217](image-20230208145129217.png)



如果是文章里的外链图片，压缩成webp放在https://7bu.top/图床上（支持webp格式）

这个是付费的图床，做了cdn加速的，也不贵

图片还是不放在七牛云上了，就放个字体文件就行

## 文章图片懒加载

[Hexo 图片懒加载 | 竹山一叶 (zsyyblog.com)](https://zsyyblog.com/a9a0bd1c.html)

![image-20230211135231325](image-20230211135231325.png)

# CSS

处理自定义CSS文件



先在`_config.yml`忽略掉一些文件，避免发布纳入

```yaml
exclude:
  - "custom/node_modules/**/*"
  - "custom/package.json"
  - "custom/bak/**/*"
```

[配置 | Hexo](https://hexo.io/zh-cn/docs/configuration)

样例

```yaml
# 处理或不处理目录或文件
include:
  - ".nojekyll"
  # 处理 'source/css/_typing.css'
  - "css/_typing.css"
  # 处理 'source/_css/' 中的任何文件，但不包括子目录及其其中的文件。
  - "_css/*"
  # 处理 'source/_css/' 中的任何文件和子目录下的任何文件
  - "_css/**/*"

exclude:
  # 不处理 'source/js/test.js'
  - "js/test.js"
  # 不处理 'source/js/' 中的文件、但包括子目录下的所有目录和文件
  - "js/*"
  # 不处理 'source/js/' 中的文件和子目录下的任何文件
  - "js/**/*"
  # 不处理 'source/js/' 目录下的所有文件名以 'test' 开头的文件，但包括其它文件和子目录下的单文件
  - "js/test*"
  # 不处理 'source/js/' 及其子目录中任何以 'test' 开头的文件
  - "js/**/test*"
  # 不要用 exclude 来忽略 'source/_posts/' 中的文件。你应该使用 'skip_render'，或者在要忽略的文件的文件名之前加一个下划线 '_'
  # 在这里配置一个 - "_posts/hello-world.md" 是没有用的。

ignore:
  # 忽略任何一个名叫 'foo' 的文件夹
  - "**/foo"
  # 只忽略 'themes/' 下的 'foo' 文件夹
  - "**/themes/*/foo"
  # 对 'themes/' 目录下的每个文件夹中忽略名叫 'foo' 的子文件夹
  - "**/themes/**/foo"
```

在`source/custom`使用webpack压缩文件

```bash
npm i webpack@4.41.6 webpack-cli@3.3.11 -D
npm i css-loader@3.4.2 style-loader@1.1.3 -D
npm i mini-css-extract-plugin@0.9.0 -D
npm i postcss-loader@3.0.0 postcss-preset-env@6.7.0 -D
npm i optimize-css-assets-webpack-plugin@5.0.3 -D
```

对应的`webpack.config.js`

```js
const {resolve} = require('path')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const OptimizeCssAssetsWebpackPlugin = require('optimize-css-assets-webpack-plugin')

module.exports = {
    entry: './js/index.js',
    output: {
        filename: 'js/built.js',
        path: resolve(__dirname, 'build')
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader'
                ]
            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: '../css/custom.min.css'
        }),
        // 压缩css
        new OptimizeCssAssetsWebpackPlugin()
    ],
    mode: 'development'
}
```



`js/index.js`中引入原来写在配置文件中的css

```js
import '../css/font.css';
import '../css/mouse.css';
import '../css/card_wx.css';
import '../css/scrollbar.css';
import '../css/windmill.css';
import '../css/optimize.css';
import '../css/video.css';
import '../css/universe.css';
import '../css/rightMenu.css';
import '../css/cat.css';

```

注意css中不要写相对路径，直接写`source`下一级的路径`/custom/css/...`即可，否则打包会不认识`webp`格式

运行`npx webpack`打包，在`css`目录中生成了`custom.min.css`

在配置文件中引入这一个css文件即可

注意：我们在写样式类名和id名时，尽量保持唯一不要重复
