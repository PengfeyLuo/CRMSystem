from django.conf.urls import url
from . import views
import rbac.views as rbacviews

urlpatterns = [
    url(r'^$', views.user_list),
    url(r'^authedit/(?P<id>\d+)$', rbacviews.users_edit),
    url(r'^add_customer/$', views.add_customer),
    url(r'^add_staff/$', views.add_staff),
    url(r'^edit/(?P<id>\d+)$', views.user_edit),
]