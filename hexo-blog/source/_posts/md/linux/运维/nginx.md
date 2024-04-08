---
title: 'nginx基本实践'
date: 2022-11-13 14:15:24
cover: false
tags:
- Linux
typora-root-url: nginx
---

# 常用网站

- nginx下载网站：[Index of /download/ (nginx.org)](http://nginx.org/download/)

# 安装

[LINUX安装nginx详细步骤](https://blog.csdn.net/t8116189520/article/details/81909574)

## **1.安装依赖包**

```bash
# 一键安装下面四个依赖
yum -y install gcc zlib zlib-devel pcre-devel openssl openssl-devel
```

## **2.下载并解压安装包**

```bash
# 创建一个文件夹
cd /usr/local
mkdir nginx
cd nginx
# 下载tar包
wget http://nginx.org/download/nginx-1.18.0.tar.gz
tar -xvf nginx-1.18.0.tar.gz
```

## **3.安装nginx**

```bash
# 进入nginx目录
cd /usr/local/nginx
# 进入目录
cd nginx-1.18.0
# 执行命令 考虑到后续安装ssl证书 添加两个模块
./configure --with-http_stub_status_module --with-http_ssl_module
//执行make命令
make
# 执行make install命令
make install
```

## **4.启动nginx服务**

```bash
# 打开配置文件
vi /usr/local/nginx/conf/nginx.conf
```

将端口号改成8089(随便挑个端口)，因为可能apeache占用80端口，apeache端口尽量不要修改，我们选择修改[nginx](https://so.csdn.net/so/search?q=nginx&spm=1001.2101.3001.7020)端口。

将localhost修改为你服务器的公网ip地址。

```bash

#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    server {
        listen       8089;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   html;
            index  index.html index.htm;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}

```

## **5.重启nginx**

```bash
/usr/local/nginx/sbin/nginx -s reload
```



## 其他

查看nginx进程

```bash
ps -ef | grep nginx
```

![image-20221113145815065](image-20221113145815065.png)

安装完成一般常用命令

进入安装目录中，

命令： cd /usr/local/nginx/sbin

启动，关闭，重启，命令：

./nginx 启动

./nginx -s stop 关闭

./nginx -s reload 重启

## 配置https

将已获取到的 `cloud.tencent.com_bundle.crt` 证书文件和 `cloud.tencent.com.key` 私钥文件从本地目录拷贝到 Nginx 服务器的 `/usr/local/nginx/conf` 目录（此处为 Nginx 默认安装目录，请根据实际情况操作）下。

配置文件新增server，并根据实际情况修改

```bash
server {
     #SSL 默认访问端口号为 443
     listen 443 ssl; 
     #请填写绑定证书的域名
     server_name cloud.tencent.com; 
     #请填写证书文件的相对路径或绝对路径
     ssl_certificate cloud.tencent.com_bundle.crt; 
     #请填写私钥文件的相对路径或绝对路径
     ssl_certificate_key cloud.tencent.com.key; 
     ssl_session_timeout 5m;
     #请按照以下协议配置
     ssl_protocols TLSv1.2 TLSv1.3; 
     #请按照以下套件配置，配置加密套件，写法遵循 openssl 标准。
     ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE; 
     ssl_prefer_server_ciphers on;
     location / {
         #网站主页路径。此路径仅供参考，具体请您按照实际目录操作。
         #例如，您的网站主页在 Nginx 服务器的 /etc/www 目录下，则请修改 root 后面的 html 为 /etc/www。
         root html; 
         index  index.html index.htm;
     }
 }

```

在 Nginx 根目录下，通过执行以下命令验证配置文件问题：

```bash
./sbin/nginx -t
```

重启nginx

```bash
./sbin/nginx -s reload
```

### HTTP 自动跳转 HTTPS 的安全配置（可选）

略，见原网站

## 配置反向代理nodejs服务

Node.js自身能作为web服务器用，但是如果要在一台机器上开启多个Node.js应用该如何做呢？有一种答案就是使用nginx做反向代理。反向代理在这里的作用就是，当代理服务器接收到请求，将请求转发到目的服务器，然后获取数据后返回。

步骤样例

一、正常使用node.js开启web服务

```js
var http = require('http');
http.createServer(function (request, response) {
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end('hello world
');
}).listen(1337);
console.log('Server running at http://127.0.0.1:1337/');
```

二、为域名配置nginx

```bash
[root@iZ25lzba47vZ vhost]# ls
default.conf               node.ruanwenwu.cn.conf  test.ruanwenwu.conf    www.tjzsyl.com.conf
laravel.ruanwenwu.cn.conf  wss.ruanwenwu.cn.conf  www.tjzsyl.com.conf.bak
[root@iZ25lzba47vZ vhost]# pwd
```

node.ruanwenwu.cn.conf：

```bash
server{
    listen 80;
    server_name node.ruanwenwu.cn;
    location / {
        proxy_pass http://127.0.0.1:1337;
    }
}
```



























