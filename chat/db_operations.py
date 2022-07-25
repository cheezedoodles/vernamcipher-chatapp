from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from chat.models import Chat, Message


@database_sync_to_async
def save_text_message(id, username, message):

    chat_id = Chat.objects.get(id=id)
    user = User.objects.get(username=username)

    return Message.objects.create(chat_id=chat_id, user=user, message=message)
