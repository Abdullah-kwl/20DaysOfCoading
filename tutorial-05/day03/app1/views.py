from django.shortcuts import render
from app1.models import Profile

# Create your views here.
def home(request):
    return render(request, 'app1/home.html')

def student(request):
    all_students = Profile.objects.all()
    return render(request, 'app1/students.html', {'students': all_students})