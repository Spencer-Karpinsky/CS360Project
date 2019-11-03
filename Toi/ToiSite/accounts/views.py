from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.apps import apps
from django.contrib.auth.models import User
def signup(request):
    UserProfile = apps.get_model('ToiApp', 'UserProfile')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            userid = User.objects.filter(username=user.username)
            for id in userid:
                currentid=id
            newProfile = UserProfile(user=currentid)
            newProfile.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'Register.html',{'form': form})
