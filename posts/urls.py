from . import views
from django.urls import path, include

from django.urls import path
from . import views

urlpatterns = [
    # Home page, lists posts
    path("", views.PostList.as_view(), name='home'),
    
    # Detail view for a single post identified by its slug
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    
    # URL for editing an existing comment on a post, identified by post's slug and comment's ID
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    
    # URL for deleting an existing comment from a post, identified by post's slug and comment's ID
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]
