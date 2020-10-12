from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import chat.routing

# 此根路由配置指定在与Channels开发服务器建立连接时，ProtocolTypeRouter将首先检查连接的类型。
# 如果是WebSocket连接（ws：//或wss：//），则该连接将分配给AuthMiddlewareStack
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})