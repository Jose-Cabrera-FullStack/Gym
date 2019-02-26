from django.shortcuts import render, get_object_or_404
from .models import Class

# Create your views here.
def classes(request):
    classes= Class.objects.all()
    return render(request,"classes/classes.html",{'classes':classes})

def clase(request,class_id):
    clase = get_object_or_404(Class,id=class_id)
    classes = Class.objects.filter(id=class_id)
    return render(request,"classes/class.html",{'clase':clase,"classes":classes})