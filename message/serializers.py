from rest_framework import serializers

from chat.models import Message, Chat
from chat.serializers import ChatSerializer


class MessageSerializer(serializers.ModelSerializer):

    chat_id = ChatSerializer()

    class Meta:
        model = Message
        fields = ["id", "chat_id", "user", "message", "created"]

    def to_representation(self, instance):
        rep = super(MessageSerializer, self).to_representation(instance)
        rep["user"] = instance.user.username
        return rep
