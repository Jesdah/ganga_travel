from django.shortcuts import render, get_object_or_404, reverse,  redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Adventure
from .forms import CommentForm, AdventureForm, PostForm



# class AdventureList(Adventure):
#     model = Adventure
#     queryset = Adventure.objects.order_by("date")
#     template_name = "index.html"
#     paginate_by = 6


def get_adventure_list(request):

    adventures = Adventure.objects.all()
    context= {
        'adventures': adventures
    }
    return render(request, 'index.html', context)


def add_adventure(request):
    if request.method == 'POST':
        form= AdventureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_adventure_list')
    form= AdventureForm()
    context= {
        'form': form
    }
    return render(request,'add_adventure.html', context)


def edit_adventure(request, adventure_id):
    adventure= get_object_or_404(Adventure, id=adventure_id)
    if request.method=='POST':
        form= AdventureForm(request.POST, instance=adventure)
        if form.is_valid():
            form.save()
            return redirect('get_adventure_list')
    form=AdventureForm(instance=adventure)
    context= {
        'form': form
    }
    return render(request,'edit_adventure.html', context)


def delete_adventure(request, adventure_id):
    adventure= get_object_or_404(Adventure, id=adventure_id)
    adventure.delete()
    return redirect('get_adventure_list')

# class PostList(generic.ListView):
#     model = Post
#     queryset = Post.objects.order_by("created_on")
#     template_name = "edit_adventure.html"
#     paginate_by = 6

def get_post_list(request, adventure_id):

    posts = Post.objects.all()
    context= {
        'posts': posts
    }
    return render(request, 'post.html', context)


def add_post(request):
    if request.method == 'POST':
        post_form= PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('get_post_list')
    post_form= PostForm()
    context= {
        'post_form': post_form
    }
    return render(request, 'add_post.html', context)


def edit_post(request, post_id):
    post= get_object_or_404(Post, id=post_id)
    if request.method=='POST':
        post_form= PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('get_post_list')
    post_form=PostForm(instance=post)
    context= {
        'post_form': post_form
    }
    return render(request,'edit_post.html', context)


def delete_post(request, post_id):
    post= get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('get_post_list')



# def get(request, adventure_id):

#     adventure = get_object_or_404(Adventure, id=adventure_id)
#     post = adventure.post.order_by("-created_on")
#     liked = False
#     if post.likes.filter(id=request.user.id).exists():
#         liked = True

#     return render(
#         request,
#         "post.html",
#         {
#             "adventure": adventure,
#             "post": post,
#             "liked": liked,
#         },
#     )

# def post(request, adventure_id):

    
#     adventure = get_object_or_404(Adventure, id=adventure_id)
#     post = adventure.post.order_by("-created_on")
#     liked = False
#     if post.likes.filter(id=request.user.id).exists():
#         liked = True

#     post_form = PostForm(data=request.POST)
#     if post_form.is_valid():
#         post_form.instance.email = request.user.email
#         post_form.instance.name = request.user.username
#         post = post_form.save(commit=False)
#         post.adventure = post
#         post.save()
#     else:
#         post_form = PostForm()

#     return render(
#         request,
#         "post.html",
#         {
#             "adventure": adventure,
#             "post": post,
#             "liked": liked
#         },
#     )


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# Create your views here.
