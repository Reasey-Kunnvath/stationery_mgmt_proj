from django.shortcuts import render ,redirect
from ..models import *
import sweetify # type: ignore
def user(request):
    return render(request, 'user.html')