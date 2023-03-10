from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # Good for data whose length is known
    title = models.CharField(max_length=128)
    # Good for data whose length is unknown
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Auto-sets the value to the current time upon record creation
    created_date = models.DateTimeField(auto_now_add=True)
    # Auto-sets the value to the time of modification
    modified_date = models.DateTimeField(auto_now=True)
    # Allows the field to contain null-values, which signifies that the post is yet to be published
    published_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name='categories')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"
