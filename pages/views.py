from django.shortcuts import render,get_object_or_404
from .models import Page

# Create your views here.
def copyright(request):
    pages = Page.objects.filter(title="CopyRight")
    return render(request,'pages/copyright.html',{'pages':pages})

def faq(request):
    pages = Page.objects.filter(title="FAQ")
    return render(request,'pages/faq.html',{'pages':pages})

def privacy(request):
    pages = Page.objects.filter(title="Privacidad")
    return render(request,'pages/privacy.html',{'pages':pages})