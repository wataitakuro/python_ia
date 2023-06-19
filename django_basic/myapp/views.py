from django.shortcuts import render

# Create your views here.

from djafrngo.http import HttpResponse

def hello(request):
    return HttpResponse('Hello')

def home(request):
    return render(request, 'myapp/home.html')

def home2(request):
    context = {
        'title': 'ホーム2です'
    }
    return render(request, 'myapp/home2.html',
context)