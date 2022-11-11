from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.TextField()
    type = models.TextField()
    age = models.PositiveIntegerField()
    isVaccinated = models.BooleanField()

class Account(models.Model):
    userName = models.EmailField()
    passWord = models.TextField()