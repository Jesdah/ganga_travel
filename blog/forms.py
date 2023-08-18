from .models import Comment, Post, Adventure
from django import forms 


class AdventureForm(forms.ModelForm):
    class Meta:
        model = Adventure
        fields = ('name', 'date', 'featured_image')

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title', 'content', 'featured_image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)