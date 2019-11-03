from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count
from .forms import PostForm
from .models import UserProfile, Post, Post_shared_with

@login_required
def index(request):
    userPosts = Post.objects.filter(created_by=request.user.id)
    shared_post_id = Post_shared_with.objects.filter(shared_id=request.user.id)
    sharedPosts = []
    for shared in shared_post_id:
            currentPost = Post.objects.filter(id=shared.post_id)
            sharedPosts.append(currentPost)
    return render(request, 'index.html/', {'userPosts' : userPosts, 'sharedPosts' : sharedPosts})
