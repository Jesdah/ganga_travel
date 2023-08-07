from django.contrib import admin
from .models import Post, Comment, Adventure
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Adventure)
class AdventureAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ['name', 'date']
    


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on',)
    search_fields = ('name', 'email', 'body')
