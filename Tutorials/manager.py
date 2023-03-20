from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
   
   def create_user(self,email,password,**extrafields):
      if email is not None:
         raise ValueError('Enter you email')

      email=self.normalize_email(email)
      user=self.model(
      email=email,
      **extrafields
         )
      user.set_password(password)
      user.save()
      return user
         
   def create_superuser(self,email,password,**extrafields):
      extrafields.setdefault('is_superuser',True)
      extrafields.setdefault('is_staff',True)
      extrafields.setdefault('is_active',True)

      if extrafields.get('is_superuser') is not True:
         raise ValueError('Superuser must have is_superuser True')
      
      if extrafields.get('is_staff') is not True:
         raise ValueError('Superuser must have is_staff True')

      if extrafields.get('is_active') is not True:
         raise ValueError('Superuser must have is_active True')


      return self.create_user(email, password,**extrafields)