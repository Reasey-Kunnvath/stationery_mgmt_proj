
from django.urls import path
from . import views

from dashboard.viewss import item_views,user_views,supplier_views,category_views, stock_in_views, stock_out_views


urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    
    #Category Routes
    path('category', category_views.category, name='category'),
    path('category/create/', category_views.categoryCreate, name='category_create'),
    path('category/store/', category_views.categoryStore, name='category_store'),
    path('category/edit/<int:id>/', category_views.categoryEdit, name='category_edit'),
    path('category/update/<int:id>/', category_views.categoryUpdate, name='category_update'),
    path('category/delete/<int:id>/', category_views.categoryDelete, name='category_delete'),
    
    # Supplier Routes
    path('supplier', supplier_views.supplier, name='supplier'),
    path('supplier/create/', supplier_views.supplierCreate, name='supplier_create'),
    path('supplier/store/', supplier_views.supplierStore, name='supplier_store'),
    path('supplier/edit/<int:id>/', supplier_views.supplierEdit, name='supplier_edit'),
    path('supplier/update/<int:id>/', supplier_views.supplierUpdate, name='supplier_update'),
    path('supplier/delete/<int:id>/', supplier_views.supplierDelete, name='supplier_delete'),

    #Item Routes
    path('item', item_views.item, name='item'),
    path('item/create/', item_views.itemCreate, name='item_create'),
    path('item/store/', item_views.itemStore, name='item_store'),
    path('item/edit/<int:id>/', item_views.itemEdit, name='item_edit'),
    path('item/update/<int:id>/', item_views.itemUpdate, name='item_update'),
    path('item/delete/<int:id>/', item_views.itemDelete, name='item_delete'),
    
    # User Routes
    path('users', user_views.user, name='user'),
    path('users/create/', user_views.userCreate, name='user_create'),
    path('users/store/', user_views.userStore, name='user_store'),
    path('users/edit/<int:id>/', user_views.userEdit, name='user_edit'),
    path('users/update/<int:id>/', user_views.userUpdate, name='user_update'),
    path('users/delete/<int:id>/', user_views.userDelete, name='user_delete'),
    
    # Logout Routes
    path('logout', user_views.logout, name='logout'),

    # Supply Management Routes
    path('supply_in', stock_in_views.supply_in, name='supply_in'),
    path('supply_out', stock_out_views.supply_out, name='supply_out'),


]
