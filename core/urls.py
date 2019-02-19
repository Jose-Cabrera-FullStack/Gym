from django.urls import path
from . import views

urlpatterns = [

    #path del core
    path('', views.home, name="home"),
    path('about-us/', views.about_us, name="about-us"),
    path('trainers/', views.trainers, name="trainers"),
    path('classes/', views.classes, name="classes"),
    path('blog/', views.blog, name="blog"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact-us/', views.contact_us, name="contact-us"),
]