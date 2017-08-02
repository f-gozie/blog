from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.utils import timezone
from .forms import RegisterForm, LoginForm, CommentForm, PostForm
# Create your views here.

def index(request):
    posts = Post.objects.all().filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    recent_comments()
    recent_posts()
    context = {'posts':posts,'recent_comments':recent_comments,'recent_posts':recent_posts}
    return render(request, 'blog/index.html',context)

def detail(request, post_slug):
    try:
        post = Post.objects.get(slug=post_slug)
        comments = Comment.objects.filter(post=post)
    except Post.DoesNotExist:
        post = None
        comments = None
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        if request.user.is_authenticated():
            comment.commenter = request.user
            comment.email = request.user.email
            comment.created_on = timezone.now()
            comment.save()
        return redirect(request.path)
    else:
        print('girl')
    recent_comments()
    recent_posts()
    context = {'post':post,'form':form,'comments':comments,'recent_comments':recent_comments,'recent_posts':recent_posts}
    return render(request, 'blog/detail.html',context)

@login_required(login_url='/login/')
def post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return index(request)
        else:
            print(form.errors)
    return render(request, 'blog/post.html', {'form':form})

def edit_post(request, post_id):
    # form = get_object_or_404(Post, pk=post_id)
    instance = get_object_or_404(Post, pk=post_id)
    form = PostForm()
    if request.method == 'POST':
        form  = PostForm(request.POST or None, instance=instance)
        if form.is_valid():
            # form = get_object_or_404(Post, pk=post_id)
            form.save(commit=True)
            return detail(request, post.slug)
        else:
            print(form.errors)
    return render(request, 'blog/edit_post.html', {'form':form})


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return index(request)

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return detail(request,comment.post.slug)

def recent_comments():
    recent_comments = Comment.objects.all().filter(created_on__lte=timezone.now()).order_by('-created_on')[:4]
    return recent_comments

def recent_posts():
    recent_posts = Post.objects.all().filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:4]
    return recent_posts

def handle_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    form = LoginForm()
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')

    return render(request,'blog/login.html',{'form':form, 'error':error})

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    # if its a post request let the form send data
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.save()
            user.refresh_from_db() #load the newly created user instance
            user.save()
            rawpassword = form.cleaned_data.get('password1')
            user = authenticate(username = user.username, password=rawpassword)
            login(request,user)
            return HttpResponseRedirect(reverse('blog:index'))
    return render(request,'blog/register.html',{'form':form})

@login_required(login_url='/login/')
def handle_logout(request):
    logout(request)
    return redirect('blog:index')

def contact(request):
    return render(request, 'blog/contact.html', {})

def about(request):
    return render(request,'blog/about.html', {})
