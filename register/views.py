from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth import authenticate, login
from .forms import RegistForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# def register(respone):
#     if respone.method == "POST":
#         form = RegisterForm(respone.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("/")
#     else:
#         form = RegisterForm()
#
#     return render(respone, "register/reg.html", {"form":form})
#

class CreateUser(generic.CreateView):
    template_name = 'register/reg.html'
    form_class = RegistForm

    def get(self, request, *args, **kwargs):
        return render(request, 'register/reg.html', {})

    def post(self, request, *args, **kwargs):
        form = RegistForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                request.POST.get('username'),
                email=request.POST.get('email'),
                password=request.POST.get('password'),
                is_active=True)
            user.save()
            return redirect("/")
        else:
            return render(request,"register/reg.html", {"form": form})







