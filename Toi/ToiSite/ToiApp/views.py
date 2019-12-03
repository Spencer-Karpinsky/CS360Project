from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count
from .forms import PostForm, updateUser, updateProfile
from .models import UserProfile, Post, Post_shared_with
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

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
            currentPost = Post.objects.filter(id=shared.post_id.id)
            sharedPosts.append(currentPost)
    return render(request, 'SharedWithMe.html', {'sharedPosts' : sharedPosts})

@login_required
def shareableUsers(request, pk):
    targetPost = Post.objects.get(id=pk)
    userProfile = UserProfile.objects.get(user=request.user.id)
    friends = userProfile.friends.all()
    return render(request, 'shareableUsers.html', {'friends': friends, 'targetPost': targetPost})


@login_required
def sharePost(request, pk, post_pk):
    sharedByUser = request.user
    targetUser = User.objects.get(id=pk)
    targetPost = Post.objects.get(id=post_pk)
    shared_relation  = Post_shared_with(post_id=targetPost,shared_id=targetUser)
    shared_relation.save()
    response = redirect('/index')
    return response

@login_required
def addFriends(request):
    currentProfile = UserProfile.objects.get(user=request.user.id)
    currentFriends = currentProfile.friends.all()
    addableUsers = User.objects.all().exclude(id__in=currentFriends)
    return render(request, 'addFriends.html', {'addableUsers': addableUsers})

@login_required
def addFriend(request, pk):
    targetUser = User.objects.get(id=pk)
    userProfile = UserProfile.objects.get(user=request.user.id)
    userProfile.friends.add(targetUser)
    response = redirect('/friends')
    return response

@login_required
def friends(request):
    userProfile = UserProfile.objects.get(user=request.user.id)
    friends = userProfile.friends.all()
    return render(request, 'friends.html', {'friends' : friends})

@login_required
def view_profile(request,pk):
    targetUser = User.objects.get(id=pk)
    posts = Post.objects.filter(created_by=pk)
    return render(request, 'view_profile.html', {'targetUser': targetUser, 'posts': posts})


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


