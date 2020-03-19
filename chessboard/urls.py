from django.urls import path
from . import views

app_name = 'chessboard'
urlpatterns =[
    path('', views.Chessboard, name="chessboard"),
]