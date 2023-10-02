from django.contrib import admin
from .models import UserAdmin,AddDr,UserContact,HomeInfo,AddWork
# Register your models here.


admin.site.site_header='Oia Clinick Admin Panel'
admin.site.register(HomeInfo)
admin.site.register(UserContact)
admin.site.register(UserAdmin)

admin.site.register(AddWork)
admin.site.register(AddDr)