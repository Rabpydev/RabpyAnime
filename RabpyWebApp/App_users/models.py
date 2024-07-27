from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    country = models.TextField(default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    