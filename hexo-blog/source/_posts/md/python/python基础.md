---
title: 'python'
date: 2023-04-01 09:03:02
cover: false
tags:
- python
categories: python
typora-root-url: python基础
---

# 环境搭建

见《python环境》篇

# 基本概念

[Python 教程 — Python 3.11.3 文档](https://docs.python.org/zh-cn/3/tutorial/index.html)

## python解释器

### 调用解释器

#### 传入参数

解释器读取命令行参数，把脚本名与其他参数转化为字符串列表存到 `sys` 模块的 `argv` 变量里。

#### 交互模式

进入解释器时，首先显示欢迎信息、版本信息、版权声明，然后才是提示符：

```bash
python3.11
Python 3.11 (default, April 4 2021, 09:25:04)
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### 解释器运行环境

#### 源文件字符编码

默认情况下，Python 源码文件的编码是 UTF-8。

如果不使用默认编码，则要声明文件的编码，文件的 *第一* 行要写成特殊注释。句法如下：

```python
# -*- coding: cp1252 -*-
```

*第一行* 的规则也有一种例外情况，源码以 [UNIX "shebang" 行](https://docs.python.org/zh-cn/3/tutorial/appendix.html#tut-scripts) 开头。此时，编码声明要写在文件的第二行。例如：

```python
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
```

> Unix 系统中，为了不与同时安装的 Python 2.x 冲突，Python 3.x 解释器默认安装的执行文件名不是 `python`。
>
> 如果加了第一行，要考虑实际环境的python的默认执行命令是哪一个

### 命令行与环境

[命令行与环境](https://docs.python.org/zh-cn/3/using/cmdline.html#)

#### 命令行

接口选项

- 解释器接口类似于 UNIX shell，但提供了额外的调用方法:
  - 用连接到 tty 设备的标准输入调用时，会提示输入并执行命令，输入 EOF （文件结束符，UNIX 中按 Ctrl-D，Windows 中按 Ctrl-Z, Enter）时终止。
  - 用文件名参数或以标准输入文件调用时，读取，并执行该脚本文件。
  - 用目录名参数调用时，从该目录读取、执行适当名称的脚本。
  - 用 `-c command` 调用时，执行 *command* 表示的 Python 语句。*command* 可以包含用换行符分隔的多条语句。注意，前导空白字符在 Python 语句中非常重要！
  - 用 `-m module-name` 调用时，在 Python 模块路径中查找指定的模块，并将其作为脚本执行。
- 非交互模式下，先解析全部输入，再执行。

#### 环境变量

[环境变量](https://docs.python.org/zh-cn/3/using/cmdline.html#environment-variables)

## python速览

### 数字

进入python解释器

解释器像一个简单的计算器：输入表达式，就会给出答案。表达式的语法很直接：运算符 `+`、`-`、`*`、`/` 的用法和其他大部分语言一样（比如，Pascal 或 C）；括号 (`()`) 用来分组。例如：

```python
2 + 2
4

50 - 5*6
20

(50 - 5*6) / 4
5.0

8 / 5  # division always returns a floating point number
1.6
```



```python
17 / 3  # classic division returns a float
5.666666666666667

17 // 3  # floor division discards the fractional part
5

17 % 3  # the % operator returns the remainder of the division
2

5 * 3 + 2  # floored quotient * divisor + remainder
17
```



```python
5 ** 2  # 5 squared
25

2 ** 7  # 2 to the power of 7
128
```

等号（`=`）用于给变量赋值。赋值后，下一个交互提示符的位置不显示任何结果：

```python
width = 20
height = 5 * 9
width * height
900
```

Python 全面支持浮点数；混合类型运算数的运算会把整数转换为浮点数：

```python
4 * 3.75 - 1
14.0
```

交互模式下，上次输出的表达式会赋给变量 `_`。把 Python 当作计算器时，用该变量实现下一步计算更简单，例如：

```python
tax = 12.5 / 100
price = 100.50
price * tax
12.5625
price + _
113.0625
round(_, 2)
113.06
```

最好把该变量当作只读类型。不要为它显式赋值，否则会创建一个同名独立局部变量，该变量会用它的魔法行为屏蔽内置变量。

除了 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 和 [`float`](https://docs.python.org/zh-cn/3/library/functions.html#float)，Python 还支持其他数字类型，例如 [`Decimal`](https://docs.python.org/zh-cn/3/library/decimal.html#decimal.Decimal) 或 [`Fraction`](https://docs.python.org/zh-cn/3/library/fractions.html#fractions.Fraction)。Python 还内置支持 [复数](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesnumeric)，后缀 `j` 或 `J` 用于表示虚数（例如 `3+5j` ）。

### 字符串

[内置类型 — Python 3.11.3 文档](https://docs.python.org/zh-cn/3/library/stdtypes.html#textseq)

#### 字符串定义与输出

字符串有多种表现形式，用单引号（`'……'`）或双引号（`"……"`）标注的结果相同 。反斜杠 `\` 用于转义：

```python
'spam eggs'  # single quotes
'spam eggs'

'doesn\'t'  # use \' to escape the single quote...
"doesn't"

"doesn't"  # ...or use double quotes instead
"doesn't"

'"Yes," they said.'
'"Yes," they said.'

"\"Yes,\" they said."
'"Yes," they said.'

'"Isn\'t," they said.'
'"Isn\'t," they said.'
```

交互式解释器会为输出的字符串加注引号，特殊字符使用反斜杠转义。虽然，有时输出的字符串看起来与输入的字符串不一样（外加的引号可能会改变），但两个字符串是相同的。如果字符串中有单引号而没有双引号，该字符串外将加注双引号，反之，则加注单引号。[`print()`](https://docs.python.org/zh-cn/3/library/functions.html#print) 函数输出的内容更简洁易读，它会省略两边的引号，并输出转义后的特殊字符：

```python
'"Isn\'t," they said.'
'"Isn\'t," they said.'
print('"Isn\'t," they said.')
"Isn't," they said.
s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output
'First line.\nSecond line.'
print(s)  # with print(), \n produces a new line
First line.
Second line.
```



#### 避免转义

在Python的string前面加上‘r’， 是为了告诉编译器这个string是个raw string，不要转意backslash ‘\’ 。 例如，\n 在raw string中，是两个字符，\和n， 而不会转意为换行符。由于正则表达式和 \ 会有冲突，因此，当一个字符串使用了正则表达式后，最好在前面加上’r’。

```python
s=r'\tt'
print(s)
Output:
'\tt'
 
s='\tt'
print(s)
Output:
'        t'
```



#### 多行字符串

字符串字面值可以包含多行。 一种实现方式是使用三重引号：`"""..."""` 或 `'''...'''`。 字符串中将自动包括行结束符，但也可以在换行的地方添加一个 `\` 来避免此情况。 参见以下示例：

```python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```



#### 字符串拼接

字符串可以用 `+` 合并（粘到一起），也可以用 `*` 重复：

```python
# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'
'unununium'
```

相邻的两个或多个 *字符串字面值* （引号标注的字符）会自动合并：

```python
'Py' 'thon'
'Python'
```

![image-20230420090921211](image-20230420090921211.png)

拼接分隔开的长字符串时，这个功能特别实用：

```python
text = ('Put several strings within parentheses '
        'to have them joined together.')
text
'Put several strings within parentheses to have them joined together.'
```

这项功能只能用于两个字面值，不能用于变量或表达式：

```python
prefix = 'Py'
prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
           ^^^^^^
SyntaxError: invalid syntax
('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
               ^^^^^
SyntaxError: invalid syntax
```

合并多个变量，或合并变量与字面值，要用 `+`：

```python
prefix + 'thon'
'Python'
```



#### 字符串索引

字符串支持 *索引* （下标访问），第一个字符的索引是 0。单字符没有专用的类型，就是长度为一的字符串：

```python
word = 'Python'
word[0]  # character in position 0
'P'
word[5]  # character in position 5
'n'
```

索引还支持负数，用负数索引时，从右边开始计数：

```
word[-1]  # last character
'n'
word[-2]  # second-last character
'o'
word[-6]
'P'
```

注意，-0 和 0 一样，因此，负数索引从 -1 开始。

#### 字符串切片

索引可以提取单个字符，*切片* 则提取子字符串：

左闭右开，不同于下标访问，切片索引从字符中间开始计算

```python
word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
```

切片索引的默认值很有用；省略开始索引时，默认值为 0，省略结束索引时，默认为到字符串的结尾：

```python
word[:2]   # character from the beginning to position 2 (excluded)
'Py'
word[4:]   # characters from position 4 (included) to the end
'on'
word[-2:]  # characters from the second-last (included) to the end
'on'
```

注意，输出结果包含切片开始，但不包含切片结束。因此，`s[:i] + s[i:]` 总是等于 `s`：

```python
word[:2] + word[2:]
'Python'
word[:4] + word[4:]
'Python'
```

还可以这样理解切片，索引指向的是字符 *之间* ，第一个字符的左侧标为 0，最后一个字符的右侧标为 *n* ，*n* 是字符串长度。例如：

```python
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

第一行数字是字符串中索引 0...6 的位置，第二行数字是对应的负数索引位置。*i* 到 *j* 的切片由 *i* 和 *j* 之间所有对应的字符组成。

对于使用非负索引的切片，如果两个索引都不越界，切片长度就是起止索引之差。例如， `word[1:3]` 的长度是 2。

索引越界会报错：

```python
word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

但是，切片会自动处理越界索引：

```python
word[4:42]
'on'
word[42:]
''
```

Python 字符串不能修改，是 [immutable](https://docs.python.org/zh-cn/3/glossary.html#term-immutable) 的。因此，为字符串中某个索引位置赋值会报错：

```python
word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

要生成不同的字符串，应新建一个字符串：

```python
'J' + word[1:]
'Jython'
word[:2] + 'py'
'Pypy'
```

内置函数 [`len()`](https://docs.python.org/zh-cn/3/library/functions.html#len) 返回字符串的长度：

```python
s = 'supercalifragilisticexpialidocious'
len(s)
34
```



### 列表

Python 支持多种 *复合* 数据类型，可将不同值组合在一起。最常用的 *列表* ，是用方括号标注，逗号分隔的一组值。*列表* 可以包含不同类型的元素，但一般情况下，各个元素的类型相同：

```python
squares = [1, 4, 9, 16, 25]
squares
[1, 4, 9, 16, 25]
```

和字符串（及其他内置 [sequence](https://docs.python.org/zh-cn/3/glossary.html#term-sequence) 类型）一样，列表也支持索引和切片：

```python
squares[0]  # indexing returns the item
1
squares[-1]
25
squares[-3:]  # slicing returns a new list
[9, 16, 25]
```

切片操作返回包含请求元素的新列表。以下切片操作会返回列表的 [浅拷贝](https://docs.python.org/zh-cn/3/library/copy.html#shallow-vs-deep-copy)：

```python
squares[:]
[1, 4, 9, 16, 25]
```

列表还支持合并操作：

```python
squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

与 [immutable](https://docs.python.org/zh-cn/3/glossary.html#term-immutable) 字符串不同, 列表是 [mutable](https://docs.python.org/zh-cn/3/glossary.html#term-mutable) 类型，其内容可以改变：

```python
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!
64
cubes[3] = 64  # replace the wrong value
cubes
[1, 8, 27, 64, 125]
```

`append()` *方法* 可以在列表结尾添加新元素（详见后文）:

```python
cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```

为切片赋值可以改变列表大小，甚至清空整个列表：

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
letters
['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
letters
[]
```

内置函数 [`len()`](https://docs.python.org/zh-cn/3/library/functions.html#len) 也支持列表：

```python
letters = ['a', 'b', 'c', 'd']
len(letters)
4
```

还可以嵌套列表（创建包含其他列表的列表），例如：

```python
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
[['a', 'b', 'c'], [1, 2, 3]]
x[0]
['a', 'b', 'c']
x[0][1]
'b'
```

以相同索引遍历两个列表

```python
for item1, item2 in zip(list1, list2):
    pritn(item1, item2)
```



## 流程控制

### if

if 语句包含零个或多个 [`elif`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#elif) 子句及可选的 [`else`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#else) 子句。关键字 '`elif`' 是 'else if' 的缩写，适用于避免过多的缩进。`if` ... `elif` ... `elif` ... 序列可以当作其他语言中 `switch` 或 `case` 语句的替代品。

如果要把一个值与多个常量进行比较，或者检查特定类型或属性，`match` 语句更实用。函数

```python
x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
```

### while



### for

Python 的 `for` 语句不迭代算术递增数值（如 Pascal），或是给予用户定义迭代步骤和暂停条件的能力（如 C），而是迭代列表或字符串等任意序列，元素的迭代顺序与在序列中出现的顺序一致。 例如：

```python
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
    
cat 3
window 6
defenestrate 12
```

遍历集合时修改集合的内容，会很容易生成错误的结果。因此不能直接进行循环，而是应遍历该集合的副本或创建新的集合：

```python
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

### range（）函数

内置函数 [`range()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#range) 常用于遍历数字序列，该函数可以生成算术级数：

```python
for i in range(5):
...     print(i)
...
0
1
2
3
4
```

生成的序列不包含给定的终止数值；`range(10)` 生成 10 个值，这是一个长度为 10 的序列，其中的元素索引都是合法的。range 可以不从 0 开始，还可以按指定幅度递增（递增幅度称为 '步进'，支持负数）：

```python
ist(range(5, 10))
[5, 6, 7, 8, 9]

>>> list(range(0, 10, 3))
[0, 3, 6, 9]

>>> list(range(-10, -100, -30))
[-10, -40, -70]
```

[`range()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#range) 和 [`len()`](https://docs.python.org/zh-cn/3/library/functions.html#len) 组合在一起，可以按索引迭代序列：

```python
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

0 Mary
1 had
2 a
3 little
4 lamb
```

不过，大多数情况下，[`enumerate()`](https://docs.python.org/zh-cn/3/library/functions.html#enumerate) 函数更便捷，详见 [循环的技巧](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#tut-loopidioms) 。

如果只输出 range，会出现意想不到的结果：

```python
range(10)
range(0, 10)
```

[`range()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#range) 返回对象的操作和列表很像，但其实这两种对象不是一回事。迭代时，该对象基于所需序列返回连续项，并没有生成真正的列表，从而节省了空间。

这种对象称为可迭代对象 [iterable](https://docs.python.org/zh-cn/3/glossary.html#term-iterable)，函数或程序结构可通过该对象获取连续项，直到所有元素全部迭代完毕。[`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 语句就是这样的架构，[`sum()`](https://docs.python.org/zh-cn/3/library/functions.html#sum) 是一种把可迭代对象作为参数的函数：

```python
sum(range(4))  # 0 + 1 + 2 + 3
6
```

下文将介绍更多返回可迭代对象或把可迭代对象当作参数的函数。 在 [数据结构](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#tut-structures) 这一章节中，我们将讨论有关 [`list()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list) 的更多细节。

### break、continue及else子句

[`break`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#break) 语句和 C 中的类似，用于跳出最近的 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 或 [`while`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#while) 循环。

循环语句支持 `else` 子句；[`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 循环中，可迭代对象中的元素全部循环完毕，或 [`while`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#while) 循环的条件为假时，执行该子句；[`break`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#break) 语句终止循环时，不执行该子句。 请看下面这个查找素数的循环示例：

```python
for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

（没错，这段代码就是这么写。仔细看：else 子句属于 for 循环，不属于 if 语句。）

与 [`if`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#if) 语句相比，循环的 `else` 子句更像 [`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 的 `else` 子句： [`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 的 `else` 子句在未触发异常时执行，循环的 `else` 子句则在未运行 `break` 时执行。`try` 语句和异常详见 [异常的处理](https://docs.python.org/zh-cn/3/tutorial/errors.html#tut-handling)。

[`continue`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#continue) 语句也借鉴自 C 语言，表示继续执行循环的下一次迭代：

```python
for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found an odd number", num)
...
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```

### pass

[`pass`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#pass) 语句不执行任何操作。语法上需要一个语句，但程序不实际执行任何动作时，可以使用该语句。例如：

```python
while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...
```

[`pass`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#pass) 还可以用作函数或条件子句的占位符，让开发者聚焦更抽象的层次。此时，程序直接忽略 `pass`：

```pyton
def initlog(*args):
...     pass   # Remember to implement this!
...
```

### match

最简单的形式是将一个目标值与一个或多个字面值进行比较：

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

注意最后一个代码块：“变量名” `_` 被作为 *通配符* 并必定会匹配成功。 如果没有 case 语句匹配成功，则不会执行任何分支。

使用 `|` （“ or ”）在一个模式中可以组合多个字面值：

```python
case 401 | 403 | 404:
    return "Not allowed"
```



模式的形式类似解包赋值，并可被用于绑定变量：

```python
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

请仔细研究此代码！ 第一个模式有两个字面值，可以看作是上面所示字面值模式的扩展。但接下来的两个模式结合了一个字面值和一个变量，而变量 **绑定** 了一个来自目标的值（`point`）。第四个模式捕获了两个值，这使得它在概念上类似于解包赋值 `(x, y) = point`。

## 函数

### 定义函数

下列代码创建一个可以输出限定数值内的斐波那契数列函数：

```python
def fib(n):    # write Fibonacci series up to n
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

*定义* 函数使用关键字 [`def`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#def)，后跟函数名与括号内的形参列表。函数语句从下一行开始，并且必须缩进。

函数内的第一条语句是字符串时，该字符串就是文档字符串，也称为 *docstring*，详见 [文档字符串](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#tut-docstrings)。利用文档字符串可以自动生成在线文档或打印版文档，还可以让开发者在浏览代码时直接查阅文档；Python 开发者最好养成在代码中加入文档字符串的好习惯。

函数在 *执行* 时使用函数局部变量符号表，所有函数变量赋值都存在局部符号表中；引用变量时，首先，在局部符号表里查找变量，然后，是外层函数局部符号表，再是全局符号表，最后是内置名称符号表。因此，尽管可以引用全局变量和外层函数的变量，但最好不要在函数内直接赋值（除非是 [`global`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 语句定义的全局变量，或 [`nonlocal`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) 语句定义的外层函数变量）。

在调用函数时会将实际参数（实参）引入到被调用函数的局部符号表中；因此，实参是使用 *按值调用* 来传递的（其中的 *值* 始终是对象的 *引用* 而不是对象的值）。当一个函数调用另外一个函数时，会为该调用创建一个新的局部符号表。

函数定义在当前符号表中把函数名与函数对象关联在一起。解释器把函数名指向的对象作为用户自定义函数。还可以使用其他名称指向同一个函数对象，并访问访该函数：

```python
fib
<function fib at 10042ed0>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89
```

`fib` 不返回值，因此，其他语言不把它当作函数，而是当作过程。事实上，没有 [`return`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#return) 语句的函数也返回值，只不过这个值比较是 `None` （是一个内置名称）。一般来说，解释器不会输出单独的返回值 `None` ，如需查看该值，可以使用 [`print()`](https://docs.python.org/zh-cn/3/library/functions.html#print)：

```python
fib(0)
>>> print(fib(0))
None
```

### 函数定义详解

函数定义支持可变数量的参数。这里列出三种可以组合使用的形式。

#### 默认值参数

为参数指定默认值是非常有用的方式。调用函数时，可以使用比定义时更少的参数，例如：

```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

该函数可以用以下方式调用：

- 只给出必选实参：`ask_ok('Do you really want to quit?')`
- 给出一个可选实参：`ask_ok('OK to overwrite the file?', 2)`
- 给出所有实参：`ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')`

本例还使用了关键字 [`in`](https://docs.python.org/zh-cn/3/reference/expressions.html#in) ，用于确认序列中是否包含某个值。

默认值在 *定义* 作用域里的函数定义中求值，所以：

```python
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
```

上例输出的是 `5`。

**重要警告：** 默认值只计算一次。默认值为列表、字典或类实例等可变对象时，会产生与该规则不同的结果。例如，下面的函数会累积后续调用时传递的参数：

```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```

输出结果如下：

```python
[1]
[1, 2]
[1, 2, 3]
```

不想在后续调用之间共享默认值时，应以如下方式编写函数：

```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

#### 关键字参数

`kwarg=value` 形式的 [关键字参数](https://docs.python.org/zh-cn/3/glossary.html#term-keyword-argument) 也可以用于调用函数。函数示例如下：

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```

该函数接受一个必选参数（`voltage`）和三个可选参数（`state`, `action` 和 `type`）。该函数可用下列方式调用：

```python
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```

以下调用函数的方式都**无效**：

```python
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
```

函数调用时，关键字参数必须跟在位置参数后面。所有传递的关键字参数都必须匹配一个函数接受的参数（比如，`actor` 不是函数 `parrot` 的有效参数），关键字参数的顺序并不重要。这也包括必选参数，（比如，`parrot(voltage=1000)` 也有效）。不能对同一个参数多次赋值，下面就是一个因此限制而失败的例子：

```python
def function(a):
...     pass
...
>>> function(0, a=0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function() got multiple values for argument 'a'
```

最后一个形参为 `**name` 形式时，接收一个字典（详见 [映射类型 --- dict](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesmapping)），该字典包含与函数中已定义形参对应之外的所有关键字参数。`**name` 形参可以与 `*name` 形参（下一小节介绍）组合使用（`*name` 必须在 `**name` 前面）， `*name` 形参接收一个 [元组](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#tut-tuples)，该元组包含形参列表之外的位置参数。例如，可以定义下面这样的函数：

```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
```

该函数可以用如下方式调用：

```python
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```

输出结果如下：

```
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
```



```python
def cheeseshop(kind, *arguments, **keywords):
    print(arguments) # ('b', 'c')
    print(keywords) # {'name': 'd', 'age': 12}

cheeseshop('a','b','c',name='d',age=12)
```

注意，关键字参数在输出结果中的顺序与调用函数时的顺序一致。



#### 特殊参数

默认情况下，参数可以按位置或显式关键字传递给 Python 函数。为了让代码易读、高效，最好限制参数的传递方式，这样，开发者只需查看函数定义，即可确定参数项是仅按位置、按位置或关键字，还是仅按关键字传递。

函数定义如下：

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

`/` 和 `*` 是可选的。这些符号表明形参如何把参数值传递给函数：位置、位置或关键字、关键字。关键字形参也叫作命名形参。

**位置或关键字参数**

函数定义中未使用 `/` 和 `*` 时，参数可以按位置或关键字传递给函数。

 **仅位置参数**

此处再介绍一些细节，特定形参可以标记为 *仅限位置*。*仅限位置* 时，形参的顺序很重要，且这些形参不能用关键字传递。仅限位置形参应放在 `/` （正斜杠）前。`/` 用于在逻辑上分割仅限位置形参与其它形参。如果函数定义中没有 `/`，则表示没有仅限位置形参。

`/` 后可以是 *位置或关键字* 或 *仅限关键字* 形参。

**仅限关键字参数**

把形参标记为 *仅限关键字*，表明必须以关键字参数形式传递该形参，应在参数列表中第一个 *仅限关键字* 形参前添加 `*`。

**函数示例**

请看下面的函数定义示例，注意 `/` 和 `*` 标记：

```python
def standard_arg(arg):
...     print(arg)
...
>>> def pos_only_arg(arg, /):
...     print(arg)
...
>>> def kwd_only_arg(*, arg):
...     print(arg)
...
>>> def combined_example(pos_only, /, standard, *, kwd_only):
...     print(pos_only, standard, kwd_only)
```



下面的函数定义中，`kwds` 把 `name` 当作键，因此，可能与位置参数 `name` 产生潜在冲突：

```python
def foo(name, **kwds):
    return 'name' in kwds
```

调用该函数不可能返回 `True`，因为关键字 `'name'` 总与第一个形参绑定。例如：

```python
foo(1, **{'name': 2})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
>>>
```

加上 `/` （仅限位置参数）后，就可以了。此时，函数定义把 `name` 当作位置参数，`'name'` 也可以作为关键字参数的键：

```
def foo(name, /, **kwds):
...     return 'name' in kwds
...
>>> foo(1, **{'name': 2})
True
```

换句话说，仅限位置形参的名称可以在 `**kwds` 中使用，而不产生歧义。

**小结**

以下用例决定哪些形参可以用于函数定义：

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
```

说明：

- 使用仅限位置形参，可以让用户无法使用形参名。形参名没有实际意义时，强制调用函数的实参顺序时，或同时接收位置形参和关键字时，这种方式很有用。
- 当形参名有实际意义，且显式名称可以让函数定义更易理解时，阻止用户依赖传递实参的位置时，才使用关键字。
- 对于 API，使用仅限位置形参，可以防止未来修改形参名时造成破坏性的 API 变动。



### 任意实参列表

调用函数时，使用任意数量的实参是最少见的选项。这些实参包含在元组中（详见 [元组和序列](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#tut-tuples) ）。在可变数量的实参之前，可能有若干个普通参数：

```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```

*variadic* 参数用于采集传递给函数的所有剩余参数，因此，它们通常在形参列表的末尾。`*args` 形参后的任何形式参数只能是仅限关键字参数，即只能用作关键字参数，不能用作位置参数：

```python
def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
```

### 解包实参列表

函数调用要求独立的位置参数，但实参在列表或元组里时，要执行相反的操作。例如，内置的 [`range()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#range) 函数要求独立的 *start* 和 *stop* 实参。如果这些参数不是独立的，则要在调用函数时，用 `*` 操作符把实参从列表或元组解包出来：

```python
list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
```



同样，字典可以用 `**` 操作符传递关键字参数：

```python
def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "def ": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```



```python
def show(name, age):
    print(name, age)  # sai 12

show(**{"name": "sai", "age": 12})

```

### Lambda 表达式

[`lambda`](https://docs.python.org/zh-cn/3/reference/expressions.html#lambda) 关键字用于创建小巧的匿名函数。`lambda a, b: a+b` 函数返回两个参数的和。Lambda 函数可用于任何需要函数对象的地方。在语法上，匿名函数只能是单个表达式。在语义上，它只是常规函数定义的语法糖。与嵌套函数定义一样，lambda 函数可以引用包含作用域中的变量：

```python
def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

上例用 lambda 表达式返回函数。还可以把匿名函数用作传递的实参：

```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

### 文档字符串

以下是文档字符串内容和格式的约定。

第一行应为对象用途的简短摘要。为保持简洁，不要在这里显式说明对象名或类型，因为可通过其他方式获取这些信息（除非该名称碰巧是描述函数操作的动词）。这一行应以大写字母开头，以句点结尾。

文档字符串为多行时，第二行应为空白行，在视觉上将摘要与其余描述分开。后面的行可包含若干段落，描述对象的调用约定、副作用等。

Python 解析器不会删除 Python 中多行字符串字面值的缩进，因此，文档处理工具应在必要时删除缩进。这项操作遵循以下约定：文档字符串第一行 *之后* 的第一个非空行决定了整个文档字符串的缩进量（第一行通常与字符串开头的引号相邻，其缩进在字符串中并不明显，因此，不能用第一行的缩进），然后，删除字符串中所有行开头处与此缩进“等价”的空白符。不能有比此缩进更少的行，但如果出现了缩进更少的行，应删除这些行的所有前导空白符。转化制表符后（通常为 8 个空格），应测试空白符的等效性。

下面是多行文档字符串的一个例子：

```python
def my_function():
    """Do nothing, but document it.

     No, really, it doesn't do anything.
     """
    pass

print(my_function.__doc__)
Do nothing, but document it.

    No, really, it doesn't do anything.
```

### 函数注解

[函数注解](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#function) 是可选的用户自定义函数类型的元数据完整信息

[标注](https://docs.python.org/zh-cn/3/glossary.html#term-function-annotation) 以字典的形式存放在函数的 `__annotations__` 属性中，并且不会影响函数的任何其他部分。 形参标注的定义方式是在形参名后加冒号，后面跟一个表达式，该表达式会被求值为标注的值。 返回值标注的定义方式是加组合符号 `->`，后面跟一个表达式，该标注位于形参列表和表示 [`def`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#def) 语句结束的冒号之间。 下面的示例有一个必须的参数，一个可选的关键字参数以及返回值都带有相应的标注:

```python
def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

### 编码风格

现在你将要写更长，更复杂的 Python 代码，是时候讨论一下 *代码风格* 了。 大多数语言都能以不同的风格被编写（或更准确地说，被格式化）；有些比其他的更具有可读性。 能让其他人轻松阅读你的代码总是一个好主意，采用一种好的编码风格对此有很大帮助。

Python 项目大多都遵循 [**PEP 8**](https://peps.python.org/pep-0008/) 的风格指南；它推行的编码风格易于阅读、赏心悦目。Python 开发者均应抽时间悉心研读；以下是该提案中的核心要点：

- 缩进，用 4 个空格，不要用制表符。

  4 个空格是小缩进（更深嵌套）和大缩进（更易阅读）之间的折中方案。制表符会引起混乱，最好别用。

- 换行，一行不超过 79 个字符。

  这样换行的小屏阅读体验更好，还便于在大屏显示器上并排阅读多个代码文件。

- 用空行分隔函数和类，及函数内较大的代码块。

- 最好把注释放到单独一行。

- 使用文档字符串。

- 运算符前后、逗号后要用空格，但不要直接在括号内使用： `a = f(1, 2) + g(3, 4)`。

- 类和函数的命名要一致；按惯例，命名类用 `UpperCamelCase`，命名函数与方法用 `lowercase_with_underscores`。命名方法中第一个参数总是用 `self` (类和方法详见 [初探类](https://docs.python.org/zh-cn/3/tutorial/classes.html#tut-firstclasses))。

- 编写用于国际多语环境的代码时，不要用生僻的编码。Python 默认的 UTF-8 或纯 ASCII 可以胜任各种情况。

- 同理，就算多语阅读、维护代码的可能再小，也不要在标识符中使用非 ASCII 字符。

### `lambda`表达式

1、在python中，函数是一个被命名的、独立完成特定功能的一段代码，并可能给调用它的程序一个返回值。

​    ①普通函数：有名函数

​    ②匿名函数：为简化程序代码，可定义匿名函数

2、[lambda表达式](https://so.csdn.net/so/search?q=lambda表达式&spm=1001.2101.3001.7020)的应用场景：若函数有一个返回值，并且只有一行简单的代码，可使用lambda简化

3、lambda表达式的基本语法

```bash
变量 = lambda 函数参数：表达式（函数代码+return返回值）
#调用变量
变量()
#注意只能返回一个值，若要返回多个值，则封装到列表、字典等数据类型中
```

4、编写lambda表达式

（1）定义一个函数，经过一系列操作，返回100(无参数):

```python
def f1():
	return 100
print(f1)#代表f()函数在内存中的地址
print(f1())#代表找到f()函数的地址并立即执行
```

 lambda简化：

```python
f2=lambda:100
print(f2)
print(f2())
```

 （2）求两数之和(有参数)：

```python
def f1(num1,num2):
	return num1+num2
print(f1(10,20))
```

  lambda简化：

```python
f2 = lambda num1,num2 : num1 + num2
print(f2)
print(f2(10,20))
```

6、lambda表达式相关应用

①带默认值的：

```python
f = lambda a,b,c = 100: a + b + c #c为默认值
print(f(10,20))
print(f(10,20,30))#此时30则将100覆盖，c等于30
```

  ②可变参数args（不定长参数）：

```python
f1 = lambda *args : args
print(f1(10,20,30,40))#函数识别的是*
 
#返回(10, 20, 30, 40)
```

 ③关键字参数`**kwargs`:

```python
f2 = lambda **kwargs : kwargs#返回的是字典
print(f2(dict1=10,dict2=20,dict3=30))
 
#返回：{'dict1': 10, 'dict2': 20, 'dict3': 30}
```

 ④带if判断的lambda表达式（求两数的最大值）：

```python
f = lambda a,b:a if a > b else b
print(f(10,20))
```

⑤列表数据+字典数据排序

```python
students = [
	{'name':'tom' ,'age':20},
	{'name':'jack' ,'age':10},
	{'name':'jane' ,'age':15}
]
#按name值升序排列
students.sort(key=lambda x:x['name'])
print(students)
#按name值降序排列
students.sort(key=lambda x:x['name'],reverse = True)
print(students)
#按age值升序排列
students.sort(key=lambda x:x['age'])
print(students)
```



## 数据结构

### 列表

#### 列表方法

`list.append(x)`

- 在列表末尾添加一个元素，相当于 `a[len(a):] = [x]` 。

`list.extend(iterable)`

- 用可迭代对象的元素扩展列表。相当于 `a[len(a):] = iterable` 。

`list.insert(i, x)`

- 在指定位置插入元素。第一个参数是插入元素的索引，因此，`a.insert(0, x)` 在列表开头插入元素， `a.insert(len(a), x)` 等同于 `a.append(x)` 。

`list.remove(x)`

- 从列表中删除第一个值为 *x* 的元素。未找到指定元素时，触发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) 异常。

`list.pop([i])`

- 删除列表中指定位置的元素，并返回被删除的元素。未指定位置时，`a.pop()` 删除并返回列表的最后一个元素。（方法签名中 *i* 两边的方括号表示该参数是可选的，不是要求输入方括号。这种表示法常见于 Python 参考库）。

`list.clear()`

- 删除列表里的所有元素，相当于 `del a[:]` 。

`list.index(x[, start[, end]])`

- 返回列表中第一个值为 *x* 的元素的零基索引。未找到指定元素时，触发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) 异常。

  可选参数 *start* 和 *end* 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 *start* 参数。

`list.count(x)`

- 返回列表中元素 *x* 出现的次数。

`list.sort(*, key=None, reverse=False)`

- 就地排序列表中的元素（要了解自定义排序参数，详见 [`sorted()`](https://docs.python.org/zh-cn/3/library/functions.html#sorted)）。

`list.reverse()`

- 翻转列表中的元素。

`list.copy()`

- 返回列表的浅拷贝。相当于 `a[:]` 。



样例：

```python
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
2
fruits.count('tangerine')
0
fruits.index('banana')
3
fruits.index('banana', 4)  # Find next banana starting at position 4
6
fruits.reverse()
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
'pear'
```

#### 用列表实现堆栈

使用列表方法实现堆栈非常容易，最后插入的最先取出（“后进先出”）。把元素添加到堆栈的顶端，使用 `append()` 。从堆栈顶部取出元素，使用 `pop()` ，不用指定索引。例如：

```python
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
[3, 4, 5, 6, 7]
stack.pop()
7
stack
[3, 4, 5, 6]
stack.pop()
6
stack.pop()
5
stack
[3, 4]
```

#### 用列表实现队列

列表也可以用作队列，最先加入的元素，最先取出（“先进先出”）；然而，列表作为队列的效率很低。因为，在列表末尾添加和删除元素非常快，但在列表开头插入或移除元素却很慢（因为所有其他元素都必须移动一位）。

实现队列最好用 [`collections.deque`](https://docs.python.org/zh-cn/3/library/collections.html#collections.deque)，可以快速从两端添加或删除元素。例如：

```python
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
'Eric'
queue.popleft()                 # The second to arrive now leaves
'John'
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

#### 列表推导式

列表推导式创建列表的方式更简洁。常见的用法为，对序列或可迭代对象中的每个元素应用某种操作，用生成的结果创建新的列表；或用满足特定条件的元素创建子序列。

例如，创建平方值的列表：

```python
squares = []
for x in range(10):
    squares.append(x**2)

squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

注意，这段代码创建（或覆盖）变量 `x`，该变量在循环结束后仍然存在。下述方法可以无副作用地计算平方列表：

```python
squares = list(map(lambda x: x**2, range(10)))
```

或等价于：

```python
squares = [x**2 for x in range(10)]
```

上面这种写法更简洁、易读。

列表推导式的方括号内包含以下内容：一个表达式，后面为一个 `for` 子句，然后，是零个或多个 `for` 或 `if` 子句。结果是由表达式依据 `for` 和 `if` 子句求值计算而得出一个新列表。 举例来说，以下列表推导式将两个列表中不相等的元素组合起来：

```python
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

等价于：

```python
combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

注意，上面两段代码中，[`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 和 [`if`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#if) 的顺序相同。

表达式是元组（例如上例的 `(x, y)`）时，必须加上括号：

```python
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]
[-8, -4, 0, 4, 8]
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
[0, 2, 4]
# apply a function to all the elements
[abs(x) for x in vec]
[4, 2, 0, 2, 4]
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
     ^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

列表推导式可以使用复杂的表达式和嵌套函数：

```python
from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

#### 嵌套的列表推导式

列表推导式中的初始表达式可以是任何表达式，甚至可以是另一个列表推导式。

下面这个 3x4 矩阵，由 3 个长度为 4 的列表组成：

```python
matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```

下面的列表推导式可以转置行列：

```python
[[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

等价于：

```python
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

反过来说，也等价于：

```python
transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

实际应用中，最好用内置函数替代复杂的流程语句。此时，[`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip) 函数更好用：

```
list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

#### 从列表中取n个元素

> https://zhuanlan.zhihu.com/p/585044711

有时，我们要从列表中取n个元素，我们通常可以采用以下几种方法：

- random.sample()

  ```python
  import random
  lst=["张三","李四","王五","赵六","麻七","侯八"]
  print(random.sample(lst,3))
  ```

- 列表推导式

  ```python
  import random
  lst=["张三","李四","王五","赵六","麻七","侯八"]
  print([random.choice(lst) for i in range(3)])
  ```

- iter()迭代函数实现按顺序取

  ```python
  lst=["张三","李四","王五","赵六","麻七","侯八"]
  print([(x,y,z) for x,y,z in zip(*[iter(lst)]*3)])  #这里如果按顺序取4个元素就把里面的3换成4
  ```

  ![image-20230516101721073](image-20230516101721073.png)

#### 在列表中插入另一个列表中的元素

> https://blog.csdn.net/qq_41289353/article/details/126880977

```python
lst1 = [1,2,3]
lst2 = [4,5]
lst1[1:1] = lst2
print(lst1)
# [1,4,5,2,3]
```

#### 打乱列表原顺序

> https://blog.csdn.net/zhangphil/article/details/88573760

```python
import random
 
array = list(range(0,10))
print("原来数据顺序:")
print(array)
 
random.shuffle(array)
 
print("打乱原顺序，新的随机数据:")
print(array)
```



### del语句

[`del`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#del) 语句按索引，而不是值从列表中移除元素。与返回值的 `pop()` 方法不同， `del` 语句也可以从列表中移除切片，或清空整个列表（之前是将空列表赋值给切片）。 例如：

```python
a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

[`del`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#del) 也可以用来删除整个变量：

```python
del a
```

此后，再引用 `a` 就会报错（直到为它赋与另一个值）。后文会介绍 [`del`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#del) 的其他用法。



### 元组和序列

列表和字符串有很多共性，例如，索引和切片操作。这两种数据类型是 *序列* （参见 [序列类型 --- list, tuple, range](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesseq)）。随着 Python 语言的发展，其他的序列类型也被加入其中。本节介绍另一种标准序列类型：*元组*。

元组由多个用逗号隔开的值组成，例如：

```python
t = 12345, 54321, 'hello!'
t[0]
12345
t
(12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable:
t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
([1, 2, 3], [3, 2, 1])
```

输出时，元组都要由圆括号标注，这样才能正确地解释嵌套元组。输入时，圆括号可有可无，不过经常是必须的（如果元组是更大的表达式的一部分）。不允许为元组中的单个元素赋值，当然，可以创建含列表等可变对象的元组。

虽然，元组与列表很像，但使用场景不同，用途也不同。元组是 [immutable](https://docs.python.org/zh-cn/3/glossary.html#term-immutable) （不可变的），一般可包含异质元素序列，通过解包（见本节下文）或索引访问（如果是 [`namedtuples`](https://docs.python.org/zh-cn/3/library/collections.html#collections.namedtuple)，可以属性访问）。列表是 [mutable](https://docs.python.org/zh-cn/3/glossary.html#term-mutable) （可变的），列表元素一般为同质类型，可迭代访问。

构造 0 个或 1 个元素的元组比较特殊：为了适应这种情况，对句法有一些额外的改变。用一对空圆括号就可以创建空元组；只有一个元素的元组可以通过在这个元素后添加逗号来构建（圆括号里只有一个值的话不够明确）。丑陋，但是有效。例如：

```python
empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)
0
len(singleton)
1
singleton
('hello',)
```

语句 `t = 12345, 54321, 'hello!'` 是 *元组打包* 的例子：值 `12345`, `54321` 和 `'hello!'` 一起被打包进元组。逆操作也可以：

```python
x, y, z = t
```

称之为 *序列解包* 也是妥妥的，适用于右侧的任何序列。序列解包时，左侧变量与右侧序列元素的数量应相等。注意，多重赋值其实只是元组打包和序列解包的组合。



### 集合

Python 还支持 *集合* 这种数据类型。集合是由不重复元素组成的无序容器。基本用法包括成员检测、消除重复元素。集合对象支持合集、交集、差集、对称差分等数学运算。

创建集合用花括号或 [`set()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set) 函数。注意，创建空集合只能用 `set()`，不能用 `{}`，`{}` 创建的是空字典，下一小节介绍数据结构：字典。

以下是一些简单的示例

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

'orange' in basket                 # fast membership testing

'crabgrass' in basket


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a

a - b                              # letters in a but not in b

a | b                              # letters in a or b or both

a & b                              # letters in both a and b

a ^ b                              # letters in a or b but not both
```

与 [列表推导式](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#tut-listcomps) 类似，集合也支持推导式：

```
a = {x for x in 'abracadabra' if x not in 'abc'}
a
```

### 字典

*字典* （参见 [映射类型 --- dict](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesmapping)） 也是一种常用的 Python 內置数据类型。其他语言可能把字典称为 *联合内存* 或 *联合数组*。与以连续整数为索引的序列不同，字典以 *关键字* 为索引，关键字通常是字符串或数字，也可以是其他任意不可变类型。只包含字符串、数字、元组的元组，也可以用作关键字。但如果元组直接或间接地包含了可变对象，就不能用作关键字。列表不能当关键字，因为列表可以用索引、切片、`append()` 、`extend()` 等方法修改。

可以把字典理解为 *键值对* 的集合，但字典的键必须是唯一的。花括号 `{}` 用于创建空字典。另一种初始化字典的方式是，在花括号里输入逗号分隔的键值对，这也是字典的输出方式。

字典的主要用途是通过关键字存储、提取值。用 `del` 可以删除键值对。用已存在的关键字存储值，与该关键字关联的旧值会被取代。通过不存在的键提取值，则会报错。

对字典执行 `list(d)` 操作，返回该字典中所有键的列表，按插入次序排列（如需排序，请使用 `sorted(d)`）。检查字典里是否存在某个键，使用关键字 [`in`](https://docs.python.org/zh-cn/3/reference/expressions.html#in)。

```python
tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

[`dict()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) 构造函数可以直接用键值对序列创建字典：

```python
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

字典推导式可以用任意键值表达式创建字典：

```python
{x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

关键字是比较简单的字符串时，直接用关键字参数指定键值对更便捷：

```python
dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

### 循环的技巧

在字典中循环时，用 `items()` 方法可同时取出键和对应的值：

```python
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

在序列中循环时，用 [`enumerate()`](https://docs.python.org/zh-cn/3/library/functions.html#enumerate) 函数可以同时取出位置索引和对应的值：

```
for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

同时循环两个或多个序列时，用 [`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip) 函数可以将其内的元素一一匹配：

```python
questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

逆向循环序列时，先正向定位序列，然后调用 [`reversed()`](https://docs.python.org/zh-cn/3/library/functions.html#reversed) 函数：

```python
for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```

按指定顺序循环序列，可以用 [`sorted()`](https://docs.python.org/zh-cn/3/library/functions.html#sorted) 函数，在不改动原序列的基础上，返回一个重新的序列：

```python
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```

使用 [`set()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set) 去除序列中的重复元素。使用 [`sorted()`](https://docs.python.org/zh-cn/3/library/functions.html#sorted) 加 [`set()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set) 则按排序后的顺序，循环遍历序列中的唯一元素：

```python
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```

一般来说，在循环中修改列表的内容时，创建新列表比较简单，且安全：

```python
import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

### 深入条件控制

`while` 和 `if` 条件句不只可以进行比较，还可以使用任意运算符。

比较运算符 `in` 和 `not in` 用于执行确定一个值是否存在（或不存在）于某个容器中的成员检测。 运算符 `is` 和 `is not` 用于比较两个对象是否是同一个对象。 所有比较运算符的优先级都一样，且低于任何数值运算符。

比较操作支持链式操作。例如，`a < b == c` 校验 `a` 是否小于 `b`，且 `b` 是否等于 `c`。

比较操作可以用布尔运算符 `and` 和 `or` 组合，并且，比较操作（或其他布尔运算）的结果都可以用 `not` 取反。这些操作符的优先级低于比较操作符；`not` 的优先级最高， `or` 的优先级最低，因此，`A and not B or C` 等价于 `(A and (not B)) or C`。与其他运算符操作一样，此处也可以用圆括号表示想要的组合。

布尔运算符 `and` 和 `or` 也称为 *短路* 运算符：其参数从左至右解析，一旦可以确定结果，解析就会停止。例如，如果 `A` 和 `C` 为真，`B` 为假，那么 `A and B and C` 不会解析 `C`。用作普通值而不是布尔值时，短路操作符返回的值通常是最后一个变量。

还可以把比较操作或逻辑表达式的结果赋值给变量，例如：

```python
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```

注意，Python 与 C 不同，在表达式内部赋值必须显式使用 [海象运算符](https://docs.python.org/zh-cn/3/faq/design.html#why-can-t-i-use-an-assignment-in-an-expression) `:=`。 这避免了 C 程序中常见的问题：要在表达式中写 `==` 时，却写成了 `=`。



### 序列和其他类型的比较

序列对象可以与相同序列类型的其他对象比较。这种比较使用 *字典式* 顺序：首先，比较前两个对应元素，如果不相等，则可确定比较结果；如果相等，则比较之后的两个元素，以此类推，直到其中一个序列结束。如果要比较的两个元素本身是相同类型的序列，则递归地执行字典式顺序比较。如果两个序列中所有的对应元素都相等，则两个序列相等。如果一个序列是另一个的初始子序列，则较短的序列可被视为较小（较少）的序列。 对于字符串来说，字典式顺序使用 Unicode 码位序号排序单个字符。下面列出了一些比较相同类型序列的例子：

```python
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```

注意，对不同类型的对象来说，只要待比较的对象提供了合适的比较方法，就可以使用 `<` 和 `>` 进行比较。例如，混合数值类型通过数值进行比较，所以，0 等于 0.0，等等。否则，解释器不会随便给出一个对比结果，而是触发 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError) 异常。

## 模块与包

[6. 模块 — Python 3.11.3 文档](https://docs.python.org/zh-cn/3/tutorial/modules.html)

退出 Python 解释器后，再次进入时，之前在 Python 解释器中定义的函数和变量就丢失了。因此，编写较长程序时，建议用文本编辑器代替解释器，执行文件中的输入内容，这就是编写 *脚本* 。随着程序越来越长，为了方便维护，最好把脚本拆分成多个文件。编写脚本还一个好处，不同程序调用同一个函数时，不用每次把函数复制到各个程序。

为实现这些需求，Python 把各种定义存入一个文件，在脚本或解释器的交互式实例中使用。这个文件就是 *模块* ；模块中的定义可以 *导入* 到其他模块或 *主* 模块（在顶层和计算器模式下，执行脚本中可访问的变量集）。

模块是包含 Python 定义和语句的文件。其文件名是模块名加后缀名 `.py` 。在模块内部，通过全局变量 `__name__` 可以获取模块名（即字符串）。例如，用文本编辑器在当前目录下创建 `fibo.py` 文件，输入以下内容：

```python
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

现在，进入 Python 解释器，用以下命令导入该模块：

```python
import fibo
```

This does not add the names of the functions defined in `fibo` directly to the current [namespace](https://docs.python.org/zh-cn/3/glossary.html#term-namespace) (see [Python 作用域和命名空间](https://docs.python.org/zh-cn/3/tutorial/classes.html#tut-scopes) for more details); it only adds the module name `fibo` there. Using the module name you can access the functions:

```python
fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

如果经常使用某个函数，可以把它赋值给局部变量：

```python
fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

### 模块详解

模块包含可执行语句及函数定义。这些语句用于初始化模块，且仅在 import 语句 第一次 遇到模块名时执行。 (文件作为脚本运行时，也会执行这些语句。)

Each module has its own private namespace, which is used as the global namespace by all functions defined in the module. Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user's global variables. On the other hand, if you know what you are doing you can touch a module's global variables with the same notation used to refer to its functions, `modname.itemname`.

Modules can import other modules. It is customary but not required to place all [`import`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) statements at the beginning of a module (or script, for that matter). The imported module names, if placed at the top level of a module (outside any functions or classes), are added to the module's global namespace.

There is a variant of the [`import`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) statement that imports names from a module directly into the importing module's namespace. For example:

```python
from fibo import fib, fib2
fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

This does not introduce the module name from which the imports are taken in the local namespace (so in the example, `fibo` is not defined).

还有一种变体可以导入模块内定义的所有名称：

```python
from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

这种方式会导入所有不以下划线（`_`）开头的名称。大多数情况下，不要用这个功能，这种方式向解释器导入了一批未知的名称，可能会覆盖已经定义的名称。

注意，一般情况下，不建议从模块或包内导入 `*`， 因为，这项操作经常让代码变得难以理解。不过，为了在交互式编译器中少打几个字，这么用也没问题。

模块名后使用 `as` 时，直接把 `as` 后的名称与导入模块绑定。

```python
import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

与 `import fibo` 一样，这种方式也可以有效地导入模块，唯一的区别是，导入的名称是 `fib`。

[`from`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#from) 中也可以使用这种方式，效果类似：

```python
from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

>  备注：为了保证运行效率，每次解释器会话只导入一次模块。如果更改了模块内容，必须重启解释器；仅交互测试一个模块时，也可以使用 [`importlib.reload()`](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.reload)，例如 `import importlib; importlib.reload(modulename)`。

####  以脚本方式执行模块

可以用以下方式运行 Python 模块：

```python
python fibo.py <arguments>
```

这项操作将执行模块里的代码，和导入模块一样，但会把 `__name__` 赋值为 `"__main__"`。 也就是把下列代码添加到模块末尾：

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

既可以把这个文件当脚本使用，也可以用作导入的模块， 因为，解析命令行的代码只有在模块以 “main” 文件执行时才会运行：

```
python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

导入模块时，不运行这些代码：

```python
import fibo
```

这种操作常用于为模块提供便捷用户接口，或用于测试（把模块当作执行测试套件的脚本运行）。

#### 模块搜索路径

当一个名为 `spam` 的模块被导入时，解释器首先搜索具有该名称的内置模块。这些模块的名字被列在 [`sys.builtin_module_names`](https://docs.python.org/zh-cn/3/library/sys.html#sys.builtin_module_names) 中。如果没有找到，它就在变量 [`sys.path`](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 给出的目录列表中搜索一个名为 `spam.py` 的文件， [`sys.path`](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 从这些位置初始化:

- 输入脚本的目录（或未指定文件时的当前目录）。
- [`PYTHONPATH`](https://docs.python.org/zh-cn/3/using/cmdline.html#envvar-PYTHONPATH) （目录列表，与 shell 变量 `PATH` 的语法一样）。
- 依赖于安装的默认值（按照惯例包括一个 `site-packages` 目录，由 [`site`](https://docs.python.org/zh-cn/3/library/site.html#module-site) 模块处理）。

More details are at [The initialization of the sys.path module search path](https://docs.python.org/zh-cn/3/library/sys_path_init.html#sys-path-init).

> 备注
>
> 在支持 symlink 的文件系统中，输入脚本目录是在追加 symlink 后计算出来的。换句话说，包含 symlink 的目录并 **没有** 添加至模块搜索路径。

初始化后，Python 程序可以更改 [`sys.path`](https://docs.python.org/zh-cn/3/library/sys.html#sys.path)。运行脚本的目录在标准库路径之前，置于搜索路径的开头。即，加载的是该目录里的脚本，而不是标准库的同名模块。 除非刻意替换，否则会报错。详见 [标准模块](https://docs.python.org/zh-cn/3/tutorial/modules.html#tut-standardmodules)。



#### “已编译的” Python 文件

为了快速加载模块，Python 把模块的编译版缓存在 `__pycache__` 目录中，文件名为 `module.*version*.pyc`，version 对编译文件格式进行编码，一般是 Python 的版本号。例如，CPython 的 3.3 发行版中，spam.py 的编译版本缓存为 `__pycache__/spam.cpython-33.pyc`。使用这种命名惯例，可以让不同 Python 发行版及不同版本的已编译模块共存。

Python 对比编译版本与源码的修改日期，查看它是否已过期，是否要重新编译，此过程完全自动化。此外，编译模块与平台无关，因此，可在不同架构系统之间共享相同的支持库。

Python 在两种情况下不检查缓存。其一，从命令行直接载入模块，只重新编译，不存储编译结果；其二，没有源模块，就不会检查缓存。为了支持无源文件（仅编译）发行版本， 编译模块必须在源目录下，并且绝不能有源模块。

专业人士的一些小建议：

- 在 Python 命令中使用 [`-O`](https://docs.python.org/zh-cn/3/using/cmdline.html#cmdoption-O) 或 [`-OO`](https://docs.python.org/zh-cn/3/using/cmdline.html#cmdoption-OO) 开关，可以减小编译模块的大小。`-O` 去除断言语句，`-OO` 去除断言语句和 __doc__ 字符串。有些程序可能依赖于这些内容，因此，没有十足的把握，不要使用这两个选项。“优化过的”模块带有 `opt-` 标签，并且文件通常会一小些。将来的发行版或许会改进优化的效果。
- 从 `.pyc` 文件读取的程序不比从 `.py` 读取的执行速度快，`.pyc` 文件只是加载速度更快。
- [`compileall`](https://docs.python.org/zh-cn/3/library/compileall.html#module-compileall) 模块可以为一个目录下的所有模块创建 .pyc 文件。
- 本过程的细节及决策流程图，详见 [**PEP 3147**](https://peps.python.org/pep-3147/)。

### 标准模块

Python 自带一个标准模块的库，它在 Python 库参考（此处以下称为"库参考" ）里另外描述。 一些模块是内嵌到编译器里面的， 它们给一些虽并非语言核心但却内嵌的操作提供接口，要么是为了效率，要么是给操作系统基础操作例如系统调入提供接口。 这些模块集是一个配置选项， 并且还依赖于底层的操作系统。 例如，[`winreg`](https://docs.python.org/zh-cn/3/library/winreg.html#module-winreg) 模块只在 Windows 系统上提供。一个特别值得注意的模块 [`sys`](https://docs.python.org/zh-cn/3/library/sys.html#module-sys)，它被内嵌到每一个 Python 编译器中。`sys.ps1` 和 `sys.ps2` 变量定义了一些字符，它们可以用作主提示符和辅助提示符:

```python
import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

只有解释器用于交互模式时，才定义这两个变量。

变量 `sys.path` 是字符串列表，用于确定解释器的模块搜索路径。该变量以环境变量 [`PYTHONPATH`](https://docs.python.org/zh-cn/3/using/cmdline.html#envvar-PYTHONPATH) 提取的默认路径进行初始化，如未设置 [`PYTHONPATH`](https://docs.python.org/zh-cn/3/using/cmdline.html#envvar-PYTHONPATH)，则使用内置的默认路径。可以用标准列表操作修改该变量：

```python
import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

####  dir() 函数

内置函数 [`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir) 用于查找模块定义的名称。返回结果是经过排序的字符串列表：

```python
import fibo, sys
dir(fibo)
['__name__', 'fib', 'fib2']
dir(sys)  
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
```

没有参数时，[`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir) 列出当前定义的名称：

```python
a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

注意，该函数列出所有类型的名称：变量、模块、函数等。

[`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir) 不会列出内置函数和变量的名称。这些内容的定义在标准模块 [`builtins`](https://docs.python.org/zh-cn/3/library/builtins.html#module-builtins) 里：

```python
import builtins
dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```

### 包

包是一种用“点式模块名”构造 Python 模块命名空间的方法。例如，模块名 `A.B` 表示包 `A` 中名为 `B` 的子模块。正如模块可以区分不同模块之间的全局变量名称一样，点式模块名可以区分 NumPy 或 Pillow 等不同多模块包之间的模块名称。

假设要为统一处理声音文件与声音数据设计一个模块集（“包”）。声音文件的格式很多（通常以扩展名来识别，例如：`.wav`， `.aiff`， `.au`），因此，为了不同文件格式之间的转换，需要创建和维护一个不断增长的模块集合。为了实现对声音数据的不同处理（例如，混声、添加回声、均衡器功能、创造人工立体声效果），还要编写无穷无尽的模块流。下面这个分级文件树展示了这个包的架构：

```python
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

导入包时，Python 搜索 `sys.path` 里的目录，查找包的子目录。

The `__init__.py` files are required to make Python treat directories containing the file as packages. This prevents directories with a common name, such as `string`, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, `__init__.py` can just be an empty file, but it can also execute initialization code for the package or set the `__all__` variable, described later.

还可以从包中导入单个模块，例如：

```python
import sound.effects.echo
```

这段代码加载子模块 `sound.effects.echo` ，但引用时必须使用子模块的全名：

```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

另一种导入子模块的方法是 ：

```python
from sound.effects import echo
```

Import 语句的另一种变体是直接导入所需的函数或变量：

```python
from sound.effects.echo import echofilter
```

同样，这样也会加载子模块 `echo`，但可以直接使用函数 `echofilter()`：

```python
echofilter(input, output, delay=0.7, atten=4)
```

注意，使用 `from package import item` 时，item 可以是包的子模块（或子包），也可以是包中定义的函数、类或变量等其他名称。`import` 语句首先测试包中是否定义了 item；如果未在包中定义，则假定 item 是模块，并尝试加载。如果找不到 item，则触发 [`ImportError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ImportError) 异常。

相反，使用 `import item.subitem.subsubitem` 句法时，除最后一项外，每个 item 都必须是包；最后一项可以是模块或包，但不能是上一项中定义的类、函数或变量。

####  从包中导入 *

使用 `from sound.effects import *` 时会发生什么？理想情况下，该语句在文件系统查找并导入包的所有子模块。这项操作花费的时间较长，并且导入子模块可能会产生不必要的副作用，这种副作用只有在显式导入子模块时才会发生。

唯一的解决方案是提供包的显式索引。[`import`](https://docs.python.org/zh-cn/3.11/reference/simple_stmts.html#import) 语句使用如下惯例：如果包的 `__init__.py` 代码定义了列表 `__all__`，运行 `from package import *` 时，它就是用于导入的模块名列表。发布包的新版本时，包的作者应更新此列表。如果包的作者认为没有必要在包中执行导入 * 操作，也可以不提供此列表。例如，`sound/effects/__init__.py` 文件包含以下代码：

```python
__all__ = ["echo", "surround", "reverse"]
```

这将意味着将 `from sound.effects import *` 导入 `sound.effects` 包的三个命名的子模块。

如果没有定义 `__all__`，`from sound.effects import *` 语句 *不会* 把包 `sound.effects` 中所有子模块都导入到当前命名空间；该语句只确保导入包 `sound.effects` （可能还会运行 `__init__.py` 中的初始化代码），然后，再导入包中定义的名称。这些名称包括 `__init__.py` 中定义的任何名称（以及显式加载的子模块），还包括之前 [`import`](https://docs.python.org/zh-cn/3.11/reference/simple_stmts.html#import) 语句显式加载的包里的子模块。请看以下代码：

```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

#### 子包参考

包中含有多个子包时（与示例中的 `sound` 包一样），可以使用绝对导入引用兄弟包中的子模块。例如，要在模块 `sound.filters.vocoder` 中使用 `sound.effects` 包的 `echo` 模块时，可以用 `from sound.effects import echo` 导入。

还可以用 import 语句的 `from module import name` 形式执行相对导入。这些导入语句使用前导句点表示相对导入中的当前包和父包。例如，相对于 `surround` 模块，可以使用：

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

注意，相对导入基于当前模块名。因为主模块名是 `"__main__"` ，所以 Python 程序的主模块必须始终使用绝对导入。

#### 多目录中的包

包支持一个更特殊的属性 [`__path__`](https://docs.python.org/zh-cn/3.11/reference/import.html#path__) 。在包的 :[file:__init__.py](file://__init__.py/) 文件中的代码被执行前，该属性被初始化为包含 :[file:__init__.py](file://__init__.py/) 文件所在的目录名在内的列表。可以修改此变量；但这样做会影响在此包中搜索子模块和子包。

这个功能虽然不常用，但可用于扩展包中的模块集。

#### 导入自定义包

[python导入自定义包 - 铭烟 - 博客园 (cnblogs.com)](https://www.cnblogs.com/ydbk/p/14960666.html)

通过`sys`模块导入自定义模块的path（处于包中的模块导入不在包中的模块也可以采用这种方法）

1. 先导入`sys`模块

2. 然后通过`sys.path.append(path)` 函数来导入自定义模块所在的目录

3. 导入自定义模块。

   ```python
   
   import requests
   import sys
   
   utils_path = r"/app/code/project-workshop/code-prac/Spider/spider_utils"
   sys.path.append(utils_path)
   
   from proxy import get_proxies
   
   if __name__ == '__main__':
       get_proxies()
   ```

   

## 输入与输出

程序输出有几种显示方式；数据既可以输出供人阅读的形式，也可以写入文件备用。本章探讨一些可用的方式。

我们已学习了两种写入值的方法：*表达式语句* 和 [`print()`](https://docs.python.org/zh-cn/3/library/functions.html#print) 函数。第三种方法是使用文件对象的 `write()` 方法；标准输出文件称为 `sys.stdout`。详见标准库参考。

对输出格式的控制不只是打印空格分隔的值，还需要更多方式。格式化输出包括以下几种方法。

- 使用 [格式化字符串字面值](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html#tut-f-strings) ，要在字符串开头的引号/三引号前添加 `f` 或 `F` 。在这种字符串中，可以在 `{` 和 `}` 字符之间输入引用的变量，或字面值的 Python 表达式。

  ```python
  year = 2016
  event = 'Referendum'
  f'Results of the {year} {event}'
  'Results of the 2016 Referendum'
  ```

- 字符串的 [`str.format()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format) 方法需要更多手动操作。该方法也用 `{` 和 `}` 标记替换变量的位置，虽然这种方法支持详细的格式化指令，但需要提供格式化信息。

  ```python
  yes_votes = 42_572_654
  no_votes = 43_132_495
  percentage = yes_votes / (yes_votes + no_votes)
  '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
  ' 42572654 YES votes  49.67%'
  ```

- 最后，还可以用字符串切片和合并操作完成字符串处理操作，创建任何排版布局。字符串类型还支持将字符串按给定列宽进行填充，这些方法也很有用。

如果不需要花哨的输出，只想快速显示变量进行调试，可以用 [`repr()`](https://docs.python.org/zh-cn/3/library/functions.html#repr) 或 [`str()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 函数把值转化为字符串。

[`str()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 函数返回供人阅读的值，[`repr()`](https://docs.python.org/zh-cn/3/library/functions.html#repr) 则生成适于解释器读取的值（如果没有等效的语法，则强制执行 [`SyntaxError`](https://docs.python.org/zh-cn/3/library/exceptions.html#SyntaxError)）。对于没有支持供人阅读展示结果的对象， [`str()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 返回与 [`repr()`](https://docs.python.org/zh-cn/3/library/functions.html#repr) 相同的值。一般情况下，数字、列表或字典等结构的值，使用这两个函数输出的表现形式是一样的。字符串有两种不同的表现形式。

示例如下：

```python
s = 'Hello, world.'
str(s)
'Hello, world.'
repr(s)
"'Hello, world.'"
str(1/7)
'0.14285714285714285'
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
The value of x is 32.5, and y is 40000...
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
'hello, world\n'
# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

[`string`](https://docs.python.org/zh-cn/3/library/string.html#module-string) 模块包含 [`Template`](https://docs.python.org/zh-cn/3/library/string.html#string.Template) 类，提供了将值替换为字符串的另一种方法。该类使用 `$x` 占位符，并用字典的值进行替换，但对格式控制的支持比较有限。

### 格式化字符串字面值

[格式化字符串字面值](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#f-strings) （简称为 f-字符串）在字符串前加前缀 `f` 或 `F`，通过 `{expression}` 表达式，把 Python 表达式的值添加到字符串内。

格式说明符是可选的，写在表达式后面，可以更好地控制格式化值的方式。下例将 pi 舍入到小数点后三位：

```python
import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```

在 `':'` 后传递整数，为该字段设置最小字符宽度，常用于列对齐：

```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

还有一些修饰符可以在格式化前转换值。 `'!a'` 应用 [`ascii()`](https://docs.python.org/zh-cn/3/library/functions.html#ascii) ，`'!s'` 应用 [`str()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str)，`'!r'` 应用 [`repr()`](https://docs.python.org/zh-cn/3/library/functions.html#repr)：

```python
animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

The `=` specifier can be used to expand an expression to the text of the expression, an equal sign, then the representation of the evaluated expression:

See [self-documenting expressions](https://docs.python.org/zh-cn/3/whatsnew/3.8.html#bpo-36817-whatsnew) for more infor

```python
bugs = 'roaches'
>>> count = 13
>>> area = 'living room'
>>> print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'
```

mation on the `=` specifier. For a reference on these format specifications, see the reference guide for the [格式规格迷你语言](https://docs.python.org/zh-cn/3/library/string.html#formatspec).

### 字符串 format() 方法

[`str.format()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format) 方法的基本用法如下所示：

```python
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

花括号及之内的字符（称为格式字段）被替换为传递给 [`str.format()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format) 方法的对象。花括号中的数字表示传递给 [`str.format()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format) 方法的对象所在的位置。

```python
print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

[`str.format()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format) 方法中使用关键字参数名引用值

```python
print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

位置参数和关键字参数可以任意组合：

```python
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
...                                                    other='Georg'))
The story of Bill, Manfred, and Georg.
```

如果不想分拆较长的格式字符串，最好按名称引用变量进行格式化，不要按位置。这项操作可以通过传递字典，并用方括号 `'[]'` 访问键来完成。

```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

This could also be done by passing the `table` dictionary as keyword arguments with the `**` notation.

```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

As an example, the following lines produce a tidily aligned set of columns giving integers and their squares and cubes:

```python
for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

[`str.format()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format) 进行字符串格式化的完整概述详见 [格式字符串语法](https://docs.python.org/zh-cn/3/library/string.html#formatstrings) 。

### 手动格式化字符串

下面是使用手动格式化方式实现的同一个平方和立方的表：

```python
for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

（注意，每列之间的空格是通过使用 [`print()`](https://docs.python.org/zh-cn/3/library/functions.html#print) 添加的：它总在其参数间添加空格。）

字符串对象的 [`str.rjust()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.rjust) 方法通过在左侧填充空格，对给定宽度字段中的字符串进行右对齐。同类方法还有 [`str.ljust()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.ljust) 和 [`str.center()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.center) 。这些方法不写入任何内容，只返回一个新字符串，如果输入的字符串太长，它们不会截断字符串，而是原样返回；虽然这种方式会弄乱列布局，但也比另一种方法好，后者在显示值时可能不准确（如果真的想截断字符串，可以使用 `x.ljust(n)[:n]` 这样的切片操作 。）

另一种方法是 [`str.zfill()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.zfill) ，该方法在数字字符串左边填充零，且能识别正负号：

```python
'12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

### 旧式字符串格式化方法

% 运算符（求余符）也可用于字符串格式化。给定 `'string' % values`，则 `string` 中的 `%` 实例会以零个或多个 `values` 元素替换。此操作被称为字符串插值。例如：

```python
import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

### 读写文件

[`open()`](https://docs.python.org/zh-cn/3/library/functions.html#open) 返回一个 [file object](https://docs.python.org/zh-cn/3/glossary.html#term-file-object) ，最常使用的是两个位置参数和一个关键字参数：`open(filename, mode, encoding=None)`

```python
f = open('workfile', 'w', encoding="utf-8")
```

第一个实参是文件名字符串。第二个实参是包含描述文件使用方式字符的字符串。*mode* 的值包括 `'r'` ，表示文件只能读取；`'w'` 表示只能写入（现有同名文件会被覆盖）；`'a'` 表示打开文件并追加内容，任何写入的数据会自动添加到文件末尾。`'r+'` 表示打开文件进行读写。*mode* 实参是可选的，省略时的默认值为 `'r'`。

通常情况下，文件是以 *text mode* 打开的，也就是说，你从文件中读写字符串，这些字符串是以特定的 *encoding* 编码的。如果没有指定 *encoding* ，默认的是与平台有关的（见 [`open()`](https://docs.python.org/zh-cn/3/library/functions.html#open) ）。因为 UTF-8 是现代事实上的标准，除非你知道你需要使用一个不同的编码，否则建议使用 `encoding="utf-8"` 。在模式后面加上一个 `'b'` ，可以用 *binary mode* 打开文件。二进制模式的数据是以 [`bytes`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes) 对象的形式读写的。在二进制模式下打开文件时，你不能指定 *encoding* 。

在文本模式下读取文件时，默认把平台特定的行结束符（Unix 上为 `\n`, Windows 上为 `\r\n`）转换为 `\n`。在文本模式下写入数据时，默认把 `\n` 转换回平台特定结束符。这种操作方式在后台修改文件数据对文本文件来说没有问题，但会破坏 `JPEG` 或 `EXE` 等二进制文件中的数据。注意，在读写此类文件时，一定要使用二进制模式。

在处理文件对象时，最好使用 [`with`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#with) 关键字。优点是，子句体结束后，文件会正确关闭，即便触发异常也可以。而且，使用 `with` 相比等效的 [`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try)-[`finally`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#finally) 代码块要简短得多：

```python
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
f.closed
```

如果没有使用 [`with`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#with) 关键字，则应调用 `f.close()` 关闭文件，即可释放文件占用的系统资源。

> 警告
>
> 调用 `f.write()` 时，未使用 `with` 关键字，或未调用 `f.close()`，即使程序正常退出，也**可能** 导致 `f.write()` 的参数没有完全写入磁盘。

通过 [`with`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#with) 语句，或调用 `f.close()` 关闭文件对象后，再次使用该文件对象将会失败。

```python
f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

### 文件对象的方法

#### read()

本节下文中的例子假定已创建 `f` 文件对象。

`f.read(size)` 可用于读取文件内容，它会读取一些数据，并返回字符串（文本模式），或字节串对象（在二进制模式下）。 *size* 是可选的数值参数。省略 *size* 或 *size* 为负数时，读取并返回整个文件的内容；文件大小是内存的两倍时，会出现问题。*size* 取其他值时，读取并返回最多 *size* 个字符（文本模式）或 *size* 个字节（二进制模式）。如已到达文件末尾，`f.read()` 返回空字符串（`''`）。

```python
f.read()
'This is the entire file.\n'
>>> f.read()
''
```

#### readline()

`f.readline()` 从文件中读取单行数据；字符串末尾保留换行符（`\n`），只有在文件不以换行符结尾时，文件的最后一行才会省略换行符。这种方式让返回值清晰明确；只要 `f.readline()` 返回空字符串，就表示已经到达了文件末尾，空行使用 `'\n'` 表示，该字符串只包含一个换行符。

```python
f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```

从文件中读取多行时，可以用循环遍历整个文件对象。这种操作能高效利用内存，快速，且代码简单：

```python
for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```

如需以列表形式读取文件中的所有行，可以用 `list(f)` 或 `f.readlines()`。

#### write()

```python
f.write('This is a test\n')
15
```

写入其他类型的对象前，要先把它们转化为字符串（文本模式）或字节对象（二进制模式）：

```python
value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```

`f.tell()` 返回整数，给出文件对象在文件中的当前位置，表示为二进制模式下时从文件开始的字节数，以及文本模式下的意义不明的数字。

`f.seek(offset, whence)` 可以改变文件对象的位置。通过向参考点添加 *offset* 计算位置；参考点由 *whence* 参数指定。 *whence* 值为 0 时，表示从文件开头计算，1 表示使用当前文件位置，2 表示使用文件末尾作为参考点。省略 *whence* 时，其默认值为 0，即使用文件开头作为参考点。

```python
f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```

在文本文件（模式字符串未使用 `b` 时打开的文件）中，只允许相对于文件开头搜索（使用 `seek(0, 2)` 搜索到文件末尾是个例外），唯一有效的 *offset* 值是能从 `f.tell()` 中返回的，或 0。其他 *offset* 值都会产生未定义的行为。

文件对象还支持 `isatty()` 和 `truncate()` 等方法，但不常用；文件对象的完整指南详见库参考。



### 使用 json 保存结构化数据

从文件写入或读取字符串很简单，数字则稍显麻烦，因为 `read()` 方法只返回字符串，这些字符串必须传递给 [`int()`](https://docs.python.org/zh-cn/3/library/functions.html#int) 这样的函数，接受 `'123'` 这样的字符串，并返回数字值 123。保存嵌套列表、字典等复杂数据类型时，手动解析和序列化的操作非常复杂。

Rather than having users constantly writing and debugging code to save complicated data types to files, Python allows you to use the popular data interchange format called [JSON (JavaScript Object Notation)](https://json.org/). The standard module called [`json`](https://docs.python.org/zh-cn/3/library/json.html#module-json) can take Python data hierarchies, and convert them to string representations; this process is called *serializing*. Reconstructing the data from the string representation is called *deserializing*. Between serializing and deserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.

只需一行简单的代码即可查看某个对象的 JSON 字符串表现形式：

```python
import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```

[`dumps()`](https://docs.python.org/zh-cn/3/library/json.html#json.dumps) 函数还有一个变体， [`dump()`](https://docs.python.org/zh-cn/3/library/json.html#json.dump) ，它只将对象序列化为 [text file](https://docs.python.org/zh-cn/3/glossary.html#term-text-file) 。因此，如果 `f` 是 [text file](https://docs.python.org/zh-cn/3/glossary.html#term-text-file) 对象，可以这样做：

```python
json.dump(x, f)
```

要再次解码对象，如果 `f` 是已打开、供读取的 [binary file](https://docs.python.org/zh-cn/3/glossary.html#term-binary-file) 或 [text file](https://docs.python.org/zh-cn/3/glossary.html#term-text-file) 对象：

```python
x = json.load(f)
```

>  JSON文件必须以UTF-8编码。当打开JSON文件作为一个 [text file](https://docs.python.org/zh-cn/3/glossary.html#term-text-file) 用于读写时，使用 `encoding="utf-8"` 。

这种简单的序列化技术可以处理列表和字典，但在 JSON 中序列化任意类的实例，则需要付出额外努力。[`json`](https://docs.python.org/zh-cn/3/library/json.html#module-json) 模块的参考包含对此的解释。

> 参见[`pickle`](https://docs.python.org/zh-cn/3/library/pickle.html#module-pickle) - 封存模块
>
> 与 [JSON](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html#tut-json) 不同，*pickle* 是一种允许对复杂 Python 对象进行序列化的协议。因此，它为 Python 所特有，不能用于与其他语言编写的应用程序通信。默认情况下它也是不安全的：如果解序化的数据是由手段高明的攻击者精心设计的，这种不受信任来源的 pickle 数据可以执行任意代码。



[json模块常用方法](http://c.biancheng.net/python_spider/json.html)

json.load() 与 json.dump() 操作的是文件流对象，实现了 json 文件的读写操作，而 json.loads() 与 json.dumps() 操作的是 Python 对象或者 JOSN 字符串。

![image-20230424144856022](image-20230424144856022.png)

- load()

  - 需要从json文件中读取数据时

- dump()

  - 它可以将 Python 对象（字典、列表等）转换为 json 字符串，并将转换后的数据写入到 json 格式的文件中 ，因此该方法必须操作文件流对象。比如当使用爬虫程序完成数据抓取后，有时需要将数据保存为 json 格式，此时就用到了 json.dump() 方法，语法格式如下：

    ```bash
    json.dump(object,f,inden=0，ensure_ascii=False)
    ```

    参数说明如下：

    - object：Python 数据对象，比如字典，列表等
    - f：文件流对象，即文件句柄。
    - indent：格式化存储数据，使 JSON 字符串更易阅读。
    - ensure_ascii：是否使用 ascii 编码，当数据中出现中文的时候，需要将其设置为 False。

    ```python
    import json
    
    item_list = []
    item = {'website': 'C语言中文网', 'url': "c.biancheng.net"}
    for k,v in item.items():
        item_list.append(v)
    
    with open('info_web.json', 'a') as f:
        json.dump(item_list, f, ensure_ascii=False)
    ```

    

  - 爬取网页数据，需要写到json文件中时

    ```python
    import json
    
    ditc_info={"name" : "c语言中文网","PV" : "50万","UV" : "20万","create_time" : "2010年"}
    with open("web.josn","a") as f:
        json.dump(ditc_info,f,ensure_ascii=False)
    ```

    

## 错误与异常

至此，本教程还未深入介绍错误信息，但如果您输入过本教程前文中的例子，应该已经看到过一些错误信息。目前，（至少）有两种不同错误：*句法错误* 和 *异常*

### 句法错误

句法错误又称解析错误，是学习 Python 时最常见的错误：

```python
while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

解析器会复现出现句法错误的代码行，并用小“箭头”指向行里检测到的第一个错误。错误是由箭头 *上方* 的 token 触发的（至少是在这里检测出的）：本例中，在 [`print()`](https://docs.python.org/zh-cn/3/library/functions.html#print) 函数中检测到错误，因为，在它前面缺少冒号（`':'`） 。错误信息还输出文件名与行号，在使用脚本文件时，就可以知道去哪里查错。

### 异常

即使语句或表达式使用了正确的语法，执行时仍可能触发错误。执行时检测到的错误称为 *异常*，异常不一定导致严重的后果：很快我们就能学会如何处理 Python 的异常。大多数异常不会被程序处理，而是显示下列错误信息：

```python
10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
'2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

错误信息的最后一行说明程序遇到了什么类型的错误。异常有不同的类型，而类型名称会作为错误信息的一部分中打印出来：上述示例中的异常类型依次是：[`ZeroDivisionError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ZeroDivisionError)， [`NameError`](https://docs.python.org/zh-cn/3/library/exceptions.html#NameError) 和 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError)。作为异常类型打印的字符串是发生的内置异常的名称。对于所有内置异常都是如此，但对于用户定义的异常则不一定如此（虽然这种规范很有用）。标准的异常类型是内置的标识符（不是保留关键字）。

此行其余部分根据异常类型，结合出错原因，说明错误细节。

错误信息开头用堆栈回溯形式展示发生异常的语境。一般会列出源代码行的堆栈回溯；但不会显示从标准输入读取的行。

[内置异常](https://docs.python.org/zh-cn/3/library/exceptions.html#bltin-exceptions) 列出了内置异常及其含义。

### 异常的处理

可以编写程序处理选定的异常。下例会要求用户一直输入内容，直到输入有效的整数，但允许用户中断程序（使用 Control-C 或操作系统支持的其他操作）；注意，用户中断程序会触发 [`KeyboardInterrupt`](https://docs.python.org/zh-cn/3/library/exceptions.html#KeyboardInterrupt) 异常。

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

```

[`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 语句的工作原理如下：

- 首先，执行 *try 子句* （[`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 和 [`except`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#except) 关键字之间的（多行）语句）。
- 如果没有触发异常，则跳过 *except 子句*，[`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 语句执行完毕。
- 如果在执行 [`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 子句时发生了异常，则跳过该子句中剩下的部分。 如果异常的类型与 [`except`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#except) 关键字后指定的异常相匹配，则会执行 *except 子句*，然后跳到 try/except 代码块之后继续执行。
- 如果发生的异常与 *except 子句* 中指定的异常不匹配，则它会被传递到外部的 [`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 语句中；如果没有找到处理程序，则它是一个 *未处理异常* 且执行将终止并输出如上所示的消息。

[`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 语句可以有多个 *except 子句* 来为不同的异常指定处理程序。 但最多只有一个处理程序会被执行。 处理程序只处理对应的 *try 子句* 中发生的异常，而不处理同一 `try` 语句内其他处理程序中的异常。 *except 子句* 可以用带圆括号的元组来指定多个异常，例如:

```python
except (RuntimeError, TypeError, NameError):
     pass
```

如果发生的异常与 [`except`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#except) 子句中的类是同一个类或是它的基类时，则该类与该异常相兼容（反之则不成立 --- 列出派生类的 *except 子句* 与基类不兼容）。 例如，下面的代码将依次打印 B, C, D:

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

请注意如果颠倒 *except 子句* 的顺序（把 `except B` 放在最前），则会输出 B, B, B --- 即触发了第一个匹配的 *except 子句*。

When an exception occurs, it may have associated values, also known as the exception's *arguments*. The presence and types of the arguments depend on the exception type.

The *except clause* may specify a variable after the exception name. The variable is bound to the exception instance which typically has an `args` attribute that stores the arguments. For convenience, builtin exception types define `__str__()` to print all the arguments without explicitly accessing `.args`.

```python
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst)) # <class 'Exception'>
    print(inst.args) # ('spam', 'eggs')
    print(inst) # ('spam', 'eggs') 
    #__str__ allows args to be printed directly,
    # but may be overridden in exception subclasses

    x, y = inst.args
    print('x =', x) # x = spam
    print('y =', y) # y = eggs

```

The exception's `__str__()` output is printed as the last part ('detail') of the message for unhandled exceptions.

[`BaseException`](https://docs.python.org/zh-cn/3/library/exceptions.html#BaseException) is the common base class of all exceptions. One of its subclasses, [`Exception`](https://docs.python.org/zh-cn/3/library/exceptions.html#Exception), is the base class of all the non-fatal exceptions. Exceptions which are not subclasses of [`Exception`](https://docs.python.org/zh-cn/3/library/exceptions.html#Exception) are not typically handled, because they are used to indicate that the program should terminate. They include [`SystemExit`](https://docs.python.org/zh-cn/3/library/exceptions.html#SystemExit) which is raised by [`sys.exit()`](https://docs.python.org/zh-cn/3/library/sys.html#sys.exit) and [`KeyboardInterrupt`](https://docs.python.org/zh-cn/3/library/exceptions.html#KeyboardInterrupt) which is raised when a user wishes to interrupt the program.

[`Exception`](https://docs.python.org/zh-cn/3/library/exceptions.html#Exception) can be used as a wildcard that catches (almost) everything. However, it is good practice to be as specific as possible with the types of exceptions that we intend to handle, and to allow any unexpected exceptions to propagate on.

The most common pattern for handling [`Exception`](https://docs.python.org/zh-cn/3/library/exceptions.html#Exception) is to print or log the exception and then re-raise it (allowing a caller to handle the exception as well):

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

[`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) ... [`except`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#except) 语句具有可选的 *else 子句*，该子句如果存在，它必须放在所有 *except 子句* 之后。 它适用于 *try 子句* 没有引发异常但又必须要执行的代码。 例如:

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

使用 `else` 子句比向 [`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 子句添加额外的代码要好，可以避免意外捕获非 `try` ... `except` 语句保护的代码触发的异常。



Exception handlers do not handle only exceptions that occur immediately in the *try clause*, but also those that occur inside functions that are called (even indirectly) in the *try clause*. For example:

```bash
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

Handling run-time error: division by zero
```

### 触发异常

[`raise`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#raise) 语句支持强制触发指定的异常。例如：

```bash
raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

The sole argument to [`raise`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#raise) indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from [`BaseException`](https://docs.python.org/zh-cn/3/library/exceptions.html#BaseException), such as [`Exception`](https://docs.python.org/zh-cn/3/library/exceptions.html#Exception) or one of its subclasses). If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments:

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

如果只想判断是否触发了异常，但并不打算处理该异常，则可以使用更简单的 [`raise`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#raise) 语句重新触发异常：

```python
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

### 异常链

If an unhandled exception occurs inside an [`except`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#except) section, it will have the exception being handled attached to it and included in the error message:

```python
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")

# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
# RuntimeError: unable to handle error

```

To indicate that an exception is a direct consequence of another, the [`raise`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#raise) statement allows an optional [`from`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#raise) clause:

```python
# exc must be exception instance or None.
raise RuntimeError from exc
```

转换异常时，这种方式很有用。例如：

```python
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc

# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#   File "<stdin>", line 2, in func
# ConnectionError

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
# RuntimeError: Failed to open database
```

It also allows disabling automatic exception chaining using the `from None` idiom:

```python
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

异常链机制详见 [内置异常](https://docs.python.org/zh-cn/3/library/exceptions.html#bltin-exceptions)。

### 用户自定义异常

程序可以通过创建新的异常类命名自己的异常（Python 类的内容详见 [类](https://docs.python.org/zh-cn/3/tutorial/classes.html#tut-classes)）。不论是以直接还是间接的方式，异常都应从 [`Exception`](https://docs.python.org/zh-cn/3/library/exceptions.html#Exception) 类派生。

异常类可以被定义成能做其他类所能做的任何事，但通常应当保持简单，它往往只提供一些属性，允许相应的异常处理程序提取有关错误的信息。

大多数异常命名都以 “Error” 结尾，类似标准异常的命名。

Many standard modules define their own exceptions to report errors that may occur in functions they define.

### 定义清理操作

[`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 语句还有一个可选子句，用于定义在所有情况下都必须要执行的清理操作。例如：

```python
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```

如果存在 [`finally`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#finally) 子句，则 `finally` 子句是 [`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 语句结束前执行的最后一项任务。不论 `try` 语句是否触发异常，都会执行 `finally` 子句。以下内容介绍了几种比较复杂的触发异常情景：

- 如果执行 `try` 子句期间触发了某个异常，则某个 [`except`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#except) 子句应处理该异常。如果该异常没有 `except` 子句处理，在 `finally` 子句执行后会被重新触发。

- `except` 或 `else` 子句执行期间也会触发异常。 同样，该异常会在 `finally` 子句执行之后被重新触发。

- 如果 `finally` 子句中包含 [`break`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#break)、[`continue`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#continue) 或 [`return`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#return) 等语句，异常将不会被重新引发。

- 如果执行 `try` 语句时遇到 [`break`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#break),、[`continue`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#continue) 或 [`return`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#return) 语句，则 `finally` 子句在执行 `break`、`continue` 或 `return` 语句之前执行。

- 如果 `finally` 子句中包含 `return` 语句，则返回值来自 `finally` 子句的某个 `return` 语句的返回值，而不是来自 `try` 子句的 `return` 语句的返回值。

  ```python
  def bool_return():
      try:
          return True
      finally:
          return False
      
  
  res = bool_return()
  print(res) # Flase
  ```

这是一个比较复杂的例子:

```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError: # try有异常，需要执行的语句
        print("division by zero!")
    else: # try没有异常，需要执行的语句
        print("result is", result)
    finally: # 不管try有没有异常，都需要执行的语句
        print("executing finally clause")

# try中的语句正常执行
divide(2, 1)
# result is 2.0
# executing finally clause

# try中的语句抛出可以捕获的异常
divide(2, 0)
# division by zero!
# executing finally clause

# try中的语句抛出不可捕获的异常
divide("2", "1")
# executing finally clause
# Traceback (most recent call last):
#   File "test.py", line 21, in <module>
#     divide("2", "1")
#   File "test.py", line 3, in divide
#     result = x / y
# TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

如上所示，任何情况下都会执行 [`finally`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#finally) 子句。[`except`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#except) 子句不处理两个字符串相除触发的 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError)，因此会在 `finally` 子句执行后被重新触发。

在实际应用程序中，[`finally`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#finally) 子句对于释放外部资源（例如文件或者网络连接）非常有用，无论是否成功使用资源。

### 预定义的清理操作

某些对象定义了不需要该对象时要执行的标准清理操作。无论使用该对象的操作是否成功，都会执行清理操作。比如，下例要打开一个文件，并输出文件内容：

```python
for line in open("myfile.txt"):
    print(line, end="")
```

这个代码的问题在于，执行完代码后，文件在一段不确定的时间内处于打开状态。在简单脚本中这没有问题，但对于较大的应用程序来说可能会出问题。[`with`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#with) 语句支持以及时、正确的清理的方式使用文件对象：

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

语句执行完毕后，即使在处理行时遇到问题，都会关闭文件 *f*。和文件一样，支持预定义清理操作的对象会在文档中指出这一点。

### Raising and Handling Multiple Unrelated Exceptions

There are situations where it is necessary to report several exceptions that have occurred. This is often the case in concurrency frameworks, when several tasks may have failed in parallel, but there are also other use cases where it is desirable to continue execution and collect multiple errors rather than raise the first exception.

The builtin [`ExceptionGroup`](https://docs.python.org/zh-cn/3/library/exceptions.html#ExceptionGroup) wraps a list of exception instances so that they can be raised together. It is an exception itself, so it can be caught like any other exception.

```python
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

f()
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |   File "<stdin>", line 3, in f
  | ExceptionGroup: there were problems
  +-+---------------- 1 ----------------
    | OSError: error 1
    +---------------- 2 ----------------
    | SystemError: error 2
    +------------------------------------
try:
    f()
except Exception as e:
    print(f'caught {type(e)}: e')

caught <class 'ExceptionGroup'>: e
>>>
```

By using `except*` instead of `except`, we can selectively handle only the exceptions in the group that match a certain type. In the following example, which shows a nested exception group, each `except*` clause extracts from the group exceptions of a certain type while letting all other exceptions propagate to other clauses and eventually to be reraised.

```python
def f():
    raise ExceptionGroup("group1",
                         [OSError(1),
                          SystemError(2),
                          ExceptionGroup("group2",
                                         [OSError(3), RecursionError(4)])])

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")

There were OSErrors
There were SystemErrors
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 2, in <module>
  |   File "<stdin>", line 2, in f
  | ExceptionGroup: group1
  +-+---------------- 1 ----------------
    | ExceptionGroup: group2
    +-+---------------- 1 ----------------
      | RecursionError: 4
      +------------------------------------
>>>
```

Note that the exceptions nested in an exception group must be instances, not types. This is because in practice the exceptions would typically be ones that have already been raised and caught by the program, along the following pattern:

```python
excs = []
... for test in tests:
...     try:
...         test.run()
...     except Exception as e:
...         excs.append(e)
...
>>> if excs:
...    raise ExceptionGroup("Test Failures", excs)
...
```

### Enriching Exceptions with Notes

When an exception is created in order to be raised, it is usually initialized with information that describes the error that has occurred. There are cases where it is useful to add information after the exception was caught. For this purpose, exceptions have a method `add_note(note)` that accepts a string and adds it to the exception's notes list. The standard traceback rendering includes all notes, in the order they were added, after the exception.

```python
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise

# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# TypeError: bad type
# Add some information
# Add some more information
```

For example, when collecting exceptions into an exception group, we may want to add context information for the individual errors. In the following each exception in the group has a note indicating when this error has occurred.

```python
def f():
    raise OSError('operation failed')

excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Happened in Iteration {i+1}')
        excs.append(e)

raise ExceptionGroup('We have some problems', excs)
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  | ExceptionGroup: We have some problems (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |   File "<stdin>", line 2, in f
    | OSError: operation failed
    | Happened in Iteration 1
    +---------------- 2 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |   File "<stdin>", line 2, in f
    | OSError: operation failed
    | Happened in Iteration 2
    +---------------- 3 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |   File "<stdin>", line 2, in f
    | OSError: operation failed
    | Happened in Iteration 3
    +------------------------------------
```

## 类

类把数据与功能绑定在一起。创建新类就是创建新的对象 **类型**，从而创建该类型的新 **实例** 。类实例支持维持自身状态的属性，还支持（由类定义的）修改自身状态的方法。

和其他编程语言相比，Python 的类只使用了很少的新语法和语义。Python 的类有点类似于 C++ 和 Modula-3 中类的结合体，而且支持面向对象编程（OOP）的所有标准特性：类的继承机制支持多个基类、派生的类能覆盖基类的方法、类的方法能调用基类中的同名方法。对象可包含任意数量和类型的数据。和模块一样，类也支持 Python 动态特性：在运行时创建，创建后还可以修改。

如果用 C++ 术语来描述的话，类成员（包括数据成员）通常为 *public* （例外的情况见下文 [私有变量](https://docs.python.org/zh-cn/3/tutorial/classes.html#tut-private)），所有成员函数都是 *virtual*。与在 Modula-3 中一样，没有用于从对象的方法中引用对象成员的简写形式：方法函数在声明时，有一个显式的参数代表本对象，该参数由调用隐式提供。 与在 Smalltalk 中一样，Python 的类也是对象，这为导入和重命名提供了语义支持。与 C++ 和 Modula-3 不同，Python 的内置类型可以用作基类，供用户扩展。 此外，与 C++ 一样，算术运算符、下标等具有特殊语法的内置运算符都可以为类实例而重新定义。

由于缺乏关于类的公认术语，本章中偶尔会使用 Smalltalk 和 C++ 的术语。本章还会使用 Modula-3 的术语，Modula-3 的面向对象语义比 C++ 更接近 Python，但估计听说过这门语言的读者很少。

### 名称和对象

对象之间相互独立，多个名称（在多个作用域内）可以绑定到同一个对象。 其他语言称之为别名。Python 初学者通常不容易理解这个概念，处理数字、字符串、元组等不可变基本类型时，可以不必理会。 但是，对涉及可变对象，如列表、字典等大多数其他类型的 Python 代码的语义，别名可能会产生意料之外的效果。这样做，通常是为了让程序受益，因为别名在某些方面就像指针。例如，传递对象的代价很小，因为实现只传递一个指针；如果函数修改了作为参数传递的对象，调用者就可以看到更改 --- 无需 Pascal 用两个不同参数的传递机制。

### 作用域和命名空间

在介绍类前，首先要介绍 Python 的作用域规则。类定义对命名空间有一些巧妙的技巧，了解作用域和命名空间的工作机制有利于加强对类的理解。并且，即便对于高级 Python 程序员，这方面的知识也很有用。

接下来，我们先了解一些定义。

*namespace* （命名空间）是映射到对象的名称。现在，大多数命名空间都使用 Python 字典实现，但除非涉及到优化性能，我们一般不会关注这方面的事情，而且将来也可能会改变这种方式。命名空间的几个常见示例： [`abs()`](https://docs.python.org/zh-cn/3/library/functions.html#abs) 函数、内置异常等的内置函数集合；模块中的全局名称；函数调用中的局部名称。对象的属性集合也算是一种命名空间。关于命名空间的一个重要知识点是，不同命名空间中的名称之间绝对没有关系；例如，两个不同的模块都可以定义 `maximize` 函数，且不会造成混淆。用户使用函数时必须要在函数名前面附加上模块名。

点号之后的名称是 **属性**。例如，表达式 `z.real` 中，`real` 是对象 `z` 的属性。严格来说，对模块中名称的引用是属性引用：表达式 `modname.funcname` 中，`modname` 是模块对象，`funcname` 是模块的属性。模块属性和模块中定义的全局名称之间存在直接的映射：它们共享相同的命名空间！ [1例外](https://docs.python.org/zh-cn/3/tutorial/classes.html#id2)

属性可以是只读或者可写的。如果可写，则可对属性赋值。模块属性是可写时，可以使用 `modname.the_answer = 42` 。[`del`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#del) 语句可以删除可写属性。例如， `del modname.the_answer` 会删除 `modname` 对象中的 `the_answer` 属性。

命名空间是在不同时刻创建的，且拥有不同的生命周期。内置名称的命名空间是在 Python 解释器启动时创建的，永远不会被删除。模块的全局命名空间在读取模块定义时创建；通常，模块的命名空间也会持续到解释器退出。从脚本文件读取或交互式读取的，由解释器顶层调用执行的语句是 [`__main__`](https://docs.python.org/zh-cn/3/library/__main__.html#module-__main__) 模块调用的一部分，也拥有自己的全局命名空间。内置名称实际上也在模块里，即 [`builtins`](https://docs.python.org/zh-cn/3/library/builtins.html#module-builtins) 。

函数的本地命名空间在调用该函数时创建，并在函数返回或抛出不在函数内部处理的错误时被删除。 （实际上，用“遗忘”来描述实际发生的情况会更好一些。） 当然，每次递归调用都会有自己的本地命名空间。

**作用域** 是命名空间可直接访问的 Python 程序的文本区域。 “可直接访问” 的意思是，对名称的非限定引用会在命名空间中查找名称。

作用域虽然是静态确定的，但会被动态使用。执行期间的任何时刻，都会有 3 或 4 个命名空间可被直接访问的嵌套作用域：

- 最内层作用域，包含局部名称，并首先在其中进行搜索
- the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contain non-local, but also non-global names
- 倒数第二个作用域，包含当前模块的全局名称
- 最外层的作用域，包含内置名称的命名空间，最后搜索

If a name is declared global, then all references and assignments go directly to the next-to-last scope containing the module's global names. To rebind variables found outside of the innermost scope, the [`nonlocal`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) statement can be used; if not declared nonlocal, those variables are read-only (an attempt to write to such a variable will simply create a *new* local variable in the innermost scope, leaving the identically named outer variable unchanged).

通常，当前局部作用域将（按字面文本）引用当前函数的局部名称。在函数之外，局部作用域引用与全局作用域一致的命名空间：模块的命名空间。 类定义在局部命名空间内再放置另一个命名空间。

划重点，作用域是按字面文本确定的：模块内定义的函数的全局作用域就是该模块的命名空间，无论该函数从什么地方或以什么别名被调用。另一方面，实际的名称搜索是在运行时动态完成的。但是，Python 正在朝着“编译时静态名称解析”的方向发展，因此不要过于依赖动态名称解析！（局部变量已经是被静态确定了。）

Python 有一个特殊规定。如果不存在生效的 [`global`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 或 [`nonlocal`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) 语句，则对名称的赋值总是会进入最内层作用域。赋值不会复制数据，只是将名称绑定到对象。删除也是如此：语句 `del x` 从局部作用域引用的命名空间中移除对 `x` 的绑定。所有引入新名称的操作都是使用局部作用域：尤其是 [`import`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句和函数定义会在局部作用域中绑定模块或函数名称。

[`global`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 语句用于表明特定变量在全局作用域里，并应在全局作用域中重新绑定；[`nonlocal`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) 语句表明特定变量在外层作用域中，并应在外层作用域中重新绑定。

#### 作用域和命名空间示例

下例演示了如何引用不同作用域和名称空间，以及 [`global`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 和 [`nonlocal`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) 对变量绑定的影响：

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

示例代码的输出是：

```bash
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

注意，**局部** 赋值（这是默认状态）不会改变 *scope_test* 对 *spam* 的绑定。 [`nonlocal`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) 赋值会改变 *scope_test* 对 *spam* 的绑定，而 [`global`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 赋值会改变模块层级的绑定。

而且，[`global`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 赋值前没有 *spam* 的绑定。

### 初探类

类引入了一点新语法，三种新的对象类型和一些新语义。

#### 类定义语法

最简单的类定义形式如下：

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

与函数定义 ([`def`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#def) 语句) 一样，类定义必须先执行才能生效。把类定义放在 [`if`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#if) 语句的分支里或函数内部试试。

在实践中，类定义内的语句通常都是函数定义，但也可以是其他语句。这部分内容稍后再讨论。类里的函数定义一般是特殊的参数列表，这是由方法调用的约定规范所指明的 --- 同样，稍后再解释。

当进入类定义时，将创建一个新的命名空间，并将其用作局部作用域 --- 因此，所有对局部变量的赋值都是在这个新命名空间之内。 特别的，函数定义会绑定到这里的新函数名称。

当（从结尾处）正常离开类定义时，将创建一个 *类对象*。 这基本上是一个包围在类定义所创建命名空间内容周围的包装器；我们将在下一节了解有关类对象的更多信息。 原始的（在进入类定义之前起作用的）局部作用域将重新生效，类对象将在这里被绑定到类定义头所给出的类名称 (在这个示例中为 `ClassName`)。

#### Class 对象

类对象支持两种操作：属性引用和实例化。

*属性引用* 使用 Python 中所有属性引用所使用的标准语法: `obj.name`。 有效的属性名称是类对象被创建时存在于类命名空间中的所有名称。 因此，如果类定义是这样的:

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

那么 `MyClass.i` 和 `MyClass.f` 就是有效的属性引用，将分别返回一个整数和一个函数对象。 类属性也可以被赋值，因此可以通过赋值来更改 `MyClass.i` 的值。 `__doc__` 也是一个有效的属性，将返回所属类的文档字符串: `"A simple example class"`。



类的 *实例化* 使用函数表示法。 可以把类对象视为是返回该类的一个新实例的不带参数的函数。 举例来说（假设使用上述的类）:

```python
x = MyClass()
```

创建类的新 *实例* 并将此对象分配给局部变量 `x`。

实例化操作（“调用”类对象）会创建一个空对象。 许多类喜欢创建带有特定初始状态的自定义实例。 为此类定义可能包含一个名为 `__init__()` 的特殊方法，就像这样:

```python
def __init__(self):
    self.data = []
```

When a class defines an `__init__()` method, class instantiation automatically invokes `__init__()` for the newly created class instance. So in this example, a new, initialized instance can be obtained by:

```python
x = MyClass()
```

当然，`__init__()` 方法还可以有额外参数以实现更高灵活性。 在这种情况下，提供给类实例化运算符的参数将被传递给 `__init__()`。 例如，

```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i
(3.0, -4.5)
```

#### 实例对象

现在我们能用实例对象做什么？ 实例对象所能理解的唯一操作是属性引用。 有两种有效的属性名称：数据属性和方法。

*数据属性* 对应于 Smalltalk 中的“实例变量”，以及 C++ 中的“数据成员”。 数据属性不需要声明；像局部变量一样，它们将在第一次被赋值时产生。 例如，如果 `x` 是上面创建的 `MyClass` 的实例，则以下代码段将打印数值 `16`，且不保留任何追踪信息:

```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

另一类实例属性引用称为 *方法*。 方法是“从属于”对象的函数。 （在 Python 中，方法这个术语并不是类实例所特有的：其他对象也可以有方法。 例如，列表对象具有 append, insert, remove, sort 等方法。 然而，在以下讨论中，我们使用方法一词将专指类实例对象的方法，除非另外显式地说明。）

实例对象的有效方法名称依赖于其所属的类。 根据定义，一个类中所有是函数对象的属性都是定义了其实例的相应方法。 因此在我们的示例中，`x.f` 是有效的方法引用，因为 `MyClass.f` 是一个函数，而 `x.i` 不是方法，因为 `MyClass.i` 不是函数。 但是 `x.f` 与 `MyClass.f` 并不是一回事 --- 它是一个 *方法对象*，不是函数对象。

#### 方法对象

通常，方法在绑定后立即被调用:

```python
x.f()
```

在 `MyClass` 示例中，这将返回字符串 `'hello world'`。 但是，立即调用一个方法并不是必须的: `x.f` 是一个方法对象，它可以被保存起来以后再调用。 例如:

```python
xf = x.f
while True:
    print(xf())
```

将持续打印 `hello world`，直到结束。

当一个方法被调用时到底发生了什么？ 你可能已经注意到上面调用 `x.f()` 时并没有带参数，虽然 `f()` 的函数定义指定了一个参数。 这个参数发生了什么事？ 当不带参数地调用一个需要参数的函数时 Python 肯定会引发异常 --- 即使参数实际未被使用...

实际上，你可能已经猜到了答案：方法的特殊之处就在于实例对象会作为函数的第一个参数被传入。 在我们的示例中，调用 `x.f()` 其实就相当于 `MyClass.f(x)`。 总之，调用一个具有 *n* 个参数的方法就相当于调用再多一个参数的对应函数，这个参数值为方法所属实例对象，位置在其他参数之前。

如果你仍然无法理解方法的运作原理，那么查看实现细节可能会弄清楚问题。 当一个实例的非数据属性被引用时，将搜索实例所属的类。 如果被引用的属性名称表示一个有效的类属性中的函数对象，会通过打包（指向）查找到的实例对象和函数对象到一个抽象对象的方式来创建方法对象：这个抽象对象就是方法对象。 当附带参数列表调用方法对象时，将基于实例对象和参数列表构建一个新的参数列表，并使用这个新参数列表调用相应的函数对象。

#### 类和实例变量

一般来说，实例变量用于每个实例的唯一数据，而类变量用于类的所有实例共享的属性和方法:

```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```

正如 [名称和对象](https://docs.python.org/zh-cn/3/tutorial/classes.html#tut-object) 中已讨论过的，共享数据可能在涉及 [mutable](https://docs.python.org/zh-cn/3/glossary.html#term-mutable) 对象例如列表和字典的时候导致令人惊讶的结果。 例如以下代码中的 *tricks* 列表不应该被用作类变量，因为所有的 *Dog* 实例将只共享一个单独的列表:

```python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

正确的类设计应该使用实例变量:

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

### 补充说明

如果同样的属性名称同时出现在实例和类中，则属性查找会优先选择实例:

```python
class Warehouse:
   purpose = 'storage'
   region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
storage west
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)
storage east
```

数据属性可以被方法以及一个对象的普通用户（“客户端”）所引用。 换句话说，类不能用于实现纯抽象数据类型。 实际上，在 Python 中没有任何东西能强制隐藏数据 --- 它是完全基于约定的。 （而在另一方面，用 C 语言编写的 Python 实现则可以完全隐藏实现细节，并在必要时控制对象的访问；此特性可以通过用 C 编写 Python 扩展来使用。）

客户端应当谨慎地使用数据属性 --- 客户端可能通过直接操作数据属性的方式破坏由方法所维护的固定变量。 请注意客户端可以向一个实例对象添加他们自己的数据属性而不会影响方法的可用性，只要保证避免名称冲突 --- 再次提醒，在此使用命名约定可以省去许多令人头痛的麻烦。

在方法内部引用数据属性（或其他方法！）并没有简便方式。 我发现这实际上提升了方法的可读性：当浏览一个方法代码时，不会存在混淆局部变量和实例变量的机会。

方法的第一个参数常常被命名为 `self`。 这也不过就是一个约定: `self` 这一名称在 Python 中绝对没有特殊含义。 但是要注意，不遵循此约定会使得你的代码对其他 Python 程序员来说缺乏可读性，而且也可以想像一个 *类浏览器* 程序的编写可能会依赖于这样的约定。

任何一个作为类属性的函数都为该类的实例定义了一个相应方法。 函数定义的文本并非必须包含于类定义之内：将一个函数对象赋值给一个局部变量也是可以的。 例如:

```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```

现在 `f`, `g` 和 `h` 都是 `C` 类的引用函数对象的属性，因而它们就都是 `C` 的实例的方法 --- 其中 `h` 完全等同于 `g`。 但请注意，本示例的做法通常只会令程序的阅读者感到迷惑。

方法可以通过使用 `self` 参数的方法属性调用其他方法:

```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

方法可以通过与普通函数相同的方式引用全局名称。 与方法相关联的全局作用域就是包含其定义的模块。 （类永远不会被作为全局作用域。） 虽然我们很少会有充分的理由在方法中使用全局作用域，但全局作用域存在许多合理的使用场景：举个例子，导入到全局作用域的函数和模块可以被方法所使用，在其中定义的函数和类也一样。 通常，包含该方法的类本身是在全局作用域中定义的，而在下一节中我们将会发现为何方法需要引用其所属类的很好的理由。

每个值都是一个对象，因此具有 *类* （也称为 *类型*），并存储为 `object.__class__` 。

### 其他

```python
print
```



### 继承

当然，如果不支持继承，语言特性就不值得称为“类”。派生类定义的语法如下所示:

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

名称 `BaseClassName` 必须定义于包含派生类定义的作用域中。 也允许用其他任意表达式代替基类名称所在的位置。 这有时也可能会用得上，例如，当基类定义在另一个模块中的时候:

```python
class DerivedClassName(modname.BaseClassName):
```

派生类定义的执行过程与基类相同。 当构造类对象时，基类会被记住。 此信息将被用来解析属性引用：如果请求的属性在类中找不到，搜索将转往基类中进行查找。 如果基类本身也派生自其他某个类，则此规则将被递归地应用。

派生类的实例化没有任何特殊之处: `DerivedClassName()` 会创建该类的一个新实例。 方法引用将按以下方式解析：搜索相应的类属性，如有必要将按基类继承链逐步向下查找，如果产生了一个函数对象则方法引用就生效。

派生类可能会重写其基类的方法。 因为方法在调用同一对象的其他方法时没有特殊权限，所以调用同一基类中定义的另一方法的基类方法最终可能会调用覆盖它的派生类的方法。 （对 C++ 程序员的提示：Python 中所有的方法实际上都是 `virtual` 方法。）

在派生类中的重载方法实际上可能想要扩展而非简单地替换同名的基类方法。 有一种方式可以简单地直接调用基类方法：即调用 `BaseClassName.methodname(self, arguments)`。 有时这对客户端来说也是有用的。 （请注意仅当此基类可在全局作用域中以 `BaseClassName` 的名称被访问时方可使用此方式。）

Python有两个内置函数可被用于继承机制：

- 使用 [`isinstance()`](https://docs.python.org/zh-cn/3/library/functions.html#isinstance) 来检查一个实例的类型: `isinstance(obj, int)` 仅会在 `obj.__class__` 为 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 或某个派生自 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 的类时为 `True`。
- 使用 [`issubclass()`](https://docs.python.org/zh-cn/3/library/functions.html#issubclass) 来检查类的继承关系: `issubclass(bool, int)` 为 `True`，因为 [`bool`](https://docs.python.org/zh-cn/3/library/functions.html#bool) 是 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 的子类。 但是，`issubclass(float, int)` 为 `False`，因为 [`float`](https://docs.python.org/zh-cn/3/library/functions.html#float) 不是 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 的子类。

#### 多重继承

Python 也支持一种多重继承。 带有多个基类的类定义语句如下所示:

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

对于多数应用来说，在最简单的情况下，你可以认为搜索从父类所继承属性的操作是深度优先、从左至右的，当层次结构中存在重叠时不会在同一个类中搜索两次。 因此，如果某一属性在 `DerivedClassName` 中未找到，则会到 `Base1` 中搜索它，然后（递归地）到 `Base1` 的基类中搜索，如果在那里未找到，再到 `Base2` 中搜索，依此类推。

真实情况比这个更复杂一些；方法解析顺序会动态改变以支持对 [`super()`](https://docs.python.org/zh-cn/3/library/functions.html#super) 的协同调用。 这种方式在某些其他多重继承型语言中被称为后续方法调用，它比单继承型语言中的 super 调用更强大。

动态改变顺序是有必要的，因为所有多重继承的情况都会显示出一个或更多的菱形关联（即至少有一个父类可通过多条路径被最底层类所访问）。 例如，所有类都是继承自 [`object`](https://docs.python.org/zh-cn/3/library/functions.html#object)，因此任何多重继承的情况都提供了一条以上的路径可以通向 [`object`](https://docs.python.org/zh-cn/3/library/functions.html#object)。 为了确保基类不会被访问一次以上，动态算法会用一种特殊方式将搜索顺序线性化， 保留每个类所指定的从左至右的顺序，只调用每个父类一次，并且保持单调（即一个类可以被子类化而不影响其父类的优先顺序）。 总而言之，这些特性使得设计具有多重继承的可靠且可扩展的类成为可能。 要了解更多细节，请参阅 https://www.python.org/download/releases/2.3/mro/。

### 私有变量

那种仅限从一个对象内部访问的“私有”实例变量在 Python 中并不存在。 但是，大多数 Python 代码都遵循这样一个约定：带有一个下划线的名称 (例如 `_spam`) 应该被当作是 API 的非公有部分 (无论它是函数、方法或是数据成员)。 这应当被视为一个实现细节，可能不经通知即加以改变。

由于存在对于类私有成员的有效使用场景（例如避免名称与子类所定义的名称相冲突），因此存在对此种机制的有限支持，称为 *名称改写*。 任何形式为 `__spam` 的标识符（至少带有两个前缀下划线，至多一个后缀下划线）的文本将被替换为 `_classname__spam`，其中 `classname` 为去除了前缀下划线的当前类名称。 这种改写不考虑标识符的句法位置，只要它出现在类定义内部就会进行。

名称改写有助于让子类重载方法而不破坏类内方法调用。例如:

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

上面的示例即使在 `MappingSubclass` 引入了一个 `__update` 标识符的情况下也不会出错，因为它会在 `Mapping` 类中被替换为 `_Mapping__update` 而在 `MappingSubclass` 类中被替换为 `_MappingSubclass__update`。

请注意，改写规则的设计主要是为了避免意外冲突；访问或修改被视为私有的变量仍然是可能的。这在特殊情况下甚至会很有用，例如在调试器中。

请注意传递给 `exec()` 或 `eval()` 的代码不会将发起调用类的类名视作当前类；这类似于 `global` 语句的效果，因此这种效果仅限于同时经过字节码编译的代码。 同样的限制也适用于 `getattr()`, `setattr()` 和 `delattr()`，以及对于 `__dict__` 的直接引用。



### 杂项说明

Sometimes it is useful to have a data type similar to the Pascal "record" or C "struct", bundling together a few named data items. The idiomatic approach is to use [`dataclasses`](https://docs.python.org/zh-cn/3/library/dataclasses.html#module-dataclasses) for this purpose:

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int
```

```bash
john = Employee('john', 'computer lab', 1000)
john.dept
'computer lab'
john.salary
1000
```

一段需要特定抽象数据类型的 Python 代码往往可以被传入一个模拟了该数据类型的方法的类作为替代。 例如，如果你有一个基于文件对象来格式化某些数据的函数，你可以定义一个带有 `read()` 和 `readline()` 方法从字符串缓存获取数据的类，并将其作为参数传入。

实例方法对象也具有属性: `m.__self__` 就是带有 `m()` 方法的实例对象，而 `m.__func__` 则是该方法所对应的函数对象。

### 迭代器

到目前为止，您可能已经注意到大多数容器对象都可以使用 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 语句:

```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

这种访问风格清晰、简洁又方便。 迭代器的使用非常普遍并使得 Python 成为一个统一的整体。 在幕后，[`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 语句会在容器对象上调用 [`iter()`](https://docs.python.org/zh-cn/3/library/functions.html#iter)。 该函数返回一个定义了 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法的迭代器对象，此方法将逐一访问容器中的元素。 当元素用尽时，[`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 将引发 [`StopIteration`](https://docs.python.org/zh-cn/3/library/exceptions.html#StopIteration) 异常来通知终止 `for` 循环。 你可以使用 [`next()`](https://docs.python.org/zh-cn/3/library/functions.html#next) 内置函数来调用 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法；这个例子显示了它的运作方式:

```bash
s = 'abc'
it = iter(s)
it
<str_iterator object at 0x10c90e650>
next(it)
'a'
next(it)
'b'
next(it)
'c'
next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```

看过迭代器协议的幕后机制，给你的类添加迭代器行为就很容易了。 定义一个 `__iter__()` 方法来返回一个带有 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法的对象。 如果类已定义了 `__next__()`，则 `__iter__()` 可以简单地返回 `self`:

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

```bash
rev = Reverse('spam')
iter(rev)
<__main__.Reverse object at 0x00A1DB50>
for char in rev:
    print(char)

m
a
p
s
```

### 生成器

[生成器](https://docs.python.org/zh-cn/3/glossary.html#term-generator) 是一个用于创建迭代器的简单而强大的工具。 它们的写法类似于标准的函数，但当它们要返回数据时会使用 [`yield`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#yield) 语句。 每次在生成器上调用 [`next()`](https://docs.python.org/zh-cn/3/library/functions.html#next) 时，它会从上次离开的位置恢复执行（它会记住上次执行语句时的所有数据值）。 一个显示如何非常容易地创建生成器的示例如下:

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```

```bash
for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```

可以用生成器来完成的操作同样可以用前一节所描述的基于类的迭代器来完成。 但生成器的写法更为紧凑，因为它会自动创建 `__iter__()` 和 [`__next__()`](https://docs.python.org/zh-cn/3/reference/expressions.html#generator.__next__) 方法。

另一个关键特性在于局部变量和执行状态会在每次调用之间自动保存。 这使得该函数相比使用 `self.index` 和 `self.data` 这种实例变量的方式更易编写且更为清晰。

除了会自动创建方法和保存程序状态，当生成器终结时，它们还会自动引发 [`StopIteration`](https://docs.python.org/zh-cn/3/library/exceptions.html#StopIteration)。 这些特性结合在一起，使得创建迭代器能与编写常规函数一样容易。

### 生成器表达式

某些简单的生成器可以写成简洁的表达式代码，所用语法类似列表推导式，但外层为圆括号而非方括号。 这种表达式被设计用于生成器将立即被外层函数所使用的情况。 生成器表达式相比完整的生成器更紧凑但较不灵活，相比等效的列表推导式则更为节省内存。

```bash
sum(i*i for i in range(10))                 # sum of squares
285

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

unique_words = set(word for line in page  for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```

## 标准库简介

### 操作系统接口

[`os`](https://docs.python.org/zh-cn/3/library/os.html#module-os) 模块提供了许多与操作系统交互的函数:

```python
import os
os.getcwd()      # Return the current working directory
'C:\\Python311'
os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell
0
```

一定要使用 `import os` 而不是 `from os import *` 。这将避免内建的 [`open()`](https://docs.python.org/zh-cn/3/library/functions.html#open) 函数被 [`os.open()`](https://docs.python.org/zh-cn/3/library/os.html#os.open) 隐式替换掉，因为它们的使用方式大不相同。

内置的 [`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir) 和 [`help()`](https://docs.python.org/zh-cn/3/library/functions.html#help) 函数可用作交互式辅助工具，用于处理大型模块，如 [`os`](https://docs.python.org/zh-cn/3/library/os.html#module-os):

```python
import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```

对于日常文件和目录管理任务， [`shutil`](https://docs.python.org/zh-cn/3/library/shutil.html#module-shutil) 模块提供了更易于使用的更高级别的接口:

```python
import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```

## 编码

### 常见的编码格式

- utf-8
- url编码

### 解码

#### url解码

常用的python url解码代码 ：

1. 使用urllib库的unquote方法进行url解码：
```python
import urllib
url = "https://www.example.com/?q=%E6%9D%8E%E5%9B%9B"
decoded_url = urllib.parse.unquote(url)
print(decoded_url)
```
输出结果为：`https://www.example.com/?q=李四`
2. 使用requests库的unquote方法进行url解码：
```python
import requests
url = "https://www.example.com/?q=%E6%9D%8E%E5%9B%9B"
decoded_url = requests.utils.unquote(url)
print(decoded_url)
```
输出结果为：`https://www.example.com/?q=李四`
3. 使用urllib.parse.unquote_plus方法进行url解码，该方法会将空格解码为加号：
```python
import urllib.parse
url = "https://www.example.com/?q=%E6%9D%8E%E5%9B%9B+%E5%8A%A0%E5%8A%A0"
decoded_url = urllib.parse.unquote_plus(url)
print(decoded_url)
```

## 异步编程

### 异步等待

```python
import asyncio

async def time_consuming():
    print('开始耗时操作')
    await asyncio.sleep(3)
    print('3秒后')

async def main():
    print('其他操作')
    await time_consuming()
    print('继续进行其他操作')
    
asyncio.run(main())

# 其他操作
# 开始耗时操作
# 3秒后
# 继续进行其他操作
```



# 进阶概念

## 常见问题

- [Python常见问题](https://docs.python.org/zh-cn/3/faq/general.html)
- [编程常见问题](https://docs.python.org/zh-cn/3/faq/programming.html)
- [设计和历史常见问题](https://docs.python.org/zh-cn/3/faq/design.html)
- [代码库和插件 FAQ](https://docs.python.org/zh-cn/3/faq/library.html)
- [扩展/嵌入常见问题](https://docs.python.org/zh-cn/3/faq/extending.html)
- [Python在Windows上的常见问题](https://docs.python.org/zh-cn/3/faq/windows.html)
- [图形用户界面（GUI）常见问题](https://docs.python.org/zh-cn/3/faq/gui.html)
- [“为什么我的电脑上安装了 Python ？”](https://docs.python.org/zh-cn/3/faq/installed.html)

## `if name main`的作用

```python
if __name__ == "__main__":
```

一个python文件通常有两种使用方法

- 第一是作为脚本直接执行
- 第二是 import 到其他的 python 脚本中被调用（模块重用）执行。

因此`if __name__ == "__main__":` 的作用就是控制这两种情况执行代码的过程，在`if __name__ == "__main__":` 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，而 import 到其他脚本中是不会被执行的。

举例说明如下：

**直接执行**

在 test.py 中写入如下代码：

```python
print('this is one')
if __name__ == "__main__":
    print('this is two')
```

直接执行`python3  test.py`，结果如下图，可以成功 print 两行字符串。即，`if __name__ == "__main__":`语句之前和之后的代码都被执行。

![image-20230418093555629](image-20230418093555629.png)

**import 执行**

然后在同一文件夹新建名称为 import_test.py 的脚本，输入如下代码：

```python
import test

```

执行`python3 import_test.py` 脚本，输出结果如下：

![image-20230418093951722](image-20230418093951722.png)

作为模块import执行，只输出了第一行字符串。即，`if __name__ == "__main__":`外部的语句被执行，内部的没有被执行。

**运行原理**

每个python模块（python文件，也就是此处的 test.py 和 import_test.py）都包含内置的变量 `__name__`，当该模块被直接当作脚本执行的时候，`__name__` 等于`__main__`；如果该模块 import 到其他模块中，则该模块的 `__name__` 等于模块（文件）名称（不包含后缀.py）。

进而当模块被直接当作脚本执行时，`__name__` ==  '`__main__`' 结果为真。

为了进一步说明，使用如下代码验证：

```python
# test.py
print('this is one')
print('__name__: ', __name__ )

if(__name__ == '__main__'):
    print('this is two')
```

直接以脚本运行，结果如下

![image-20230419094141166](image-20230419094141166.png)

新建`import_test.py`

```python
# import_test.py

import test
```

运行`python3 import_test.py`，结果如下：

![image-20230419094318903](image-20230419094318903.png)




## 上下文管理器

Context Manager指的是python在执行一段代码前后，做的一些预处理和后处理，使得代码块运行处于一个小的环境（surrounding），出了这个小环境之后，资源释放，环境中的各种配置也失效。

例如在打开文件需要关闭，连接数据库后需要关闭连接。很多优雅第三方库也会利用上下文使得对象进入特定的某种状态。

###  with关键字

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

###  例子

####  资源操作：

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

#### 状态维护

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

###  使用contextlib简化编写

python内置的标准库contextlib可以使得代码书写更加简洁，本质是一样的。比较有用的是`contextlib.contextmanager`这个装饰器，被装饰的函数在`yield`的前面相当于__enter__，yield的后面相当于__exit__，`yield`本身的返回值赋给`as`后的变量

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

## `__init__.py`

[Python中常见的__init__.py是什么意思？详解Python import的方式和原理](https://zhuanlan.zhihu.com/p/482687037)

Python包以`__init__.py`为标志，用于实现工程模块化，假设包组织结构的实例如下：

```python
package
    |- subpackage1
        |- __init__.py
        |- moduleA.py       #fun1() fun2()
    |- subpackage2
        |- __init__.py
        |- moduleA.py       #fun1()
        |- moduleB.py       #fun3() fun4()
```

用**虚拟文件夹**的方式理解Python包。所有的包都可视作文件夹，其下包含模块或子包(子文件夹)，模块中包含函数、类、变量等属性。当前路径位置可视作一个空白文件夹，关键字from理解为“打开”，关键字import理解为“导入”，必须指出：所有import相关操作都要落实到模块或属性。

一般地，导入有如下方式：

```python
import subpackage1.moduleA
```

此方式相当于把一个名为subpackage1的文件夹复制粘贴到当前路径下，文件夹只包含模块moduleA，即使subpackage1中可能还有其他模块，引用moduleA中的func1()需要subpackage1.moduleA.fun1()，即打开subpackage1文件夹，再使用模块moduleA中的属性fun1()。注意，如果仅import subpackage1，相当于只引入了一个空文件夹，此时无法调用fun1()，除非在__init__.py中提前导入了模块。

```python
from subpackage1 import moduleA
```

此方式相当于打开一个名为subpackage1的文件夹，再将其中的模块moduleA复制粘贴到当前空白文件夹下，引用moduleA的fun1()需要moduleA.fun1()。这种方式下，还有`from subpackage1 import *`的句式可以引入包中的所有模块。

```python
from subpackage.moduleA import fun1()
```

此方式相当于打开一个名为subpackage1的文件夹下的模块moduleA，再将其中的fun1()复制粘贴到当前空白文件夹，引用fun1()只需fun1()即可。



除了应用上述导入句式外，还需要注意当前文件的运行路径，如下所示为一个忽略路径因素造成的导入包报错，因为运行目录`app\pkg_2\`下没有文件pkg_1且环境变量中也不存在pkg_1。



```bash
app
    |- pkg_1
        |- __init__.py
        |- moduleA.py    # fun1()
    |- pkg_2
        |- __init__.py
        |- test.py

# test.py中引用
# from pkg_1.moduleA import fun1
# 执行如下
>>> python app\pkg_2\test.py
>>> from pkg_1.moduleA import fun1
ModuleNotFoundError: No module named 'pkg_1'
```

若需要保持运行目录不变，必须进行环境变量配置，在import pkg_1前先添加父级目录到python解释器的运行环境变量中，在pkg_2的父级目录app下可访问到pkg_1，具体实现上依赖于sys和os包

```python
import sys, os
sys.path.append(os.path.realpath('..'))
```

或者更换执行脚本的目录

## `python -m`参数详解

[Python 中 -m 的典型用法、原理解析与发展演变](https://www.jb51.net/article/174005.htm)

> 这篇文章主要介绍了Python 中 -m 的典型用法、原理解析与发展演变,需要的朋友可以参考下

在命令行中使用 Python 时，它可以接收大约 20 个选项（option），语法格式如下：

```bash
python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]
```

本文想要聊聊比较特殊的“-m”选项： **关于它的典型用法、原理解析与发展演变的过程。**

首先，让我们用“--help”来看看它的解释：

![image-20230513091520505](image-20230513091520505.png)

```bash
-m mod run library module as a script (terminates option list)
```

"mod"是“module”的缩写，即“-m”选项后面的内容是 module（模块），其作用是把模块当成脚本来运行。

“terminates option list”意味着“-m”之后的其它选项不起作用，在这点上它跟“-c”是一样的，都是“终极选项”。官方把它们定义为“接口选项”（Interface options），需要区别于其它的普通选项或通用选项。

### `-m` 选项的五个典型用法

Python 中有很多使用 -m 选项的场景，相信大家可能会用到或者看见过，我在这里想分享 5 个。

在 Python3 中，只需一行命令就能实现一个简单的 HTTP 服务：

```python
python -m http.server 8000

# 注:在 Python2 中是这样
python -m SimpleHTTPServer 8000
```

![image-20230513091810360](image-20230513091810360.png)

执行后，在本机打开“ [http://localhost:8000](http://localhost:8000/) ”，或者在局域网内的其它机器上打开“ http://本机ip:8000  ”，就能访问到执行目录下的内容，例如下图就是我本机的内容：

![image-20230513092021536](image-20230513092021536.png)

与此类似，我们只需要一行命令“`python -m pydoc -p xxx`”，就能生成 HTML 格式的官方帮助文档，可以在浏览器中访问。

![image-20230513092039704](image-20230513092039704.png)

上面的命令执行了 pydoc 模块，会在 9000 端口启动一个 http 服务，在浏览器中打开，我的结果如下：

![image-20230513092554190](image-20230513092554190.png)

它的第三个常见用法是执行 pdb 的调试命令“`python -m pdb xxx.py`”，以调试模式来执行“xxx.py”脚本：

![image-20230513093953496](image-20230513093953496.png)

第四个同样挺有用的场景是用 timeit 在命令行中测试一小段代码的运行时间。以下的 3 段代码，用不同的方式拼接 “0-1-2-……-99” 数字串。可以直观地看出它们的效率差异：

![image-20230513094019458](image-20230513094019458.png)

最后，还有一种常常被人忽略的场景：“python -m pip install xxx”。我们可能会习惯性地使用“pip install xxx”，或者做了版本区分时用“pip3 install xxx”，总之不在前面用“python -m”做指定。但这种写法可能会出问题。

很巧合的是，在本月初（2019.11.01），Python 的核心开发者、[第一届指导委员会 五人成员之一的 Brett Cannon ](https://mp.weixin.qq.com/s/hjcVFaGgI_Ww--Ktv7XP9Q)专门写了一篇博客《 [Why you should use "python -m pip](https://snarky.ca/why-you-should-use-python-m-pip/)" 》，提出应该使用“python -m pip”的方式，并做了详细的解释。

他的主要观点是：在存在多个 Python 版本的环境中，这种写法可以精确地控制三方库的安装位置。例如用“python3.8 -m pip”，可以明确指定给 3.8 版本安装，而不会混淆成其它的版本。

（延伸阅读：关于 Brett 的文章，这有一篇简短的归纳《 [原来我一直安装 Python 库的姿势都不对呀！](https://www.jb51.net/article/174002.htm) 》）

### `-m` 选项的两种原理解析

看了前面的几种典型用法，你是否开始好奇： **“-m”是怎么运作的？它是怎么实现的？**

对于“python -m name”，一句话解释： Python 会检索 `sys.path` ，查找名字为“name”的模块或者包（含命名空间包），并将其内容当成“`__main__`”模块来执行。

**对于普通模块**

以“.py”为后缀的文件就是一个模块，在“-m”之后使用时，只需要使用模块名，不需要写出后缀，但前提是该模块名是有效的，且不能是用 C 语言写成的模块。

在“-m”之后，如果是一个无效的模块名，则会报错“No module named xxx”。

如果是一个带后缀的模块，则首先会导入该模块，然后可能报错：Error while finding module specification for 'xxx.py' (AttributeError: module 'xxx' has no attribute '`__path__`'。

```python
# -*- encoding: utf-8 -*-

if __name__ == '__main__':
    print('Hello world')
    print('Hello pythoncat')
```



![image-20230513153645196](image-20230513153645196.png)

对于一个普通模块，有时候这两种写法表面看起来是等效的：

![image-20230513153702587](image-20230513153702587.png)

两种写法都会把定位到的模块脚本当成主程序入口来执行，即在执行时，该脚本的 `__name__` 都是”`__main__`“，跟 import 导入方式是不同的。

但它的前提是：在执行目录中存在着“test.py”，且只有唯一的“test”模块。对于本例，如果换一个目录执行的话，“python test.py”当然会报找不到文件的错误，然而，“`python -m test`”却不会报错，因为解释器在遍历 `sys.path` 时可以找到同名的“test”模块，并且执行

![image-20230513154302073](image-20230513154302073.png)

由此差异，我们其实可以总结出“-m”的用法： 已知一个模块的名字，但不知道它的文件路径，那么使用“-m”就意味着交给解释器自行查找，若找到，则当成脚本执行。

以前文的“`python -m http.server 8000`”为例，我们也可以找到“server”模块的绝对路径，然后执行，尽管这样会变得很麻烦。

![image-20230513154334903](image-20230513154334903.png)

那么，“-m”方式与直接运行脚本相比，在实现上有什么不同呢？

1、直接运行脚本时，相当于给出了脚本的完整路径（不管是绝对路径还是相对路径），解释器根据 **文件系统的查找机制，** 定位到该脚本，然后执行 

使用“-m”方式时，解释器需要在不 import 的情况下，在 **所有模块命名空间** 中查找，定位到脚本的路径，然后执行。为了实现这个过程，解释器会借助两个模块： `pkgutil` 和 `runpy` ，前者用来获取所有的模块列表，后者根据模块名来定位并执行脚本 

2、对于包内模块，如果“-m”之后要执行的是一个包，那么解释器经过前面提到的查找过程，先定位到该包，然后会去执行它的“`__main__`”子模块，也就是说，在包目录下需要实现一个“`__main__`.py”文件。

换句话说，假设有个包的名称是“pname”，那么， “python -m pname”，其实就等效于“python -m pname.`__main__`”。

仍以前文创建 HTTP 服务为例，“http”是 Python 内置的一个包，它没有“`__main__.py”`文件，所以使用“-m”方式执行时，就会报错：No module named http.`__main__`; 'http' is a package and cannot be directly executed。

![image-20230513154627118](image-20230513154627118.png)

作为对比，我们可以看看前文提到的 pip，它也是一个包，为什么“python -m pip”的方式可以使用呢？当然是因为它有“`__main__`.py”文件：

![image-20230513155153049](image-20230513155153049.png)

“python -m pip”实际上执行的就是这个“`__main__`.py”文件，它主要作为一个调用入口，调用了核心的"pip._internal.main"。

http 包因为没有一个统一的入口模块，所以采用了“python -m 包.模块”的方式，而 pip 包因为有统一的入口模块，所以加了一个“__main__.py”文件，最后只需要写“python -m 包”，简明直观。

### `-m` 选项的十年演变过程

最早引入 -m 选项的是 Python 2.4 版本（2004年），当时功能还挺受限，只能作用于普通的内置模块（如 pdb 和 profile）。

随后，知名开发者 Nick Coghlan 提出的《[PEP 338 -- Executing modules as scripts ](https://www.python.org/dev/peps/pep-0338/)》把它的功能提升了一个台阶。这个 PEP 在 2004 年提出，最终实现在 2006 年的 2.5 版本。

（插个题外话：Nick Coghlan 是核心开发者中的核心之一，也是第一届指导委员会的五人成员之一。记得当初看材料，他是在 2005 年被选为核心开发者的，这时间与 PEP-338 的时间紧密贴合）

![image-20230513155322761](image-20230513155322761.png)

这个 PEP 的几个核心点是：

- 结合了 PEP-302 的新探针机制（new import hooks），提升了解释器查找包内模块的能力
- 结合了其它的导入机制（例如 `zipimport` 和冻结模块(frozen modules)），拓展了解释器查找模块的范围与精度
- 开发了新的 `runpy.run_module(modulename)` 来实现本功能，而不用修改 CPython 解释器，如此可方便移植到其它解释器

至此，-m 选项使得 Python 可以在所有的命名空间内定位到命令行中给定的模块。

2009 年，在 Python 3.1 版本中，只需给定包的名称，就能定位和运行它的“`__main__`”子模块。2014 年，-m 扩展到支持命名空间包。

至此，经过十年的发展演变，-m 选项变得功能齐全，羽翼丰满。

最后，我们来个 ending 吧：-m 选项可能看似不起眼，但它绝对是最特别的选项之一，它使得在命令行中，使用内置模块、标准包与三方库时变得更轻松便利。有机会就多用一下吧，体会它带来的愉悦体验。

参考材料

https://docs.python.org/3.7/using/cmdline.html#cmdoption-m

https://snarky.ca/why-you-should-use-python-m-pip

https://www.python.org/dev/peps/pep-0338/

## 调试 Python 程序

### pdb 调试 Python 程序

[命令行下 pdb 调试 Python 程序](https://blog.csdn.net/lyshark_lyshark/article/details/125846871)

> 官方参考网站 The Python Debugger ： https://docs.python.org/3/library/pdb.html
> gdb 调试命令的使用及总结：https://blog.csdn.net/freeking101/article/details/54406982
> 使用 Pdb 调试 Python：https://segmentfault.com/a/1190000006628456
>
> 增强的调试器，比如 IPython 的 ipdb 和 pdb++



# 模块专题

>  [Python 标准库 — Python 3.11.3 文档](https://docs.python.org/zh-cn/3/library/index.html)

## 生成数据

### Faker

Faker是一个Python库，主要用于生成各种类型的虚假数据，包括但不限于姓名、地址、电子邮件、电话号码、公司名称、身份证号码、信用卡信息等。Faker的目的是帮助数据科学家、开发人员和测试人员快速、高效地创建随机数据，以满足测试和演示的需要。

https://blog.csdn.net/qq_41130705/article/details/125204884

https://zhuanlan.zhihu.com/p/620757661







## requests

## numpy

> [NumPy documentation — NumPy v1.24 Manual](https://numpy.org/doc/stable/)
>
> 教程：

### 发展历史

NumPy是一个开源的Python科学计算库，能够直接对数组和矩阵进行操作，可以省略很多循环语句，众多的数学函数也会让编写代码的工作轻松许多。

安装方式：

   （1）在终端输入：`pip install numpy`

   （2） 第二种：`conda install numpy`



NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

NumPy 的前身 Numeric 最早是由 Jim Hugunin 与其它协作者共同开发，2005 年，Travis Oliphant 在 Numeric 中结合了另一个同性质的程序库 Numarray 的特色，并加入了其它扩展而开发了 NumPy。NumPy 为开放源代码并且由许多协作者共同维护开发。

NumPy 是一个运行速度非常快的数学库，主要用于数组计算，包含：

- 一个强大的N维数组对象 ndarray
- 广播功能函数
- 整合 C/C++/Fortran 代码的工具
- 线性代数、傅里叶变换、随机数生成等功能

**numpy应用**

NumPy 通常与 SciPy（Scientific Python）和 Matplotlib（绘图库）一起使用， 这种组合广泛用于替代 MatLab，是一个强大的科学计算环境，有助于我们通过 Python 学习数据科学或者机器学习。

SciPy 是一个开源的 Python 算法库和数学工具包。

SciPy 包含的模块有最优化、线性代数、积分、插值、特殊函数、快速傅里叶变换、信号处理和图像处理、常微分方程求解和其他科学与工程中常用的计算。

Matplotlib 是 Python 编程语言及其数值数学扩展包 NumPy 的可视化操作界面。它为利用通用的图形用户界面工具包，如 Tkinter, wxPython, Qt 或 GTK+ 向应用程序嵌入式绘图提供了应用程序接口（API）。

### numpy核心

- 多维数组
  - 掌握到二维数组的处理，基本就够用了
  - 能够用numpy去处理，之前用列表时处理的问题（用多维数组去替换列表使用）

- 代码简洁：减少python代码中的循环
- 底层实现：厚内核（C） + 薄接口（Python），保证性能

### 安装numpy

```bash
pip3 install numpy scipy matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### ndarray数组对象介绍

之前用列表保存一组数据，现在用ndarray数组保存一组数据

学习过程中，要比较和列表的差异以加深印象，如增删改查、切片等

用`np.ndarray`类的对象，表示n维数组

```python
import numpy as np
ary = np.array([1, 2, 3, 4, 5, 6])
print(ary, type(ary)) # [1 2 3 4 5 6] <class 'numpy.ndarray'>

# 维度 
print(ary.ndim) # 1
# 形状
print(ary.shape) # (6,)
ary.shape = (2, 3) # 形状改为2行3列
print(ary, ary.shape) 
# [[1 2 3]
#  [4 5 6]] (2, 3)
ary.shape = (6,)

# 数组的运算（矢量化运算）
print(ary * 3)
# [ 3  6  9 12 15 18]
print(ary > 3)
# [False False False  True  True  True]
print(ary + ary)
# [ 2  4  6  8 10 12]
```

**内存中的ndarray对象**

- 元数据（metadata）

  存储目标数组的描述信息，如：`dim`、`count`、`dimensions`、`dtype`、`data`等

- 实际数据

  - 完整的数组数据
  - 将实际数据与元数据分开存放，一方面提高了内存空间的使用效率，另一方面减少对实际数据的访问频率，提高性能。

![image-20230506095647801](image-20230506095647801.png)

ndarray数组对象的特点

- numpy数组是同质数组，即所有元素的数据类型必须相同
- numpy数组的下标从0开始，最后一个元素的下标为数组长度减1



NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。

ndarray 对象是用于存放同类型元素的多维数组。

ndarray 中的每个元素在内存中都有相同存储大小的区域。



ndarray： N维数组。它是一系列同类型数据的集合，以0下标为开始进行集合中元素的索引。用于存放同类型元素的多维数组。

![image-20230425195757900](image-20230425195757900.png)

ndarray 中的每个元素在内存中都有相同存储大小的区域。

ndarray 内部由以下内容组成：

- 一个指向数据（内存或内存映射文件中的一块数据）的指针。
- 数据类型或 dtype，描述在数组中的固定大小值的格子。
- 一个表示数组形状（shape）的元组，表示各维度大小的元组。
- 一个跨度元组（stride），其中的整数指的是为了前进到当前维度下一个元素需要"跨过"的字节数。



ndarray 的内部结构:

![image-20230426140523995](image-20230426140523995.png)

跨度可以是负数，这样会使数组在内存中后向移动，切片中 **obj[::-1]** 或 **obj[:,::-1]** 就是如此。

创建一个 ndarray 只需调用 NumPy 的 array 函数即可：

```python
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
```

| 名称   | 描述                                                      |
| :----- | :-------------------------------------------------------- |
| object | 数组或嵌套的数列                                          |
| dtype  | 数组元素的数据类型，可选                                  |
| copy   | 对象是否需要复制，可选                                    |
| order  | 创建数组的样式，C为行方向，F为列方向，A为任意方向（默认） |
| subok  | 默认返回一个与基类类型一致的数组                          |
| ndmin  | 指定生成数组的最小维度                                    |

```python
import numpy as np 
a = np.array([1,2,3])  
print (a)
# [1 2 3]

# 多于一个维度  
import numpy as np 
a = np.array([[1,  2],  [3,  4]])  
print (a)
# [[1  2] 
#  [3  4]]

# 最小维度  
import numpy as np 
a = np.array([1, 2, 3, 4, 5], ndmin =  2)  
print (a)
# [[1 2 3 4 5]]

# dtype 参数  
import numpy as np 
a = np.array([1,  2,  3], dtype = complex)  
print (a)
# [1.+0.j 2.+0.j 3.+0.j]
```

ndarray 对象由计算机内存的连续一维部分组成，并结合索引模式，将每个元素映射到内存块中的一个位置。内存块以行顺序(C样式)或列顺序(FORTRAN或MatLab风格，即前述的F样式)来保存元素。



### ndarray创建

- np.array

  ```python
  import numpy as np
  a = np.array([1,2,3,4])
  ```

- np.arange(起始值(0), 终止值, 步长)

  ```python
  import numpy as np
  a = np.arange(0, 5, 1)
  print(a) # [0 1 2 3 4]
  
  b = np.arange(0, 10, 2)
  print(b) # [0 2 4 6 8] 
  ```

- np.zeros(数组元素个数， dtype='类型')

  ```python
  import numpy as np
  a = np.zeros(10)
  print(a)
  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
  
  b = np.zeros(10, dtype='int32')
  print(b, b.dtype)
  # [0 0 0 0 0 0 0 0 0 0] int32
  ```

- np.ones(数组元素个数， dtype='类型')

  ```python
  import numpy as np
  a = np.ones(10)
  print(a)
  # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
  
  b = np.ones((2, 3), dtype='float32')
  print(b, b.shape, b.dtype)
  # [[1. 1. 1.]
  #  [1. 1. 1.]] (2, 3) float32
  
  print(np.ones(5) / 5)
  # [0.2 0.2 0.2 0.2 0.2]
  ```

- 扩展：

  - np.zeros_like() & np.ones_like() 生成维度一致的0或1数组

    ```python
    import numpy as np
    
    a = np.arange(0, 12, 2)
    a.shape = (2, 3)
    print(a)
    # [[ 0  2  4]
    #  [ 6  8 10]]
    
    print(np.zeros_like(a))
    # [[0 0 0]
    #  [0 0 0]]
    
    print(np.ones_like(a))
    # [[1 1 1]
    #  [1 1 1]]
    ```

### ndarray对象属性

- 数组的维度：np.ndarray.shape

  ```python
  # 维度基础操作
  import numpy as np
  
  a = np.arange(1, 9)
  print(a, a.shape)
  # [1 2 3 4 5 6 7 8] (8,)
  
  a.shape = (2, 4)
  print(a, a.shape)
  # [[1 2 3 4]
  #  [5 6 7 8]] (2, 4)
  ```

- 元素的类型：np.ndarray.dtype

  ```python
  # 维度基础操作
  import numpy as np
  
  a = np.arange(1, 9)
  print(a, a.dtype)
  # [1 2 3 4 5 6 7 8] int64
  
  # a.dtype = 'float32' # 直接操作的是内存，不是这么改的
  # print(a, a.dtype)
  # [1.4e-45 0.0e+00 2.8e-45 0.0e+00 4.2e-45 0.0e+00 5.6e-45 0.0e+00 7.0e-45
  # 0.0e+00 8.4e-45 0.0e+00 9.8e-45 0.0e+00 1.1e-44 0.0e+00] float32
  b = a.astype('float32') # 得到一个新的ndarray数组对象（a本身没变化）
  print(b, b.dtype)
  # [1. 2. 3. 4. 5. 6. 7. 8.] float32
  ```

- 数组元素的个数：np.ndarray.size

  ```python
  import numpy as np
  
  a = np.arange(0, 12, 2)
  a.shape = (2, 3)
  
  # 观察shape、size和len的区别
  print(a.shape) # (2, 3)
  print(a.size) # 6
  print(len(a)) # 2 可以理解为包含两个一维数组
  ```

- 数组元素索引（下标）

  数组对象[..., 页号, 行号, 列号]

  下标从0开始，到数组len-1结束

  ```python
  import numpy as np
  
  a = np.arange(1, 19)
  a.shape = (3, 2, 3) # (页 行 列) 可以理解为看书，看书的过程就是在扫描一个三维数组
  print(a)
  # [[[ 1  2  3]
  #   [ 4  5  6]]
  
  #  [[ 7  8  9]
  #   [10 11 12]]
  
  #  [[13 14 15]
  #   [16 17 18]]]
  
  print(a[0])
  # [[1 2 3]
  #  [4 5 6]]
  
  print(a[0][1])
  # [4 5 6]
  
  print(a[0][1][0]) # 4
  print(a[0, 1, 0]) # 4
  print(a.shape) # (3, 2, 3) 通过shape属性，获取页数、行数、列数
  
  for i in range(a.shape[0]):
      for j in range(a.shape[1]):
          for k in range(a.shape[2]):
              print(a[i, j, k]) # 打印所有元素，多维数组的扁平迭代器
  ```


### dtype：numpy内部基本数据类型

| 类型名     | 类型表示符                          |
| ---------- | ----------------------------------- |
| 布尔型     | bool_                               |
| 有符号整型 | int(-128~127)/int16/int32/int64     |
| 无符号整型 | uint8(0~255)/uint16/uint32/uint64   |
| 浮点型     | float16/float32/float64             |
| 复数型     | complex64/complex128                |
| 字串型     | str_，每个字符用32位Unicode编码表示 |

#### **自定义复合类型**

```python
# 自定义复复合类型
import numpy as np

data = [
    ('xs', [80, 90, 88], 15),
    ('zs', [84, 93, 48], 15),
    ('os', [80, 60, 68], 16)
]

# a = np.array(data)
# print(a) # 直接将符合数据类型，作为参数的话，会报错不识别

# 第一种设置dtype的方式
a = np.array(data, dtype='U2, 3int32, int32') # U2表示：Unicode字符，出现两个（一个Unicode字符占32位）
print('a===========')
print(a)
print(a[1][1]) # 当字段过多时，不可能一个一个数

# 第二种设置dtype的方式
b = np.array(data, dtype=[
    ('name', 'str_', 2),
    ('scores', 'int32', 3),
    ('ages', 'int32', 1)
])
print('b===========')
print(b)
print(b[1]['scores'])

# 第三种设置dtype的方式，比较常用，简洁
c = np.array(data, {
    'names': ['name', 'scores', 'ages'],
    'formats': ['U3', '3int32', 'int32']
})
print('c===========')
print(c)
print(c[0]['name'])
print(c.itemsize) # 每一个元素，占用的内存空间大小

# 第四种设置dtype的方式，少见
d = np.array(data, dtype={
    'name': ('U3', 0), # 后面的数字，表示字节偏移量
    'scores': ('3int32', 16),
    'ages': ('int32', 28)
})
print('d===========')
print(d[0]['scores'])

# 第五种设置dtype的方式，和大小端字节序有关，不用管
e = np.array([0x1234, 0x5576], dtype=(
    'U2',
    {
        'lowc': ('u1', 0),
        'highc': ('u1', 1)
    }
))
print('e===========')
print(e['lowc'][0])
print(e['highc'][0])
```

#### 日期数据类型

```python
import numpy as np
dates = [
    '2021-01-01',
    '2022-02',
    '2023',
    '2024-04-04 04:04:00'
]

dates = np.array(dates)
print(dates) # ['2021-01-01' '2022-02' '2023' '2024-04-04 04:04:00'] # numpy中时横杠，不认斜杠
print(dates.dtype) # <U19
# 转换类型
dates = dates.astype('M8[D]') # D代表天,s代表秒
print(dates) # ['2021-01-01' '2022-02-01' '2023-01-01' '2024-04-04']
print(dates.dtype) # datetime64[D]
print(dates[2] - dates[1]) # 334 days
```

#### 类型字符码

数据类型简写

| 类型              | 字符码                              |
| ----------------- | ----------------------------------- |
| np.bool           | ?                                   |
| np.int8/16/32/64  | i1/i2/i4/i8                         |
| np.uint8/16/32/64 | u1/u2/u4/u8                         |
| np.float/16/32/64 | f2/f4/f8                            |
| np.complex64/128  | c8/ c16                             |
| np.str_           | U<字符数>                           |
| np.datetime64     | M8[Y] M8[M] M8[D] M8[h] M8[m] M8[s] |

字节序前缀， 用于多字节整数和字符串

`</>/[=]`分别表示小端/大端/硬件字节序

类型字符码格式

`<字节序前缀><维度><类型><字节数或字符数>`

| 格式     | 释义                                                         |
| -------- | ------------------------------------------------------------ |
| 3i4      | 大端字节序，3个元素的的一维数组，每个元素都是整型，每个整型元素占4个字节 |
| <(2,3)u8 | 小端字节序，6个元素2行3列的二维数组，每个元素都是无符号整型，每个无符号整型元素占8个字节 |
| U7       | 包含7个字符的Unicode字符串，每个字符占4个字节，采用默认字节序 |



### shape：ndarray数组对象的维度操作



#### 视图变维

数据共享：reshape()与revel()

```python

```



## pandas

>  工具类的api

```bash
 pip3 install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**样例**

```python
import pandas as pd

mydataset = {
    'site': ["Google", "Runoob", "Wiki"],
    'number': [1, 2, 3]
}

myvar = pd.DataFrame(mydataset)
print(myvar)
```

![image-20230502132247990](image-20230502132247990.png)



### pandas介绍

python data analysis library

pandas是基于numpy的一种**工具**，该工具是为了解决数据分析任务而创建的。

pandas纳入了大量库和一些标准的数据模型，提供了高效操作**大型结构化数据集（二维表）**所需的工具。非结构化数据pandas不搞，如图片、音频等。

### pandas核心数据结构

> 数据结构是计算机存储、组织数据的方式。通常情况下，精心选择的数据结构可以带来更高的运行或者存储效率。数据结构往往同高效的检索算法和索引技术有关。

#### 数据结构 - Series

Pandas Series 类似表格中的一个列（column），类似于一维数组，只是index可以自己改动。类似于定长的有序字典，有index和value。可以保存任何数据类型。

Series提供了更多的维度，让我们可以更方便的操作一维数组（可以自定义索引标签名称，代码易读）



Series 由索引（index）和列组成，函数如下：

```python
pandas.Series( data, index, dtype, name, copy)
```

参数说明：

- **data**：一组数据(ndarray 类型)。
- **index**：数据索引标签，如果不指定，默认从 0 开始。
- **dtype**：数据类型，默认会自己判断。
- **name**：设置名称。
- **copy**：拷贝数据，默认为 False。

创建一个简单的 Series 实例：

```python
import pandas as pd

a = [1, 2, 3]

myvar = pd.Series(a)

print(myvar)
```

![img](FD659034-1715-4020-A6BF-400FAC9CE849.jpg)

从上图可知，如果没有指定索引，索引值就从 0 开始，我们可以根据索引值读取数据：

```python
import pandas as pd

a = [1, 2, 3]

myvar = pd.Series(a)

print(myvar[1]) # 2
```

我们可以指定索引值，如下实例：

```python
import pandas as pd

a = ["Google", "Runoob", "Wiki"]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
```

![img](32B49FA4-ED68-446A-9EBF-C52FCB6D0CD6.jpg)

根据索引值读取数据:

```python
import pandas as pd

a = ["Google", "Runoob", "Wiki"]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar["y"]) # Runoob
```

我们也可以使用 key/value 对象，类似字典来创建 Series：

```python
import pandas as pd

sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites)

print(myvar)
```

![img](C01F8A55-5D06-4FAD-BE34-A569A8B05E2C.jpg)

从上图可知，字典的 key 变成了索引值。

如果我们只需要字典中的一部分数据，只需要指定需要数据的索引即可，如下实例：

```python
import pandas as pd

sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites, index = [1, 2])

print(myvar)
```

![img](6CC2CFBA-3CC5-459D-8FE0-D89C1EE1AEB9.jpg)

设置 Series 名称参数：

```python
import pandas as pd

sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites, index = [1, 2], name="RUNOOB-Series-TEST" )

print(myvar)
```

![img](1FB6D419-06D7-4229-9148-1F4E79DE6ACF.jpg)



完整样例及拓展

```python
import pandas as pd

a = [1, 2, 3]

myvar = pd.Series(a)
print(myvar)
print(myvar[2])
print('\n')

myvar = pd.Series(a, index = ['x', 'y', 'z'])
print(myvar)
print(myvar['z'])
print('\n')

b = {
    2: 'Google',
    3: 'Microsoft',
    4: 'IBM',
    'name': 'sai'
}
myvar1 = pd.Series(b)
print(myvar1)
print(myvar1[4], myvar1['name'])
print('\n')

myvar1 = pd.Series(b, index=[2, 'name'], name = "custom_name")
print(myvar1)

```

![image-20230505072423716](image-20230505072423716.png)

##### 创建Series

```python
import numpy as np
import pandas as pd

# 创建一个空的序列
s = pd.Series()
print(s)
# Series([], dtype: object) <class 'pandas.core.series.Series'> object

# 从ndarray中创建序列
data = np.array(['a', 'b', 'c', 'd', 'e'])
s1 = pd.Series(data)
print(s1)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64
s1 = pd.Series(data, index = [100, 101, 102, 103, 104])
print(s1)
# 100    a
# 101    b
# 102    c
# 103    d
# 104    e
# dtype: object

# 从字典创建序列
data1 = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3
}
 
s2 = pd.Series(data1)
print(s2)
# a    0
# b    1
# c    2
# d    3
# dtype: int64

# 从标量创建一个系列
s3 = pd.Series(5, index = [0, 1, 2, 3])
print(s3)
# 0    5
# 1    5
# 2    5
# 3    5
# dtype: int64
```

##### 访问Series

```python
import pandas as pd
s = pd.Series([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e'])
# 使用索引下标（不易读）
print(s[0]) # 1

print(s[:3])
# a    1
# b    2
# c    3
# dtype: int64

print(s[-3:])
# c    3
# d    4
# e    5
# dtype: int64


# 使用标签检索数据
print(s['a']) # 1

print(s[['a', 'c', 'd']])
# a    1
# c    3
# d    4
# dtype: int64
```

##### 日期处理

pd.to_datetime()

```python
import pandas as pd
# 以日为频率
datelist = pd.date_range('2019/08/21', periods = 5)
print(datelist)
# DatetimeIndex(['2019-08-21', '2019-08-22', '2019-08-23', '2019-08-24',
#                '2019-08-25'],
#               dtype='datetime64[ns]', freq='D')

# 以月为频率
datelist = pd.date_range('2019/08/21', periods = 5, freq = 'M')
print(datelist)
# DatetimeIndex(['2019-08-31', '2019-09-30', '2019-10-31', '2019-11-30',
#                '2019-12-31'],
#               dtype='datetime64[ns]', freq='M')

# 构建某个区间的时间序列
# start = pd.datetime(2017, 11, 1)
# end = pd.datetime(2017, 11, 5)
# dates = pd.date_range(start, end)
# print(dates)

# 生成时间序列（工作日时间序列）
dates = pd.bdate_range('2023/5/4', periods=7) # 6、7是周六日，自动跳过
print(dates)
```

Series.dt提供了很多日期相关操作，使用时可以查阅相关文档

##### DateTimeIndex

通过指定周期和频率，使用date_range()函数就可以创建日期序列。默认情况下，范围的频率是天



#### 数据结构 - DataFrame

DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。

![img](pandas-DataStructure.png)

![img](df-dp.png)

可以理解为一个二维数组，索引有两个维度，可更改。DataFrame具有以下特点：

- 潜在的列是不同的类型
- 大小可变
- 标记轴（行和列）
- 可以对行和列执行算术运算

DataFrame 构造方法如下：

```
pandas.DataFrame( data, index, columns, dtype, copy)
```

参数说明：

- **data**：一组数据(ndarray、series, map, lists, dict 等类型)。
- **index**：索引值，或者可以称为行标签。
- **columns**：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
- **dtype**：数据类型。
- **copy**：拷贝数据，默认为 False。

Pandas DataFrame 是一个二维的数组结构，类似二维数组。

```python
import pandas as pd

data = [['Google',10],['Runoob',12],['Wiki',13]]

df = pd.DataFrame(data,columns=['Site','Age'])

print(df)
```

以下实例**使用 ndarrays 创建**，ndarray 的长度必须相同， 如果传递了 index，则索引的长度应等于数组的长度。如果没有传递索引，则默认情况下，索引将是range(n)，其中n是数组长度。

```python
import pandas as pd

data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}

df = pd.DataFrame(data)

print (df)
```



从以上输出结果可以知道， DataFrame 数据类型类似一个表格，包含 rows（行） 和 columns（列）：



还可以**使用字典（key/value）**，其中字典的 key 为列名:

```python
import pandas as pd

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

df = pd.DataFrame(data)

print (df)
```



没有对应的部分数据为 **NaN**。

Pandas 可以使用 **loc** 属性返回指定行的数据，如果没有设置索引，第一行索引为 **0**，第二行索引为 **1**，以此类推：

```
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])
```



**注意：**返回结果其实就是一个 Pandas Series 数据。

也可以返回多行数据，使用 **[[ ... ]]** 格式，**...** 为各行的索引，以逗号隔开：

```
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

# 返回第一行和第二行
print(df.loc[[0, 1]])
```



**注意：**返回结果其实就是一个 Pandas DataFrame 数据。

我们可以指定索引值，如下实例：

```
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)
```

> ```
>    calories  duration
> day1       420        50
> day2       380        40
> day3       390        45
> ```

Pandas 可以使用 **loc** 属性返回指定索引对应到某一行：

```
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# 指定索引
print(df.loc["day2"])
```

> ```
> calories    380
> duration     40
> Name: day2, dtype: int64
> ```

##### 创建DataFrame

```python
import pandas as pd

# 创建一个空的DataFrame
df = pd.DataFrame()
print(df)
# Empty DataFrame
# Columns: []
# Index: []

# 从列表创建DataFrame
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df)
#    0
# 0  1
# 1  2
# 2  3
# 3  4
# 4  5
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
#      Name  Age
# 0    Alex   10
# 1     Bob   12
# 2  Clarke   13
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
#    a   b     c
# 0  1   2   NaN
# 1  5  10  20.0

# 从字典来创建DataFrame
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 28, 43]}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4'])
print(df)
#      Name  Age
# s1    Tom   28
# s2   Jack   34
# s3  Steve   28
# s4  Ricky   43
data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data)
print(df)
#    one  two
# a  1.0    1
# b  2.0    2
# c  3.0    3
# d  NaN    4
```

##### 操作DataFrame

- 列访问

  DataFrame的单列数据为一个Series。根据DataFrame的定义可以知晓，DataFrame是一个带有标签的二维数组，每个标签相当每一列的列名

  ```python
  import pandas as pd
  
  data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
  df = pd.DataFrame(data)
  print(df['one'])
  # a    1.0
  # b    2.0
  # c    3.0
  # d    NaN
  # Name: one, dtype: float64
  print(df[['one', 'two']])
  #    one  two
  # a  1.0    1
  # b  2.0    2
  # c  3.0    3
  # d  NaN    4
  ```

- 列添加

  DataFrame添加一列的方法非常简单，只需要新建一个列索引。并对该索引下的数据进行赋值操作即可

  ```python
  import pandas as pd
  
  data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 28, 43]}
  df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4'])
  # df['Score'] = pd.Series([90, 80, 70, 60], index=['s1', 's2', 's3', 's4'])
  df['Score'] = pd.Series([90, 80, 70, 60], index=df.index)
  print(df)
  #      Name  Age  Score
  # s1    Tom   28     90
  # s2   Jack   34     80
  # s3  Steve   28     70
  # s4  Ricky   43     60
  ```

- 列删除

  删除某列数据需要用到pandas提供的方法pop

  注意，该方法影响原数据集

  ```python
  import pandas as pd
  
  data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
  df = pd.DataFrame(data)
  print(df)
  #    one  two  three
  # a  1.0    1   10.0
  # b  2.0    2   20.0
  # c  3.0    3   30.0
  # d  NaN    4    NaN
  
  # 删除一列
  del(df['one'])
  print(df)
  #    two  three
  # a    1   10.0
  # b    2   20.0
  # c    3   30.0
  # d    4    NaN
  
  # 调用pop方法删除一列
  df.pop('two')
  print(df)
  #    three
  # a   10.0
  # b   20.0
  # c   30.0
  # d    NaN
  ```

- 行访问

  如果只是需要访问DataFrame某几行数据，实现方式则采用数组的选取方式（切片访问），使用`:`即可

  ```python
  import pandas as pd
  
  data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
  df = pd.DataFrame(data)
  print(df[2:4])
  #    one  two  three
  # c  3.0    3   30.0
  # d  NaN    4    NaN
  ```

  loc方法是针对DataFrame索引名称的切片方法。loc方法使用方法如下

  ```python
  import pandas as pd
  
  data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
  df = pd.DataFrame(data)
  print(df)
  #    one  two  three
  # a  1.0    1   10.0
  # b  2.0    2   20.0
  # c  3.0    3   30.0
  # d  NaN    4    NaN
  print(df.loc['b'])
  # one       2.0
  # two       2.0
  # three    20.0
  # Name: b, dtype: float64
  print(df.loc[['a', 'c']])
  #    one  two  three
  # a  1.0    1   10.0
  # c  3.0    3   30.0
  ```

  iloc和loc区别是iloc接受的必须是行索引的位置。

  ```python
  import pandas as pd
  
  data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
  df = pd.DataFrame(data)
  print(df)
  #    one  two  three
  # a  1.0    1   10.0
  # b  2.0    2   20.0
  # c  3.0    3   30.0
  # d  NaN    4    NaN
  print(df.iloc[2]) 
  # one       3.0
  # two       3.0
  # three    30.0
  # Name: c, dtype: float64
  
  print(df.iloc[[2, 3]]) # 只支持行位置索引
  #    one  two  three
  # c  3.0    3   30.0
  # d  NaN    4    NaN
  
  print(df.iloc[1, 1]) # 少写一个方括号，返回的是具体的标量：2
  ```

  在Pandas中，`iloc`是一个用于通过整数位置进行数据选择和切片的方法。它允许你通过指定行和列的位置来访问和操作DataFrame或Series中的数据。

  `iloc`的语法如下：

  ```python
  
  df.iloc[row_indexer, column_indexer]
  ```

  其中，`row_indexer`和`column_indexer`是用于指定行和列位置的整数、整数列表、切片对象或布尔数组。

  下面是一些常见的用法和示例：

  1. 选择特定行和列：

  ```python
  # 选择第1行和第2列的数据
  value = df.iloc[0, 1]
  
  # 选择前3行和所有列的数据
  subset = df.iloc[:3, :]
  
  # 选择第1列的数据
  column = df.iloc[:, 0]
  ```

  1. 使用整数列表选择多行或多列：

  ```python
  # 选择第1、3和5行的数据
  rows = df.iloc[[0, 2, 4], :]
  
  # 选择第0、2和4列的数据
  columns = df.iloc[:, [0, 2, 4]]
  
  # 选择第1、2和4行，第0和3列的数据
  subset = df.iloc[[1, 2, 4], [0, 3]]
  ```

  1. 使用切片对象进行切片选择：

  ```python
  # 选择前5行的数据
  subset = df.iloc[:5, :]
  
  # 选择第3到第7行的数据
  subset = df.iloc[2:7, :]
  
  # 选择第2到第5列的数据
  subset = df.iloc[:, 1:5]
  ```

  1. 使用布尔数组进行条件选择：

  ```python
  # 选择满足条件的行
  subset = df.iloc[df['column'] > 5, :]
  
  # 选择满足条件的列
  subset = df.iloc[:, df.columns.str.contains('keyword')]
  ```

  通过使用`iloc`方法，你可以通过整数位置灵活地选择和操作DataFrame或Series中的数据，无论是选择特定的行和列，还是进行切片选择。

- 行添加

  方法一：

  ```python
  import pandas as pd
  
  # 创建一个空的DataFrame
  df = pd.DataFrame(columns=['Column1', 'Column2', 'Column3'])
  
  # 创建新行的数据
  new_row = {'Column1': 1, 'Column2': 2, 'Column3': 3}
  
  # 将新行添加到DataFrame
  df = df.append(new_row, ignore_index=True)
  
  # 输出DataFrame
  print(df)
  
  ```

  

  方法二：

  ```python
  import pandas as pd
  
  df = pd.DataFrame([
      ['zs', 12],
      ['ls', 4],
  ], columns=['Name', 'Age'])
  
  df2 = pd.DataFrame([
      ['ww', 16],
      ['zl', 8]
  ], columns=['Name', 'Age'])
  
  # df = df.append(df2) 新版本弃用
  df = pd.concat([df, df2], ignore_index=True)
  
  print(df)
  #   Name  Age
  # 0   zs   12
  # 1   ls    4
  # 2   ww   16
  # 3   zl    8
  ```

- 行删除

  使用索引标签从DataFrame中删除或删除行。如果标签重复，则会删除多行

  ```python
  import pandas as pd
  
  df = pd.DataFrame([
      ['zs', 12],
      ['ls', 4],
  ], columns=['Name', 'Age'])
  
  df2 = pd.DataFrame([
      ['ww', 16],
      ['zl', 8]
  ], columns=['Name', 'Age'])
  
  df = pd.concat([df, df2], ignore_index=True)
  
  # 删除index为0的行
  df = df.drop(0)
  print(df)
  #   Name  Age
  # 1   ls    4
  # 2   ww   16
  # 3   zl    8
  ```

- 更改DataFrame中的数据，原理是将这部分数据提取出来，重新赋值为新的数据

  ```python
  import pandas as pd
  
  df = pd.DataFrame([
      ['zs', 12],
      ['ls', 4],
  ], columns=['Name', 'Age'])
  
  df2 = pd.DataFrame([
      ['ww', 16],
      ['zl', 8]
  ], columns=['Name', 'Age'])
  
  df = pd.concat([df, df2], ignore_index=True)
  
  df['Name'][0] = 'Tom'
  print(df)
  #   Name  Age
  # 0  Tom   12
  # 1   ls    4
  # 2   ww   16
  # 3   zl    8
  ```

- 常用属性或方法

  | 属性或方法 | 描述                             |
  | ---------- | -------------------------------- |
  | axes       | 返回行/列 标签（index）列表      |
  | dtype      | 返回对象的数据类型               |
  | empty      | 如果序列为空，则返回True         |
  | ndim       | 返回底层数据的维度， 默认定义：1 |
  | size       | 返回基础数据中的元素数           |
  | values     | 将序列作为ndarray返回            |
  | head()     | 返回前n行                        |
  | tail()     | 返回最后n行                      |

  ```python
  import pandas as pd
  
  df = pd.DataFrame([
      ['zs', 12],
      ['ls', 4],
  ], columns=['Name', 'Age'])
  
  df2 = pd.DataFrame([
      ['ww', 16],
      ['zl', 8]
  ], columns=['Name', 'Age'])
  
  df = pd.concat([df, df2], ignore_index=True)
  print(df)
  #   Name  Age
  # 0   zs   12
  # 1   ls    4
  # 2   ww   16
  # 3   zl    8
  print(df.axes) # [RangeIndex(start=0, stop=4, step=1), Index(['Name', 'Age'], dtype='object')]
  print(df.empty) # False
  print(df.ndim) # 2
  print(df.values)
  # [['zs' 12]
  #  ['ls' 4]
  #  ['ww' 16]
  #  ['zl' 8]]
  ```

### pandas核心

#### 描述性统计

数值型的描述性统计，主要包括了计算数值型数据的完整情况、最小值、均值、中位数、最大值、四分位数、极差、标准差、方差、协方差等

在Numpy库中，一些常用的统计学函数也可用与对数据框(DataFrame)进行描述性统计

```python
np.min 最小值
np.max 最大值
np.mean 均值
np.ptp 极差
np.median 中位数
np.std 标准差
np.var 方差
np.cov 协方差
```

```python
import pandas as pd
import numpy as np

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vim', 'Steve', 'Minsu', 'Jack', 'Lee', 'David', 'Betina']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40 ,30]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80])
}
df = pd.DataFrame(data)
print(df)
#      Name  Age  Rating
# 0     Tom   25    4.23
# 1   James   26    3.24
# 2   Ricky   25    3.98
# 3     Vim   23    2.56
# 4   Steve   30    3.20
# 5   Minsu   29    4.60
# 6    Jack   23    3.80
# 7     Lee   34    3.78
# 8   David   40    2.98
# 9  Betina   30    4.80
# 描述性统计函数
print(df.sum())
# Name      TomJamesRickyVimSteveMinsuJackLeeDavidBetina
# Age                                                285
# Rating                                           37.17
# dtype: object

# print(df.sum(1)) # 按行计算

print(df['Age'].mean()) # 28.5
# print(df.mean(1))

print(df.max())
# Name      Vim
# Age        40
# Rating    4.8
# dtype: object
```

pandas提供了统计相关函数

| 函数      | 含义                 |
| --------- | -------------------- |
| count()   | 非空观测数量（计数） |
| sum()     | 所有值之和           |
| mean()    | 所有值的平均值       |
| median()  | 所有值的中位数       |
| std()     | 值的标准偏差         |
| min()     | 所有值中的最小值     |
| max()     | 所有值中的最大值     |
| abs()     | 绝对值               |
| prod()    | 数组元素的乘积       |
| cumsum()  | 累计总和             |
| cumprod() | 累计乘积             |

```python
print(df.count())
# Name      10
# Age       10
# Rating    10
# dtype: int64
```

pandas还提供了一个方法叫做descrbibe，能够一次性得出DataFrame所有数值型特征的非空值数目、均值、标准差等

```python
import pandas as pd
import numpy as np

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vim', 'Steve', 'Minsu', 'Jack', 'Lee', 'David', 'Betina']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40 ,30]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80])
}
df = pd.DataFrame(data)

print(df.describe())
#              Age     Rating
# count  10.000000  10.000000
# mean   28.500000   3.717000
# std     5.359312   0.720525
# min    23.000000   2.560000
# 25%    25.000000   3.210000
# 50%    27.500000   3.790000
# 75%    30.000000   4.167500
# max    40.000000   4.800000
print(df.describe(include=['object']))
#        Name
# count    10
# unique   10
# top     Tom
# freq      1
print(df.describe(include=['number']))
#              Age     Rating
# count  10.000000  10.000000
# mean   28.500000   3.717000
# std     5.359312   0.720525
# min    23.000000   2.560000
# 25%    25.000000   3.210000
# 50%    27.500000   3.790000
# 75%    30.000000   4.167500
# max    40.000000   4.800000
```



#### 排序

pandas有两种排序，分别是按标签与按实际值排序

```python
import pandas as pd 
import numpy as np

unsorted_df = pd.DataFrame(np.random.rand(10, 2), index=[1,4,6,2,3,5,9,8,0,7], columns=['col2', 'col1'])
print(unsorted_df) # 随机二维数组
```

##### 按行标签排序

使用`sort_index()`方法，通过传递`axis`参数和排序顺序，可以对`DataFrame`进行排序。

默认情况下，按照升序对行标签进行排序

```python
import pandas as pd 
import numpy as np

unsorted_df = pd.DataFrame(np.random.rand(10, 2), index=[1,4,6,2,3,5,9,8,0,7], columns=['col2', 'col1'])
print(unsorted_df)
#        col2      col1
# 1  0.164731  0.888115
# 4  0.252891  0.931582
# 6  0.691138  0.080611
# 2  0.070959  0.606531
# 3  0.196151  0.616428
# 5  0.605811  0.253877
# 9  0.969352  0.263449
# 8  0.082737  0.747610
# 0  0.380823  0.177485
# 7  0.817889  0.109617

# 按照行标签进行排序
sorted_df = unsorted_df.sort_index()
print(sorted_df)
#        col2      col1
# 0  0.380823  0.177485
# 1  0.164731  0.888115
# 2  0.070959  0.606531
# 3  0.196151  0.616428
# 4  0.252891  0.931582
# 5  0.605811  0.253877
# 6  0.691138  0.080611
# 7  0.817889  0.109617
# 8  0.082737  0.747610
# 9  0.969352  0.263449

# 按照列标签进行排序
print(unsorted_df.sort_index(axis=1))
#        col1      col2
# 1  0.888115  0.164731
# 4  0.931582  0.252891
# 6  0.080611  0.691138
# 2  0.606531  0.070959
# 3  0.616428  0.196151
# 5  0.253877  0.605811
# 9  0.263449  0.969352
# 8  0.747610  0.082737
# 0  0.177485  0.380823
# 7  0.109617  0.817889

# 控制排序顺序
print(unsorted_df.sort_index(ascending=False)) # 默认为升序，False设置成降序
#        col2      col1
# 9  0.969352  0.263449
# 8  0.082737  0.747610
# 7  0.817889  0.109617
# 6  0.691138  0.080611
# 5  0.605811  0.253877
# 4  0.252891  0.931582
# 3  0.196151  0.616428
# 2  0.070959  0.606531
# 1  0.164731  0.888115
# 0  0.380823  0.177485
```

##### 按某列值排序

像索引排序一样，`sort_values`是按值排序的方法。

它接受一个by参数，它将使用要与其排序值的DataFrame的列名称。

```python
import pandas as pd
import numpy as np

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vim', 'Steve', 'Minsu', 'Jack', 'Lee', 'David', 'Betina']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40 ,30]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80])
}
unsorted_df = pd.DataFrame(data)
print(unsorted_df)
#      Name  Age  Rating
# 0     Tom   25    4.23
# 1   James   26    3.24
# 2   Ricky   25    3.98
# 3     Vim   23    2.56
# 4   Steve   30    3.20
# 5   Minsu   29    4.60
# 6    Jack   23    3.80
# 7     Lee   34    3.78
# 8   David   40    2.98
# 9  Betina   30    4.80
# 按年龄进行排序
sorted_age = unsorted_df.sort_values(by='Age')
print(sorted_age)
#      Name  Age  Rating
# 3     Vim   23    2.56
# 6    Jack   23    3.80
# 0     Tom   25    4.23
# 2   Ricky   25    3.98
# 1   James   26    3.24
# 5   Minsu   29    4.60
# 4   Steve   30    3.20
# 9  Betina   30    4.80
# 7     Lee   34    3.78
# 8   David   40    2.98

sorted_rating = unsorted_df.sort_values(by='Rating', ascending=False)
print(sorted_rating)
#      Name  Age  Rating
# 9  Betina   30    4.80
# 5   Minsu   29    4.60
# 0     Tom   25    4.23
# 2   Ricky   25    3.98
# 6    Jack   23    3.80
# 7     Lee   34    3.78
# 1   James   26    3.24
# 4   Steve   30    3.20
# 8   David   40    2.98
# 3     Vim   23    2.56

# 先按年龄排序，再按rate排序
# 评分降序
sort_age_rating = unsorted_df.sort_values(by=['Age', 'Rating'], ascending=[True, False])
print(sort_age_rating)
#      Name  Age  Rating
# 6    Jack   23    3.80
# 3     Vim   23    2.56
# 0     Tom   25    4.23
# 2   Ricky   25    3.98
# 1   James   26    3.24
# 5   Minsu   29    4.60
# 9  Betina   30    4.80
# 4   Steve   30    3.20
# 7     Lee   34    3.78
# 8   David   40    2.98
```



#### 分组

在许多情况下，我们将数据分成多个集合，并在每个子集上应用一些函数。

在应用函数中，可以执行以下操作：

- 聚合：计算汇总统计
- 转换：执行一些特定于组的操作
- 过滤：在某些情况下丢弃数据

```python
import pandas as pd

ipl_data = {
    'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings', 'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1,2,2,4,4,5,1,1,2,4,1,2],
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points': [876,789,863,673,741,812,756,788,694,701,804,690]
}

df = pd.DataFrame(ipl_data)
print(df)
#       Team  Rank  Year  Points
# 0   Riders     1  2014     876
# 1   Riders     2  2015     789
# 2   Devils     2  2014     863
# 3   Devils     4  2015     673
# 4    Kings     4  2014     741
# 5    kings     5  2015     812
# 6    Kings     1  2016     756
# 7    Kings     1  2017     788
# 8   Riders     2  2016     694
# 9   Royals     4  2014     701
# 10  Royals     1  2015     804
# 11  Riders     2  2017     690
```

##### 将数据拆分成组

```python
# 按照年份Year字段分组
print(df.groupby('Year'))
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fcb71094e20>
# 查看分组结果
print(df.groupby('Year').groups)
# {2014: [0, 2, 4, 9], 2015: [1, 3, 5, 10], 2016: [6, 8], 2017: [7, 11]}
```

##### 迭代遍历分组

groupby返回可迭代对象，可以使用for循环遍历（不常用）：

```python
grouped = df.groupby('Year')
for year, group in grouped:
    print(year)
    print(group)
# 2014
#      Team  Rank  Year  Points
# 0  Riders     1  2014     876
# 2  Devils     2  2014     863
# 4   Kings     4  2014     741
# 9  Royals     4  2014     701
# 2015
#       Team  Rank  Year  Points
# 1   Riders     2  2015     789
# 3   Devils     4  2015     673
# 5    kings     5  2015     812
# 10  Royals     1  2015     804
# 2016
#      Team  Rank  Year  Points
# 6   Kings     1  2016     756
# 8  Riders     2  2016     694
# 2017
#       Team  Rank  Year  Points
# 7    Kings     1  2017     788
# 11  Riders     2  2017     690
```

##### 获得一个分组细节

```python
grouped = df.groupby('Year')
print(grouped.get_group(2014))
#      Team  Rank  Year  Points
# 0  Riders     1  2014     876
# 2  Devils     2  2014     863
# 4   Kings     4  2014     741
# 9  Royals     4  2014     701
```

##### 分组聚合

聚合函数为每个组返回聚合值。当创建了分组(group by)对象，就可以对每个分组数据执行求和、求标准差等操作

```python
grouped = df.groupby('Year')
# 聚合每一年的平均得分
print(grouped['Points'].agg(np.mean))
# Year
# 2014    795.25
# 2015    769.50
# 2016    725.00
# 2017    739.00
# Name: Points, dtype: float64

# 聚合每一年的分数之和、平均分、标准差
agg = grouped['Points'].agg([np.sum, np.mean, np.std])
print(agg)
#        sum    mean        std
# Year                         
# 2014  3181  795.25  87.439026
# 2015  3078  769.50  65.035888
# 2016  1450  725.00  43.840620
# 2017  1478  739.00  69.296465
```

####  数据表关联操作

pandas具有功能全面的高性能内存中连接操作，与SQL等关系数据库非常相似。

pandas提供了一个单独的merge()函数，作为DataFrame对象之间所有标准数据库连接操作的入口。

```python
import pandas as pd

left = pd.DataFrame({
    'students_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'students_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung', 'Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'class_id': [1,1,1,2,2,2,3,3,3,4]
})

right = pd.DataFrame({
    'class_id': [1,2,3,5],
    'class_name': ['ClassA', 'ClassB', 'ClassC', 'ClassE']
})

print(left)
#    students_id students_name  class_id
# 0            1          Alex         1
# 1            2           Amy         1
# 2            3         Allen         1
# 3            4         Alice         2
# 4            5        Ayoung         2
# 5            6         Billy         2
# 6            7         Brian         3
# 7            8          Bran         3
# 8            9         Bryce         3
# 9           10         Betty         4
print(right)
#    class_id class_name
# 0         1     ClassA
# 1         2     ClassB
# 2         3     ClassC
# 3         5     ClassE

# 合并两个DataFrame，默认是内连接
rs = pd.merge(left, right)
print(rs)
#    students_id students_name  class_id class_name
# 0            1          Alex         1     ClassA
# 1            2           Amy         1     ClassA
# 2            3         Allen         1     ClassA
# 3            4         Alice         2     ClassB
# 4            5        Ayoung         2     ClassB
# 5            6         Billy         2     ClassB
# 6            7         Brian         3     ClassC
# 7            8          Bran         3     ClassC
# 8            9         Bryce         3     ClassC
```

使用how参数合并DataFrame：

```python
# 合并两个DataFrame（左连接）
rs = pd.merge(left, right, how='left')
print(rs)
#    students_id students_name  class_id class_name
# 0            1          Alex         1     ClassA
# 1            2           Amy         1     ClassA
# 2            3         Allen         1     ClassA
# 3            4         Alice         2     ClassB
# 4            5        Ayoung         2     ClassB
# 5            6         Billy         2     ClassB
# 6            7         Brian         3     ClassC
# 7            8          Bran         3     ClassC
# 8            9         Bryce         3     ClassC
# 9           10         Betty         4        NaN
```

其他合并方法同数据库相同：

| 合并方法 | SQL等效          | 描述             |
| -------- | ---------------- | ---------------- |
| left     | left outer join  | 使用左侧对象的键 |
| right    | right outer join | 使用右侧对象的键 |
| outer    | full outer join  | 使用键的联合     |
| inner    | inner join       | 使用键的交集     |

如果两个表中，有字段相同，需要指定按照哪个字段去做关联

```python
rs = pd.merge(left, right, on='subject_id', how='right')
```

#### 透视表与交叉表

透视表（pivot table）是各种电子表格程序和其他数据分析软件中一种常见的数据汇总工具。它根据一个或多个键对数据进行分组聚合，并根据每个分组进行数据汇总。

```python
```







#### 透视表



### 数据分析实践

#### 电影评分数据分析

需求

1.读取数据，从用户表读取用户信息、同样方法，导入电影评分表、电影数据表

2.合并数据表

3.对数据初步描述分析

4.查看每一部电影不同性别的平均评分，并计算分歧插值，之后排序

5.算出每部电影平均的分并对其进行排序

6.查看评分次数多的电影并进行排序

7.过滤评分条目数不足250条的电影

8.评分最高的十部电影

8.查看不同年龄的分布情况并且采用直方图进行可视化

### pandas处理CSV 文件

CSV（Comma-Separated Values，逗号分隔值，有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）。

CSV 是一种通用的、相对简单的文件格式，被用户、商业和科学广泛应用。

Pandas 可以很方便的处理 CSV 文件，本文以 [nba.csv](https://static.runoob.com/download/nba.csv) 为例，你可以[下载 nba.csv](https://static.runoob.com/download/nba.csv) 或[打开 nba.csv](https://static.runoob.com/download/nba.csv.txt) 查看。

```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.to_string())
```

**to_string()** 用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 **...** 代替。

![image-20230502135923494](image-20230502135923494.png)



我们也可以使用 **to_csv()** 方法将 DataFrame 存储为 csv 文件：

```python
import pandas as pd
   
# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
   
# 字典
dict = {'name': nme, 'site': st, 'age': ag}
     
df = pd.DataFrame(dict)
 
# 保存 dataframe
df.to_csv('site.csv')
```



#### head()

**head( n )** 方法用于读取前面的 n 行，如果不填参数 n ，默认返回 5 行。

 读取前面 10 行

```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.head(10))
```

#### tail()

**tail( n )** 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 NaN。

```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.tail())
```

#### info()

info() 方法返回表格的一些基本信息：

```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.info())
```

> ```
> <class 'pandas.core.frame.DataFrame'>
> RangeIndex: 458 entries, 0 to 457          # 行数，458 行，第一行编号为 0
> Data columns (total 9 columns):            # 列数，9列
>  #   Column    Non-Null Count  Dtype       # 各列的数据类型
> ---  ------    --------------  -----  
>  0   Name      457 non-null    object 
>  1   Team      457 non-null    object 
>  2   Number    457 non-null    float64
>  3   Position  457 non-null    object 
>  4   Age       457 non-null    float64
>  5   Height    457 non-null    object 
>  6   Weight    457 non-null    float64
>  7   College   373 non-null    object         # non-null，意思为非空的数据    
>  8   Salary    446 non-null    float64
> dtypes: float64(4), object(5)                 # 类型
> ```

non-null 为非空数据，我们可以看到上面的信息中，总共 458 行，College 字段的空值最多。

### pandas处理JSON文件

JSON（**J**ava**S**cript **O**bject **N**otation，JavaScript 对象表示法），是存储和交换文本信息的语法，类似 XML。

JSON 比 XML 更小、更快，更易解析，更多 JSON 内容可以参考 [JSON 教程](https://www.runoob.com/json/json-tutorial.html)。

Pandas 可以很方便的处理 JSON 数据，本文以 [sites.json](https://static.runoob.com/download/sites.json) 为例，内容如下：

```json
[
   {
   "id": "A001",
   "name": "菜鸟教程",
   "url": "www.runoob.com",
   "likes": 61
   },
   {
   "id": "A002",
   "name": "Google",
   "url": "www.google.com",
   "likes": 124
   },
   {
   "id": "A003",
   "name": "淘宝",
   "url": "www.taobao.com",
   "likes": 45
   }
]


```

```python
import pandas as pd

df = pd.read_json('sites.json')
   
print(df.to_string())
```

**to_string()** 用于返回 DataFrame 类型的数据，我们也可以直接处理 JSON 字符串。

```python
import pandas as pd

data =[
    {
      "id": "A001",
      "name": "菜鸟教程",
      "url": "www.runoob.com",
      "likes": 61
    },
    {
      "id": "A002",
      "name": "Google",
      "url": "www.google.com",
      "likes": 124
    },
    {
      "id": "A003",
      "name": "淘宝",
      "url": "www.taobao.com",
      "likes": 45
    }
]
df = pd.DataFrame(data)

print(df)
```

> ```
>      id    name             url  likes
> 0  A001    菜鸟教程  www.runoob.com     61
> 1  A002  Google  www.google.com    124
> 2  A003      淘宝  www.taobao.com     45
> ```



JSON 对象与 Python 字典具有相同的格式，所以我们可以直接将 Python 字典转化为 DataFrame 数据：

```python
import pandas as pd


# 字典格式的 JSON                                                                                              
s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}

# 读取 JSON 转为 DataFrame                                                                                          
df = pd.DataFrame(s)
print(df)
```

> ```
>       col1 col2
> row1     1    x
> row2     2    y
> row3     3    z
> ```



从 URL 中读取 JSON 数据：

```python
import pandas as pd

URL = 'https://static.runoob.com/download/sites.json'
df = pd.read_json(URL)
print(df)
```

> ```
>      id    name             url  likes
> 0  A001    菜鸟教程  www.runoob.com     61
> 1  A002  Google  www.google.com    124
> 2  A003      淘宝  www.taobao.com     45
> ```

#### 内嵌的 JSON 数据

假设有一组内嵌的 JSON 数据文件 **nested_list.json** ：

```python
{
    "school_name": "ABC primary school",
    "class": "Year 1",
    "students": [
    {
        "id": "A001",
        "name": "Tom",
        "math": 60,
        "physics": 66,
        "chemistry": 61
    },
    {
        "id": "A002",
        "name": "James",
        "math": 89,
        "physics": 76,
        "chemistry": 51
    },
    {
        "id": "A003",
        "name": "Jenny",
        "math": 79,
        "physics": 90,
        "chemistry": 78
    }]
}
```

```python
import pandas as pd

df = pd.read_json('nested_list.json')

print(df)
```

> ```
>           school_name   class                                           students
> 0  ABC primary school  Year 1  {'id': 'A001', 'name': 'Tom', 'math': 60, 'phy...
> 1  ABC primary school  Year 1  {'id': 'A002', 'name': 'James', 'math': 89, 'p...
> 2  ABC primary school  Year 1  {'id': 'A003', 'name': 'Jenny', 'math': 79, 'p...
> ```

这时我们就需要使用到 **json_normalize()** 方法将内嵌的数据完整的解析出来：

```python
import pandas as pd
import json

# 使用 Python JSON 模块载入数据
with open('nested_list.json','r') as f:
    data = json.loads(f.read())

# 展平数据
df_nested_list = pd.json_normalize(data, record_path =['students'])
print(df_nested_list)
```

> ```
>      id   name  math  physics  chemistry
> 0  A001    Tom    60       66         61
> 1  A002  James    89       76         51
> 2  A003  Jenny    79       90         78
> ```

**data = json.loads(f.read())** 使用 Python JSON 模块载入数据。

**json_normalize()** 使用了参数 **record_path** 并设置为 **['students']** 用于展开内嵌的 JSON 数据 **students**。

显示结果还没有包含 school_name 和 class 元素，如果需要展示出来可以使用 meta 参数来显示这些元数据：

```python
import pandas as pd
import json

# 使用 Python JSON 模块载入数据
with open('nested_list.json','r') as f:
    data = json.loads(f.read())

# 展平数据
df_nested_list = pd.json_normalize(
    data,
    record_path =['students'],
    meta=['school_name', 'class']
)
print(df_nested_list)
```

> ```
>      id   name  math  physics  chemistry         school_name   class
> 0  A001    Tom    60       66         61  ABC primary school  Year 1
> 1  A002  James    89       76         51  ABC primary school  Year 1
> 2  A003  Jenny    79       90         78  ABC primary school  Year 1
> ```

接下来，让我们尝试读取更复杂的 JSON 数据，该数据嵌套了列表和字典，数据文件 **nested_mix.json** 如下：

```json
{
    "school_name": "local primary school",
    "class": "Year 1",
    "info": {
      "president": "John Kasich",
      "address": "ABC road, London, UK",
      "contacts": {
        "email": "admin@e.com",
        "tel": "123456789"
      }
    },
    "students": [
    {
        "id": "A001",
        "name": "Tom",
        "math": 60,
        "physics": 66,
        "chemistry": 61
    },
    {
        "id": "A002",
        "name": "James",
        "math": 89,
        "physics": 76,
        "chemistry": 51
    },
    {
        "id": "A003",
        "name": "Jenny",
        "math": 79,
        "physics": 90,
        "chemistry": 78
    }]
}
```

nested_mix.json 文件转换为 DataFrame：

```python
import pandas as pd
import json

# 使用 Python JSON 模块载入数据
with open('nested_mix.json','r') as f:
    data = json.loads(f.read())
   
df = pd.json_normalize(
    data,
    record_path =['students'],
    meta=[
        'class',
        ['info', 'president'],
        ['info', 'contacts', 'tel']
    ]
)

print(df)
```

> ```
>      id   name  math  physics  chemistry   class info.president info.contacts.tel
> 0  A001    Tom    60       66         61  Year 1    John Kasich         123456789
> 1  A002  James    89       76         51  Year 1    John Kasich         123456789
> 2  A003  Jenny    79       90         78  Year 1    John Kasich         123456789
> ```

#### 读取内嵌数据中的一组数据

以下是实例文件 **nested_deep.json**，我们只读取内嵌中的 **math** 字段：

```json
{
    "school_name": "local primary school",
    "class": "Year 1",
    "students": [
    {
        "id": "A001",
        "name": "Tom",
        "grade": {
            "math": 60,
            "physics": 66,
            "chemistry": 61
        }
 
    },
    {
        "id": "A002",
        "name": "James",
        "grade": {
            "math": 89,
            "physics": 76,
            "chemistry": 51
        }
       
    },
    {
        "id": "A003",
        "name": "Jenny",
        "grade": {
            "math": 79,
            "physics": 90,
            "chemistry": 78
        }
    }]
}
```

这里我们需要使用到 **glom** 模块来处理数据套嵌，**glom** 模块允许我们使用 **.** 来访问内嵌对象的属性。

第一次使用我们需要安装 glom：

```bash
 pip3 install glom -i https://pypi.tuna.tsinghua.edu.cn/simple
```



```python
import pandas as pd
from glom import glom

df = pd.read_json('nested_deep.json')

data = df['students'].apply(lambda row: glom(row, 'grade.math'))
print(data)
```

> ```
> 0    60
> 1    89
> 2    79
> Name: students, dtype: int64
> ```

### pandas处理Excel文件

#### Excel读取

> https://blog.csdn.net/weixin_43092663/article/details/124155354

##### 读写Excel详解

Excel的读取可以采用ExcelFile类和read_excel两种方法，在实际使用中差别不大。其区别可以见[e-learn](https://www.e-learn.cn/topic/210541)上贴子讨论，观点摘录如下：

除了语法之外没有特别的区别。从技术上讲，ExcelFile是一个类，read_excel是一个函数。在任何一种情况下，实际都是由定义在ExcelFile的_parse_excel解析
ExcelFile.parse循环速度更快（存疑）

###### ExcelFile类

类的定义和方法参数感兴趣的可以查看源码

```python
ExcelFile.parse(sheet_name=0, header=0, names=None, index_col=None, usecols=None, squeeze=None, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, parse_dates=False, date_parser=None, thousands=None, comment=None, skipfooter=0, convert_float=None, mangle_dupe_cols=True, **kwds)

```

```python
import pandas as pd
table = pd.ExcelFile('./data/table1.xlsx')
print(type(table))
print(table.sheet_names) ##按顺序获取sheet名称
## 提取表格信息
sheet1 = table.parse(sheet_name=0) #可以使用序号，一次性读取多个用列表[0,1]
sheet2 = table.parse(sheet_name=table.sheet_names[1]) #也可以使用sheet名
print('sheet1:\n{0}\n sheet2:\n{1}'.format(sheet1,sheet2))

```

输出结果如下：

![image-20230419112206485](image-20230419112206485.png)



###### read_excel()方法

```python
pandas.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, squeeze=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, parse_dates=False, date_parser=None, thousands=None, decimal=’.’, comment=None, skipfooter=0, convert_float=None, mangle_dupe_cols=True, storage_options=None)

主要参数	解释
io	文件路径
sheet_name	sheet名称，可以是数字或sheet名，默认‘sheet1 ’
header	指定标题行，默认第一行为标题，可以设置多行如[0,1]为标题行
names	在header=None的前提下，补充列名
index_col	用于指定索引，默认为None，设置多列索引index_col=[0,1]
usecols	用于指定读取的列，默认为None，读取第2-4列usecols = [1,2,3]
engine	“xlrd”支持.xls，“openpyxl”支持.xlsx
dtype	指定数据列的类型，如{‘a’: np.float64, ‘b’: str}
converters	转换指定列的函数字典{“A”:lambda x: x/100,“B”:lambda x: x/100}
skiprows	省略指定行数的数据，从第一行开始
skipfooter	省略指定行数的数据，是从尾部数的行开始
```

示例如下

```python
##可以逐个sheet读取，也可以一次读取
st1 = pd.read_excel('./data/table1.xlsx',sheet_name='1班')
st2 = pd.read_excel('./data/table1.xlsx',sheet_name='2班')
table = pd.read_excel('./data/table1.xlsx',sheet_name=[0,1]) ## 一次性读取 st1 = table[0],st2 = table[1]
print('st1:\n{0}\n st2:\n{1}'.format(st1,st2)) #与上面输出结果相同

```

使用其他参数

```python
st3 = pd.read_excel('./data/table1.xlsx',sheet_name=1,dtype={'体重': int,'分数': float}) 
st4 = pd.read_excel('./data/table1.xlsx',sheet_name=1,converters={'身高':lambda x:x*100,'体重':lambda x:x*2}) 
#Both a converter and dtype were specified for column 体重 - only the converter will be used
st5 = pd.read_excel('./data/table1.xlsx',sheet_name=1,dtype={'体重': int,'分数': float},converters={'身高':lambda x:x*100,'体重':lambda x:x*2})
print('st3:\n{0}\n st4:\n{1}\n st5:\n{2}'.format(st3,st4,st5))

```

注意：对某一列同时使用dtype和converters，仅仅converter被有效使用

![image-20230419112722695](image-20230419112722695.png)

```python
df = pd.read_excel('./xdiwfjH98xxone (1).xlsx')
row, col = df.shape
# print(row, col)
for i in range(row):
    tmp = df.iloc[i]
    print(tmp[key]) # key为excel中每一列的关键字
```

#### Excel写入

##### 写入Excel

有两种方法可以进行写入，使用to_excel方法和ExcelWriter类，如要写入到一个文件中多个sheet，需要使用ExcelWriter类。
ExcelWriter定义如下：

```python
class pandas.ExcelWriter(path, engine=None, date_format=None, datetime_format=None, mode=‘w’, storage_options=None, if_sheet_exists=None, engine_kwargs=None, **kwargs)
```

to_excel方法：

```python
DataFrame.to_excel(excel_writer, sheet_name=‘Sheet1’, na_rep=’’, float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep=‘inf’, verbose=True, freeze_panes=None, storage_options=None)
```

ExcelWriter()可以向同一个excel的不同sheet中写入对应的表格数据
代码如下（示例）：

```python
#使用pd.to_excel方法
st5.to_excel('./data/table2.xlsx',sheet_name='newSheet')

```

ExcelWriter类写入流程：基于已创建的writer对象，利用to_excel()方法将不同的dataframe及其对应的sheet名称写入该writer对象中，并在全部表格写入完成之后，使用save()方法来执行writer中内容向对应实体excel文件写入数据的过程
同python文件IO一样，有两种写入方式。writer应该作为上下文管理器，否则，需要调用close() 保持和关闭打开的文件句柄
第一种：

```python
writer = pd.ExcelWriter('./data/table3.xlsx')
st4.to_excel(writer,sheet_name='st4',index=False)
st5.to_excel(writer,sheet_name='st5',index=False)
##数据写出到excel文件中
writer.save()

```

第二种：

```python
with pd.ExcelWriter('./data/table4.xlsx') as writer:  
    st4.to_excel(writer, sheet_name='st4',index=False)
    st5.to_excel(writer, sheet_name='st5',index=False)

```

##### 已有Excel增加sheet

mode分为两种写入’w’和追加‘a’，在已有表格中增加sheet使用‘a’模式，指定写入的sheet名称，代码如下（示例）：

```python
with pd.ExcelWriter('./data/table4.xlsx',mode='a',engine='openpyxl') as writer:
    st3.to_excel(writer, sheet_name='st3',index=False)

```

##### 覆盖Excel中已有sheet

如果需要重新写入Excel中某个sheet，直接往Excel写入同名sheet不会覆盖，而是创建一个新的表单（sheet1），需要采用以下方法

```python
with pd.ExcelWriter('./data/table4.xlsx',mode='a',engine='openpyxl') as writer:
    wb = writer.book # openpyxl.workbook.workbook.Workbook 获取所有sheet
    wb.remove(wb['st3']) #删除需要覆盖的sheet
    st1.to_excel(writer, sheet_name='st3',index=False) ##sheet st3的内容更新成st1值

```

##### 已有sheet中追加数据

读取原表格的Workbook和sheets，赋给writer句柄，保证数据内容的一致。获取拟写入表单的数据行数，从下一行开始写入，需要设置header = False

```python
import pandas as pd
from openpyxl import load_workbook
newdata = pd.DataFrame([('6','LUCY','F',190,135,90),('7','ROB','M',181,145,78),('8','FRADI','M',176,133,80)])#需要新写入的数据
df = pd.read_excel('./data/table4.xlsx',sheet_name='st4') #读取原数据文件和表
writer = pd.ExcelWriter('./data/table4.xlsx',engine='openpyxl')
book = load_workbook('./data/table4.xlsx')
writer.book = book # openpyxl.workbook.workbook.Workbook
writer.sheets = dict((ws.title, ws) for ws in book.worksheets) #{'st4': <Worksheet "st4">, 'st5': <Worksheet "st5">, 'st3': <Worksheet "st3">}
df_rows = df.shape[0] #获取原数据的行数
newdata.to_excel(writer, sheet_name='st4',startrow = df_rows + 1, index = False, header = False)#将数据写入excel中的st3,从第一个空行开始写
writer.save()#保存

```

### pandas数据清洗

数据清洗是对一些没有用的数据进行处理的过程。

很多数据集存在数据缺失、数据格式错误、错误数据或重复数据的情况，如果要对使数据分析更加准确，就需要对这些没有用的数据进行处理。

在这个教程中，我们将利用 Pandas包来进行数据清洗。

本文使用到的测试数据 [property-data.csv](https://static.runoob.com/download/property-data.csv) 如下：

![img](6A6DE9DA-E0EE-4001-8C21-1D6A8EBF70FF.jpeg)

#### 清洗空值

上表包含了四种空数据：

- n/a
- NA
- —
- na

如果我们要删除包含空字段的行，可以使用 **dropna()** 方法，语法格式如下：

```bash
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
```

**参数说明：**

- axis：默认为 **0**，表示逢空值剔除整行，如果设置参数 **axis＝1** 表示逢空值去掉整列。
- how：默认为 **'any'** 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 **how='all'** 一行（或列）都是 NA 才去掉这整行。
- thresh：设置需要多少非空值的数据才可以保留下来的。
- subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
- inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。

我们可以通过 **isnull()** 判断各个单元格是否为空。

```python
import pandas as pd

df = pd.read_csv('property-data.csv')

print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())
```

![img](2A5B93BC-E0A3-4864-98B7-7DAE0E92C5F2.jpg)

以上例子中我们看到 Pandas 把 n/a 和 NA 当作空数据，na 不是空数据，不符合我们要求，我们可以指定空数据类型：

```python
import pandas as pd

missing_values = ["n/a", "na", "--"]
df = pd.read_csv('property-data.csv', na_values = missing_values)

print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())
```

![img](FCE8C077-C981-4764-ACBC-CB129304F831.jpg)

接下来的实例演示了删除包含空数据的行。

```python
import pandas as pd

df = pd.read_csv('property-data.csv')

new_df = df.dropna()

print(new_df.to_string())
```

![img](4744B204-1527-49DE-B749-E39D6C7DFE01.jpg)

**注意：**默认情况下，dropna() 方法返回一个新的 DataFrame，不会修改源数据。

如果你要修改源数据 DataFrame, 可以使用 **inplace = True** 参数:

```python
import pandas as pd

df = pd.read_csv('property-data.csv')

df.dropna(inplace = True)

print(df.to_string())
```



我们也可以移除指定列有空值的行：

```python
# 移除 ST_NUM 列中字段值为空的行：

import pandas as pd

df = pd.read_csv('property-data.csv')

df.dropna(subset=['ST_NUM'], inplace = True)

print(df.to_string())
```

![img](C83C70BC-5E47-4397-938D-7445104BE551.jpg)

我们也可以 **fillna()** 方法来替换一些空字段：

使用 12345 替换空字段：

```python
import pandas as pd

df = pd.read_csv('property-data.csv')

df.fillna(12345, inplace = True)

print(df.to_string())
```

![img](5033AA75-BC7D-4192-9428-221765EA3C58.jpg)

我们也可以指定某一个列来替换数据：

使用 12345 替换 PID 为空数据：

```python
import pandas as pd

df = pd.read_csv('property-data.csv')

df['PID'].fillna(12345, inplace = True)

print(df.to_string())
```

![img](2F955E95-8C4C-4E7C-B788-5714B2C898C2.jpg)

替换空单元格的常用方法是计算列的均值、中位数值或众数。

Pandas使用 **mean()**、**median()** 和 **mode()** 方法计算列的均值（所有值加起来的平均值）、中位数值（排序后排在中间的数）和众数（出现频率最高的数）。

使用 mean() 方法计算列的均值并替换空单元格：

```python
import pandas as pd

df = pd.read_csv('property-data.csv')

x = df["ST_NUM"].mean()

df["ST_NUM"].fillna(x, inplace = True)

print(df.to_string())
```

![img](6A758363-02FA-4F6E-9F30-7A3E4489639A.jpg)

使用 median() 方法计算列的中位数并替换空单元格：

```python
import pandas as pd

df = pd.read_csv('property-data.csv')

x = df["ST_NUM"].median()

df["ST_NUM"].fillna(x, inplace = True)

print(df.to_string())
```

![img](551B8875-D393-4003-BB68-695EBEDBB0FE.jpg)

使用 mode() 方法计算列的众数并替换空单元格：

```python
import pandas as pd

df = pd.read_csv('property-data.csv')

x = df["ST_NUM"].mode()

df["ST_NUM"].fillna(x, inplace = True)

print(df.to_string())
```

![img](40F6D1C2-CFD7-4C53-B887-86695F486E6D.jpg)

#### 清洗格式错误数据

数据格式错误的单元格会使数据分析变得困难，甚至不可能。

我们可以通过包含空单元格的行，或者将列中的所有单元格转换为相同格式的数据。

以下实例会格式化日期：

```python
import pandas as pd

# 第三个日期格式错误
data = {
  "Date": ['2020/12/01', '2020/12/02' , '20201226'],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())
```

> ```
>            Date  duration
> day1 2020-12-01        50
> day2 2020-12-02        40
> day3 2020-12-26        45
> ```

#### 清洗错误数据

数据错误也是很常见的情况，我们可以对错误的数据进行替换或移除。

以下实例会替换错误年龄的数据：

```python
import pandas as pd

person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)

df.loc[2, 'age'] = 30 # 修改数据

print(df.to_string())
```

将 age 大于 120 的设置为 120:

```python
import pandas as pd

person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 200, 12345]    
}

df = pd.DataFrame(person)

for x in df.index:
  if df.loc[x, "age"] > 120:
    df.loc[x, "age"] = 120

print(df.to_string())
```

> ```
>      name  age
> 0  Google   50
> 1  Runoob   40
> ```

#### 清洗重复数据

如果我们要清洗重复数据，可以使用 **duplicated()** 和 **drop_duplicates()** 方法。

如果对应的数据是重复的，**duplicated()** 会返回 True，否则返回 False。

```python
import pandas as pd

person = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]  
}
df = pd.DataFrame(person)

print(df.duplicated())
```

> ```
> 0    False
> 1    False
> 2     True
> 3    False
> dtype: bool
> ```

删除重复数据，可以直接使用**drop_duplicates()** 方法。

```python
import pandas as pd

persons = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]  
}

df = pd.DataFrame(persons)

df.drop_duplicates(inplace = True)
print(df)
```

> ```
>      name  age
> 0  Google   50
> 1  Runoob   40
> 3  Taobao   23
> ```

### pandas 常用函数

> [Pandas 常用函数 | 菜鸟教程 (runoob.com)](https://www.runoob.com/pandas/pandas-functions.html)

#### 读取数据

| 函数                                  | 说明                       |
| :------------------------------------ | :------------------------- |
| pd.read_csv(filename)                 | 读取 CSV 文件；            |
| pd.read_excel(filename)               | 读取 Excel 文件；          |
| pd.read_sql(query, connection_object) | 从 SQL 数据库读取数据；    |
| pd.read_json(json_string)             | 从 JSON 字符串中读取数据； |
| pd.read_html(url)                     | 从 HTML 页面中读取数据。   |

```python
import pandas as pd

# 从 CSV 文件中读取数据
df = pd.read_csv('data.csv')

# 从 Excel 文件中读取数据
df = pd.read_excel('data.xlsx')

# 从 SQL 数据库中读取数据
import sqlite3
conn = sqlite3.connect('database.db')
df = pd.read_sql('SELECT * FROM table_name', conn)

# 从 JSON 字符串中读取数据
json_string = '{"name": "John", "age": 30, "city": "New York"}'
df = pd.read_json(json_string)

# 从 HTML 页面中读取数据
url = 'https://www.runoob.com'
dfs = pd.read_html(url)
df = dfs[0] # 选择第一个数据框
```
`pd.read_excel()`

- 文件路径
- 读取引擎：engine，可以不指定，让pandas自己处理。xls:xlrd, xlsx:openpyxl	
- 页：sheet_name，字符串或者数字	
- 行索引：
  - 默认pandas会给数据每一行的前面，加上索引:index_col=None。也可以手动指定：index_col=0。不建议多行索引:index_col=[0, 1]
  - 手动指定:pd.set_index('Name', inplace=True)
- 列索引
  - 默认header=0，第一行为列索引




#### 查看数据

| 函数          | 说明                                                       |
| :------------ | :--------------------------------------------------------- |
| df.head(n)    | 显示前 n 行数据；                                          |
| df.tail(n)    | 显示后 n 行数据；                                          |
| df.info()     | 显示数据的信息，包括列名、数据类型、缺失值等；             |
| df.describe() | 显示数据的基本统计信息，包括均值、方差、最大值、最小值等； |
| df.shape      | 显示数据的行数和列数。                                     |

```python
import pandas as pd

data = [
    {"name": "Google", "likes": 25, "url": "https://www.google.com"},
    {"name": "Runoob", "likes": 30, "url": "https://www.runoob.com"},
    {"name": "Taobao", "likes": 35, "url": "https://www.taobao.com"}
]

df = pd.DataFrame(data)
# 显示前两行数据
print(df.head(2))
# 显示前最后一行数据
print(df.tail(1))
```

> ```
>      name  likes                     url
> 0  Google     25  https://www.google.com
> 1  Runoob     30  https://www.runoob.com
>      name  likes                     url
> 2  Taobao     35  https://www.taobao.com
> ```

读取每一行

```python
import pandas as pd

# 读取 Excel 文件数据
data = pd.read_excel('test.xlsx')

# 生成问答对
for index, row in data.iterrows():
    project = row['项目类型']
    container = row['容器名称']
    cpu = str(row['CPU']*100) + '%'
    memory_cache = row['memory/cache']
    disk = row['磁盘:挂载目录']

    # 输出问答对

    if disk == '\\':
        print(f'{project}项目中{container}容器需要占用的CPU、内存及挂载目录磁盘需要多少')
        print(f'{container}容器资源占用情况：CPU为{cpu}，memory/cache为{memory_cache}，挂载目录磁盘无要求\n')
    else:
        print(f'{project}项目中{container}容器需要占用的CPU、内存及挂载目录磁盘需要多少')
        print(f'{container}容器资源占用情况：CPU为{cpu}，memory/cache为{memory_cache}，挂载目录磁盘为{disk}\n')
```



#### 数据清洗

| 函数                             | 说明                     |
| :------------------------------- | :----------------------- |
| df.dropna()                      | 删除包含缺失值的行或列； |
| df.fillna(value)                 | 将缺失值替换为指定的值； |
| df.replace(old_value, new_value) | 将指定值替换为新值；     |
| df.duplicated()                  | 检查是否有重复的数据；   |
| df.drop_duplicates()             | 删除重复的数据。         |

##### df.drop_duplicates()

在一个数据集中，找出重复的数据删并将其删除，最终只保存一个唯一存在的数据项，这就是数据去重的整个过程。删除重复数据是数据分析中经常会遇到的一个问题。通过数据去重，不仅可以节省内存空间，提高写入性能，还可以提升数据集的精确度，使得数据集不受重复数据的影响。

 drop_duplicates()函数的语法格式如下：

`df.drop_duplicates(subset=['A','B','C'],keep='first',inplace=True)`
参数说明如下：

subset：表示要进去重的列名，默认为 None。
keep：有三个可选参数，分别是 first、last、False，默认为 first，表示只保留第一次出现的重复项，删除其余重复项，last 表示只保留最后一次出现的重复项，False 则表示删除所有重复项。
inplace：布尔值参数，默认为 False 表示删除重复项后返回一个副本，若为 Ture 则表示直接在原数据上删除重复项。

```python
import pandas as pd
data={
'A':[1,0,1,1],
'B':[0,2,5,0],
'C':[4,0,4,4],
'D':[1,0,1,1]
}
df=pd.DataFrame(data=data)

   A  B  C  D
0  1  0  4  1
1  0  2  0  0
2  1  5  4  1
3  1  0  4  1
```



```python
1) 默认保留第一次出现的重复项
#默认保留第一次出现的重复项 df.drop_duplicates()
 
输出结果：
  A B C D
0 1 0 4 1
1 0 2 0 0
2 1 5 4 1
 
2) keep=False删除所有重复项
#默认保留第一次出现的重复项
df.drop_duplicates(keep=False)
 
输出结果：
  A B C D
1 0 2 0 0
2 1 5 4 1
```

**根据指定标签去重**

```python
#去除所有重复项，对于B列来说两个0是重复项
df.drop_duplicates(subset=['B'],keep=False)
#简写，省去subset参数
#df.drop_duplicates(['B'],keep=False)
print(df)
 
输出结果：
  A B C D
1 0 2 0 0
2 1 5 4 1
```

从上述示例可以看出，删除重复项后，行标签使用的数字是原来的，并没有从 0 重新开始，那么我们应该怎么从 0 重置索引呢？Pandas 提供的 `reset_index()` 函数会直接使用重置后的索引。如下所示：

```python
#重置索引，从0重新开始 df.reset_index(drop=True)
 
输出结果：
  A B C D
0 0 2 0 0
1 1 5 4 1
```

**指定多列同时去重**

```python
#last只保留最后一个重复项
# 指定多列时，需要同时都有重复数据才会去重操作
df.drop_duplicates(['B','C'],keep='last')
 
输出结果：
  A B C D
1 0 2 0 0
2 1 5 4 1
3 1 0 4 1
```

上述数据集中，第 0 行、第 3 行对应的列标签数据相同，我们使用参数值“last”保留最后一个重复项，也就是第 3 行数据。



#### 数据选择和切片

| 函数                                          | 说明                         |
| :-------------------------------------------- | :--------------------------- |
| df[column_name]                               | 选择指定的列；               |
| df.loc[row_index, column_name]                | 通过标签选择数据；           |
| df.iloc[row_index, column_index]              | 通过位置选择数据；           |
| df.ix[row_index, column_name]                 | 通过标签或位置选择数据；     |
| df.filter(items=[column_name1, column_name2]) | 选择指定的列；               |
| df.filter(regex='regex')                      | 选择列名匹配正则表达式的列； |
| df.sample(n)                                  | 随机选择 n 行数据。          |

#### 数据排序

| 函数                                                         | 说明                 |
| :----------------------------------------------------------- | :------------------- |
| df.sort_values(column_name)                                  | 按照指定列的值排序； |
| df.sort_values([column_name1, column_name2], ascending=[True, False]) | 按照多个列的值排序； |
| df.sort_index()                                              | 按照索引排序。       |

Pands 提供了两种排序方法，分别是**按标签排序和按数值排序**。

```python
import pandas as pd
import numpy as np
#行标签乱序排列，列标签乱序排列
unsorted_df=pd.DataFrame(np.random.randn(4,2),index=[1,3,2,0],columns=['col2','col1'])
print(unsorted_df)
 
输出结果：
       col2      col1
1 -0.053290 -1.442997
3 -0.203066 -0.702727
2  0.111759  0.965251
0 -0.896778  1.100156
```

上述示例，行标签和数值元素均未排序，下面分别使用标签排序、数值排序对其进行操作。

##### df.sort_index()

**按行标签排序**

使用 sort_index() 方法对行标签排序，指定轴参数（axis）或者排序顺序。或者可以对 DataFrame 进行排序。默认情况下，按照行标签序排序。

```python

# 排序顺序，通过将布尔值传递给ascending参数，可以控制排序的顺序（行号顺序）
sorted_df = unsorted_df.sort_index(ascending=False)
print(sorted_df)
 
输出结果：
       col2      col1
3 -0.203066 -0.702727
2  0.111759  0.965251
1 -0.053290 -1.442997
0 -0.896778  1.100156
```

**按列标签排序**

通过给 axis 轴参数传递 0 或 1，可以对列标签进行排序。默认情况下，axis=0 表示按行排序；而 axis=1 则表示按列排序。

```
sorted_df=unsorted_df.sort_index(axis=1)
print (sorted_df)
 
输出结果：
       col1      col2
1 -1.442997 -0.053290 
3 -0.702727 -0.203066 
2  0.965251  0.111759  
0  1.100156 -0.896778  
```

##### df.sort_values()

按值排序，接受一个by参数，该参数值是要排序数列的 DataFrame 列名。

```python
import pandas as pd
import numpy as np
unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
 
# 注意：当对 col1 列排序时，相应的 col2 列的元素值和行索引也会随 col1 一起改变。
sorted_df = unsorted_df.sort_values(by='col1')
print (sorted_df)
 
输出结果：
   col1  col2
1     1     3
2     1     2
3     1     4
0     2     1
 
# by 参数可以接受一个列表参数值，如下所示：
sorted_df = unsorted_df.sort_values(by=['col1','col2'])
print (sorted_df）
 
输出结果：
   col1  col2
2     1     2
1     1     3
3     1     4
0     2     1
```

**排序算法**

sort_values() 提供了参数`kind`用来指定排序算法。这里有三种排序算法：

- mergesort
- heapsort
- quicksort

默认为 quicksort(快速排序) ，其中 Mergesort 归并排序是最稳定的算法。

```python
sorted_df = unsorted_df.sort_values(by='col1' ,kind='mergesort')
print (sorted_df)
 
输出结果：
   col1  col2
1     1     3
2     1     2
3     1     4
0     2     1
```



#### 数据分组和聚合

| 函数                                            | 说明                         |
| :---------------------------------------------- | :--------------------------- |
| df.groupby(column_name)                         | 按照指定列进行分组；         |
| df.aggregate(function_name)                     | 对分组后的数据进行聚合操作； |
| df.pivot_table(values, index, columns, aggfunc) | 生成透视表。                 |

#### 新增行

> 使用loc(len(df))新增行

```python
with open('./project.json', 'r', encoding='utf-8') as fr:
    content = json.load(fr)
    item_list = jsonpath(content, '$[*]')
    
    df = pd.DataFrame(columns=['id', 'key', 'value']) # 外部定义空的DataFrame
    
    for item in item_list:
        id = jsonpath(item, '$.id')
        key_list = jsonpath(item, '$..value.labels[*]')
        value_list = jsonpath(item, '$..value.text')
        if(key_list != False and value_list != False):
            for i in range(0, len(key_list)):
                new_row = {'id': id[0], 'key': key_list[i], 'value': value_list[i]}
                
                df.loc[len(df)] = new_row # 使用loc方法，新增行
```



#### 数据合并

| 函数                               | 说明                             |
| :--------------------------------- | :------------------------------- |
| pd.concat([df1, df2])              | 将多个数据框按照行或列进行合并； |
| pd.merge(df1, df2, on=column_name) | 按照指定列将两个数据框进行合并。 |

##### `pd.concat`

`pandas.concat`是一个用于合并（连接）pandas对象的函数，可以将多个DataFrame或Series对象沿指定轴进行连接。它提供了灵活的选项，可根据需求进行行或列的连接。

以下是`pandas.concat`函数的基本语法：

```python
pandas.concat(objs, axis=0, join='outer', ignore_index=False)
```

参数说明：

- `objs`: 要连接的DataFrame或Series对象的序列（例如列表、元组、字典）。
- `axis`: 连接的轴方向。默认为0，表示按行连接；设置为1时表示按列连接。
- `join`: 连接的方式。默认为'outer'，表示使用并集连接；设置为'inner'时表示使用交集连接。
- `ignore_index`: 是否忽略原始索引，生成新的索引。默认为False。

下面是几个使用`pandas.concat`函数的示例：

1. 行连接多个DataFrame：

```python
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
result = pd.concat([df1, df2])
print(result)
```

输出：

```python
   A  B
0  1  3
1  2  4
0  5  7
1  6  8
```

1. 列连接多个DataFrame：

```python
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]})
result = pd.concat([df1, df2], axis=1)
print(result)
```

输出：

```python
   A  B  C  D
0  1  3  5  7
1  2  4  6  8
```

1. 忽略原始索引，生成新的索引：

```python
import pandas as pd

s1 = pd.Series([1, 2])
s2 = pd.Series([3, 4])
result = pd.concat([s1, s2], ignore_index=True)
print(result)
```

输出：

```python
0    1
1    2
2    3
3    4
dtype: int64
```

以上是`pandas.concat`函数的基本用法，它可以在数据处理和数据合并的过程中起到很大的作用。你可以根据实际需求使用不同的参数组合来完成连接操作。

#### 数据选择和过滤

| 函数                                 | 说明                                   |
| :----------------------------------- | :------------------------------------- |
| df.loc[row_indexer, column_indexer]  | 按标签选择行和列。                     |
| df.iloc[row_indexer, column_indexer] | 按位置选择行和列。                     |
| df[df['column_name'] > value]        | 选择列中满足条件的行。                 |
| df.query('column_name > value')      | 使用字符串表达式选择列中满足条件的行。 |

#### 数据统计和描述

| df.describe() | 计算基本统计信息，如均值、标准差、最小值、最大值等。 |
| ------------- | ---------------------------------------------------- |
| df.mean()     | 计算每列的平均值。                                   |
| df.median()   | 计算每列的中位数。                                   |
| df.mode()     | 计算每列的众数。                                     |
| df.count()    | 计算每列非缺失值的数量。                             |

#### 数据分组并应用函数

在Pandas中，`groupby()`方法用于对数据进行分组，并返回一个`GroupBy`对象。`GroupBy`对象允许你在每个组上应用函数或方法，其中包括使用`apply()`方法。

要使用`apply()`方法，你需要首先创建一个函数，该函数将应用于每个组。然后，你可以通过`apply()`方法将该函数应用于`GroupBy`对象。

以下是一个示例，演示如何使用`groupby()`和`apply()`方法：

```python
import pandas as pd

# 创建一个示例数据集
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
        'Subject': ['Math', 'English', 'Math', 'English', 'Math'],
        'Score': [80, 75, 90, 85, 95]}
df = pd.DataFrame(data)

# 使用groupby()方法按照姓名（Name）进行分组
grouped = df.groupby('Name')

# 定义一个函数，用于计算每个组的平均分数
def calculate_average(group):
    print(group) # 有多少分组，就有多少个分组对象
    #   Name  Subject  Score
    # 0  Alice     Math     80
    # 3  Alice  English     85

    #   Name  Subject  Score
    # 1  Bob  English     75
    # 4  Bob     Math     95

    #   Name Subject  Score
    # 2  Charlie    Math     90
    return group['Score'].mean()

# 应用calculate_average函数到每个组
result = grouped.apply(calculate_average) # 将每一个分组对象，作为实参

# print(result)
```

输出结果将是每个组的平均分数：

```python
Name
Alice      87.5
Bob        85.0
Charlie    90.0
dtype: float64
```

在这个例子中，我们按照姓名（Name）对数据进行分组，并定义了一个名为`calculate_average`的函数，用于计算每个组的平均分数。然后，我们使用`apply()`方法将该函数应用于`GroupBy`对象，并将结果存储在`result`中。最后，我们打印出`result`来显示每个组的平均分数。



备注：直接打印分组对象，是看不到实际数据的，可以通过`print(grouped.apply(lambda x: x))`来查看，也可以将结果写到excel中，更直观。也可以用`grouped.values`方法

#### 计算唯一值数量

在Pandas中，`nunique()`是一个用于计算唯一值数量的方法。它用于统计一个Series或DataFrame中不同值的个数，忽略缺失值（NaN）。

`nunique()`的语法如下：

- 对于Series对象：`series.nunique(dropna=True)`
- 对于DataFrame对象：`df.nunique(axis=0, dropna=True)`

其中，参数说明如下：

- `dropna`（可选）：布尔值，表示是否在计算唯一值数量时忽略缺失值。默认值为`True`，即忽略缺失值。

下面是一些示例，演示了如何使用`nunique()`方法：

1. 对于Series对象：

```python
import pandas as pd

# 创建一个Series对象
s = pd.Series([1, 2, 3, 3, 4, 4, 5, 5, 5, None])

# 计算唯一值的数量（忽略缺失值）
unique_count = s.nunique()
print(unique_count)  # 输出: 5
```

在这个例子中，Series对象`s`包含10个元素，其中有5个不同的值。使用`nunique()`方法计算唯一值的数量，结果为5。

1. 对于DataFrame对象：

```python
import pandas as pd

# 创建一个DataFrame对象
data = {'A': [1, 2, 3, 4, None],
        'B': [2, 3, 4, 4, 5],
        'C': [1, 1, 1, None, None]}

df = pd.DataFrame(data)

# 计算每列的唯一值数量（忽略缺失值）
unique_counts = df.nunique()
print(unique_counts)
```

在这个例子中，DataFrame对象`df`包含3列，每列包含5个元素。使用`nunique()`方法计算每列的唯一值数量，结果将是一个Series对象，其中包含每列的唯一值数量。输出结果将是：

```python
A    4
B    4
C    1
dtype: int64
```

结果显示，列"A"和"B"都有4个不同的值，而列"C"只有1个不同的值。

`nunique()`方法对于数据的探索和统计非常有用，特别是在数据预处理和数据分析过程中，用于了解数据中的唯一值数量和数据分布情况。

#### 求和

在Pandas中，`sum()`是一个用于计算序列或数据框中数值列的总和的方法。它可以应用于Series对象或DataFrame对象。

`sum()`的语法如下：

- 对于Series对象：`series.sum()`
- 对于DataFrame对象：`df.sum(axis=0, skipna=None)`

其中，参数说明如下：

- `axis`（可选）：用于指定计算总和的轴。默认值为0，表示沿着列进行计算，将每列的值相加得到总和。如果`axis=1`，则表示沿着行进行计算，将每行的值相加得到总和。
- `skipna`（可选）：布尔值，表示是否忽略缺失值（NaN）。默认值为`None`，表示根据对象类型和输入数据的缺失值处理策略来确定是否忽略缺失值。当`skipna=True`时，将忽略缺失值；当`skipna=False`时，缺失值将被视为0。

下面是一些示例，演示了如何使用`sum()`方法：

1. 对于Series对象：

```python
import pandas as pd

# 创建一个Series对象
s = pd.Series([1, 2, 3, 4, 5])

# 计算序列的总和
total = s.sum()
print(total)  # 输出: 15
```

在这个例子中，Series对象`s`包含5个元素，使用`sum()`方法计算这些元素的总和，结果为15。

1. 对于DataFrame对象：

```python
import pandas as pd

# 创建一个DataFrame对象
data = {'A': [1, 2, 3, 4],
        'B': [2, 3, 4, 5],
        'C': [3, 4, 5, 6]}

df = pd.DataFrame(data)

# 计算每列的总和
column_sums = df.sum()
print(column_sums)
```

在这个例子中，DataFrame对象`df`包含3列，每列包含4个元素。使用`sum()`方法计算每列的总和，结果将是一个Series对象，其中包含每列的总和。输出结果将是：

```python
A    10
B    14
C    18
dtype: int64
```

结果显示，列"A"的总和为10，列"B"的总和为14，列"C"的总和为18。

注意，`sum()`方法在将布尔值`True`视为1，而布尔值`False`视为0，因此计算总和实际上就是计算`True`值的数量。如果是计算整体准确率，可以先将数组扁平化。



按行求和

```
import pandas as pd

# 假设数据存储在一个名为df的DataFrame中

# 统计每一行中True的数量
row_counts = df.iloc[:, 1:].sum(axis=1)

# 计算每一行中True的占比
row_percentages = row_counts / df.shape[1]

print("每一行True的数量：")
print(row_counts)

print("\n每一行True的占比：")
print(row_percentages)
```

输出将会有两个部分。第一部分是每一行中`True`的数量，即每行中除去第一列的`True`值的总数。第二部分是每一行中`True`的占比，即每行中除去第一列的`True`值的总数除以总列数。

注意，`sum()`方法的`axis`参数设置为`1`，表示按行进行求和。`df.iloc[:, 1:]`用于选择除去第一列的所有列，即从第二列开始计算。

另外，使用`df.shape[1]`可以获取DataFrame的总列数。这里假设第一列是索引列，所以通过`df.shape[1]`获取总列数减去1，即不包括索引列。

请注意，输出的结果是每一行的统计结果，其中每一行对应输入数据中的一行。

#### 写入数据

```python
# 写入excel
```



#### 去重

读取某一列后，使用`drop_duplicates()`方法

#### 其他

- 数组扁平化：`dataFrame.flatten()`，可以将数组降维

- 对一个dataFrame调用len()方法：

  在Pandas中，对DataFrame对象调用`len()`方法将返回DataFrame的行数。`len()`函数计算对象的长度，对于DataFrame对象，它返回的是行数。

  ```python
  import pandas as pd
  
  data = {'A': [1, 2, 3],
          'B': [4, 5, 6],
          'C': [7, 8, 9]}
  
  df = pd.DataFrame(data)
  
  length = len(df)
  print(length)
  ```

  在这个例子中，DataFrame `df`包含3行数据。通过对`df`调用`len()`方法，我们获得DataFrame的行数，输出结果为3。

  请注意，`len()`方法返回的是DataFrame的行数，并不包括列数。如果你想获取DataFrame的列数，可以使用`len(df.columns)`。

#### 行遍历



## sys

### `sys.path`

详细解释：[Python sys.path详解 ](https://www.jianshu.com/p/04701cb81e38)

```python
# test.py

import sys
from pkg_a import module_a


print(sys.path)
module_a.print_a()
```

![image-20230513160835773](image-20230513160835773.png)

进入`pkg_test`目录，直接执行`python pkg_b/test.py`

![image-20230513160951236](image-20230513160951236.png)

可以注释掉导包命令，看下`sys.path`

```python
# from pkg_a import module_a
import sys
print(sys.path)
# module_a.print_a()
```

![image-20230513162046133](image-20230513162046133.png)

是把当前脚本所在的路径，放入了`sys.path`，自然是找不到pkg_a这个兄弟的包的，而`python -m`允许将模块以脚本的形式运行，并且将当前目录加入到了`sys.path`中（父级目录），当然可以根据`/app/tag/utils/pkg_test`路径找到对应的模块

![image-20230513161705388](image-20230513161705388.png)

导入一个叫 mod1 的模块时，解释器先在当前目录中搜索名为 mod1.py 的文件。如果没有找到的话，接着会到 sys.path 变量中给出的目录列表中查找。 sys.path 变量的初始值来自如下：

- 输入脚本的目录（当前目录）。
- 环境变量 PYTHONPATH 表示的目录列表中搜索(这和 shell 变量 PATH 具有一样的语法，即一系列目录名的列表)。
- Python 默认安装路径中搜索。
   实际上，解释器由 sys.path 变量指定的路径目录搜索模块，该变量初始化时默认包含了输入脚本（或者当前目录）， PYTHONPATH 和安装目录。这样就允许 Python程序了解如何修改或替换模块搜索目录。

### `sys.path`写入

```python
print(type(sys.path)) # <class 'list'>
```

#### append

如果在当前目录执行，需要导入兄弟包中的模块

```python
import sys, os
sys.path.append(os.path.realpath('..'))

```







#### insert

### PYTHONPATH 与 sys.path的关系

```bash
(mumu-store-server-env) [~/vhost/nemu-statistics]$ echo $PYTHONPATH

(mumu-store-server-env) [~/vhost/nemu-statistics]$ python 
>>> import sys
>>> sys.path
['', '/home/lidongwei/.virtualenvs/mumu-store-server-env/lib/python2.7', '/home/lidongwei/.virtualenvs/mumu-store-server-env/lib/python2.7/plat-x86_64-linux-gnu', '/home/lidongwei/.virtualenvs/mumu-store-server-env/lib/python2.7/lib-tk', '/home/lidongwei/.virtualenvs/mumu-store-server-env/lib/python2.7/lib-old', '/home/lidongwei/.virtualenvs/mumu-store-server-env/lib/python2.7/lib-dynload', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/home/lidongwei/.virtualenvs/mumu-store-server-env/local/lib/python2.7/site-packages', '/home/lidongwei/.virtualenvs/mumu-store-server-env/lib/python2.7/site-packages']
```

默认情况下PYTHONPATH是空的， 然后进去看到sys.path是一个列表，包括有所有查找包的目录

下面我们给PYTHON加个目录

```bash
(mumu-store-server-env) [~/vhost/nemu-statistics]$ export PYTHONPATH=/home/lidongwei/Desktop 
(mumu-store-server-env) [~/vhost/nemu-statistics]$ python 
>>> import sys
>>> sys.path
['', '/home/lidongwei/Desktop', '/home/lidongwei/.virtualenvs/mumu-store-server-env/lib/python2.7', '/home/lidongwei/.virtualenvs/mumu-store-server-env/lib/python2.7/plat-x86_64-linux-gnu', '/home/lidongwei/.virtualenvs/mumu-store-server-env/lib/python2.7/lib-tk', '/home/lidongwei/.virtualenvs/mumu-store-server-env/lib/python2.7/lib-old', '/home/lidongwei/.virtualenvs/mumu-store-server-env/lib/python2.7/lib-dynload', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/home/lidongwei/.virtualenvs/mumu-store-server-env/local/lib/python2.7/site-packages', '/home/lidongwei/.virtualenvs/mumu-store-server-env/lib/python2.7/site-packages']
```

可以看到'`/home/lidongwei/Desktop`' 这个目录已经被加到sys.path了， 说明PYTHONPATH会加到sys.path

## 通用操作系统服务

### os -- 多种操作系统接口

> [os --- 多种操作系统接口 — Python 3.11.3 文档](https://docs.python.org/zh-cn/3/library/os.html#file-object-creation)

#### `os.walk`

`os.walk(top, topdown=True, onerror=None, followlinks=False)`

生成目录树中的文件名，方式是按上->下或下->上顺序浏览目录树。对于以 *top* 为根的目录树中的每个目录（包括 *top* 本身），它都会生成一个三元组 `(dirpath, dirnames, filenames)`。

*dirpath* is a string, the path to the directory. *dirnames* is a list of the names of the subdirectories in *dirpath* (including symlinks to directories, and excluding `'.'` and `'..'`). *filenames* is a list of the names of the non-directory files in *dirpath*. Note that the names in the lists contain no path components. To get a full path (which begins with *top*) to a file or directory in *dirpath*, do `os.path.join(dirpath, name)`. Whether or not the lists are sorted depends on the file system. If a file is removed from or added to the *dirpath* directory during generating the lists, whether a name for that file be included is unspecified.

如果可选参数 *topdown* 为 `True` 或未指定，则在所有子目录的三元组之前生成父目录的三元组（目录是自上而下生成的）。如果 *topdown* 为 `False`，则在所有子目录的三元组生成之后再生成父目录的三元组（目录是自下而上生成的）。无论 *topdown* 为何值，在生成目录及其子目录的元组之前，都将检索全部子目录列表。

当 *topdown* 为 `True` 时，调用者可以就地修改 *dirnames* 列表（也许用到了 [`del`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#del) 或切片），而 [`walk()`](https://docs.python.org/zh-cn/3/library/os.html#os.walk) 将仅仅递归到仍保留在 *dirnames* 中的子目录内。这可用于减少搜索、加入特定的访问顺序，甚至可在继续 [`walk()`](https://docs.python.org/zh-cn/3/library/os.html#os.walk) 之前告知 [`walk()`](https://docs.python.org/zh-cn/3/library/os.html#os.walk) 由调用者新建或重命名的目录的信息。当 *topdown* 为 `False` 时，修改 *dirnames* 对 walk 的行为没有影响，因为在自下而上模式中，*dirnames* 中的目录是在 *dirpath* 本身之前生成的。

默认将忽略 [`scandir()`](https://docs.python.org/zh-cn/3/library/os.html#os.scandir) 调用中的错误。如果指定了可选参数 *onerror*，它应该是一个函数。出错时它会被调用，参数是一个 [`OSError`](https://docs.python.org/zh-cn/3/library/exceptions.html#OSError) 实例。它可以报告错误然后继续遍历，或者抛出异常然后中止遍历。注意，可以从异常对象的 `filename` 属性中获取出错的文件名。

[`walk()`](https://docs.python.org/zh-cn/3/library/os.html#os.walk) 默认不会递归进指向目录的符号链接。可以在支持符号链接的系统上将 *followlinks* 设置为 `True`，以访问符号链接指向的目录。

> 备注
>
> 注意，如果链接指向自身的父目录，则将 *followlinks* 设置为 `True` 可能导致无限递归。[`walk()`](https://docs.python.org/zh-cn/3/library/os.html#os.walk) 不会记录它已经访问过的目录。
>
>  
>
> 如果传入的是相对路径，请不要在恢复 [`walk()`](https://docs.python.org/zh-cn/3/library/os.html#os.walk) 之间更改当前工作目录。[`walk()`](https://docs.python.org/zh-cn/3/library/os.html#os.walk) 不会更改当前目录，并假定其调用者也不会更改当前目录

返回值是一个可迭代对象

```python
import os
print(os.walk('/app/tag/utils/pkg_test'))
# <generator object walk at 0x7ff0562a0c80>
```

迭代打印返回值

```python
import os
# 
for root, dirs, files in os.walk('/app/tag/utils/pkg_test'):
    print(root)
    # 目标文件夹，以及所有的子文件夹
    # /app/tag/utils/pkg_test
    # /app/tag/utils/pkg_test/pkg_b
    # /app/tag/utils/pkg_test/pkg_b/__pycache__
    # /app/tag/utils/pkg_test/pkg_a
    # /app/tag/utils/pkg_test/pkg_a/__pycache__

    print(dirs)
    # 每个文件夹下，所拥有的子文件夹列表
    # ['pkg_b', 'pkg_a']
    # ['__pycache__']
    # []
    # ['__pycache__']
    # []
    print(files)
    # 每个文件夹下，所拥有的文件列表
    # []
    # ['test.py', '__init__.py']
    # ['__init__.cpython-38.pyc', 'test.cpython-38.pyc']
    # ['module_a.py', 'module_b.py', '__init__.py']
    # ['__init__.cpython-38.pyc', 'module_a.cpython-38.pyc']
    # for name in files:
    #     print(name, join(root, name))
    # print(dirs)
```

#### `os.mkdir`

https://blog.csdn.net/weixin_43781229/article/details/112424564

`os.mkdir(path, mode=0o777, *, dir_fd=None)`
创建一个名为 path 的目录，应用以数字表示的权限模式 mode。

创建一级目录，其参数path 为要创建目录的路径。



如果目录已经存在， FileExistsError 会被提出。如果路径中的父目录不存在，则会引发 FileNotFoundError 。

某些系统会忽略 mode。如果没有忽略它，那么将首先从它中减去当前的 umask 值。如果除最后 9 位（即 mode 八进制的最后 3 位）之外，还设置了其他位，则其他位的含义取决于各个平台。在某些平台上，它们会被忽略，应显式调用 chmod() 进行设置。

本函数支持 基于目录描述符的相对路径。

如果需要创建临时目录，请参阅 tempfile 模块中的 tempfile.mkdtemp() 函数。

引发一个 审计事件 os.mkdir，附带参数 path、mode、dir_fd。



创建目录前，通常需要判断该目录是否存在

```python
if not os.path.isdir(filename + "_dir"):
    os.mkdir(filename + "_dir")
```

#### `os.chdir`

`os.chdir(path)`

用于改变当前工作目录到指定的路径。

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

path = "/tmp"

# 查看当前工作目录
retval = os.getcwd()
print "当前工作目录为 %s" % retval

# 修改当前工作目录
os.chdir( path )

# 查看修改后的工作目录
retval = os.getcwd()

print "目录修改成功 %s" % retval
```

结果

```bash
当前工作目录为 /www
目录修改成功 /tmp
```

#### `os.listdir`

```python
# 获取文件夹内的文件和子文件夹名称
# 结果为列表

print(os.listdir('/app/tag/backup'))
# ['readme.md', '合同类数据汇总', '要素记录']
```

## 文件和目录访问

> [文件和目录访问 — Python 3.11.3 文档](https://docs.python.org/zh-cn/3/library/filesys.html)

### os.path -- 常用路径操作

> [os.path --- 常用路径操作 — Python 3.11.3 文档](https://docs.python.org/zh-cn/3/library/os.path.html#module-os.path)

- 将脚本所在父级目录添加到运行路径`os.path`中（要求：在子目录中运行，不要在添加后，跑到父级目录运行，这样加的路径也随着执行目录而变化）

  ```python
  import sys, os
  sys.path.append(os.path.realpath('..'))
  ```
  

#### `os.path.realpath`

`os.path.realpath(path, *, strict=False)`

- 传入相对路径，不传参或者传一个点`.`，结果是执行脚本时所在的实际路径

- 返回指定文件的规范路径，消除路径中存在的任何符号链接（如果操作系统支持）。

  如果一个路径不存在或是遇到了符号链接循环，并且 *strict* 为 `True`，则会引发 [`OSError`](https://docs.python.org/zh-cn/3/library/exceptions.html#OSError)。 如果 *strict* 为 `False`，则会尽可能地解析路径并添加结果而不检查路径是否存在。

  备注

  这个函数会模拟操作系统生成规范路径的过程，Windows 与 UNIX 的这个过程在处理链接和后续路径组成部分的交互方式上有所差异。

  操作系统 API 会根据需要来规范化路径，因此通常不需要调用此函数。

#### `os.path.relpath`

`os.path.relpath(path, start=os.curdir)`

- 传入绝对路径，返回相当于当前执行目录的一个绝对路径

- 返回从当前目录或可选的 *start* 目录至 *path* 的相对文件路径。 这只是一个路径计算：不会访问文件系统来确认 *path* 或 *start* 是否存在或其性质。 在 Windows 上，当 *path* 和 *start* 位于不同驱动器时将引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError)。

  *start* 默认为 [`os.curdir`](https://docs.python.org/zh-cn/3/library/os.html#os.curdir)。

  [可用性](https://docs.python.org/zh-cn/3/library/intro.html#availability): Unix, Windows。

#### `os.path.join`

`os.path.join(path, *paths)`

- Join one or more path segments intelligently. The return value is the concatenation of *path* and all members of **paths*, with exactly one directory separator following each non-empty part, except the last. That is, the result will only end in a separator if the last part is either empty or ends in a separator. If a segment is an absolute path (which on Windows requires both a drive and a root), then all previous segments are ignored and joining continues from the absolute path segment.

- On Windows, the drive is not reset when a rooted path segment (e.g., `r'\foo'`) is encountered. If a segment is on a different drive or is an absolute path, all previous segments are ignored and the drive is reset. Note that since there is a current directory for each drive, `os.path.join("c:", "foo")` represents a path relative to the current directory on drive `C:` (`c:foo`), not `c:\foo`.

- 连接两个或更多的路径名组件：https://blog.csdn.net/Ybc_csdn/article/details/124508003

  - 如果各组件名首字母不包含’/’，则函数会自动加上
  - 如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃
  - 如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾
  - 可以拼接路径，也可以拼接路径+文件

- demo01

  ```python
  import os
  
  Path1 = 'home'
  Path2 = 'develop'
  Path3 = 'code'
  
  Path10 = Path1 + Path2 + Path3
  Path20 = os.path.join(Path1,Path2,Path3)
  print ('Path10 = ',Path10) 
  print ('Path20 = ',Path20)
  
  # Path10 = homedevelopcode
  # Path20 = home/develop/code
  ```

- demo02

  ```python
  import os
  
  Path1 = '/home'
  Path2 = 'develop'
  Path3 = 'code'
  
  Path10 = Path1 + Path2 + Path3
  Path20 = os.path.join(Path1,Path2,Path3)
  print ('Path10 = ',Path10)
  print ('Path20 = ',Path20) 
  
  # Path10 = /homedevelopcode
  # Path20 = /home/develop/code
  
  ```

- demo03

  ```python
  import os
  
  Path1 = 'home'
  Path2 = '/develop'
  Path3 = 'code'
  
  Path10 = Path1 + Path2 + Path3
  Path20 = os.path.join(Path1,Path2,Path3)
  print ('Path10 = ',Path10)
  print ('Path20 = ',Path20) 
  
  # Path10 = home/developcode
  # Path20 = /develop/code
  
  ```

- demo04

  ```python
  import os
  
  Path1 = 'home'
  Path2 = 'develop'
  Path3 = '/code'
  
  Path10 = Path1 + Path2 + Path3
  Path20 = os.path.join(Path1,Path2,Path3)
  print ('Path10 = ',Path10)
  print ('Path20 = ',Path20 )
  
  # Path10 = homedevelop/code
  # Path20 = /code
  
  ```

- 实际应用

  ```python
  video_path = "./data/testvideo1.mp4"
  label_path = "./data/labels"
  file_name = "testvideo1"
  
  label_file_path = os.path.join(label_path, file_name + "_" + str(frame_counter) + ".txt")
  
  ```

  ![image-20230517103143570](image-20230517103143570.png)

#### `os.path.getsize`

`os.path.getsize()`

#### `os.path.basename`

`os.path.basename(path)`

- 返回路径 *path* 的基本名称。这是将 *path* 传入函数 [`split()`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.split) 之后，返回的一对值中的第二个元素。请注意，此函数的结果与Unix **basename** 程序不同。**basename** 在 `'/foo/bar/'` 上返回 `'bar'`，而 [`basename()`](https://docs.python.org/zh-cn/3/library/os.path.html#os.path.basename) 函数返回一个空字符串 (`''`)。

  ```python
  print(os.path.basename('/app/tag/utils/test.py')) # test.py
  print(os.path.basename('/app/tag/utils')) # utils
  print(os.path.basename('/app/tag/utils/')) # '' 空字符串
  ```


#### `os.path.isDir`

`os.path.isdir(path)`

如果 path 是 现有的 目录，则返回 True。本方法会跟踪符号链接，因此，对于同一路径，islink() 和 isdir() 都可能为 True。

### tempfile -- 生成临时文件和目录

>  https://blog.csdn.net/weixin_37926734/article/details/123563067
>
>  Python的`tempfile`模块是用来创建临时文件或者文件夹的跨平台工具。在大型数据处理项目中，有的处理结果是不需要向用户最终展示的，但是它们的应用又是贯穿项目始终的，在这种情况下，我们就需要使用`tempfile`模块来解决这种问题。



**创建临时目录**

**TemporaryDirectory**
TemporaryDirectory函数使用与mkdtemp()相同的规则安全地创建临时目录。生成的对象可以用作上下文管理器（这里给出示例）。完成上下文或销毁临时目录对象后，新创建的临时目录及其所有内容将从文件系统中删除。其调用格式如下所示：

```python
TemporaryDirectory(suffix=None, prefix=None, dir=None)
```

调用该函数后，创建的目录名可以从返回对象的name属性中检索到。当返回的对象作为上下文管理器时，该名称将被分配给with语句中as子句的目标。另外，可以通过调用cleanup()方法显式清理目标。

```python
with tempfile.TemporaryDirectory() as path:
        print(path) # linux默认是在/tmp/目录下生成，也可以在调用时指定相对路径
        images_from_path = convert_from_path(filename, output_folder = path)
```



### glob -- Unix风格路径名模式扩展

> https://blog.csdn.net/weixin_41261833/article/details/108069945
>
> https://docs.python.org/zh-cn/3/library/glob.html

`glob.glob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)`

用来查找`符合特定规则`的目录和文件，并将搜索的到的结果返回到一个列表中。使用这个模块最主要的原因就是，该模块`支持`几个特殊的`正则通配符`

![image-20230517091809067](image-20230517091809067.png)

- glob.glob()：返回符合匹配条件的所有文件的路径；
- glob.iglob()：返回一个迭代器对象，需要循环遍历获取每个元素，得到的也是符合匹配条件的所有文件的路径；
-  glob.escape()：escape可以忽略所有的特殊字符，就是星号、问号、中括号，用处不大；
- recursive=False：代表递归调用，与特殊通配符“**”一同使用，默认为False，False表示不递归调用，True表示递归调用；

#### glob()函数

```python
path1 = r"C:\Users\黄伟\Desktop\publish\os模块\test_shutil_a\[0-9].png"
glob.glob(path1)

path2 = r"C:\Users\黄伟\Desktop\publish\os模块\test_shutil_a\[0-9a-z].*"
glob.glob(path2)

```

![image-20230517094737440](image-20230517094737440.png)

#### iglob()函数

```python
path1 = r"C:\Users\黄伟\Desktop\publish\os模块\test_shutil_a\[0-9].png"
a = glob.iglob(path1)
for i in a:
    print(i)

```

![image-20230517095119812](image-20230517095119812.png)

#### escape()函数

通过下方两行代码的对比，可以看出escape()函数只是让`*`只表示它本来的意思，而不再具有通配符的作用。

```python
glob.glob('t*')
glob.escape('t*')

```

![image-20230517095340781](image-20230517095340781.png)

我们还需要注意一点，`os库`、`shutil库`、`glob库`是互补的，我们要善于发挥各自的优势，充分利用它们的优势，帮助我们快速的操作文件和文件夹。

### shutil -- 高阶文件操作

> https://docs.python.org/zh-cn/3/library/shutil.html#module-shutil

[`shutil`](https://docs.python.org/zh-cn/3.11/library/shutil.html#module-shutil) 模块提供了一系列对文件和文件集合的高阶操作。 特别是提供了一些支持文件拷贝和删除的函数。 对于单个文件的操作，请参阅 [`os`](https://docs.python.org/zh-cn/3.11/library/os.html#module-os) 模块。

> 警告
>
>  即便是高阶文件拷贝函数 ([`shutil.copy()`](https://docs.python.org/zh-cn/3.11/library/shutil.html#shutil.copy), [`shutil.copy2()`](https://docs.python.org/zh-cn/3.11/library/shutil.html#shutil.copy2)) 也无法拷贝所有的文件元数据。
>
> 在 POSIX 平台上，这意味着将丢失文件所有者和组以及 ACL 数据。 在 Mac OS 上，资源钩子和其他元数据不被使用。 这意味着将丢失这些资源并且文件类型和创建者代码将不正确。 在 Windows 上，将不会拷贝文件所有者、ACL 和替代数据流。

#### `shutil.copy`

复制文件

```python
#复制hello.txt到"C:\myweb\chapter02"目录下
>>> shutil.copy('hello.txt', r'C:\myweb\chapter02')
		
'C:\\myweb\\chapter02\\hello.txt'
 
#复制hello.txt到"C:\myweb\chapter02"目录并修改名称为hello_01.txt
>>> shutil.copy('hello.txt', r'C:\myweb\chapter02\hello_01.txt')
		    
'C:\\myweb\\chapter02\\hello_01.txt'
```

复制文件夹

```python
#复制"C:\myweb\chapter01"到"C:\myweb\chapter02"目录下
>>> shutil.copytree(r'C:\myweb\chapter01', r'C:\myweb\chapter02\chapter01')
		    
'C:\\myweb\\chapter02\\chapter01'
 
#复制"C:\myweb\chapter01"到"C:\myweb\chapter02"目录下并修改名称为chapter01_bak
>>> shutil.copytree(r'C:\myweb\chapter01', r'C:\myweb\chapter02\chapter01_bak')
		    
'C:\\myweb\\chapter02\\chapter01_bak'
```



## json

常见json格式

```
[{}, {}]
```

**读取**

将**文件对象**，读取成python对象，使用`load`

```
# 读取json文件
import json

infile = 'filename.txt'
with open(infile, 'r', encoding='utf-8') as fr:
        json_context = json.load(fr)
        print(json_context[0])
```

将**字符串**，读取成pytho对象，使用`loads`

```python
# 读取json文件
import json

infile = 'filename.txt'
with open(infile, 'r', encoding='utf-8') as fr:
        json_context = json.loads(fr.read())
        print(json_context[0])
```



**写入**



## memory_profiler

## reportlab

官方文档：https://docs.reportlab.com/reportlab/userguide/ch1_intro/





模块代码示例:https://vimsky.com/examples/detail/python-module-reportlab.platypus.html

1. [reportlab.platypus.Paragraph()](https://vimsky.com/examples/detail/python-method-reportlab.platypus.Paragraph.html) ，22个项目使用

2. [reportlab.platypus.Table()](https://vimsky.com/examples/detail/python-method-reportlab.platypus.Table.html) ，13个项目使用

3. [reportlab.platypus.TableStyle()](https://vimsky.com/examples/detail/python-method-reportlab.platypus.TableStyle.html) ，13个项目使用

4. [reportlab.platypus.Image()](https://vimsky.com/examples/detail/python-method-reportlab.platypus.Image.html) ，13个项目使用

5. [reportlab.platypus.SimpleDocTemplate()](https://vimsky.com/examples/detail/python-method-reportlab.platypus.SimpleDocTemplate.html) ，12个项目使用

6. [reportlab.platypus.Spacer()](https://vimsky.com/examples/detail/python-method-reportlab.platypus.Spacer.html) ，11个项目使用

7. [reportlab.platypus.PageBreak()](https://vimsky.com/examples/detail/python-method-reportlab.platypus.PageBreak.html) ，10个项目使用

8. [reportlab.platypus.Frame()](https://vimsky.com/examples/detail/python-method-reportlab.platypus.Frame.html) ，5个项目使用

### 基本用法

> https://blog.csdn.net/bocai_xiaodaidai/article/details/102820431
>
> https://blog.csdn.net/sixqingfeng/article/details/125141390
>
> [Python生成PDF：Reportlab的六种使用方式 - windfic - 博客园 (cnblogs.com)](https://www.cnblogs.com/windfic/archive/2023/03/02/17157841.html)

reportlab文档：https://www.reportlab.com/docs/reportlab-userguide.pdf

reportlab实例：https://www.programcreek.com/python/index/1920/reportlab.platypus

reportlab生成pdf文档的基本途径有三种：

1、利用reportlab.pdfgen.canvas模块

pdfgen包是生成PDF文档的最低级别接口。pdfgen程序本质上是将文档“绘制”到页面序列上的指令序列。对象的接口 提供绘画操作的是pdfgen画布。 画布应该被认为是一张白纸，纸上的点用笛卡尔坐标来标识 (X,Y)坐标，默认在页面的左下角有(0,0)原点。此外，默认情况下，第一个坐标x向右，第二个坐标y向上。

 

2、利用reportlab.platypus.Paragraph模块

Paragraph是最有用最方便的途径之一。就像word一样操作每个段落。它可以格式化任意的文本，并提供使用XML样式的内联字体样式和颜色变化标记。格式化文本的整体形状可以调整为右对齐、左对齐、不规则或居中。XML 标记甚至可以用来插入希腊字符或做下标。

 

3、使用RML标记语言

类似html语法一样编写RML文档。



可以先看第二种

#### reportlab.pdfgen.canvas

> https://zhuanlan.zhihu.com/p/157097813

ReportLab是一个非常强大的库。 稍加努力，您几乎可以想到任何布局。 多年来，我一直使用它来复制许多复杂的页面布局。在本文中，我们将学习如何使用ReportLab的pdfgen软件包。

pdfgen软件包的级别很低。 您将在画布上绘画或“涂画”以创建PDF。 画布是从pdfgen包中导入的。 当您在画布上绘画时，您将需要指定X / Y坐标，以告诉ReportLab从哪里开始绘画。 默认值为（0,0），其原点位于页面的左下角。 许多桌面用户界面工具包，例如wxPython，Tkinter等，也具有此概念。 您也可以使用X / Y坐标将按钮绝对放置在许多工具包中。 这样可以非常精确地放置要添加到页面中的元素。

我需要提及的另一项内容是，当您在PDF中放置某项时，是根据您从原点开始的点数进行定位。 它是点，而不是像素，毫米或英寸。 点！ 让我们来看看一个字母大小的页面上有多少个点：

```python
>>> from reportlab.lib.pagesizes import letter
>>> letter
(612.0, 792.0)
```

在这里，我们了解到一个letter宽612点，高792点。 （letter是美国的版面大小约定）让我们找出英寸和毫米分别有多少个点：（这些在`reportlab.lib.pagesizes.py` 以及同级的`units.py`文件中定义）

```python
>>> from reportlab.lib.units import inch
>>> inch
72.0
>>> from reportlab.lib.units import mm
>>> mm
2.834645669291339
```

![image-20230516142252582](image-20230516142252582.png)

这些信息将帮助我们将图纸放置在您的画上。 至此，我们已经准备好创建PDF！



canvas对象位于pdfgen包中。 让我们导入它并绘制一些文本：

```python
# hello_reportlab.py

# 导入canvas对象
from reportlab.pdfgen import canvas

# 实例化Canvas对象
c = canvas.Canvas('hello.pdf')
c.drawString(100, 100, 'Welcome to Reportlab!')

# 保存画布的当前页面
c.showPage()
# 将文档保存到磁盘
c.save()
```

在此示例中，我们导入canvas对象，然后实例化Canvas对象。 您会注意到，唯一的要求参数是文件名或路径。 接下来，我们在画布对象上调用drawString（），并告诉它开始在原点右边100点向上100点绘制字符串。 之后，我们调用showPage（）方法。 showPage（）方法将保存画布的当前页面。 实际上不是必需的，但建议使用。 showPage（）方法也会结束当前页面。 如果在调用showPage（）之后绘制另一个字符串或其他元素，则该对象将被绘制到新页面。 最后，我们调用canvas对象的save（）方法，该方法将文档保存到磁盘。 现在我们可以打开它，看看我们的PDF是什么样的：

![image-20230516143702856](image-20230516143702856.png)

您可能会注意到，我们的文字位于文档底部附近。 原因是原点（0,0）是文档的左下角。 因此，当我们告诉ReportLab绘制文本时，我们是在告诉它从左侧开始绘制100点，从底部开始绘制100点。 这与在Tkinter或wxPython中创建用户界面（左上角是起源）形成对比。

另请注意，由于我们未指定页面大小，因此默认使用ReportLab配置中的默认大小，通常为A4。 在reportlab.lib.pagesizes中可以找到一些常见的页面大小。

让我们看一下Canvas的构造函数，以了解其对参数的要求（现在已经不止这么多了）：

```python
def __init__(self,filename,
             pagesize=None,
             bottomup = 1,
             pageCompression=None,
             invariant = None,
             verbosity=0,
             encrypt=None,
             cropMarks=None,
             pdfVersion=None,
             enforceColorSpace=None,
             ):
```

在这里，我们可以看到可以将pagesize作为参数传递。 pagesize实际上是一个以点为单位的宽度和高度的元组。 

![image-20230516144437935](image-20230516144437935.png)

如果要从默认的左下角更改原点，则可以将bottomup参数设置为0，这会将原点更改为左上角。

pageCompression参数默认为零或关闭。 基本上，它将告诉ReportLab是否压缩每个页面。 启用压缩后，文件生成过程会变慢。 如果您的工作需要尽快生成PDF，则需要将默认值保持为零。 但是，如果不关心速度，并且您想使用更少的磁盘空间，则可以打开页面压缩。 请注意，PDF中的图像将始终被压缩，因此打开页面压缩的主要用例是每页上有大量文本或大量矢量图形时。

ReportLab的《用户指南》没有提及不变参数`invariant`的用途，因此我看了一下源代码。 根据消息来源，它会产生具有相同时间戳信息的可重复的相同PDF（用于回归测试）。 我从未见过有人在他们的代码中使用此参数，并且由于消息人士说该参数用于回归测试，所以我认为我们可以放心地忽略它。

下一个参数是详细程度`verbosity`，用于记录级别。 Zero（0），ReportLab将允许其他应用程序从标准输出中捕获PDF。 如果将其设置为一（1），则每次创建PDF时都会打印出一条确认消息。 可能添加了其他级别，但是在撰写本文时，这是仅有的两个文档。



> https://blog.csdn.net/weixin_48923393/article/details/129173640

**创建 PDF 文档**

```python
from reportlab.pdfgen import canvas

pdf_name = "my_tech_article.pdf"
pdf = canvas.Canvas(pdf_name)
```

**添加文本**

前两个参数是文本的x和y坐标，第三个参数是文本内容。

```python
pdf.drawString(50, 750, "My Technical Article")
```

**添加图像**

前三个参数是图像路径或名称、x和y坐标，第四个参数是图像的宽度，第五个参数是图像的高度。

```python
from reportlab.lib.pagesizes import letter
 
pdf.drawImage("my_image.png", 50, 650, width=letter[0], height=letter[1]/2)
```

**添加表格**

```python
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table
 
data = [    ["Name", "Age", "Gender"],
    ["John", "25", "Male"],
    ["Sarah", "30", "Female"],
    ["Tom", "35", "Male"],
]
 
table = Table(data)
table.setStyle(
    [
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 14),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
        ("ALIGN", (0, 1), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]
)
```

其它内容自行翻阅官方文档

#### reportlab.platypus.Paragraph

以下仅仅展示了最常用的样式，更多丰富的样式如：目录、页眉页脚、表格、图形等等需后续学习。

示例代碼一：

这份代码没有做封装

```python
import tempfile
 
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, LongTable, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from io import BytesIO
 
pdfmetrics.registerFont(TTFont('SimSun', './SimSun.ttf'))  # 默认不支持中文，需要注册字体
pdfmetrics.registerFont(TTFont('SimSunBd', './SimSun-bold.ttf'))
# registerFontFamily('SimSun', normal='SimSun', bold='SimSunBd', italic='VeraIt', boldItalic='VeraBI')
 
stylesheet = getSampleStyleSheet()   # 获取样式集
 
# 获取reportlab自带样式
Normal = stylesheet['Normal']
BodyText = stylesheet['BodyText']
Italic = stylesheet['Italic']
Title = stylesheet['Title']
Heading1 = stylesheet['Heading1']
Heading2 = stylesheet['Heading2']
Heading3 = stylesheet['Heading3']
Heading4 = stylesheet['Heading4']
Heading5 = stylesheet['Heading5']
Heading6 = stylesheet['Heading6']
Bullet = stylesheet['Bullet']
Definition = stylesheet['Definition']
Code = stylesheet['Code']
 
# 自带样式不支持中文，需要设置中文字体，但有些样式会丢失，如斜体Italic。有待后续发现完全兼容的中文字体
Normal.fontName = 'SimSun'
Italic.fontName = 'SimSun'
BodyText.fontName = 'SimSun'
Title.fontName = 'SimSunBd'
Heading1.fontName = 'SimSun'
Heading2.fontName = 'SimSun'
Heading3.fontName = 'SimSun'
Heading4.fontName = 'SimSun'
Heading5.fontName = 'SimSun'
Heading6.fontName = 'SimSun'
Bullet.fontName = 'SimSun'
Definition.fontName = 'SimSun'
Code.fontName = 'SimSun'
 
 
# 添加自定义样式
stylesheet.add(
    ParagraphStyle(name='body',
                   fontName="SimSun",
                   fontSize=10,
                   textColor='black',
                   leading=20,                # 行间距
                   spaceBefore=0,             # 段前间距
                   spaceAfter=10,             # 段后间距
                   leftIndent=0,              # 左缩进
                   rightIndent=0,             # 右缩进
                   firstLineIndent=20,        # 首行缩进，每个汉字为10
                   alignment=TA_JUSTIFY,      # 对齐方式
 
                   # bulletFontSize=15,       #bullet为项目符号相关的设置
                   # bulletIndent=-50,
                   # bulletAnchor='start',
                   # bulletFontName='Symbol'
                   )
            )
body = stylesheet['body']
 
 
story = []
 
# 段落
content1 = "<para><u color='red'><font fontSize=13>区块链</font></u>是分布式数据存储、<strike color='red'>点对点传输</strike>、共识机制、" \
          "<font color='red' fontSize=13>加密算法</font>等计算机技术的<font name='SimSunBd'>新型应用模式</font>。<br/>" \
          "&nbsp&nbsp<a href='www.baidu.com' color='blue'>区块链（Blockchain）</a>，" \
          "是比特币的一个重要概念，它本质上是一个去中心化的数据库，同时作为比特币的底层技术，是一串使用密码学方法相关联产生的" \
          "数据块，每一个数据块中包含了一批次比特币网络交易的信息，用于验证其信息的有效性（防伪）和生成下一个区块 [1]。</para>"
 
content2 = "区块链起源于比特币，2008年11月1日，一位自称中本聪(SatoshiNakamoto)的人发表了《比特币:一种点对点的电子现金系统》" \
           "一文 [2]  ，阐述了基于P2P网络技术、加密技术、时间戳技术、区块链技术等的电子现金系统的构架理念，这标志着比特币的诞生" \
           "。两个月后理论步入实践，2009年1月3日第一个序号为0的创世区块诞生。几天后2009年1月9日出现序号为1的区块，并与序号为" \
           "0的创世区块相连接形成了链，标志着区块链的诞生 [5]  。<br/><img src='./1.jpg' width=180 height=100 valign='top'/><br/><br/><br/><br/><br/>"
 
content3 = "2008年由中本聪第一次提出了区块链的概念 [2]  ，在随后的几年中，区块链成为了电子货币比特币" \
           "的核心组成部分：作为所有交易的公共账簿。通过利用点对点网络和分布式时间戳服务器，区块链数据库能够进行自主管理。为比特币而发明的区块链使它成为" \
           "第一个解决重复消费问题的数字货币。比特币的设计已经成为其他应用程序的灵感来源。<br/>&nbsp&nbsp 2014年，区块链2.0成为一个关于去中心" \
           "化区块链数据库的术语。对这个第二代可编程区块链，经济学家们认为它是一种编程语言，可以允许用户写出更精密和智能的协议 " \
           "[7]  。因此，当利润达到一定程度的时候，就能够从完成的货运订单或者共享证书的分红中获得收益。区块链2.0技术跳过了交易" \
           "和“价值交换中担任金钱和信息仲裁的中介机构”。它们被用来使人们远离全球化经济，使隐私得到保护，使人们“将掌握的信息兑换" \
           "成货币”，并且有能力保证知识产权的所有者得到收益。第二代区块链技术使存储个人的“永久数字ID和形象”成为可能，并且对“潜在" \
           "的社会财富分配”不平等提供解决方案 [8]  。<br/>&nbsp&nbsp 2016年1月20日，中国人民银行数字货币研讨会宣布对数字货币研究取得阶段性成果。" \
           "会议肯定了数字货币在降低传统货币发行等方面的价值，并表示央行在探索发行数字货币。中国人民银行数字货币研讨会的表达大大" \
           "增强了数字货币行业信心。这是继2013年12月5日央行五部委发布关于防范比特币风险的通知之后，第一次对数字货币表示明确的态度" \
           "。 [9] <br/>&nbsp&nbsp 2016年12月20日，数字货币联盟——中国FinTech数字货币联盟及FinTech研究院正式筹建 [10]  。<br/>&nbsp&nbsp如今，比特币仍是" \
           "数字货币的绝对主流，数字货币呈现了百花齐放的状态，常见的有bitcoin、litecoin、dogecoin、dashcoin，除了货币的应用" \
           "之外，还有各种衍生应用，如以太坊Ethereum、Asch等底层应用开发平台以及NXT，SIA，比特股，MaidSafe，Ripple等行业应用 [11]  。"
 
 
# Table 表格
 
image = Image('./1.jpg')
image.drawWidth = 160
image.drawHeight = 100
table_data = [['year我是标题行，\n\n比较特殊，不能上下居中\n', '我的背景色被绿了', '我是标题，我比别人大\n'],
              ['2017\n我是换行符，\n单元格中的字符串只能用我换行', '3', '12'],
              [Paragraph('指定了列宽，可以在单元格中嵌入paragraph进行自动换行，不信你看我', body), '4', '13'],
              ['2017', '5', '我们是表格'],
              ['2017', '我是伪拆分单元格，\n通过合并前hou两个兄弟得到', '15'],
              ['2018', '7', '16'],
              [Paragraph(content1, body), '8', [image, Paragraph('这样我可以在一个单元格内同时显示图片和paragraph', body)]],
              ['2018', '我们被合并了，合并的值为右上角单元格的值', '18'],
              ['我被绿了', '10', '19'],
              ]
table_style = [
    ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),  # 字体
    ('FONTSIZE', (0, 0), (-1, 0), 15),  # 第一行的字体大小
    ('FONTSIZE', (0, 1), (-1, -1), 10),  # 第二行到最后一行的字体大小
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 所有表格左右中间对齐
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐
 
    ('SPAN', (-2, -2), (-1, -1)),  # 合并
    ('SPAN', (0, 4), (0, 5)),  # 合并
    ('SPAN', (2, 4), (2, 5)),  # 合并
    ('BACKGROUND', (0, 0), (-1, 0), colors.green),  # 设置第一行背景颜色
    ('TEXTCOLOR', (0, -1), (0, -1), colors.green),  # 设置表格内文字颜色
    ('GRID', (0, 0), (-1, -1), 0.1, colors.black),  # 设置表格框线为灰色，线宽为0.1
]
table = Table(data=table_data, style=table_style, colWidths=180)
 
 
story.append(Paragraph("区块链", Title))
story.append(Paragraph("<seq id='spam'/>.区块链概念", Heading2))
story.append(Paragraph(content1, body))
story.append(Paragraph("<seq id='spam'/>.区块链起源", Heading2))
story.append(Paragraph(content2, body))
story.append(Paragraph("<seq id='spam'/>.区块链发展历程", Heading2))
story.append(Paragraph(content3, body))
story.append(table)
 
# bytes
# buf = BytesIO()
# doc = SimpleDocTemplate(buf, encoding='UTF-8')
# doc.build(story)
# print(buf.getvalue().decode())
 
# file
doc = SimpleDocTemplate('hello.pdf')
doc.build(story)
```

Tips: simsun就是宋体

[simsun字体下载](https://www.onlinedown.net/soft/10033540.htm)

[宋体粗体 Version 3.03 Font Download-TTF](https://eng.m.fontke.com/font/23023735/download/)

示例代码二：

这份代码作了封装，看上去较为清晰

```python
from reportlab.pdfbase import pdfmetrics   # 注册字体
from reportlab.pdfbase.ttfonts import TTFont  # 字体类
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Image  # 报告内容相关类
from reportlab.lib.pagesizes import letter  # 页面的标志尺寸(8.5*inch, 11*inch)
from reportlab.lib.styles import getSampleStyleSheet  # 文本样式
from reportlab.lib import colors  # 颜色模块
from reportlab.graphics.charts.barcharts import VerticalBarChart  # 图表类
from reportlab.graphics.charts.legends import Legend  # 图例类
from reportlab.graphics.shapes import Drawing  # 绘图工具
from reportlab.lib.units import cm  # 单位：cm

# 注册字体(提前准备好字体文件, 如果同一个文件需要多种字体可以注册多个)
pdfmetrics.registerFont(TTFont('SimSun', './SimSun.ttf'))


class Graphs:
    # 绘制标题
    @staticmethod
    def draw_title(title: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 拿到标题样式
        ct = style['Heading1']
        # 单独设置样式相关属性
        ct.fontName = 'SimSun'      # 字体名
        ct.fontSize = 18            # 字体大小
        ct.leading = 50             # 行间距
        ct.textColor = colors.green     # 字体颜色
        ct.alignment = 1    # 居中
        ct.bold = True
        # 创建标题对应的段落，并且返回
        return Paragraph(title, ct)

  # 绘制小标题
    @staticmethod
    def draw_little_title(title: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 拿到标题样式
        ct = style['Normal']
        # 单独设置样式相关属性
        ct.fontName = 'SimSun'  # 字体名
        ct.fontSize = 15  # 字体大小
        ct.leading = 30  # 行间距
        ct.textColor = colors.red  # 字体颜色
        # 创建标题对应的段落，并且返回
        return Paragraph(title, ct)

    # 绘制普通段落内容
    @staticmethod
    def draw_text(text: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 获取普通样式
        ct = style['Normal']
        ct.fontName = 'SimSun'
        ct.fontSize = 12
        ct.wordWrap = 'CJK'     # 设置自动换行
        ct.alignment = 2        # 左对齐
        ct.firstLineIndent = 32     # 第一行开头空格
        ct.leading = 25
        return Paragraph(text, ct)

    # 绘制表格
    @staticmethod
    def draw_table(*args):
        # 列宽度
        col_width = 120
        style = [
            ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),  # 字体
            ('FONTSIZE', (0, 0), (-1, 0), 12),  # 第一行的字体大小
            ('FONTSIZE', (0, 1), (-1, -1), 10),  # 第二行到最后一行的字体大小
            ('BACKGROUND', (0, 0), (-1, 0), '#d5dae6'),  # 设置第一行背景颜色
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 第一行水平居中
            ('ALIGN', (0, 1), (-1, -1), 'LEFT'),  # 第二行到最后一行左右左对齐
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.darkslategray),  # 设置表格内文字颜色
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # 设置表格框线为grey色，线宽为0.5
            # ('SPAN', (0, 1), (0, 2)),  # 合并第一列二三行
            # ('SPAN', (0, 3), (0, 4)),  # 合并第一列三四行
            # ('SPAN', (0, 5), (0, 6)),  # 合并第一列五六行
            # ('SPAN', (0, 7), (0, 8)),  # 合并第一列五六行
        ]
        table = Table(args, colWidths=col_width, style=style)
        return table

    # 创建图表
    @staticmethod
    def draw_bar(bar_data: list, ax: list, items: list):
        drawing = Drawing(500, 250)
        bc = VerticalBarChart()
        bc.x = 45       # 整个图表的x坐标
        bc.y = 45      # 整个图表的y坐标
        bc.height = 200     # 图表的高度
        bc.width = 350      # 图表的宽度
        bc.data = bar_data
        bc.strokeColor = colors.black       # 顶部和右边轴线的颜色
        bc.valueAxis.valueMin = 5000           # 设置y坐标的最小值
        bc.valueAxis.valueMax = 26000         # 设置y坐标的最大值
        bc.valueAxis.valueStep = 2000         # 设置y坐标的步长
        bc.categoryAxis.labels.dx = 2
        bc.categoryAxis.labels.dy = -8
        bc.categoryAxis.labels.angle = 20
        bc.categoryAxis.categoryNames = ax

        # 图示
        leg = Legend()
        leg.fontName = 'SimSun'
        leg.alignment = 'right'
        leg.boxAnchor = 'ne'
        leg.x = 475         # 图例的x坐标
        leg.y = 240
        leg.dxTextSpace = 10
        leg.columnMaximum = 3
        leg.colorNamePairs = items
        drawing.add(leg)
        drawing.add(bc)
        return drawing

    # 绘制图片
    @staticmethod
    def draw_img(path):
        img = Image(path)       # 读取指定路径下的图片
        img.drawWidth = 5*cm        # 设置图片的宽度
        img.drawHeight = 8*cm       # 设置图片的高度
        return img


if __name__ == '__main__':
    # 创建内容对应的空列表
    content = list()

    # 添加标题
    content.append(Graphs.draw_title('数据分析就业薪资'))

    # 添加图片
    content.append(Graphs.draw_img('./png/1.png'))

    # 添加段落文字
    content.append(Graphs.draw_text(
        '众所周知，大数据分析师岗位是香饽饽，近几年数据分析热席卷了整个互联网行业，与数据分析的相关的岗位招聘、培训数不胜数。很多人前赴后继，想要参与到这波红利当中。那么数据分析师就业前景到底怎么样呢？'))
    content.append(Graphs.draw_text(
        '甲方<div style="margin-right:10">乙方</div>'
    ))
    # 添加小标题
    content.append(Graphs.draw_title(''))
    content.append(Graphs.draw_little_title('不同级别的平均薪资'))
    # 添加表格
    data = [
        ('职位名称', '平均薪资', '较上年增长率'),
        ('数据分析师', '18.5K', '25%'),
        ('高级数据分析师', '25.5K', '14%'),
        ('资深数据分析师', '29.3K', '10%')
    ]
    content.append(Graphs.draw_table(*data))

    # 生成图表
    content.append(Graphs.draw_title(''))
    content.append(Graphs.draw_little_title('热门城市的就业情况'))
    b_data = [(25400, 12900, 20100, 20300, 20300, 17400),
              (15800, 9700, 12982, 9283, 13900, 7623)]
    ax_data = ['BeiJing', 'ChengDu', 'ShenZhen',
               'ShangHai', 'HangZhou', 'NanJing']
    leg_items = [(colors.red, '平均薪资'), (colors.green, '招聘量')]
    content.append(Graphs.draw_bar(b_data, ax_data, leg_items))

    # 生成pdf文件
    doc = SimpleDocTemplate('report.pdf', pagesize=letter)
    doc.build(content)

```



##### 内容左右显示

> https://www.jianshu.com/p/c5035e5e0296

在reportlab中可以使用**SimpleDocTemplate**创建一个文档，然后向里面添加内容，但是直接添加内容只能将值上下显示，如果要将内容左右显示的话，可以使用reportlab中*BalancedColumns*，它可以将内容分割成两个或者更多大小相等的列。（实际未使用，不清楚api怎么用，这个样例不全）

分列显示的内容，可以是表格、图表、文字等
只是这样将内容分列，内容上面的显示仍然不是特别的灵活。

```python
from reportlab.platypus.flowables import BalancedColumns
from reportlab.platypus.frames import ShowBoundaryValue
mytable = [[1,2,3,4],[5,6,7]]#按照这个格式填写
img_activity=Image('./image/**.png')
F = [ mytable, img_activity]#在该列表中填写需要分列展示的内容
story.append(
 Balanced(
 F, #the flowables we are balancing
 nCols = 2, #the number of columns
 needed = 72,#the minimum space needed by the flowable
 spacBefore = 0,
 spaceAfter = 0,
 showBoundary = None, #optional boundary showing
leftPadding=None, #these override the created frame
 rightPadding=None, #paddings if specified else the
 topPadding=None, #default frame paddings
 bottomPadding=None, #are used
 innerPadding=None, #the gap between frames if specified else
 #use max(leftPadding,rightPadding)
 name='', #for identification purposes when stuff goes awry
 endSlack=0.1, #height disparity allowance ie 10% of available height
 )
 )
```

![image-20230515112000081](image-20230515112000081.png)

也可以直接用画表格的形式，设置边框为透明，并设置列宽，若需要换行，添加`\n`

以下为实际工作中的需求，随机生成合同左右两列的pdf数据

![image-20230516111131215](image-20230516111131215.png)

```python
import json
from faker import Faker
import random
import string
from reportlab.pdfbase import pdfmetrics   # 注册字体
from reportlab.pdfbase.ttfonts import TTFont  # 字体类
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Image  # 报告内容相关类
from reportlab.lib.pagesizes import letter  # 页面的标志尺寸(8.5*inch, 11*inch)
from reportlab.lib.styles import getSampleStyleSheet  # 文本样式
from reportlab.lib import colors  # 颜色模块
from reportlab.graphics.charts.barcharts import VerticalBarChart  # 图表类
from reportlab.graphics.charts.legends import Legend  # 图例类
from reportlab.graphics.shapes import Drawing  # 绘图工具
from reportlab.lib.units import cm  # 单位：cm

# 随机生成传真


def generate_fax():
    fax = '+' + str(random.randint(80, 89)) + '-' + \
        str(random.randint(1000000, 9999999))
    return fax


print(generate_fax())
# 随机生成企业名称


def generate_company_name():
    prefix = ['ABC', 'XYZ', 'ACME', 'BEST', 'TOP']
    suffix = ['Corp', 'Inc', 'Ltd', 'LLC']
    return random.choice(prefix) + ' ' + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + ' ' + random.choice(suffix)

# 随机生成统一社会信用代码


def generate_credit_code():
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(18))

# 示例输出
# company_name = generate_company_name()
# credit_code = generate_credit_code()
# print("企业名称：", company_name)
# print("统一社会信用代码：", credit_code)


def addWrap(string, index=18):
    string = str(string)
    return string[:index] + '\n' + string[index:]


# res =  addWrap('sodifhweoifweojfjwepfjwepof')
# print(res)
faker = Faker('zh-CN')
# 注册字体(提前准备好字体文件, 如果同一个文件需要多种字体可以注册多个)
pdfmetrics.registerFont(TTFont('SimSun', './SimSun.ttf'))


class Graphs:
    # 绘制标题
    @staticmethod
    def draw_title(title: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 拿到标题样式
        ct = style['Heading1']
        # 单独设置样式相关属性
        ct.fontName = 'SimSun'      # 字体名
        ct.fontSize = 18            # 字体大小
        ct.leading = 50             # 行间距
        ct.textColor = colors.green     # 字体颜色
        ct.alignment = 1    # 居中
        ct.bold = True
        # 创建标题对应的段落，并且返回
        return Paragraph(title, ct)

  # 绘制小标题
    @staticmethod
    def draw_little_title(title: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 拿到标题样式
        ct = style['Normal']
        # 单独设置样式相关属性
        ct.fontName = 'SimSun'  # 字体名
        ct.fontSize = 15  # 字体大小
        ct.leading = 30  # 行间距
        ct.textColor = colors.red  # 字体颜色
        # 创建标题对应的段落，并且返回
        return Paragraph(title, ct)

    # 绘制普通段落内容
    @staticmethod
    def draw_text(text: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 获取普通样式
        ct = style['Normal']
        ct.fontName = 'SimSun'
        ct.fontSize = 12
        ct.wordWrap = 'CJK'     # 设置自动换行
        ct.alignment = 0        # 左对齐
        ct.firstLineIndent = 25     # 第一行开头空格
        ct.leading = 25
        return Paragraph(text, ct)

    # 绘制表格
    @staticmethod
    def draw_table(*args):
        # 列宽度
        col_width = (20, 240, 240)
        style = [
            ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),  # 字体
            ('FONTSIZE', (0, 0), (-1, 0), 12),  # 第一行的字体大小
            ('FONTSIZE', (0, 1), (-1, -1), 12),  # 第二行到最后一行的字体大小
            # ('BACKGROUND', (0, 0), (-1, 0), '#d5dae6'),  # 设置第一行背景颜色
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # 第一行水平居中 CENTER
            ('ALIGN', (0, 1), (-1, -1), 'LEFT'),  # 第二行到最后一行左右左对齐
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),  # 所有表格上下居中对齐
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),  # 设置表格内文字颜色
            # ('BOX', (0, 0), (-1, -1), 0.5, colors.grey),  # 设置表格框线为grey色，线宽为0.5 GRID
            # 设置表格框线为grey色，线宽为0.5 GRID
            ('BOX', (0, 0), (-1, -1), 0.5, colors.transparent),
            # ('SPAN', (0, 1), (0, 2)),  # 合并第一列二三行
            # ('SPAN', (0, 3), (0, 4)),  # 合并第一列三四行
            # ('SPAN', (0, 5), (0, 6)),  # 合并第一列五六行
            # ('SPAN', (0, 7), (0, 8)),  # 合并第一列五六行
        ]
        table = Table(args, colWidths=col_width, style=style)
        return table

    # 创建图表
    @staticmethod
    def draw_bar(bar_data: list, ax: list, items: list):
        drawing = Drawing(500, 250)
        bc = VerticalBarChart()
        bc.x = 45       # 整个图表的x坐标
        bc.y = 45      # 整个图表的y坐标
        bc.height = 200     # 图表的高度
        bc.width = 350      # 图表的宽度
        bc.data = bar_data
        bc.strokeColor = colors.black       # 顶部和右边轴线的颜色
        bc.valueAxis.valueMin = 5000           # 设置y坐标的最小值
        bc.valueAxis.valueMax = 26000         # 设置y坐标的最大值
        bc.valueAxis.valueStep = 2000         # 设置y坐标的步长
        bc.categoryAxis.labels.dx = 2
        bc.categoryAxis.labels.dy = -8
        bc.categoryAxis.labels.angle = 20
        bc.categoryAxis.categoryNames = ax

        # 图示
        leg = Legend()
        leg.fontName = 'SimSun'
        leg.alignment = 'right'
        leg.boxAnchor = 'ne'
        leg.x = 475         # 图例的x坐标
        leg.y = 240
        leg.dxTextSpace = 10
        leg.columnMaximum = 3
        leg.colorNamePairs = items
        drawing.add(leg)
        drawing.add(bc)
        return drawing

    # 绘制图片
    @staticmethod
    def draw_img(path):
        img = Image(path)       # 读取指定路径下的图片
        img.drawWidth = 5*cm        # 设置图片的宽度
        img.drawHeight = 8*cm       # 设置图片的高度
        return img


if __name__ == '__main__':
    # 创建内容对应的空列表
    content = list()

    with open('./config.json', 'r', encoding='utf-8') as fr:
        config = json.loads(fr.read())

        # 添加标题
        # 添加图片
        for i in range(500):
            # 添加段落文字
            content.append(Graphs.draw_text(faker.text(max_nb_chars=250)))

            content.append(Graphs.draw_text(faker.text(max_nb_chars=100)))
            random_data = [
                ('', '地址：' + addWrap(faker.address()),
                 '地址：' + addWrap(faker.address())),
                ('', '电话：' + addWrap(faker.phone_number()),
                 '电话：' + addWrap(faker.phone_number())),
                ('', '传真：' + addWrap(generate_fax()),
                 '传真：' + addWrap(generate_fax())),
                ('', '电子信箱：' + addWrap(faker.free_email(), index=25),
                 '电子信箱：' + addWrap(faker.free_email(), index=25)),
            ]

            random_sample = random.sample(random_data, random.randint(0, 3))

            table_data = [
                ('', '甲方：' + addWrap(faker.company()),
                 '乙方：' + addWrap(faker.company())),
                ('', '发包人（公章）：', '承包人（公章）：'),
                ('', '法定代表人（签字）：' + addWrap(faker.name()),
                 '法定代表人（签字）：' + addWrap(faker.name())),
                ('', '统一社会信用代码：' + addWrap(generate_credit_code()),
                 '统一社会信用代码：' + addWrap(generate_credit_code())),
                ('', '开户银行：' + addWrap(config['bank_name'][random.randint(0, 46)], index=13),
                 '开户银行：' + addWrap(config['bank_name'][random.randint(0, 46)], index=13)),
                ('', '账号：' + addWrap(faker.credit_card_number(card_type=None), index=20),
                 '账号：' + addWrap(faker.credit_card_number(card_type=None), index=20)),
            ]
            table_data[4:4] = random_sample # 合并两个列表元素
            content.append(Graphs.draw_table(*table_data))

            # 生成pdf文件
            doc = SimpleDocTemplate(
                './pdf_result/' + str(i) + '.pdf', pagesize=letter)

            # 随机content中3段的位置
            random.shuffle(content)
            doc.build(content)

```



## paddleocr



## pdf2image

> https://www.cnpython.com/pypi/pdf2image#description

## pydoc

在网页中生成注释文档

一定要cd到文件所在文件夹

输入指令：python3 -m pydoc -h                            查看注释文档的生成方法

输入指令：python3 -m pydoc -k 关键字                检索含有关键字的模块

输入指令： python3 -m pydoc -p 1233                  python3为版本，1233为指定端口

输入指令： python3 -m pydoc -b                          相比于-p，不用写端口，自动寻找闲置端口

输入指令： python3 -m pydoc -w  文件名



文件名不用加.py后缀，生成html文件，可以右键文件在浏览器打开




![image-20230513170359951](image-20230513170359951.png)





# 函数专题

## apply()

[python数据分析技巧篇-apply高级函数](https://zhuanlan.zhihu.com/p/444575338)

```bash
DataFrame.apply(func: 'AggFuncType', axis: 'Axis' = 0,raw: 'bool' = False,result_type=None,args=(),**kwargs)
```





# 数据获取

> 见爬虫篇



# 数据处理

> 存在key-value的数据，无论是啥格式，第一步优先处理成json格式

## txt



## docx







## xls

## xlsx

如果我们只是要 `读取` Excel文件里面的数据进行处理，可以使用 `xlrd` 这个库。

首先我们安装xlrd库，执行下面的命令，必须指定版本号

```bash
pip install xlrd==1.2.0
```

注意：xlrd 新版本只支持 xls 格式，所以我们这里指定安装 1.2.0 老版本，可以支持xlsx格式。[点击这里，下载 Excel文件 income.xlsx](https://cdn2.byhy.net/files/py/income.xlsx)



**使用pandas**

```python
# 处理模型提取的结果
def deal_al_res():
    # 打开表
    df = pd.read_excel('./xdiwfjH98xxone (1).xlsx')
    row, col = df.shape
    # print(row, col)
    for i in range(row):
        tmp = df.iloc[i]
        print(tmp['file_name'])
        with open('res.txt', 'a', encoding='utf-8') as fw:
            fw.write(tmp['file_name'] + '\n' + str(tmp['合同名称']) + '\n')
        # break
```



## csv

https://www.cnblogs.com/junpengwang/p/10803339.html



## pdf

### pdf2png

将文件夹下多个pdf文件，切分成一张张图片

```python
from pdf2image import convert_from_path
import tempfile
import numpy as np
import os


def pdf2img(filename,outputDir=None):
    print('filename=', filename)

    with tempfile.TemporaryDirectory() as path:
        images = convert_from_path(filename)
    return images


def pdfs2img(pdf_dir, save_dir):
    for rt, folders, files in os.walk(pdf_dir):
        for f in files:
            if not f.endswith("pdf"):
                continue
            pdf_path = os.path.join(rt, f)
            try:
                images = pdf2img(filename=pdf_path)
            except Exception as e:
                print(f"f:{pdf_path},error_msg:{e}")
                continue
            for index, img in enumerate(images):
                img.save(save_dir + f"{f.strip('.pdf')}_{index}.png")
    print("Compeleted.")


if __name__ == "__main__":
    pdf_dir = "/app/tag/04_单据要素提取_20230508/pdf"
    save_dir = "/app/tag/04_单据要素提取_20230508/pdf_img/"
    pdfs2img(pdf_dir=pdf_dir, save_dir=save_dir)


```

## png

### png2pdf

将多张图片合成为pdf

>  [使用Python将多张图片合成为pdf ](https://zhuanlan.zhihu.com/p/591944357?utm_id=0)

安装库：

```bash
pip install -i https://pypi.douban.com/simple --trusted-host pypi.douban.com pillow

pip install -i https://pypi.douban.com/simple --trusted-host pypi.douban.com reportlab
# 报错 Could not build wheels for pycairo which use PEP 517 and cannot be installed directly
# 解决方案
# CentOS环境下安装cairo-devel，Ubuntu环境下安装libcairo2-dev

```





### 将多张图片合成为pdf



```python
# v1.0 该版本的代码，合成的pdf都会多一个内边距
import os
from reportlab.platypus import SimpleDocTemplate, Image, PageBreak
from reportlab.lib.pagesizes import A4, landscape
from PIL import Image as pilImage

#允许转换的文件类型
__allow_type = ['.jpg', ',jpeg', '.bmp', '.png']

def convert_imagesToPDF(file_dir, save_name):
    '''
    转换一个目录文件夹下的图片至PDF
    参数：
        file_dir: 图片所在的文件夹的路径
        save_name: 目标PDF的文件名（需以.pdf结尾）
    '''
    book_pages = []
    
    for parent, dirnames, filenames in os.walk(file_dir):# os.walk()方法：返回的是一个三元组(root,dirs,files)
        # 选中目录下的所有图片                                    # root 所指的是当前正在遍历的这个文件夹的本身的地址
        for file_name in filenames:                                # dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
            file_path = os.path.join(parent, file_name)     # files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
            #是否图片
            if __isAllow_file(file_path):
                book_pages.append(file_path)

        save_path = os.path.join(file_dir, save_name)

        if len(book_pages) > 0 :
            #开始转换
            print("-----开始转换-----")
            __converted(save_path, book_pages)
            print("-----转换完成-----")


def __isAllow_file(filepath):
    '''
    是否图片文件
    '''
    if filepath and (os.path.splitext(filepath)[1] in __allow_type):
        return True
    return False

def __converted(save_book_name, book_pages = []):
    '''
    开始转换
    参数：
        save_book_name : 保存的pdf文件路径
        book_pages: 图片数组
    '''
    # A4 纸的宽高
    __a4_w, __a4_h = landscape(A4)

    # 对数据进行排序
    book_pages.sort()

    bookPagesData = []
    
    #创建一个简单模板
    bookDoc = SimpleDocTemplate(save_book_name)

    for page in book_pages:
        #获取图片的宽和高
        img_w, img_h = ImageTools().getImageSize(page)
        #取合适的比例
        if __a4_w / img_w < __a4_h / img_h:
            ratio = __a4_w / img_w
        else:
            ratio = __a4_h / img_h

        data = Image(page, img_w * ratio, img_h * ratio)
        # data = Image(page)
        print(data)
        bookPagesData.append(data)
        bookPagesData.append(PageBreak())
    bookDoc.build(bookPagesData)

class ImageTools:
    def getImageSize(self, imagePath):
        '''
        由图片路径获取宽和高
        
        '''
        img = pilImage.open(imagePath)
        return img.size


if __name__ == '__main__':
    convert_imagesToPDF(r'./png', './conver.pdf')
```

## 压缩包

> http://www.studyofnet.com/489212037.html

# 底层原理

## Python程序的执行过程

> 其实了解Python程序的执行过程对于大部分程序员来说意义都是不大的，那么真正有意义的是，我们可以从Python解释器的做法上**学到一些处理问题的方式和方法**

[Python程序的执行过程原理（解释型语言和编译型语言）](https://www.shuzhiduo.com/A/obzbMY1bdE/)

**Python是一门解释型语言？**

我初学Python时，听到的关于Python的第一句话就是Python是一门解释型语言，我就这样一直相信下去，直到发现.pyc文件的存在，如果真是解释型语言，那么生成的.pyc文件的是什么呢？c应该是compiled的缩写才对啊！
为了防止其他学习Python的人也被这句话误解，那么我们就在文中来澄清一下这个问题，并且把一些基础概念给理一理。

**解释型语言和编译型语言**

计算机是不能够识别高级语言的，所以当我们运行一个高级语言程序的时候，就需要一个“翻译机”来从事把高级语言转变成计算机能读懂的机器语言的过程。这个过程分成两类，第一种是编译，第二种是解释。
编译型语言在程序执行之前，先会通过编译器对程序执行一个编译的过程，把程序转变成机器语言。运行时就不需要翻译，而直接执行就可以了，最典型的例子就是C语言。

解释型语言就没有这个编译过程，而是在程序运行的时候，通过解释器对程序逐行做出解释，然后直接运行，最典型的例子是Ruby。
通过以上的例子，我们可以来总结一下解释型语言和编译型语言的优缺点，因为编译型语言在程序运行之前就已经对程序做出了“翻译”，所以在运行时就少掉了“翻译”的过程，所以效率比较高。但是我们也不能一概而论，一些解释型语言也可以通过解释器的优化来在对程序做出翻译时对整个程序做出优化，从而在效率上超过编译型语言。

此外，随着Java等基于虚拟机的语言的兴起，我们又不能把语言纯粹的分成解释型和编译型这两种。
用Java来举例，Java首先是通过编译器编译成字节码文件，然后在运行时通过解释器给解释成机器文件。所以我们说Java是一种先编译后解释的语言。
再换成C#，C#首先是通过编译器将C#文件编译成IL文件，然后在通过CLR将IL文件编译成机器文件。所以我们说C#是一门纯编译语言，但是C#是一门需要二次编译的语言。同理也可以等效运用到基于.NET平台上的 其他语言。

**Python到底属于哪一种类型？**

其实Python和Java/C#一样，也是一门基于虚拟机的语言，我们先来从表面上简单的了解一下Python程序的运行过程吧。
当我们在命令行中输入python hello.py时，其实是激活了Python的“解释器”，告诉“解释器”：你要开始工作了。可是在“解释”之前，其实执行的第一项工作和Java一样，是编译。
熟悉Java的同学可以想象一下我们在命令行中如何执行一个Java的程序：

```bash
javac hello.java
java hello
```

只是我们在用eclipse之类的IDE时，将这两步给融合成了一步而已。其实Python也是一样的，当我们执行python hello.py时，它也一样执行了这么一个过程，所以我们应该这样来描述Python，Python是一门先编译后解释的语言。

**简述Python中程序的运行过程**

在说这个问题之前，我们先来说两个概念，PyCodeObject和pyc文件。
我们在硬盘上看到的pyc自然不必多说，而其实PyCodeObject则是Python编译器真正编译成的结果。我们先简单知道就可以了，继续向下看。
当Python程序运行时，编译的结果则是保存在位于内存中的PyCodeObject中，当Python程序运行结束时，Python解释器则将PyCodeObject写回到pyc文件中。
当Python程序第二次运行时，首先程序会在硬盘中寻找对应的pyc文件，如果找到，则直接载入，否则就重复上面的过程。

所以我们应该这样来定位PyCodeObject和pyc文件：pyc文件其实是PyCodeObject的一种持久化保存方式。

我们先来简单看两个例子
写一段简单的程序运行一下：

```python
def print_hello(s):
    print('welcome information: %s' %s)

if __name__ == '__main__':
    print_hello('hello world')
```

执行`python3 test.py`

我们发现在运行完test.py这个程序后，当前路径下并没有生成相应的pyc文件。那是为什么呢？
我们再来做一个小测试，将test.py当做模块导入到test888.py文件中，然后在这个程序中运行print_hello这个程序：

`test.py`

```python
def print_hello(s):
    print('welcome information: %s' %s)
```

`test888.py`

```python
from test import print_hello

if __name__ == '__main__':
    print_hello('hello world')
```

我们可以发现运行完test888.py文件后在当前路径下出现了一个名叫`__pycache__`的文件夹，里面包含了一个pyc文件，下面我们来分析一下这个过程到底发生了什么。

![image-20230419092124600](pythonimage-20230419092124600.png)

**pyc文件的目的**
回想上面我们在分析编译型语言和解释型语言的优缺点时，编译型语言的优点在于，我们可以在程序运行时不用解释，而直接利用已经翻译过的文件。也就是说，我们之所以要把py文件编译成pyc文件，最大的优点在于我们在运行程序时，不需要重新对该模块进行再次解释。
所以，需要编译成pyc文件的应该是那些可以重用的模块，这于我们在设计类时是一样的目的。所以Python的解释器认为：只有import进来的模块，才是需要被重用的模块。

这个时候也许有人会有疑问，我的test.py不是也需要运行吗，虽然不是一个模块，但是以后我每次运行也可以节省时间啊！
OK，我们从实际情况出发，思考一下我们在什么时候才可能运行python xxx.py文件：

1. 执行测试时；
2. 开启一个Web进程时；
3. 执行一个脚本时。

我们来逐条分析，第一种情况就不多说了，这个时候哪怕所有的文件都没有pyc文件都是无所谓的。

第二种情况，试想一个web.py的程序，通常是这样执行的：

然后这个程序就类似于一个守护进程一样一直监视着8000端口，而一旦中断，只可能是程序被杀死或者其他的意外情况，那么你要做的是把整个Web服务重启，那么既然一直监视着，把PyCodeObject一直放在内存中就足够了，完全没有必要持久化到硬盘上。

再来看看最后一个情况，执行一个程序脚本，一个程序的主入口其实很类似于Web程序中的Controller，也就是说，他负责的应该是Model之间的调度，而不包含任何的主逻辑在内，只是负责把参数转来转去而已，那么如果做算法的同学可以知道，在一段算法脚本中，最容易改变的就是算法的各个参数，那么这个时候将它持久化成pyc文件就未免有些画蛇添足了。

所以我们可以这样理解Python解释器的意图，Python解释器只是把我们可能重用到的模块持久化成pyc文件。

**pyc文件的过期时间**

说完了pyc文件，可能有人会想到，每次Python解释器都把模块给持久化成pyc文件，那么当我的模块发生改变的时候，是不是都要手动的把之前的pyc文件remove掉呢？
当然Python的设计者是不会犯这样的错误的，这个过程其实取决于PyCodeObject是如何写入pyc文件中的。
我们仔细看一下Import模块的源码其实不难发现，它在写入pyc文件的时候，写了一个Long型变量，变量的内容则是文件的最近修改日期，同理，在pyc文件中，每次在载入之前都会检查一下py文件和pyc文件保存的最后修改日期，如果不一致则重新生成新的pyc文件。

**总结**

其实了解Python程序的执行过程对于大部分程序员来说意义都是不大的，那么真正有意义的是，我们可以从Python解释器的做法上**学到一些处理问题的方式和方法**：

在Python中判断是否生成pyc文件和我们在设计缓存系统时是一样的，我们可以仔细想想，到底什么是值得扔在缓存里面的，什么是不值得的。
在运行一个耗时的Python脚本时，我们如何能够做到稍微压榨一些程序的运行时间呢？就是将模块从主模块分开。（虽然往往这都不是瓶颈）
在设计一个软件系统时，重用和非重用的东西是不是也可以分开来对待，这是软件设计原则的重要部分。
在设计缓存系统（或者其他系统）时，我们如何来避免程序的过期，其实Python解释器为我们提供了一个特别常见而且有效的解决方案。

## `__main__`最高层级代码环境

[__main__ --- 最高层级代码环境 — Python 3.11.3 文档](https://docs.python.org/zh-cn/3/library/__main__.html#module-__main__)

在 Python 中，特殊名称 `__main__` 被用于两个重要的构造:

1. 程序的最高层级环境的名称，可以使用 `__name__ == '__main__'` 表达式来检查它；以及
2. Python 包中的 `__main__.py` 文件。

这两种机制都有 Python 模块有关；用户如何与它们交互以及它们之间如何交互。 下文将进行详细说明。 如果你还不了解 Python 模块，请查看教程 [模块](https://docs.python.org/zh-cn/3/tutorial/modules.html#tut-modules) 一节的介绍。

## 深浅拷贝

[copy --- 浅层 (shallow) 和深层 (deep) 复制操作 — Python 3.11.3 文档](https://docs.python.org/zh-cn/3/library/copy.html#shallow-vs-deep-copy)

Python 的赋值语句不复制对象，而是创建目标和对象的绑定关系。对于自身可变，或包含可变项的集合，有时要生成副本用于改变操作，而不必改变原始对象。本模块提供了通用的浅层复制和深层复制操作，（如下所述）。

浅层与深层复制的区别仅与复合对象（即包含列表或类的实例等其他对象的对象）相关：

- *浅层复制* 构造一个新的复合对象，然后（在尽可能的范围内）将原始对象中找到的对象的 *引用* 插入其中。
- *深层复制* 构造一个新的复合对象，然后，递归地将在原始对象里找到的对象的 *副本* 插入其中。

深度复制操作通常存在两个问题, 而浅层复制操作并不存在这些问题：

- 递归对象 (直接或间接包含对自身引用的复合对象) 可能会导致递归循环。
- 由于深层复制会复制所有内容，因此可能会过多复制（例如本应该在副本之间共享的数据）。

# 源码剖析



# 办公自动化专题

> 涵盖了Excel、Word、PPT、ODF、PDF、邮件、微信、文件处理等所有能在办公场景实现自动化的库

## Excel自动化库

1.xlwings 库

官网：

https://www.xlwings.org/

特点：xlwings 是开源且免费的，预装了 Anaconda 和 WinPython，可在 Windows 和 macOS 上运行。通过 Python 脚本或 Jupyter notebook 自动化 Excel，通过宏从 Excel 调用 Python，并编写用户定义的函数（UDF 仅适用于 Windows）



 2.openpyxl 库

官网：

[https://openpyxl.readthedocs.io](https://openpyxl.readthedocs.io/)

特点：openpyxl 是一个用于读取 / 编写 Excel 2010 xlsx/xlsm/xltx/xltm 文件的 Python 库。它是由于缺乏从 Python 中读取 / 编写 Office Open XML 格式的现有库而诞生的。



3.xlrd 库

官网：

https://pypi.python.org/pypi/xlrd

特点：在 python 中，xlrd 库是一个很常用的读取 excel 文件的库，其对 excel 文件的读取可以实现比较精细的控制。



 4.xlwt 库

官网：

https://pypi.org/project/xlwt/

特点：类比于 xlrd 的 reader，那么 xlwt 就相对于 writer，而且很纯正的一点就是它只能对 Excel 进行写操作。xlwt 和 xlrd 不光名字像，连很多函数和操作格式也是完全相同。



5.xlutils 库

官网：

https://pypi.org/project/xlutils/

特点：xlutils（excel utilities）是一个提供了许多操作修改 excel 文件方法的库。xlutils 库也仅仅是通过复制一个副本进行操作后保存一个新文件，xlutils 库就像是 xlrd 库和 xlwt 库之间的一座桥梁，因此，xlutils 库是依赖于 xlrd 和 xlwt 两个库的。



6.xlsxwriter 库

官网：

https://xlsxwriter.readthedocs.io/

特点：xlsxwriter 是用于创建 Excel XLSX 文件的 Python 模块，可用于将文本、数字、公式和超链接写入 Excel2007 + XLSX 文件中的多个工作表。它支持格式化等功能。可以说除了 Excel 本身，就属这个功能最齐全了。



7.pandas 库

官网：

https://www.pypandas.cn/docs/

特点：pandas 是基于 NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。



8.Marmir 库

官网：

https://github.com/brianray/mm

特点：Marmir 采用 Python 数据结构并将其转换为电子表格。它是类固醇上的 xlwt 和 google 电子表格。目标是使用最少的配置轻松生成多种类型的有用表文件。



## Word自动化库



9.python-docx 库

官网：

https://python-docx.readthedocs.io/en/latest/

特点：python-docx 是一个用于创建和更新 Microsoft Word (.docx) 文件的 Python 库。快速开始、处理文档、处理文本、使用截面、使用页眉和页脚、API基础理、解样式、使用样式理解图片和其他形状。只对 windows 平台有效。



10.textract 库

官网：

https://gitee.com/mirrors/textract

特点：它同时兼顾 “doc” 和 “docx”，但安装过程需要一些依赖。你可以批量的用 python 生成 word 文件，推荐使用 docx，不需要会太多。



## PPT自动化库



11.python-pptx 库

官网：

[https://python-pptx.readthedocs.io](https://python-pptx.readthedocs.io/)

特点：python-pptx 是一个用于创建和更新 PowerPoint (.pptx) 文件的 Python 库。典型用途是从数据库内容生成自定义 PowerPoint 演示文稿，可通过单击 Web 应用程序中的链接下载。



## ODF自动化库

12.Relatorio 库

官网：

https://pypi.org/project/relatorio/

特点：Relatorio 是一个模板库，它提供了一种轻松输出多种文件（odt、ods、png、svg 等）的方法。通过为它们创建插件可以轻松添加对更多文件类型的支持。Relatorio 还提供了一个报告存储库，允许您将 python 对象和报告链接在一起，按 mimetype/name/python 对象查找报告。ODF：开放文档格式（外文名：OpenDocument Format，外语简称：ODF）是一种规范，基于 XML（标准通用标记语言的子集）的文件格式，因应试算表、图表、演示稿和文字处理文件等电子文件而设置。

## PDF自动化库

13.PyPDF2 库

官网：

https://github.com/mstamy2/PyPDF2

特点：PyPDF2 是一个纯 Python PDF 库，能够拆分、合并、裁剪和转换 PDF 文件的页面。它还可以向 PDF 文件添加自定义数据、查看选项和密码。它可以从 PDF 中检索文本和元数据，也可以将整个文件合并在一起。



14.ReportLab 库

官网：

https://www.reportlab.com/opensource/

特点：ReportLab 是久经考验、超强大的开源引擎，用于创建复杂的、数据驱动的 PDF 文档和自定义矢量图形。它是免费的、开源的，并且是用 Python 编写的。



15.PDFminer 库

官网：

https://github.com/euske/pdfminer

特点：PDFMiner 是一款用于 PDF 文档的文本提取工具。

## 邮件自动化库

16.Django Celery SES 库

官网：

https://github.com/StreetVoice/django-celery-ses

特点：这个包提供了一个 EmailBackend 来利用 django-celery 发送电子邮件。您可以将 EmailBackend 插入您的项目中，而无需对代码进行任何修改。



17.Envelopes 库

官网：

http://tomekwojcik.github.io/envelopes/

特点：Envelopes 是 Python 的电子邮件和 smtplib 模块的包装器。它旨在使在 Python 中处理外发电子邮件变得简单而有趣。



18.Flanker 库

官网：

https://github.com/mailgun/flanker

特点：由 mailgun 开源的 Flanker - email address and MIME parsing for Python 是一个解析高效、容错率不错的 python 第三方扩展库。python 3 也可以正常使用，该库包含了邮件地址解析和邮件 mime 格式解析。



 19.imbox 库

官网：

https://github.com/martinrusev/imbox

特点：用于读取 IMAP 邮箱并将电子邮件内容转换为机器可读数据的 Python 库



20.inbox.py 库

官网：

https://github.com/billzhong/inbox.py

特点：这是您见过的最简单的 SMTP 服务器。它是异步的。一个实例每秒应该处理一千多封电子邮件。



21.sync-engine 库

官网：

https://github.com/nylas/sync-engine

特点：Nylas 同步引擎在强大的电子邮件同步平台之上提供了一个 RESTful API，可以轻松地在电子邮件之上构建应用程序。



22.Lamson 库

官网：

https://github.com/zedshaw/lamson

特点：Lamson 是一个纯 Python SMTP 服务器，旨在以现代 Web 框架（如 Django）的风格创建强大而复杂的邮件应用程序。



23.Marrow Mailer 库

官网：

https://github.com/marrow/mailer

特点：Marrow Mailer 是一个 Python 库，可以轻松地从您的应用程序发送电子邮件。通过使用 Marrow Mailer，您可以：轻松构建纯文本和 HTML 电子邮件；提高电子邮件传递的可测试性；使用不同的邮件投递管理策略；例如立即，延迟，甚至多服务器等。



24.Modoboa 库

官网：

https://github.com/modoboa/modoboa

特点：Modoboa 是一个邮件托管和管理平台，包括一个现代和简化的 Web 用户界面。它提供了有用的组件，例如管理面板或网络邮件。



25.smtplib 库

官网：

https://docs.python.org/zh-cn/3/library/smtplib.html

特点：smtplib 模块是 python 中 smtp (简单邮件传输协议) 的客户端实现。我们可以使用 smtplib 模块，轻松的发送电子邮件。

## 微信自动化库

26.Python wxpy 库

官网：

https://wxpy.readthedocs.io/zh/latest/

特点：微信机器人/可能是最优雅的微信个人号API，wxpy 在 itchat 的基础上，通过大量接口优化提升了模块的易用性，并进行丰富的功能扩展。

## 文件处理自动化库

27.os 库

官网：

https://docs.python.org/zh-cn/3/library/os.html?highlight=os#module-os

特点：本模块提供了一种使用与操作系统相关的功能的便捷式途径。如果你只是想读写一个文件，请参阅 open()，如果你想操作文件路径，请参阅 os.path 模块，如果你想读取通过命令行给出的所有文件中的所有行，请参阅 fileinput 模块。为了创建临时文件和目录，请参阅 tempfile 模块，对于高级文件和目录处理，请参阅 shutil 模块。



## 综合功能自动化库

28.win32com 库

官网：

https://pypi.org/project/pywin32/

特点：win32com 模块主要为 Python 提供调用 windows 底层组件对 word 、Excel、PPT 等进行操作的功能，只能在 Windows 环境下使用，并且需要安装 office 相关软件才行（WPS 也行）。



 29.unoconv 库

官网：

https://github.com/unoconv/unoconv



特点：是一个命令行工具，可以将 LibreOffice 可以导入的任何文档格式转换为 LibreOffice 可以导出的任何文档格式。它利用 LibreOffice 的 UNO 绑定进行文档的非交互式转换，也支持 OpenOffice。



30.Tablib 库

官网：

https://www.osgeo.cn/tablib/

特点：Python tablib 模块是第三方模块，主要作用是将数据导出为各种不同的格式，包括 excel，json，html，yaml，csv，tsv 等格式，怎么样，有点心动了吧，当然这个模块使用起来也是超级简单的。



31.SnowNLP 库

官网：

https://github.com/isnowfy/snownlp

特点：SnowNLP 是一个 python 写的类库，可以方便的处理中文文本内容，是受到了 TextBlob 的启发而写的，由于现在大部分的自然语言处理库基本都是针对英文的，于是写了一个方便处理中文的类库，并且和 TextBlob 不同的是，这里没有用 NLTK，所有的算法都是自己实现的，并且自带了一些训练好的字典。注意本程序都是处理的 unicode 编码，所以使用时请自行 decode 成 unicode。



32.TextBlob 库

官网：

[https://textblob.readthedocs.io](https://textblob.readthedocs.io/)

特点：TextBlob 是一个用于处理文本数据的 Python（2 和 3）库。它提供了一个简单的 API，用于深入研究常见的自然语言处理 (NLP) 任务，例如词性标注、名词短语提取、情感分析、分类、翻译等。



33.TextGrocery 库

官网：

[https://textgrocery.readthedocs.io](https://textgrocery.readthedocs.io/)

特点：TextGrocery 是一个基于 LibLinear 和结巴分词的短文本分类工具，特点是高效易用，同时支持中文和英文语料。



34.NumPy 库

官网：

https://www.numpy.org.cn/

特点：NumPy 是 Python 中科学计算的基础包。它是一个 Python 库，提供多维数组对象，各种派生对象（如掩码数组和矩阵），以及用于数组快速操作的各种 API，有包括数学、逻辑、形状操作、排序、选择、输入输出、离散傅立叶变换、基本线性代数，基本统计运算和随机模拟等等。

# 工具软件

## 文件整理系统设计

[ 有哪些值得借鉴的工作文件分类和整理方法？](https://www.zhihu.com/question/34633472?sort=created)

### 文件夹相关

**命名**

以`数字-部门/功能`

```
01_HR
02_admin
03_Fin
04_Engg
05_Sales
```

**嵌套**

取消多级文件夹嵌套，两层最好，最多三层

所有文件夹，甭管它属于哪个大分类，全部都在最外层。直接把所有子文件夹放到外面来，然后用数字前缀归类。

![image-20230419161931232](image-20230419161931232.png)

二级分类也可以按照A、B、C、D字母排，看自己的喜好。

单独的file可以建立一个folder，里面只装这个file，让它强制参与folder的排序就OK了。

后期维护可以手动修改前缀调整逻辑层级，或者借助批量命名工具等(linux环境下更方便)

问题：文件会越来越多怎么办？继续往下看

**全盘文件分类**

按用途分，同一个用途下，不管什么类型的文件，都可以放在一起

![image-20230419163129678](image-20230419163129678.png)

- 01 工作目录

  所有正在处理或者待处理的工作，都在这个文件夹 下。包括公司的工作、私活、杂事、计算房贷、个人计划、打官司、帮别人写资料等。可以理解为是一个todolist，可以在编号前加上时间，比如：

  ![image-20230419163448449](image-20230419163448449.png)

  这里的文件迟早会越积越多，会督促我们及时处理。需要及时把处理完的文件移动到08 存档资料中。

  宗旨是，要把工作目录里的文件夹控制在一定的数量，做完就移走

  拓展：上面描述的是已经在做的事，和知道了即将要做的事，可以做一个excel，记录下文件夹名称，及此次job的背景、目标等。也可记录即将可能落到自己头上的事情。当然也没必要这样，因为这需要始终同步。不一定同步，如果不通过这种方式来写readme，可以在每个文件夹下，加上各自的readme即可。

- 02 学习资料

  放一些学习教程，如职场技能学习，英语学习、法律学习等等，同样也只建立一层子文件夹，参考上述第二点。

  ![image-20230419164117933](image-20230419164117933.png)

  我自己的实际是，把所有的文档笔记，放在一个目录下，用tpora管理，并同步github

  ![image-20230419164224210](image-20230419164224210.png)

- 03 参考资料&素材

  可能需要用到的参考资料，这是从事工作的原材料。比如网上下载的模板、表格、视频、字体等

- 04 视频

  放一些娱乐视频，不包括学习教程，不包括自己收集拍摄的视频

  自己的实际是将学习教程下载下来，同步到网盘

- 05 相册

  按照时间 + 主题建立子文件夹

- 06 软件工具

  放一些软件安装包，如office365、abobe系列、IDE等

  自己的实际是同步到网盘

- 07 个人重要资料

  身份证复印件、户口本复印件、房产证复印件、银行卡复印件、体检报告、个人简历等等

  这种类型的资料最好集中存放。云端的话自行选择

- 08 存档资料

  放已经完成的工作

以上只是参考，根据实际情况自行调整



**其他技巧**

- 桌面建立临时文件夹
- 添加到快速访问
- 配合`everything`文件搜索

### 文件相关

**如何给文件起名**

文件添加时间后缀，如project_checklist_20220523

这样的好处是下载下来永远不会乱，系统会自动按照时间顺序排列，而你也知道这个文件是什么时候创建的，方便识别和追溯。

在创建文件加事件后缀，发给比人修改后从接收新的文件，也要更新时间后缀。如果基于已有的某个版本更新，复制当前副本并修改时间后缀。这样永远知道那个版本是最新的。

发给别人的文件如果都加上一个时间后缀，会显得专业很多。



其他：

2、工作文件夹命名可以采用：年月节点+ 项目名 + 备注的方式，备注可以写用途等，比如：22年中_大促_100亿补贴

3、文件夹和文件名尽量采用下划线，非数字文本下划线的字符，在计算机里有时会被判断为非法字符

4、可以用 QTTabBar 加强文件管理器的功能，翻文件和另存为时会很方便

5、同步文件的工具，可以用 OneDrive，重要资料放里面

5、用 Zotero 可以管理信息，配合 OneDrive，可以同步和检索各种格式的数据，包括PDF、Excel、PPT等。有两大亮点：一是Zotero 里点一下就能打开其他文件，这是各类笔记不支持的功能；二是支持给文件加标签，树状目录+标签的方式检索功能更强大，适合沉淀专业知识

6、工具软件可以用一个硬盘来存，重装系统，换电脑的迁移成本会小点

7、梯子可以用 V2，开启Pac模式，可以后台常驻。Zotero 和 OneDrive 要搭配用，Chrome 上一些好用的插件也需要在应用商店里下

### 邮件相关

处理的主要是数据，此篇略

### 桌面整理相关







## ETL工具

### Kettle

> 现在的数据库种类越来越多，数据库备份的格式也越来越复杂，所以数据格式化一直是一个老生常谈的问题。据库备份文件格式那么多，既有SQL的，也有BAK的，还有TXT的等。数据库种类也有很多，MySQL，Oracle，SQL server等，怎么对这些数据库进行管理？

[数据库数据格式化之Kettle Spoon_51CTO博客_kettle 数据同步](https://blog.51cto.com/u_15076209/4338401)

视频教程：https://www.bilibili.com/video/BV1NT4y1c7o8/

## 配置

选择设置--配置用户代码段，选择 python。会自动生成 python.json。编辑为如下：

vscode添加头模板：https://www.cnblogs.com/odesey/p/16555873.html

```json
{
	// Place your snippets for python here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"HEADER": {
		"prefix": "desc",
		"body": [
			"#!/usr/bin/env python",
			"# -*- encoding: utf-8 -*-",
			"'''",
			"@File    :   $TM_FILENAME",
			"@Time    :   $CURRENT_YEAR/$CURRENT_MONTH/$CURRENT_DATE $CURRENT_HOUR:$CURRENT_MINUTE:$CURRENT_SECOND",
			"@Version :   1.0",
			"@Desc    :   None",
			"'''",
			"",
			"# import lib here",
			"",
			"",
			"if __name__ == '__main__':",
			"\t$0",
			"\tpass"
		],
	}
}
```















