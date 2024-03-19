from django.apps import AppConfig


class PostsConfig(AppConfig):
    """
    Configuration class for the 'posts' application.
    This class is used by Django to configure aspects of the 'posts' app,
    such as specifying the default auto field type for model IDs.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
