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
    return render(request, "Register/register.html")


def home(request):
    collect_bb = Messages.objects.all()
    for element in collect_bb:
        print(element.title)
        print(element.content)
        print(element.author)
        print(element.date)
        print(len(collect_bb))
    return render(request, "Billboard_app/home.html", context={'Billboards': collect_bb, 'size': len(collect_bb)})


@csrf_exempt
def add_bb(request):
    if request.is_ajax():
        resp = {'status': 'success'}
        print(request.POST.get('title'))
        print(request.POST.get('content'))
        print(request.POST.get('author'))
        msg = Messages(title=request.POST.get('title'), content=request.POST.get('content'),
                       author=request.POST.get('author'))
        msg.save()
    else:
        resp = {'status': 'error'}
    return HttpResponse(resp)



