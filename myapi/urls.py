from django.contrib import admin
from django.urls import path
from myapi import views

urlpatterns = [
    path("",views.index,name='Home'),
    path("about",views.about,name='About'),
    path("",views.article,name='article'),
    path("",views.Contact,name='contact'),

]