from django.db import models
from login.models import *

# Create your models here.
class Category(models.Model):
    cate_id = models.AutoField(primary_key=True)
    cate_name = models.CharField(max_length=255)
    cate_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    item_desc = models.TextField()
    item_img = models.ImageField(upload_to='item_images/')
    cate_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

class Supplier(models.Model):
    splr_id = models.AutoField(primary_key=True)
    splr_name = models.CharField(max_length=255)
    splr_contact_person = models.CharField(max_length=255)
    splr_email = models.EmailField()
    splr_phone = models.CharField(max_length=20)
    splr_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
class StockIn(models.Model):
    stock_in_id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)



class StockOut(models.Model):
    stock_out_id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_id = models.ForeignKey('user.OrderItem', on_delete=models.CASCADE)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
