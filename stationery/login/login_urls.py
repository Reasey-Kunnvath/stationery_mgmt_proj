
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('login/auth', views.auth_adm_login, name='auth_adm_login'),
    
    path('dashboard/', include('dashboard.dashboard_urls')),
]
