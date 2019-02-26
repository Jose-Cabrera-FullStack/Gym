from django.shortcuts import render, get_object_or_404
from .models import Trainer
# Create your views here.
def trainers(request):
    trainers = Trainer.objects.all()
    return render(request,"trainers/trainers.html",{"trainers":trainers})

def trainer(request,trainer_id):
    trainer = get_object_or_404(Trainer,id=trainer_id)
    trainers = Trainer.objects.filter(id=trainer_id)
    return render(request,"trainers/trainer.html",{'trainer':trainer,"trainers":trainers})