
from django.urls import path
from . import views
from .controller import user_controller

urlpatterns = [
    path('login', views.login_page, name='user_login_page'), 
    path('login/action', user_controller.user_login, name='user_login_action'),

    path('logout', user_controller.user_logout, name='user_logout'), 

    path('home', views.home_page, name='user_home_page'),
    path('submit-order/', user_controller.submit_order, name='submit_order'),


]
