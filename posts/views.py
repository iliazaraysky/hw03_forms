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
def post_view(request):
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
    latest = User.objects.get(username=username)
    return render(request, 'profile.html', {'latest': latest})
#
#
# def post_view(request, username, post_id):
#     pass
#
#
# def post_edit(request, username, post_id):
#     pass
