from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count
from .forms import PostForm
from .models import UserProfile, Post, Post_shared_with
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def index(request):
    userPosts = Post.objects.filter(created_by=request.user.id)
    return render(request, 'index.html/', {'userPosts' : userPosts})

@login_required
def sharedWithMe(request):
    shared_post_id = Post_shared_with.objects.filter(shared_id=request.user.id)
    sharedPosts = []
    for shared in shared_post_id:
            currentPost = Post.objects.filter(id=shared.post_id)
            sharedPosts.append(currentPost)
    return render(request, 'SharedWithMe.html', {'sharedPosts' : sharedPosts})

@login_required
def viewPost(request, pk):
    pass

@login_required
def viewProfile(request,pk):
    pass

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'photo', 'caption']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
