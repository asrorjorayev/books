from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image=models.ImageField(upload_to='image_user',default="")
    phone_num=models.CharField(max_length=13,null=True,blank=True)
