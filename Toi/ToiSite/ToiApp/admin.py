from django.contrib import admin
from .models import Post, UserProfile, Post_shared_with

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Post_shared_with)