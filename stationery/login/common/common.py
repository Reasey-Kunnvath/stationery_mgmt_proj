from login import models
from login.config import roles

def auth_adm(username, password):
    try:
        user = models.Users.objects.get(username=username)
        if user.check_password(password):
            # Check role or superuser status
            admin_role = getattr(models.Roles, 'admin', None)
            if user.role_id == admin_role or user.is_superuser:
                return True, 'Login successful'
            else:
                return False, 'Unauthorized access.'
        else:
            return False, 'Invalid username or password'
    except models.Users.DoesNotExist:
        return False, 'Invalid username or password'