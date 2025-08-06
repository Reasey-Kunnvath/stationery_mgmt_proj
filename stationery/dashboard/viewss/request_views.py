from django.shortcuts import render ,redirect
from login.models import *
from user.models import *
from dashboard.models import *
from ..models import *
import datetime
import sweetify # type: ignore


def request(request):
	order = Order.objects.all()
	return render(request, 'supply_mgmt/request/index.html', {'orders': order})

def request_detail(request, id):
	order = OrderItem.objects.filter(order_id=id)
	orderDetail = Order.objects.get(order_id=id)
	return render(request, 'supply_mgmt/request/detail.html', {'orders': order, 'orderDetail': orderDetail})
def request_delete(request, id):
    try:
        order = Order.objects.get(order_id=id)
        order.delete()
        sweetify.success(request, 'Request deleted successfully!', icon='success')
    except Order.DoesNotExist:
        sweetify.error(request, 'Request not found!', icon='error')
    except Exception as e:
        sweetify.error(request, f'An error occurred: {str(e)}', icon='error')
    return redirect('request')