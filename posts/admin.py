from django.contrib import admin
from .models import Post, Post_Attachments
# Register your models here.
admin.site.register(Post)
admin.site.register(Post_Attachments)