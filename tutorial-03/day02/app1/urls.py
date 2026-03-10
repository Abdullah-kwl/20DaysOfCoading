from django.urls import path
from app1.views import home, about, info, contact

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('myinfo/', info, name='info'),
    path('contact/', contact, name='contact'),
]
