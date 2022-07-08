from django.urls import path, include

from . import views

app_name ='chats'

urlpatterns = [
    #path('', views.chat_list, name='chat_list'),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('login/', views.user_login, name='login'),
    #path('register/', views.register, name='register'),
    path('<int:chat_id>/', views.chat, name='chat'),
]