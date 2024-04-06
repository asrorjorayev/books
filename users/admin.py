from django.contrib import admin
from .models import User,FriendRequest

class UserAdmin(admin.ModelAdmin):
    list_display=('id','username','first_name','phone_num')
    list_display_links=('id','username')
    search_fields=('username','phone_num')

admin.site.register(User,UserAdmin)

class FriendrequestAdmin(admin.ModelAdmin):
    list_display=('id','from_user','to_user')
    list_display_links=('id','from_user')

admin.site.register(FriendRequest,FriendrequestAdmin)

