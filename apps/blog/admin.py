from django.contrib import admin

from apps.blog.models import Blog, Category
from .models import BlogComment, BlogPost

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(BlogComment)
admin.site.register(BlogPost)
