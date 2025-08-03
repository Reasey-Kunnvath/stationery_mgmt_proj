from django.shortcuts import render ,redirect
from login.models import *
from ..models import *
import datetime
import sweetify # type: ignore

def supply_in(request):
    stockin = StockIn.objects.all().order_by('stock_in_id')
    items = Item.objects.all()
    print("Supply In View")
    return render(request, 'supply_mgmt/stock_in/index.html', {'stockins': stockin, 'items': items})
def supply_in_create(request):
    item = Item.objects.all()
    categories = Category.objects.all()
    suppliers = Supplier.objects.all()
    users = Users.objects.all()
    return render(request, 'supply_mgmt/stock_in/create.html', {'items': item, 'categories': categories, 'suppliers': suppliers, 'users': users})
def supply_in_store(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = request.POST.get('item_qty')
        price = request.POST.get('item_price')
        total_price = int(quantity) * float(price)
        supplier = request.POST.get('supplier_id')
        created_by = request.POST.get('user_id')
        created_at = datetime.datetime.now()

        stock_in = StockIn(
            item_id_id=item_id,
            quantity=quantity,
            price=price,
            total_price=total_price,
            supplier_id_id=supplier,
            created_by_id=created_by,
            created_at=created_at
        )
        stock_in.save()
        
        sweetify.success(request, 'Stock In Created Successfully', icon='success', timer=3000)
        return redirect('supply_in_create')
    return render(request, 'supply_mgmt/stock_in/create.html')
def supply_in_edit(request, id):
    stockin = StockIn.objects.get(stock_in_id=id)
    item = Item.objects.all()
    categories = Category.objects.all()
    suppliers = Supplier.objects.all()
    users = Users.objects.all()
    return render(request, 'supply_mgmt/stock_in/edit.html', {'stockins': stockin,'items': item, 'categories': categories, 'suppliers': suppliers, 'users': users})
def supply_in_update(request, id):
    item = Item.objects.all()
    categories = Category.objects.all()
    suppliers = Supplier.objects.all()
    users = Users.objects.all()
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = request.POST.get('item_qty')
        price = request.POST.get('item_price')
        total_price = int(quantity) * float(price)
        supplier = request.POST.get('supplier_id')
        created_by = request.POST.get('user_id')

        stock_in = StockIn.objects.get(stock_in_id=id)
        stock_in.item_id_id = item_id
        stock_in.quantity = quantity
        stock_in.price = price
        stock_in.total_price = total_price
        stock_in.supplier_id_id = supplier
        stock_in.created_by_id = created_by
        stock_in.updated_at = datetime.datetime.now()  # Uncomment if you want to track updates
        stock_in.save()

        sweetify.success(request, 'Stock In Updated Successfully', icon='success', timer=3000)
        return redirect('supply_in')
    return render(request, 'supply_mgmt/stock_in/edit.html', {'stockins': stock_in, 'items': item, 'categories': categories, 'suppliers': suppliers, 'users': users})
def supply_in_delete(request, id):
    stock_in = StockIn.objects.get(stock_in_id=id)
    stock_in.delete()
    sweetify.success(request, 'Stock In Deleted Successfully', icon='success', timer=3000)
    return redirect('supply_in')