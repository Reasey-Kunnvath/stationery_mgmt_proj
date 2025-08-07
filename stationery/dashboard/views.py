from itertools import count
from django.shortcuts import render ,redirect
from .models import *
from user.models import *
from login.models import *
from dashboard.models import *
from django.db.models import Avg, Count, Min, Sum
import sweetify # type: ignore
def dashboard_home(request):
    order_count = Order.objects.count()
    user_count = Users.objects.count()
    stock_out_count = StockOut.objects.values('order_id').distinct().count()
    stock_in_count = StockIn.objects.aggregate(total_qty=Sum("quantity"))['total_qty']
    context = {
        'order_count': order_count,
        'user_count': user_count,
        'stock_out_count': stock_out_count,
        'stock_in_count': stock_in_count
    }
    return render(request, 'index.html', context)
