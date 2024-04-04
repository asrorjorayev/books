from django.urls import path
from .views import RegisterViev,LoginViev,LogoutViev,ProfileVievUpdate,Profile_viev,ResetPassword
app_name='users'

urlpatterns=[
    path('register/',RegisterViev.as_view(),name='register'),
    path('login_page/', LoginViev.as_view(),name='login'),
    path('logout_page/', LogoutViev.as_view(),name='logout_page'),
    path('profile/', ProfileVievUpdate.as_view(),name='profile'),
    path('profile_viev/', Profile_viev.as_view(),name='profile_viev'),
    path('reset_page/', ResetPassword.as_view(),name='reset_page'),
    
]