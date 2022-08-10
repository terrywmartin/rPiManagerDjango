from django.contrib import admin

from .models import User, UserProfile, UserSettings

# Register your models here.
admin.site.register(User)
admin.site.register(UserSettings)
admin.site.register(UserProfile)