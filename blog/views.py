"""
Creates an adventure first and then creates a destination,
destinations and adventures are linked together with the adventure id
so that destinations with the same adventure id
are shown at the same time on the destination page.
"""
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Post, Adventure, User, Comment
from .forms import CommentForm, AdventureForm, PostForm


class AdventureList(generic.ListView):
    """
    Renders The adventures on adventure page.

    """
    model = Adventure
    queryset = Adventure.objects.filter().order_by("date")
    template_name = "index.html"


class AdventureDetail(View):
    """
    Class for add post and get post
    """

    def get(self, request, adventure_id, *args, **kwargs):
        """
        Redners Destinations on destination page.
        When a Destination is created this function connects
        the destination with adventure_id.
        """
        queryset = Adventure.objects.filter()
        adventure = get_object_or_404(queryset, id=adventure_id)
        posts = adventure.posts.filter().order_by('created_on')
        comments = adventure.comments.filter().order_by('created_on')
        return render(
            request,
            'post.html', {
                'adventure': adventure,
                'posts': posts,
                'comments': comments,
                'post_form': PostForm(),
                'comment_form': CommentForm(),
            }
        )

    def post(self, request, adventure_id, author_id, *args, **kwargs):
        """
        Creates a destination and connects it with adventure_id
        """
        queryset = Adventure.objects.filter()
        adventure = get_object_or_404(queryset, id=adventure_id)
        posts = adventure.posts.filter().order_by('created_on')
        comments = adventure.comments.filter().order_by('created_on')
        post = Post.adventure
        post_form = PostForm(request.POST, request.FILES)
        user = get_object_or_404(User, pk=author_id)
        if user.has_perm('blog.add_post'):
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.adventure = adventure
                post.save()
                messages.success(request, 'New Destination created')
                return HttpResponseRedirect(reverse('adventure_detail',
                                            args=[adventure_id, author_id]))
            else:
                messages.error(request, 'Something went wrong!')
            return render(
                request,
                'post.html', {
                    'adventure': adventure,
                    'posts': posts,
                    'comments': comments,
                    'post_form': PostForm(),
                    'comment_form': CommentForm()
                }
            )
        else:
            return HttpResponse('You do not have permission to add Posts')


def delete_post(request, adventure_id, post_id, author_id):
    """
    Checks if the user has permission and then lets the user to delete data.
    """
    post = get_object_or_404(Post, id=post_id)
    user = get_object_or_404(User, pk=author_id)
    if user.has_perm('blog.delete_post'):
        post.delete()
        messages.info(request, 'Destination deleted')
        return HttpResponseRedirect(reverse('adventure_detail',
                                    args=[adventure_id, author_id]))
    else:
        return HttpResponse('You do not have permission to delete Posts')


def edit_post(request, adventure_id, author_id, post_id):
    """
    Render Edit_post.html, checks if the user has permission,
    allows the user to change data.
    """
    post = get_object_or_404(Post, id=post_id)
    user = get_object_or_404(User, pk=author_id)
    if user.has_perm('blog.change_post'):
        if request.method == 'POST':
            post_form = PostForm(request.POST, request.FILES, instance=post)
            if post_form.is_valid():
                post_form.save()
                messages.info(request, 'Destination changed')
                return HttpResponseRedirect(reverse('adventure_detail',
                                            args=[adventure_id, author_id]))
            else:
                messages.error(request, 'Something went wrong!')
        post_form = PostForm(instance=post)
        return render(
            request,
            'edit_post.html', {
                'edit_form': post_form,
            }
        )
    else:
        return HttpResponse('You do not have permission to edit Posts')


def add_comment(request, adventure_id, author_id):
    """
    Checks if the user has permission and lets the user to add comment.
    """
    queryset = Adventure.objects.filter()
    adventure = get_object_or_404(queryset, id=adventure_id)
    posts = adventure.posts.filter().order_by('created_on')
    comments = adventure.comments.filter().order_by('created_on')
    comment = Comment.adventure
    user = get_object_or_404(User, pk=author_id)
    if user.has_perm('blog.add_comment'):
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.name = request.user.username
            comment.adventure = adventure
            comment.save()
            return HttpResponseRedirect(reverse('adventure_detail',
                                        args=[adventure_id, author_id]))
        else:
            comment_form = CommentForm()
        return render(
            request,
            'add_comment.html', {
                'adventure': adventure,
                'posts': posts,
                'comments': comments,
                'post_form': PostForm(),
                'comment_form': CommentForm()
            }
        )
    else:
        return HttpResponse('You do not have permission to comment')


def delete_comment(request, adventure_id, comment_id, author_id):
    """
    Checks if the user is the author of the comment
    and then lets the user delete comment.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.name == request.user.username:
        comment.delete()
        return HttpResponseRedirect(reverse('adventure_detail',
                                    args=[adventure_id, author_id]))
    else:
        return HttpResponse(
            'You do not have permission to delete this Comment')


def add_adventure(request, author_id):
    """
    Checks if the user has permission and then lets the user to add adventure.
    """
    queryset = User.objects.filter()
    current_user = get_object_or_404(queryset, id=author_id)
    user = get_object_or_404(User, pk=author_id)
    if user.has_perm('blog.add_adventure'):

        if request.method == 'POST':
            adventure_form = AdventureForm(request.POST, request.FILES)
            adventure_user = Adventure.author
            if adventure_form.is_valid():
                adventure_user = adventure_form.save(commit=False)
                adventure_user.author = current_user
                adventure_form.save()
                messages.success(request, 'New adventure created')
            else:
                messages.error(request, 'Something went wrong!')
            return redirect('home')
        return render(
                request,
                'add_adventure.html', {
                    'adventure_form': AdventureForm()
                }
            )
    else:
        return HttpResponse('You do not have permission to add Adventure')


def edit_adventure(request, adventure_id, author_id):
    """
    Checks if the user has permission and then lets the user to edit adventure.
    """
    adventure = get_object_or_404(Adventure, id=adventure_id)
    user = get_object_or_404(User, pk=author_id)
    if user.has_perm('blog.change_adventure'):
        if request.method == 'POST':
            form = AdventureForm(request.POST, request.FILES,
                                 instance=adventure)
            if form.is_valid():
                form.save()
                messages.info(request, 'Adventure changed')
            else:
                messages.error(request, 'Something went wrong!')
            return redirect('home')
        form = AdventureForm(instance=adventure)
        context = {
            'form': form
        }
        return render(request, 'edit_adventure.html', context)
    else:
        return HttpResponse('You do not have permission to edit Adventure')


def delete_adventure(request, adventure_id, author_id):
    """
    Checks if the user has permission and the lets the user to delete comment.
    """
    adventure = get_object_or_404(Adventure, id=adventure_id)
    user = get_object_or_404(User, pk=author_id)
    if user.has_perm('blog.delete_adventure'):
        adventure.delete()
        messages.info(request, 'Adventure deleted')
        return redirect('home')
    else:
        return HttpResponse('You do not have permission to delete Adventure')
