from django.shortcuts import render

from .models import Post
from django.utils import timezone

from .forms import PostForm

from django.shortcuts import redirect

# Create your views here.


def home(request):
    return render(request,'home.html')

def post_list(request):
    ##me = User.objects.get(username='hejho')
    ##posts = Post.objects.filter(author=me).order_by('title')
    posts = Post.objects.filter(title__contains='cos').order_by('title')
    return render(request,'./post_list.html',{'posts':posts})

def post_detail(request,pk):
    Post.objects.get(pk=pk)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request,'post_edit.html',{'form':form})
    

def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'blog/post_edit.html',{'form':form})

