from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^item/$", views.item_list),
    url(r"^order/$", views.order_list),
    url(r"^add_order/$", views.add_order),
    url(r"^add_item/$", views.add_item),
    url(r"^item/edit/(?P<id>\d+)$", views.edit_item),
    url(r"^order/edit/(?P<id>\d+)$", views.edit_order),
    url(r"^order/rate/(?P<id>\d+)$", views.rate),
]