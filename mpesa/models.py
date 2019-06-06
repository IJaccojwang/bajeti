from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to='profiles/')
    prefname = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.prefname

class Statement(models.Model):
    month = models.CharField(max_length=15)
    statement = models.FileField(upload_to='statements/')

    def __str__(self):
        return self.month

