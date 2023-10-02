from django.contrib import admin
from main.models import MyUser, Publications, Likes, Comments, View, Followers


admin.site.register(MyUser)
admin.site.register(Publications)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(View)
admin.site.register(Followers)
