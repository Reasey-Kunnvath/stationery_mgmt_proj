from django.shortcuts import redirect, render
import sweetify
from login import models


def login(username, password):
    try:
        user = models.Users.objects.get(username=username)
        if user.check_password(password):
            return True, 
        else:
            return False, 
    except models.Users.DoesNotExist:
        return False,
    

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_valid = login( username=username, password=password)
        
        if is_valid:
            sweetify.success(request, 'Login Successful', text='Welcome back!', persistent='OK')
            return redirect('user_home_page')  
        else:
            sweetify.error(request, 'Login Failed', text='Invalid username or password', persistent='OK')
            return redirect('user_login_page') 

    return render(request, 'login.html')
