
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.test_page, name='test_page'),
]
