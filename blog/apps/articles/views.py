#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, django!')

def test(request):
    return HttpResponse('This is test!')
