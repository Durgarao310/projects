from django.shortcuts import render,redirect,get_object_or_404
from . models import Post,PostLike,Comment
from . forms import PostForm,CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render (request, 'main/post_list.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'main/post_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class UserPostListView(ListView):
    model = Post
    template_name = 'main/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('/',pk=post.pk)
    else:
        form = PostForm()
    return render(request,'main/post_edit.html',{'form':form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('post-detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'main/post_edit.html',{'form':form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()
        return redirect('home')
    else: 
        return redirect("post-detail", pk=post.pk)
    

def post_detail(request, pk):
    post =get_object_or_404(Post, pk=pk)
    return render(request, 'main/post_detail.html',{'post':post})

@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    num_of_likes = PostLike.objects.filter(user=request.user, post=post).count()
    if num_of_likes > 0:
        already_like = PostLike.objects.get(post=post,user=request.user).delete()
    else:
        already_like = PostLike.objects.create(post=post,user=request.user)
    return redirect("/",pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'main/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post-detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post-detail', pk=comment.post.pk)

@login_required
def comment_edit(request, pk):                        
    comment = get_object_or_404(Comment, pk=pk)
    if request.method=="POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request,'main/add_comment_to_post.html',{'form':form})

