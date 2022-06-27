from rest_framework import serializers
from chat.models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'sent_from_id', 'sent_to_id']
    

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'chat_id', 'message', 'created']