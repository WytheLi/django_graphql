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


### 参考
- [Django使用GraphQL详解](https://blog.csdn.net/ns2250225/article/details/79348914)
- [graphene-django](https://www.howtographql.com/graphql-python/0-introduction/)
- [Insomnia客户端 -- REST和GraphQL API调试](https://insomnia.rest/download/)