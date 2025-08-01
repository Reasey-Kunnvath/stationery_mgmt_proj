from django.shortcuts import render ,redirect
from ..models import *
import sweetify # type: ignore

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
def itemUpdate(request, id):
    categories = Category.objects.all()
    if request.method == 'POST':
        item = Item.objects.get(item_id=id)
        item.item_name = request.POST.get('item_name')
        item.item_desc = request.POST.get('item_desc')
        if len(request.FILES) > 0:          
            if item.item_img:
                item.item_img.delete()          
            item.item_img = request.FILES['item_img']
        item.cate_id_id = request.POST.get('cate_id')
        item.save()
        sweetify.success(request, 'Item Updated Successfully') # type: ignore
        return redirect(to='item')
    else:
        return render(request=request, template_name='setting/item/edit.html', context={'items': item, 'categories': categories})
def itemDelete(request, id):
    item = Item.objects.get(item_id=id)
    if item.item_img:
        item.item_img.delete()
    item.delete()
    sweetify.success(request, 'Item Deleted Successfully') # type: ignore
    return redirect(to='item')
