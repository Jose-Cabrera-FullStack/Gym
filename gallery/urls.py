from django.urls import path
from . import views

urlpatterns = [
    #path del gallery
    path('', views.gallery, name="gallery"),
]