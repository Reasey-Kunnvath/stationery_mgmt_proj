
from django.urls import path
from . import views
from .controller import auth_controller

urlpatterns = [
    path('login', views.login_page, name='user_login_page'), 
    path('login/action', auth_controller.user_login, name='user_login_action'),

    path('home', views.home_page, name='user_home_page'),
]
