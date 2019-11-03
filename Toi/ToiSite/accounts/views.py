from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import SignUpForm
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # auth_login(request, user)
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'Register.html',{'form': form})
