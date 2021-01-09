
from django.contrib import admin
from .views import login_chect,index,login
from django.urls import path

urlpatterns = [
    path('login',login),
    path('index',index),
    path('login_check',login_chect),
    path('',login)
]
