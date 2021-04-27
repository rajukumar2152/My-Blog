# from django.contrib import admin
# from .models import Post ,BlogComment

# # Register your models here.
# # admin.site.register(Post)
# admin.site.register(BlogComment)


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     class Media:
#         js= ('tinyInject.js',)


from django.contrib import admin
from blog.models import Post, BlogComment

admin.site.register((BlogComment))
@admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)



        