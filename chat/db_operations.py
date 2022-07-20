from channels.db import database_sync_to_async
from chat.models import Chat, Message


@database_sync_to_async
def save_text_message(id, message):

    chat_id = Chat.objects.get(id=id)

    return Message.objects.create(chat_id=chat_id, message=message)
