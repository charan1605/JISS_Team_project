

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models


    

class registrar(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class judge(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class lawyer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)



    