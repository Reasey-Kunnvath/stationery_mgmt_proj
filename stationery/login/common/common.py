from login import models
from login.config import roles

def auth_adm(username, password):
    try:
        user = models.Users.objects.get(username=username)
        if user.check_password(password):
            if user.role_id_id == roles.admin:
                return True, 'Login successful'
            else:
                return False, 'Unauthorized access.'
        else:
            return False, 'Invalid username or password'
    except models.Users.DoesNotExist:
        return False, 'Invalid username or password'