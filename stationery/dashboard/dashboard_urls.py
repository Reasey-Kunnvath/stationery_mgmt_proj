
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    
    #Category Routes
    path('category', views.category, name='category'),
    path('category/create/', views.categoryCreate, name='category_create'),
    path('category/store/', views.categoryStore, name='category_store'),
    path('category/edit/<int:id>/', views.categoryEdit, name='category_edit'),
    path('category/update/<int:id>/', views.categoryUpdate, name='category_update'),
    path('category/delete/<int:id>/', views.categoryDelete, name='category_delete'),


    #Item Routes
    path('users', views.user, name='user'),
    path('item', views.item, name='item'),
    
]
