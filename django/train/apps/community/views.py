from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .models import Post
from .forms import postForm,CommentForm


def community(request):
    posts = Post.objects.all().order_by('-posted_time')
    comment_form = CommentForm()
    return render(request, 'community/community.html', {'posts': posts, 'comment_form': comment_form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('community')
    return redirect('community')

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
    return redirect('community')


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user) 
    else:
        post.likes.add(request.user)  
    return redirect('community')  