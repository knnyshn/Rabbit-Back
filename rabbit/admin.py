from django.contrib import admin
from .models import Burrow, Post, Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Burrow)
admin.site.register(Comment)
