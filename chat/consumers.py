import json

from channels.generic.websocket import AsyncWebsocketConsumer

from .db_operations import save_text_message


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self):
        self.chat_id = None
        self.chat_group_name = None
        self.user = None
        super().__init__()

    async def connect(self):
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.user = self.scope["url_route"]["kwargs"]["username"]
        self.chat_group_name = "chat_%s" % self.chat_id
        await self.channel_layer.group_add(self.chat_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.chat_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await save_text_message(self.chat_id, message)

        await self.channel_layer.group_send(
            self.chat_group_name,
            {"type": "chat_message", "message": message, "username": self.user},
        )

    async def chat_message(self, event):
        user = event["username"]
        message = event["message"]

        await self.send(
            text_data=json.dumps(
                {
                    "username": user,
                    "message": message,
                }
            )
        )
