from chat.models import Chat, Message
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ChatSerializer, MessageSerializer

class ChatList(generics.ListCreateAPIView):
    """
    API endpoint for chats
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MessageList(generics.ListCreateAPIView):
    """
    API endpoint for messages
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request, chat_id):
        queryset = self.get_queryset()
        serializer = MessageSerializer(
            queryset.filter(chat_id=chat_id),
            many=True
        )
        return Response(serializer.data)
