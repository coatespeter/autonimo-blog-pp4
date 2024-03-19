from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
        """
        Admin class for the Post model. It configures the list display, search fields, filters,
        slug prepopulation, and integrates Summernote for the content field in the Django Admin interface.
        """

        list_display = ('title', 'slug', 'status', 'created_on')
        search_fields = ['title', 'content']
        list_filter = ('status', 'created_on',)
        prepopulated_fields = {'slug': ('title',)}
        summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)