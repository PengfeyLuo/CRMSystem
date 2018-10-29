from django.contrib import admin
from .models import Menu, Permission, Role, UserInfo

# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("title", 'parent')


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("title", 'url', 'menu')


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(UserInfo)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("username", 'password', 'nickname', 'email', 'is_customer', 'database_id',)