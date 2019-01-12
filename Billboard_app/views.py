from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def index(request):
    return render(request, "Billboard_app/index.html")


def login(request):
    return render(request, "Register/login.html")


def register(request):
    if request.method == "POST":
        user = UserCreationForm(request.POST)
        if user.is_valid():
            return HttpResponseRedirect('')
    else:
        return render(request, "Register/register.html")


def home(request):
    return render(request, "Billboard_app/home.html", {"posts": get_recent_posts(), "form": BillboardForm()})


@csrf_exempt
def add_bb(request):
    if request.method == "POST":
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return HttpResponseRedirect('/billboard/')
    else:
        return render(request, 'registration/register.html', {"form": UserCreationForm()})



