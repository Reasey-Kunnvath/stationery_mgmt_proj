from django.shortcuts import render ,redirect
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from login.models import *
from user.models import *
from dashboard.models import *
from ..models import *
import datetime
import sweetify # type: ignore

def supply_out(request):
    stockout = StockOut.objects.all().order_by('-created_at')
    return render(request, 'supply_mgmt/stock_out/index.html', {'stockout': stockout})

def supply_out_create(request,id):
    order = OrderItem.objects.filter(order_id=id)
    orderDetail = Order.objects.get(order_id=id)
    # Logic for creating a stock out entry
    return render(request, 'supply_mgmt/stock_out/create.html', {'orderDetail': orderDetail, 'orders': order})
def supply_out_store(request):
    if request.method == 'POST':
        item_ids = request.POST.getlist('item_id')
        quantities = request.POST.getlist('item_qty')
        order_ids = request.POST.getlist('order_id')

        created_count = 0  # for success tracking

        for i in range(len(item_ids)):
            try:
                order_id = order_ids[i]
                item_id = item_ids[i]
                quantity = quantities[i]

                order_item = OrderItem.objects.get(id=order_id)

                stock_out = StockOut(
                    item_id_id=item_id,
                    quantity=quantity,
                    order_id=order_item,
                    created_by_id=request.user.user_id,
                    created_at=datetime.datetime.now()
                )
                stock_out.save()
                created_count += 1

            except ObjectDoesNotExist:
                sweetify.error(request, f'Order with ID {order_id} not found!', icon='error')
            except MultipleObjectsReturned:
                sweetify.error(request, f'Multiple Orders with ID {order_id} found!', icon='error')
            except Exception as e:
                print(f'An error occurred: {str(e)}')
        if created_count:
            sweetify.success(request, f'{created_count} stock out entries created successfully!', icon='success')
            Order.objects.filter(order_id=order_id).update(status='completed')
        return redirect('supply_out')

    return render(request, 'supply_mgmt/stock_out/index.html')

