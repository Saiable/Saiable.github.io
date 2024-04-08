---
title: 'vscode插件'
date: 2022/7/8 07:15:24
cover: false
---



[vscode配置使用教程 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/113222681)

# 本地安装

https://zhuanlan.zhihu.com/p/402278573

https://marketplace.visualstudio.com/

以下方式适用于所有vscode插件的离线安装，在我们的开发环境下都比较管用。

打开浏览器，进入网站：https://marketplace.visualstudio.com/

搜索所需要的插件，如现在我们要用的“http://Draw.io Integration”

进入插件介绍的页面后，找到右下角的“Download Extension”，下载插件，vsix格式的文件，比如这次我们想要的画图插件名称为hediet.vscode-drawio-1.0.3.vsix，放到某个你指定的文件夹。

最后cmd打开命令行，cd到上面指定的文件夹，输入

```bash
code --install-extension hediet.vscode-drawio-1.0.3.vsix
```

# 基本设置

打开`setting.json`

1.ctrl +shift +p
2.输入setting
3.找到这一项

# Open in External App

下载插件Open in External App

右击文件后会多一个Open in External App选项，这个插件的作用是使用默认系统应用来打开相应文件

设置settings.json

设置[vscode](https://so.csdn.net/so/search?q=vscode&spm=1001.2101.3001.7020)的settings.json，这样右击选择Open in External App后就会直接用typora文件打开md文件

```json
"openInExternalApp.openMapper": [
    {
      // 文件后缀名
      "extensionName": "md",
      "apps": [
        {
          "title": "typora",
          "isElectronApp": true,
          // exe文件路径,需要换成自己的
          "openCommand": "D:\\manager\\Typora\\Typora.exe"
        }
      ]
    }
  ],

```



备注：装了配置后，没有生效



# Open in Typora

需要新增一下Typora的环境变量即可，重启vscode生效

# vscode-pdf

预览pdf



# 快捷键

# 设置图片保存位置
https://www.cnblogs.com/qinweijie/p/17656330.html
```bash
**/*.md
${documentBaseName}/${fileName}
```

![Alt text](vscode%E6%8F%92%E4%BB%B6/image-2.png)