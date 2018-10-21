from django.contrib import admin
from .models import ServiceInfo, ComplaintInfo
# Register your models here.

admin.site.register(ServiceInfo)
admin.site.register(ComplaintInfo)