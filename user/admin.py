from django.contrib import admin
from .models import CustomerMessage, StaffMessage
# Register your models here.

admin.site.register(CustomerMessage)
admin.site.register(StaffMessage)
