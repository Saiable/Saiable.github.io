---
title: 'python_网络编程'
date: 2022-8-9 09:03:02
cover: false
---



教程来源：https://www.bilibili.com/video/BV1bZ4y1V7Nm?p=4

教程笔记：https://www.cnblogs.com/Eva-J/articles/8244551.html



- 网络编程
  - 网络基础
  - 基于tcp和udp的socket
  - 解决tcp协议的粘包问题
  - 并发问题

# 1.网络基础

## 1.1.网络架构

- 两个运行中的程序，如何传递信息？
  - 整一个中间的文件，一个程序负责写，一个程序负责读
- 两台机器上，两个运行中的程序，如何通信？
  - 通过网络
- 网络应用开发架构
  - C/S
    - client 客户端
    - server 服务端
  - B/S
    - browser 浏览器
    - server 服务端
  - B/S和C/S架构的关系
    - B/S是特殊的C/S架构

## 1.2.网络通讯基础

请看我的`思科CCNA网络基础入门.md`，在`network`项目里

## 1.3.Socket实现通信

`socket`是实现网络通信的模块

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

```
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))

msg = sk.recv(1024)
print(msg)
sk.send(b'byebye')

sk.close()
```

启动顺序：先启动`server.py`，再启动`client.py`

# 2.网络协议与OSI七层模型

- TCP协议
  - 协议的特点
    - 三次握手、四次挥手
- UDP协议
  - 协议的特点
- OSI七层模型
  - 每一层的物理设备
  - 每一层的常见协议
- 代码部分
  - 介绍socket
  - 使用socket完成tcp协议的web通信
    - 练习
  - 使用socket完成udp协议的web通信
    - 练习

## 2.1.TCP协议



## 2.2.UDP协议



## 2.3.OSI七层模型



# 3.Socket介绍



## 3.1.socket介绍

python中socket模块，完成网络编程的功能

socket本质，是一个工作在应用层与传输层之间的抽象层：

![在这里插入图片描述](https://img-blog.csdnimg.cn/40b2e3069e9e4422ae1119f947545486.png)

虽然socket还有底层，但是对于程序员来说，已经是网络操作的底层了

你只需要给sockect IP、端口等，让它发就完事了

至于数据怎么封装，怎么发，怎么实现，我们并不关心

socket历史：

- 同一台机器上的两个服务之间的通信
  - 基于文件
- 基于网络的多台机器之间的多个服务通信
  - 现代通信机制

知道以上，就足够了，以后socket对于你来说，就是一个模块，你会调用就可以

# 4.Socket实现TCP通信

## 4.1.tcp代码详解

`server.py`

创建对象：`sk = socket.socket()`，这个是有默认参数的

- `family=AF_INET`
  - 表示基于网络通信
- `type=SOCK_STREAM`
  - 表示协议是TCP

绑定地址：`sk.bind()`，告诉sk对象，我要通信的对端是谁

监听请求：`sk.listen()`，python3.4之前（包括），还需要传n，表示允许有多少个客户端等待，3.4之后，就没有这样的限制

以上还没有建立3次握手，只是准备阶段



`sk.accept()`，接受请求的状态，处于阻塞状态，直到有客户端来连接

右边是`client.py`，这是实现了三次握手

![在这里插入图片描述](https://img-blog.csdnimg.cn/68089c5d93c849a0aee944027b988f9a.png)



server端是通过conn通信，而client是通过sk通信的，为啥？

- 对于server端来说，并不知道谁要连接
- 来一个client，后面不连接了，对于server来说，只要关连接就行了，而不用关服务
- 对于client，关了就是关了



信息收发：

![在这里插入图片描述](https://img-blog.csdnimg.cn/02e5e127d5e34ebca2ce4b6405ca2b75.png)

client端采取什么编码并不重要，重要的是client采取的是utf-8编码，server端也要采取utf-8解码

聊天实现：

将直接传递的字符串，替换为input即可

server.py

```python
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

print('*'*20)
conn,addr = sk.accept()
while True:
	msg = conn.recv(1024)
	print(msg.decode('utf-8'))
	
	inp = input('>>>')
	conn.send(inp.encode('utf-8'))
	
conn.close()
sk.close()
```



client.py

```python
import socket

sk = socket.socket()

sk.connect(('127.0.0.1',9000))
while True:
	inp = input('>>>')
	sk.send(inp.encode('utf-8'))
	
	msg = sk.recv(1024)
	print(msg.decode('utf-8'))
	
sk.close()
```

`server.py`

![在这里插入图片描述](https://img-blog.csdnimg.cn/47e34ee98341455693764df7a55120ba.png)

`client.py`

![在这里插入图片描述](https://img-blog.csdnimg.cn/a8e4ffba0185434b97156e6be3df6e0f.png)

先启动server，再启动client，然后先在client里发消息



## 4.2.实现退出

添加退出代码：

server.py

```python
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

print('*' * 20)
conn, addr = sk.accept()

while True:
    msg = conn.recv(1024).decode('utf-8')
    if msg.upper() == 'Q':break
    print(msg)

    inp = input('>>>')
    conn.send(inp.encode('utf-8'))
    if inp.upper() == 'Q': break

conn.close()
sk.close()
```

client.py

```python
import socket

sk = socket.socket()

sk.connect(('127.0.0.1', 9000))
while True:
    inp = input('>>>')
    sk.send(inp.encode('utf-8'))
    if inp.upper() == 'Q': break

    msg = sk.recv(1024).decode('utf-8')
    if msg.upper() == 'Q': break
    print(msg)

sk.close()
```



## 4.3.通信占用问题

我们复制一份client，然后在上面的基础上，与server进行通信

![在这里插入图片描述](https://img-blog.csdnimg.cn/7e8a8498d0214c05b521893e98d8d0f1.png)

我们发现，此时并没有能够通信

![在这里插入图片描述](https://img-blog.csdnimg.cn/e43bf688a7d54f06a15d016c46ded95d.png)

并且第一个客户端退出后，客户端也会直接关闭

解决方案：使用循环嵌套

server.py

```python
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

print('*' * 20)

while True:
    conn, addr = sk.accept()

    while True:
        msg = conn.recv(1024).decode('utf-8')
        if msg.upper() == 'Q': break
        print(msg)

        inp = input('>>>')
        conn.send(inp.encode('utf-8'))
        if inp.upper() == 'Q': break

    conn.close()
sk.close()
```

客户端代码不变

此时，客户端1关闭后，服务端仍可和客户端2通信

## 4.4.小结

- 想说啥就说啥
  - input实现
- 想说多久说多久
  - 循环内层
- 和一个人聊完，再和另外一个人聊
  - 循环外层

# 5.Socket实现UDP通信

## 5.1.UDP代码详解

server.py

```python
import socket

sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.01',9000))

while True:
    #ret = sk.recvfrom(1024) 
    # ret是一个元组，是client发过来的msg和addr
    # 使用recvfrom是因为不确定谁会给我发消息
    #print(ret)
    
    msg,client_addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    
    msg = input('>>>').encode('utf-8')
    sk.sendto(msg,client_addr)

sk.close()
```

client.py

```python
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)

while True:
    inp = input('>>>').encode('utf-8')
    sk.sendto(inp, ('127.0.0.1',9000))
    # ret = sk.recv(1024) # recvfrom也可以，因为已经确定了ip和端口
    # print(ret)
    msg,server_addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
sk.close()
```

备注：这两端代码实际运行会报错

```
Traceback (most recent call last):
  File "F:/workspace/git/md/python/code/网络编程/09.client_udp.py", line 9, in <module>
    ret = sk.recvfrom(1024)
ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
```

查了下，也没解决，暂且跳过

# 6.粘包问题

## 6.1.粘包现象

现象：客户端连续发送两条，会在一行显示

解释：TCP是无边界流式传输

## 6.2.解决粘包现象



# 7.非阻塞IO模型



# 8.验证客户端的合法性



# 9.socketserver模块



# 10.作业

## 10.1.不同好友，聊天字体颜色不用

需求：

1.通信连接后，能知道对面这个人是哪一个好友

提醒：`qq号记录表`

2.不同好友的聊天字体颜色不同

提醒：`python控制台输出，带颜色`

server.py

```python
import socket
import json

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

color_dict = {
    '12345': {'color':'\033[31m','name':'alex'},
    '12346': {'color': '\033[33m', 'name': 'sia'},

}

print('*' * 20)


def chat(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        dic_msg = json.loads(msg)
        uid = dic_msg['id']
        # name,msg = msg.split('|')
        # print('%s: %s'%(name,msg))
        # print('%s: %s'%(dic_msg['name'],dic_msg['msg']))

        if dic_msg['msg'].upper() == 'Q':
            print('%s已经下线'%color_dict[uid]['name'])
            break
        print('%s%s: %s\033[0m'%(color_dict[uid]['color'],color_dict[uid]['name'],dic_msg['msg']))

        inp = input('>>>')
        conn.send(inp.encode('utf-8'))
        if inp.upper() == 'Q':
            print('你已经断开和%s的聊天！'%color_dict[uid]['name'])
            break
    conn.close()


while True:
    conn, addr = sk.accept()
    chat(conn)
    
    # 可不可以用with呢？
    # with sk.accept() as a:
    #	print(a)
    
    # 实际运行时报错了，因为内部没有__enter__方法
    # 我们可以自己写一个装饰器实现
sk.close()
```

client.py

```python
import socket
import json

sk = socket.socket()

id = '12345'
sk.connect(('127.0.0.1', 9000))
while True:
    inp = input('>>>')
    name = 'alex'
    # dic = {'msg':inp, 'name':name}
    dic = {'msg':inp,'id':id}
    str_dict = json.dumps(dic)
    # sk.send('|'.join([name,inp]).encode('utf-8'))
    sk.send(str_dict.encode('utf-8'))
    if inp.upper() == 'Q':
        print('你已经断开和server的聊天！')
        break
    msg = sk.recv(1024).decode('utf-8')

    if msg.upper() == 'Q': break

    print(msg)
sk.close()
```

小结：客户端和服务端，需要统一一下交互的数据格式

## 10.2.



进阶需求：

1.多个人能同时互相聊

客户端1发给服务端，服务端转发给客户端2

2.如果对方不在线，怎么办

3.基于TCP协议实现用户登陆

- 基础：只实现基础的登陆
- 进阶：加入hashlib密文存储密码

4.基于tcp协议完成文件上传

 - 基础：两台机器能从一台发往另一台即可
 - 进阶：考虑大文件
