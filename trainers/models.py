from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    feature = models.CharField(max_length=200, verbose_name="Feature")
    facebook = models.URLField(max_length=200, verbose_name="Facebook", null=True,blank=True)
    twitter = models.URLField(max_length=200, verbose_name="Twitter", null=True,blank=True)
    linkedin = models.URLField(max_length=200, verbose_name="Linkedin", null=True,blank=True)
    instagram = models.URLField(max_length=200, verbose_name="Instagram", null=True,blank=True)
    content = RichTextField(max_length=1000, verbose_name="Content")
    image = models.ImageField(verbose_name="Image",upload_to="trainers", null=True,blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                 processors=[ResizeToFill(345, 345)],
                                 format='JPEG',
                                 options={'quality': 60})
    crossfit = models.PositiveSmallIntegerField(verbose_name="Crossfit",default=50)
    yoga = models.PositiveSmallIntegerField(verbose_name="Yoga",default=50)
    step = models.PositiveSmallIntegerField(verbose_name="Step",default=50)
    body = models.PositiveSmallIntegerField(verbose_name="Body",default=50)
    gap = models.PositiveSmallIntegerField(verbose_name="GAP",default=50)
    spinning = models.PositiveSmallIntegerField(verbose_name="Spinning",default=50)
    created = models.DateTimeField(verbose_name= "Creation Date", auto_now_add=True)
    updated = models.DateTimeField(verbose_name= "Updation Date", auto_now_add=True)


    class Meta:
        verbose_name = "Trainer"
        verbose_name_plural = "Trainers"
        ordering = ['-created']

    def __str__(self):
        return self.name
        