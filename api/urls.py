from django.urls import path
from .views import*

app_name='api'

urlpatterns=[
    path('places-list/',PlacesApiViev.as_view(),name='places_view'),
    path('detail-list/<int:id>/',PlacesApiDetail.as_view(),name='detail_view'),
    path('comment-list/',CommentApiView.as_view(),name='comment_view'),
]