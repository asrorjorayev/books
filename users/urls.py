from django.urls import path
from .views import RegisterViev,LoginViev,LogoutViev,ProfileViev
app_name='users'

urlpatterns=[
    path('register/',RegisterViev.as_view(),name='register'),
    path('login_page/', LoginViev.as_view(),name='login_page'),
    path('logout_page/', LogoutViev.as_view(),name='logout_page'),
    path('profile/', ProfileViev.as_view(),name='profile'),
    
]