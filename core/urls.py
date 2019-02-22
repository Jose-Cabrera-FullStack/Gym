from django.urls import path
from . import views

urlpatterns = [

    #path del core
    path('', views.home, name="home"),
    path('about-us/', views.about_us, name="about-us"),
    path('trainers/', views.trainers, name="trainers"),
    path('gallery/', views.gallery, name="gallery"),
]