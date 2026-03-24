from django.urls import path
from api.views import student_api

urlpatterns = [
    path('studentapi/', student_api, name='student_api'),
]