from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count
from .forms import PostForm, updateUser, updateProfile
from .models import UserProfile, Post, Post_shared_with
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
    return render(request, 'Register.html')

@login_required
def index(request):
    userPosts = Post.objects.filter(created_by=request.user.id)
    return render(request, 'index.html', {'userPosts' : userPosts})

@login_required
def sharedWithMe(request):
    shared_post_id = Post_shared_with.objects.filter(shared_id=request.user.id)
    sharedPosts = []
    for shared in shared_post_id:
            currentPost = Post.objects.filter(id=shared.post_id)
            sharedPosts.append(currentPost)
    return render(request, 'SharedWithMe.html', {'sharedPosts' : sharedPosts})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = updateUser(request.POST, instance=request.user)
        p_form = updateProfile(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')#to avoid the post/get redirect pattern and sends get request
    else: #when new data is submitted
        u_form = updateUser(instance=request.user)
        p_form = updateProfile(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'profile.html', context)

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

class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)
