from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

from django.db import models
from cloudinary.models import CloudinaryField

class About(models.Model):
    """
    Model representing information about the website or organization, such as an 'About Us' section.
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        """
        String for representing the Model object in Admin site and elsewhere.
        """
        return self.title

class CollaborateRequest(models.Model):
    """
    Model for storing collaboration requests submitted via the website.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        """
        String for representing the Model object, making it easier to identify individual requests.
        """
        return f"Collaboration request from {self.name}"
