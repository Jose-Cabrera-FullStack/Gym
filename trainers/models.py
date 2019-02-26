from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    feature = models.CharField(max_length=200, verbose_name="Feature")
    content = RichTextField(verbose_name="Content")
    image = models.ImageField(verbose_name="Image",upload_to="trainers", null=True,blank=True)
    created = models.DateTimeField(verbose_name= "Creation Date", auto_now_add=True)
    updated = models.DateTimeField(verbose_name= "Updation Date", auto_now_add=True)


    class Meta:
        verbose_name = "Trainer"
        verbose_name_plural = "Trainers"
        ordering = ['-created']

    def __str__(self):
        return self.name
        