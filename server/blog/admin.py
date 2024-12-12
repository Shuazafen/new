from django.contrib import admin
from .models import Blog, Comment, Category
from unfold.admin import ModelAdmin

# Register your models here.
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']
    

@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ['id','title', 'image', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ['id','blog', 'content', 'created_by', 'created_at']
    list_filter = ['blog']
    search_fields = ['content']