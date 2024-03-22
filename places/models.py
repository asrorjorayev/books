from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

class Places(models.Model):
    name=models.CharField(max_length=255)
    discription=models.TextField()
    addres=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Owner(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    bio=models.TextField()

    
    def __str__(self):
        return self.first_name
    
class PlacesOwner(models.Model):
    place=models.ForeignKey(Places,on_delete=models.CASCADE)
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.place}ning asoschisi {self.owner}"

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    place=models.ForeignKey(Places,on_delete=models.CASCADE)
    comment_text=models.TextField
    stars_given=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)]) 
    def __str__(self):
        return f"{self.user} comment to {self.place} and give {self.stars_given} stars"