from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,LoginForm
# Create your views here.
class RegisterViev(View):
    def get(self,request):
        form=RegisterForm()
        return render(request,'users/register.html',context={"form":form})
    
    def post(self,request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('landing')

        return render(request,'users/register.html',context={"form":form})

class LoginViev(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'users/login_page.html',context={"form":form})
    
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:register')
        return render(request,'users/login_page.html',context={"form":form})
