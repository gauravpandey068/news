from django.contrib import admin
from .models import Category, Post, Topbar


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'trending', 'slideshow', 'created_at')
    search_fields = ['title', 'content']
    list_filter = ('status', 'trending', 'slideshow')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Topbar)
