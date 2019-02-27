from django.urls import path
from . import views

urlpatterns = [
    #path del blog
    path('copyright/', views.copyright, name="copyright"),
    path('faq/', views.faq, name="faq"),
    path('privacy/', views.privacy, name="privacy"),
]