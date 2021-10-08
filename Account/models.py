from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    referCode = models.CharField(max_length=255)
    point = models.IntegerField(default=0)
    dollar = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    date = models.CharField(max_length=255)
    #image = models.ImageField(upload_to='Users/image/', blank=True)
    dailyCheckCount = models.IntegerField(default=0)
    redeem = models.IntegerField(default=0)
    #username = None

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []
