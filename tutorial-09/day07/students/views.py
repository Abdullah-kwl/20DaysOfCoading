from django.shortcuts import render
from students.models import Profile

# Create your views here.
def home(request):
    return render(request, 'students/home.html')

def profile(request,roll_number):
    profile = Profile.objects.filter(roll_number=roll_number).first()
    if profile:
        return render(request, 'students/profile.html', context={'profile': profile})
    return render(request, 'students/profile.html', context={'error': 'Profile not found.'})