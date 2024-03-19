from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

class PostList(generic.ListView):
    """
    A view that inherits from Django's generic ListView to display a list of published posts.
    It uses a specific queryset to filter posts by their 'status' to show only published posts.
    The view paginates the posts to show a limited number per page.
    """
    queryset = Post.objects.filter(status=1)
    template_name = "posts/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    View function for displaying the detail of a single post, identified by its 'slug'.
    It includes displaying approved comments associated with the post and a form for submitting new comments.
    Submitted comments are saved with the status awaiting approval.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    comment_form = CommentForm()  # Initialize comment_form here
    
    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        print("About to render template")
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    return render(
        request,
        "posts/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

def comment_edit(request, slug, comment_id):
    """
    View function to edit an existing comment. It checks if the comment author is the same as the request user.
    If valid, the comment is updated and set as unapproved. An error message is displayed if the update is invalid.
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    View function to delete a comment. It verifies that the comment author is the request user before deletion.
    Success or error messages are displayed based on whether the user has permission to delete the comment.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
