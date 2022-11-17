from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
  def create_user(self, email, password = None, **extra_fields):
    """Create, save and return new user"""
    user = self.model(email = email , **extra_fields)
    user.set_password(password)
    user.save(using = self._db)
    return user

  def create_superuser(self, email, password):
    """Create and return new superuser"""
    user = self.create_user(email,password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using =self._db)
    return user