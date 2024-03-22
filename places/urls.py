from django.urls import path
from .views import*
app_name='place'
urlpatterns=[
    path('places/',places_page,name='places_page'),
    path('haqida/<int:id>',haqida,name='haqida_page')
]