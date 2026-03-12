from django.shortcuts import render
from django.http import  HttpResponseRedirect
from app1.forms import RegisterForm
from app1.models import Profile

# Create your views here.

def home(request):
    return render(request, 'app1/home.html')

def register(request):
    if request.method == 'POST':
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            age = fm.cleaned_data['age']
            city = fm.cleaned_data['city']
            Profile.objects.create(name=name, age=age, city=city)
            return HttpResponseRedirect('/success/')
            # return HttpResponseRedirect('/register/')
    fm=RegisterForm()
    return render(request, 'app1/register.html', {'form': fm})

def success(request):
    return render(request, 'app1/success.html')