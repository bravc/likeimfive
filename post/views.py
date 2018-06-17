from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
import logging

# Create your views here.


def index(request):
    return render(request, 'post/allposts.html')


def search(request, id=''):
    if request.method == "POST":
        post_id = request.POST['q']
        post = get_object_or_404(Post, pk=post_id)
        tags = post.tags.all()
        comments = Comment.objects.filter(post=post.id)
        return render(request, 'post/post.html', {'post': post, 'tags': tags, 'comments': comments})
    else:
        post = get_object_or_404(Post, pk=id)
        return render(request, 'post/post.html', {'post': post})


def all(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'post/allposts.html', {'posts': posts})


# def newComment(request):
#     if request.method == "POST":
#         text = request.POST['comment']
