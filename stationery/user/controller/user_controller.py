from django.shortcuts import redirect, render
from django.urls import reverse  # ✅ Import this
import sweetify
from login.models import Users
from user.models import Order, OrderItem
from dashboard.models import Item
from login import models
import json

def login(username, password):
    try:
        user = models.Users.objects.get(username=username)
        if user.check_password(password):
            return True, user 
        else:
            return False, None
    except models.Users.DoesNotExist:
        return False, None

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        is_valid, user = login(username=username, password=password) 

        if is_valid:
            request.session['user_id'] = user.user_id 

            sweetify.success(request, 'Login Successful', text='Welcome back!', persistent='OK')
            return redirect('user_home_page')  
        else:
            sweetify.error(request, 'Login Failed', text='Invalid username or password', persistent='OK')
            return redirect('user_login_page') 

    return render(request, 'login.html')

def submit_order(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        print("user id", user_id)
        if not user_id:
            sweetify.error(request, 'Not Logged In', text='Please log in first.', persistent='OK')
            return redirect('user_login_page')

        try:
            user = Users.objects.get(user_id=user_id)
            cart_data = json.loads(request.POST.get('cart', '[]'))

            if not cart_data:
                sweetify.error(request, 'Empty Cart', text='No items in cart.', persistent='OK')
                return redirect('user_home_page')

            order = Order.objects.create(user=user)

            for item in cart_data:
                item_obj = Item.objects.get(item_id=item['id'])
                OrderItem.objects.create(order=order, item=item_obj, quantity=item['quantity'])

            sweetify.success(request, 'Order Placed', text='Your order has been submitted.', persistent='OK')

            return redirect(f"{reverse('user_home_page')}?ordered=1")

        except Exception as e:
            sweetify.error(request, 'Error', text=str(e), persistent='OK')
            return redirect('user_home_page')

    return redirect('user_home_page')


def user_logout(request):
    request.session.flush()
    return redirect('user_login_page') 