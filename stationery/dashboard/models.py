from django.db import models

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

