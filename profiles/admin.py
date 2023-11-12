# from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'subscribe_newsletter'
    )

admin.site.register(UserProfile, UserProfileAdmin)




