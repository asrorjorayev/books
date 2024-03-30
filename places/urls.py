from django.urls import path
from .views import*
app_name='place'
urlpatterns=[
    path('places/',places_page,name='places_page'),
    path(' about/', about,name='about_web'),
    path('haqida/<int:id>',haqida,name='haqida_page'),
    path('Add_comment/<int:id>',AddCommentViev.as_view(),name='Add_comment'),
]