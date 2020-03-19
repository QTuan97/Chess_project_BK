from django.shortcuts import render
from django.views import generic


def Chessboard(request):
    return render(request, "chessboard/board.html")
