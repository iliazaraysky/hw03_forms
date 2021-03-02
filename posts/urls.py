from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.post_view, name="new_post"),
    path("group/<str:slug>", views.group_posts, name="group"),
]
