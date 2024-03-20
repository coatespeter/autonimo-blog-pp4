from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin class for the About model with Summernote integration.
    The Summernote widget is applied to the 'content' field, providing
    a rich-text interface for editing HTML content.
    """
    summernote_fields = ('content',)

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin class for CollaborateRequest model.
    Customizes the admin interface for CollaborateRequest objects by
    displaying the 'message' and 'read' status in the admin list view.
    """
    list_display = ('message', 'read',)