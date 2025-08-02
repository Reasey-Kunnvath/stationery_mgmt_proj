from django.shortcuts import render
from dashboard.models import Item

def login_page(request):
    return render(request, 'user_login.html')

def home_page(request): 
    items = Item.objects.all()
    for item in items:
        print(f"ID: {item.item_id}, Name: {item.item_name}, Desc: {item.item_desc}, Category: {item.cate_id.cate_name} {item.item_img}")    
    return render(request, 'user_home.html', {'items': items})
