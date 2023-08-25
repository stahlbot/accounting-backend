from django.contrib import admin
from .models import Account, AccountChart, User
from .models import Client

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(AccountChart)
admin.site.register(Account)