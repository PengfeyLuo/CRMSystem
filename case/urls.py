from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^item/$", views.item_list),
    url(r"^order/$", views.order_list),
]