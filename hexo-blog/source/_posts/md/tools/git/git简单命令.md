---
title: 'git简单命令'
date: 2022-7-8 07:15:24
cover: false
tags:
- git
categories: git
---



# 更新`git`

https://blog.csdn.net/w544924116/article/details/119360491

实操是在腾讯云主机上装的

在Linux/Centos服务器上，如果使用的git版本过低，使用的时候可能会由于低版本不支持遇到各种问题，比如[Centos7](https://so.csdn.net/so/search?q=Centos7&spm=1001.2101.3001.7020)系统自带的git版本一般是1.8.3.1的，比较旧，通常建议升级git后再使用。下面我们来说下如果升级git最新版本。

先安装下各种前置包

```bash
yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel 
yum install -y curl curl-devel
yum -y install perl-devel perl-CPAN
yum install tcl  build-essential tk gettext
yum install perl-ExtUtils-MakeMaker package
yum install gettext-devel
```

备注：如果是在卸载`git`之后再安装这些包，还需要重新卸载git，这里面好像有个把git重装了

1、查看git版本

```bash
git --version
```

查看当前git版本，看git版本是否过旧。

2、安装依赖
源代码安装和编译git，需要安装依赖，具体命令如下：

```bash
yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel asciidoc
yum install gcc perl-ExtUtils-MakeMaker
```

出现Complete!则代表安装成功

3、卸载git（旧版本）

```js
yum remove git
```

4、打开文件夹

```bash
cd /usr/local/src/
```

5、下载git压缩包

使用国内指定下载最新版本，目前最新版是v2.9.5，可以复制下链接`https://mirrors.edge.kernel.org/pub/software/scm/git/`，上去看一下

```bash
wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.9.5.tar.xz	
```

6、解压

```bash
tar -xvf git-2.9.5.tar.xz
```

 7、打开解压好的git文件夹

```bash
cd git-2.9.5
```

 8、编译

```bash
make prefix=/usr/local/git all
```

报错1 ：

```bash
[root@VM-4-12-centos git-2.9.5]# make prefix=/usr/local/git all
    CC http.o
In file included from http.c:2:0:
http.h:6:23: fatal error: curl/curl.h: No such file or directory
 #include <curl/curl.h>
                       ^
compilation terminated.
make: *** [http.o] Error 1


```

问题原因：缺少依赖库

解决办法：

```bash
yum -y install curl-devel 
```

报错2：

```bash

http-push.c:18:19: fatal error: expat.h: No such file or directory
 #include <expat.h>
                   ^
```

解决办法：

```bash
yum install expat-devel 
```

报错3：

```bash
make[1]: *** [perl.mak] Error 2
make: *** [perl/perl.mak] Error 2
```

解决办法：

```bash
yum install perl-ExtUtils-MakeMaker package
```

https://note.youdao.com/s/dEaLK17t

 9、安装git

```bash
make prefix=/usr/local/git install
```

出现如下表示安装成功：

```bash
remote_curl_aliases="git-remote-https git-remote-ftp git-remote-ftps" && \
for p in $remote_curl_aliases; do \
        rm -f "$execdir/$p" && \
        test -z "" && \
        ln "$execdir/git-remote-http" "$execdir/$p" 2>/dev/null || \
        ln -s "git-remote-http" "$execdir/$p" 2>/dev/null || \
        cp "$execdir/git-remote-http" "$execdir/$p" || exit; \
done && \
./check_bindir "z$bindir" "z$execdir" "$bindir/git-add"

```



10、配置环境变量
 写到环境变量中

```bash
echo "export PATH=$PATH:/usr/local/git/bin" >> /etc/profile && source /etc/profile
```

最好是手动写，并重启，`export`没写进去

11、验证git版本

再次查看当前版本，验证是否已更新

安装之后 git --version 仍然是旧版本

# 提交`git`

现在需要使用`token`来提交了

https://note.youdao.com/s/6bRkUL42

已设置过期时间

```
git remote set-url origin https://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@github.com/Saiable/cognition

git remote set-url origin https://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@github.com/Saiable/saiable.github.io


```

# 在 GitHub 上搭建个人网站（github.io）

https://note.youdao.com/s/Pqu6oeCM

https://docs.github.com/cn/pages/getting-started-with-github-pages/about-github-pages





## ssh

Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.



# 创建cdn

[(18条消息) 免费开源CDN jsDelivr使用_鹿码的博客-CSDN博客_jsdelivr](https://blog.csdn.net/Mrlujiao_code/article/details/113309542)

[github创建tag-前端开发博客 (caibaojian.com)](http://caibaojian.com/github-create-tag.html)