from django.contrib import admin
# Register your models here.
from .models import Comment, Post, LatLong

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(LatLong)