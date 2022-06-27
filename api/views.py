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


#class MessageList(generics.ListCreateAPIView):
#    """
#    API endpoint for messages
#    """
#   queryset = Message.objects.all()
#    serializer_class = MessageSerializer
#    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@api_view(['GET', 'POST'])
def message_list(request, pk, format=None):
    if request.method == 'GET':
        messages = Message.objects.filter(chat_id=pk)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
