from django.shortcuts import render ,redirect
from .models import *
import sweetify # type: ignore
def dashboard_home(request):
    return render(request, 'index.html')
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
def user(request):
    return render(request, 'user.html')
def item(request):
    return render(request, 'setting/item/index.html')
def itemCreate(request):
    return render(request, 'setting/item/create.html')