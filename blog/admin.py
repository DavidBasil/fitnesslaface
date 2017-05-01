from django.contrib import admin
from .models import Post, Comment, Tag


class PostAdmin(admin.ModelAdmin):
    """Modifies the display of blog posts in admin section"""
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'publish', 'author')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)} # when adding new post
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


class CommentAdmin(admin.ModelAdmin):
    """Modifies the display of post comments in admin section"""
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email')


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
