from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from chat.serializers import ChatSerializer
from chat.models import Chat


class ChatListView(generics.ListCreateAPIView):
    """
    API endpoint used for listing and creating chats
    """

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(Q(sent_from_id=user.id) | Q(sent_to_id=user.id))

    def create(self, request, *args, **kwargs):
        try:
            user1_pk = User.objects.get(username=request.data["sent_from_id"]).pk
            user2_pk = User.objects.get(username=request.data["sent_to_id"]).pk
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = {"sent_from_id": user1_pk, "sent_to_id": user2_pk}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
