---
title: 'crx问题记录'
date: 2022-7-19 07:28:42
cover: false
---



记录crx开发中，遇到的问题

# unsafe-eval

使用的vue开发的页面，用到了eval方法，在插件中不通过

需要在manifest.json中配置安全策略

```json
,"content_security_policy": "script-src 'self' 'unsafe-eval'; object-src 'self'"
```

参考：[(3条消息) CHROME扩展笔记之拒绝unsafe-eval求值_slongzhang_的博客-CSDN博客](https://blog.csdn.net/qq_35606400/article/details/114986532)

