from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_affector = models.BooleanField(default=False)
    name = models.CharField(max_length=20, verbose_name='이름')


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    tag = models.CharField(max_length=50, blank=True)
    domain = models.CharField(max_length=10)
    price = models.CharField(max_length=250)
    follower = models.DecimalField(default=0, decimal_places=0, max_digits=8)
    valuation = models.FloatField(default=0.0)


class Review(models.Model):
    target = models.ForeignKey('Profile', on_delete=models.CASCADE)
    target_valuation = models.FloatField(default=None)
    target_desc = models.TextField(blank=True)

# Create your models here.
