"""django admin customization"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

from core import models


class UserAdmin(BaseUserAdmin):
    """Define admin page for user"""

    ordering = ["id"]
    list_display = ["email", "name"]


admin.site.register(models.User, UserAdmin)
