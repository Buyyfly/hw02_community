from .models import Group, Post
from .settings import POSTS_PAGE
from django.shortcuts import get_object_or_404, render


def index(request):
    posts = Post.objects.all()[:POSTS_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).all()[:POSTS_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
