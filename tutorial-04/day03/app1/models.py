from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15,default="null")
    comment = models.TextField()

