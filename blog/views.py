from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,4)
    page = request.GET.get('page')

    post = paginator.get_page(page)

    return render(request,"blog/blog.html",{"posts":posts,"post":post})

def category(request,category_id):
    category = get_object_or_404(Category,id=category_id)
    posts = Post.objects.filter(categories=category)
    paginator = Paginator(posts,4)
    page = request.GET.get('page')

    post = paginator.get_page(page)

    return render(request,"blog/category.html",{"category":category,'posts':posts,"post":post})

def post(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    posts = Post.objects.filter(id=post_id)
    todos = Post.objects.all()
    return render(request,"blog/post.html",{"post":post,"posts":posts,"todos":todos})