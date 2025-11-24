from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'created_date', 'status']
    search_fields = ['title', 'content']
    list_filter = ['status', 'created_date', 'published_date', 'author']
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'published_date'
    ordering = ['status', 'published_date']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_date', 'approved']
    list_filter = ['approved', 'created_date']
    search_fields = ['author__username', 'content']
    actions = ['approve_comments']

    def approve_comments(self,  query, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"