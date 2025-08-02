from django.shortcuts import render ,redirect

def supply_in(request):
    return render(request, '<h1>Stock In Page</h1>')