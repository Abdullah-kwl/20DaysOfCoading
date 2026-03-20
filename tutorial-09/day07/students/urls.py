from django.urls import path
from students.views import home, profile

urlpatterns = [
    path('', home, name='home'),
    path('profile/<str:roll_number>/', profile, name='profile'),
]