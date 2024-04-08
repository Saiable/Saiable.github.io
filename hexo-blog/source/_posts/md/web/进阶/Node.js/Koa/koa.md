---
title: Koa2搭建API服务
date: 2022/7/25 23:52:13
cover: false
tags:
- Koa
categories: Koa
description: "包含内容：koa项目初始化、目录结构优化、ORM工具继承、错误处理"
toc_number: true
typora-root-url: koa
---

# Koa2入门

https://www.bilibili.com/video/BV18h411H7GE?spm_id_from=333.999.0.0

# Node+Koa2搭建`API`服务

教程来源：https://www.bilibili.com/video/BV13A411w79h?spm_id_from=333.999.0.0

## 初始化

- `npm init -y`
- `git init`，并新建`.gitignore`，添加`node_modules`
  - 提交版本后，并通过`git log`查看记录
- 新建`README.md`文档

## 项目初始化

- `npm i koa`

- 根目录新建`src/main.js`

  ```js
  const Koa = require('koa') // 导入Koa，由于导出的是类，一般大写
  
  const app = new Koa() // 实例化
  
  app.use((ctx, next) => { // 中间件
      ctx.body = 'hello world' // 测试代码
  })
  
  app.listen(3000, () => { // 开启服务
      console.log('server is running on http://localhost:3000 !');
  })
  ```

- 启动开发服务：

  - `node .\src\main.js`:`node`方式启动，是常驻内存，不是热加载的

## 开发优化

### 自动重启服务

- `npm i nodemon -D`

- 配置`dev`脚本：如果`nodemon`装在了全局，则不需要加`npx`

  `package.json`

  ```json
  {
    "name": "01",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "test": "echo \"Error: no test specified\" && exit 1",
      "dev": "npx nodemon ./src/main.js"
    },
    "keywords": [],
    "author": "",
    "license": "ISC",
    "dependencies": {
      "koa": "^2.13.4",
      "nodemon": "^2.0.19"
    }
  }
  
  ```

- `npm run dev`启动

  ```bash
  PS D:\workspace\github\code\project-workshop\code-prac\koa\01> npm run dev
  
  > 01@1.0.0 dev
  > npx nodemon ./src/main.js
  
  [nodemon] 2.0.19
  [nodemon] to restart at any time, enter `rs`
  [nodemon] watching path(s): *.*
  [nodemon] watching extensions: js,mjs,json // 监听这三种文件
  [nodemon] starting `node ./src/main.js` // 使用node启动
  server is running on http://localhost:3000 ! // 打印输出内容
  ```

### 读取配置文件

- 安装`dotenv`（可以去`npm`官网上查看介绍）：在根目录中加载`.env`的配置文件，将键值对加载到`process.env`的环境变量中

  - `npm i dotenv`

  - 项目根目录，新建`.env`配置文件并添加配置

    `.env`

    ```
    APP_PORT = 8000
    ```

- 读取配置

  - 新建`src/config/config.default.js`

    ```js
    require('dotenv').config() // 导入dotenv，调用config方法，读取配置并写入到`process.env`中
    
    module.export = process.env
    ```

  - 改写`main.js`，使用解构赋值的方式，获取到`APP_PORT`的配置

    ```js
    const Koa = require('koa')
    const {APP_PORT} = require('./config/config.default') // 导入process.env环境变量中的APP_PORT字段
    const app = new Koa()
    
    app.use((ctx, next) => {
        ctx.body = 'hello world'
    })
    
    app.listen(APP_PORT, () => {
        console.log(`server is running on http://localhost:${APP_PORT} !`); // 使用模板字符串
    })
    ```

  - 启动开发服务

## 添加路由

所谓的`api`，就是根据不同`url`返回不同的数据

目前`http://localhost:8000`和`http://localhost:8000/users`返回的内容都是一样的

需要使用路由，来根据不同的`url`，调用不同的处理函数



安装`koa-router`

- ``api官网：`[router/API.md at master · koajs/router (github.com)](https://github.com/koajs/router/blob/master/API.md)
- `npm install @koa/router`

官网案例：

```js
const Koa = require('koa');
const Router = require('@koa/router'); // 1.导入Router

const app = new Koa();
const router = new Router(); // 2.新建router实例对象

router.get('/', (ctx, next) => { // 3.编写路由
  // ctx.router available
});

app // 4.注册中间件
  .use(router.routes()) // use方法只能接受函数作为参数，通过router.routes()方法返回一个函数给中间件处理
  .use(router.allowedMethods());
```

配置多个路由

```js
const Koa = require('koa') // 导入Koa，由于导出的是类，一般大写
const Router = require('@koa/router') // 导入router

const {APP_PORT} = require('./config/config.default')
const app = new Koa() // 实例化


// app.use((ctx, next) => { // 中间件
//     ctx.body = 'hello world' // 测试代码
// })

const indexRouter = new Router()
indexRouter.get('/', (ctx, next) => {
    ctx.body = 'hello world'
})

const userRouter = new Router()
userRouter.get('/user', (ctx, next) => {
    ctx.body = 'user'
})


app.use(indexRouter.routes())
app.use(userRouter.routes())

app.listen(APP_PORT, () => { // 开启服务
    console.log(`server is running on http://localhost:${APP_PORT} !`);
})
```

但是代码都写在一起肯定不行，需要拆分一下路由

新建`src/router`文件夹

新建`user.routes.js`

```js
const Router = require('@koa/router')
const router = new Router({prefix: '/user'})


router.get('/', (ctx, next) => {
    ctx.body = 'user'
})

module.exports = router

```

修改`main.js`

```js
const Koa = require('koa') // 导入Koa，由于导出的是类，一般大写
const Router = require('@koa/router') // 导入router

const {APP_PORT} = require('./config/config.default')
const app = new Koa() // 实例化
const userRouter = require('./router/user.route')

const indexRouter = new Router()
indexRouter.get('/', (ctx, next) => {
    ctx.body = 'hello world'
})

app.use(indexRouter.routes()) // 后续这里也会继续优化，不然当路由很多时，写法也会很恶心
app.use(userRouter.routes())

app.listen(APP_PORT, () => { // 开启服务
    console.log(`server is running on http://localhost:${APP_PORT} !`);
})

```

## 目录结构优化

### 拆分`http`服务和业务代码

我们在`main.js`里面写了太多的功能

- 拆分`http`服务与业务相关代码

  - 新建`src/app/index.js`，专门放业务代码

  ```js
  const Koa = require('koa') // 导入Koa，由于导出的是类，一般大写
  const Router = require('@koa/router') // 导入router
  
  const userRouter = require('../router/user.route')
  
  const app = new Koa() // 实例化
  const indexRouter = new Router()
  indexRouter.get('/', (ctx, next) => {
      ctx.body = 'hello world'
  })
  
  app.use(indexRouter.routes())
  app.use(userRouter.routes())
  
  module.exports = app
  
  ```

  修改`man.js`

  ```js
  
  const {APP_PORT} = require('./config/config.default')
  
  const app = require('./app')
  
  app.listen(APP_PORT, () => { // 开启服务
      console.log(`server is running on http://localhost:${APP_PORT} !`);
  })
  
  
  ```

### 抽离控制层

将路由`router`中的处理函数，单独抽离成控制层`controller`

- 新建`src/controller`文件夹

- 新建`user.controller.js`

  ```js
  class UserController{
      async register(ctx, next) {
          ctx.body = '用户注册成功'
      }
  }
  
  module.exports = new UserController()
  ```

  修改`router/user.route.js`

  ```js
  const Router = require('@koa/router')
  const router =  new Router({prefix: '/user'})
  const {register} = require('../controller/user.conroller')
  
  // 注册接口
  router.post('/register', register)
  
  module.exports = router
  
  ```

- 测试接口

  这里我们写成了`post`请求，使用`postman`或者是`Apifox`（国内的）来测试`post`请求

  这里以`apifox`为例，下载后，新建项目 > 新建接口

  按图示配置

  ![image-20220725220620161](image-20220725220620161.png)

  ![image-20220725220748784](image-20220725220748784.png)

  配置好路由后，点击运行，可以拿到数据了：

  ![image-20220725220846437](image-20220725220846437.png)

- 我们再写一个登录的接口

  `user.router.js`

  ```js
  const Router = require('@koa/router')
  const router =  new Router({prefix: '/user'})
  const {register, login} = require('../controller/user.conroller')
  
  // 注册接口
  router.post('/register', register)
  // 登录接口
  router.post('/login', login)
  
  
  module.exports = router
  
  ```

  `user.controller.js`

  ```js
  class UserController{
      async register(ctx, next) {
          ctx.body = '用户注册成功'
      }
  
      async login(ctx, next) {
          ctx.body = '用户登录成功'
      }
  }
  
  module.exports = new UserController()
  ```


## 解析`body`、拆分`service`层

### 解析`body`

> 完整的注册接口

```
POST /user/register
```

> 请求参数

```
user_name, password
```

> 响应

成功：

```
{
    "code": 0,
    "message": "用户注册成功",
    "result": {
		"id": 2,
        "user_name": "user"
    }
}
```

原型图：

<img src="image-20220725222952833.png" alt="image-20220725222952833" style="zoom:67%;" />

`koa`需要借助中间件，来解析参数

- `koa-body`：https://www.npmjs.com/package/koa-body

  ```
  A full-featured koa body parser middleware. Supports multipart, urlencoded, and json request bodies. Provides the same functionality as Express's bodyParser - multer.
  ```

  官方基础样例：

  ```js
  const Koa = require('koa');
  const koaBody = require('koa-body'); // 1.引入中间件
  
  const app = new Koa();
  
  app.use(koaBody()); // 在所有请求之前，注册这个中间件，就把所有的内容写到了ctx.request.body里面
  app.use(ctx => {
    ctx.body = `Request Body: ${JSON.stringify(ctx.request.body)}`; // 3.看下request.body
  });
  
  app.listen(3000);
  ```

  - 更推荐，相比较于`koa-bodyparser`，还支持文件上传

- `koa-bodyparser`



将之前`apifox`的注册接口完善下，由于是`post`请求，我们在`body`里面，设置参数

![image-20220725225232579](image-20220725225232579.png)

 安装`koa-body`

```bash
npm i koa-body
```



在`app/index.js`中添加`koa-body`相关代码

`app/index.js`

```js
const Koa = require('koa')
const Router = require('@koa/router')
const koaBody = require('koa-body') // 1.导入koa-body
const userRouter = require('../router/user.route')

const app = new Koa()
app.use(koaBody()) // 2.在所有中间件之前，注册koa-body

const indexRouter = new Router()
indexRouter.get('/', (ctx, next) => {   
    ctx.body = `Request Body: ${JSON.stringify(ctx.request.body)}`
})

app.use(indexRouter.routes())
app.use(userRouter.routes())

module.exports = app

```

控制层（处理函数）`user.config.js`

```js
class UserController{
    async register(ctx, next) {
        console.log(ctx.request.body)
        ctx.body = ctx.request.body // 我的理解：把请求的参数，放在响应的body里面，再返给客户端
    }

    async login(ctx, next) {
        ctx.body = '用户登录成功'
    }
}

module.exports = new UserController()
```

回到`apifox`中，我们生成下`body`请求体，发送下注册的请求

![image-20220725230641092](image-20220725230641092.png)

后台也打印结果了

![image-20220725230741773](image-20220725230741773.png)

控制器里一般做这些事

- 1.获取数据
- 2.操作数据库
  - 如果操作数据库的逻辑很复杂，也会单独抽出这一部分（`service`层）
- 3.返回结果



### 抽取`servcie`层

和数据库相关的，根据客户端传递的不同参数，来操作数据库

新建`src/service`目录

新建`user.service.js`

```js
class UserService {
    // 主要用来操作数据库
    // 处理函数对应数据库的操作，就是增删改查
    // 注册，就是往数据库里，增加一条记录
    async createUser(user_name, password) { // 当参数超过三个时，建议用一个对象
        //@TODO: 写入数据库
        return '写入数据库成功'
    }
}

module.exports = new UserService()
```

修改`user.controller.js`

```js
const {createUser} = require('../service/user.service')

class UserController{
    async register(ctx, next) {
        // 1. 获取数据
        // console.log(ctx.request.body)
        const {user_name, password} = ctx.request.body
        // 2.操作数据库
        const res = await createUser(user_name, password)

        // 3.返回结果
        ctx.body = ctx.request.body // 我的理解：把请求的参数，放在响应的body里面，再返给客户端
    }

    async login(ctx, next) {
        ctx.body = '用户登录成功'
    }
}

module.exports = new UserController()
```

后台打印结果：

![image-20220725232505667](image-20220725232505667.png)



## `ORM`工具集成

### `sequelize`介绍

`ORM`：对象关系映射

- 数据表映射（对应）一个类
- 数据表中的数据行（记录）对应一个对象
- 数据表字段对应对象的属性
- 数据表的操作，对应对象的方法
- 就是使用面向对象的方式，来操作数据库

使用`sequelize` `ORM`数据库工具：https://github.com/demopark/sequelize-docs-Zh-CN/tree/master

- 基于`Promise`的`ORM`工具
- Sequelize 是一个基于` promise` 的 `Node.js ORM` 工具, 目前支持 `Postgres, MySQL, MariaDB, SQLite 以及 Microsoft SQL Server, Amazon Redshift 和 Snowflake’s Data Cloud`. 它具有强大的事务支持, 关联关系, 预读和延迟加载,读取复制等功能.

- 安装`sequelize`和`mysql2`（支持`Promise`）

  ```
  npm i sequelize mysql2
  ```

  得注意下安装的`sequelize`支持的最低版本的`mysql`，目前默认安装的`sequlize`版本是`6.21.3`，对应的`mysql`版本至少是`5.7`及以上：https://github.com/demopark/sequelize-docs-Zh-CN/tree/v6

  ![image-20220726064512073](image-20220726064512073.png)



### 安装数据库

#### `windows`安装

在正式连接之前，我们需要装下`mysql`数据库，这里暂时安装`windows`版本，参照：https://blog.csdn.net/jsugs/article/details/124143762

启动`mysql`服务

```
输入net start mysql或sc start mysql
```



![image-20220726070015186](image-20220726070015186.png)



改密码后再用`navicat连接`，会报错`Authentication plugin 'caching_sha2_password' cannot be loaded`，参照：https://www.jianshu.com/p/465a444ad846

```bash
ALTER USER 'root'@'localhost' IDENTIFIED BY '123123' PASSWORD EXPIRE NEVER;   #修改加密规则 
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123123';   #更新一下用户的密码
FLUSH PRIVILEGES;   #刷新权限 
```



![image-20220726071528438](image-20220726071528438.png)

查询mysql进程，并杀掉

```bash
netstat -aon|findstr "3306"

taskkill /pid 26372 -t -f
```

成功进入后，新建数据库

一开始是没有选中下面两个的，设置名称后直接确定

![image-20220726071755569](image-20220726071755569.png)

#### `linux`安装

使用`docker`安装，参见

- 待添加

- [Docker安装mysql5.7报错 ERROR 1045 (28000): Access denied for user - 简书 (jianshu.com)](https://www.jianshu.com/p/a49389497a0c)

最后一步报语法错误，可以不用管

### 连接数据库

官方示例：https://github.com/demopark/sequelize-docs-Zh-CN/blob/v6/core-concepts/getting-started.md

```js
const { Sequelize } = require('sequelize');

// 方法 1: 传递一个连接 URI
const sequelize = new Sequelize('sqlite::memory:') // Sqlite 示例
const sequelize = new Sequelize('postgres://user:pass@example.com:5432/dbname') // Postgres 示例

// 方法 2: 分别传递参数 (sqlite)
const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: 'path/to/database.sqlite'
});

// 方法 3: 分别传递参数 (其它数据库)
const sequelize = new Sequelize('database', 'username', 'password', {
  host: 'localhost',
  dialect: /* 选择 'mysql' | 'mariadb' | 'postgres' | 'mssql' 其一 */
});
```

新建`src/db/seq.js`

该文件中实现数据库的连接，并导出

```js
const {Sequelize} = require('sequelize')

const seq = new Sequelize('mytest', 'root', '123123', { // 需要手动新建mytest
    host: 'localhost', // host: '1.12.**.**', // 若需要指定其他端口号，请参阅官网查询配置
    dialect: 'mysql'
})


seq.authenticate().then(res => {
    console.log('数据库连接成功', res)
}).catch(error => {
    console.log('数据库连接失败', error)
})

module.exports = seq
```

在`db`目录下，使用`node`测试下：

![image-20220726200218491](image-20220726200218491.png)

开发环境我们这样搞没事，生产环境可能会用连接池

### 配置文件

使用`dotenv`将参数提取成配置文件

修改`.env`

```
APP_PORT = 8000

MYSQL_HOST = localhost
MYSQL_PORT = 3306
MYSQL_USER = root
MYSQL_PASSWORD = 123123
MYSQL_DATABASE = mytest
```

`seq.js`中导入并使用

```js
const { Sequelize } = require('sequelize')
const { 
    MYSQL_HOST,
    MYSQL_PORT,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_DATABASE 
} = require('../config/config.default')

console.log(MYSQL_HOST,MYSQL_DATABASE)
const seq = new Sequelize(MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, {
    host: MYSQL_HOST,
    dialect: 'mysql',
})


// seq.authenticate().then(res => {
//     console.log('数据库连接成功', res)
// }).catch(error => {
//     console.log('数据库连接失败', error)
// })

module.exports = seq
```

此时需要在根目录下测试，不然读不到`.env`文件

![image-20220726201817869](image-20220726201817869.png)

测试完将测试代码注释掉

## 创建`User`模型

### 模型创建

新建`src/model`文件夹

`service`层通过`model`层来具体操作数据库

新建`user.model.js`，使用`define`方法来创建模型：https://www.sequelize.com.cn/core-concepts/model-basics#%E4%BD%BF%E7%94%A8-sequelizedefine

全局定义表名等于模型名，`seq.js`：

```js
const { Sequelize } = require('sequelize')
const { 
    MYSQL_HOST,
    MYSQL_PORT,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_DATABASE 
} = require('../config/config.default')

console.log(MYSQL_HOST,MYSQL_DATABASE)
const seq = new Sequelize(MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, {
    host: MYSQL_HOST,
    dialect: 'mysql',
    define: {
        freezeTableName: true // 全局定义表明等于模型名
    }
})

module.exports = seq
```

根据表设计文档，定义模型属性：

**用户表**

表名：`sai_users`

| 字段名    | 字段类型     | 说明                              |
| --------- | ------------ | --------------------------------- |
| id        | int          | 主键，自增（sequelize会自动维护） |
| user_name | varchar(255) | 用户名，unique                    |
| password  | char(64)     | 密码                              |
| is_admin  | tinyint(1)   | 0：不是管理员，1：是管理员        |

定义模型属性时的数据类型，参见：https://www.sequelize.com.cn/core-concepts/model-basics#%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B

`user.model.js`

```js
const { DataTypes } = require("sequelize") // 不要相信vscode的自动导入，坑！！

const seq = require('../db/seq')

// 创建模型
const User = seq.define('sai_user', {
    // id会被sequelize自动创建

    // user_name
    user_name: {
        type: DataTypes.STRING,
        allowNull: false, // 不允许为空
        unique: true,
        comment: '用户名唯一' // 注释
    },
    // password
    password: {
        type: DataTypes.CHAR(64),
        allowNull: false,
        comment: '密码'
    },
    is_admin: {
        type: DataTypes.BOOLEAN,
        allowNull: false,
        defaultValue: 0,
        comment: '是否为管理员，0：不是管理员（默认值），1：是管理员'
    }
})

User.sync({force: true})
```

有关模型同步：https://www.sequelize.com.cn/core-concepts/model-basics#%E6%A8%A1%E5%9E%8B%E5%90%8C%E6%AD%A5

根目录下，执行`node src/model/user.model.js`

就是执行了`sql`语句

```bash
PS D:\workspace\github\code\project-workshop\code-prac\koa\01> node .\src\model\user.model.js
localhost mytest
Executing (default): DROP TABLE IF EXISTS `sai_user`;
Executing (default): CREATE TABLE IF NOT EXISTS `sai_user` (`id` INTEGER NOT NULL auto_increment , `user_name` VARCHAR(255) NOT NULL UNIQUE COMMENT '用户名唯一', `password` CHAR(64) NOT NULL COMMENT '
密码', `is_admin` TINYINT(1) NOT NULL DEFAULT 0 COMMENT '是否为管理员，0：不是管理员（默认值），1：是管理员', `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB;
Executing (default): SHOW INDEX FROM `sai_user`
```

可以看到，数据库中多了一个表：

![image-20220726211457412](image-20220726211457412.png)

![image-20220726211857584](image-20220726211857584.png)

其中，`createAt`和`updatedAt`是`sequelize`自动给我们维护的，如果不需要时间戳，在`define`函数中，添加配置项：`{timestamps: false}`，但是一般情况下，都是保留的

导出`User`模型，并注释掉`sync`的代码

```js
const { DataTypes } = require("sequelize")

const seq = require('../db/seq')

// 创建模型
const User = seq.define('sai_user', {
    // id会被sequelize自动创建

    // user_name
    user_name: {
        type: DataTypes.STRING,
        allowNull: false, // 不允许为空
        unique: true,
        comment: '用户名唯一' // 注释
    },
    // password
    password: {
        type: DataTypes.CHAR(64),
        allowNull: false,
        comment: '密码'
    },
    is_admin: {
        type: DataTypes.BOOLEAN,
        allowNull: false,
        defaultValue: 0,
        comment: '是否为管理员，0：不是管理员（默认值），1：是管理员'
    }
})

// User.sync({force: true}) // 强制同步数据库（创建数据表）
module.exports = User
```

### 添加用户

我们继续完善写入数据库的代码

需要通过`ORM`实现标准的`CRUD`：https://www.sequelize.com.cn/core-concepts/model-querying-basics

新建`src/service/user.service.js`

```js
const User = require('../model/user.model')

class UserService {
    // 主要用来操作数据库
    // 处理函数对应数据库的操作，就是增删改查
    // 注册，就是往数据库里，增加一条记录
    async createUser(user_name, password) { // 当参数超过三个时，建议用一个对象
        //@TODO: 写入数据库
        // 插入数据
        const res = await User.create({
            user_name,
            password
        })
        console.log(res)

        return res
    }
}

module.exports = new UserService()
```

使用`apifox`发送`register`接口，成功后查看数据库

![image-20220726231148358](image-20220726231148358.png)

![image-20220726231243724](image-20220726231243724.png)

成功注册，注意下时区慢8小时

再看下后台打印：

执行的了`insert`语句

`User.create`返回的是一个`sai_user`的表模型对象，`dataValues`对应着表里面的一条记录

```bash
Executing (default): INSERT INTO `sai_user` (`id`,`user_name`,`password`,`is_admin`,`createdAt`,`updatedAt`) VALUES (DEFAULT,?,?,?,?,?);
sai_user {
  dataValues: {
    is_admin: false,
    id: 1,
    user_name: '邵洋',
    password: 'do',
    updatedAt: 2022-07-26T15:08:52.849Z,
    createdAt: 2022-07-26T15:08:52.849Z
  },
  _previousDataValues: {
    user_name: '邵洋',
    password: 'do',
    id: 1,
    is_admin: false,
    createdAt: 2022-07-26T15:08:52.849Z,
    updatedAt: 2022-07-26T15:08:52.849Z
  },
  uniqno: 1,
  _changed: Set(0) {},
  _options: {
    isNewRecord: true,
    _schema: null,
    _schemaDelimiter: '',
    attributes: undefined,
    include: undefined,
    raw: undefined,
    silent: undefined
  },
  isNewRecord: false
}
```

我们要返回给用户`dataValues`的结果

对于其他的值，在`service`层就可以直接过滤掉，直接返回`res.dataValues`

`user.service.js`

```js
const User = require('../model/user.model')
class UserService {
    // 主要用来操作数据库
    // 处理函数对应数据库的操作，就是增删改查
    // 注册，就是往数据库里，增加一条记录
    async createUser(user_name, password) { // 当参数超过三个时，建议用一个对象
        //@TODO: 写入数据库
        // 插入数据
        const res = await User.create({ user_name, password })

        return res.dataValues
    }
}

module.exports = new UserService()
```

那么`controller`层拿到返回的数据后，再根据接口文档，构建最终要返回给客户端的数据格式

注册接口：

成功

```json
{
	"code": 0,
	"message": "用户注册成功",
    "result": {
        "id": 2,
        "user_name": "user"
    }
}
```

失败

```json
{
    "code": "10001",
    "message": "用户名或密码不能为空",
    "result": ""
}
```

修改控制层

`user.controller.js`

```js
const {createUser} = require('../service/user.service')

class UserController{
    async register(ctx, next) {
        // 1. 获取数据
        // console.log(ctx.request.body)
        const {user_name, password} = ctx.request.body
        // 2.操作数据库
        const res = await createUser(user_name, password)
        // console.log(res)
        // 3.返回结果
        ctx.body = {
            code: 0,
            message: '用户注册成功',
            result: {
                id: res.id,
                user_name: res.user_name
            }
        }
    }

    async login(ctx, next) {
        ctx.body = '用户登录成功'
    }
}

module.exports = new UserController()
```

再次使用`apifox`测试下`register`接口，注意要使用新的样例（不要重复注册，目前没做异常处理）

![image-20220727060131292](image-20220727060131292.png)

整个的流程小结：

用户发送请求，`koa`服务接受到请求，先导入各种中间件，然后处理路由，根据路由调用处理函数（控制层），处理函数中涉及业务逻辑及数据库操作（服务层），服务层根据模型层，返回给控制层操作数据库的结果，控制层根据该结果封装接口数据，返回给路由，最后`koa`将路由的结果，作为接口响应发送到服务端

### 错误处理

重复注册和没有用户名，目前都会返回`500`，错误类型不够细致

![image-20220727061109390](image-20220727061109390.png)



后台是可以看到两次操作的错误提示的

![image-20220727061249819](image-20220727061249819.png)

对于不同的错误类型，我们要分别处理



在控制层接受到用户参数时，要进行验证

- 合法性验证

  `user.controller.js`

  ```js
  const {createUser} = require('../service/user.service')
  
  class UserController{
      async register(ctx, next) {
          const {user_name, password} = ctx.request.body
          // 合法性验证
          if(!user_name || !password) {
              // 记录错误信息，后续可以记录到错误日志中
              console.error('用户名或密码为空')
              ctx.status = 400
              ctx.body = {
                  code: '10001', // 自定义的，公司一般会有开发规范
                  message: '用户名或者密码为空',
                  result: ''
              }
  
              return // 合法性验证不通过的话，直接返回
          }
  
  		// 验证通过后，再去操作数据库
          const res = await createUser(user_name, password)
          console.log(res)
          ctx.body = {
              code: 0,
              message: '用户注册成功',
              result: {
                  id: res.id,
                  user_name: res.user_name
              }
          }
      }
  
      async login(ctx, next) {
          ctx.body = '用户登录成功'
      }
  }
  
  module.exports = new UserController()
  ```

  参数只写一个字段，测试一下注册接口：
  ![image-20220727062331691](image-20220727062331691.png)

  可以看到后台，打印的错误日志

  ![image-20220727062455540](image-20220727062455540.png)

  

- 合理性验证

  - `controller`层，需要根据传入的参数，查询数据库

    `user.controller.js`

    ```js
    const {createUser, getUserInfo} = require('../service/user.service')
    
    class UserController{
        async register(ctx, next) {
            const {user_name, password} = ctx.request.body
            if(!user_name || !password) {
                console.error('用户名或密码为空')
                ctx.status = 400
                ctx.body = {
                    code: '10001',
                    message: '用户名或者密码为空',
                    result: ''
                }
    
                return
            }
    
            // 合理性验证
            // 需要再次查询数据库 getUserInfo
            if(await getUserInfo({user_name})) { // 根据用户名来查询，参数使用对象，这样可以让查询参数不受顺序影响
                ctx.status = 409 // 状态完成冲突，不熟悉的话，可以去MDN上看下常见状态码
                ctx.body = {
                    code: '10002',
                    message: '用户名已经存在',
                    result: ''
                }
                return 
            }
    
    
            const res = await createUser(user_name, password)
            console.log(res)
            ctx.body = {
                code: 0,
                message: '用户注册成功',
                result: {
                    id: res.id,
                    user_name: res.user_name
                }
            }
        }
    
        async login(ctx, next) {
            ctx.body = '用户登录成功'
        }
    }
    
    module.exports = new UserController()
    ```

  - `service`层中新增`getUserInfo`方法

    `user.service.js`

    ```js
    const User = require('../model/user.model')
    class UserService {
    
        async createUser(user_name, password) {
            const res = await User.create({ user_name, password })
            return res.dataValues
        }
    
        async getUserInfo({id, user_name, password, is_admin}) { // 参数设计成一个对象，因为查询用户，有可能根据id、user_name、password、is_admin字段去查询
            // 判断参数是否存在，拿到实参
            const  whereOpt = {}
            id && Object.assign(whereOpt, {id})
            user_name && Object.assign(whereOpt, {user_name})
            password && Object.assign(whereOpt, {password})
            is_admin && Object.assign(whereOpt, {is_admin})
    
            // 调用ORM查询接口：findOne，这是一个异步函数
            const res = User.findOne({
                attributes: ['id', 'user_name', 'password', 'is_admin'],
                where: whereOpt
            })
    
            return res ? res.dataValues : null
        }
    }
    
    module.exports = new UserService()
    ```

    测试下接口返回值

    选一个数据库中已经有的用户名进行测试

    ![image-20220727070845751](image-20220727070845751.png)

    后代打印的`sql`

    ![image-20220727070942651](image-20220727070942651.png)

### 错误处理函数封装

我们可以把格式的验证，单独封装成一个中间件（处理函数）

![image-20220727071500267](image-20220727071500267.png)

在`controller`层拆分中间件

新建`middleware/user.middleware.js`，中间件里定义各种函数，然后导出

`user.middleware.js`

从`controller`里把合法性验证的代码抽离出来

```js
const userValidator = async (ctx, next) => {
    const { user_name, password } = ctx.request.body

    if (!user_name || !password) {
        console.error('用户名或密码为空', ctx.request.body)
        ctx.status = 400
        ctx.body = {
            code: '10001',
            message: '用户名或者密码为空',
            result: ''
        }

        return // 校验没通过，直接返回
    }
    
    await next() // 校验通过了的话，就放行


}

module.exports = {
    userValidator
}
```

那么什么时候执行中间件呢？

在路由匹配的时候，只要路由一匹配上，就立刻调用校验的中间件

`user.route.js`

```js
const Router = require('@koa/router')
const router = new Router({ prefix: '/user' })
const { register, login } = require('../controller/user.conroller')
const { userValidator } = require('../middleware/user.middleware')
// 注册接口
router.post('/register', userValidator, register)
// 登录接口
router.post('/login', login)

module.exports = router

```

用`apifox`测试一下，可以正常打印错误日志

再抽离查询用户的代码（合理性验证）

`user.middleware.js`

```js
const { getUserInfo } = require('../service/user.service')

const userValidator = async (ctx, next) => {
    const { user_name, password } = ctx.request.body

    if (!user_name || !password) {
        console.error('用户名或密码为空', ctx.request.body)
        ctx.status = 400
        ctx.body = {
            code: '10001',
            message: '用户名或者密码为空',
            result: ''
        }
        return
    }
    
    await next() 
}

const verifyUser = async (ctx, next) => {
    const { user_name } = ctx.request.body
    if (getUserInfo({ user_name })) {
        ctx.status = 409
        ctx.body = {
            code: '10002',
            message: '用户名已经存在',
            result: ''
        }
        return
    }

    await next()
}

module.exports = {
    userValidator,
    verifyUser
}
```

`user.route.js`

```js
const Router = require('@koa/router')
const router = new Router({ prefix: '/user' })
const { register, login } = require('../controller/user.conroller')
const { userValidator, verifyUser } = require('../middleware/user.middleware')

// 注册接口
router.post('/register', userValidator, verifyUser, register)
// 登录接口
router.post('/login', login)

module.exports = router
```

测试下用户名已存在的情况，正常



至此，逻辑已经很清晰了，但我们还可以进一步管理**错误信息**

### 统一错误管理

在`koa`中，怎么进行错误管理呢？

- 中间件里提交错误类型

通过`ctx.app`可以拿到实例化的`koa`对象，它有一个`emit`方法用来提交错误，我们可以对此做一个检测

`ctx.app.emit('error', {}, ctx)`

- 该对象是自定义的错误类型，可以统一放在一个新的文件里管理

新建`src/constant`常量文件夹

新建`error.type.js`

```js
// 定义错误类型
module.exports = {
    userFormateError: {
        code: '10001',
        message: '用户名或者密码为空',
        result: ''
    },
    userAlreadyExists: {
        code: '10002',
        message: '用户名已经存在',
        result: ''
    }
}
```

修改`user.middle.js`

```js
const { getUserInfo } = require('../service/user.service')
const { userFormateError, userAlreadyExists } = require('../constant/error.type')

const userValidator = async (ctx, next) => {
    const { user_name, password } = ctx.request.body

    if (!user_name || !password) {
        console.error('用户名或密码为空', ctx.request.body)
        // ctx.status = 400
        ctx.app.emit('error', userFormateError, ctx) // 该对象是自定义的错误类型，可以统一放在一个新的文件里管理
        return
    }

    await next()

}

const verifyUser = async (ctx, next) => {
    const { user_name } = ctx.request.body

    if (getUserInfo({ user_name })) {
        // ctx.status = 409
        ctx.app.emit('error', userAlreadyExists, ctx)	
        return
    }

    await next()
}

module.exports = {
    userValidator,
    verifyUser
}
```

在`app/index.js`中统一进行错误处理

```js
const Koa = require('koa')
const Router = require('@koa/router')
const koaBody = require('koa-body')
const userRouter = require('../router/user.route')
const errHandler = require('./errorHandler')
const app = new Koa()

app.use(koaBody())
const indexRouter = new Router()
indexRouter.get('/', (ctx, next) => {   
    ctx.body = `Request Body: ${JSON.stringify(ctx.request.body)}`
})

app.use(indexRouter.routes())
app.use(userRouter.routes())


// 统一进行错误处理
// 发布订阅模式
app.on('error', errHandler)
module.exports = app

```

同级目录下，新建`errHandler.js`错误处理函数

`errHandler.js`

```js
module.exports = (err, ctx) => {
    let status = 500 // 默认错误状态码
    switch (err.code) {
        case '10001':
            status = 400
            break
        case '10002':
            status = 409
            break
        default:
            status = 500
    }

    ctx.status = status
    ctx.body = err
}
```



### 小问题

`verifyUser`中间件调用的`getUserInfo`返回的是一个`Promise`对象，恒为真，正常注册流程也走不下去了

`user.middleware.js`

```js
const verifyUser = async (ctx, next) => {
    const { user_name } = ctx.request.body

    if (getUserInfo({ user_name })) {
        ctx.app.emit('error', userAlreadyExists, ctx)
        return
    }

    await next()
}

```

修改

- 添加`await`，相当于判断条件是一个表达式

  ```js
  const verifyUser = async (ctx, next) => {
      const { user_name } = ctx.request.body
  
      if (await getUserInfo({ user_name })) {
          ctx.app.emit('error', userAlreadyExists, ctx)
          return
      }
  
      await next()
  }
  
  ```

  

另外假设中间件都没问题，到了控制层`createUser`这一步了，目前我们对这一步做任何的异常处理，使用`try-catch`来处理下

虽说这一步是`sequelize`自己操作的数据库，不大可能会出错，但为了代码的健壮性，还是要处理下的

`user.controller.js`

```js
const { createUser } = require('../service/user.service')
const { userRegisterError } = require('../constant/error.type')
class UserController {
    async register(ctx, next) {
        const { user_name, password } = ctx.request.body
		
        // 处理写入用户数据时，可能出现的异常
        try {
            const res = await createUser(user_name, password)
            console.log(res)
            ctx.body = {
                code: 0,
                message: '用户注册成功',
                result: {
                    id: res.id,
                    user_name: res.user_name
                }
            }
        } catch (err) {
            console.log(err)
            ctx.app.emit('error', userRegisterError, ctx)
			return // 发生错误就不要继续往下执行了
        }
    }

    async login(ctx, next) {
        ctx.body = '用户登录成功'
    }
}

module.exports = new UserController()
```

定义错误类型

`constant/error.type.js`

```js
// 定义错误类型
module.exports = {
    userFormateError: {
        code: '10001',
        message: '用户名或者密码为空',
        result: ''
    },
    userAlreadyExists: {
        code: '10002',
        message: '用户名已经存在',
        result: ''
    },
    userRegisterError: {
        code: '10003',
        message: '用户注册错误',
        result: ''
    }
}
```

我们在`createUser`方法中，模拟下写入数据库时发生了错误

`user.service.js`

```js
const User = require('../model/user.model')

class UserService {

    async createUser(user_name, password) {
        const res = await User.create({ user_name, password })
        console.log(aa) // 打印不存在的变量，模拟数据库操作错误
        return res.dataValues
    }

	// ...
}

module.exports = new UserService()
```

测试下

![image-20220728194137316](image-20220728194137316.png)



后台日志

![image-20220728194219755](image-20220728194219755.png)



建议调用`service`层所有的函数时，都加上错误处理

继续完善`verifyUser`

```js
const verifyUser = async (ctx, next) => {
    const { user_name } = ctx.request.body

    try {
        const res = await getUserInfo({ user_name })
        if (res) {
            console.error('用户名已存在', { user_name })
            ctx.app.emit('error', userAlreadyExists, ctx)
            return
        }
    } catch (err) {
        console.err('获取用户信息错误', err)
        ctx.app.emit('error', userQueryError, ctx)
        return 
    }

    await next()
}

```

`error.type.js`

```js
// 定义错误类型
module.exports = {
    userFormateError: {
        code: '10001',
        message: '用户名或者密码为空',
        result: ''
    },
    userAlreadyExists: {
        code: '10002',
        message: '用户名已经存在',
        result: ''
    },
    userRegisterError: {
        code: '10003',
        message: '用户注册错误',
        result: ''
    },
    userQueryError: {
        code: '10004',
        message: '用户查询错误',
        result: ''
    }
}
```

可以看到，真正要写代码的部分，其实是比较少的

很重要的一部分，在于提高代码的质量上，都在一些异常捕获和错误处理上，这一块是需要下功夫的，平时写代码的时候，要有这样的意识

这样当代码上线后，如果有问题，我们调试错误会很方便

`ctx.app.emit`提交的错误，最后会以接口的形式返回给客户端，如果服务器自己想记录错误信息，可以使用`console.error()`来记录日志信息



目前来说，这里还是有一个问题，就是重复注册直接走到了`register`，验证重复用户名的中间件直接就通过了！！

原因是`getUserInfo`函数里的`User.findOne`是一个异步函数，需要加一个`await`，否则会出错

```js
    async getUserInfo({id, user_name, password, is_admin}) {
        const  whereOpt = {}
        id && Object.assign(whereOpt, {id})
        user_name && Object.assign(whereOpt, {user_name})
        password && Object.assign(whereOpt, {password})
        is_admin && Object.assign(whereOpt, {is_admin})

        // 调用ORM查询接口：findOne，这是一个异步函数
        const res = await User.findOne({
            attributes: ['id', 'user_name', 'password', 'is_admin'],
            where: whereOpt
        })

        return res ? res.dataValues : null
    }
}
```

这样重复注册走到`verifyUser`中间件时，就不会被当做异常处理

### 加密

在将密码保存到数据库之前，要对密码进行加密处理

`md5`加密还是有可能被破解的，使用`bcrypt`加密

第一个依赖也多，这里我们使用第二个`bcryptjs`：在 JavaScript 中优化了 `bcrypt`，零依赖关系。

![image-20220729054812130](image-20220729054812130.png)

安装

```
npm i bcryptjs
```

用法：有同步和异步的用法：https://www.npmjs.com/package/bcryptjs

使用：

- 将代码加密功能，也抽离成一个中间件（单一职责原则）
  - 不想`bcrypt`这种加密方式，耦合到代码中
  - 后面有可能会换成其他加密方式：`hash`、`md5`

`user.middleware.js`

```js
const bcrypt = require('bcryptjs')

// ...
const scyptPassword = async (ctx, next) => {
    const { password } = ctx.request.body
    const salt =  bcrypt.genSaltSync(10); // 生成盐
    const hash = bcrypt.hashSync(password, salt); // 根据盐生成hash，hash保存的是密文
    ctx.request.body.password = hash // 使用hash覆盖password
    await next()
}


module.exports = {
    userValidator,
    verifyUser,
    scyptPassword
}
```

`user.route.js`导入并使用

测试注册接口成功后，查看`user`表`password`字段，已加密

![image-20220729060929127](image-20220729060929127.png)

仍存在的问题：密码在前端传给后端的过程中，是明文的，应该前端先加密，后端存储密文；而登录时，后面采用和前端一样的加密算法解密即可

### 小结：注册接口

梳理一下整理流程，及每个模块的功能

## 登录接口

`user.controller.js`

```js
    async login(ctx, next) {
        const { user_name } = ctx.request.body
        ctx.body = `欢迎回来，${user_name}`
    }
```

完善`apifox`

![image-20220729062050491](image-20220729062050491.png)

添加样例，应为数据库有已有的数据

![image-20220729062118325](image-20220729062118325.png)

![image-20220729062229643](image-20220729062229643.png)

但事实上，现在`login`对任何的输入都是可以的，我们需要对数据进行一个校验

- 是否为空（合法性校验）
  - 复用

- 是否存在（合理性校验）
  - 复用

- 验证登录

  `user.middleware.js`

  ```js
  const verifyLogin = async (ctx, next) => {
      // 1.判断用户是否存在（不存在：报错）
      const { user_name, password } = ctx.request.body
      try {
          const res = await getUserInfo({ user_name })
          if (!res) {
              console.log('用户不存在', res)
              return ctx.app.emit('error', userNotFound, ctx)
          }
          // 2.找到了用户，比对密码是否匹配（不匹配：报错）
          if (!bcrypt.compareSync(password, res.password)) {
              return ctx.app.emit('error', userInvalidPassword, ctx)
          }
      } catch (err) {
          console.error(err)
          return ctx.app.emit('error', userLoginFailed, ctx) // getUserInfo出错，在不同场景下，抛出的错误应该是不同的
      }
  
      //通过
      await next()
  
  }
  
  ```

- 登录成功后记录用户状态

  - 用户认证与授权




## 用户认证和授权

### 颁发`token`

登录成功后，给用户颁发一个令牌`token`，用户在以后的每一次请求中，携带这个令牌

前后端分离中，使用`jwt`：`json web token`

- `header`：头部
- `payload`：载荷
- `signature`：签名

如何使用

- 使用`jsonwebtoken`包：https://www.npmjs.com/package/jsonwebtoken

  - 安装：`npm i jsonwebtoken`
  - `sign`方法生成`token`

- `user.controller.js`

  ```js
  const jwt = require('jsonwebtoken')
  
  // ...
  
  class UserController {
      // ...
      
      async login(ctx, next) {
              const { user_name } = ctx.request.body
              // 获取用户信息（在paylaod中，记录id、user_name、is_admin）
              try {
                  // 从返回结果中，过滤掉password，将剩下的属性，放在新的res对象中
                  const { password, ...res } = await getUserInfo({ user_name })
                  ctx.body = {
                      code: 0,
                      message: '用户登录成功',
                      result: {
                          /*
                          * @params1:配置对象
                          * @params2:秘钥
                          * @params3:过期时间，一天
                          */
                          token: jwt.sign(res, JWT_SECRET, {expiresIn: '1d'})
                      }
                  }
  
              } catch (err) {
                  console.error('用户登录失败', err)
                  return
              }
      }
  }
  ```

  测试：

  ![image-20220730062107079](image-20220730062107079.png)

### 用户认证

我们新建一个修改密码的接口

![image-20220730063834013](/image-20220730063834013.png)

修改的操作

- `PUT`：全量修改
- `PATCH`：部分修改



写对应的路由

`user.route.js`

```js
const Router = require('@koa/router')
const router = new Router({ prefix: '/user' })
const { register, login } = require('../controller/user.conroller')
const { userValidator, verifyUser, scyptPassword, verifyLogin } = require('../middleware/user.middleware')

// 注册接口
router.post('/register', userValidator, verifyUser, scyptPassword, register)
// 登录接口
router.post('/login', userValidator,  verifyLogin, login)
// 修改密码接口
router.patch('/modifyPassword', (ctx, next) => {
    ctx.body = '修改密码成功'
})

module.exports = router

```

先简单测试下

我们在上面颁发`token`后，后续的请求（如修改密码）需要携带这个`token`

请求头新增`Authorization`，值一开始固定的是`Bearer `，有一个空格

![image-20220730082130815](image-20220730082130815.png)

后面发送请求时，需要加上签发的`token`



新建`auth.middleware.js`文件，将认证相关的验证放在这里面

```js
const jwt = require('jsonwebtoken')
const { JWT_SECRET } = require('../config/config.default')
const { tokenExpiredError, invalidToken} = require('../constant/error.type')
const auth = async (ctx, next) => {
    // 获取请求头的token
    const { authorization = 'Bearer ' } = ctx.request.header // 如果没带请求头，要给一个默认值
    const token = authorization.replace('Bearer ','') // 这里要有一个空格
    // 根据自定义私钥，使用jwt验证token
    console.log('token', token)
    try {
        // user中包含了payload的信息：user_name, id, is_admin
        const user = jwt.verify(token, JWT_SECRET) // 如果jwt.verify验证失败，会抛出一个异常
        // console.log('user', user)
        ctx.state.user = user
    } catch (err) {
        // console.log('err name', err.name)
        // jwt.verify异常情况有多种，可参照Npm文档 https://www.npmjs.com/package/jsonwebtoken
        switch (err.name) {
            case 'TokenExpiredError': // jwt返回的错误类型
                console.error('token已过期', err)
                ctx.app.emit('error', tokenExpiredError, ctx)
                return
            case 'JsonWebTokenError':
                console.error('无效的token', err)
                return ctx.app.emit('error', invalidToken, ctx)
            default:
                console.error('token错误', err)
                return
        }
    }

    await next()
}

module.exports = {
    auth
}
```

`error.type.js`

```js
// 定义错误类型
// 100 用户模块
// 101 授权模块
module.exports = {
	// ...
    tokenExpiredError: {
        code: '10101',
        message: 'token已过期',
        result: ''
    },
    invalidToken: {
        code: '10102',
        message: '无效的token',
        result: ''
    }
}
```

在路由上，加上`token`认证的中间件

`user.route.js`

```js
const Router = require('@koa/router')
const router = new Router({ prefix: '/user' })
const { register, login } = require('../controller/user.conroller')
const { userValidator, verifyUser, scyptPassword, verifyLogin } = require('../middleware/user.middleware')
const { auth } = require('../middleware/auth.middleware')
// 注册接口
router.post('/register', userValidator, verifyUser, scyptPassword, register)
// 登录接口
router.post('/login', userValidator, verifyLogin, login)
// 修改密码接口
router.patch('/modifyPassword', auth, (ctx, next) => { // 加上认证的中间件
    ctx.body = '修改密码成功'
})

module.exports = router

```

接口测试工具中，将登录成功后颁发的`token`，存为全局变量

![image-20220730172723345](image-20220730172723345.png)这样在修改密码的接口里，就可以不用复制`token`了

![image-20220730172826331](image-20220730172826331.png)

![image-20220730172900867](image-20220730172900867.png)

但这里有个不好的地方，我想测试下错误`token`的响应，是不支持修改的，测试的时候还是需要手动复制



正常接口返回的`user`

```bash
user {
  id: 46,
  user_name: 'sai',
  is_admin: false,
  iat: 1659173449,
  exp: 1659259849
}

```

测试无效的`token`

![image-20220730173957547](image-20220730173957547.png)



把`token`失效时间改为`5s`，测试过期`token`（记得测试完改回去）

重新登录后，测试下

![image-20220730174247201](image-20220730174247201.png)



#### 修改密码

测试没问题后，我们再加上加密的中间件，并正式写修改密码接口对应的处理函数

`user.route.js`

```js
// 修改密码接口
router.patch('/modifyPassword', auth, scyptPassword, modifyPassword)
```

`user.controller.js`

```js
const { createUser, getUserInfo, updateById } = require('../service/user.service')

// ...

async modifyPassword(ctx, next) {

        // 1. 获取数据
        const id = ctx.state.user.id
        const password = ctx.request.body.password

        try {
            // 2. 操作数据库
            const res = await updateById({ id, password })

            // 3. 返回结果
            if (res) {
                ctx.body = {
                    code: 0,
                    message: '修改密码成功',
                    result: ''
                }
            } else {
                ctx.app.emit('error', modifyPasswordFailed, ctx)

                return
            }
        } catch (err) {
            console.error('修改密码更新数据库失败', err)
            ctx.app.emit('error', modifyPasswordFailed, ctx)
            return
        }

        console.log(id, password)
    }
```

`user.service.js`

```js
    async updateById({ id, user_name, password, is_admin }) { // 接口的设计要考虑到复用性，不要这次只是根据id修改密码，就只写这一个功能
        const whereOpt = { id }
        const newUser = {}
        user_name && Object.assign(newUser, { user_name })
        password && Object.assign(newUser, { password })
        is_admin && Object.assign(newUser, { is_admin })

        const res = await User.update(newUser, {
            where: whereOpt
        })

        // console.log('res', res, typeof res) // 返回是一个数组
        return res[0] > 0 ? true : false

    }
```

小问题：入参为空对象时，应该做处理；修改密码还是原密码时，应该做处理



## 商品模块

### 整体流程打通

**路由**

新建`router/goods.route.js`

```js
const Router = require('@koa/router')
const router = new Router({ prefix: '/goods' })

const { upload } = require('../controller/goods.controller')


router.post('/upload', upload)

module.exports = router
```

**控制器**

新建`controller/goods/controller.js`

```js
class GoodsController {
    // 根据实际业务，可以写的很复杂，比如支持word、excel、图片等资源上传
    async upload(ctx, next) {
        ctx.body = '商品上传成功'
    }
}

module.exports = new GoodsController()
```

`app/index.js`	

```js
const Koa = require('koa')
const Router = require('@koa/router')
const koaBody = require('koa-body')
const userRouter = require('../router/user.route')
const goodsRouter = require('../router/goods.route')
const errHandler = require('./errHandler')
const app = new Koa()

app.use(koaBody())
app.use(userRouter.routes())
app.use(goodsRouter.routes())


// 统一进行错误处理
// 发布订阅模式
app.on('error', errHandler)
module.exports = app

```

**测试接口**

![image-20220730191605224](image-20220730191605224.png)

至此，整个流程已经打通

### 自动加载路由

上面我们在`app/index.js`注册路由时，需要手动一个个导入

可以使用`fs`模块实现自动导入

新建`router/index.js`

```js
const fs = require('fs')
const Router = require('@koa/router')
const router = new Router()

fs.readdirSync(__dirname).forEach(file => { // readdirSync方法，以同步的方式获取文件名
    // console.log(file) // 当前目录下的所有文件名
    if (file !== 'index.js') { // 过滤掉自身
        let r = require('./' + file) // 加载文件
        router.use(r.routes())
    }
})

module.exports = router
```

改写`app/index.js`

```js
const Koa = require('koa')
const koaBody = require('koa-body')
const router = require('../router') // 默认会找index.js
const errHandler = require('./errHandler')
const app = new Koa()

// use方法返回app自身
app
    .use(koaBody())
    .use(router.routes())
    .use(router.allowedMethods()) // 请求类型不支持的话，会更友好的响应
    .on('error', errHandler)

module.exports = app

```

`use(router.allowedMethods()) `，请求类型不支持的话，会更友好的响应

![image-20220730193114786](image-20220730193114786.png)

### 封装管理员权限

#### 准备工作

- 用户要登录
  - 先将`auth`中间件加上（认证）
- 还要有管理员权限
  - 然后再添加一个判断管理员权限的中间件（授权）

`goods.route.js`

```js
const Router = require('@koa/router')
const router = new Router({ prefix: '/goods' })

const { upload } = require('../controller/goods.controller')
const { auth, hasAdminPermission } = require('../middleware/auth.middleware')

router.post('/upload', auth, hasAdminPermission, upload)

module.exports = router
```

`auth.middleware.js`

```js
const { tokenExpiredError, invalidToken, hasNoAdminPermission } = require('../constant/error.type')

// ...
const hasAdminPermission = async (ctx, next) => {
    const { is_admin } = ctx.state.user
    if (!is_admin) {
        console.log('该用户无管理员权限', ctx.state.user)
        ctx.app.emit('error', hasNoAdminPermission, ctx)
        return
    }
    await next()
}
module.exports = {
    auth,
    hasAdminPermission
}
```

`error.type.js`

```js
// ...
    hasNoAdminPermission: {
        code: '10103',
        message: '无管理员权限',
        result:''
    }
```

然后注册`admin`用户，在数据库里`is_admin`字段的值改为`1`，接着用测试工具登录，然后测一下上传图片接口

#### 图片上传

`koa-body`是支持文件上传的（参数配置项，见`npm`）

- `multipart`配置项默认是`false`，要改成`true`
- `formidable`是一些关于文件上传的配置信息，`multipart`依赖`fomidabel`这个包
  - `uploadDir`：上传路径
  - `keepExtensions`：保持后缀名

- 会把上传成功的文件信息，挂载到`ctx.request.files`中

  - 可以上传多个文件

  - 上传时需要约定好的一个`key`，表示具体的某一个文件，这里约定为`file`

    ![image-20220731074001576](image-20220731074001576.png)

修改`app.index.js`

```js
const path = require('path')

const Koa = require('koa')
const koaBody = require('koa-body')

const router = require('../router') // 默认会找index.js
const errHandler = require('./errHandler')


const app = new Koa()
// use方法返回app自身
app
    .use(koaBody({
        multipart: true,
        formidable: {
            // 单独在src下新建一个upload文件夹，不推荐配置成../upload，这样的相对路径
            // 在option里相对路径不是相对于当前文件，是相对于proces.cwd()，指向当前脚本执行时所在的目录，可以打印一下
            // 使用node的path模块，写成绝对路径
            uploadDir: path.join(__dirname, '../upload'), 
            keepExtensions: true
        }
    }))
    .use(router.routes())
    .use(router.allowedMethods())
    .on('error', errHandler)

module.exports = app

```

我们在`upload`处理函数里，打印下文件信息

```js
class GoodsController {
    // 根据实际业务，可以写的很复杂，比如支持word、excel、图片等资源上传
    async upload(ctx, next) {
        console.log('file', ctx.request.files.file)
        ctx.body = '商品上传成功'
    }
}

module.exports = new GoodsController()
```

信息如下，有用的几个字段：`lastModifiedDate`、`mimetype`、`size`等

注意：不同版本的`koa-body`，里面的字段可能不一样，需要打印看下

```bash
file PersistentFile {
  _events: [Object: null prototype] { error: [Function (anonymous)] },
  _eventsCount: 1,
  _maxListeners: undefined,
  lastModifiedDate: 2022-07-30T23:43:02.773Z,
  filepath: 'D:\\workspace\\github\\code\\project-workshop\\code-prac\\koa\\01\\src\\upload\\8d12dbfca3833df9df3594700.png',
  newFilename: '8d12dbfca3833df9df3594700.png',
  originalFilename: 'blog.png',
  mimetype: 'image/png',
  hashAlgorithm: false,
  size: 257457,
  _writeStream: WriteStream {
    fd: null,
    path: 'D:\\workspace\\github\\code\\project-workshop\\code-prac\\koa\\01\\src\\upload\\8d12dbfca3833df9df3594700.png',
    flags: 'w',
    mode: 438,
    start: undefined,
    pos: undefined,
    bytesWritten: 257457,
    closed: false,
    _writableState: WritableState {
      objectMode: false,
      highWaterMark: 16384,
      finalCalled: false,
      needDrain: true,
      ending: true,
      ended: true,
      finished: true,
      destroyed: true,
      decodeStrings: true,
      defaultEncoding: 'utf8',
      length: 0,
      writing: false,
      corked: 0,
      sync: false,
      bufferProcessing: false,
      onwrite: [Function: bound onwrite],
      writecb: null,
      writelen: 0,
      afterWriteTickInfo: null,
      buffered: [],
      bufferedIndex: 0,
      allBuffers: true,
      allNoop: true,
      pendingcb: 0,
      constructed: true,
      prefinished: true,
      errorEmitted: false,
      emitClose: true,
      autoDestroy: true,
      errored: null,
      closed: false,
      closeEmitted: false,
      [Symbol(kOnFinished)]: []
    },
    _events: [Object: null prototype] { error: [Function (anonymous)] },
    _eventsCount: 1,
    _maxListeners: undefined,
    [Symbol(kFs)]: {
      appendFile: [Function: appendFile],
      appendFileSync: [Function: appendFileSync],
      access: [Function: access],
      accessSync: [Function: accessSync],
      chown: [Function: chown],
      chownSync: [Function: chownSync],
      chmod: [Function: chmod],
      chmodSync: [Function: chmodSync],
      close: [Function: close],
      closeSync: [Function: closeSync],
      copyFile: [Function: copyFile],
      copyFileSync: [Function: copyFileSync],
      cp: [Function: cp],
      cpSync: [Function: cpSync],
      createReadStream: [Function: createReadStream],
      createWriteStream: [Function: createWriteStream],
      exists: [Function: exists],
      existsSync: [Function: existsSync],
      fchown: [Function: fchown],
      fchownSync: [Function: fchownSync],
      fchmod: [Function: fchmod],
      fchmodSync: [Function: fchmodSync],
      fdatasync: [Function: fdatasync],
      fdatasyncSync: [Function: fdatasyncSync],
      fstat: [Function: fstat],
      fstatSync: [Function: fstatSync],
      fsync: [Function: fsync],
      fsyncSync: [Function: fsyncSync],
      ftruncate: [Function: ftruncate],
      ftruncateSync: [Function: ftruncateSync],
      futimes: [Function: futimes],
      futimesSync: [Function: futimesSync],
      lchown: [Function: lchown],
      lchownSync: [Function: lchownSync],
      lchmod: undefined,
      lchmodSync: undefined,
      link: [Function: link],
      linkSync: [Function: linkSync],
      lstat: [Function: lstat],
      lstatSync: [Function: lstatSync],
      lutimes: [Function: lutimes],
      lutimesSync: [Function: lutimesSync],
      mkdir: [Function: mkdir],
      mkdirSync: [Function: mkdirSync],
      mkdtemp: [Function: mkdtemp],
      mkdtempSync: [Function: mkdtempSync],
      open: [Function: open],
      openSync: [Function: openSync],
      opendir: [Function: opendir],
      opendirSync: [Function: opendirSync],
      readdir: [Function: readdir],
      readdirSync: [Function: readdirSync],
      read: [Function: read],
      readSync: [Function: readSync],
      readv: [Function: readv],
      readvSync: [Function: readvSync],
      readFile: [Function: readFile],
      readFileSync: [Function: readFileSync],
      readlink: [Function: readlink],
      readlinkSync: [Function: readlinkSync],
      realpath: [Function],
      realpathSync: [Function],
      rename: [Function: rename],
      renameSync: [Function: renameSync],
      rm: [Function: rm],
      rmSync: [Function: rmSync],
      rmdir: [Function: rmdir],
      rmdirSync: [Function: rmdirSync],
      stat: [Function: stat],
      statSync: [Function: statSync],
      symlink: [Function: symlink],
      symlinkSync: [Function: symlinkSync],
      truncate: [Function: truncate],
      truncateSync: [Function: truncateSync],
      unwatchFile: [Function: unwatchFile],
      unlink: [Function: unlink],
      unlinkSync: [Function: unlinkSync],
      utimes: [Function: utimes],
      utimesSync: [Function: utimesSync],
      watch: [Function: watch],
      watchFile: [Function: watchFile],
      writeFile: [Function: writeFile],
      writeFileSync: [Function: writeFileSync],
      write: [Function: write],
      writeSync: [Function: writeSync],
      writev: [Function: writev],
      writevSync: [Function: writevSync],
      Dir: [class Dir],
      Dirent: [class Dirent],
      Stats: [Function: Stats],
      ReadStream: [Getter/Setter],
      WriteStream: [Getter/Setter],
      FileReadStream: [Getter/Setter],
      FileWriteStream: [Getter/Setter],
      _toUnixTimestamp: [Function: toUnixTimestamp],
      F_OK: 0,
      R_OK: 4,
      W_OK: 2,
      X_OK: 1,
      constants: [Object: null prototype],
      promises: [Getter]
    },
    [Symbol(kIsPerformingIO)]: false,
    [Symbol(kCapture)]: false
  },
  hash: null,
  [Symbol(kCapture)]: false
}

```

完善`upload`处理函数

`goods.controller.js`

```js
const path = require('path')

const { fileUploadFailed } = require('../constant/error.type')

class GoodsController {
    async upload(ctx, next) {
        const { file } = ctx.request.files
        if (file) {
            ctx.body = {
                code: 0,
                message: '商品图片上传成功',
                result: {
                    goods_img: path.basename(file.filepath)
                }
            }
        } else {
            return ctx.app.emit('error', fileUploadFailed, ctx)
        }
    }
}

module.exports = new GoodsController()
```

`error.type.js`

每一种类型可以进一步携带`status`，这里没有做那么细

```js
// ...
    fileUploadFailed: {
        code: '10201',
        message: '商品图片上传失败',
        result:''
    }
```

测试：

![image-20220731075739871](image-20220731075739871.png)

#### 静态资源回显

现在我们希望对静态资源做一个回显，将某个目录设置成静态资源文件夹

安装`koa-static`

```
npm i koa-static
```

`app/index.js`中使用

```js
const path = require('path')

const Koa = require('koa')
const koaBody = require('koa-body')
const KoaStatic =  require('koa-static')

const router = require('../router') // 默认会找index.js
const errHandler = require('./errHandler')


const app = new Koa()
// use方法返回app自身
app
    .use(koaBody({
        multipart: true,
        formidable: {
            uploadDir: path.join(__dirname, '../upload'), 
            keepExtensions: true
        }
    }))
    .use(KoaStatic(path.join(__dirname, '../upload')))
    .use(router.routes())
    .use(router.allowedMethods())
    .on('error', errHandler)

module.exports = app

```

重启项目，可以通过`http://localhost:8000/4f791979542fe84e316506b00.png`访问静态资源（后面跟实际的文件名）

#### 前端实现上传图片

后面会讲到

- `form`表单
- `ajax`

#### 图片类型判断

不能在`upload`处理函数里面校验，走到这一步时图片已经上传了

下面的方式不建议

`goods.controller.js`

```js
    async upload(ctx, next) {
        const { file } = ctx.request.files
        console.log(file)
        const fileTypes = ['image/png', 'image/jpg', 'image/jpeg', 'image/webp']
        if (file) {
            if(!fileTypes.includes(file.mimetype)) {
                return ctx.app.emit('error', unSupportedFileType, ctx)
            }
            ctx.body = {
                code: 0,
                message: '商品图片上传成功',
                result: {
                    goods_img: path.basename(file.filepath)
                }
            }
        } else {
            return ctx.app.emit('error', fileUploadFailed, ctx)
        }
    }
```

`error.type.js`

```js
    unSupportedFileType: {
        code: '10202',
        message: '商品图不支持的文件类型',
        result:''
    }
```

测试接口上传`txt`文件

![image-20220731091404172](image-20220731091404172.png)



但我们看到，后台文件其实已经上传了

更好的方式失去配置`formidable`，但如果要统一错误处理，还需要写专门的中间件去返回错误类型



### 发布商品接口

> 路由

```js
POST /goods/release
```

> 请求参数

```js
goods_name, goods_price, goods_num, goods_img
```

> 响应

成功

```json
{
    "code": 0,
    "message": "发布商品成功",
    "result": {
        id: "",
        goods_name: "",
        goods_price: "",
        goods_img: "",
        goods_num: ""
    }
}
```

新增路由

`goods.route.js`

```js
const { upload, release } = require('../controller/goods.controller')


router.post('/release', auth, hasAdminPermission, release)
```



#### 参数格式校验

发布商品，除了需要认证、授权中间件，还需要参数格式校验的中间件

- 如果使用`ts`写的话，自带类型校验

新建`goods.middleware.js`

```js
const validator = async(ctx, next) => {

}

module.exports = {
    validator
}
```

之前写`user`模块的时候，我们是自己写的参数校验，不是说不好，实际写业务的时候，可以直接用社区里稳定的包

`koa-parameter`或者其它（先跟着教程里的来，这个库是5年前的，并且周下载量 不高了）https://www.npmjs.com/package/koa-parameter，是基于`parameter`这个库

安装

```js
npm i koa-parameter
```

在`app/index.js`中导入，并在路由注册之前，导入该中间件

```js
const path = require('path')

const Koa = require('koa')
const koaBody = require('koa-body')
const KoaStatic =  require('koa-static')
const parameter = require('koa-parameter') // 导入koa-parameter

const router = require('../router')
const errHandler = require('./errHandler')


const app = new Koa()
// use方法返回app自身
app
    .use(koaBody({
        multipart: true,
        formidable: {
            uploadDir: path.join(__dirname, '../upload'), 
            keepExtensions: true
        }
    }))
    .use(KoaStatic(path.join(__dirname, '../upload')))
    .use(parameter(app)) // 传入app实例，在app原型对象上添加校验的方法：verifyParams
    .use(router.routes())
    .use(router.allowedMethods())
    .on('error', errHandler)


module.exports = app

```

完善校验逻辑

`goods.middleware.js`

```js
const {goodsParamsError} = require('../constant/error.type')

const validator = async (ctx, next) => {
    try {
        ctx.verifyParams({
            goods_name: {type: 'string', required: true},
            goods_price: {type: 'number', required: true},
            goods_num: {type: 'number', required: true},
            goods_img: {type: 'string', required: true}
        })
    } catch (err) {
        console.error(err)
        // 把第三方的错误信息，传递到自定义的错误信息中，做一个统一
        goodsParamsError.result = err
        ctx.app.emit('error', goodsParamsError, ctx)
        return
    }

    await next()
}

module.exports = {
    validator
}
```

`error.type.js`

```js
    goodsParamsError: {
        code: '10203',
        message: '商品参数格式错误',
        result:''
    }
```

新建发布商品接口，并测试

我们将价格参数写成字符串，错误提示正确：

![image-20220801191725388](image-20220801191725388.png)

#### 发布商品写入数据库

`goods.controller.js`

```js
const path = require('path')

const { fileUploadFailed, unSupportedFileType, publishGoodsError } = require('../constant/error.type')
const {createGoods} = require('../service/goods.service')

class GoodsController {
    async upload(ctx, next) {
        const { file } = ctx.request.files
        console.log("file", file)
        const fileTypes = ['image/png', 'image/jpg', 'image/jpeg', 'image/webp']
        if (file) {
            if(!fileTypes.includes(file.mimetype)) {
                return ctx.app.emit('error', unSupportedFileType, ctx)
            }
            ctx.body = {
                code: 0,
                message: '商品图片上传成功',
                result: {
                    goods_img: path.basename(file.filepath)
                }
            }
        } else {

            return ctx.app.emit('error', fileUploadFailed, ctx)
        }
    }

    async release(ctx, next) {
        try {
            const {createdAt, updatedAt, ...res} = await createGoods(ctx.request.body)
            ctx.body = {
                code: 0,
                message: '发布商品成功',
                result: res
            }
        } catch(err) {
            console.error(err)
            return ctx.app.emit('error', publishGoodsError, ctx) // 不要把数据库相关的报错信息，暴露给前端
        }
    }
}

module.exports = new GoodsController()
```

`error.type.js`

```js
    publishGoodsError: {
        code: '10204',
        message: '商品发布失败',
        result:''  
    }
```

`goods.service.js`

```js
const Goods  = require('../model/goods.model') // 导入模型层时，不用解构赋值
class goodsService {
    async createGoods(goods) {
        const res = await Goods.create(goods)
        return res.dataValues
    }
}

module.exports = new goodsService()
```

`goods.model.js`

生成表结构后，记得注释掉`seq.sync()`

```js
const {DataTypes} = require('sequelize')

const seq = require('../db/seq')

const Goods = seq.define('sai_goods', {
    goods_name: {
        type: DataTypes.STRING,
        allowNull: false,
        comment: '商品名称'
    },
    goods_price: {
        type: DataTypes.DECIMAL(10, 2),
        allowNull: false,
        comment: '商品价格'
    },
    goods_num: {
        type: DataTypes.INTEGER,
        allowNull: false,
        comment: '商品库存'
    },
    goods_img: {
        type: DataTypes.STRING,
        allowNull: false,
        comment: '商品图片的url地址'
    }
})

// 创建表后注释掉
// Goods.sync({force: true})
module.exports = Goods
```

测试接口

![image-20220801195958558](image-20220801195958558.png)



### 修改商品接口

```
PUT /goods/modify/:id
```

> 请求参数

```
goods_name, goods_price, goods_num, goods_img
```

> 响应

成功

```json
{
    "code": 0,
    "message": "修改商品成功",
    "result": {
        "id": "",
        "goods_name": "",
        "goods_prcie": "",
        "goods_img": ""
    }
}
```

新建修改商品的测试接口

![image-20220802062718051](image-20220802062718051.png)

![image-20220802062725439](image-20220802062725439.png)

`goods.route.js`

```js
const Router = require('@koa/router')
const router = new Router({ prefix: '/goods' })

const { upload, release, update } = require('../controller/goods.controller')
const { auth, hasAdminPermission } = require('../middleware/auth.middleware')
const { validator } = require('../middleware/goods.middleware')
// 商品图片上传接口
router.post('/upload', auth, hasAdminPermission, upload)
// 发布商品接口
router.post('/release', auth, hasAdminPermission, validator, release)
// 修改商品接口
router.put('/update/:id',auth, hasAdminPermission, validator, update)
module.exports = router
```

`goods.controller.js`

```js
    async update(ctx, next) {
        try {
            const res = await updateGoods(ctx.params.id, ctx.request.body)
            if (res) {
                ctx.body = {
                    code: 0,
                    message: '修改商品成功',
                    result: ''
                }
            } else {
                return ctx.app.emit('error', invalidGoodsId, ctx)
            }
        } catch (err) {
            console.error(err)

            return ctx.app.emit('error', updateGoodsError, ctx)
        }
    }
```

`error.type.js`

```js
    invalidGoodsId: {
        code: '10205',
        message: '待修改的商品不存在',
        result:''  
    },
    updateGoodsError: {
        code: '10206',
        message: '更新商品失败',
        result:''  
    }
```

`goods.service.js`

```js
    async updateGoods(id, goods) {
        const res = await Goods.update(goods, { where: { id } }) // 这里的id记得加括号
        return res[0] > 0 ? true : false
    }
}
```

测试接口

成功：

![image-20220802062917097](image-20220802062917097.png)

失败：

![image-20220802062940954](image-20220802062940954.png)





### 删除商品接口

- 硬删除（直接从数据库中删除）
- 软删除（通过字段标识是否删除）

```
DELETE /goods/remove/:id
```

> 请求参数

```
无
```

> 响应

成功

```json
{
    "code": 0,
    "message": "删除商品成功",
    "result": ""
}
```





#### 硬删除

`goods.router.js`

```js
const Router = require('@koa/router')
const router = new Router({ prefix: '/goods' })

const { upload, release, update, remove } = require('../controller/goods.controller')
const { auth, hasAdminPermission } = require('../middleware/auth.middleware')
const { validator } = require('../middleware/goods.middleware')
// 商品图片上传接口
router.post('/upload', auth, hasAdminPermission, upload)
// 发布商品接口
router.post('/release', auth, hasAdminPermission, validator, release)
// 修改商品接口
router.put('/update/:id',auth, hasAdminPermission, validator, update)
// 删除接口
router.delete('/remove/:id', auth, hasAdminPermission, remove)
module.exports = router
```

`goods.controller.js`

```js
    async remove(ctx, next) {
        await removeGoods(ctx.params.id)
        ctx.body = {
            code: 0,
            message: '商品删除成功',
            result: ''
        }
    }
```

`goods.service.js`

```js
    async removeGoods(id) {
        const res = await Goods.destroy({ where: { id } })
        return res[0] > 0 ? true : false
    }
}
```



#### 软删除

> 扩展

可以做成上下架的状态，考虑加一个状态字段，删除商品做成下架，下架商品更新字段值

 一般不会硬删除的

修改`goods.model.js`

`define`函数新增第三个参数，然后取消`sync`注释重新创建表

```js
const {DataTypes} = require('sequelize')

const seq = require('../db/seq')

const Goods = seq.define('sai_goods', { 
    goods_name: {
        type: DataTypes.STRING,
        allowNull: false,
        comment: '商品名称'
    },
    goods_price: {
        type: DataTypes.DECIMAL(10, 2),
        allowNull: false,
        comment: '商品价格'
    },
    goods_num: {
        type: DataTypes.INTEGER,
        allowNull: false,
        comment: '商品库存'
    },
    goods_img: {
        type: DataTypes.STRING,
        allowNull: false,
        comment: '商品图片的url地址'
    }
}, {
    paranoid: true
})

// 创建表后注释掉
Goods.sync({force: true})
module.exports = Goods
```

重新执行后，商品表会多一个字段，删除时会更新一个时间戳，表示删除

![image-20220802215458234](image-20220802215458234.png)

将硬删除改为软删除接口

`goods.router.js`

```js
// 下架商品，注意改成了post方法
router.post('/remove/:id/off', auth, hasAdminPermission, remove)
```

新建软删除测试接口，`deleteAt`字段有值，表示下架

![image-20220802220330688](image-20220802220330688.png)

调通后，完善错误处理

`goods.controller.js`

```js
const { fileUploadFailed, unSupportedFileType, publishGoodsError, invalidGoodsId } = require('../constant/error.type')


	async remove(ctx, next) {
        const res = await removeGoods(ctx.params.id)
        if(res) {
            ctx.body = {
                code: 0,
                message: '商品下架成功',
                result: ''
            }
        } else {
            return ctx.app.emit('error', invalidGoodsId, ctx)
        }
    }
```

`goods.service.js`

```js
    async removeGoods(id) {
        const res = await Goods.destroy({ where: { id } }) // destroy的返回值，不是数组
        return res > 0 ? true : false // 返回值为0或1
    }
```

测试下架商品接口，

对于重复下架、下架不存在的商品，给出错误提示

![image-20220802221044222](image-20220802221044222.png)



**上架接口**

`goods.router.js`

```js
// 上架商品
router.post('/remove/:id/on', auth, hasAdminPermission, restore)
```

`goods.controller.js`

```js
	async restore(ctx, next) {
        const res = await restoreGoods(ctx.params.id)
        if (res) {
            ctx.body = {
                code: 0,
                message: '商品上架成功',
                result: ''
            }
        } else {
            return ctx.app.emit('error', invalidGoodsId, ctx)
        }
    }
```

`goods.service.js`

```js
    async restoreGoods(id) {
        const res = await Goods.restore({ where: { id } })
        return res > 0 ? true : false
    }
```

测试上架接口，

对于重复上架、上架不存在的商品，给出错误提示

![image-20220802221044222](image-20220802221044222.png)

### 商品列表接口

```
GET/goods
```

> 请求参数

```
pageNum(default=1)
pageSize(default=10)
```

> 响应

成功

```json
{
    "code": 0,
    "message": "获取商品成功",
    "result": {
        "pageNum": 1,
        "pageSize": 10, 
		"total": 2,
        "list": [
 			{
            	"id": 1,
            	"goods_name": "",
            	"goods_price": "",
                "goods_img": ""
            },
        	{
            	"id": 2,
            	"goods_name": "",
            	"goods_price": "",
                "goods_img": ""
            }, 
        ]
    }
}
```

`goods.route.js`

```js
// 获取商品列表
router.get('/lists', findAll)

```

`goods.controller.js`

```js
    async findAll(ctx, next) {
        try {
            console.log(ctx.params.query)

            const { pageNum = 1, pageSize = 10 } = ctx.request.query
            const res = await findGoods(pageNum, pageSize)
            ctx.body = {
                code: 0,
                message: '获取商品列表成功',
                result: res
            }
        } catch(err) {
            console.error(err)
        }
    }
```

`goods.service.js`

```js
async findGoods(pageNum, pageSize) {
        // 获取表记录数
        const count = await Goods.count() // count()和findAll()将看不到软删除的记录

        // 获取分页具体数据
        const offset = (pageNum - 1) * pageSize
        const rows = await Goods.findAll({ offset, limit: pageSize * 1 })

        // 返回字段对应接口文档
        return {
            pageNum,
            pageSize,
            total: count,
            list: rows
        }

    }
```

![image-20220803203126192](image-20220803203126192.png)

这个接口还是有很多问题的，如参数校验、异常处理等

## 购物车模块

### 添加购物车

```
POST /carts
```

> 请求参数

```
goods_id
```

- 计算登录用户的`user_id`	
  - 如果该用户下的`goods_id`不存在，新建一条记录
  - 如果该用户下的`goods_id`已存在，更新数量+1

> 响应



**购物车表**

表名：`sai_carts`

| 字段名   | 字段类型 | 说明               |
| -------- | -------- | ------------------ |
| id       | int      | 主键，自增         |
| goods_id | int      | 商品id             |
| user_id  | int      | 用户id             |
| number   | int      | 数量               |
| selected | tinyint  | 0：没选中；1：选中 |

`cart.route.js`

```js
const Router = require('@koa/router')
const router = new Router({ prefix: '/carts' })
const { validator } = require('../middleware/cart.middleware')
const { auth } = require('../middleware/auth.middleware')
const { add } = require('../controller/cart.controller')


router.post('/', auth, validator, add)

module.exports = router

```

`cart.controller.js`

```js
const {createOrUpdate} = require('../service/cart.service')

class CartController {
    async add(ctx, next) {
        try {
            const user_id = ctx.state.user.id
            const goods_id = ctx.request.body.goods_id
    
            const res  = await createOrUpdate(user_id, goods_id)
            ctx.body = {
                code: 0,
                message: '添加到购物车成功',
                result: res
            }
        } catch(err) {
            console.error(err)
        }
    }
}

module.exports = new CartController()
```

`cart.service.js`

```js
const Cart = require('../model/cart.model')
const {Op} = require('sequelize') // 要以解构赋值的形式导入


class CartService {
    async createOrUpdate(user_id, goods_id) {
        // 根据user_id和goods_id同时查找
        const res = await Cart.findOne({
            [Op.and]: {
                user_id,
                goods_id
            }
        })

        // 已经存在一条记录，将number + 1
        if(res) {
            await res.increment('number')
            return await res.reload()
        } else {
            return await Cart.create({
                user_id,
                goods_id
            })
        }
    }
}

module.exports = new CartService()
```

`cart.model.js`

```js
const seq = require('../db/seq')
const {DataTypes} = require('sequelize')

const Cart = seq.define('sai_carts', {
    goods_id: {
        type: DataTypes.INTEGER,
        allowNull: false,
        comment: '商品的id'
    },
    user_id: {
        type: DataTypes.INTEGER,
        allowNull: false,
        comment: '用户的id'
    },
    number: {
        type: DataTypes.INTEGER,
        allowNull: false,
        defaultValue: 1,
        comment: '商品的数量'
    },
    selected: {
        type: DataTypes.BOOLEAN,
        allowNull: false,
        defaultValue: true,
        comment: '是否选中'
    }
})

// Cart.sync({force: true})

module.exports = Cart
```

小问题：这里=我们没有对`goods_id`是否存在做校验，并且已经下架的商品是不能够进行操作的



要做一个真实的、可以商用的接口，不是那么简单的，会有很多的细节要考虑

### 获取购物车列表

```
GET /carts
```

> 请求参数

```
pageNum(default=1)
pageSize(default=10)
```

> 响应

成功

```json
{
    "code": 0,
    "message": "获取购物车列表成功",
    "result": {
        "pageNum": 1,
        "pageSize": 10,
        "total": 2,
        "list": [
            {
                "id": 1,
                "goods_info": {
                    "id": 2,
                    "goods_name": "蓝牙耳机",
                    "goods_price": 199.00,
                    "goods_img": "./32048091210.jpg"
                },
                "number": 1,
                "selected": 1
            },
            {
                "id": 2,
                "goods_info": {
                    "id": 2,
                    "goods_name": "蓝牙耳机",
                    "goods_price": 199.00,
                    "goods_img": "./32048091210.jpg"
                },
                "number": 1,
                "selected": 1
            }
        ]
    }
}
```

表关联：https://www.sequelize.com.cn/core-concepts/assocs

`cart.route.js`

```js
router.get('/', auth, findAll)
```

`cart.controller.js`

```js
    async findAll(ctx, next) {
        const {pageNum = 1, pageSize = 10} = ctx.request.query
        const res = await findCarts(pageNum, pageSize)
        ctx.body = {
            code: 0,
            message: '获取购物车列表成功',
            result: res
        }
    }
```

`cart.service.js`

```js
    async findCarts(pageNum, pageSize) {
        const offset = (pageNum - 1) * pageSize
        const { count, rows } = await Cart.findAndCountAll({
            attributes: ['id', 'number', 'selected'], // 指定需要查找的字段
            offset: offset,
            limit: pageSize * 1
        })
        return {
            pageNum,
            pageSize,
            total: count,
            list: rows
        }
    }
```

添加几件商品到购物车后，测试获取购物车列表的接口：

```json
{
    "code": 0,
    "message": "获取购物车列表成功",
    "result": {
        "pageNum": "1",
        "pageSize": "10",
        "total": 4,
        "list": [
            {
                "id": 1,
                "number": 4,
                "selected": true
            },
            {
                "id": 3,
                "number": 1,
                "selected": true
            },
            {
                "id": 4,
                "number": 2,
                "selected": true
            },
            {
                "id": 5,
                "number": 2,
                "selected": true
            }
        ]
    }
}
```

现在需要做一个联表查询，查询具体的商品信息

现在是`cart`表要关联`goods`表（根据`cart`表里的`goods_id`去`goods`表里查询）

`cart.model.js`

```js
const seq = require('../db/seq')
const {DataTypes} = require('sequelize')
const Goods = require('./goods.model') // 导入Goods模型


const Cart = seq.define('sai_carts', {
	// ...
})

// Cart.sync({force: true})
Cart.belongsTo(Goods, {
    foreignKey: 'goods_id',
    as: 'goods_info'
}) // 外键在Cart表里用belongsTo，否则用hasOne


module.exports = Cart
```

`cart.service.js`

```js
const Goods = require('../model/goods.model')

// ...
	async findCarts(pageNum, pageSize) {
        const offset = (pageNum - 1) * pageSize
        const { count, rows } = await Cart.findAndCountAll({
            attributes: ['id', 'number', 'selected'],
            offset: offset,
            limit: pageSize * 1,
            include: {
                model: Goods,
                as: 'goods_info', // 指定查询结构的别名，和接口文档的字段保持一致
                attributes: ['id', 'goods_name', 'goods_price', 'goods_img'] // 这里的先后顺序，会反映到接口中的字段顺序
            }
        })
        return {
            pageNum,
            pageSize,
            total: count,
            list: rows
        }
    }
```

测试接口：

```json
{
    "code": 0,
    "message": "获取购物车列表成功",
    "result": {
        "pageNum": "1",
        "pageSize": "10",
        "total": 4,
        "list": [
            {
                "id": 1,
                "number": 4,
                "selected": true,
                "goods_info": {
                    "id": 3,
                    "goods_name": "证断影然度叫",
                    "goods_img": "http://dummyimage.com/400x400",
                    "goods_price": "53.00"
                }
            },
            {
                "id": 3,
                "number": 1,
                "selected": true,
                "goods_info": {
                    "id": 2,
                    "goods_name": "酸这争取",
                    "goods_img": "http://dummyimage.com/400x400",
                    "goods_price": "13.00"
                }
            },
            {
                "id": 4,
                "number": 2,
                "selected": true,
                "goods_info": {
                    "id": 3,
                    "goods_name": "证断影然度叫",
                    "goods_img": "http://dummyimage.com/400x400",
                    "goods_price": "53.00"
                }
            },
            {
                "id": 5,
                "number": 2,
                "selected": true,
                "goods_info": {
                    "id": 2,
                    "goods_name": "酸这争取",
                    "goods_img": "http://dummyimage.com/400x400",
                    "goods_price": "13.00"
                }
            }
        ]
    }
}
```

如果自己写`SQL`也可以，可以用`LEFT OUTER JOIN`做联表查询

```sql
SELECT `sai_carts`.`id`, `sai_carts`.`number`, `sai_carts`.`selected`, `goods_info`.`id` AS `goods_info.id`, `goods_info`.`goods_name` AS `goods_info.goods_name`, `goods_info`.`goods_img` AS `goods_info.goods_img`, `goods_info`.`goods_price` AS `goods_info.goods_price` FROM `sai_carts` AS `sai_carts` LEFT OUTER JOIN `sai_goods` AS `goods_info` ON `sai_carts`.`goods_id` = `goods_info`.`id` AND (`goods_info`.`deletedAt` IS NULL) LIMIT 0, 10;
```

一个接口把前端想要的所有信息都返回，避免两次网络请求（否则将根据`goods_id`又重新发送请求获取商品信息）

要多看看`sequelize`官方文档



### 更新购物车

通过更新接口可以修改购物车中商品的选中状态和数量

```
PATCH /carts/:id
```

> 请求参数

```
number, selected
```

>  响应

成功

```json
{
    "code": 0,
    "message": "获取购物车列表成功",
    "result": {
        "pageNum": 1,
        "pageSize": 10,
        "total": 2,
        "list": [
            {
                "id": 1,
                "goods_info": {
                    "id": 2,
                    "goods_name": "蓝牙耳机",
                    "goods_price": 199.00,
                    "goods_img": "./32048091210.jpg"
                },
                "number": 1,
                "selected": 1
            },
            {
                "id": 2,
                "goods_info": {
                    "id": 2,
                    "goods_name": "蓝牙耳机",
                    "goods_price": 199.00,
                    "goods_img": "./32048091210.jpg"
                },
                "number": 1,
                "selected": 1
            }
        ]
    }
}
```

`cart.route.js`

```js
// 更新购物车
router.patch(
    '/:id',
    auth,
    validator({
        number: { type: 'number', required: false },
        selected: { type: 'bool',   required: false }
    }),
    update
)
```

`cart.controller.js`

```js
 	async update(ctx, next) {
        // 解析参数
        const { id } = ctx.request.params
        const { number, selected } = ctx.request.body

        // 参数判断
        if (number === undefined && selected === undefined) {
            cartFormatError.message = 'number和selected不能同时为空'
            return ctx.app.emit('error', cartFormatError, ctx)
        }

        // 操作数据库
        const res = await updateCarts({ id, number, selected })

        ctx.body = {
            code: 0,
            message: '更新购物车成功',
            result: res
        }
    }
```

`error.type.js`

```js
    cartFormatError: {
        code: '10301',
        message: '购物车数据格式错误',
        result: ''

    }
```

`cart.service.js`

```js
    async updateCarts(params) {
        const { id, number, selected } = params

        const res = await Cart.findByPk(id)
        if(!res) return ''
        number !== undefined ? (res.number =  number) : ''
        selected !== undefined ? (res.selected = selected) : ''

        return await res.save()

    }
```

### 刪除购物车

```
DELETE /carts
```

> 请求参数

```json
{
    "ids": [1, 2, 3]
}
```

> 响应

成功

```json
{
    "code": 0,
    "message": "获取购物车列表成功",
    "result": {
        "pageNum": 1,
        "pageSize": 10,
        "total": 2,
        "list": [
            {
                "id": 1,
                "goods_info": {
                    "id": 2,
                    "goods_name": "蓝牙耳机",
                    "goods_price": 199.00,
                    "goods_img": "./32048091210.jpg"
                },
                "number": 1,
                "selected": 1
            },
            {
                "id": 2,
                "goods_info": {
                    "id": 2,
                    "goods_name": "蓝牙耳机",
                    "goods_price": 199.00,
                    "goods_img": "./32048091210.jpg"
                },
                "number": 1,
                "selected": 1
            }
        ]
    }
}
```

`cart.route.js`

```js
// 删除购物车，默认delete、get、head请求方法下,koa-body不会把请求体放到ctx.body中，需要在koa-body中开启：parsedMethods: ['POST', 'PUT', 'PATCH', 'DELETE']
router.delete('/', auth, validator({ ids: 'array' }), remove)

```

`app.index.js`

```js
// ...
const app = new Koa()
app
    .use(koaBody({
        multipart: true,
        formidable: {

            uploadDir: path.join(__dirname, '../upload'), 
            keepExtensions: true
        },
        parsedMethods: ['POST', 'PUT', 'PATCH', 'DELETE'] // 让其支持DELETE方法下，也写入body参数
    }))
    .use(KoaStatic(path.join(__dirname, '../upload')))
    .use(parameter(app))
    .use(router.routes())
    .use(router.allowedMethods())
    .on('error', errHandler)


module.exports = app

```

`cart.controller.js`

```js
async remove(ctx, next) {
        try {
            const { ids } = ctx.request.body
            console.log(ids)
            const res = await removeCarts(ids)

            ctx.body = {
                code: 0,
                message: '删除购物车成功',
                result: res
            }
        } catch (err) {
            console.error(err)
        }
    }
```

`cart.service.js`

```js
async removeCarts(ids) {
        return await Cart.destroy({
            where: {
                id: {
                    [Op.in]: ids
                }
            }
        })
    }
```



### 全选中接口

```
POST /carts/selectAll
```

> 请求参数

无

> 响应

成功

```json
{
    "code": 0,
    "message": "获取购物车列表成功",
    "result": {
        "pageNum": 1,
        "pageSize": 10,
        "total": 2,
        "list": [
            {
                "id": 1,
                "goods_info": {
                    "id": 2,
                    "goods_name": "蓝牙耳机",
                    "goods_price": 199.00,
                    "goods_img": "./32048091210.jpg"
                },
                "number": 1,
                "selected": 1
            },
            {
                "id": 2,
                "goods_info": {
                    "id": 2,
                    "goods_name": "蓝牙耳机",
                    "goods_price": 199.00,
                    "goods_img": "./32048091210.jpg"
                },
                "number": 1,
                "selected": 1
            }
        ]
    }
}
```



### 全不选中接口

```
POST /carts/unSelectAll
```

> 请求参数

无

> 响应

成功

```json
{
    "code": 0,
    "message": "获取购物车列表成功",
    "result": {
        "pageNum": 1,
        "pageSize": 10,
        "total": 2,
        "list": [
            {
                "id": 1,
                "goods_info": {
                    "id": 2,
                    "goods_name": "蓝牙耳机",
                    "goods_price": 199.00,
                    "goods_img": "./32048091210.jpg"
                },
                "number": 1,
                "selected": 1
            },
            {
                "id": 2,
                "goods_info": {
                    "id": 2,
                    "goods_name": "蓝牙耳机",
                    "goods_price": 199.00,
                    "goods_img": "./32048091210.jpg"
                },
                "number": 1,
                "selected": 1
            }
        ]
    }
}
```



`cart.route.js`

```js
// 全选 和 全部不选 ，其实可以合并起来写
router.post('/selectAll', auth, selectAll)
router.post('/unselectAll', auth, unSelectAll)

```

`cart.controller.js`

```js
async selectAll(ctx, next) {
        try {
            const user_id = ctx.state.user.id
            const res = await selectAllCarts(user_id)

            ctx.body = {
                code: 0,
                message: '全部选中',
                result: res
            }
        } catch (err) {
            console.error(err)
        }
    }

    async unSelectAll(ctx, next) {
        const user_id = ctx.state.user.id

        const res = await unSelectAllCarts(user_id)

        ctx.body = {
            code: 0,
            message: '全不选',
            result: res
        }
    }
```

`cart.service.js`

```js
 	async selectAllCarts(user_id) {
        return await Cart.update({ selected: true }, {
            where: {
                user_id
            }
        })
    }

    async unSelectAllCarts(user_id) {
        return await Cart.update({ selected: false }, {
            where: {
                user_id
            }
        })
    }
```

### 获取购物车商品总数量接口

```
GET /carts/total
```

> 请求参数

无

> 响应

成功

```json
{
    "code": 0,
    "message": "获取购物车商品数量成功",
    "result": {
        "total": 10
    }
}
```



这个接口可以不写，直接在前端计算显示

## 地址模块

### 添加地址接口

这里我们做一下限制，假设只支持3个地址

```
POST /address
```

> 请求参数

```
consignee, phone, address
```

> 响应

成功

```json
{
    "code": 0,
    "message": "添加地址成功",
    "result": {
        
    }
}
```



地址表

表名：`sai_address`

| 字段名     | 字段类型     | 说明                     |
| ---------- | ------------ | ------------------------ |
| id         | int          | 主键，自增               |
| user_id    | int          | 用户id                   |
| consignee  | varchar(255) | 收货人                   |
| phone      | char(11)     | 手机号                   |
| address    | varchar(255) | 收货地址                 |
| is_default | tinyint      | 0：不是默认，1：默认地址 |

`address.route.js`

```js
const Router = require('@koa/router')
const router = new Router({ prefix: '/address' })

const { auth } = require('../middleware/auth.middleware')
const { validator } = require('../middleware/address.middleware')
const {create} = require('../controller/address.controller')


router.post('/', auth, validator({
    consignee: 'string',
    phone: { type: 'string', format: /^1\d{10}$/ }, // 简单的手机号正则
    address: 'string'
}), create)


module.exports = router


```

`address.middleware.js`

```js
const { addressFormatError } = require('../constant/error.type')

const validator = (rules) => {
    return async (ctx, next) => {
        try {
            await ctx.verifyParams(rules)
        } catch (err) {
            console.error(err)
            addressFormatError.result = err
            ctx.app.emit('error', addressFormatError, ctx)
            return
        }

        await next()
    }
}

module.exports = {
    validator
}
```

不同模块的参数校验中间件，可以进一步封装的

`address.controller.js`

```js
const {createAddr} = require('../service/address.service')

class AddressController {
    async create(ctx, next) {
        const user_id = ctx.state.user.id
        const { consignee, phone, address } = ctx.request.body

        const res = await createAddr({user_id, consignee, phone, address})

        ctx.body = {
            code: 0,
            message: '添加地址成功',
            result: res
        }
    }
}

module.exports = new AddressController()
```

`address.service.js`

```js
const Address = require('../model/address.model')

class AddressService {
    async createAddr(addr) {
        return await Address.create(addr)
    }
}

module.exports = new AddressService()
```

`address.model.js`

```js
const seq = require('../db/seq')
const {DataTypes} = require('sequelize')

const Address = seq.define('sai_address', {
    user_id: {
        type: DataTypes.INTEGER,
        allowNull: false,
        comment: '用户id'
    },
    consignee: {
        type: DataTypes.STRING,
        allowNull: false,
        comment: '收货人姓名'
    },
    phone: {
        type: DataTypes.CHAR(11),
        allowNull: false,
        comment: '收货人手机号'
    },
    address: {
        type: DataTypes.STRING,
        allowNull: false,
        comment: '收货人地址'
    },
    is_default: {
        type: DataTypes.BOOLEAN,
        allowNull: false,
        defaultValue: false,
        comment: '是否为默认地址，0：不是，1：是'
    }
})

// Address.sync({force: true})

module.exports = Address
```



### 获取地址列表接口

```
GET /address
```

> 请求 参数

无

> 响应

成功

```json
{
    "code": 0,
    "message": "获取列表成功",
    "result": [
        {
            "id": 1,
            "consignee": "enim Duis id",
            "phone": "18167553843",
            "address": "澳门特别行政区贵港市滨湖区"
        },
        {
            "id": 2,
            "consignee": "nisi ullamco",
            "phone": "13157913140",
            "address": "陕西省揭阳市玛多县"
        }
    ]
}
```

`address.route.js`

```js
// 获取地址
router.get('/', auth, findAll)
```

`address.controller.js`

```js
   async findAll(ctx, next) {
        const user_id = ctx.state.user.id

        // const { user_id: uid, createdAt, updatedAt, ...res } = await findAllAddr(user_id) // 返回的是数组，过滤属性可以在service层
        const res = await findAllAddr(user_id)

        ctx.body = {
            code: 0,
            message: '获取地址成功',
            result: res
        }
    }
```

`address.service.js`

```js
    async findAllAddr(user_id) {
        return await Address.findAll({
            attributes: ['id', 'consignee', 'phone', 'address', 'is_default'],
            where: { user_id }
        })
    }
```

正确响应：

```json
{
    "code": 0,
    "message": "获取地址成功",
    "result": [
        {
            "id": 1,
            "consignee": "enim Duis id",
            "phone": "18167553843",
            "address": "澳门特别行政区贵港市滨湖区",
            "is_default": false
        },
        {
            "id": 2,
            "consignee": "commodo adipisicing officia",
            "phone": "18661881741",
            "address": "安徽省广元市青神县",
            "is_default": false
        },
        {
            "id": 3,
            "consignee": "nisi ullamco",
            "phone": "13157913140",
            "address": "陕西省揭阳市玛多县",
            "is_default": false
        }
    ]
}
```





### 修改地址接口

```
PUT /address/:id
```

> 请求参数

```
consignee, phone, address
```

> 响应

成功

```json
{
    "code": 0,
    "message": "修改列表成功",
    "result": [
        {
            "id": 1,
            "consignee": "enim Duis id",
            "phone": "18167553843",
            "address": "澳门特别行政区贵港市滨湖区"
        },
        {
            "id": 2,
            "consignee": "nisi ullamco",
            "phone": "13157913140",
            "address": "陕西省揭阳市玛多县"
        }
    ]
}
```

`address.route.js`

```js
// 修改地址
router.put('/:id', auth, validator({
    consignee: 'string',
    phone: { type: 'string', format: /^1\d{10}$/ },
    address: 'string'
}), update)

```

`address.controller.js`

```js
    async update(ctx, next) {
        const id = ctx.request.params.id

        const res = await updateAddr(id, ctx.request.body)

        ctx.body = {
            code: 0,
            message: '更新地址成功',
            result: res
        }
    }
```

`address.service.js`

```js
    async updateAddr(id, addr) {
        return await Address.update(addr, { where: { id } })
    }
```

正确响应

```json
{
    "code": 0,
    "message": "更新地址成功",
    "result": [
        1
    ]
}
```

如果修改后的地址需要回填，就需要进一步完善

### 删除接口

```
DELETE /address/:id
```

> 请求参数

```
无
```

> 响应

```json
{
    "code": 0,
    "message": "获取列表成功",
    "result": [
        {
            "id": 1,
            "consignee": "enim Duis id",
            "phone": "18167553843",
            "address": "澳门特别行政区贵港市滨湖区"
        },
        {
            "id": 2,
            "consignee": "nisi ullamco",
            "phone": "13157913140",
            "address": "陕西省揭阳市玛多县"
        }
    ]
}
```

`address.route.js`

```js
// 删除地址
router.delete('/:id', auth, remove)

```

`address.controller.js`

```js
	async remove(ctx, next) {
        const id = ctx.request.params.id

        const res = await removeAddr(id)
        
        ctx.body = {
            code: 0,
            message: '删除地址成功',
            result: res
        }
    }
```

`address.service.js`

```js
    async removeAddr(id) {
        return await Address.destroy({ where: { id } })
    }
```

成功响应

```json
{
    "code": 0,
    "message": "删除地址成功",
    "result": 1
}
```

### 设为默认接口

```
PATCH /address/:id
```

> 请求参数

```
无
```

`address.route.js`

```js
// 删除地址
router.delete('/:id', auth, remove)
```

`address.controller.js`

```js
	async setDefault(ctx, next) {
        const user_id = ctx.state.user.id
        const id = ctx.request.params.id

        const res = await setDefaultAddr(user_id, id)

        ctx.body = {
            code: 0,
            message: '设置默认地址成功',
            result: res
        }
    }
```

`address.service.js`

```js
    async setDefaultAddr(user_id, id) {
        // 先把所有的地址都设置为非默认
        await Address.update( 
            { is_default: false },
            {
                where: { user_id }
            }
        )
        // 再根据传的值，设置为默认地址
        return await Address.update(
            { is_default: true },
            {
                where: { id }
            }
        )

    }
```

成功响应：

```json
{
    "code": 0,
    "message": "设置默认地址成功",
    "result": [
        1
    ]
}
```

## 订单模块

### 生成订单接口

```
POST /orders
```

> 请求参数

```
address_id, goods_info, total
```

> 响应

成功

```json
{
    "code": 0,
    "message": "生成订单成功",
    "result": {
        "id": 1,
        "address_id": 1,
        "goods_info": "",
        "total": "",
        "order_number": ""
    }
}
```

订单表

表名：`sai_orders`



| 字段名       | 字段类型      | 说明                                                         |
| ------------ | ------------- | ------------------------------------------------------------ |
| id           | int           | 主键，自增                                                   |
| user_id      | int           | 用户id                                                       |
| address_id   | int           | 地址id                                                       |
| goods_info   | text          | 商品信息，json字符                                           |
| total        | decimal(10,2) | 订单总金额                                                   |
| order_number | char(16)      | 订单号，唯一订单标识                                         |
| status       | tinyint       | 订单状态（ 0：未支付，1：已支付，2：已发货，3：已签收，4：取消 ） |



`order.route.js`

```js
const Router = require('@koa/router')
const router = new Router({ prefix: '/orders' })

const { auth } = require('../middleware/auth.middleware')
const { validator } = require('../middleware/order.middleware')
const { create } = require('../controller/order.controller')

router.post(
    '/',
    auth,
    validator({
        address_id: 'int',
        goods_info: 'string',
        total: 'string'
    }),
    create
)

module.exports = router
```

`order.middleware.js`

```js
const { orderFormatError } = require('../constant/error.type')

const validator = (rules) => {
    return async (ctx, next) => {
        try {
            await ctx.verifyParams(rules)
        } catch (err) {
            console.error(err)
            orderFormatError.result = err
            ctx.app.emit('error', orderFormatError, ctx)
            return
        }

        await next()
    }
}

module.exports = {
    validator
}
```

`error.type.js`

```js
    orderFormatError: {
        code: '10401',
        message: '数据格式错误',
        result: ''
    }
```

`order.controller.js`

```js
const { createOrder } = require('../service/order.service')

class OrderController {
    async create(ctx, next) {
        const user_id = ctx.state.user.id
        const { address_id, goods_info, total } = ctx.request.body
        const order_number = 'sai' + Date.now()

        const res = await createOrder({
            user_id,
            address_id,
            goods_info,
            total,
            order_number
        })

        ctx.body = {
            code: 0,
            message: '生成订单成功',
            result: res
        }
    }
}

module.exports = new OrderController()
```

`order.service.js`

```js
const Order  = require('../model/order.model')
class OrderService {
    async createOrder(order) {
        return await Order.create(order)
    }
}

module.exports = new OrderService()
```

`order.model.js`

```js
const seq = require('../db/seq')
const {DataTypes} = require('sequelize')

const Order = seq.define('sai_orders', {
    user_id: {
        type: DataTypes.INTEGER,
        allowNull: false,
        comment: '用户id'
    },
    address_id: {
        type: DataTypes.INTEGER,
        allowNull: false,
        comment: '地址id'
    },
    goods_info: {
        type: DataTypes.TEXT,
        allowNull: false,
        comment: '商品信息'
    },
    total: {
        type: DataTypes.DECIMAL(10,2),
        allowNull: false,
        comment: '订单总金额'
    },
    order_number: {
        type: DataTypes.CHAR(16),
        allowNull: false,
        comment: '订单号'
    },
    status: {
        type: DataTypes.TINYINT,
        allowNull: false,
        defaultValue: 0,
        comment: '订单状态（ 0：未支付，1：已支付，2：已发货，3：已签收，4：取消 ）'
    }
})

// Order.sync({force: true})

module.exports = Order
```

正确响应：

```json
{
    "code": 0,
    "message": "生成订单成功",
    "result": {
        "status": 0,
        "id": 2,
        "user_id": 48,
        "address_id": 2,
        "goods_info": "[{}, {}, {}]",
        "total": "199.99",
        "order_number": "sai1659969030037",
        "updatedAt": "2022-08-08T14:30:30.041Z",
        "createdAt": "2022-08-08T14:30:30.041Z"
    }
}
```

### 订单列表接口

```
GET /orders
```

> 请求参数

```json
{
	"pageNum": 1,
    "pageSize": 10,
    "status": 0
}
```

> 响应

```json
{
    "code": 0,
    "messaeg": "获取订单列表成功",
    "result": [
        {
            "id": 1,
            "goods_info": "",
            "total": "",
            "order_number": "",
            "status": 0
        }
    ]
}
```

`order.route.js`

```js
// 获取订单列表
router.get('/', auth, findAll)
```

`order.controller.js`

```js
    async findAll(ctx, next) {
        const {pageNum = 1,pageSize = 10, status = 0} = ctx.request.query
        const res = await findAllOrder(pageNum, pageSize, status)
        ctx.body = {
            code: '',
            message: '获取订单列表成功',
            result: res
        }
    }
```

`order.service.js`

```js
    async findAllOrder(pageNum, pageSize, status) {
        const { count, rows } = await Order.findAndCountAll({
            attributes: ['goods_info', 'total', 'order_number', 'status'],
            where: {
                status
            },
            offset: (pageNum - 1) * pageSize,
            limit: pageSize * 1,
        })

        return {
            pageNum,
            pageSize,
            total: count,
            list: rows
        }
    }
```

### 修改订单接口

```
PATCH /order/:id
```

> 请求参数

```json
{
    "status": 1
}
```

对于会员，可以取消订单（取消订单也是更新状态）

`order.route.js`

```js
// 修改订单
router.patch('/:id', auth, validator({
    status: 'number'
}), update)
```

`order.controller.js`

```js
    async update(ctx, next) {
        const id = ctx.request.params.id
        const {status} = ctx.request.body
        const res = await updateOrder(id, status)

        ctx.body = {
            code: 0,
            message: '更新订单状态成功',
            result: res
        }
    }
```

`order.service.js`

```js
    async updateOrder(id, status) {
        return await Order.update({ status }, { where: { id } })
    }
```

成功响应

```json
{
    "code": 0,
    "message": "更新订单状态成功",
    "result": [
        1
    ]
}
```





















































