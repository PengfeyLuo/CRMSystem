from django.shortcuts import render
from .models import ItemInfo, OrderInfo
# Create your views here.


def item_list(request):
    item_list = ItemInfo.objects.all()
    return render(request, "itemlist.html", {"item_list": item_list})


def order_list(request):
    order_list = OrderInfo.objects.all()
    return render(request, "orderlist.html", {"order_list": order_list})