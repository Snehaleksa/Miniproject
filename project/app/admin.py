from django.contrib import admin
from .models import User,CustomUser,Bank,Transaction
# Register your models here.

admin.site.register(User)
admin.site.register(CustomUser)
admin.site.register(Bank)
admin.site.register(Transaction)