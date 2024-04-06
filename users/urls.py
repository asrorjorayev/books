from django.urls import path
from .views import *
app_name='users'

urlpatterns=[
    path('register/',RegisterViev.as_view(),name='register'),
    path('login_page/', LoginViev.as_view(),name='login'),
    path('logout_page/', LogoutViev.as_view(),name='logout_page'),
    path('profile/', ProfileVievUpdate.as_view(),name='profile'),
    path('profile_viev/', Profile_viev.as_view(),name='profile_viev'),
    path('reset_page/', ResetPassword.as_view(),name='reset_page'),
    path('user_page/',  UserView.as_view(),name='user_page'),



    #users so'rov yuborish
    path('send-request/<int:id>/',  FriendRequestView.as_view(),name='send_request'),
    path('networks-page/',  MyNetworks.as_view(),name='networks_page'),
    path('accept-friend/<int:id>/',  AcceptFriendRequestView.as_view(),name='accept'),
    path('ignore-friend/<int:id>/',  IgnoreFriendView.as_view(),name='ignore'),
    path('delete-friend/<int:id>/',  DeleteFriendView.as_view(),name='delete_friend'),
    
]