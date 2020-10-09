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

### 三、对象操作
1. 创建book
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


### 参考
- [Django使用GraphQL详解](https://blog.csdn.net/ns2250225/article/details/79348914)