from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^service/$", views.service_list),
    url(r"^service/edit/(?P<id>\d+)$", views.edit_service),
    url(r"^complaint/edit/(?P<id>\d+)$", views.edit_complaint),
    url(r"^complaint/$", views.complaint_list),
    url(r"^add_service/$", views.add_service),
    url(r"^add_complaint/$", views.add_complaint),
]