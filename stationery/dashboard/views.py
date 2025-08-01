from django.shortcuts import render ,redirect
from .models import *
import sweetify # type: ignore
def dashboard_home(request):
    return render(request, 'index.html')
