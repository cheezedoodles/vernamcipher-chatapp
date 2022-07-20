from rest_framework import serializers

from chat.models import Message, Chat
from chat.serializers import ChatSerializer


class MessageSerializer(serializers.ModelSerializer):

    chat_id = ChatSerializer()

    class Meta:
        model = Message
        fields = ["id", "chat_id", "message", "created"]
