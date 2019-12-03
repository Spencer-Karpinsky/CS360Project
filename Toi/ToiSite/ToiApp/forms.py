from django import forms
from .models import Post, UserProfile
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('photo','title','caption')

class updateUser(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class updateProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic']