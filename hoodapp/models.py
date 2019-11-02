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
    
# Post model     
class Post(models.Model):
    description =  models.CharField(max_length=70)
    post_image = models.ImageField(upload_to='images/', null=True,blank=True)
    categories = models.CharField(max_length=70)
    time_created =  models.DateTimeField(auto_now=True, null =True)
    location=models.ForeignKey(Neighbourhood)
    user = models.ForeignKey(User, null=True)
    user_profile = models.ForeignKey(Profile)
    
    def __str__(self):
        return self.description       
    
# Business model     
class Business(models.Model):
    bsn_name = models.CharField(max_length=64, unique= True)
    bsn_user = models.ForeignKey(User,on_delete=models.CASCADE)
    bsn_email = models.EmailField(max_length=64, unique= True) 
    location=models.ForeignKey(Neighbourhood) 
    
    def __str__(self):
        return self.bsn_name     
    
# Comment model     
class Comment(models.Model):
    post = models.ForeignKey(Post, null=True)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment        
    