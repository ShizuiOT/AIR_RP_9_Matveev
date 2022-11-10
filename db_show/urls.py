from django.contrib import admin
from django.urls import path
from db_show import views

urlpatterns = [
    path('getSoftware', views.ReqgetSoftware),
    path('addSoftware', views.ReqsetSoftware),
]