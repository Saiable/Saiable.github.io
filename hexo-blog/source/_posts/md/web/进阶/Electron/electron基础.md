---
title: 'electron基础'
date: 2022-11-23 09:03:02
cover: false
tags:
- electron
categories: electron
typora-root-url: electron基础
---



# 什么是`Electron`



# 第一个`Electron`程序

`npm i --save-dev electron`

`npm i nodemon`

`package.json`

```json
{
  "name": "01",
  "version": "1.0.0",
  "description": "",
  "main": "main.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "nodemon --exec electron ."
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "nodemon": "^2.0.20"
  },
  "devDependencies": {
    "electron": "^21.3.0"
  }
}

```

`main.js`

```js
const {app, BrowserWindow} = require('electron')

const createWindow = () => {
    const win = new BrowserWindow({
        width: 1000,
        height: 800
    })
    // win.loadURL('https://www.mindcons.cn')
    win.loadFile('index.html')

    // 允许打开调试
    win.webContents.openDevTools()
    
}

app.whenReady().then(createWindow)
```

`index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="./renderer/index.js"></script>
</head>
<body>
    <div>Hello</div>
</body>
</html>
```

`renderer/index.js`

```js
console.log(100)
```

![image-20221123201614720](image-20221123201614720.png)

关闭所有的安全警告，不推荐

```js
process.env['ELECTRON_DISABLE_SECURITY_WARNINGS'] = 'true'
```

这个警告是关于`CSP`的，可以在`index.html`中配置`CSP`策略，该策略允许导入本地资源

```html
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src 'self' data:; script-src 'self'; style-src 'self' 'unsafe-inline'">

```

这个策略不一定涵盖所有的`csp`警告，但至少我们可以知道忽略了什么警告

# 核心概念

## `Electron`主进程与渲染进程

主进程：启动项目时运行的`main.js`就是我们所说的主进程，在主进程运行的脚本可以创建`Web`页面的形式展示`GUI`。主进程只有一个。

渲染进程：每个`Electron`页面都在运行着自己的进程，这样的进程称之为渲染进程（基于`Chromium`的多进程结构）

![image-20221123200637342](image-20221123200637342.png)

主进程使用`BrowserWindow`创建实例，主进程销毁后，对应的渲染进程被终止，主进程与渲染进程通过`IPC`方式（事件驱动）进行通信

早期`Electron`中的渲染进程和主进程并没有隔离，渲染进程可以直接访问到主进程，有安全问题

```js
    const win = new BrowserWindow({
        width: 1000,
        height: 800,
        webPreferences: {
            nodeIntegration: true, // 集成node
            contextIsolation: false // 不隔离主进程和渲染进程了
        }
    })
```

此时可以在`index.js`的渲染进程中，调用`node`模块了

我们在桌面创建一个文本文件，里面内容是`abc`

`renderer/index.js`

```js
const fs = require('fs')
console.log(fs)

fs.writeFile('C:/Users/Administrator/Desktop/example.txt', 'abc', () => {
    console.log('done')
})
```

![image-20221123203329171](image-20221123203329171.png)

我们关闭了隔离选项，用户可以在`js`代码中直接操作`node`的文件，这个就很危险了，现在不会这么做了

上述的配置项不要使用

那么应该怎么做呢？

就是接下来要学习的，关于主进程和渲染进程的方方面面

## 主进程事件生命周期

在Windows和Linux上，关闭所有窗口通常会完全退出一个应用程序。

为了实现这一点，你需要监听 `app` 模块的 [`'window-all-closed'`](https://www.electronjs.org/zh/docs/latest/api/app#event-window-all-closed) 事件。如果用户不是在 macOS(`darwin`) 上运行程序，则调用 [`app.quit()`](https://www.electronjs.org/zh/docs/latest/api/app#appquit)。

关闭窗口

```js
app.on('window-all-closed', () => {
    console.log('close')
    // 对于mac系统，关闭窗口时，不能直接退出应用
    if(process.platform !== 'darwin') { // mac系统的名字
        app.quit()
    }
})
```

当 Linux 和 Windows 应用在没有窗口打开时退出了，macOS 应用通常即使在没有打开任何窗口的情况下也继续运行，并且在没有窗口可用的情况下激活应用时会打开新的窗口。

为了实现这一特性，监听 `app` 模块的 [`activate`](https://www.electronjs.org/zh/docs/latest/api/app#event-activate-macos) 事件。如果没有任何浏览器窗口是打开的，则调用 `createWindow()` 方法。

因为窗口无法在 `ready` 事件前创建，你应当在你的应用初始化后仅监听 `activate` 事件。 通过在您现有的 `whenReady()` 回调中附上您的事件监听器来完成这个操作。

```js
app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})
```

> 注意：此时，您的窗口控件应功能齐全！



## 渲染进程如何使用`Node`模块

在渲染进程开始之前，给了一个机会，去调用`Node`

通过`webPreferences`配置项

```js
const path = require('path')
const createWindow = () => {
    const win = new BrowserWindow({
        width: 1000,
        height: 800,
        webPreferences: {
            nodeIntegration: true, // 高版本要开启nodeIntegration配置项
            // contextIsolation: false
            preload: path.resolve(__dirname, './preload.js')
        },
    })
    // win.loadURL('https://www.mindcons.cn')
    win.loadFile('index.html')

    // 允许打开调试
    win.webContents.openDevTools()

    // process.env['ELECTRON_DISABLE_SECURITY_WARNINGS'] = 'true'
}
```

任何去请求`index.html`文件之前，先做一个预加载

将之前写文件的代码，放在`preload.js`中

```js
const fs = require('fs')
console.log(fs)

fs.writeFile('C:/Users/Administrator/Desktop/example.txt', 'abc', () => {
    console.log('done')
})
```

可以正确执行

![image-20221124071624388](image-20221124071624388.png)



`preload.js`变量，想在`index.html`里面用怎么办呢

透支一个概念，桥的概念，`contextBridge`

`preload.js`

```js
const {contextBridge} = require('electron')
console.log(contextBridge)
```

可以看到这是一个对象，以及它的作用域链情况

![image-20221124072426782](image-20221124072426782.png)

`preload`中定义

```js
contextBridge.exposeInMainWorld('myApi', {
    platform: process.platform
})
```

`renderer/index.js`中使用

```js
console.log(window.myApi)
```

![image-20221124210603952](image-20221124210603952.png)

通过`contextBridge`可以将`Node`中的模块及其他变量，挂载到渲染进程的`window`对象上

## 主进程与渲染进程通信

主进程中注册使用`ipcMain.handle`监听一个`channel`

`main.js`

```js
// 主进程中注册好事件
ipcMain.handle('send-event', (event, msg) => {
    console.log(msg) // 后台打印
    retrun msg // 收到渲染进程传递的参数后，再返回回去
})
```

预加载器中使用`ipcMain.renderer`向指定`channel`发送消息，并通过`contextBridge`挂载到渲染进程的`window`对象上

`preload.js`

```js
const handleSend = (arg) => {
    let callback = await ipcRenderer.invoke('send-event', arg)
    console.log(callback) // 前台打印
}
contextBridge.exposeInMainWorld('myApi', {
        platform: process.platform,
        handleSend
})

```

渲染进程使用暴露的方法，与主进程通信

```js
document.querySelector('#btn').addEventListener('click', () => {
    console.log('btn')
    const {handleSend} = myApi
    handleSend('haha')
})
```

# 主进程

> `Electron API`有两种
>
> - `Main Process`（主进程）
> - `Renderer Process`（渲染进程）

## `App`

### 事件

#### `before-quit`

> 在应用程序开始关闭之前触发

```js
app.on('before-quit', () => {
    console.log('App is quiting')
})

```

#### `browser-window-blur`

> 在`browserWindow`失去焦点时触发

```js
app.on('browser-window-blur', (e) => {
    console.log('App unfocused')
})
```

#### `browser-window-focus`

> 在`browserWindow`获得焦点时触发

```js
app.on('browser-window-focus', (e) => {
    console.log('App focused')
})

```

### 方法

#### `app.quit()`

```
app.on('browser-window-blur', (e) => {
    console.log('App unfocused')
    setTimeout(() => {
        app.quit()
    }, 3000)
})

app.on('browser-window-blur', (e) => {
    console.log('App unfocused')
    setTimeout(app.quit, 3000)
})
```

#### `app.getPath(name)`

```js
app.whenReady().then(() => {
    createWindow()

    // 在Mac系统下，当全部窗口关闭，点击dock图标，窗口再次打开（针对mac下关闭窗口后不能重新打开的问题）
    app.on('active',() => {
        if(BrowserWindow.getAllWindows().length === 0) {
            createWindow()
        }
    })
    console.log(app.getPath('desktop'))
    console.log(app.getPath('music'))
    console.log(app.getPath('temp'))
    console.log(app.getPath('userData'))
})
```

结果

```bash
C:\Users\Administrator\Desktop
C:\Users\Administrator\Music
C:\Users\ADMINI~1\AppData\Local\Temp
C:\Users\Administrator\AppData\Roaming\myElectron
```

## `BrowserWindow`

> `electron.BrowserWindow`：创建和控制浏览器窗口

### 实例方法

`win.loadURL(url[, options])`和`loadFile`互斥

```js
const createWindow = () => {
    const win = new BrowserWindow({
        width: 1000,
        height: 800,
        webPreferences: {
            nodeIntegration: true,
            preload: path.resolve(__dirname, './preload.js')
        },
    })
    
    // win.loadURL('https://www.mindcons.cn')
    win.loadFile('index.html')

    win.webContents.openDevTools()

}
```

### 优雅的显示窗口

- 使用`ready-to-show`事件

  ```js
  const createWindow = () => {
      const win = new BrowserWindow({
          width: 1000,
          height: 800,
          show: false, // 一开始不显示
          webPreferences: {
              nodeIntegration: true,
              preload: path.resolve(__dirname, './preload.js')
          },
      })
      win.loadURL('https://www.mindcons.cn')
  
      win.webContents.openDevTools()
  
      win.on('ready-to-show', () => { // 准备完资源后再显示，看具体情况使用
          win.show()
      })
  }
  ```

- 设置窗口背景颜色，该颜色并不是通过给标签元素添加背景颜色实现的，而是设置的窗口背景颜色

  ```js
  const createWindow = () => {
      const win = new BrowserWindow({
          width: 1000,
          height: 800,
          show: false,
          backgroundColor: 'purple',
          webPreferences: {
              nodeIntegration: true,
              preload: path.resolve(__dirname, './preload.js')
          },
      })
      win.loadURL('https://www.mindcons.cn')
  
      win.webContents.openDevTools()
  
      win.on('ready-to-show', () => {
          win.show()
      })
  }
  ```

### 父子窗口

- 窗口定义

  ```js
  const createWindow = () => {
      const win = new BrowserWindow({
          width: 1000,
          height: 800,
          show: false,
          backgroundColor: 'purple',
          webPreferences: {
              nodeIntegration: true,
              preload: path.resolve(__dirname, './preload.js')
          },
      })
  
  
      win.loadFile('index.html')
      win.webContents.openDevTools()
  
      win.on('ready-to-show', () => {
          win.show()
      })
  
      const win2 = new BrowserWindow({
          width: 600,
          height: 400
      })
      win2.loadURL('https://www.baidu.com')
  }
  
  ```

  

- 窗口关系

  ```js
  const createWindow = () => {
      const win = new BrowserWindow({
          width: 1000,
          height: 800,
          show: false,
          backgroundColor: 'purple',
          webPreferences: {
              nodeIntegration: true,
              preload: path.resolve(__dirname, './preload.js')
          },
      })
  
  
      win.loadFile('index.html')
      win.webContents.openDevTools()
  
      win.on('ready-to-show', () => {
          win.show()
      })
  
      const win2 = new BrowserWindow({
          width: 600,
          height: 400,
          parent: win, // 指定父级关联关系，父子窗口都可点击
          modal: true, // 指定为模态窗口，只能操作win2窗口
      })
      win2.loadURL('https://www.baidu.com')
  }
  
  ```

  

### 无边框窗口

```js
    const win = new BrowserWindow({
        width: 1000,
        height: 800,
        show: false,
        backgroundColor: 'purple',
        frame: false, // 设置无边框
        webPreferences: {
            nodeIntegration: true,
            preload: path.resolve(__dirname, './preload.js')
        },
    })
```

<img src="image-20221128211617229.png" alt="image-20221128211617229" style="zoom:50%;" />

配合`CSS`实现拖拽

在此之前我们用`nodemon`监听`html`等文件的变化

```json
    "start": "nodemon --exec electron . --watch ./ --ext .js, .html, .css, .vue"
```

注意由于`meta`配置的`csp`策略，不能写内部样式。另外`link`标签必须指定`rel`属性，否则引入失效，估计和渲染引擎有关

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src 'self' data:; script-src 'self'; style-src 'self' 'unsafe-inline'">
    <title>Document</title>
    <link rel="stylesheet" href="./style.css"></link>
</head>
<body>
    <div>Hello</div>
    <button id="btn">send</button>
    <script src="./renderer/index.js"></script>

</body>
</html>
```

`style.css`

```css
html {
    height: 100%;

}
body {
    height: 100%;
    user-select: none;
    -webkit-app-region: drag;/* drag/nodrag */
}
```



显示红绿灯（最小化、最大化、关闭）

```js
    const win = new BrowserWindow({
        width: 1000,
        height: 800,
        show: false,
        backgroundColor: 'purple',
        frame: false,
        titleBarStyle:'hidden', // Or hiddenInset 距离红绿灯更近
        webPreferences: {
            nodeIntegration: true,
            // contextIsolation: false
            preload: path.resolve(__dirname, './preload.js')
        },
    })
```

实测下，`windows`并没有出现

## 属性与方法

