from django.urls import path
from . import views

app_name = 'register'
urlpatterns = [
    path('', views.CreateUser.as_view(), name='reg'),
]