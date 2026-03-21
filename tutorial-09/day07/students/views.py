from django.shortcuts import render
from students.models import Profile

# Create your views here.
def home(request):
    all_profiles = Profile.objects.all()
    if all_profiles:
        return render(request, 'students/home.html', context={'profiles': all_profiles})
    return render(request, 'students/home.html')

def profile(request,roll_number):
    profile = Profile.objects.filter(roll_number=roll_number).first()
    if profile:
        return render(request, 'students/profile.html', context={'profile': profile})
    return render(request, 'students/profile.html', context={'error': 'Profile not found.'})