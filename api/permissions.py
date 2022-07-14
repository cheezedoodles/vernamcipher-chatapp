from rest_framework import permissions
from chat.models import Chat


class RelatedToChatPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        chat_id = view.kwargs.get('chat_id')
        user = request.user

        chat = Chat.objects.get(id=chat_id)

        sender = chat.sent_from_id.id == user.id
        recipient = chat.sent_to_id.id == user.id
        return sender or recipient
