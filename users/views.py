from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm,LoginForm,ProfileUpdateViev
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import check_password
from .forms import ResetPasswordViev
from .models import *
# Create your views here.
class RegisterViev(View):
    def get(self,request):
        form=RegisterForm()
        return render(request,'users/register.html',context={"form":form})
    
    def post(self,request):
        form=RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,"Siz muvaffaqiyatli registratsiya qildingiz ")
            return redirect('landing')

        return render(request,'users/register.html',context={"form":form})

class LoginViev(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'users/login_page.html',context={"form":form})
    
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
             username=form.cleaned_data['username']
             password=form.cleaned_data['password']
             user=authenticate(username=username,password=password)
             if user is not None:
                 login(request,user)
                 messages.success(request,"Siz muvaffaqiyatli login qildingiz ")
                 return redirect('landing')
        return render(request,'users/login_page.html',context={"form":form})
    
class LogoutViev(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,"Siz muvaffaqiyatli logout qildingiz ")
        return redirect('landing')
    

class ProfileVievUpdate(LoginRequiredMixin,View):
    def get(self,request):
        form=ProfileUpdateViev(instance=request.user)
        return render(request,'users/profile.html',context={"form":form})

    def post(self,request):
        form=ProfileUpdateViev(instance=request.user,data=request.POST,files=request.FILES)

        if form.is_valid():
            form.save()
            messages.info(request,"Siz muvaffaqiyatli yangilanish qildingiz ")
            return redirect('users:profile_viev')
        return render(request,'users/profile.html',context={"form":form})

class Profile_viev(LoginRequiredMixin,View):
    def get(self,request):

        return render(request,'users/profile_viev.html')

class ResetPassword(LoginRequiredMixin,View):
    def get(self,request):
        form=ResetPasswordViev()
        return render(request,'users/reset_password.html',context={"form":form})
    
    def post(self,request):
        user=request.user
        form=ResetPasswordViev(request.POST)
        if form.is_valid():
            if check_parol(user,form.cleaned_data['old_password']):
                user.set_password(form.cleaned_data['confirm_password'])
                user.save()
                return redirect('users:profile_viev')
            else:
                return render(request,'users/reset_password.html',context={"form":form})
    
        return render(request,'users/reset_password.html',context={"form":form})

def check_parol(user,password):
    return user.check_password(password)

class UserView(LoginRequiredMixin,View):
    def get(self,request):
        users=User.objects.exclude(username=request.user.username)
        friend_request=User.objects.filter(id__in=FriendRequest.objects.filter(from_user=request.user).values_list('to_user'))

        return render(request,'users/users_page.html',{"users":users,"friend_request":friend_request})
    
class MyNetworks(LoginRequiredMixin,View):
    def get(self,request):
        networks=FriendRequest.objects.filter(to_user=request.user,is_accepted=False)
        return render(request,'networks.html',{"networks":networks})
    

    
class FriendRequestView(LoginRequiredMixin,View):
    def get(self,request,id):
        to_user=User.objects.get(id=id)
        from_user=request.user
        FriendRequest.objects.get_or_create(from_user=from_user,to_user=to_user)

        return redirect('users:user_page')
    
class AcceptFriendRequestView(LoginRequiredMixin,View):
    def get(self,request,id):
        friend_rquest=FriendRequest.objects.get(id=id)
        from_user=friend_rquest.from_user

        main_user=request.user
        main_user.friends.add(from_user)

        return redirect('users:networks_page')

class IgnoreFriendView(LoginRequiredMixin,View):
    def get(self,request,id):
        friend_request=FriendRequest.objects.get(id=id)
        friend_request.delete()
        return redirect('users:networks_page')
    
class DeleteFriendView(LoginRequiredMixin,View):
    def get(self,request,id):
        friend=User.objects.get(id=id)
        user=request.user
        user.friends.remove(friend)
        return redirect('users:networks_page')

    