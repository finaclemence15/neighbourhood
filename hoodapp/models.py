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
    occupants_count = models.IntegerField(default=0, blank=True)
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hood', null=True)
    time_created = models.DateTimeField(auto_now_add=True , null=True)
    
           
    def __str__(self):
        return self.name  
    
    def save_neigborhood(self):
        self.save()      
    
    def create_neigborhood(self):
        self.create()    
        
    def update_neighborhood(self):
        self.update()

    def delete_neigborhood(self):
        self.delete()    
        
    def update_occupants(self):
        self.occupants += 1
        self.save()
                                
    @classmethod
    def find_neighborhood(cls,neigborhood_id):
        neighborhood = cls.objects.get(id = neigborhood_id)
        return neighborhood

    
# Post model     
class Post(models.Model):
    description = HTMLField(blank=True)
    post_image = models.ImageField(upload_to='images/', null=True,blank=True)
    time_created =  models.DateTimeField(auto_now=True, null =True)
    location=models.ForeignKey(Neighbourhood,  null =True)
    user = models.ForeignKey(User, null=True)
    user_profile = models.ForeignKey(Profile,  null =True)
    
    def __str__(self):
        return self.description       
    
# Business model     
class Business(models.Model):
    bsn_name = models.CharField(max_length=64, unique= True)
    bsn_user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    bsn_email = models.EmailField(max_length=64, unique= True) 
    location=models.ForeignKey(Neighbourhood, null=True) 
    bsn_description = HTMLField(blank=True)
    
    def __str__(self):
        return self.bsn_name  
    
    def save_business(self):
        self.save()    
        
    def update_business(self):
        self.update()

    def delete_business(self):
        self.delete()     
        
    def create_business(self):
        self.create()        
            
    @classmethod
    def find_business(cls,business_id):
        business = Business.objects.get(id = business_id)
        return business
         
    
# Comment model     
class Comment(models.Model):
    post = models.ForeignKey(Post, null=True)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment        
    
    def create_business(self):
        self.create()    
        
    def update_business(self):
        self.update()

    def delete_business(self):
        self.delete()    
        
    def find_business(self):
        self.find()      