from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'app/index.html', {})


def login(request):
    return render(request, "app/login.html", {})


def units(request):
    return render(request, "app/units.html", {})
