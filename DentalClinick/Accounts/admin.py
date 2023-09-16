from django.contrib import admin
from .models import UserAdmin,AddDr,UserContact,HomeInfo
# Register your models here.


admin.site.register(HomeInfo)
admin.site.register(AddDr)