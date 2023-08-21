from .models import Comment, Post, Adventure
from django import forms 

# The code for the datepicker is taken from
# https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django
class DateInput(forms.DateInput):
    input_type = 'date'

class AdventureForm(forms.ModelForm):
    class Meta:
        model = Adventure
        fields = ('name', 'date', 'featured_image')
        widgets= {
            'date': DateInput(),
        }
class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title', 'content', 'featured_image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)