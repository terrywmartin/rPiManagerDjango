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
   
    