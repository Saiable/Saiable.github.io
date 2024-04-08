---
title: 'shell'
date: 2023-03-01 09:03:02
cover: false
tags:
- python
categories: shell
typora-root-url: shell
---

# 文件批量重命名

## rename 命令

顾名思义，rename 命令就是用来进行重命名文件名的。rename 命令有非常强大的功能，我们可以用它来实现各种各样复杂的文件名修改。但是，本文只介绍它最最基本的功能。其最基本的格式如下：

```bash
rename 源字符串 目标字符串 文件
```

其中，源字符串表示原文件名需要替换的字符串，可以是原文件名的全部或部分；

目标字符串就是想要替换成的字符串；

文件就是需要更改文件名的文件列表，可以是一个或多个。

现假如目录下有一堆 atb_mod_01.cpp、atb_mod_02.cpp、atb_mod_03.cpp、atb_mod_04.cpp 等形式的文件，我们的需求是将文件名中的 mod 改成 adb，那么完成这个需求的命令如下：

```bash
[alvin@VM_0_16_centos exp3]$ ls
atb_mod_01.cpp atb_mod_02.cpp atb_mod_03.cpp atb_mod_04.cpp
[alvin@VM_0_16_centos exp3]$ rename mod adb *
[alvin@VM_0_16_centos exp3]$ ls
atb_adb_01.cpp atb_adb_02.cpp atb_adb_03.cpp atb_adb_04.cpp
```

## mv 命令配合 for 循环方式

假如我们现在有一堆 .txt 文件，我们想将它们的后缀改成 .cpp。先来看完整的代码：

```bash
#!/bin/bash
for name in `ls *.txt`
do
mv $name ${name%.txt}.cpp
done
```

我们都知道，在 Linux 里重命名是用 mv 命令，那批量重命名自然会想到用循环语句嵌套 mv 命令。

在这里，我们用 `ls *.txt` 将当前目录下所有的 txt 文件全部列出来，然后逐个放在 name 变量里去循环操作。

在循环体里，我们使用 mv 命令进行重命名。这里我们使用 ${name%.txt} 这种字符串处理方式，表示从name尾部开始删除与 .txt 匹配的最小部分，并返回剩余部分。之后，再加上 .cpp 后缀。通过这种操作，我们就可以将文件名后缀从 .txt 改为 .cpp。最后我们用 mv 命令将这个文件名真正改过来。

## sed 命令配合 for 循环方式

假如我们现在有一堆文件，文件名格式是 test01.txt、test02.txt、test03.txt、test04.txt 也就是前半部分是英文，后半部分是数字。我们现在想将文件名改成 test-01.txt 这种形式。这次，我们用 sed 命令来完成这个需求。

我们还是先来看看完整的代码：

```bash
#!/bin/bash
for file in `ls *.txt`
do
newFile=`echo $file | sed 's/\([a-z]\+\)\([0-9]\+\)/\1-\2/'`
mv $file $newFile
done
```

前面一样用 `ls \*.txt` 来获取所有的 .txt 文件。之后再用 echo 命令将其顺次输出，作为 sed 命令的输入。

接下来，到达关键部分了。乍一看 sed 的命令可能有点可怕，但老司机早已习以为常了。反引号里的内容其实是这样的基本结构：

s/ 原字符串 / 替代的字符串 /

这里我们用到了分组匹配，也就是用括号按照一定的正则表达式将原字符串进行分组，后面再用 `\1，\2，\3……` 来引用前面的分组，从而在替代的字符串里拼凑成相应的格式。

前文已讲述，原文件名是由前部分英文及后部分数字所构成的，英文可以用 [a-z]+ 表示，数字可以用 [0-9]+ 表示。注意不要忘记加号，表示前面字符的若干重复。然后，我们用 \1、\2 分别引用前面的对应部分，再用横杆连起来，于是就成了这样：：

```bash
s/([a-z]+)([0-9]+)/\1-\2/
```

因为在不同的 Shell 里，括号及加号可能会有不同的含义，所以前面要再加一个转义符，于是就成了前面所见到的样子。

再之后，同样使用 mv 命令完成重命名动作。

拓展：[sed命令详解](https://mp.weixin.qq.com/s?__biz=MzI3NDc4NTQ0Nw==&mid=2247489511&idx=2&sn=5838d71c209ab1ca167dcce69c908d1c&chksm=eb0fe22fdc786b39e300f0a2b903165ffa12fe011092a9fe3f62d90b0daec639730cea542690&scene=27)

**需求一：**

背景：`labelstudio`上传文件会自己删掉一些符号，现在希望把所有的原始文件重命名01、02的形式，并保留文件名的映射关系

```bash
# 先使用bat批量加一下前缀

```



# 压缩与解压

https://blog.csdn.net/weixin_49164248/article/details/121151062

1、tar命令

功能描述：将文件或者目录进行打包、或者解压缩 格式：tar [参数] [打包后的文件名] [需要打包的文件或目录]

其中参数包括一下几个：

- c 创建压缩文件
- x 展开归档文件
- t 显示包括在tar文件中的文件列表
- z 压缩/解压缩文件（gz格式）
- v 写入或读取时，显示所有的文件
- f 指明要展开的归档文件名
- j 压缩或解压缩文件（bz2格式）

将home下目录test打包成tar包

```
[root@localhost ~]# tar cvf test.tar /home/test 
```

将test.tar解压缩

```
[root@localhost ~]# tar xvf test.tar
```

例：

```
[root@localhost 桌面]# tar cvf a.tar a
[root@localhost 桌面]# tar xvf a.tar
```

# 查看文件大小

https://m.php.cn/article/467502.html

1.使用“stat 文件名”命令显示指定文件的详细信息,即可查看文件大小;

2.使用“wc -c 文件名”命令来查看;

3.使用“du -h 文件名”命令来查看;

4.使用“ls -l 文件名”命令来查看。

[ 更多 >](http://www.baidu.com/link?url=0Gbg-PkIiZnYo7vVO3BZ34hK-tDv6jRs7Scr9T8dvmrce0nlLjy-24wjNnz03wO7)

# 复制





























































