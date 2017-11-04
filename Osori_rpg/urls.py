from django.conf.urls import url, include
from django.contrib import admin
from Osori_rpg import views

urlpatterns = [
    url(r'^$', views.User_List.as_view()),
    url(r'^signup/$', views.Signup.as_view()),
]
