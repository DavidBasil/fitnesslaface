from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """Modifies profile display in admin section"""
    list_display = ['user', 'date_of_birth']


admin.site.register(Profile, ProfileAdmin)
