from django.contrib import admin
from .models import Post, Follow, Comment, directMessage

# Register your models here.
admin.site.register((Post , Follow, Comment, directMessage ))
