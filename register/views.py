from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(respone):
    if respone.method == "POST":
        form = RegisterForm(respone.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()

    return render(respone, "register/register.html", {"form":form})