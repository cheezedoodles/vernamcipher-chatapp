from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('chats/', views.ChatList.as_view()),
    path('chat/<int:pk>/', views.message_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)