from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello2(request):
    return HttpResponse("Hello World 2")


def welcome2(request , **kwargs):
    name = kwargs.get('name')
    return HttpResponse(f"Welcome to Django 2 \n {name}")


def home2(request):
    page = "<h1>This is the home page 2</h1>"
    return HttpResponse(page)