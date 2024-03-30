 
from django.shortcuts import render,get_list_or_404,redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from places.forms import PlaceCommentView
from places.models import*
def  landing_page(request):
    place=Places.objects.all()
    form=PlaceCommentView()
    data={
        'places':place,
        'form':form
    }
    return render(request,'landing.html',context=data)
