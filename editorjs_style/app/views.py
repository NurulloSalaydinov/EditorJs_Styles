from django.shortcuts import render, redirect
from .models import Post
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView


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

def delete_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('/')


class AddPostView(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'post.html'
    success_url = '/'


class EditPostView(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'post.html'
    success_url = '/'
