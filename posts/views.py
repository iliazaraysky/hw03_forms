from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User
from .forms import NewPost
from django.shortcuts import redirect


def index(request):
    latest = Post.objects.all()
    paginator = Paginator(latest, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, "index.html", {"page": page})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"groups": group, "posts": posts})


@login_required
def post_new(request):
    if request.method != 'POST':
        form = NewPost()
        return render(request, 'newpost.html', {'form': form})

    form = NewPost(request.POST)

    if not form.is_valid():
        return render(request, 'newpost.html', {'form': form})
    post = form.save(commit=False)
    post.author = request.user
    post.save()
    return redirect('index')


def profile(request, username):
    author = get_object_or_404(User, username=username)
    all_posts = Post.objects.all().filter(author__username=username)
    counter = all_posts.count()
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'profile.html',
                  {'page': page, 'author': author, 'counter': counter})


def post_view(request, username, post_id):
    author = get_object_or_404(User, username=username)
    full_post = get_object_or_404(Post, id=post_id)
    all_posts = Post.objects.all().filter(author__username=username)
    counter = all_posts.count()
    return render(request, 'post.html',
                  {'author': author, 'full_post': full_post,
                   'counter': counter})


def post_edit(request, username, post_id):
    post = get_object_or_404(Post, id=post_id)
    author = get_object_or_404(User, username=username)
    if request.method == 'GET':
        if request.user != post.author:
            return redirect('post', username=post.author, post_id=post.id)
        form = NewPost(instance=post)

    if request.method == 'POST':
        form = NewPost(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('post', username=post.author, post_id=post.id)

    return render(request, 'newpost.html',
                  {'form': form, 'post': post, 'author': author})
