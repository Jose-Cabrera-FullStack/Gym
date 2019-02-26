from django.urls import path
from . import views

urlpatterns = [
    #path del trainers
    path('', views.trainers, name="trainers"),
    path('<int:trainer_id>/', views.trainer, name="trainer"),
]