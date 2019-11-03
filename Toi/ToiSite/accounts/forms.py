from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from ToiApp.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password1', 'password2')
