from django.urls import path
from app1.views import home, register, success

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('success/', success, name='success'),
]
