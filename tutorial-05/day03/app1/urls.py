from app1.views import home, student
from django.urls import path, include

urlpatterns = [
    path('home/', home, name='home'),
    path('student/', student, name='student'),
]
