---
title: 'Vant Weapp'
date: 2022-12-15 07:15:24
cover: false
tags:
- Vant
typora-root-url: Vant Weapp
---

# 背景知识

使用 Vant Weapp 前，请确保你已经学习过微信官方的 [小程序简易教程](https://developers.weixin.qq.com/miniprogram/dev/framework/) 和 [自定义组件介绍](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/)。

配置注意：

2.27.0的版本（或以上），没有手动指定`miniprogram_npm`路径，直接在`app.json`中引入也可使用

# 使用

## Button

[Button 按钮 - Vant Weapp (gitee.io)](https://vant-contrib.gitee.io/vant-weapp/#/button)

- 设置长度不生效，可用布局组件配合`block`即可



## Radio



## IndexBar 索引栏

[小程序使用Vant weapp的索引栏IndexBar无法正常跳转至对应锚点且底部异常 | 码农家园 (codenong.com)](https://www.codenong.com/cs105809390/)

[[Bug Report\] IndexBar 索引栏与overflow: auto;冲突 · Issue #4252 · youzan/vant-weapp (github.com)](https://github.com/youzan/vant-weapp/issues/4252)



# 修改外部样式类

https://blog.csdn.net/Z_PTOPONE/article/details/124238781

```html
<van-col span="8" custom-class="desc_info">任务说明</van-col>
```

