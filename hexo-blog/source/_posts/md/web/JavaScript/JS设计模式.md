---
title: 'JS设计模式'
date: 2022-12-19 07:15:24
cover: false
tags:
- 设计模式
categories: '设计模式'
typora-root-url: JS设计模式
---





# 观察者模式

> - 观察者模式一种设计模式。
>
> - 观察者模式定义了对象间的一种 一对多 的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都将得到通知，并自动更新。

![image-20221219103112456](image-20221219103112456.png)

## 基本逻辑

观察者（Observer）直接订阅（Subscribe）主题（Subject），而当主题被激活的时候，会触发（Fire Event）观察者里的事件

- 被观察者需要有状态

  ```js
  // 定义主题 Subject
  function Subject() {
      this.state = '开心'
  }
  ```

- 可以有多个观察者

  ```js
  // 定义观察者 Observer
  function Observer(name) {
      // 可以有多个观察者
      this.name = name
  }
  ```

- Observer要做到可以观察Subject的状态，需要将Observer放在Subject的身上

  Subject中定义一个数组，并向外暴露一个attach方法，接收Observer实例作为attach实参，存到数组里

  ```js
  // 定义主题 Subject
  function Subject() {
      this.state = '开心'
      this.observers = []
      this.attach = function (observerInstance) {
          this.observers.push(observerInstance)
          return this
      }
  }
  
  // 定义观察者 Observer
  function Observer(name) {
      // 可以有多个观察者
      this.name = name
  
  }
  
  let baby = new Subject()
  let father = new Observer('father')
  let mother = new Observer('mother')
  
  baby.attach(father).attach(mother)
  
  ```

  ![image-20221219105641224](image-20221219105641224.png)

- 如果Subject状态发生了变化，需要让Observer知道（调用Observer身上的方法，并传递实参）

  - Subject中要提供一个更新状态的方法

    ```js
    function Subject(name) {
        this.name = name
        this.state = '开心'
        this.observers = []
        this.attach = function(observerInstance) {
            this.observers.push(observerInstance)
            return this
        }
    
        this.setState = function(state) {
            // 更新状态
            this.state = state
            // 循环取出每个Observer，并通知Observer（调用Observer身上的方法，并传递实参）
            this.observers.forEach(item => {
                item.watch(this) // 向Observer传递最新的Subject实例
            })
        }
    }
    ```

  - Observer中也要提供一个观察Subject的方法

    ```js
    function Observer(name) {
        this.name = name
        // 定义观察Subject的方法
        this.watch = function(subjectInstance) {
            console.log(`${this.name}: 观察到${subjectInstance.name}的状态是${subjectInstance.state}`)
        }
    }
    
    ```

  - 变更Subject的状态

    ```js
    let baby = new Subject('baby')
    let father = new Observer('father')
    let mother = new Observer('mother')
    
    baby.attach(father).attach(mother)
    baby.setState('不开心')
    
    ```

    我们二次修改Subject的状态，也被观察到了

    ![image-20221219111608121](image-20221219111608121.png)

**小结**

- 将对象二的实例存到对象一的数组属性上
- 对象一属性变更时，将变更后的对象一实例，以实参的形式，通过调用对象二身上的方法，传递给对象二（函数调用可以传递实参）
  - 进一步加深理解堆内存的引用关系

## 进阶

### 发布者

上面案例中，我们是在代码中修改Subject的状态，这个可以通过**发布者**概念来进一步抽象

https://www.jb51.net/article/230975.htm

- 倘若即将到来双11，想要在双11购买商品的人就是观察者(Observer)
- 想要购买的商品就是被观察者(Observed)
- 为了更加形象，添加一个商家来改变商品的价格，商家也就是发布者(Publish)
- 当双11当天，商家(发布者(Publish))会修改商品（被观察者(Observed)）的价格，然后关注订阅该商品的人（观察者(Observer)）就会收到信息通知。

![image-20221219113105756](image-20221219113105756.png)



```js
//观察者设计模式
//发布者 -->商家
var shopObj = {};
//商品列表 [key:[]], key为商品名
shopObj.list = [];
//订阅方法
shopObj.listen = function ( key, fn) {// key是商品型号, fn这个函数就是订阅的行为
    if (!this.list[key]) {
        this.list[key] = [];
    }
    this.list[key].push(fn);//往商品名为key的商品列表中添加订阅
}
//发布消息方法
shopObj.publish = function (key) {
    //var key = arguments[0];//如果不传参数key，这样也可以
    var fns = this.list[key];
    // for (var i = 0; i < fns.length; i++) {
        for(var i = 0 ,fn; fn = fns[i++];){
        //执行订阅的函数fn  arguemnts储存的所有实参
        // var fn = fns[i++];
        fn.apply(this, arguments)
    }
}
//A用户添加订阅
shopObj.listen("华为", function (brand, model) {
    console.log( "A用户收到：" + brand + model + "手机降价了");
})
//B用户添加订阅
shopObj.listen("华为", function (brand, model) {
    console.log("B用户收到：" + brand + model + "手机降价了");
})
//c用户添加订阅
shopObj.listen("小米", function (brand, model) {
    console.log("C用户收到：" + brand + model + "手机降价了");
})
//双11 商家发布消息华为降价的信息
shopObj.publish("华为", "p30");
shopObj.publish("小米", "Mix4");

```

重构代码

```js
//观察者设计模式
var Eevent = {
    //商品列表 [key:[]], key为商品名
    list: [],
    //订阅方法
    listen: function (key, fn) {// key是商品型号, fn这个函数就是订阅的行为
        if (!this.list[key]) {
            this.list[key] = [];
        }
        this.list[key].push(fn);
    },
    //发布消息方法
    publish: function (key) {
        //var key = arguments[0];//如果不传参数key，这样也可以
        var fns = this.list[key];
        // for (var i = 0; i < fns.length; i++) {
        for (var i = 0, fn; fn = fns[i++];) {
            //执行订阅的函数fn  arguemnts储存的所有实参
            // var fn = fns[i++];
            fn.apply(this, arguments)
        }
    }
}
//观察者对象初始化
var initEvent = function (obj) {
    for (var i in Eevent) {
        obj[i] = Eevent[i];
    }
}
//发布者 -->商家
var shopObj = {};
initEvent(shopObj);
//A用户添加订阅
shopObj.listen("华为", function (brand, model) {
    console.log("A用户收到：" + brand + model + "手机降价了");
})
//B用户添加订阅
shopObj.listen("华为", function (brand, model) {
    console.log("B用户收到：" + brand + model + "手机降价了");
})
//c用户添加订阅
shopObj.listen("小米", function (brand, model) {
    console.log("C用户收到：" + brand + model + "手机降价了");
})
//双11 商家发布消息华为降价的信息
shopObj.publish("华为", "p30");
shopObj.publish("小米", "Mix4");

```

### 移除观察



```js
function Subject(name) {
    this.detach = function (observerInstance) {
        this.observers.forEach((ob, index, obs) => {
            if(ob.name === observerInstance.name) {
                obs.splice(index, 1)
            }
        })
        return this
    } 
}
```



## 应用

# 发布订阅模式

![image-20221219103331023](image-20221219103331023.png)

订阅者（Subscriber）把自己想订阅的事件注册（Subscribe）到调度中心（Topic）（向调度中心申请），当发布者（Publisher）发布该事件（Public Topic）到调度中心，也就是该事件触发时，由调度中心统一调度（Fire Event）订阅者注册到调度中心的处理代码





# 工厂函数

https://www.jianshu.com/p/9ce26a5044e6







