from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Author
import logging
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, 'post/allposts.html')


def post(request, post_id):
    post = get_object_or_404(Post.objects, pk=post_id)
    tags = post.tags.all()
    comments = Comment.objects.filter(post=post.id).order_by('-posted_at')
    return render(request, 'post/post.html', {'post': post, 'tags': tags, 'comments': comments})


def search(request, id=''):
    if request.method == "POST":
        post_id = request.POST['q']
        return redirect('/post/' + post_id)
    else:
        post = get_object_or_404(Post, pk=id)
        return render(request, 'post/post.html', {'post': post})


def all(request):
    posts = Post.objects.all()
    return render(request, 'post/allposts.html', {'posts': posts})


def newComment(request):
    if request.method == "POST":
        text = request.POST['comment']
        comment = Comment()
        comment.author = Author.objects.filter(id=1)[0]
        comment.posted_at = datetime.now()
        comment.description = text
        comment.post = Post.objects.filter(id=1)[0]
        comment.save()
        return redirect('/post/1')
