from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required

@login_required
def Chessboard(request):
    return render(request, "chessboard/board1.html")
