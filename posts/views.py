from django.shortcuts import render, get_object_or_404
import datetime as dt
from .models import Post, Group


def year(request):
    now_year = dt.datetime.now().year
    return {'year': now_year}


def index(request):
    latest = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"groups": group, "posts": posts})
