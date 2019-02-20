from django.shortcuts import render
from .models import Class

# Create your views here.
def classes(request):
    classes= Class.objects.all()
    return render(request,"classes/classes.html",{'classes':classes})