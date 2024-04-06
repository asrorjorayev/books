 
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from places.forms import PlaceCommentView
from places.models import*
from users.models import FriendRequest,User


def  landing_page(request):
    place=Places.objects.all()
    form=PlaceCommentView()
    data={
        'places':place,
        'form':form
    }
    return render(request,'landing.html',context=data)

class HomeView(LoginRequiredMixin,View):
    def get(self,request):
         
        place_reviews = Comment.objects.filter(user__in=request.user.friends.all()).order_by('-created_at')
        
        return render(request,'home.html',{"place_reviews":place_reviews})
