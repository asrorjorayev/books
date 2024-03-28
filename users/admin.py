from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display=('id','username','first_name','phone_num')
    list_display_links=('id','username')
    search_fields=('username','phone_num')

admin.site.register(User,UserAdmin)

