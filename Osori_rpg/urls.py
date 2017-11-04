"""Osori_level_meter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views
from Osori_rpg import views

urlpatterns = [
    url(r'^$', views.index, name='index_page'),
    url(r'^contribute_info/$', views.contribute_info, name='contribute_info'),
    url(r'^update_info/$', views.update_info, name='update_info'),
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
    url(r'^signin/$', views.Signin.as_view(), name='signin'),
    url(r'^exp_request/$', views.ExpRequest.as_view()),
    url(r'^exp_request_list/$', views.ExpRequestAccept.as_view()),
]
