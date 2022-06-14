from django.shortcuts import render
from .models import Post

def home_view(request):
    post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'index.html', context)

def detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'object': post
    }
    return render(request, 'detail.html', context)
