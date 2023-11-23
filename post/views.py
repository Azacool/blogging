from django.shortcuts import render
from .models import Post

def main(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def detail(request, pk):
    post = Post.objects.get(id=int(pk))
    images = Post.objects.filter(post=pk)
    return render(request, 'post.html', {'images':images, 'post':post})