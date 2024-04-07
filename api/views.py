from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from .serializers import PlaceSerializer,PlaceDetailSerializer,PlacesCommentSerializer
from rest_framework.response import Response
from places.models import Places,Comment

class PlacesApiViev(APIView):
    def get(self,request):
        places=Places.objects.all()
        serializer=PlaceSerializer(places,many=True)
        return  Response(data=serializer.data)
    
    def post(self,request):
        serializer=PlaceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        
    
class PlacesApiDetail(APIView):
    def get(self,request,id):
        place=Places.objects.get(id=id)
        serializer=PlaceDetailSerializer(place )
        
        return JsonResponse(data=serializer.data)


class CommentApiView(APIView):
    def get(self,request):
        comments=Comment.objects.all()
        serializer=PlacesCommentSerializer(comments,many=True)

        return JsonResponse(serializer.data,safe=False  )
    
    def post(self,request):
        serializer=PlacesCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




        



