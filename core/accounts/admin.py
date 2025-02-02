from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_superuser', 'is_active')
    searching_fields = ('email')
    ordering = ['created_at']
    fieldsets = (
        ("Privacy", {"fields": ("email", "password")}),
        ("Acces", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Permissions", {"fields": ("groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)})
    )
    add_fieldsets = (
        ('Authentication',
         {"fields": ("email", "password1", "password2")}), (
            "Access",
            {"fields": ("is_staff", "is_active", "is_superuser")}))

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','title' , 'sent_to')
    ordering = ['sent_in']

admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Message)