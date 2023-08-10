from django.shortcuts import render, get_object_or_404, reverse,  redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Adventure, User, Comment
from .forms import CommentForm, AdventureForm, PostForm



class AdventureList(generic.ListView):
    model = Adventure
    queryset = Adventure.objects.filter().order_by("date")
    template_name = "index.html"
    paginate_by = 6


class AdventureDetail(View):

    def get(self, request, adventure_id, *args, **kwargs):
        queryset=Adventure.objects.filter()
        adventure= get_object_or_404(queryset, id=adventure_id)
        posts = adventure.posts.filter().order_by('created_on')
        comments = adventure.comments.filter().order_by('created_on')
        return render(
            request,
            'post.html',{
                'adventure': adventure,
                'posts':posts,
                'comments':comments,
                'post_form':PostForm(),
                'comment_form':CommentForm()
            }
        )
    


    def post(self, request, adventure_id, *args, **kwargs):
        queryset=Adventure.objects.filter()
        adventure= get_object_or_404(queryset, id = adventure_id)
        post = adventure.posts.filter().order_by('created_on')
        post= Post.adventure
        post_form=PostForm(data=request.POST)
        if post_form.is_valid():
            post=post_form.save(commit=False)
            post.adventure= adventure
            post.save()
            return HttpResponseRedirect(reverse('adventure_detail', args=[adventure_id]))
        else:
            post_form = PostForm()
        # return HttpResponseRedirect(reverse('adventure_detail', args=[adventure_id]))
        return render(
            request,
            'post.html',{
                'adventure': adventure,
                'post_form':PostForm(),
                'comment_form':CommentForm()
            }
        )


def add_comment(request, adventure_id, *args, **kwargs):
    queryset=Adventure.objects.filter()
    adventure= get_object_or_404(queryset, id = adventure_id)
    comments = adventure.comments.filter().order_by('created_on')
    comment_form=CommentForm(data=request.POST)
    if comment_form.is_valid():
        
        comment= comment_form.save(commit=False)
        comment.name = request.user.username
        comment.adventure= adventure
        comment.save()
        return HttpResponseRedirect(reverse('adventure_detail', args=[adventure_id]))
    else:
        comment_form = CommentForm()
    
    return render(
        request,
        'add_comment.html',{
            'adventure': adventure,
            'comments':comments,
            'post_form':PostForm(),
            'comment_form':CommentForm()
        }
    )



def add_adventure(request, author_id):
    queryset=User.objects.filter()
    current_user = get_object_or_404(queryset,id=author_id)
    if request.method == 'POST':
        adventure_form= AdventureForm(request.POST)
        adventure_user = Adventure.author
        if adventure_form.is_valid():
            
            adventure_user=adventure_form.save(commit=False)
            adventure_user.author= current_user
            adventure_user.save()
            return redirect('home')
    return render(
            request,
            'add_adventure.html',{
                'adventure_form': AdventureForm()
            }
        )


def edit_adventure(request, adventure_id):
    adventure= get_object_or_404(Adventure, id=adventure_id)
    if request.method=='POST':
        form= AdventureForm(request.POST, instance=adventure)
        if form.is_valid():
            form.save()
            return redirect('home')
    form=AdventureForm(instance=adventure)
    context= {
        'form': form
    }
    return render(request,'edit_adventure.html', context)


def delete_adventure(request, adventure_id):
    adventure= get_object_or_404(Adventure, id=adventure_id)
    adventure.delete()
    return redirect('home')


def edit_post(request, post_id):
    post= get_object_or_404(Post, id=post_id)
    if request.method=='POST':
        post_form= PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    post_form=PostForm(instance=post)
    context= {
        'post_form': post_form
    }
    return render(request,'edit_post.html', context)


def delete_post(request, post_id):
    post= get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('home')




