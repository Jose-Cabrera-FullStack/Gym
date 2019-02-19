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

def classes(request):
    return render(request,"core/classes.html")

def blog(request):
    return render(request,"core/blog.html")

def gallery(request):
    return render(request,"core/gallery.html")
    
def contact_us(request):
    return render(request,"core/contact-us.html")
