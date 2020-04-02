from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST)
    print("login")
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        print("pass")
        return redirect("/")
    else:
        print("fail")
    context = {
        'form': form
    }

    return render(request, "login/login.html", context)

