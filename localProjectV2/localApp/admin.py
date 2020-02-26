from django.contrib import admin
from .models import Posts,Comments,Users,Post_Likes_Dislikes

admin.site.register(Users)
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Post_Likes_Dislikes)