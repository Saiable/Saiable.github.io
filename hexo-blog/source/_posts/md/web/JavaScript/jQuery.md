---
title: 'jQuery'
date: 2022-08-08 07:15:24
cover: false
tags:
- jQuery
categories: 'jQuery'

---

# jQuery

## jQuery - AJAX

### jQuery - AJAX 简介

简短地说，在不重载整个网页的情况下，AJAX 通过后台加载数据，并在网页上进行显示。

 **如果没有 jQuery，AJAX 编程还是有些难度的。**

编写常规的 AJAX 代码并不容易，因为不同的浏览器对 AJAX 的实现并不相同。这意味着您必须编写额外的代码对浏览器进行测试。不过，jQuery 团队为我们解决了这个难题，我们只需要一行简单的代码，就可以实现 AJAX 功能。

 [jQuery AJAX 简介](https://www.runoob.com/jquery/jquery-ajax-intro.html)

[jQuery – AJAX get() 和 post() 方法](https://www.runoob.com/jquery/jquery-ajax-get-post.html) 

### jQuery - AJAX load() 方法

load() 方法从服务器加载数据，并把返回的数据放入被选元素中。

`$(selector).load(URL,data,callback);`

必需的 *URL* 参数规定您希望加载的 URL。

可选的 *data* 参数规定与请求一同发送的查询字符串键/值对集合。

可选的 *callback* 参数是 load() 方法完成后所执行的函数名称。

```javascript
$(document).ready(function(){
	$("button").click(function(){
		$("#div1").load("/try/ajax/demo_test.txt");
	});
});
```

下面的例子把 "demo_test.txt" 文件中 id="p1" 的元素的内容，加载到指定的` <div> `元素中：

```javascript
$("#div1").load("demo_test.txt #p1");
```

回调函数可以设置不同的参数：

- *responseTxt* - 包含调用成功时的结果内容
- *statusTXT* - 包含调用的状态
- *xhr* - 包含 XMLHttpRequest 对象

```javascript
$("button").click(function(){
  $("#div1").load("demo_test.txt",function(responseTxt,statusTxt,xhr){
    if(statusTxt=="success")
      alert("外部内容加载成功!");
    if(statusTxt=="error")
      alert("Error: "+xhr.status+": "+xhr.statusText);
  });
});
```

为了避免多页面情形下的代码重复，可以利用 load() 方法，将重复的部分（例如导航栏）放入单独的文件，使用下列方法进行导入：

```javascript
//1.当前文件中要插入的地方使用此结构：
<div class="include" file="***.html"></div>

//2.***.html中放入内容，用html格式仅仅因为会有编辑器的书写辅助。。

//3.代码：
$(".include").each(function() {
    if (!!$(this).attr("file")) {
        var $includeObj = $(this);
        $(this).load($(this).attr("file"), function(html) {
            $includeObj.after(html).remove(); //加载的文件内容写入到当前标签后面并移除当前标签
        })
    }
});
或者在index文件里只写重复部分，剩下的一股脑放各自单独文件 load() 进来~
```

### jQuery - AJAX get() 和 post() 方法

两种在客户端和服务器端进行请求-响应的常用方法是：GET 和 POST。

- *GET* - 从指定的资源请求数据
- *POST* - 向指定的资源提交要处理的数据

GET 基本上用于从服务器获得（取回）数据。注释：GET 方法可能返回缓存数据。

POST 也可用于从服务器获取数据。不过，POST 方法不会缓存数据，并且常用于连同请求一起发送数据。

$.get() 方法通过 HTTP GET 请求从服务器上请求数据。

`$.get(URL,callback);`

```javascript
$("button").click(function(){
  $.get("demo_test.php",function(data,status){
    alert("数据: " + data + "\n状态: " + status);
  });
});
```

$.get() 的第一个参数是我们希望请求的 URL（"demo_test.php"）。

第二个参数是回调函数。第一个回调参数存有被请求页面的内容，第二个回调参数存有请求的状态。

$.post() 方法通过 HTTP POST 请求向服务器提交数据。

`$.post(URL,data,callback);`

```javascript
$("button").click(function(){
    $.post("/try/ajax/demo_test_post.php",
    {
        name:"菜鸟教程",
        url:"http://www.runoob.com"
    },
    function(data,status){
        alert("数据: \n" + data + "\n状态: " + status);
    });
});
```

$.post() 的第一个参数是我们希望请求的 URL ("demo_test_post.php")。

然后我们连同请求（name 和 url）一起发送数据。

"demo_test_post.php" 中的 PHP 脚本读取这些参数，对它们进行处理，然后返回结果。

第三个参数是回调函数。第一个回调参数存有被请求页面的内容，而第二个参数存有请求的状态。

**提示：** 这个 PHP 文件 ("demo_test_post.php") 类似这样：

```php
<?php
$name = isset($_POST['name']) ? htmlspecialchars($_POST['name']) : '';
$url = isset($_POST['url']) ? htmlspecialchars($_POST['url']) : '';
echo '网站名: ' . $name;
echo "\n";
echo 'URL 地址: ' .$url;
?>
```

### GET 和 POST 方法的区别：

**1、发送的数据数量**

在 GET 中，只能发送有限数量的数据，因为数据是在 URL 中发送的。

在 POST 中，可以发送大量的数据，因为数据是在正文主体中发送的。

**2、安全性**

GET 方法发送的数据不受保护，因为数据在 URL 栏中公开，这增加了漏洞和黑客攻击的风险。

POST 方法发送的数据是安全的，因为数据未在 URL 栏中公开，还可以在其中使用多种编码技术，这使其具有弹性。

**3、加入书签中**

GET 查询的结果可以加入书签中，因为它以 URL 的形式存在；而 POST 查询的结果无法加入书签中。

**4、编码**

在表单中使用 GET 方法时，数据类型中只接受 ASCII 字符。

在表单提交时，POST 方法不绑定表单数据类型，并允许二进制和 ASCII 字符。

**5、可变大小**

GET 方法中的可变大小约为 2000 个字符。

POST 方法最多允许 8 Mb 的可变大小。

**6、缓存**

GET 方法的数据是可缓存的，而 POST 方法的数据是无法缓存的。

**7、主要作用**

GET 方法主要用于获取信息。而 POST 方法主要用于更新数据。

[get方法与post方法对比](
