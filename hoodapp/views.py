from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Profile,User
from .forms import NewProfileForm
import datetime as dt

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    profile = Profile.objects.all()
    return render(request, 'index.html', {'profile':profile})

#  function to create profile

@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()
            return redirect('welcome')

    else:
        form = NewProfileForm()
    username=User.objects.all()    
    profiles = Profile.objects.filter(username = current_user)  
    
    return render(request, 'profile.html', {"form": form, "username": username,"profiles": profiles}) 

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user

    if request.method =='POST':
        
        if Profile.objects.filter(username_id=current_user).exists():
            form = NewProfileForm(request.POST,request.FILES,instance=Profile.objects.get(username_id = current_user))    
        else:
            form=NewProfileForm(request.POST,request.FILES)   
           
        if form.is_valid():
            profile=form.save(commit=False)
            profile.username=current_user
            profile.save()
            return redirect('profile', current_user.id)    
     
    else:
        if Profile.objects.filter(username_id = current_user).exists():
            form=NewProfileForm(instance =Profile.objects.get(username_id=current_user))
        else:
            form=NewProfileForm()     
            
    return render(request,'editProfile.html',{"form":form})   