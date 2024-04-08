---
title: 'python环境'
date: 2023-02-16 09:03:02
cover: false
tags:
- python
categories: python
typora-root-url: python环境
---

# windows安装python3

官网下载：[Download Python | Python.org](https://www.python.org/downloads/)，国外下载慢，网盘：https://www.aliyundrive.com/s/xfEJeFK7Evw

配置环境变量：[win10如何安装python3及设置环境变量](https://jingyan.baidu.com/article/09ea3ede4f4c22c0aede39ac.html)

如果本机上已经配置了其他版本的python，可以将python3根目录下的`python.exe`重命名，如`python3.11`。再用`python3.11`调用即可

同理配置下pip的环境变量，在`python311\Scripts`目录

# linux安装python3

[Linux系统安装Python3环境（超详细）](https://zhuanlan.zhihu.com/p/469420901?utm_id=0)

默认情况下，Linux会自带安装Python，可以运行python --version命令查看

查看Linux默认安装的Python位置

```bash
[root@localhost ~]# whereis python
python: /usr/bin/python /usr/bin/python2.7 /usr/lib/python2.7 /usr/lib64/python2.7 /etc/python /usr/include/python2.7 /usr/share/man/man1/python.1.gz

[root@localhost ~]# ls -l /usr/bin/py*
-rwxr-xr-x. 1 root root   78 Oct 14  2020 /usr/bin/pydoc
-rwxr-xr-x. 1 root root  188 Jun 10  2014 /usr/bin/pygtk-demo
-rwxr-xr-x. 1 root root   42 Dec 29  2013 /usr/bin/pyinotify
lrwxrwxrwx. 1 root root    7 May  6  2022 /usr/bin/python -> python2
lrwxrwxrwx. 1 root root    9 May  6  2022 /usr/bin/python2 -> python2.7
-rwxr-xr-x. 1 root root 7144 Oct 14  2020 /usr/bin/python2.7
lrwxrwxrwx. 1 root root   36 May  6  2022 /usr/bin/python3_django -> /data/data01/cht/python3/bin/python3
```

看到/usr/bin/python和/usr/bin/python2都是软链接，/usr/bin/python指向/usr/bin/python2，而/usr/bin/python2最终又指向/usr/bin/python2.7。所以运行python/python2/python2.7是一样的

```bash
[root@localhost ~]# python --version
Python 2.7.5
[root@localhost ~]# python2 --version
Python 2.7.5
[root@localhost ~]# python2.7 --version
Python 2.7.5
```

**安装python3**

- 登录[https://www.python.org/downloads/source/](https://link.zhihu.com/?target=https%3A//www.python.org/downloads/source/)，找到对应版本

- 将文件上传到Linux系统的某个目录下，根据自己情况上传

# python多环境管理

## 背景

[附001.Python多版本环境管理 ](https://www.cnblogs.com/itzgr/p/16324135.html#_label0)

由于Python的版本过多，且不同版本之间差异性较大。同时又因系统底层需要调用当前版本Python，所以不能随意变更当前系统Python版本。因此，在多版本共存的情况下，Python多环境管理工具非常重要，常见Python多环境管理工具有Pyenv和Virtualenv。

Pyenv对Python的版本进行管理，实现不通版本间的切换和使用；

Virtualenv通过创建虚拟环境，实现与系统环境以及其他Python环境的隔离。

## pyenv部署与使用

### pyenv简介

[GitHub - pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv#installation)

pyenv是一个Python版本管理工具，可方便地切换全局Python版本，安装多个不通的Python版本，设置独立的某个文件夹或工程目录特意的Python版本，同时创建Python虚拟环境。

注意：该工具不支持Windows。

### pyenv工作原理

1.pyenv安装后会在系统PATH中插入shims路径，每次执行Python相关的可执行文件时，会优先在shims里查找Python路径`~/.pyenv/shims:/usr/local/bin:/usr/bin:/bin;`

2.系统选择Python版本，依如下顺序选择Python版本：

- 1. Shell变量设置（执行pyenv shell查看）
  2. 当前可执行文件目录下的`.python_version`文件里的版本号（执行pyenv shell查看）
  3. 上层目录查询找到的第一次`.pyenv-version`文件
  4. 全局的版本号在`~/.pyenv/version`文件内（执行pyenv shell查看）

3. 确定版本文件的位置和Python版本后，pyenv会根据版本号在~/.pyenv/versions/文件夹中查找对应的Python版本。

**提示：执行命令pyenv versions可查看系统当前安装的Python版本。**

**python优先级：shell > local > global**

**pyenv 会从当前目录开始向上逐级查找.python-version文件，直到根目录为止。若找不到，就用global版本。**

### pyenv安装部署-手动安装

```bash
[root@localhost ~]# yum -y install git		#安装git工具
[root@localhost ~]# yum -y install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel			#安装相关环境基础包
[root@localhost ~]# git clone https://github.com/pyenv/pyenv.git ~/.pyenv
#clone pyenv至家目录
[root@localhost ~]# echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
[root@localhost ~]# echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
[root@localhost ~]# echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
#修改环境变量
[root@localhost ~]# source ~/.bash_profile		#重启当前Shell
[root@localhost ~]# pyenv versions			#查看版本
```

![clipboard](/680719-20220529163642365-2119085018.png)

### pyenv安装部署-自动安装

```bash
[root@localhost ~]# yum -y install git		#安装git工具
[root@localhost ~]# yum -y install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel		#安装相关环境基础包
[root@localhost ~]# curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
[root@localhost ~]# pyenv versions			#查看版本
```

![clipboard](680719-20220529163642829-646989826.png)

**提示：手动安装和自动挡安装任选其一即可。**

**自动安装可能出现环境变量未添加的情况，可参考手动安装进行添加。**

### pyenv使用实例

```bash
[root@localhost ~]# pyenv update			#pyenv升级

[root@localhost ~]# rm -rf $(pyenv root)		#卸载
[root@localhost ~]# vi ~/.bash_profile			#删除以下条目
export PATH="~/.pyenv/bin:$PATH"			#删除
eval "$(pyenv init -)"					#删除
eval "$(pyenv virtualenv-init -)"			#删除

[root@localhost ~]# pyenv install -list			#查看可安装的版本列表
[root@localhost ~]# pyenv install 3.6.5			#安装指定版本的Python
[root@localhost tmp]# pyenv local 2.7.15
```

![clipboard](680719-20220529163643288-1249939713.png)

切换当前目录的Python版本，通过将版本号写入当前目录下的`.python-version`文件的方式。通过这种方式设置的 Python版本优先级较global高。

![clipboard](https://img2022.cnblogs.com/blog/680719/202205/680719-20220529163643735-357972950.png)

设置全局的Python版本，通过将版本号写入`~/.pyenv/version`文件的方式。

### pyenv常见参数

|        命令        | 说明                                                         |
| :----------------: | ------------------------------------------------------------ |
|   pyenv version    | 显示当前Python的版本和来源。                                 |
|   pyenv versions   | 列出当前环境的所有可用Python版本。                           |
|  pyenv install -l  | 列出所有可以安装的Python版本。                               |
|  pyenv install -v  | 安装Python，-v 显示编译过程。                                |
|    pyenv shell     | 查看或列出、设置Shell环境下的的Python版本， 设置当前shell session的Python版本，它的优先级高于global和local。 |
| pyenv shell –unset | 取消shell版本设置。                                          |
|    pyenv global    | 查看或列出、设置全局环境下的的Python版本， 设置全局Python版本替换系统自带版本，可能会引起某些配置失效 （如yum命令），不建议使用！！！设置后恢复系统版本：pyenv global system。 |
|    pyenv local     | 查看或列出、设置当前环境下的的Python版本， 设置当前用户的可用的本地Python版本，它的优先级高于全局Python版本。 |
| pyenv local –unset | 取消本地版本设置。                                           |
|  pyenv uninstall   | 卸载特定Python版本。                                         |
|    pyenv which     | 列出command的全路径。                                        |
|    pyenv whence    | 列出包含command的所有Python版本。                            |
|   pyenv commands   | 列出所有pyenv可用命令行。                                    |
|    pyenv rehash    | 重新加载pyenv的shims路径，即刷新数据库， 安装完Python版本后下需要执行该命令。 |

## Virtualenv部署与使用

### Virtualenv简介

Virtualenv是一个用来为一个应用创建一套“隔离”的Python运行环境，使得每个应用拥有一套“独立”的Python运行环境。Virtualenv通过创建一个虚拟化的python运行环境，将我们所需的依赖安装进去的，不同项目之间相互不干扰。特点：

- 在没有权限的情况下安装新套件
- 不同应用可以使用不同的套件版本
- 套件升级不影响其他应用

### Virtualenv安装部署

```bash
pip install virtualenv
```

![clipboard](680719-20220529163644179-893802653.png)

###  Virtualenv的使用

```bash
[root@localhost ~]# mkdir /study		#创建工作目录
[root@localhost ~]# cd /study/			#进入工作目录
[root@localhost study]# virtualenv venv         #为此工程创建一个虚拟环境，venv为虚拟环境目录名，目录名自定义
```

> **提示：**
>
> **virtualenv venv将会在当前的目录中创建一个文件夹，包含了Python可执行文件，以及pip库的一份拷贝，这样就能安装其他包了。虚拟环境的名字（此例中是 venv ）可以是任意的，若省略名字将会把文件均放在当前目录。**
>
> **在任何你运行命令的目录中，这会创建Python的拷贝，并将之放在叫做 venv 的文件中。**

```bash
[root@localhost study]# virtualenv -p /usr/bin/python2.7 study01   #-p参数指定Python解释器程序路径
[root@localhost study]# source study01/bin/activate	#激活虚拟环境
(study01)[root@localhost study]# deactivate		#退出当前系统环境
```



### Virtualenv常见参数

```bash
# virtualenv [OPTIONS] DEST_DIR 
选项:
--version		#显示当前版本号。 
-h, –help		#显示帮助信息。 
-v, –verbose		#显示详细信息。 
-q, –quiet		#不显示详细信息。 
-p PYTHON_EXE, –python=PYTHON_EXE
#指定所用的python解析器的版本，比如–python=python2.5就使用2.5版本的解析器创建新的隔离环境。
#默认使用的是当前系统安装(/usr/bin/python)的python解析器 
--clear			#清空非root用户的安装，并重头开始创建隔离环境。 
--no-site-packages	#令隔离环境不能访问系统全局的site-packages目录。 
--system-site-packages	#令隔离环境可以访问系统全局的site-packages目录。 
--unzip-setuptools	#安装时解压Setuptools或Distribute 
--relocatable
#重定位某个已存在的隔离环境。使用该选项将修正脚本并令所有.pth文件使用相当路径。 
--distribute
#使用Distribute代替Setuptools，也可设置环境变量VIRTUALENV_DISTRIBUTE达到同样效要。 
--extra-search-dir=SEARCH_DIRS
#用于查找setuptools/distribute/pip发布包的目录。可以添加任意数量的–extra-search-dir路径。 
--never-download
#禁止从网上下载任何数据。此时，如果在本地搜索发布包失败，virtualenv就会报错。 
--prompt==PROMPT	#定义隔离环境的命令行前缀。
```

实操：

```bash
created virtual environment CPython3.11.3.final.0-64 in 1605ms
  creator CPython3Windows(dest=G:\Program Files\python_virtualenv\env_data, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Administrator\AppData\Local\pypa\virtualenv)
    added seed packages: pip==23.1, setuptools==67.6.1, wheel==0.40.0
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
```

windows环境下，在`Scripts`目录下激活，可以看到命令行前面，已经激活了虚拟环境

![image-20230420065938013](image-20230420065938013.png)

另外，在虚拟环境中，直接输入`python`调用即可，不需要加后缀了

![image-20230420071629084](image-20230420071629084.png)

这样我们可以基于不同的python版本，创建不同的环境；也可以基于同一个python初始版本，创建不同应用的不同包的生产环境

![image-20230420070201477](image-20230420070201477.png)

在windows下我们需要手动进入不同的虚拟环境，linux环境下可以使用`update-alternatives`



## update-alternatives部署与使用

update-alternatives是用来维护系统命令的符号链接，以决定系统默认使用什么命令，可以设置系统默认加载的首选程序。即用于处理linux系统中软件版本的切换。

# 使用docker python环境

[Docker 安装 Python ](https://www.runoob.com/docker/docker-install-python.html)

[docker安装并运行python文件](https://www.cnblogs.com/spll/p/17036651.html)

查找镜像：[python Tags | Docker Hub](https://hub.docker.com/_/python/tags)

拉取镜像：

```bash
docker pull python:3.9.16
```



# 使用docker构建Ubuntu桌面开发环境



# python环境迁移部署



# pip镜像

永久配置pip下载镜像源方法（window版本）：https://blog.csdn.net/mghoumin/article/details/126911991

[Python下载第三方库，国内镜像汇总 ](https://zhuanlan.zhihu.com/p/544490001)

```bash
pip3 install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
```



# 第一行 #!/usr/bin/python

[(13条消息) python 第一行 #!/usr/bin/python 详解](https://blog.csdn.net/misayaaaaa/article/details/102309624)

脚本语言的第一行 (只对 Linux/Unix 用户适用) 用来指定本脚本用什么解释器来执行。

#!/usr/bin/python 是告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python 解释器。

#!/usr/bin/env python 这种用法是为了防止操作系统用户没有将 python 装在默认的 /usr/bin 路径里。当系统看到这一行的时候，首先会到 env 设置里查找 python 的安装路径，再调用对应路径下的解释器程序完成操作。



#!/usr/bin/python 相当于写死了 python 路径。

分成两种情况：

（1）如果调用 python 脚本时，使用:

```python
python script.py 
```

\#!/usr/bin/python 被忽略，等同于注释

（2）如果调用python脚本时，使用:

```python
./script.py 
```

\#!/usr/bin/python 指定解释器的路径



#!/usr/bin/env python 会去环境设置寻找 python 目录，可以增强代码的可移植性，推荐这种写法。



