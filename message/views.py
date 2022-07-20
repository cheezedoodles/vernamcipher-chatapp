from rest_framework import generics, permissions, status
from rest_framework.response import Response

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from message.serializers import MessageSerializer
from chat.models import Message
from api.permissions import RelatedToChatPermission


class MessageListView(generics.ListCreateAPIView):
    """
    API endpoint used for listing and creating messages
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, RelatedToChatPermission]

    def list(self, request, chat_id, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MessageSerializer(
            queryset.filter(chat_id=chat_id),
            many=True,
        )
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        channel_layer = get_channel_layer()

        chat_id = request.data["chat_id"]
        message = request.data["message"]

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        async_to_sync(channel_layer.group_send)(
            f"chat_{chat_id}",
            {"type": "chat_message", "message": message},
        )

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
