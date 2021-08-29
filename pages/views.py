from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse('<h1>Hello World</h>')
    return render(request, 'pages/index.html')


def about(reqest):
    return render(reqest, 'pages/about.html')

def tnc(request):
    return render(request, 'pages/tnc.html')