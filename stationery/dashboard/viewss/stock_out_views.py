from django.shortcuts import render ,redirect

def supply_out(request):
    return render(request, '<h1>Stock Out Page</h1>')