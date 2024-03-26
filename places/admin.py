from django.contrib import admin
from .models import *
admin.site.register([PlacesOwner])

class OwnerAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email']
    search_fields=['first_name','last_name','email']

class PlaceAdmin(admin.ModelAdmin):
    list_display=['id','name','addres']
    search_fields=['name','addres']

class CommentAdmin(admin.ModelAdmin):
    list_display=['id','comment_text','user']
    search_fields=['comment_text','user','stars_given']
admin.site.register(Owner,OwnerAdmin)
admin.site.register(Places,PlaceAdmin)
admin.site.register(Comment,CommentAdmin)
