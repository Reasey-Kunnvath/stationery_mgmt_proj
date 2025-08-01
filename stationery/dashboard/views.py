from django.shortcuts import render ,redirect
from .models import *
import sweetify # type: ignore
def dashboard_home(request):
    return render(request, 'index.html')
# Category Routes
def category(request):
    category=Category.objects.all()
    return render(request, 'setting/category/index.html', {'categories': category})
def categoryCreate(request):
    
    return render(request, 'setting/category/create.html')
def categoryStore(request):
    category=Category.objects.all()
    if request.method == 'POST':
        category = Category()
        category.cate_name = request.POST.get('cate_name')
        category.cate_desc = request.POST.get('cate_desc')
        category.save()
        sweetify.success(request, 'Category Create Successfully ') # type: ignore
        return redirect(to='category')
    else:
        return render(request=request, template_name='setting/category/create.html')
def categoryEdit(request,id):
    category = Category.objects.get(cate_id=id)
    return render(request, 'setting/category/edit.html', {'category': category})
def categoryUpdate(request, id):
    if request.method == 'POST':
        category = Category.objects.get(cate_id=id)
        category.cate_name = request.POST.get('cate_name')
        category.cate_desc = request.POST.get('cate_desc')
        category.save()
        sweetify.success(request, 'Category Updated Successfully') # type: ignore
        return redirect(to='category')
    else:
        return render(request=request, template_name='setting/category/edit.html', context={'category': category})
def categoryDelete(request, id):
    category = Category.objects.get(cate_id=id)
    category.delete()
    sweetify.success(request, 'Category Deleted Successfully') # type: ignore
    return redirect(to='category')

# Supplier Routes
def supplier(request):
    supplier = Supplier.objects.all()
    return render(request, 'setting/supplier/index.html', {'suppliers': supplier})
def supplierCreate(request):
    return render(request, 'setting/supplier/create.html')
def supplierStore(request):
    if request.method == 'POST':
        supplier = Supplier()
        supplier.splr_name = request.POST.get('supplier_name')
        supplier.splr_contact_person = request.POST.get('supplier_contact')
        supplier.splr_email = request.POST.get('supplier_email')
        supplier.splr_phone = request.POST.get('supplier_phone')
        supplier.splr_address = request.POST.get('supplier_address')
        supplier.save()
        sweetify.success(request, 'Supplier Created Successfully') # type: ignore
        return redirect(to='supplier')
    else:
        return render(request=request, template_name='setting/supplier/create.html')
def supplierEdit(request, id):
    supplier = Supplier.objects.get(splr_id=id)
    return render(request, 'setting/supplier/edit.html', {'suppliers': supplier})
def supplierUpdate(request, id):
    if request.method == 'POST':
        supplier = Supplier.objects.get(splr_id=id)
        supplier.splr_name = request.POST.get('supplier_name')
        supplier.splr_contact_person = request.POST.get('supplier_contact')
        supplier.splr_email = request.POST.get('supplier_email')
        supplier.splr_phone = request.POST.get('supplier_phone')
        supplier.splr_address = request.POST.get('supplier_address')
        supplier.save()
        sweetify.success(request, 'Supplier Updated Successfully') # type: ignore
        return redirect(to='supplier')
    else:
        return render(request=request, template_name='setting/supplier/edit.html', context={'suppliers': supplier})
def supplierDelete(request, id):
    supplier = Supplier.objects.get(splr_id=id)
    supplier.delete()
    sweetify.success(request, 'Supplier Deleted Successfully') # type: ignore
    return redirect(to='supplier')
def user(request):
    return render(request, 'user.html')

# Item Routes
def item(request):
    items = Item.objects.all()
    return render(request, 'setting/item/index.html', {'items': items})
def itemCreate(request):
    categories = Category.objects.all()
    return render(request, 'setting/item/create.html', {'categories': categories})
def itemStore(request):
    if request.method == 'POST':
        item = Item()
        item.item_name = request.POST.get('item_name')
        item.item_desc = request.POST.get('item_desc')
        item.item_img = request.FILES['item_img']
        if len(request.FILES) > 0:          
                item.item_img = request.FILES['item_img']
        item.cate_id_id = request.POST.get('cate_id')
        item.save()
        sweetify.success(request, 'Item Created Successfully') # type: ignore
        return redirect(to='item')
    else:
        return render(request=request, template_name='setting/item/create.html')
def itemEdit(request, id):
    item= Item.objects.get(item_id = id)
    categories = Category.objects.all()
    return render(request,'setting/item/edit.html',{'items':item,'categories':categories})
