from django.shortcuts import render
from blog.models import Post

# Create your views here.
"""
-home
-about us
-trainers
-classes
-blog
-gallery
-contact us
"""

def home(request):
    posts = Post.objects.filter(published=True).order_by('-created')[0:3]
    return render(request,"core/home.html",{"posts":posts})

def about_us(request):
    return render(request,"core/about-us.html")

