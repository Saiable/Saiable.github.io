---
title: 'windows系统下常见的bat命令'
date: 2022/7/8 07:15:24
cover: false
---

# `bat`语法快速入门

https://blog.csdn.net/qq_21845263/article/details/109683934

# 列出目录下的所有文件名

```
dir/s/b > name.txt
```

# 复制特定后缀文件到其他目录

```bash
@echo off
for /r %%a in (*.txt) do copy %%a D:\1
pause
```

1、for /r主要用于搜索指定路径及其所有子目录中符合要求的文件（/r后如果没有指定目录，则使用当前目录）

2、上述例子实现将脚本所在目录下后缀为txt的文件复制到目录D:\1中

3、批处理当中的 for 循环的结构：for   in   do。

%%a 为变量，/r 为递归方式，in 与 do 之间一定要有 ()。

for 循环的工作流程：查找当前文件夹及其子文件夹里面的 txt 文件，找到后把文件路径赋值给变量 %%a，然后执行 do 后面的语句，直到遍历完全部文件。

4、copy可以替换为move。表示移动文件。

```
@echo
for /f "delims=" %%p in ('dir /b/ad') do copy "%%p\*.*" F:\AAA视频\test
pause
```

源文件位置：     *.*

目标文件位置：  F:\AAA视频\test

注意：copy的源文件位置之所以用双引号，是因为我本地的文件夹的名称中有空格，可以加也可以不加

[Windows bat批处理 如何批量复制指定的文件夹？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/480662243/answer/2073356686)

































