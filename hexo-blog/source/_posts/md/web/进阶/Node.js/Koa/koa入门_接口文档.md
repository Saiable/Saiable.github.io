---
title: koa入门_接口文档 v1.0.0
date: 2022/8/9 6:52:13
cover: false
tags:
- Koa
categories: Koa
toc_number: true
typora-root-url: koa
headingLevel: 2
generator: "@tarslib/widdershins v4.0.15"
---

# koa入门

> v1.0.0

# 用户模块

## POST 用户注册接口

POST /user/register

> Body 请求参数

```json
{
  "user_name": "string",
  "password": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» user_name|body|string| 是 | 用户名|用户名|
|» password|body|string| 是 | 密码|密码|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 用户登录接口

POST /user/login

> Body 请求参数

```json
{
  "user_name": "高芳",
  "password": "in"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» user_name|body|string| 是 ||none|
|» password|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "message": "string",
  "result": {
    "token": "string"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» result|object|true|none||none|
|»» token|string|true|none||none|

## PATCH 用户修改密码接口

PATCH /user/modifyPassword

> Body 请求参数

```json
{
  "password": "dolore culpa pariatur"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» password|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

# 商品模块

## POST 上传图片

POST /goods/upload

> Body 请求参数

```yaml
file: file://F:\Pictures\blog.png

```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» file|body|string(binary)| 否 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 发布商品

POST /goods/release

> Body 请求参数

```json
{
  "goods_name": "里而热集便象",
  "goods_price": 53,
  "goods_num": 61,
  "goods_img": "4602f8abfd1abe5046e15e300.png"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» goods_name|body|string| 是 ||商品名称|
|» goods_price|body|number| 是 ||商品价格|
|» goods_num|body|number| 是 ||商品数量|
|» goods_img|body|string| 是 ||商品图片名称|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## PUT 修改商品

PUT /goods/update/{id}

> Body 请求参数

```json
{
  "goods_name": "string",
  "goods_price": 0,
  "goods_num": 0,
  "goods_img": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|id|path|number| 是 ||none|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» goods_name|body|string| 是 ||none|
|» goods_price|body|number| 是 ||none|
|» goods_num|body|number| 是 ||none|
|» goods_img|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## DELETE 硬删除商品

DELETE /goods/remove/{id}

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|id|path|number| 是 ||none|
|Authorization|header|string| 否 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 下架商品

POST /goods/remove/{id}/off

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|id|path|string| 是 ||none|
|Authorization|header|string| 是 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 上架商品

POST /goods/remove/{id}/on

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|id|path|string| 是 ||none|
|Authorization|header|string| 是 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## GET 获取商品列表

GET /goods/lists/

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|pageNum|query|number| 否 ||none|
|pageSize|query|number| 否 ||none|
|Authorization|header|string| 是 ||none|

> 返回示例

> 成功

```json
{
  "code": 0,
  "message": "获取商品列表成功",
  "result": {
    "pageNum": "1",
    "pageSize": "10",
    "total": 3,
    "list": [
      {
        "id": 2,
        "goods_name": "酸这争取",
        "goods_price": "13.00",
        "goods_num": 14,
        "goods_img": "http://dummyimage.com/400x400",
        "createdAt": "2022-08-02T13:55:31.000Z",
        "updatedAt": "2022-08-02T13:55:31.000Z",
        "deletedAt": null
      },
      {
        "id": 3,
        "goods_name": "证断影然度叫",
        "goods_price": "53.00",
        "goods_num": 58,
        "goods_img": "http://dummyimage.com/400x400",
        "createdAt": "2022-08-02T14:07:27.000Z",
        "updatedAt": "2022-08-02T14:07:27.000Z",
        "deletedAt": null
      },
      {
        "id": 4,
        "goods_name": "周根角万广",
        "goods_price": "95.00",
        "goods_num": 66,
        "goods_img": "http://dummyimage.com/400x400",
        "createdAt": "2022-08-02T14:07:31.000Z",
        "updatedAt": "2022-08-02T14:07:31.000Z",
        "deletedAt": null
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

# 购物车模块

## POST 添加到购物车

POST /carts

> Body 请求参数

```json
{
  "goods_id": 78
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» goods_id|body|number| 是 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## GET 获取购物车列表

GET /carts

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|pageSize|query|number| 否 ||none|
|pageNum|query|string| 否 ||none|
|Authorization|header|string| 是 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## DELETE 删除购物车列表

DELETE /carts

> Body 请求参数

```json
{
  "ids": [
    0
  ]
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» ids|body|[number]| 是 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## PATCH 更新购物车列表

PATCH /carts/{id}

> Body 请求参数

```json
{
  "number": 0,
  "selected": true
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|id|path|number| 是 ||none|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» number|body|number| 否 ||数量|
|» selected|body|boolean| 是 ||是否添加|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 全选

POST /carts/selectAll

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 否 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 全不选

POST /carts/unSelectAll

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 否 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

# 地址模块

## POST 新增地址

POST /address

> Body 请求参数

```json
{
  "consignee": "string",
  "phone": "string",
  "address": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» consignee|body|string| 是 ||none|
|» phone|body|string| 是 ||none|
|» address|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## GET 获取地址列表

GET /address

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 否 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## PUT 修改地址

PUT /address/{id}

> Body 请求参数

```json
{
  "consignee": "string",
  "phone": "string",
  "address": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|id|path|number| 是 ||none|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» consignee|body|string| 是 ||none|
|» phone|body|string| 是 ||none|
|» address|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## DELETE 删除地址

DELETE /address/{id}

> Body 请求参数

```json
{
  "consignee": "string",
  "phone": "string",
  "address": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|id|path|number| 是 ||none|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» consignee|body|string| 是 ||none|
|» phone|body|string| 是 ||none|
|» address|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## PATCH 设置默认地址

PATCH /address/{id}

> Body 请求参数

```json
{
  "consignee": "string",
  "phone": "string",
  "address": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|id|path|number| 是 ||none|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» consignee|body|string| 是 ||none|
|» phone|body|string| 是 ||none|
|» address|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

# 订单模块

## POST 生成订单

POST /orders

> Body 请求参数

```json
{
  "address_id": 0,
  "goods_info": "string",
  "total": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» address_id|body|integer| 是 ||none|
|» goods_info|body|string| 是 ||none|
|» total|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## GET 获取订单列表

GET /orders

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|pageNum|query|number| 否 ||none|
|pageSize|query|number| 否 ||none|
|status|query|integer| 否 ||none|
|Authorization|header|string| 否 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## PATCH 更新订单状态

PATCH /orders/{id}

> Body 请求参数

```json
{
  "status": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|id|path|string| 是 ||none|
|Authorization|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» status|body|number| 是 ||none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

# 数据模型

<h2 id="tocS_购物车模型">购物车模型</h2>

<a id="schema购物车模型"></a>
<a id="schema_购物车模型"></a>
<a id="tocS购物车模型"></a>
<a id="tocs购物车模型"></a>

```json
{
  "id": 0,
  "goods_id": 0,
  "user_id": 0,
  "number": 0,
  "selected": 0
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|id|number|true|none||none|
|goods_id|number|true|none||none|
|user_id|number|true|none||none|
|number|number|true|none||none|
|selected|number|true|none||none|

