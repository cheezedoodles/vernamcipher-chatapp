from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from knox import views as knox_views
from api import views as api_views
from chat import views as chat_views
from message import views as message_views
from user import views as user_views

urlpatterns = [
    path("chats/", chat_views.ChatListView.as_view()),
    path("chat/<int:chat_id>/", message_views.MessageListView.as_view()),
    path("users/", user_views.UsersListView.as_view()),
    path("users/<str:username>/", user_views.UserDetailView.as_view()),
    path("create/", user_views.CreateUserView.as_view()),
    path("login/", api_views.LoginView.as_view(), name="knox_login"),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("logoutall/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
]


urlpatterns = format_suffix_patterns(urlpatterns)
