from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone

# Create your models here.


class HoodRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    
# Profile model

class Profile(models.Model):
    profile_pict = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length =60)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    username = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile',null=True)
    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()    
        
    def update_profile(self):
        self.update()

    def delete_profile(self):
        self.delete()   
      
# Neighbourhood model  
class Neighbourhood(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64, null=True)
    created_by =  models.CharField(max_length=64, null=True)
    police = models.CharField(max_length=20)
    police_address = models.CharField(max_length=20)
    health_center = models.CharField(max_length=20)
    health_center_address = models.CharField(max_length=20)
           
    def __str__(self):
        return self.name           