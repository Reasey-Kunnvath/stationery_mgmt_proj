import datetime
from django.shortcuts import render ,redirect
from ..models import *
import sweetify # type: ignore


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
        category.updated_at = datetime.datetime.now()
        sweetify.success(request, 'Category Updated Successfully') # type: ignore
        return redirect(to='category')
    else:
        return render(request=request, template_name='setting/category/edit.html', context={'category': category})
def categoryDelete(request, id):
    category = Category.objects.get(cate_id=id)
    category.delete()
    sweetify.success(request, 'Category Deleted Successfully') # type: ignore
    return redirect(to='category')