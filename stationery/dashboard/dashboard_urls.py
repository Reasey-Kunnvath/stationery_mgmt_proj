
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('category', views.category, name='category'),
    path('users', views.user, name='user'),
]
