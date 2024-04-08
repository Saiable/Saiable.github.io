---
title: 'python操作Redis'
date: 2022-8-9 09:03:02
cover: false
---



## 7.python操作Redis

### 7.1.远程连接redis注意事项：

- bind注释掉或者修改为`0.0.0.0`
- 关闭保护模式`protected-mode no`
- 关闭linux防火墙
  - 查看防火墙状态：`systemctl status firewalld`
  - 临时关闭防火墙：`systemctl stop firewalld`
- 如果使用的是腾讯云或者华为云等云服务器，请在控制台开启6379端口号。
- `pip install redis`安装redis库
- 注意，链接redis的文件名，不能取名为redis

#### 7.1.1.一般连接

```python 
from redis import Redis

'''
	一般连接，使用Redis连接
'''
conn = Redis(host ='localhost',port = '6379',password = 'foobared',db = 0,decode_responses = True)
# host可以是ip地址
# decode_responses = True，表示以字符串的格式，存储数据，否则将以二进制存储数据
conn.set('k1','v1')
value = conn.get('k1')
print(value)
```

```python
from redis import Redis

'''
	一般连接，使用StrictRedis连接
'''
conn = StrictRedis(host='localhost',port='6379',password='foobared',db=0,decode_responsed=True)

conn.set('k1','v1')
value = conn.get('k1')
print(value)
```

redis-py提供了两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，Redis是StrcitRedis子类，用于向后兼容旧版本的redis-py

#### 7.1.2.使用连接池

```python
from redis import Redis
from redis import ConnectionPool

'''
	使用连接池，连接Redis库的Redis
'''
# 创建pool
pool = ConnectionPool(host = 'localhost',port = '6379',password = 'foobared',db = 0,decode_responses = True)
#传入pool
conn = Redis(connection_pool = pool)
#下方是获取操作的结果
value1 = conn.hget('mark','name')
value2 = conn.hmget('mark','name','age','h')
value3 = conn.hgeall('mark')

# 下方是输出操作结果
print(value1,type(value1),sep='类型是：')
print(value2,type(value2),sep='类型是：')
print(value3,type(value3),sep='类型是：')
```

```python
from redis import Redis
from redis import ConnectionPool

'''
	使用连接池，连接Redis库的StrictRedis
'''
pool = ConnectionPool(host='lcoahost',port='6379',password='foobared',db=0,decode_responses=True)
conn = StrictRedis(connection_pool = pool)

#下方是获取操作的结果
value1 = conn.hget('mark','name')
value2 = conn.hmget('mark','name','age','h')
value3 = conn.hgeall('mark')

# 下方是输出操作结果
print(value1,type(value1),sep='类型是：')
print(value2,type(value2),sep='类型是：')
print(value3,type(value3),sep='类型是：')
```

redis-py使用connection_pool来管理对一个redis-server的所有连接，避免每次建立、释放连接的开销，默认，每个Redis实例都会维护一个自己的连接池。

可以直接建立一个连接池，然后作为参数Redis，这样就可以实现**多个Redis实例共享一个连接池**

```python
import redis

kwargs = {
    'hosts':'127.0.0.1',
    'port':'6379',
    'decode_responses':'True',
    'retry_on_timeout':3,
    'max_connections':1024 # 默认2^31
}
```

