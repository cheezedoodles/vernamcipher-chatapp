from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import get_object_or_404

from rest_framework import (generics, permissions, status,
                            authentication)
from rest_framework.settings import api_settings
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from knox.views import LoginView as KnoxLoginView
from .serializers import (ChatSerializer, MessageSerializer,
                          UserSerializer, AuthSerializer)
from chat.models import Chat, Message

class ChatListView(generics.ListCreateAPIView):
    """
    API endpoint for chats
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = self.request.user
        print(user)
        return Chat.objects.filter(Q(sent_from_id=user.id)|\
                                   Q(sent_to_id=user.id))

    def create(self, request, *args, **kwargs):
        try:
            user1_pk = User.objects.get(username=request.data['sent_from_id']).pk
            user2_pk = User.objects.get(username=request.data['sent_to_id']).pk
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = {'sent_from_id': user1_pk, 'sent_to_id': user2_pk}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MessageListView(generics.ListCreateAPIView):
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


class CreateUserView(generics.CreateAPIView):
    """
    API endpoint for users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(KnoxLoginView):
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)    


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'username'

