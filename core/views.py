from django.shortcuts import render

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
    return render(request,"core/home.html")

def about_us(request):
    return render(request,"core/about-us.html")

def trainers(request):
    return render(request,"core/trainers.html")

def gallery(request):
    return render(request,"core/gallery.html")
    

