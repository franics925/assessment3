from django.urls import path
from . import views
from django.shortcuts import render, redirect

urlpatterns = [
  path('', views.home, name='home'),
  path('widget/<int:widget_id>/', views.delete, name='delete')
]
