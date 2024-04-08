---
title: 'hadoop'
date: '2022-10-9 09:03:02'
cover: false
tags:
- hadoop
- bigdata
categories: bigdata
typora-root-url: hadoop
---



教程来源：https://www.bilibili.com/video/BV1Qp4y1n7EN?p=1

# 入门

## 1.1.Hadoop是什么

## 1.2.Hadoop发展历史

## 1.3.Hadoop三大发行版本

## 1.4.Hadoop优势

## 1.5.Hadoop组成

### 1.5.1.HDFS概述

### 1.5.2.Yarn架构概述

### 1.5.3.MapReduce架构概述

## 1.6.大数据技术生态体系

## 1.7.推荐系统架构图

# Hadoop运行环境搭建（开发重点）

## 模板虚拟机环境准备

### 安装模板虚拟机

|       IP       | 主机名称  | 内存 | 硬盘 |
| :------------: | :-------: | :--: | :--: |
| 192.168.10.100 | hadoop100 |  4G  | 50G  |

### VMware

虚拟机 VMware Workstation Pro 15.5.0 及永久激活密钥：https://www.cnblogs.com/zero-vic/p/11584437.html

------

15 虚拟机下载地址：https://download3.vmware.com/software/wkst/file/VMware-workstation-full-15.5.0-14665864.exe

16虚拟机下载地址：http://download3.vmware.com/software/wkst/file/VMware-workstation-full-16.1.0-17198959.exe

------

激活密钥许可证VMware Workstation Pro 15 
激活许可证
UY758-0RXEQ-M81WP-8ZM7Z-Y3HDA
VF750-4MX5Q-488DQ-9WZE9-ZY2D6
UU54R-FVD91-488PP-7NNGC-ZFAX6
YC74H-FGF92-081VZ-R5QNG-P6RY4
YC34H-6WWDK-085MQ-JYPNX-NZRA2

激活密钥许可证VMware Workstation Pro 16
激活许可证
ZF3R0-FHED2-M80TY-8QYGC-NPKYF

#### 版本

以下是VMware WorkStation Pro 15.5的安装步骤

- 模拟准备物理硬件

![在这里插入图片描述](7d85d432db81441f9fa84f918b8462cd.png)

![在这里插入图片描述](4cf8b30e0f2a465d99a354f2965b1bf5.png)

![在这里插入图片描述](354790178bbd4dd58ae6e6df147793ff.png)

![在这里插入图片描述](3f1fd0d950184a718e343601196e9a4c.png)

![在这里插入图片描述](b8bd590cefce4d6781f290710b930e37.png)

![在这里插入图片描述](432c2e10017540ca9f31183ded55e14e.png)

这里需要查看下自己的cpu核数，我这里是16核的，后面要新建4台左右的虚拟机，每台处理器的内核总数为，16/4

![在这里插入图片描述](23379a60450a46a48b744261ca412ad6.png)

![image-20211019065226809](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211019065226809.png)

![在这里插入图片描述](c767324fab17405abebf3be1f33baecb.png)

接下来两步，都是默认下一步

![在这里插入图片描述](5b5e4566f8c94befab7468aae983689f.png)

![在这里插入图片描述](5577ab8a706941739a5c1f6bbdf8b0e3.png)

![在这里插入图片描述](c1f74d7f25f84e05b90b8a559b8852f8.png)

![在这里插入图片描述](3fc1e57213a74023a50c257e60f0070a.png)

如果虚拟化没有开启，报的是以下错误

![在这里插入图片描述](84dd88112ccc4c29a0e7fdd92ebc9f9d.png)

Win10直接可以在任务管理器中的【性能】面看查看，Win7则需要进入bios中查看



### CentOS

系统的安装得分两步，第一步得配置一台电脑，选CPU、内存、磁盘、网卡等硬件

第二步才是安装系统

[CentOS-7-x86_64-DVD-1804.iso](http://mirrors.sohu.com/centos/7.5.1804/isos/x86_64/CentOS-7-x86_64-DVD-1804.iso)

安装系统前，得开启一下Bios

进入虚拟机，选好iso镜像文件后，点击确定

注意是要有DVD的后缀的

然后开启虚拟机

![在这里插入图片描述](6bbcc9b158484536856b2500a5099402.png)

进入后，保持默认敲回车，

进入语言选择界面

![在这里插入图片描述](9cb6b8b3a00f4de681f57056b84e8578.png)

继续后，进行其他设置

![在这里插入图片描述](8e65a4d4f4964c2abbf70be975445b49.png)

设置日期和时间

软件-软件选择

![在这里插入图片描述](d04e0ee59cc34ba7ad3cb010fe8a891f.png)

可以保持默认，初始学习阶段，可以使用桌面，后续可以切换到最小安装的功能

系统-安装位置

自己配置分区

![在这里插入图片描述](69eca70f95694562bc3b462e52133451.png)

添加1g的boot挂载点，文件系统修改为ex4

![在这里插入图片描述](cd6e0c0e303b4ba5a03f5e13272bccec.png)

添加4g的swap分区

![在这里插入图片描述](e5c2e4ded577427db48e07c5f53b6b9a.png)

剩余45g的分区挂载到根目录

![在这里插入图片描述](bfda9499f9cd408b84174801f3cf0bfe.png)

点击完成，接受并更改

学习阶段禁用kdump，生产阶段需要启用，可以看系统崩溃前夕的日志

配置网络和主机名称，打开网络，主机名是hadoop100

后续会学习如何在命令行中配置

![在这里插入图片描述](0db3ccd597e9498d9baecba235644074.png)

安全策略，保持默认打开



安装过程中，可以配置下密码

学习阶段的密码：111111，系统会提示是一个弱密码，点击两次强制确定

暂时不用创建用户

加载完后重启

接受许可协议

![在这里插入图片描述](210d2bf2a4fc4b6bb1afb37d34a69cf6.png)

语言选择中文，时区选择上海，

其他的默认

设置账号，密码保持一致，这里是111111

![在这里插入图片描述](a2e064d735d144a5a211692594b0f361.png)

至此虚拟机安装完成

![在这里插入图片描述](ae9462e61a5b4bf89de69c94dafffa6f.png)

### 配置IP和主机名称

vmware的菜单栏，点击编辑>虚拟网络编辑器

![在这里插入图片描述](9454b937db514e0a9047f9d0bb5fe96c.png)

点击NAT设置

![在这里插入图片描述](70dece7483e7421295396146354475b1.png)

此时虚拟机的IP地址配置完成

然后配置本机的Vmware Network Adapter VMnet8设置：

路径：控制面板\网络和 Internet\网络连接

![在这里插入图片描述](01039d71db274bbd832c7c54cfec067a.png)

右键属性：

![在这里插入图片描述](bd4c4e140a1d4f5bb03773dc1c8d0b47.png)

如果vmnet8没出来，在vmware菜单栏，虚拟网络编辑器处，点击还原默认设置即可

- 修改ip地址

进入hadoop01

su root，输入密码111111

编辑：`vim /etc/sysconfig/network-scripts/ifcfg-ens33`

```
修改为静态获取ip，否则每次重启系统，ip地址都会变化的
BOOTPROTO="static" 
# 有的是没有引号的，和上下文保持一致
```



完整配置

```
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no

#改为静态获取ip
BOOTPROTO=static

DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=ens33
UUID=66119999-13b4-4d2b-8943-68612a85156f  # 随机id
DEVICE=ens33  # 接口名（设备、网卡）
ONBOOT=yes  # 系统启动的时候网络接口是否有效（yes/no）

# IP地址
IPADDR=192.168.10.100
# 网关
GATEWAY=192.168.10.2
# 域名解析器
DNS1=192.168.10.2

```

- 修改主机名称

`vi /etc/hostname`

```
hadoop100
```

- 修改主机名称映射

`vim /etc/hosts`

完整配置如下：

```
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

192.168.10.100 hadoop100
192.168.10.101 hadoop101
192.168.10.102 hadoop102
192.168.10.103 hadoop103
192.168.10.104 hadoop104
192.168.10.105 hadoop105
192.168.10.106 hadoop106
192.168.10.107 hadoop107
192.168.10.108 hadoop108

```

最后`reboot`重启一下

查看一下ip：

`ifconfig`

```
[root@hadoop100 sai]# ifconfig
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.10.100  netmask 255.255.255.0  broadcast 192.168.10.255
        inet6 fe80::7f40:9399:9c40:3ab8  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:b2:d0:f5  txqueuelen 1000  (Ethernet)
        RX packets 56  bytes 19427 (18.9 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 68  bytes 8539 (8.3 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

```

`inet 192.168.10.100  netmask 255.255.255.0  broadcast 192.168.10.255`

如果linux的ip没有更改

```
service network restart
```



ping一下外网：

```
[root@hadoop100 sai]# ping www.baidu.com
PING www.a.shifen.com (14.215.177.38) 56(84) bytes of data.
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=1 ttl=128 time=29.2 ms
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=2 ttl=128 time=29.4 ms
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=3 ttl=128 time=28.9 ms
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=4 ttl=128 time=29.1 ms

```

是可以的





如果隔了几天之后，提示网络不可达，最大的可能性，就是Windows下的Vm虚拟机的DHCP，在某次你杀毒或者清理启动项的时候，被关掉了

按下键盘`win`+`R`，输入`services.msc`

手动打开Vm相关启动项：

![image-20211207065804610](image-20211207065804610.png)

测试一下，在linux中ping，可以正常连接了

### 远程终端工具安装

安装xshell，远程登录192.168.10.100

![在这里插入图片描述](056c988adbfb49eaba27c0ef7d55b92f.png)



在windows中修改主机名称映射：

进入`C:\Windows\System32\drivers\etc`

修改hosts文件，将

```
192.168.10.100 hadoop100
192.168.10.101 hadoop101
192.168.10.102 hadoop102
192.168.10.103 hadoop103
192.168.10.104 hadoop104
192.168.10.105 hadoop105
192.168.10.106 hadoop106
192.168.10.107 hadoop107
192.168.10.108 hadoop108
```

复制到最后并保存后，就可以用hostname远程登录了：

![在这里插入图片描述](619bea2c3b404f9298ea16e6d09ecc35.png)

win10由于权限问题，需要将hosts整个文件先复制一份，然后修改，最后替换原来的hosts，win7直接修改即可



linux虚拟机

ip：192.168.10.100

网关：192.168.10.2

DNS1：192.168.10.2



Vmware 虚拟网络编辑器

子网IP：192.168.10.0

子网掩码：255.255.255.0

网关：192.168.10.2



windows电脑 VMnet8

IP：192.168.10.1

子网掩码：255.255.255.0

默认网关：192.168.10.2



dns1：192.168.10.2

dns2：8.8.8.8





### 模板虚拟机基础配置

hadoop100虚拟机配置如下，本文Linux系统全部以centos 7.5-x86-1804为例

- ping一下百度，测试网络连通情况

- 安装`epel-release`

- 注：Extart Packages for Enterprise Linux是“红帽系”的操作系统，提供的额外的软件包，适用于RHEL、CENTOS和Scientific Linux。相当于是一个软件仓库，大多数rpm包在官方repository中是找不到的

  ```
  yum install -y epel-release
  ```

- 如果linux安装的是最小系统版，还需要安装如下工具，如果安装的是Linux桌面标准版，则不需要

  - net-tool：工具包集合，包含Ifconfig等命令

    ```
    yum install -y net-tools
    ```

  - vim编辑器

    ```
    yum install -y vim
    ```

- 关闭防火墙，以及关闭防火墙开机自启

  ```
  systemctl stop firewalld
  systemctl disable firewalld.service
  
  [root@hadoop100 yum.repos.d]# systemctl disable firewalld.service
  Removed symlink /etc/systemd/system/multi-user.target.wants/firewalld.service.
  Removed symlink /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service.
  
  ```

- 创建atguigu用户，并修改atguigu用户密码

  ```
  useradd atguigu
  passwd atguigu
  111111
  ```

  - 配置atguigu用户，具有root权限

    ```
    vim /etc/sudoers
    
    ## Allows people in group wheel to run all commands
    %wheel  ALL=(ALL)       ALL
    
    # 添加如下配置
    atguigu ALL=(ALL)       NOPASSWD:ALL
    
    ```

  - 注意，不要放在root行下面，因为所有用户都属于wheel组，否则执行到%wheel行时，配置就被覆盖了

- 在/opt目录下创建文件夹，并修改所属主和所属组

  - 在opt目录下，创建module和software文件夹

    ```
    mkdir module
    mkdir software
    ```

  - 修改用户和用户组为atguigu

    ```
    chown atguigu:atguigu /opt/module/ opt/software/
    ```

- 写在虚拟机自带的JDK（如果是最小化安装，则跳过这一步）

  ```
  rpm -qa | grep -i java | xargs -n1 | rpm -e --nodeps
  ```

  - rpm -qa：查询所安装的所有rpm包
  - grep -i：忽略大小写

### 主机内存不够怎么办

使用Docker



## 克隆虚拟机



## 2.3.在hadoop102安装JDK



## 2.4.在hadoop102安装Hadoop



## 2.5.Hadoop目录结构

# 第三章、MapReduce



# 第四章、Hadoop源码解析



# 第五章、生产调优手册



# 第六章、Yarn

