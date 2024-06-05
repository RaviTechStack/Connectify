from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.index),
    path("login", views.handellogin),
    path("signup", views.signup),
    path("post", views.post),
    path("search", views.searchUser),
    path("logout", views.handellogout),
    path("userprofile/<id>", views.showProfile),
    path("addLike", views.addlike),
    path("follow", views.addFollow),
    path("detailPost/<id>", views.detailPost),
    path("yourPost", views.yourPost),
    path("comment", views.commentsApi),
    path("friends/<id>", views.showFriends),
    path("editPost/<id>", views.editPost),
    path("deletePost/<id>", views.delPost),
    path("api", views.postserial.as_view()),
    path("chat", views.chat)
]