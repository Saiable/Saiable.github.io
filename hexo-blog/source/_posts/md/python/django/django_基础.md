---
title: 'django基础'
date: 2022-8-9 09:03:02
cover: false
tags:
- django
categories: django
---



# 1.web应用程序

## 1.1.实现简单的web应用程序

server.py

```
import socket

sock = socket.socket()
sock.bind(('127.0.0.1',9090))
sock.listen(5)

while 1:
    print('server waiting...')
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print('data:',data)
    # 响应首行和响应体之间，用\r\n\r\n隔开
    conn.send(b'HTTP/1.1 200 OK\r\n\r\nHello World')


```

运行之后，在浏览器访问`127.0.0.1:9009`，可以到输出的`Hello World`

后台`print`如下：

```
server waiting...
data: b'GET /favicon.ico HTTP/1.1\r\nHost: 127.0.0.1:9090\r\nConnection: keep-alive\r\nPragma: no-cache\r\nCache-Control: no-cache\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4506.400\r\nAccept: image/webp,image/apng,image/*,*/*;q=0.8\r\nReferer: http://127.0.0.1:9090/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'

```

咱们把`\r\n`用换行替代一下：

```
server waiting...
data: b'GET /favicon.ico HTTP/1.1
Host: 127.0.0.1:9090
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4506.400
Accept: image/webp,image/apng,image/*,*/*;q=0.8
Referer: http://127.0.0.1:9090/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9

'
```

这就是一个简单的web应用程序了



注意，如果不加响应首行，如

```
conn.send(b'HelloWorld')
```

则会报以下错误，表示浏览器已经拿到响应了，但是我解析不了

```
ERR_INVALID_HTTP_RESPONSE
```

因为浏览器拿到服务器传过来的二进制数据，无法解析，需要加上Http响应首行，按照Http协议进行解析

## 1.2.对比TCP连接

在Socket编程时，都是一个server.py，一个client.py

server.py

```
import socket

sk = socket.socket() # 买手机
sk.bind(('127.0.0.1',9000)) # 绑定卡号
sk.listen() # 开机

conn,addr = sk.accept() # 等着接电话
conn.send(b'hello')
msg = conn.recv(1024)
print(msg)

conn.close() # 挂电话
sk.close() # 关机（释放端口资源）
```

client.py

```python
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))

msg = sk.recv(1024)
print(msg)
sk.send(b'HTTP/1.1 200 OK\r\n\r\nHello World')

sk.close()
```

当不通过浏览器解析，而直接通过TCP传输时，上述的响应首行，只会被解释成和`Hello World`一样的字符串

![在这里插入图片描述](https://img-blog.csdnimg.cn/050b58ae82754fff8bf68fa86687c715.png)

所以说，Http是应用层协议

## 1.3.新增web应用程序的功能

### 1.3.1.加粗标题

现在server提供的服务，仅仅是展示`Hello World`字符串

我们现在增加`<h1>`标签：

```
import socket

sock = socket.socket()
sock.bind(('127.0.0.1',9090))
sock.listen(5)

while 1:
    print('server waiting...')
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print('data:',data)
    # 响应首行和响应体之间，用\r\n\r\n隔开
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n<h1>Hello World</h1>')

    
```

显示如下：

![在这里插入图片描述](https://img-blog.csdnimg.cn/1085104df1b24fba800d7a5d1d097649.png)

浏览器`Preview`展示的，其实就是最上面的`Hello World`

而`Response`，则是传给浏览器引擎的数据，即含有`html`标签的数据

那么，`HTTP/1.1 200 OK\r\n\r\n`，则是在服务器传给浏览器，经过Http协议解析了



所以，`HTTP/1.1 200 OK\r\n\r\n<h1>Hello World</1>`这个字符串的解析顺序如下：

只考虑数据达到浏览器后，该层属于应用层，发现是HTTP协议头，于是按照Http协议进行解析，解析完的数据给浏览器这个应用程序

浏览器应用程序，对`<h1>Hello World</1>`进行解析，经过浏览器引擎渲染，最终是加粗的`Hello World`效果

### 1.3.2.加上图片

```python
import socket

sock = socket.socket()
sock.bind(('127.0.0.1',9090))
sock.listen(5)

while 1:
    print('server waiting...')
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print('data:',data)
    # 响应首行和响应体之间，用\r\n\r\n隔开
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n<h1>Hello World</h1><img src="https://img2.baidu.com/it/u=1170422687,3709426869&fm=26&fmt=auto">')


```

显示效果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/42824bba773042e095e9333f3f8e4d59.png)

渲染过程和之前一样，只不过又向百度的服务器发了一个请求

### 1.3.3.封装前端代码

一个页面是由很多这样的标签语言的，如果都写在`send()`方法中，既累人又不易于维护

所以我们先写html代码，然后把从html文件中，读取出来给send就可以了



新建`index.html`

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Hello World</h1>
    <img src="https://img2.baidu.com/it/u=1170422687,3709426869&fm=26&fmt=auto" alt="">
    <a href="http://www.baidu.com">click</a>
</body>
</html>
```

server.py

```python
import socket

sock = socket.socket()
sock.bind(('127.0.0.1',9090))
sock.listen(5)

while 1:
    print('server waiting...')
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print('data:',data)

    with open('index.html','r') as fr:
        response = fr.read()
    # 响应首行和响应体之间，用\r\n\r\n隔开
    conn.send(('HTTP/1.1 200 OK\r\n\r\n%s'%response).encode('utf-8'))
```



# 2.Http协议

详细参见《阅读笔记《图解HTTP》.md》：https://gitee.com/mindcons-g/network/blob/master/%E9%98%85%E8%AF%BB%E7%AC%94%E8%AE%B0%E3%80%8A%E5%9B%BE%E8%A7%A3HTTP%E3%80%8B.md

## 2.1.请求协议

### 2.1.1.get请求

请求格式

![在这里插入图片描述](https://img-blog.csdnimg.cn/0dc2f712e7bd4d67940f928db0fd3191.png)

请求方式：get与post请求

- GET提交的数据会放在URL之后，以`？`分割URL和传输数据，参数之间以`&`相连，如`EditBook?name=test&id=123456`
- POST方法是把提交的数据放在HTTP包的请求体中
- GET提交的数据有大小限制（因为浏览器对URL长度有限制），而POST方法提交的数据没有限制
- GET于POST请求在服务器端获取请求数据方式不同

我们再来详细分析一下，传递给服务器的data值

```
server waiting...
data: b'GET /favicon.ico HTTP/1.1\r\nHost: 127.0.0.1:9090\r\nConnection: keep-alive\r\nPragma: no-cache\r\nCache-Control: no-cache\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4506.400\r\nAccept: image/webp,image/apng,image/*,*/*;q=0.8\r\nReferer: http://127.0.0.1:9090/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'

```

两个`\r\n`分割的是请求头和请求体，只有POST才有请求体

对于请求报文，可以简单理解为，就是前段传给服务的一段字符串，以一定的格式组织了一定的信息

### 2.1.2.post请求

我们构建一个post请求

`post_test.html`

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
<form action="http://127.0.0.1:9090/" method="post">
    用户名 <input type="text" name="user">
    密码 <input type="password" name="pwd">
    <input type="submit">
</form>

</body>
</html>
```

server.py

```python
import socket

sock = socket.socket()
sock.bind(('127.0.0.1',9090))
sock.listen(5)

while 1:
    print('server waiting...')
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print('data:',data)

    with open('post_test.html','rb') as fr:
        response = fr.read()
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n%s'%response)
```

前台显示：

![在这里插入图片描述](https://img-blog.csdnimg.cn/d22ac988630e444fb47521e21b90363c.png)

我们填写一下并提交，看一下后台：

```
data: b'POST / HTTP/1.1\r\nHost: 127.0.0.1:9090\r\nConnection: keep-alive\r\nContent-Length: 20\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4506.400\r\nOrigin: http://127.0.0.1:9090\r\nContent-Type: application/x-www-form-urlencoded\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nReferer: http://127.0.0.1:9090/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\nuser=test&pwd=123445'

```

POST请求的最后，是有请求体数据的：`user=test&pwd=123445`

## 2.2.响应协议

### 2.2.1.响应报文构成

![在这里插入图片描述](https://img-blog.csdnimg.cn/acc4da7250c54ca98e7552cb1d9856d3.png)

具体到代码层面：

```python
conn.send(b'HTTP/1.1 200 OK\r\n\r\n%s'%response)

conn.send(b'HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n\r\n%s'%response)
```

### 2.2.1响应状态码

状态码的职责是，当客户端向服务端发送请求时，返回的请求结果。

借助状态码，用户可以知道服务器是正常处理了请求，还是出现了错误。

状态码，如`200`表示`OK`，是以3位数字和原因短语构成的，响应状态码分别有以下5种：

![在这里插入图片描述](https://img-blog.csdnimg.cn/6d6513396f8744f695b6094fe36b5683.png)



# 3.wsgiref模块

## 3.1.web框架

Web框架（Web framework）是一种开发框架，用来支持动态网站、网络应用和网络服务的开发。这大多数的web框架提供了一套开发和部署网站的方式，也为web行为提供了一套通用的方法。web框架已经实现了很多功能，开发人员使用框架提供的方法并且完成自己的业务逻辑，就能快速开发web应用了。浏览器和服务器的是基于HTTP协议进行通信的。也可以说web框架就是在以上十几行代码基础张扩展出来的，有很多简单方便使用的方法，大大提高了开发的效率。



```python
from wsgiref.simple_server import make_server


def application(environ, start_response):
    # 按着http协议解析数据，所有解析好的data，存在environ中：environ
    # 按着http协议组装数据:start_response
    start_response('200 OK', [('Content-Type', 'text/html')])
    print(environ)
    print(type(environ))
    return [b'<h1>Hello, web!</h1>']

# 封装socket
httpd = make_server('', 8080, application)

print('Serving HTTP on port 8000...')
# 开始监听HTTP请求，等待用户连接:
httpd.serve_forever()
```

`environ`中有一个`PATH_INFO`的键，保存着当前访问路径

```python
from wsgiref.simple_server import make_server


def application(environ, start_response):

    print(environ)
    print(type(environ))

    # 获取当前请求路径
    path = environ.get('PATH_INFO')
    start_response('200 OK', [])

    if path == '/login':
        with open('login.html', 'r') as fr:
            data = fr.read()
    elif path == '/index':
        with open('index.html','r') as fr:
            data = fr.read()
    return [data.encode('utf-8')]

httpd = make_server('', 8090, application)

print('Serving HTTP on port 8090...')
# 开始监听HTTP请求:
httpd.serve_forever()
```

我们可以根据访问路径的不同，给用户返回不同的页面



# 4.DIY一个web框架

## 4.1.方案一



## 4.2.方案二



## 4.3.解耦



## 4.4.什么是框架

反复要写的，必写的，琐碎的内容，由框架先写好

框架，就是一个文件夹（包）而已，里面每个文件（夹）都有各自的功能

程序员只要专注业务逻辑的编码



## 4.5.关于数据库的操作（核心）

之前的代码，真正跑起来，只有`main.py`一个文件



注册页面，需要用数据库，存放用户数据

登陆页面，需要和数据库里的内容验证



`models.py`作用：在项目启动前，生成表结构

## 4.6.web 框架功能总结



# 5.Django简介

https://www.cnblogs.com/yuanchenqi/articles/8875659.html

## 5.1.MVC与MTV模型

模型概念的衍生

## 5.2.Django下载与基本命令



## 5.3.Django简单示例

基本流程演示

## 5.4.静态文件配置

### 5.4.1.static配置

`settings.py`的最后添加

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
```

然后在manage.py的同级目录下，创建`static`文件夹，也可以放在app的目录下

在html中就可以引用：

```html
<link rel="stylesheet" href="/static/plugin/bootstrap/css/bootstrap.css">
```



## 5.5.路由控制

参考：https://www.cnblogs.com/yuanchenqi/articles/8931472.html

### 5.5.1.简单配置

request



Httpresponse



re_path中的正则



正则中只要分组了，就会作为位置参数，传递给视图函数



正则和视图函数的关系，是多对一



若有两个正则，同时匹配了，会走先匹配的视图函数



### 5.5.2.有名分组

`？P<>`固定写法，相当于起了个别名

re_path(r')



### 5.5.3.路由分发



```python
'''
At any point, your urlpatterns can “include” other URLconf modules. This
essentially “roots” a set of URLs below other ones.

'''

from django.urls import path,re_path,include
from app01 import views

urlpatterns = [
   re_path(r'^admin/', admin.site.urls),
   re_path(r'^blog/', include('blog.urls')),
]
```

### 5.5.4.登陆验证示例

在视图函数中，进行http请求类别的判断，以进行不同的行为

```python
def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        print(request.GET)
        print(request.POST)
        # 取字典的方式取值
        user = request.POST.get("user")
        pwd request.POST.get("pwd")
        
        return HttpResponse("OK")
```



### 5.5.5.反向解析

路由的名字，在实际开发的时候，并不是一成不变的

html中的反向解析



视图函数中的反向解析

反向解析中，如果还有正则，则需要加`args`参数

只要设置了别名，就可以反向解析到url，只要有args参数，就可以替换掉url中的正则



### 5.5.6.名称空间

多个app中，可能有相同的别名



### 5.5.7.path方法



#### 5.5.7.1.内置转换器



#### 5.5.7.2.自定义转换器

对于一些复杂或者复用的需要，可以定义自己的转化器。转化器是一个类或接口，它的要求有三点：

- `regex` 类属性，字符串类型

- `to_python(self, value)` 方法，value是由类属性 `regex` 所匹配到的字符串，返回具体的Python变量值，以供Django传递到对应的视图函数中。
- `to_url(self, value)` 方法，和 `to_python` 相反，value是一个具体的Python变量值，返回其字符串，通常用于url反向引用。

例子：

```python
class FourDigitYearConverter:  
    regex = '[0-9]{4}'  
    def to_python(self, value):  
        return int(value)  
    def to_url(self, value):  
        return '%04d' % value  
```

使用`register_converter` 将其注册到URL配置中：

```python
from django.urls import register_converter, path  
from . import converters, views  
register_converter(converters.FourDigitYearConverter, 'yyyy')  
urlpatterns = [  
    path('articles/2003/', views.special_case_2003),  
    path('articles/<yyyy:year>/', views.year_archive),  
    ...  
]  
```

## 5.6.视图

参考：https://www.cnblogs.com/yuanchenqi/articles/8876856.html

一个视图函数，简称视图，是一个简单的Python 函数，它接受Web请求并且返回Web响应。响应可以是一张网页的HTML内容，一个重定向，一个404错误，一个XML文档，或者一张图片. . . 是任何东西都可以。无论视图本身包含什么逻辑，都要返回响应。代码写在哪里也无所谓，只要它在你的Python目录下面。除此之外没有更多的要求了——可以说“没有什么神奇的地方”。为了将代码放在某处，约定是将视图放置在项目或应用程序目录中的名为`views.py`的文件中。

下面是一个返回当前日期和时间作为HTML文档的视图：

```python
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
```



### 5.6.1.请求对象

#### 5.6.1.1.request属性 

django将请求报文中的请求行、首部信息、内容主体封装成 HttpRequest 类中的属性。 除了特殊说明的之外，其他均为只读的。

```python
/*

1.HttpRequest.GET

　　一个类似于字典的对象，包含 HTTP GET 的所有参数。详情请参考 QueryDict 对象。

2.HttpRequest.POST

　　一个类似于字典的对象，如果请求中包含表单数据，则将这些数据封装成 QueryDict 对象。

　　POST 请求可以带有空的 POST 字典 —— 如果通过 HTTP POST 方法发送一个表单，但是表单中没有任何的数据，QueryDict 对象依然会被创建。
   因此，不应该使用 if request.POST  来检查使用的是否是POST 方法；应该使用 if request.method == "POST"
　　另外：如果使用 POST 上传文件的话，文件信息将包含在 FILES 属性中。
   
   注意：键值对的值是多个的时候,比如checkbox类型的input标签，select标签，需要用：
        request.POST.getlist("hobby")

3.HttpRequest.body

　　一个字符串，代表请求报文的主体。在处理非 HTTP 形式的报文时非常有用，例如：二进制图片、XML,Json等。
　　但是，如果要处理表单数据的时候，推荐还是使用 HttpRequest.POST 。


4.HttpRequest.path

　　一个字符串，表示请求的路径组件（不含域名）。
　　例如："/music/bands/the_beatles/"

5.HttpRequest.method

　　一个字符串，表示请求使用的HTTP 方法。必须使用大写。
　　例如："GET"、"POST"


6.HttpRequest.encoding

　　一个字符串，表示提交的数据的编码方式（如果为 None 则表示使用 DEFAULT_CHARSET 的设置，默认为 'utf-8'）。
   这个属性是可写的，你可以修改它来修改访问表单数据使用的编码。
   接下来对属性的任何访问（例如从 GET 或 POST 中读取数据）将使用新的 encoding 值。
   如果你知道表单数据的编码不是 DEFAULT_CHARSET ，则使用它。


7.HttpRequest.META

 　　一个标准的Python 字典，包含所有的HTTP 首部。具体的头部信息取决于客户端和服务器，下面是一些示例：

    CONTENT_LENGTH —— 请求的正文的长度（是一个字符串）。
    CONTENT_TYPE —— 请求的正文的MIME 类型。
    HTTP_ACCEPT —— 响应可接收的Content-Type。
    HTTP_ACCEPT_ENCODING —— 响应可接收的编码。
    HTTP_ACCEPT_LANGUAGE —— 响应可接收的语言。
    HTTP_HOST —— 客服端发送的HTTP Host 头部。
    HTTP_REFERER —— Referring 页面。
    HTTP_USER_AGENT —— 客户端的user-agent 字符串。
    QUERY_STRING —— 单个字符串形式的查询字符串（未解析过的形式）。
    REMOTE_ADDR —— 客户端的IP 地址。
    REMOTE_HOST —— 客户端的主机名。
    REMOTE_USER —— 服务器认证后的用户。
    REQUEST_METHOD —— 一个字符串，例如"GET" 或"POST"。
    SERVER_NAME —— 服务器的主机名。
    SERVER_PORT —— 服务器的端口（是一个字符串）。
 　　从上面可以看到，除 CONTENT_LENGTH 和 CONTENT_TYPE 之外，请求中的任何 HTTP 首部转换为 META 的键时，
    都会将所有字母大写并将连接符替换为下划线最后加上 HTTP_  前缀。
    所以，一个叫做 X-Bender 的头部将转换成 META 中的 HTTP_X_BENDER 键。

8.HttpRequest.FILES

　　一个类似于字典的对象，包含所有的上传文件信息。
   FILES 中的每个键为<input type="file" name="" /> 中的name，值则为对应的数据。
　　注意，FILES 只有在请求的方法为POST 且提交的<form> 带有enctype="multipart/form-data" 的情况下才会
   包含数据。否则，FILES 将为一个空的类似于字典的对象。


9.HttpRequest.COOKIES

　　一个标准的Python 字典，包含所有的cookie。键和值都为字符串。



10.HttpRequest.session

 　　一个既可读又可写的类似于字典的对象，表示当前的会话。只有当Django 启用会话的支持时才可用。
    完整的细节参见会话的文档。


11.HttpRequest.user(用户认证组件下使用)

　　一个 AUTH_USER_MODEL 类型的对象，表示当前登录的用户。

　　如果用户当前没有登录，user 将设置为 django.contrib.auth.models.AnonymousUser 的一个实例。你可以通过 is_authenticated() 区分它们。

    例如：

    if request.user.is_authenticated():
        # Do something for logged-in users.
    else:
        # Do something for anonymous users.


     　　user 只有当Django 启用 AuthenticationMiddleware 中间件时才可用。

     -------------------------------------------------------------------------------------

    匿名用户
    class models.AnonymousUser

    django.contrib.auth.models.AnonymousUser 类实现了django.contrib.auth.models.User 接口，但具有下面几个不同点：

    id 永远为None。
    username 永远为空字符串。
    get_username() 永远返回空字符串。
    is_staff 和 is_superuser 永远为False。
    is_active 永远为 False。
    groups 和 user_permissions 永远为空。
    is_anonymous() 返回True 而不是False。
    is_authenticated() 返回False 而不是True。
    set_password()、check_password()、save() 和delete() 引发 NotImplementedError。
    New in Django 1.8:
    新增 AnonymousUser.get_username() 以更好地模拟 django.contrib.auth.models.User。

*/
```

#### 5.6.1.2.request常用方法

```python
/*

1.HttpRequest.get_full_path()

　　返回 path，如果可以将加上查询字符串。

　　例如："/music/bands/the_beatles/?print=true"


2.HttpRequest.is_ajax()

　　如果请求是通过XMLHttpRequest 发起的，则返回True，方法是检查 HTTP_X_REQUESTED_WITH 相应的首部是否是字符串'XMLHttpRequest'。

　　大部分现代的 JavaScript 库都会发送这个头部。如果你编写自己的 XMLHttpRequest 调用（在浏览器端），你必须手工设置这个值来让 is_ajax() 可以工作。

　　如果一个响应需要根据请求是否是通过AJAX 发起的，并且你正在使用某种形式的缓存例如Django 的 cache middleware，
   你应该使用 vary_on_headers('HTTP_X_REQUESTED_WITH') 装饰你的视图以让响应能够正确地缓存。

*/
```



### 5.6.2.响应对象

响应对象主要有三种形式：

- HttpResponse()
- render()
- redirect()

HttpResponse()括号内直接跟一个具体的字符串作为响应体，比较直接很简单，所以这里主要介绍后面两种形式。

#### 5.6.2.1.render()

```
render(request, template_name[, context]）
 
结合一个给定的模板和一个给定的上下文字典，并返回一个渲染后的 HttpResponse 对象。
```

```
参数：
     request： 用于生成响应的请求对象。

     template_name：要使用的模板的完整名称，可选的参数

     context：添加到模板上下文的一个字典。默认是一个空字典。如果字典中的某个值是可调用的，视图将在渲染模板之前调用它。render方法就是将一个模板页面中的模板语法进行渲染，最终渲染成一个html页面作为响应体。
```

#### 5.6.2.2.redirect()

传递要重定向的一个硬编码的URL

```
def my_view(request):
    ...
    return redirect('/some/url/')
```

也可以是一个完整的URL：

```
def my_view(request):
    ...
    return redirect('http://example.com/')　
```

key：两次请求　

```
1）301和302的区别。

　　301和302状态码都表示重定向，就是说浏览器在拿到服务器返回的这个状态码后会自动跳转到一个新的URL地址，这个地址可以从响应的Location首部中获取
  （用户看到的效果就是他输入的地址A瞬间变成了另一个地址B）——这是它们的共同点。

　　他们的不同在于。301表示旧地址A的资源已经被永久地移除了（这个资源不可访问了），搜索引擎在抓取新内容的同时也将旧的网址交换为重定向之后的网址；

　　302表示旧地址A的资源还在（仍然可以访问），这个重定向只是临时地从旧地址A跳转到地址B，搜索引擎会抓取新的内容而保存旧的网址。 SEO302好于301

 

2）重定向原因：
（1）网站调整（如改变网页目录结构）；
（2）网页被移到一个新地址；
（3）网页扩展名改变(如应用需要把.php改成.Html或.shtml)。
        这种情况下，如果不做重定向，则用户收藏夹或搜索引擎数据库中旧地址只能让访问客户得到一个404页面错误信息，访问流量白白丧失；再者某些注册了多个域名的
    网站，也需要通过重定向让访问这些域名的用户自动跳转到主站点等。

关于301与302
```

用redirect可以解释APPEND_SLASH的用法！

## 5.7.模板语法

### 5.7.1.变量



### 5.7.2.过滤器



### 5.7.3.标签



### 5.7.4.自定义标签和过滤器



### 5.7.5.继承



## 5.8.ORM

### 5.8.1.ORM简介

- MVC或者MVC框架中包括一个重要的部分，就是ORM，它实现了数据模型与数据库的解耦，即数据模型的设计不需要依赖于特定的数据库，通过简单的配置就可以轻松更换数据库，这极大的减轻了开发人员的工作量，不需要面对因数据库变更而导致的无效劳动
- ORM是“对象-关系-映射”的简称。

```python
#sql中的表                                                      

 #创建表:
     CREATE TABLE employee(                                     
                id INT PRIMARY KEY auto_increment ,                    
                name VARCHAR (20),                                      
                gender BIT default 1,                                  
                birthday DATA ,                                         
                department VARCHAR (20),                                
                salary DECIMAL (8,2) unsigned,                          
              );


  #sql中的表纪录                                                  

  #添加一条表纪录:                                                          
      INSERT employee (name,gender,birthday,salary,department)            
             VALUES   ("alex",1,"1985-12-12",8000,"保洁部");               

  #查询一条表纪录:                                                           
      SELECT * FROM employee WHERE age=24;                               

  #更新一条表纪录:                                                           
      UPDATE employee SET birthday="1989-10-24" WHERE id=1;              

  #删除一条表纪录:                                                          
      DELETE FROM employee WHERE name="alex"                             





#python的类
class Employee(models.Model):
     id=models.AutoField(primary_key=True)
     name=models.CharField(max_length=32)
     gender=models.BooleanField()
     birthday=models.DateField()
     department=models.CharField(max_length=32)
     salary=models.DecimalField(max_digits=8,decimal_places=2)


 #python的类对象
      #添加一条表纪录:
          emp=Employee(name="alex",gender=True,birthday="1985-12-12",epartment="保洁部")
          emp.save()
      #查询一条表纪录:
          Employee.objects.filter(age=24)
      #更新一条表纪录:
          Employee.objects.filter(id=1).update(birthday="1989-10-24")
      #删除一条表纪录:
          Employee.objects.filter(name="alex").delete()
```



### 5.8.2.单表操作

#### 5.8.2.1.创建表

##### 1.创建模型

创建名为book的app，在book下的models.py中创建模型：

```python
from django.db import models

# Create your models here.


class Book(models.Model):
     id=models.AutoField(primary_key=True)
     title=models.CharField(max_length=32)
     state=models.BooleanField()
     pub_date=models.DateField()
     price=models.DecimalField(max_digits=8,decimal_places=2)
     publish=models.CharField(max_length=32)
```

##### 2 更多字段和参数

每个字段有一些特有的参数，例如，CharField需要max_length参数来指定`VARCHAR`数据库字段的大小。还有一些适用于所有字段的通用参数。 这些参数在文档中有详细定义，这里我们只简单介绍一些最常用的：

**更多字段：**

```
'''
 
<1> CharField
        字符串字段, 用于较短的字符串.
        CharField 要求必须有一个参数 maxlength, 用于从数据库层和Django校验层限制该字段所允许的最大字符数.
 
<2> IntegerField
       #用于保存一个整数.
 
<3> FloatField
        一个浮点数. 必须 提供两个参数:
         
        参数    描述
        max_digits    总位数(不包括小数点和符号)
        decimal_places    小数位数
                举例来说, 要保存最大值为 999 (小数点后保存2位),你要这样定义字段:
                 
                models.FloatField(..., max_digits=5, decimal_places=2)
                要保存最大值一百万(小数点后保存10位)的话,你要这样定义:
                 
                models.FloatField(..., max_digits=19, decimal_places=10)
                admin 用一个文本框(<input type="text">)表示该字段保存的数据.
 
<4> AutoField
        一个 IntegerField, 添加记录时它会自动增长. 你通常不需要直接使用这个字段;
        自定义一个主键：my_id=models.AutoField(primary_key=True)
        如果你不指定主键的话,系统会自动添加一个主键字段到你的 model.
 
<5> BooleanField
        A true/false field. admin 用 checkbox 来表示此类字段.
 
<6> TextField
        一个容量很大的文本字段.
        admin 用一个 <textarea> (文本区域)表示该字段数据.(一个多行编辑框).
 
<7> EmailField
        一个带有检查Email合法性的 CharField,不接受 maxlength 参数.
 
<8> DateField
        一个日期字段. 共有下列额外的可选参数:
        Argument    描述
        auto_now    当对象被保存时,自动将该字段的值设置为当前时间.通常用于表示 "last-modified" 时间戳.
        auto_now_add    当对象首次被创建时,自动将该字段的值设置为当前时间.通常用于表示对象创建时间.
        （仅仅在admin中有意义...)
 
<9> DateTimeField
         一个日期时间字段. 类似 DateField 支持同样的附加选项.
 
<10> ImageField
        类似 FileField, 不过要校验上传对象是否是一个合法图片.#它有两个可选参数:height_field和width_field,
        如果提供这两个参数,则图片将按提供的高度和宽度规格保存.    
<11> FileField
     一个文件上传字段.
     要求一个必须有的参数: upload_to, 一个用于保存上载文件的本地文件系统路径. 这个路径必须包含 strftime #formatting,
     该格式将被上载文件的 date/time
     替换(so that uploaded files don't fill up the given directory).
     admin 用一个<input type="file">部件表示该字段保存的数据(一个文件上传部件) .
 
     注意：在一个 model 中使用 FileField 或 ImageField 需要以下步骤:
            （1）在你的 settings 文件中, 定义一个完整路径给 MEDIA_ROOT 以便让 Django在此处保存上传文件.
            (出于性能考虑,这些文件并不保存到数据库.) 定义MEDIA_URL 作为该目录的公共 URL. 要确保该目录对
             WEB服务器用户帐号是可写的.
            （2） 在你的 model 中添加 FileField 或 ImageField, 并确保定义了 upload_to 选项,以告诉 Django
             使用 MEDIA_ROOT 的哪个子目录保存上传文件.你的数据库中要保存的只是文件的路径(相对于 MEDIA_ROOT).
             出于习惯你一定很想使用 Django 提供的 get_<#fieldname>_url 函数.举例来说,如果你的 ImageField
             叫作 mug_shot, 你就可以在模板中以 {{ object.#get_mug_shot_url }} 这样的方式得到图像的绝对路径.
 
<12> URLField
      用于保存 URL. 若 verify_exists 参数为 True (默认), 给定的 URL 会预先检查是否存在( 即URL是否被有效装入且
      没有返回404响应).
      admin 用一个 <input type="text"> 文本框表示该字段保存的数据(一个单行编辑框)
 
<13> NullBooleanField
       类似 BooleanField, 不过允许 NULL 作为其中一个选项. 推荐使用这个字段而不要用 BooleanField 加 null=True 选项
       admin 用一个选择框 <select> (三个可选择的值: "Unknown", "Yes" 和 "No" ) 来表示这种字段数据.
 
<14> SlugField
       "Slug" 是一个报纸术语. slug 是某个东西的小小标记(短签), 只包含字母,数字,下划线和连字符.#它们通常用于URLs
       若你使用 Django 开发版本,你可以指定 maxlength. 若 maxlength 未指定, Django 会使用默认长度: 50.  #在
       以前的 Django 版本,没有任何办法改变50 这个长度.
       这暗示了 db_index=True.
       它接受一个额外的参数: prepopulate_from, which is a list of fields from which to auto-#populate
       the slug, via JavaScript,in the object's admin form: models.SlugField
       (prepopulate_from=("pre_name", "name"))prepopulate_from 不接受 DateTimeFields.
 
<13> XMLField
        一个校验值是否为合法XML的 TextField,必须提供参数: schema_path, 它是一个用来校验文本的 RelaxNG schema #的文件系统路径.
 
<14> FilePathField
        可选项目为某个特定目录下的文件名. 支持三个特殊的参数, 其中第一个是必须提供的.
        参数    描述
        path    必需参数. 一个目录的绝对文件系统路径. FilePathField 据此得到可选项目.
        Example: "/home/images".
        match    可选参数. 一个正则表达式, 作为一个字符串, FilePathField 将使用它过滤文件名. 
        注意这个正则表达式只会应用到 base filename 而不是
        路径全名. Example: "foo.*\.txt^", 将匹配文件 foo23.txt 却不匹配 bar.txt 或 foo23.gif.
        recursive可选参数.要么 True 要么 False. 默认值是 False. 是否包括 path 下面的全部子目录.
        这三个参数可以同时使用.
        match 仅应用于 base filename, 而不是路径全名. 那么,这个例子:
        FilePathField(path="/home/images", match="foo.*", recursive=True)
        ...会匹配 /home/images/foo.gif 而不匹配 /home/images/foo/bar.gif
 
<15> IPAddressField
        一个字符串形式的 IP 地址, (i.e. "24.124.1.30").
<16> CommaSeparatedIntegerField
        用于存放逗号分隔的整数值. 类似 CharField, 必须要有maxlength参数.
 
 
 
'''　　
```

**更多参数：**

```
(1)null
 
如果为True，Django 将用NULL 来在数据库中存储空值。 默认值是 False.
 
(1)blank
 
如果为True，该字段允许不填。默认为False。
要注意，这与 null 不同。null纯粹是数据库范畴的，而 blank 是数据验证范畴的。
如果一个字段的blank=True，表单的验证将允许该字段是空值。如果字段的blank=False，该字段就是必填的。
 
(2)default
 
字段的默认值。可以是一个值或者可调用对象。如果可调用 ，每有新对象被创建它都会被调用。
 
(3)primary_key
 
如果为True，那么这个字段就是模型的主键。如果你没有指定任何一个字段的primary_key=True，
Django 就会自动添加一个IntegerField字段做为主键，所以除非你想覆盖默认的主键行为，
否则没必要设置任何一个字段的primary_key=True。
 
(4)unique
 
如果该值设置为 True, 这个数据字段的值在整张表中必须是唯一的
 
(5)choices
由二元组组成的一个可迭代对象（例如，列表或元组），用来给字段提供选择项。 如果设置了choices ，默认的表单将是一个选择框而不是标准的文本框，<br>而且这个选择框的选项就是choices 中的选项。
```

##### 3 settings配置

若想将模型转为mysql数据库中的表，需要在settings中配置：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'bms',     　　 　  # 要连接的数据库，连接前需要创建好
        'USER':'root',　　　　　　  # 连接数据库的用户名
        'PASSWORD':'',　　　　　　  # 连接数据库的密码
        'HOST':'127.0.0.1',       # 连接主机，默认本级
        'PORT'：3306    　　　     #  端口 默认3306
    }
}
```

注意1：NAME即数据库的名字，在mysql连接前该数据库必须已经创建，而上面的sqlite数据库下的db.sqlite3则是项目自动创建 USER和PASSWORD分别是数据库的用户名和密码。设置完后，再启动我们的Django项目前，我们需要激活我们的mysql。然后，启动项目，会报错：no module named MySQLdb 。这是因为django默认你导入的驱动是MySQLdb，可是MySQLdb 对于py3有很大问题，所以我们需要的驱动是PyMySQL 所以，我们只需要找到项目名文件下的__init__,在里面写入：

```
import pymysql
pymysql.install_as_MySQLdb()
```

最后通过两条数据库迁移命令即可在指定的数据库中创建表 ：

```
python manage.py makemigrations
python manage.py migrate
```

注意2:确保配置文件中的INSTALLED_APPS中写入我们创建的app名称

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "book"
]
```

注意3:如果报错如下：

```
django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.3 or newer is required; you have 0.7.11.None
```

MySQLclient目前只支持到python3.4，因此如果使用的更高版本的python，需要修改如下：

通过查找路径C:\Programs\Python\Python36-32\Lib\site-packages\Django-2.0-py3.6.egg\django\db\backends\mysql
这个路径里的文件把

```python
if version < (1, 3, 3):
     raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__)
```

注释掉 就OK了。

注意4: 如果想打印orm转换过程中的sql，需要在settings中进行如下配置：

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}　　
```

### 5.8.3.添加表记录

#### 方式一：create

```python
# create方法的返回值book_obj，就是插入book表中的python葵花宝典这本书籍纪录对象
  book_obj=Book.objects.create(title="python葵花宝典",state=True,price=100,publish="苹果出版社",pub_date="2012-12-12")
```



#### 方式二： save

```python
book_obj=Book(title="python葵花宝典",state=True,price=100,publish="苹果出版社",pub_date="2012-12-12")
book_obj.save()
```

### 5.8.4.查询表记录

#### 5.8.4.1.查询API

要清晰各个方法的返回值，以及方法的调用者

这样才能明白，什么情况下调用什么方法

```python
<1> all():                  查询所有结果，返回一个QuerySet对象
  
<2> filter(**kwargs):       它包含了与所给筛选条件相匹配的对象，相当于where语句
  
<3> get(**kwargs):          返回与所给筛选条件相匹配的对象，返回结果有且只有一个，
                            如果符合筛选条件的对象超过一个或者没有都会抛出错误。返回一个model对象
  
<4> exclude(**kwargs):      它包含了与所给筛选条件不匹配的对象，返回一个QuerySet对象
 
<5> order_by(*field):       对查询结果排序，默认升序，参数前加一个-，就是降序，调用者和返回值，都是一个QuerySet对象
  
<6> reverse():              对查询结果反向排序
  
<8> count():                返回数据库中匹配查询(QuerySet)的对象数量，调用者是QuerySet对象，返回值是int
  
<9> first():                返回第一条记录，调用者是QuerySet对象，返回一个model对象
  
<10> last():                返回最后一条记录，调用者是QuerySet对象，返回一个model对象
  
<11> exists():              如果QuerySet包含数据，就返回True，否则返回False
 
<12> values(*field):        返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列model的实例化对象，而是一个可迭代的字典序列
    						调用者和返回值，都是一个QuerySet对象
        					ret = Book.objects.all().values("price")

<13> values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
    						ret = Book.objects.all().values_list("price","title")
        					
 
<14> distinct():            从返回结果中剔除重复纪录
    						reg = Book.objects.all.values("price").distinct()
```

#### 5.8.4.2.基于双下划线的模糊查询



```python
Book.objects.filter(price__in=[100,200,300])
Book.objects.filter(price__gt=100) # 大于
Book.objects.filter(price__lt=100) # 小于
Book.objects.filter(price__range=[100,200])
Book.objects.filter(title__contains="python") # 包含某个字符
Book.objects.filter(title__icontains="python") # 包含某个字符，不区分大小写
Book.objects.filter(title__startswith="py") # 以某个字符串开头
Book.objects.filter(pub_date__year=2012) #只有date类型，才能这样写
```



### 5.8.5删除表纪录

删除方法就是 delete()。它运行时立即删除对象而不返回任何值。例如：

```python
model_obj.delete()
```

你也可以一次性删除多个对象。每个 QuerySet 都有一个 delete() 方法，它一次性删除 QuerySet 中所有的对象。

例如，下面的代码将删除 pub_date 是2005年的 Entry 对象：

```python
Entry.objects.filter(pub_date__year=2005).delete()
```

在 Django 删除对象时，会模仿 SQL 约束 ON DELETE CASCADE 的行为，换句话说，删除一个对象时也会删除与它相关联的外键对象。例如：

```python
b = Blog.objects.get(pk=1)
# This will delete the Blog and all of its Entry objects.
b.delete()
```

要注意的是： delete() 方法是 QuerySet 上的方法，但并不适用于 Manager 本身。这是一种保护机制，是为了避免意外地调用 Entry.objects.delete() 方法导致 所有的 记录被误删除。如果你确认要删除所有的对象，那么你必须显式地调用：

```python
Entry.objects.all().delete()　　
```

如果不想级联删除，可以设置为:

```python
pubHouse = models.ForeignKey(to='Publisher', on_delete=models.SET_NULL, blank=True, null=True)
```

### 5.8.6.修改表纪录

```python
Book.objects.filter(title__startswith="py").update(price=120)
```

此外，update()方法对于任何结果集（QuerySet）均有效，这意味着你可以同时更新多条记录，update()方法会返回一个整型数值，表示受影响的记录条数。　



### 5.8.7.图书管理系统小练习

图书管理系统

![在这里插入图片描述](https://img-blog.csdnimg.cn/bb1cad80838f43a9bd957c90e3427b27.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/1200a9866b5448afa9f8b3d0db6076f5.png)

```
1 查询人民出版社出版过的价格大于200的书籍
 
2 查询2017年8月出版的所有以py开头的书籍名称
 
3 查询价格为50,100或者150的所有书籍名称及其出版社名称
 
4 查询价格在100到200之间的所有书籍名称及其价格
 
5 查询所有人民出版社出版的书籍的价格（从高到低排序，去重）
```

#### 5.8.7.1.添加页面





#### 5.8.7.2.查看书籍



#### 5.8.7.3.查看书籍



#### 5.8.7.4.删除书籍



#### 5.8.7.5.编辑功能

删除



























