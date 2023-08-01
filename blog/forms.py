from .models import Comment, Post, Adventure
from django import forms


class AdventureForm(forms.ModelForm):
    class Meta:
        model = Adventure
        fields = ('name', 'date',)

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)