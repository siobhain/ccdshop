# from django.contrib import admin
# Register your models here.

from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserProfile._meta.fields]

admin.site.register(UserProfile, UserProfileAdmin)




