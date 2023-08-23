
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.dispatch import receiver
# from django.db.models.signals import post_save
# from rest_framework.authtoken.models import Token


class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(blank=True)

    def __str__(self):
        return self.username
    

class Client(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()
    created_at = models.DateTimeField()
    clerk = models.ForeignKey('User', on_delete=models.PROTECT)
    # legalform = 
    # bookings = 
    # accounts =
    # kontenrahmen
    # address

    def __str__(self) -> str:
        return f"{self.name} ({self.number})"