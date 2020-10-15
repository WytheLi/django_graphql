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

3、确保channel layer可以与Redis通信。打开Django shell并运行以下命令：
python manage.py shell
```
>>> import channels.layers
>>> channel_layer = channels.layers.get_channel_layer()
>>> from asgiref.sync import async_to_sync
>>> async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
>>> async_to_sync(channel_layer.receive)('test_channel')
{'type': 'hello'}
```

### 服务器配置
1. 项目下添加 asgi.py 文件
2. 安装daphne：`pip install daphne`
3. 运行项目：`daphne -b 0.0.0.0 -p 8001 django_graphql.asgi:application`
4. nginx配置
```
upstream channels-backend {
    server localhost:8000;
}
# ...
server {
    # ...
    location / {
        try_files $uri @proxy_to_app;
    }
    # ...
    location @proxy_to_app {
        proxy_pass http://channels-backend;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Host $server_name;
    }
    # ...
}
```
5. supervisor启动daphne

5.1 安装supervisor
```
pip install supervisor
```

5.2 生成配置文件
```
>>> mkdir Supervisor
>>> cd Supervisor/
>>> echo_supervisord_conf > supervisord.conf
>>> ls
supervisord.conf
>>> cat supervisord.conf 
```

5.3 添加启动配置
```
>>> vim daphne.ini
# 加入下面的内容

[program:daphne]
directory=/home/user/ITNest
command=daphne -b 127.0.0.1 -p 8001 --proxy-headers ITNest.asgi:application
autostart=true
autorestart=true
stdout_logfile=/tmp/websocket.log
redirect_stderr=true
```

5.4 修改supervisor配置文件
```
>>> vim supervisord.conf 

# 最后加上
[include]
;files = relative/directory/*.ini
files = /home/user/ITNest/Supervisor/*.ini
```

5.5 启动supervisord
```
>>> supervisord -c supervisord.conf 

>>> tail /tmp/websocket.log 
```

重启
```
>>> supervisorctl -c supervisord.conf restart
Error: restart requires a process name
restart <name>      Restart a process
restart <gname>:*   Restart all processes in a group
restart <name> <name>   Restart multiple processes or groups
restart all     Restart all processes
Note: restart does not reread config files. For that, see reread and update.
>>> supervisorctl -c Supervisor/supervisord.conf restart all
daphne: stopped
daphne: started
```


### 参考
- [Django使用GraphQL详解](https://blog.csdn.net/ns2250225/article/details/79348914)
- [graphene-django](https://www.howtographql.com/graphql-python/0-introduction/)
- [Insomnia客户端 -- REST和GraphQL API调试](https://insomnia.rest/download/)
- [channels官方文档 & 实现聊天服务器demo](https://channels.readthedocs.io/en/latest/)
- [\_\_call__()。该方法的功能类似于在类中重载 () 运算符，使得类实例对象可以像调用普通函数那样，以“对象名()”的形式使用](http://c.biancheng.net/view/2380.html)
- [Django使用Channels实现WebSocket消息通知功能](https://www.jianshu.com/p/0f75e2623418)
- [beatserver ](https://github.com/rajasimon/beatserver/)