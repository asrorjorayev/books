from rest_framework import serializers
from places.models import*
from django.utils import timezone

class PlaceSerializer(serializers.Serializer):
    name=serializers.CharField()
    discription=serializers.CharField()
    addres=serializers.CharField()
    image=serializers.ImageField()

    def validate(self, data):
        name=data.get('name')

        if len(name)<4 or len(name)>30:
            result={
                "messege":"name uzunligi 4 dan uzun 30 dan qisqa bolishi kerak"
            }
            raise serializers.ValidationError(result)
        
        addres=data.get('addres')
        if addres.isalpha():
            result={
                "messege":" manzlni kiritishda raqamlar ham kiriting"
            }
            raise serializers.ValidationError(result)
        
        return data
    def create(self, validated_data):
        name=validated_data.get('name')
        discription=validated_data.get('discription')
        addres=validated_data.get('addres')
        image=validated_data.get('image')
        Places.objects.create(
            name=name,
            discription=discription,
            addres=addres,
            image=image 
        )

        return validated_data

#Place Detail Serializer
class PlaceDetailSerializer(serializers.Serializer):
    name=serializers.CharField()
    discription=serializers.CharField()
    image=serializers.ImageField()

# Comment Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'image']

class PlaceSerializerView(serializers.ModelSerializer):
    class Meta:
        model=Places
        fields=['id','name','image']



class PlacesCommentSerializer(serializers.Serializer):
    comment_text=serializers.CharField()
    stars_given=serializers.IntegerField()
    created_at=serializers.DateField(default=timezone.now)
    user=UserSerializer()
    place=PlaceSerializerView()

    def validate(self, data):
        stars_given=data.get('stars_given')
        if stars_given>5 and stars_given<0:
            result={
                "messege":" siz 5 tagacha yulduz bera olasiz"
            }
            raise serializers.ValidationError(result)
        
        return data
    
    def create(self, validated_data):
        comment_text=validated_data.get("comment_text")
        stars_given=validated_data.get("stars_given")
        Comment.objects.create(
            comment_text=comment_text,
            stars_given=stars_given
        )
        return validated_data
        

        
