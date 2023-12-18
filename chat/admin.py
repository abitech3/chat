from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, AddUser, AddUserProfile, AddCompany, AppSetting, FbIntegrate, BotSetting


admin.site.register(User)
admin.site.register(AddUser)
admin.site.register(AddCompany)
admin.site.register(AppSetting)
admin.site.register(AddUserProfile)
admin.site.register(FbIntegrate)
admin.site.register(BotSetting)