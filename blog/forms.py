from django import forms
from .models import Comment, Post, Adventure


# The code for the datepicker is taken from
# https://stackoverflow.com/questions/3367091/whats
# -the-cleanest-simplest-to-get-running-datepicker-in-django
class DateInput(forms.DateInput):
    """
    I am using this to get a datepicker.
    """
    input_type = 'date'


class AdventureForm(forms.ModelForm):
    """
    Adventure form
    """
    class Meta:
        """
        Creating a datepicker.
        """
        model = Adventure
        fields = ('name', 'date', 'featured_image')
        widgets = {
            'date': DateInput(),
        }


class PostForm(forms.ModelForm):
    """
    Destination form.
    """
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image')


class CommentForm(forms.ModelForm):
    """
    Comment form
    """
    class Meta:
        model = Comment
        fields = ('body',)
