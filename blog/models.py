"""
Creates an adventure first and then creates a destination,
destinations and adventures are linked together with the adventure id
so that destinations with the same adventure id
are shown at the same time on the destination page.
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Adventure(models.Model):
    """
    Adventure Model
    """
    name = models.CharField(max_length=50)
    date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_adventure")
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        """
        Order by date.
        """
        ordering = ['date']

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Post Model, connected to Adventure
    """
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE,
                                  related_name="posts")
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Order by created_on.
        """
        ordering = ["-created_on"]


class Comment(models.Model):
    """
    Comment Model, connected to Adventure
    """
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE,
                                  related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Order by created_on.
        """
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
