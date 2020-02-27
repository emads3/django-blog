from django.contrib import admin
# from .models import Forbidden_Words

from .models import Post,Comments,post_likes,Categories,Tag


admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(post_likes)
admin.site.register(Categories)

# Register your models here.

# admin.site.register(Forbidden_Words)