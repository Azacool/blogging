from django.contrib import admin
from .models import Post,Media

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['owner','text','image']
    list_filter = ['owner']
    ordering = ['owner']



    
