from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    """
    A Django form for creating or editing comments on blog posts.
    This form is linked to the Comment model and specifies that only the 'body'
    field of a comment is exposed for user input.
    """
    class Meta:
        model = Comment
        fields = ('body',)