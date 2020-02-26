from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.utils import timezone 
from . models import PostLike
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'main/post_list.html', context)

def about(request):
    return render(request, 'main/about.html',{'title':'about'})

def home(request):
    return render(request, 'main/home.html', {'title':'home'})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/post_detail.html', {'post':post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'main/post_edit.html', {'form': form})
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user==post.author and request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False) 
            post.author = request.user
            post.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'main/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()
        return redirect('post-list')
    else:
        return redirect('post-detail', pk=post.pk)

@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    num_of_likes = PostLike.objects.filter(user=request.user, post=post).count()
    if num_of_likes > 0:
        already_like = PostLike.objects.get(post=post,user=request.user).delete()
    else:
        already_like = PostLike.objects.create(post=post,user=request.user)
    print(num_of_likes)
    return redirect("post-detail",pk=pk)



@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'main/comment_a_post.html', {'form': form})
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.user == request.user:
        comment.delete()
        return redirect('post-detail', pk=comment.post.pk)
    else:
        return redirect('post-detail', pk=pk)
