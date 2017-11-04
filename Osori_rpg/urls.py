from django.conf.urls import url, include
from django.contrib import admin
from Osori_rpg import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.User_List.as_view()),
    url(r'^signup/$', views.Signup.as_view()),
    url(r'^signin/$', views.Signin.as_view()),
    url(r'^exp_request/$', views.ExpRequest.as_view()),
    url(r'^exp_request_list/$', views.ExpRequestAccept.as_view()),
]
