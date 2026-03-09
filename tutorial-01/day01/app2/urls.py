from django.urls import path
from app2.views import hello2, welcome2
    
urlpatterns = [
    path('hello/', hello2, name='hello2'),
    path('welcome/', welcome2, name='welcome2', kwargs={'name': 'Abdullah'}),
    # path('welcome/', welcome2, name='welcome2'),
]
