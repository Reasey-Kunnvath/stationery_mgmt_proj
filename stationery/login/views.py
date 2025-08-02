from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from . import models
from .common.common import auth_adm
import sweetify
import logging

logger = logging.getLogger(__name__)

def login_page(request):
    error = request.GET.get('error', 'False')
    message = request.GET.get('message', '')
    return render(request, 'login/login_page.html', {'error': error, 'message': message})

def auth_adm_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        is_valid, message = auth_adm(username, password)

        if is_valid:
            # Authenticate the user with Django's authentication system
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('dashboard_home')  # Use a named URL
            else:
                messages.error(request, 'Authentication failed internally.')
                return redirect('login_page')
        else:
            if 'Unauthorized' in message:
                sweetify.error(request, 'Access Denied', text=message, persistent='OK')
            else:
                sweetify.error(request, 'Login Failed', text=message, persistent='OK')
            return redirect('login_page')
    return render(request, 'login/login_page.html')