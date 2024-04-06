from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image=models.ImageField(upload_to='image_user',default="")
    phone_num=models.CharField(max_length=13,null=True,blank=True)
    friends=models.ManyToManyField('users.User', blank=True)


class FriendRequest(models.Model):
    from_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='from_user')
    to_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user')
    is_accepted=models.BooleanField(default=False)
