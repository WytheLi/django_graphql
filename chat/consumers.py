import asyncio
import json
import time

from channels.consumer import AsyncConsumer, SyncConsumer
# async_to_sync()包装器，使得同步的WebsocketConsumer能调用异步的channel layer(通道层)方法
# 它可以将任何异步协程调用转换为可同步调用
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(self.scope)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # join room group
        # async_to_sync(self.channel_layer.group_add)(
        #         #     self.room_group_name,
        #         #     self.channel_name
        #         # )
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        print('Websocket connected...')
        await self.accept()


    async def disconnect(self, code):
        print('Websocket disconnected...')
        # leave room group
        # async_to_sync(self.channel_layer.group_discard)(
        #     self.room_group_name,
        #     self.channel_name
        # )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # receive message from websocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)

        # send message to room group
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message', # 'type'键，该值对应于应在接收事件的使用者上调用的方法
        #         'message': message
        #     }
        # )
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

        # self.send(text_data=json.dumps({'message': message}))

    # receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # send message to websocket
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))
        await self.send(text_data=json.dumps({
            'message': message
        }))


class PrintConsumer(SyncConsumer):
    def test_print(self, message):
        # 接受来自beatserver的数据, 将消息发送到channel layer组
        async_to_sync(self.channel_layer.group_send)(
            message['message']['group'],
            {
                "type": "stream.message",
                "message": message['message']['pushData']
            }
        )


class StreamConsumer(WebsocketConsumer):
    def connect(self):
        print('Stream Connect...')
        self.room_group_name = self.scope['url_route']['kwargs'].get('group_name', None)

        # join room_group，将ws连接与channel layer指定组映射
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        # receive json data, example {"message": "hello websocket!"}
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # 及时应答客户端
        self.send(text_data=json.dumps({
            "data": {
                "receive": message,
                "status": 200,
                "message": message.replace(' ', '--')
            }
        }))

        # Send message to room_group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "stream_message",
                "message": message
            }
        )

    # Receive message from room_group
    def stream_message(self, event):
        message = event['message']
        print(event['type'])

        # Send message to websocket
        self.send(text_data=json.dumps({"data": message}))