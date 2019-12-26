from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def debug_test(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:20]
    return render(request, 'blog/test.html', {'posts': posts})

def page_non(request):
    return render(request, 'blog/page_non.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:20]
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:20]
    return render(request, 'blog/post_edit.html', {'form': form, 'posts': posts})

def tips_kitei(request):
    return render(request, 'blog/tips_kitei.html')
