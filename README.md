### 一、创建项目
```
django-admin startproject django_graphql
cd django_graphql
python manage.py startapp book
```

### 二、启动项目
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
访问：/localhost:8080/graphql/
```

Django shell操作
```
python manage.py shell
```

### 三、对象操作
1. 创建记录
```
mutation createBook {
  createBook(bookData: {title:"django-graphgl2", author: "ns2250225"}) {
    book {
      title {
        id,
        name
      },
      author {
        id,
        name
      }
    }
    ok
  }
}
```

```
mutation createUser {
  createUser(username:"test02", email: "test02@163.com", password: "password"){
    msg
  }
}
```

2. 查询
```
query {
  allBooks {
    id,
    title {
      id,
      name
    },
    author {
      id,
      name
    }
  }
}
```

3. 签发token
```
mutation {
  tokenAuth(username: "willi", password: "password"){
    token
  }
}
```

```
{
  "data": {
    "tokenAuth": {
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IndpbGxpIiwiZXhwIjoxNjAyMzEyNTY2LCJvcmlnSWF0IjoxNjAyMzEyMjY2fQ.VTd6Fu7h2ocix8c17idjQmRYpuBQ8fN8j_s7LEW9D_8"
    }
  }
}
```

### 聊天室
1、ASGI/Channels

2、channels_redis
启动channel layer（频道层/通道层)，channel layer是一种通信系统。

例如：在我们的聊天应用程序中，我们希望ChatConsumer同一房间中的多个实例彼此通信。为此，我们将让每个ChatConsumer将其频道添加到名称基于房间名称的组中。这样，ChatConsumers可以将消息传输到同一房间中的所有其他ChatConsumers

我们将redis用作channel layer的后备存储


### 参考
- [Django使用GraphQL详解](https://blog.csdn.net/ns2250225/article/details/79348914)
- [graphene-django](https://www.howtographql.com/graphql-python/0-introduction/)
- [Insomnia客户端 -- REST和GraphQL API调试](https://insomnia.rest/download/)
- [channels官方文档 & 实现聊天服务器demo](https://channels.readthedocs.io/en/latest/)
- [\_\_call__()。该方法的功能类似于在类中重载 () 运算符，使得类实例对象可以像调用普通函数那样，以“对象名()”的形式使用](http://c.biancheng.net/view/2380.html)