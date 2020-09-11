from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'body']

admin.site.register(Post, PostAdmin)
