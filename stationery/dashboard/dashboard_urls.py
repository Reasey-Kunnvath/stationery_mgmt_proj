
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
    
    # Supplier Routes
    path('supplier', views.supplier, name='supplier'),
    path('supplier/create/', views.supplierCreate, name='supplier_create'),
    path('supplier/store/', views.supplierStore, name='supplier_store'),
    path('supplier/edit/<int:id>/', views.supplierEdit, name='supplier_edit'),
    path('supplier/update/<int:id>/', views.supplierUpdate, name='supplier_update'),
    path('supplier/delete/<int:id>/', views.supplierDelete, name='supplier_delete'),

    #Item Routes
    path('item', views.item, name='item'),
    path('item/create/', views.itemCreate, name='item_create'),
    path('item/store/', views.itemStore, name='item_store'),
    path('item/edit/<int:id>/', views.itemEdit, name='item_edit'),
    # path('item/update/<int:id>/', views.itemUpdate, name='item_update'),
    # path('item/delete/<int:id>/', views.itemDelete, name='item_delete'),
    
    # User Routes
    path('users', views.user, name='user'),
    
    
]
