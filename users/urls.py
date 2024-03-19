from django.urls import path
from .views import RegisterViev,LoginViev
app_name='users'

urlpatterns=[
    path('register/',RegisterViev.as_view(),name='register'),
    path('login_page/', LoginViev.as_view(),name='login_page'),
    
]