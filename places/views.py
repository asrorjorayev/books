from django.shortcuts import render,get_list_or_404
from django.views.generic import DetailView
from .models import*


def places_page(request):
    place=Places.objects.all()
    data={
        'places':place
    }
    return render(request,'places.html',context=data)

def haqida(request,id):
    place=get_list_or_404(Places,pk=id)
    
    data={
        'places':place
    }
    return render(request,'haqida.html',context=data)

 


