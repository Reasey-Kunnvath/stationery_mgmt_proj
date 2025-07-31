from django.shortcuts import render

def dashboard_home(request):
    return render(request, 'index.html')

def category(request):
    return render(request, 'category.html')

def user(request):
    return render(request, 'user.html')