from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    sent_from_id = models.ForeignKey(User,
                                     on_delete=models.CASCADE,
                                     related_name='sender')
    sent_to_id = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='receiver')


class Message(models.Model):
    chat_id = models.ForeignKey(Chat,
                                on_delete=models.CASCADE,
                                related_name='chat')
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Chat {self.chat_id} message sent at {self.created}'
