from rest_framework import serializers
from chat.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["id", "sent_from_id", "sent_to_id"]
