from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    return HttpResponse("Hello World")


def welcome(request):
    return HttpResponse("Welcome to Django")


def home(request):
    page = "<h1>This is the home page</h1>"
    return HttpResponse(page)