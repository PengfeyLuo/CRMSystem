from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^service/$", views.service_list),
    url(r"^complaint/$", views.complaint_list),
    url(r"^add_service/$", views.add_service),
]