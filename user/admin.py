from django.contrib import admin
from .models import CustomerInfo, StaffInfo
# Register your models here.


@admin.register(CustomerInfo)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("company", 'representative', 'postcode', 'address', 'apartment', 'agent', 'telephone', 'bank', 'taxid')


@admin.register(StaffInfo)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("age", 'gender', 'apartment', 'role', 'rate_times', 'rate')
