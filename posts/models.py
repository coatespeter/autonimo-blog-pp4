from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    Model representing a blog post. Each post has a title, category, slug, featured image,
    author, excerpt, content, creation date, status, and update date. The 'category' field
    allows for categorization of posts into predefined choices. The 'status' field indicates
    whether the post is a draft or published.
    """

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
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
        )
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=[(0, "Draft"), (1, "Publish")])
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} | written by {self.author}"

class Comment(models.Model):
    
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
        )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    """
    Model representing a comment made on a blog post. Comments are linked to both the blog post
    they belong to ('post') and the author ('author') who made the comment.
    """
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
