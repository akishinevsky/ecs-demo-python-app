from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, this is Polls app index")

def index_check(request):
    return HttpResponse("Hello, this is app index check request")
