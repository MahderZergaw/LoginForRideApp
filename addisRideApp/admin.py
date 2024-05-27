from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, DriverProfile, UserProfile

admin.site.register(CustomUser, UserAdmin)
admin.site.register(DriverProfile)
admin.site.register(UserProfile)
