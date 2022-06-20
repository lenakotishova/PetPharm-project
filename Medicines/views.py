from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse('Hello')


def index1(request):
    print(request)
    return HttpResponse('<b>Test page</b>')
