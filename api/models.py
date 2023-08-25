
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
    created_at = models.DateTimeField(auto_now_add=True)
    clerk = models.ForeignKey('User', on_delete=models.PROTECT)
    # legalform = 
    # bookings = 
    # accounts =
    # kontenrahmen
    # address

    def __str__(self) -> str:
        return f"{self.name} ({self.number})"
    

class AccountChart(models.Model):
    name = models.CharField(max_length=128)
    is_template = models.BooleanField(default=False)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f"{self.name} ({self.id})"
    

class Account(models.Model):
    name =  models.CharField(max_length=128, default="Default")
    number = models.IntegerField(default=0)
    non_deductible_tax = models.BooleanField(default=False)
    account_chart = models.ForeignKey('AccountChart', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, default=None)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    BALANCE = "BA"
    PROFIT_LOSS = "PL"
    DOCUMENT_CHOICES = [
        (BALANCE, "Balance"),
        (PROFIT_LOSS, "Profit and Loss")
    ]

    name = models.CharField(max_length=1024)
    document = models.CharField(max_length=2, choices=DOCUMENT_CHOICES, default=BALANCE)

    def __str__(self):
        return f"{self.document}: {self.name}"
