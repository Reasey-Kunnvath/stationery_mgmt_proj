from django.shortcuts import render, redirect
from login.models import Users
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import sweetify # type: ignore

def user(request):
    users = Users.objects.raw("""
             SELECT a.user_id, 
                    a.username,
                    a.email, 
                    CASE WHEN a.is_superuser THEN
                        'Admin'
                    ELSE 
                        b.role_desc 
                    END AS role_desc, 
                    a.created_at, 
                    a.updated_at 
                FROM login_users a LEFT JOIN login_roles b ON a.role_id::int = b.role_id::int ORDER BY a.user_id ASC
        """)
    context = {
        'users': users,
    }
    return render(request, './setting/user/index.html', context)

def userCreate(request):
    return render(request, './setting/user/create.html')

def userStore(request):
    if request.method == 'POST':
        user = Users()
        user.username = request.POST.get('ad_username')
        user.email = request.POST.get('user_email')
        user.password = make_password(request.POST.get('user_pwd'))
        user.updated_at = timezone.now()
        user.role_id_id = request.POST.get('user_role')

        user.save()
        sweetify.success(request, 'User Created Successfully')
        return redirect(to='user')
    
def userEdit(request, id):
    users = Users.objects.all().filter(user_id=id).first()
    return render(request, './setting/user/edit.html', {'user': users})

def userUpdate(request, id):
    if request.method == 'POST':
        user = Users.objects.get(user_id=id)
        user.username = request.POST.get('ad_username')
        user.email = request.POST.get('user_email')
        user.password = make_password(request.POST.get('user_pwd'))
        user.updated_at = timezone.now()
        user.role_id_id = request.POST.get('user_role')

        user.save()
        sweetify.success(request, 'User Updated Successfully')
        return redirect(to='user')
    
def userDelete(request, id):
    user = Users.objects.get(user_id=id)
    user.delete()
    sweetify.success(request, 'User Deleted Successfully')
    return redirect(to='user')

def logout(request):
    request.session.flush()
    sweetify.success(request, 'Logged out successfully', timer=1000)
    return redirect(to='login_page')