from .models import CollaborateRequest
from django import forms

class CollaborateForm(forms.ModelForm):
    """
    A Django form for creating CollaborateRequest entries.
    This ModelForm is linked to the CollaborateRequest model and includes
    fields for the user's name, email, and message. It simplifies the process
    of collecting collaboration inquiries from users.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')