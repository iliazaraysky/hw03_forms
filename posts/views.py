from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from .forms import NewPost
from django.shortcuts import redirect


def index(request):
    latest = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"groups": group, "posts": posts})


def post_view(request):
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = NewPost()
    return render(request, 'newpost.html', {'form': form})
