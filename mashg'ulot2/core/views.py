from django.shortcuts import render

# Create your views here.


def index(request):
    ctx = {}
    return render(request, "index.html", ctx)

def computers(request):
    ctx = {}
    return render(request, "computers.html", ctx)

def games(request):
    ctx = {}
    return render(request, "games.html", ctx)

