---
title: 'linux基础'
date: 2022-8-9 09:03:02
cover: false
---



# 常见命令

## yum

### 参考链接

[yum源配置的三种方法 - Huidoo_Yang - 博客园 (cnblogs.com)](https://www.cnblogs.com/yangp/p/8506264.html)

#### yum源概述

yum需要一个yum库，也就是yum源。默认情况下，CentOS就有一个yum源。

在/etc/yum.repos.d/目录下有一些默认的配置文件（可以将这些文件移到/opt下，或者直接在yum.repos.d/下重命名）。

首先要找一个yum库（源），然后确保本地有一个客户端（yum这个命令就是客户端），由yum程序去连接服务器。

连接的方式是由配置文件决定的。通过编辑/etc/yum.repos.d/CentOS-Base.repo文件，可以修改设置。



打开CentOS-Base.repo文件，可以看到url路径是CentOS的官网自身的yum源，

[http://mirrorlist.centos.org/?release=releasever&arch=releasever&arch=basearch&repo=os](http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os)。

可以将这个mirrorlist注释掉，然后将baseurl设置成国内的阿里云源http://mirrors.aliyun.com/repo/Centos-6.repo，

也可以在用于大量的rpm包的前提下设置成自己的本地文件系统（挂载目录），需要移除CentOS-Base.repo文件，并编辑CentOS-Media.repo文件。

```
name=Description#一个描述，随意。
baseurl=#设置资源库的地址，可以写阿里云也可以是自己的yum
    ftp://
    http://
    file:///
enabled={1|0}#enabled=1开启本地更新模式
gpgcheck={1|0}# gpgcheck=1表示检查；可以不检查gpgcheck=0
gpgkey=#检查的key；如果上面不检查这一行可以不写。
```

### yum源配置方法一（阿里云源）

#### 1) 安装wget

```
yum install -y wget
```

#### 2) 备份/etc/yum.repos.d/CentOS-Base.repo文件

```
cd /etc/yum.repos.d/
mv CentOS-Base.repo CentOS-Base.repo.back
```

#### 3) 下载阿里云的Centos-6.repo文件

```
wget -O CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo
wget -O CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
```

#### 4) 重新加载yum

```
yum clean all

已加载插件：fastestmirror, langpacks
正在清理软件源： base epel extras updates
Cleaning up everything
Maybe you want: rm -rf /var/cache/yum, to also free up space taken by orphaned data from disabled or removed repos
Cleaning up list of fastest mirrors


```



```
yum makecache
```

### yum源配置方法二（本地挂载目录）

#### 1) 下载iso文件

　　从CentOS的官网](http://isoredirect.centos.org/centos/6/isos/)下载CentOS的完整版iso文件，并上传到Linux文件系统中，例如/opt/tools/。

http://isoredirect.centos.org/centos/7/isos/x86_64/

如果是虚拟机的话，直接就可以用一开始的iso文件

#### 2) 创建挂载目录

　　为iso文件的挂载创建目录。

```
mkdir /mnt/vcdrom
```

#### 3) 挂载

　　将iso文件挂载到挂载目录。

```
mount -o loop -t iso9660 /opt/tools/CentOS-6.7-x86_64-bin-DVD1.iso /mnt/vcdrom
```

#### 4) 移除或备份Centos-Base.repo文件

```
cd /etc/yum.repos.d/
mv Centos-Base.repo Centos-Base.repo.back
```

#### 5) 编辑Centos-Media.repo文件

```
vim /etc/yum.repos.d/Centos-Media.repo
```



```
name=CentOS-$releasever - Media

baseurl=file:///mnt/vcdrom/#将baseurl修改为DVD的挂载目录

gpgcheck=1

enabled=1#开启本地更新模式
```



#### 6) 重新加载yum

```
yum clean all
yum makecache
```

#### 7) 编写脚本并开机自动挂载

　　首先，编写脚本。

```
vim /opt/shell/mymount.sh
#!/bin/bash
#
mount -o loop -t iso9660 /opt/tools/CentOS-6.7-x86_64-bin-DVD1.iso /mnt/vcdrom
```

　　其次，修改脚本执行权限。

```
chmod 777 /opt/shell/mymount.sh
```

　　再次，修改/etc/rc.local配置文件。

```
vim /etc/rc.local
```

　　在文件最后一行加上如下

```
/opt/shell/mymount.sh
```

　　最后，重启机器测试。

```
init 6 
```

## wget

### 参考链接

[wget命令详解 - 随性i - 博客园 (cnblogs.com)](https://www.cnblogs.com/sx66/p/11887022.html)

### wget概述

wget是Linux中的一个下载文件的工具，wget是在Linux下开发的开放源代码的软件，作者是Hrvoje Niksic，后来被移植到包括Windows在内的各个平台上。

它用在命令行下。对于Linux用户是必不可少的工具，尤其对于网络管理员，经常要下载一些软件或从远程服务器恢复备份到本地服务器。

如果我们使用虚拟主机，处理这样的事务我们只能先从远程服务器下载到我们电脑磁盘，然后再用ftp工具上传到服务器。这样既浪费时间又浪费精力，那不没办法的事。

而到了Linux VPS，它则可以直接下载到服务器而不用经过上传这一步。

wget工具体积小但功能完善，它支持断点下载功能，同时支持FTP和HTTP下载方式，支持代理服务器和设置起来方便简单。

## vim/vi

- yy：复制某一行
- p：粘贴复制的行

## systemctl

## firewalld

## useradd

## grep

# 常见命令参数含义

## yum

```
yum install -y wget
-y(当安装过程提示选择全部为"yes")
```

### yum clean all

```
杂谈
========
相关介绍：
今天发现一台机器/var > 70% ,查了下是/var/cache/yum目录。

使用yum clean all 清除，很方便，绕开了没有root权限的问题。
该命令介绍如下，作用：清除YUM缓存。
yum 会把下载的软件包和header存储在cache中，而不自动删除。如果觉得占用磁盘空间，可以使用yum clean指令进行清除，
更精确 的用法是
yum clean headers清除header，
yum clean packages清除下载的rpm包，
yum clean all一全部清除。

```

### yum repolist



### yum makecache

参考：[为centos7配置阿里yum源遇到的问题以及解决方法 - 我得去图书馆了 - 博客园 (cnblogs.com)](https://www.cnblogs.com/xuelisheng/p/11452926.html)

执行yum makecache，配置阿里云源的那一步，一直报如下错误

```
extras/7/x86_64/primary_db     FAILED                                          
http://mirrors.aliyun.com/centos/7/extras/x86_64/repodata/db1c88508275ffebdc6cd8686da08745d2552e5b219b2e6f4cbde7b8afd3b1a3-primary.sqlite.bz2: [Errno 14] curl#6 - "Could not resolve host: mirrors.aliyun.com; Unknown error"6 MB  00:02:12 ETA 
正在尝试其它镜像。
```

【解决方法】

在网上找了好多帖子，都没能解决我的问题，后来看到是HTTP请求失败，尝试本地访问之前wget下来的 CentOS-Base.repo 发现其中的：

http://mirrors.aliyun.com/centos/$releasever/os/$basearch/

等URL通过http的形式根本无法访问，

此时将变量$releasever改为7（我的系统是centos 7），发现可以访问了，

顺便将所有的变量$releasever都改为7。

感觉这个变量$releasever根本就没起作用呀。

改完之后，执行yum clean all 以及 yum makecache 成功。



### /var/run/yum.pid 已被锁定

删除/var/run/yum.pid就可以正常使用了，即rm -rf /var/run/yum.pid.

## wget

[ Linux —— wget -qO- 命令详解_洛丹伦的夏天-CSDN博客_wget-o](https://blog.csdn.net/qq_32331073/article/details/79239323)

### wget -qO- 命令详解

参数
URL：下载指定的URL地址。

其中 -O：下载并以指定的文件名保存

```
wget -O wordpress.zip http://www.linuxde.net/download.aspx?id=1080
```


wget默认会以最后一个符合/的后面的字符来命名，对于动态链接的下载通常文件名会不正确。

**错误**：下面的例子会下载一个文件并以名称download.aspx?id=1080保存:

wget http://www.linuxde.net/download?id=1
即使下载的文件是zip格式，它仍然以download.php?id=1080命名。

**正确**：为了解决这个问题，我们可以使用参数-O来指定一个文件名：

```
wget -O wordpress.zip http://www.linuxde.net/download.aspx?id=1080
```

**特殊的：**

-O file（--output-document=file）
     The documents will not be written to the appropriate files, but all will be concatenated together and written to file.  If - is used as file, documents will be  printed to standard output, disabling link conversion.  (Use ./- to print to a file literally named -.)

表示：wget 会把url中获取的数据统一写入 '-O' 指定的file中。
        wget -O-   以'-'作为file参数，那么数据将会被打印到标准输出，通常为控制台。
        wget -O ./-   以'./-'作为file参数，那么数据才会被输出到名为'-'的file中。

## grep

### grep -i

忽略大小写

# 常用目录

## /etc

### /etc/yum.repos.d/

### /etc/systemd

### /etc/sudoers

## /var

### /var/cache/yum

### /var/run/yum.pid

































用户和用户组：http://c.biancheng.net/view/3038.html

账户和用户是一个概念

在登录系统时，只有正确输入用户名和密码，才能进入系统和自己的主目录

用户组是具有相同特征用户的逻辑集合

用户和用户组的对应关系有以下 4 种：

1. 一对一：一个用户可以存在一个组中，是组中的唯一成员；
2. 一对多：一个用户可以存在多个用户组中，此用户具有这多个组的共同权限；
3. 多对一：多个用户可以存在一个组中，这些用户具有和组相同的权限；
4. 多对多：多个用户可以存在多个组中，也就是以上 3 种关系的扩展。



https://www.runoob.com/linux/linux-user-manage.html

```
useradd 选项 用户名
```

参数说明：

- 选项:

  - -c comment 指定一段注释性描述。
  - -d 目录 指定用户主目录，如果此目录不存在，则同时使用-m选项，可以创建主目录。
  - -g 用户组 指定用户所属的用户组。
  - -G 用户组，用户组 指定用户所属的附加组。
  - -s Shell文件 指定用户的登录Shell。
  - -u 用户号 指定用户的用户号，如果同时有-o选项，则可以重复使用其他用户的标识号。

- 用户名:

  指定新账号的登录名。

修改用户账号就是根据实际情况更改用户的有关属性，如用户号、主目录、用户组、登录Shell等



sudo su

https://www.cnblogs.com/mrcln/p/6117267.html

sed

https://www.runoob.com/linux/linux-comm-sed.html



查看磁盘情况：fdisk -l
查看磁盘挂载情况：df -h

CentOS7 挂载磁盘出错mount: /dev/sdb is write-protected, mounting mount: unknown filesystem type '(null)'
https://blog.csdn.net/llwy1428/article/details/93848439

centos7磁盘分区与挂载解析
https://www.cnblogs.com/lizhangshu/p/9719018.html

linux怎么分多个区,linux 分两个区的方法（FAT32，EXT4）
https://blog.csdn.net/weixin_39631667/article/details/116884907

Linux命令大全
http://ipcmen.com/lsblk

配置/etc/fstab参数实现开机自动挂载
https://www.cnblogs.com/unclemac/p/12783396.html

anaconda-ks.cfg
这个文件记录的是安装系统时的一些信息
那这个文件有什么用呢？
这个配置文件经修改之后可以用于雷同环境下，使用Kickstart来自动安装大量同样的操作系统
系统安装的时候生成的一个文件，通过这个文件可以修改成自动安装的脚本,用于自动安装同样配置的系统
https://blog.csdn.net/whyhonest/article/details/7555229#commentBox

给磁盘根目录扩容
https://www.jb51.net/article/144291.htm
https://www.cnblogs.com/liyy7520/p/11905979.html
你不能挂到根目录下呀。你原来的系统是根目录。你挂载到根目录下那系统不就挂了？
你可以新建一个目录。然后把新加的硬盘。通过fdisk 进行分区。格式化后挂载到别的目录下。
如果系统做了lvm，就直接把这个硬盘加到卷组里使用。然后调整逻辑卷的分区大小

现在的问题是没有做lvm

pvcreate命令不存在解决方案
https://blog.csdn.net/weixin_34177064/article/details/91561425

linux磁盘没做lvm怎么扩容,简述linux下lvm 磁盘扩容
https://blog.csdn.net/weixin_42410566/article/details/116736556

LVM管理(很细致以及系统)
https://www.cnblogs.com/diantong/p/10554831.html
云服务器centos6.5调整home根目录大小
http://blog.itpub.net/69957453/viewspace-2757328/
fuser 命令小结
https://www.cnblogs.com/yuboyue/archive/2011/07/18/2109838.html
记录一次华为云服务器给根目录扩容（底下还有好多链接）
https://www.cnblogs.com/homjun/p/14266004.html


Linux修改hostname时/etc/hosts、/etc/sysconfig/network ，hostname，三者的区别和联系
https://www.cnblogs.com/itfat/p/9212698.html