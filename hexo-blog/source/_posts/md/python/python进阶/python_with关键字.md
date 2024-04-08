---
title: 'python_with关键字'
date: 2022-8-9 09:03:02
cover: false
---



## 1. 上下文管理器概念

Context Manager指的是python在执行一段代码前后，做的一些预处理和后处理，使得代码块运行处于一个小的环境（surrounding），出了这个小环境之后，资源释放，环境中的各种配置也失效。

例如在打开文件需要关闭，连接数据库后需要关闭连接。很多优雅第三方库也会利用上下文使得对象进入特定的某种状态。

## 2. with关键字

with的基本用法如下：

```python
with EXPR as VAR:
  BLOCK
```

其中发生了一系列过程：

1. EXPR语句被执行，得到ContextManager
2. 调用ContextManager.__enter__方法
3. 如果有as VAR，则ContextManager.__enter__的返回值赋给VAR，否则就不管返回值
4. 执行BLOCK，如果有VAR被用到，就和普通变量一样
5. 调用ContextManager.__exit__方法
   - __exit__有三个参数：type, value, traceback，BLOCK出异常时会得到对应值，正常情况就都为None
   - __exit__返回值为True表示BLOCK中出现的异常可以忽略，False表示需要raise

## 3. 例子

### 3.1 资源操作：

```python
class CustomOpen:
    def __init__(self, filename: str):
        self.__filename = filename
        self.__handler = None
    
    def __enter__(self):
        print("enter......")
        self.__handler = open(self.__filename)
        return self.__handler
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit...", exc_type, exc_val, exc_tb)
        if self.__handler is not None:
            self.__handler.close()
        return True


with CustomOpen("hello.txt") as f:
    print(f.read())
```

运行结果：

```bash
enter......
hello world
exit... None None None
```

### 3.2 状态维护

```python
class CustomBrain:
    def __init__(self):
        self.__status = "normal"
    
    def say(self):
        if self.__status == "normal":
            print("You're a great man")
        elif self.__status == "special":
            print("You are a very outstanding person ")

    def __enter__(self):
        self.__status = "special"

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__status = "normal"


brain = CustomBrain()
brain.say() # 普通状态

# 可以通过上下文维护一些状态
with brain:
    brain.say() # 特殊状态

brain.say() # 普通状态
```

运行结果：

```bash
You're a great man
You are a very outstanding person
You're a great man
```

## 4. 使用contextlib简化编写

python内置的标准库contextlib可以是的代码书写更加简洁，本质是一样的。比较有用的是contextlib.contextmanager这个装饰器，被装饰的函数在yield的前面相当于__enter__，yield的后面相当于__exit__，yield本身的返回值赋给as后的变量

所以第一个示例可以这么写：

```python
from contextlib import contextmanager

@contextmanager
def custom_open(filename: str):
    print("enter......")
    handler = open(filename)

    yield handler

    print("exit...")
    handler.close()


with custom_open("hello.txt") as f:
    print(f.read())
```

还是优雅了许多~