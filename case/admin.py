from django.contrib import admin
from .models import ItemInfo, OrderInfo
# Register your models here.


@admin.register(ItemInfo)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", 'num', 'model', 'price', 'production_date', 'left_amount', 'rate_times', 'rate')


@admin.register(OrderInfo)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'customer_id', 'staff_id', 'amount', 'date', 'is_rated')