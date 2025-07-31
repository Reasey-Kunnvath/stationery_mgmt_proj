from django.shortcuts import render, redirect
from login.common.common import auth_adm
from login.config import roles
import sweetify

# Create your views here.
def login_page(request):
    return render(request, 'login/login_page.html', {'error': request.GET.get('error', 'False'), 'message': request.GET.get('message', '')})

def auth_adm_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        is_valid, message = auth_adm(username, password)

        if is_valid:
            return redirect('../dashboard')
        else:
            if 'Unauthorized' in message:
                sweetify.error(request, 'Access Denied', text=message, persistent='OK')
            else: 
                sweetify.error(request, 'Login Failed', text=message, persistent='OK')
            return redirect('login_page')
    return render(request, 'login/login_page.html')
