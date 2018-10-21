"""CRMSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from user import views as userviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', userviews.index),
    url(r'^logout/$', userviews.logout),
    url(r'^login/$', userviews.login),
    url(r'^$', userviews.login),

    url(r'^case/', include('case.urls')),
    url(r'^rbac/', include('rbac.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^feedback/', include('feedback.urls')),
]
