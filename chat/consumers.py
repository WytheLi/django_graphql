import json

# async_to_sync()包装器，使得同步的WebsocketConsumer能调用异步的channel layer(通道层)方法
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print(self.scope)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        print('Websocket connected...')
        self.accept()


    def disconnect(self, code):
        print('Websocket disconnected...')
        # leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # receive message from websocket
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)

        # send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message', # 'type'键，该值对应于应在接收事件的使用者上调用的方法
                'message': message
            }
        )

        # self.send(text_data=json.dumps({'message': message}))

    # receive message from room group
    def chat_message(self, event):
        message = event['message']

        # send message to websocket
        self.send(text_data=json.dumps({
            'message': message
        }))