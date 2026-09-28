from django.contrib import admin

# forum/admin.py
from django.contrib import admin
from .models import Thread, Post

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_pinned')
    list_filter = ('is_pinned', 'created_at')
    search_fields = ('title', 'author__username')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('thread', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'author__username')
# Register your models here.
