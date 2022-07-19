from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from knox import views as knox_views
from . import views

urlpatterns = [
    path("chats/", views.ChatListView.as_view()),
    path("chat/<int:chat_id>/", views.MessageListView.as_view()),
    path("users/", views.UsersListView.as_view()),
    path("users/<str:username>/", views.UserDetailView.as_view()),
    path("create/", views.CreateUserView.as_view()),
    path("login/", views.LoginView.as_view(), name="knox_login"),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("logoutall/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
]


urlpatterns = format_suffix_patterns(urlpatterns)
