import datetime
from django.shortcuts import render ,redirect
from ..models import *
import sweetify # type: ignore

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
        supplier.updated_at = datetime.datetime.now()
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