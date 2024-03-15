from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):

    CATEGORY_CHOICES = [
        ('transportation', 'Transportation'),
        ('land_management', 'Land Management'),
        ('swimming_pool_management', 'Swimming Pool Management'),
        ('handyman', 'Handyman'),
    ]

    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=[(0, "Draft"), (1, "Publish")])
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} | written by {self.author}"
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
    

