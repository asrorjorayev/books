from typing import Any
from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        self.fields['password_confirm']=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']


    def clean_password_confirm(self):
        password=self.cleaned_data['password']
        password_confirm=self.cleaned_data['password_confirm']

        if password!=password_confirm:
            raise forms.ValidationError('Parolni tekshiring va bir xil kiriting')
        
        return password
    
    def clean_username(self):
        username=self.cleaned_data['username']

        if len(username)<4 or len(username)>30:
            raise forms.ValidationError('username uzunligi 5 dan katta 30 dan kichik bolishi kerakl')
        return username

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username=self.cleaned_data['username']
        if not isinstance(username,str):
            raise forms.ValidationError('usernameni stringda kiriting')
        if len(username)<5 or len(username)>30:
            raise forms.ValidationError('username uzunligi 5 dan katta 30 dan kichik bolishi kerakl')
        return username
    
    def clean_password(self):
        password=self.cleaned_data['password']
        if not password.isdigit():
            raise forms.ValidationError('passwordni raqamda kiriting ')
        return password
    
class ProfileUpdateViev(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']