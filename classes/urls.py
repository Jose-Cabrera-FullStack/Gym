from django.urls import path
from . import views

urlpatterns = [
    #path del classes
    path('', views.classes, name="classes"),

]