from django.shortcuts import render
from app1.forms import ProfileForm
from app1.models import Profile
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'app1/home.html')


def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            city = form.cleaned_data['city']
            pr = Profile(name=name, age=age, city=city)
            pr.save()
            return HttpResponseRedirect("/success/")
        
    else:
        form = ProfileForm()
        return render(request, 'app1/register.html', {"fm" : form})


def success(request):
    return HttpResponse("<h1>Profile created successfully!</h1>")