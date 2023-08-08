from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



class Adventure(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date= models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_adventure")
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering=['date']

    def __str__(self):
        return self.name



class Post(models.Model):
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE,related_name="posts")
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blogpost_like', blank=True)


    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"