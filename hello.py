from django.shortcuts import render,redirect,HttpResponse
from stuapp.emailbackend import emailbackend
from django.contrib.auth import authenticate,logout,login

from stuapp.models import CustomUser


from django.contrib.auth.decorators import login_required

from django.contrib import messages
def base(request):
    return render(request,'base.html') 


def loginn(request):
    return render(request,'login.html')

def dologin(request):
    
    if request.method == "POST":
       user = emailbackend.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'),)
       if user!=None:
           login(request,user)
           user_type = user.user_type
           if user_type == '1':
               return redirect('hodhome')
            # return HttpResponse('This is hod Panel')
           elif user_type == '2':
               return redirect('staffhome')
           elif user_type == '3':
               return redirect('studenthome')
           else:
               messages.error(request,'Email and Password Are Invalid !')
               return redirect('loginn')
       else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('loginn')
       
       
def dologout(request):
    logout(request)
    return redirect('loginn')


@login_required(login_url='/')
def profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    dict={
        'user':user,
    }
    
    return render(request,'profile.html')

@login_required(login_url='/')
  
def profileUpdate(request):
    if request.method=='POST':
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get ('password')
        
        
        try:
            user=CustomUser.objects.get(id=request.user.id)
            user.first_name=first_name
            user.last_name=last_name
            
            if password!=None and password!="":
                user.set_password(password)
            if profile_pic !=None and profile_pic != "":
                user.profile_pic = profile_pic
            user.save()   
            messages.success(request,"Updated successfully")
            return redirect('profile')
        except:
            messages.error(request,'error occured')
            
            
    return render(request,'profile.html')