---
title: 'npm基础及常用工具包'
date: 2022-11-13 09:03:02
cover: false
tags:
- Node.js
categories: Node.js
---



# 常用工具包

## 加解密

### `jsonwebtoken`



- 安装

  ```js
  npm i jsonwebtoken
  ```

- 使用

  ```js
  // server.js - node.js
  
  // 1.引入
  const jwt = require('jsonwebtoken')
  
  // 2.服务端加密返回数据
  let person = {
      name: 'sai',
      age: 18, // 自定义字段
      openId // 第三方平台的字段，如小程序
  }
  let token = jwt.sign(person, 'myMiniProgram') // 自定义秘钥
  res.send(token)
  
  // 补充，别人即使拿到了数据，但没有秘钥，也是看不了数据的
  let reuslt = jwt.verify(token, 'myMiniProgram-wrong')
  
  ```

  ```js
  //  client.js - 小程序
  // 拿到token后存储本地，发送请求时header携带token
  const _token = JSON.stringify(token)
  wx.setStorageSync('jwt', _token)
  
  // 用的时候可以再用 JSON.parse 处理一下存储在 Storage 里的 Token 数据。
  const _jwt = wx.getStorageSync('jwt')
  const jwt = JSON.parse(_jwt)
  
  // 服务端签发过来的 Token ，除了 Token 本身，还有一些用户相关的信息，比如头像，名字，邮件等等。我们可以直接在小程序的页面上利用这些数据。
  wx.setJWT(response.data)
  wx.switchTab({
      url: '/pages/index/index'
  })
  
  ```



# 常见问题

## `ENOSPC`错误

```bash
[root@VM-4-12-centos crawler]# npm run serve

> crawler@0.1.0 serve
> vue-cli-service serve

 INFO  Starting development server...
[10%] building (0/0 modules)
node:internal/errors:464
    ErrorCaptureStackTrace(err);
    ^

Error: ENOSPC: System limit for number of file watchers reached, watch '/home/coder/code-prac/crawlerSchedule/crawler/public'
    at FSWatcher.<computed> (node:internal/fs/watchers:244:19)
    at Object.watch (node:fs:2249:34)
    at createFsWatchInstance (/home/coder/code-prac/crawlerSchedule/crawler/node_modules/chokidar/lib/nodefs-handler.js:119:15)
    at setFsWatchListener (/home/coder/code-prac/crawlerSchedule/crawler/node_modules/chokidar/lib/nodefs-handler.js:166:15)
    at NodeFsHandler._watchWithNodeFs (/home/coder/code-prac/crawlerSchedule/crawler/node_modules/chokidar/lib/nodefs-handler.js:331:14)
    at NodeFsHandler._handleDir (/home/coder/code-prac/crawlerSchedule/crawler/node_modules/chokidar/lib/nodefs-handler.js:567:19)
    at processTicksAndRejections (node:internal/process/task_queues:96:5)
    at async NodeFsHandler._addToNodeFs (/home/coder/code-prac/crawlerSchedule/crawler/node_modules/chokidar/lib/nodefs-handler.js:617:16)
    at async /home/coder/code-prac/crawlerSchedule/crawler/node_modules/chokidar/index.js:451:21
    at async Promise.all (index 0)
Emitted 'error' event on FSWatcher instance at:
    at FSWatcher._handleError (/home/coder/code-prac/crawlerSchedule/crawler/node_modules/chokidar/index.js:647:10)
    at NodeFsHandler._addToNodeFs (/home/coder/code-prac/crawlerSchedule/crawler/node_modules/chokidar/lib/nodefs-handler.js:645:18)
    at processTicksAndRejections (node:internal/process/task_queues:96:5)
    at async /home/coder/code-prac/crawlerSchedule/crawler/node_modules/chokidar/index.js:451:21
    at async Promise.all (index 0) {
  errno: -28,
  syscall: 'watch',
  code: 'ENOSPC',
  path: '/home/coder/code-prac/crawlerSchedule/crawler/public',
  filename: '/home/coder/code-prac/crawlerSchedule/crawler/public'
}
```

`Error: ENOSPC: System limit for number of file watchers reached, watch'所在文件路径'`

`vue`工程在 deepin15.11 系统环境中运行 `npm run serve`命令时出现如下错误：


解决方案
在终端按顺序执行下面两个命令即可解决问题

```bash
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p

sudo sysctl --system
```

是`linux`系统的限制导致这个报错了，需要设置一下：`fs.inotify.max_user_watches` 这个参数。

**解决方法**

执行：`vim /etc/sysctl.conf`，添加如下内容：

```bash
fs.inotify.max_user_watches=524288
```

`esc`，输入：`:wq`，保存退出

在命令行执行：`sysctl -p`







































