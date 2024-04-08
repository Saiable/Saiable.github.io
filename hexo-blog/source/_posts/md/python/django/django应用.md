---
title: 'django应用'
date: 2023-07-13 09:03:02
cover: false
tags:
- Django
- python
categories: Django
typora-root-url: django应用
---
# Django概述

官网：[编写你的第一个 Django 应用，第 1 部分 | Django 文档 | Django (djangoproject.com)](https://docs.djangoproject.com/zh-hans/4.2/intro/tutorial01/)

## 安装

```bash
pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 新建项目

选择进入一个文件夹，新建项目

```bash
django-admin startproject project_name
```

![image-20230714090800969](image-20230714090800969.png)

文件介绍

```bash
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

- 最外层的 `mysite/` 根目录只是你项目的容器， 根目录名称对 Django 没有影响，你可以将它重命名为任何你喜欢的名称。
- `manage.py`: 一个让你用各种方式管理 Django 项目的命令行工具。你可以阅读 [django-admin 和 manage.py](https://docs.djangoproject.com/zh-hans/4.2/ref/django-admin/) 获取所有 `manage.py` 的细节。
- 里面一层的 `mysite/` 目录包含你的项目，它是一个纯 Python 包。它的名字就是当你引用它内部任何东西时需要用到的 Python 包名。 (比如 `mysite.urls`).
- `mysite/__init__.py`：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。如果你是 Python 初学者，阅读官方文档中的 [更多关于包的知识](https://docs.python.org/3/tutorial/modules.html#tut-packages)。
- `mysite/settings.py`：Django 项目的配置文件。如果你想知道这个文件是如何工作的，请查看 [Django 配置](https://docs.djangoproject.com/zh-hans/4.2/topics/settings/) 了解细节。
- `mysite/urls.py`：Django 项目的 URL 声明，就像你网站的“目录”。阅读 [URL调度器](https://docs.djangoproject.com/zh-hans/4.2/topics/http/urls/) 文档来获取更多关于 URL 的内容。
- `mysite/asgi.py`：作为你的项目的运行在 ASGI 兼容的 Web 服务器上的入口。阅读 [如何使用 ASGI 来部署](https://docs.djangoproject.com/zh-hans/4.2/howto/deployment/asgi/) 了解更多细节。
- `mysite/wsgi.py`：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。阅读 [如何使用 WSGI 进行部署](https://docs.djangoproject.com/zh-hans/4.2/howto/deployment/wsgi/) 了解更多细节。

启动：

```bash
python manage.py runserver 8080
```

## 创建应用

```bash
python manage.py startapp polls
```

该应用的目录结构如下：

```bash
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

## 注册应用

在项目的 `settings.py`中 `INSTALLED_APPS`字段中，注册app

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
  
    'dataTask.apps.DatataskConfig', # 其实就是告诉这个app的配置类的位置：dataTask目录下的apps.py文件中的DatataskConfig类
]
```

## 编写 `url`和视图函数映射关系

 `polls/views.py`

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

这是 Django 中最简单的视图。如果想看见效果，我们需要将一个 URL 映射到它——这就是我们需要 URLconf 的原因了。

在polls目录中，新建 `urls.py`

 `polls/urls.py`

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

下一步是要在根 URLconf 文件中指定我们创建的 `polls.urls` 模块。在 `mysite/urls.py` 文件的 `urlpatterns` 列表里插入一个 `include()`， 如下：

 `mysite/urls.py`

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

函数 [`include()`](https://docs.djangoproject.com/zh-hans/4.2/ref/urls/#django.urls.include) 允许引用其它 URLconfs。每当 Django 遇到 [`include()`](https://docs.djangoproject.com/zh-hans/4.2/ref/urls/#django.urls.include) 时，它会截断与此项匹配的 URL 的部分，并将剩余的字符串发送到 URLconf 以供进一步处理。

我们设计 [`include()`](https://docs.djangoproject.com/zh-hans/4.2/ref/urls/#django.urls.include) 的理念是使其可以即插即用。因为投票应用有它自己的 URLconf( `polls/urls.py` )，他们能够被放在 `"/polls/" ， "/fun_polls/" ，"/content/polls/"`，或者其他任何路径下，这个应用都能够正常工作

现在把 `index` 视图添加进了 URLconf。通过以下命令验证是否正常工作：

```bash
python manage.py runserver
```

## `templates`模板

`app/views.py`

对应的 `app`下新建templates目录，再新建 `project_list.html`

```python
def project_list(request):
    # 对应的app下新建templates目录
    return render(request, 'project_list.html')
```

项目配置文件 `settings.py`的 `TEMPLATES`配置下的 `DIR`字段，指定模板文件路径，默认为空列表，寻找模板文件时，从每个 `app`自己的 `template`目录中寻找文件，数序按照 `app`注册的顺序，最后再去根目录找

如果该配置修改成了 ` 'DIRS': [os.path.join(BASE_DIR, 'templates')]`，则优先去根目录找，一般不会修改

## 静态文件

图片、`css`、`js`等文件

如果app下的模板文件需要引入静态文件，需要在对应的 `app`目录下，新建 `static`文件夹（在项目配置文件中配置的名称）

然后在模板文件中，即可引入

![image-20230714102800233](/image-20230714102800233.png)

添加文件后，如要重启服务才能生效

![image-20230714102908256](image-20230714102908256.png)

注意：路径不是平时所理解的相对引用，并且为了项目实际部署需要，`Django`中的模板文件中，不推荐这样写

可以按以下语法

第一行需要引入 `static`

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'css/index.css' %}">
</head>
<body>
    <h2>Project List in app dir</h2>
    <img src="{% static 'robot.png' %}" alt=""></img>

    <script src="{%static 'js/index.js'%}"></script>
</body>
</html>
```

![image-20230714104009473](image-20230714104009473.png)

## 模板语法

传参

视图函数：

```python
def project_list(request):
    # 对应的app下新建templates目录
    name = 'sai'
    scores = ['88', '99']
    return render(request, 'project_list.html', {'name': name, 'scores': scores}) # key为模板中对应的变量，可以自定义
```

模板文件：

```html
    <h3>{{name}}</h3>
    <div>
        {% for score in scores %}
            <span>{{score}}</span>
        {% endfor %}
    </div>
```

![image-20230714105449996](image-20230714105449996.png)

备注：不建议这样写，现在基本是前后端分离，前端可以用 `vue`或 `react`构建

## 请求和响应

视图函数中的入参 `request`，是一个对象，该对象包含了用户发送过来的所有数据

```python
def project_list(request):
    # 对应的app下新建templates目录
    name = 'sai'
    scores = ['88', '99']

    print(request) # <WSGIRequest: GET '/dataTask/project_list/'>
    print(request.method) # GET
    print(request.GET) # 获取GET请求参数。假设请求是/dataTask/project_list/?name=sai&age=18，则结果为<QueryDict: {'name': ['sai'], 'age': ['18']}>
    print(request.POST) # 获取POST请求中的参数
  
    # 响应内容为字符串
    return HttpResponse('添加项目')
  
    # 响应内容为html文件
    return render(request, 'project_list.html', {'name': name, 'scores': scores}) # key为模板中对应的变量，可以自定义
    # 重定向请求
    return HttpResponseRedirect('https://www.baidu.com') # 告诉浏览器，让它自己重新法请求到百度

```

## 数据库操作

可以直接用 `pymysql`的等模板来操作数据库，但有更好的选择

![image-20230714112037610](image-20230714112037610.png)

使用 `orm`框架，不用自己一条条写 `sql`，`Django`内部集成了 `orm`框架

- 创建、修改、删除数据库中的表、表数据（不用写 `sql`）
- 但是数据库还是需要自己额外创建的

### mysql

`mysql`对应的 `orm`框架，可以用 `mysqlclient`

```bash
pip install mysqlclient -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn
```

可能会因为缺少 `wheel`文件安装失败，根据错误提示自行百度解决

可以先安装下 `pkg-config`再试试：

```bash
 sudo apt-get install pkg-config
```

[安装mysqlclient失败解决办法_exception: can not find valid pkg-config name. spe_](https://blog.csdn.net/zhengrong9/article/details/124095267)

获取一个mysql服务

`Django`连接 `mysql`配置：https://docs.djangoproject.com/en/4.2/ref/settings/#databases

在 `settings.py`中配置

备注：如果是容器访问，容器名或者容器ID，即为HOST值。（前提：两个容器都配置到了同一网络下）

### postgres

要在 Django 中连接 PostgreSQL 数据库，你需要安装以下模块：

1. `psycopg2` 或 `psycopg2-binary`：这是 Django 中连接 PostgreSQL 数据库所需的 PostgreSQL 客户端库。你可以选择安装 `psycopg2` 或 `psycopg2-binary` 中的任何一个。

   - 通过 `psycopg2` 进行安装：

     ```bash
     pip install psycopg2
     ```
   - 通过 `psycopg2-binary` 进行安装：

     ```
     pip install psycopg2-binary -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn
     ```

   请注意，`psycopg2-binary` 是 `psycopg2` 的二进制分发版本，它没有外部依赖关系，更容易安装。
2. Django：确保你已经安装了 Django 框架本身。你可以使用 pip 包管理器执行以下命令进行安装：

   ```
   pip install Django
   ```

在安装了上述模块之后，你就可以在 Django 的配置文件中配置 PostgreSQL 连接。

请注意，确保在 Django 的配置文件中正确配置 PostgreSQL 的连接设置，包括数据库名称、用户名、密码和主机等。在配置文件的 `DATABASES` 部分设置中，将 `'ENGINE'` 的值设置为 `'django.db.backends.postgresql'`。

安装上述模块和正确配置 Django 的数据库连接设置后，你就可以在 Django 中连接和使用 PostgreSQL 数据库了。

```bash
apt-get update
apt-get install postgresql-client -y
```

```python

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "data_tag.", # 数据库名称
        "USER": "postgres",
        "PASSWORD": "mypassword",
        "HOST": "fe66bb995f5d", # postgres容器id
        "PORT": "5432",
        'OPTIONS': {
            'options': '-c search_path=your_schema_name', # 模式名
        },
    }
}
```

如果没有配置 `OPTIONS`字段，则表默认生成到 `public`模式中

### 操作表

以 `postgres`数据库为例

#### 新建表

修改app目录下的models.py

```python
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
```

进入项目根目录

来创建数据库迁移文件，这将根据模型的变更创建一个数据库迁移文件：

```bash
python manage.py makemigrations
```

应用数据库迁移：执行以下命令来应用数据库迁移，实际在数据库中创建表：

```bash
python manage.py migrate
```

#### 新增字段

在表中新增列时，由于源表可能存在数据，需要以一种方式添加值

执行脚本时，会让你选择：

输入 `1`：手动输入值。或者指定默认值

```python
age = models.IntegerField(default=0)
```

#### 表已存在

如果在连接到 PostgreSQL 数据库的特定模式时，**该模式中已经存在表**，可以考虑以下两种处理方式：

1. 重命名模型：如果你的 Django 模型与模式中现有的表有冲突，你可以通过在模型类中指定 `db_table` 属性来为模型设置一个不同的表名。例如，在模型类的定义中添加 `db_table` 属性：

   ```
   class MyModel(models.Model):
       field1 = models.CharField(max_length=100)
       field2 = models.IntegerField()
   
       class Meta:
           db_table = 'my_custom_table_name'
   ```

   通过这样设置，Django 将使用指定的自定义表名而不是自动生成的表名。
2. 迁移现有表：如果你想在 Django 中管理现有模式中的表，可以使用 Django 的 `inspectdb` 命令生成模型类的代码。执行以下命令来生成模型类（配置中要选对模式）：

   ```
   python manage.py inspectdb > models.py
   ```

   这将根据数据库中现有表的结构生成相应的模型类代码，并将其保存在 `models.py` 文件中。你可以在生成的模型类中进行适当的修改和调整，以满足你的需求。（生成在了根目录下，需要替换掉app目录下的 `models.py`）

   请注意，`inspectdb` 命令生成的模型类代码是基于现有表的结构，但不包括与表相关的业务逻辑或验证规则等。因此，你可能需要在生成的模型类中添加适当的字段验证、方法和关联等。

无论选择哪种方式，确保在 Django 的配置文件中正确配置 PostgreSQL 的连接设置，并设置 `'OPTIONS'` 部分以指定要连接的特定模式。

在进行任何更改之前，建议先备份现有的数据库和表数据，以防意外发生。

通过上述处理方式，你可以在 Django 中连接到 PostgreSQL 数据库的特定模式，并管理其中已存在的表。

#### 指定 `id`自增

在 Django 中，如果你已经有一个包含 `id` 字段且自增的表，并且通过 `inspectdb` 命令生成了相应的模型类，你可以采取以下步骤来确保在新增数据时 `id` 字段自动自增而无需指定：

1. 在生成的模型类中，将 `id` 字段的名称更改为 `'id'`：

   ```python
   class YourModel(models.Model):
       id = models.AutoField(primary_key=True)
       name = models.CharField(max_length=100)
       # 其他字段和属性
   ```

   通过将 `id` 字段名称设置为 `'id'`，确保与现有的自增 `id` 字段匹配。
2. 在 `Meta` 类中，设置 `auto_created` 为 `True`：

   ```python
   class YourModel(models.Model):
       id = models.AutoField(primary_key=True)
       name = models.CharField(max_length=100)
       # 其他字段和属性
   
       class Meta:
           auto_created = True
   ```

   这将告诉 Django 在保存新的对象时自动生成 `id` 字段的值。

现在，在通过模型类创建和保存新对象时，`id` 字段将自动自增而无需指定。例如：

```python
new_obj = YourModel(name='Some Name')
new_obj.save()
```

Django 将自动为 `id` 字段分配适当的自增值。

请注意，确保在生成的模型类中进行适当的调整和修改，以确保与现有表的结构和字段匹配。此外，建议在进行任何更改之前备份现有数据，以防意外发生。

注意：如果是空表，这一部即可解决问题。

但是我们对接的是有数据的表，此时 `id`还不会自增，如果 `id`自增，数据库表本身也需要设置成允许自增，同时原来的表数据中，`id`字段的 `虚拟类型`设置为 `GENERATED BY DEFAULT AS IDENTITY`，这种类型的列通常用作主键或唯一标识符，并且在每次插入新记录时自动分配新的唯一值。如果你未显式指定该列的值，则将使用自动生成的默认值。(如果选择 `GENERATED ALWAYS AS IDENTITY`，则不能直接是使用 `navicat`新增数据了，只能通过 `orm`接口)

同时要查询下历史数据的最大id，然后自增开始值为最大id加1，见如下配置：

![image-20230715143146929](image-20230715143146929.png)

如果使用 `orm`接口新增数据，如果 `id`存在肯定会报错的，测试时只要多请求几次接口即可，会自增id然后尝试重新插入，一旦orm记录了id后，数据库的 `开始值`改回1也没关系

#### 常见 `Meta`属性

### 操作表数据：增删改查

> 前提：已经基于 `orm`生成了 `models.py`

`views.py`

#### 新增数据

一行代码对应一条记录

```python
from .models import Project
def orm(request):
    # 新增数据
    Project.objects.create(name='test') # 本质就是sql中的insert语句
    Project.objects.create(description='destiption test')
    return HttpResponse('成功')
```

如果后台想要拿到前台 `post`请求携带的数据，注意下前台请求携带的数据格式，不然有可能为 `None`：

[【Django】request.POST.get(“xxx“)接收数据总为None_](https://blog.csdn.net/adafawe/article/details/122380920)

[Django框架request.POST.get 获取数据的问题 ](https://www.ngui.cc/el/3126291.html?action=onClick)

现象：

```python
print(request.POST.get('case_id'))
None
```

原因：

`request.POST.get()`接口为接收并解析的是 `form-data`而传送的是 `Json`数据时，会因编码方式不同而无法解析，进而得不到想要的键值对。

解决方案：

方案一：改变代码解析时的编码方式

```python
import json
data = json.loads(request.body.decode('utf-8'))
case_id = data.get('case_id')
```

方案二：在 `Postman`中修改发送的携带数据格式为 `form-data`：

但是我们前后台分离时，写业务代码的话，此方案就没啥用了

![image-20230719110136114](image-20230719110136114.png)

- 允许跨域：https://www.cnblogs.com/randomlee/p/9752705.html

  安装django-cors-headers，[详情请看官方文档](https://github.com/ottoyiu/django-cors-headers)

  ```
  pip install django-cors-headers
  ```

如果想拿到 `GET`请求的参数，可以直接调用 `requests.GET.get('key')`

#### 删除数据

- 找到 `id`为3的记录并删除：

  ```python
  Project.objects.filter(id=3).delete()
  ```
- 删除表全部数据

  ```python
  Project.objects.all().delete()
  ```
- 提供接口

  ```python
  # 看项目需要是否提供，逻辑同新增数据
  
  ```

#### 查询数据

- 查询所有记录

  ```python
  data_list = Project.objects.all() # 是一个QuerySet对象
  print(data_list)  # <QuerySet [<Project: Project object (2)>, <Project: Project object (1)>, <Project: Project object (8)>]>
  # 获取每一行
  for data in data_list:
      print(data.id, data.name, data.description) # 获取每一条记录，如果数据库中是null，则在python中对应为None
  ```
- 条件查询

  ```python
  data_list = Project.objects.filter(name='test') # 即使是一条记录，得到的也是QeurySet对象
  
  # 如果明确就知道了，只有一条记录，可以使用first()
  data = Project.objects.filter(id='4').first()
  print(data) # Project object (4)
  print(data.id, data.name) # 4 test4
  ```
- 提供接口

  路由：

  ```python
  from django.urls import path
  
  from . import views
  
  urlpatterns = [
      path("index/", views.index, name="index"),
      path("project/list/", views.project_list, name="project_list")
  ]
  ```

  视图函数：

  ```python
  from django.shortcuts import render
  from django.http import HttpResponse, JsonResponse
  from django.core.serializers.json import DjangoJSONEncoder
  from .models import Project
  import json
  
  def project_list(request):
      # 对应的app下新建templates目录
      projects = Project.objects.all()
      project_list = []
      for project in projects:
          project_dict = {
              'id': project.id,
              'name': project.name,
              'timestamp': project.timestamp,
              'description': project.description,
              'poject_id': project.project_id,
          }
          project_list.append(project_dict)
  
      # 构造json响应字符串
      response = {
          'code': 200,
          'data': project_list,
          'message': '查询成功'
      }
      return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False}) # 返回json数据，允许返回中文
  
  ```

#### 更新数据

- 需要先找到数据，然后更新

  ````python
  # 将表中所有记录的description字段，设置为test
  Project.objects.all(description='test')
  
  # 增加筛选条件，更新指定条件的数据
  Project.objects.filter(id=5).update(description='update')
  
  ````
  或者：

  ```python
  from django.shortcuts import get_object_or_404
  
  def update_project(request):
      if request.method == 'POST':
          project_id = '0001'  # 假设要修改的项目的 project_id 是 0001
          name = request.POST.get('name')  # 从请求中获取要更新的 name 值
          timestamp = request.POST.get('timestamp')  # 从请求中获取要更新的 timestamp 值
          description = request.POST.get('description')  # 从请求中获取要更新的 description 值
  
          # 查找具有 project_id 为 0001 的项目对象
          project = get_object_or_404(Project, project_id=project_id)
  
          # 更新项目对象的其他字段
          project.name = name
          project.timestamp = timestamp
          project.description = description
  
          # 保存更新后的项目对象到数据库
          project.save()
  
          # 返回更新成功的响应
          response = {
              'code': 200,
              'message': '项目信息更新成功'
          }
          return JsonResponse(response)
  
      # 返回请求方法错误的响应
      response = {
          'code': 405,
          'message': '只支持 POST 请求'
      }
      return JsonResponse(response, status=405)
  
  ```
