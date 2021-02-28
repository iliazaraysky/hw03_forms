from django.urls import path

from . import views
from .forms import NewPost


urlpatterns = [
    path("", views.index, name="index"),
    path("new", NewPost.as_view(), name="new_post"),
    path("group/<str:slug>", views.group_posts, name="group"),
]
