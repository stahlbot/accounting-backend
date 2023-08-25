from django.contrib import admin
from .models import Account, AccountChart, Category, User
from .models import Client

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(AccountChart)
admin.site.register(Account)
admin.site.register(Category)