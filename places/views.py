from django.shortcuts import render,get_list_or_404,redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PlaceCommentView
from .models import*

def about(request):
    return render(request,'about.html')

def places_page(request):
    place=Places.objects.all()
    query_search=request.GET.get("q","")
    if query_search:
        place=place.filter(name__icontains=query_search)
    return render(request,'places.html',context={'places':place})

def haqida(request,id):
    place=get_list_or_404(Places,pk=id)
    form=PlaceCommentView()
    data={
        'places':place,
        'form':form
    }
    return render(request,'haqida.html',context=data)

class AddCommentViev(LoginRequiredMixin,View):
    def post(self,request,id):
        place=Places.objects.get(id=id)
        form=PlaceCommentView(request.POST)

        if form.is_valid():
           comment= Comment.objects.create(
                user=request.user,
                place=place,
                comment_text=form.cleaned_data['comment_text'],
                stars_given=form.cleaned_data['stars_given']
            )
        return redirect(reverse("place:haqida_page",kwargs={"id":place.id}))
