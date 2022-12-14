from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
   pass

class UserProfile(models.Model):
   full_name = models.CharField(max_length=250,null=True,blank=True)
   user = models.OneToOneField(User,on_delete=models.CASCADE)

   def __str__(self):
      return self.full_name

class UserSettings(models.Model):
   owner = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
   
class PasswordToken(models.Model):
    token = models.UUIDField(null=False)
    email = models.EmailField(null=False, blank=False)
    name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    user_id = models.PositiveIntegerField(null=True)
    is_staff = models.BooleanField(null=False, default=False)
    token_life = models.PositiveIntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.token)