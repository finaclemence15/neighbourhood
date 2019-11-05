from django import forms
from . models import Comment, Business, Post,Neighbourhood, Profile,User

        
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']  
        
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['categories', 'time_created', 'location', 'user_profile']              
       
    