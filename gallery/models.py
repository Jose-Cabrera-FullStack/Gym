from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    feature = models.CharField(max_length=200, verbose_name="Feature")
    image = models.ImageField(verbose_name="Image",upload_to="gallery", null=True,blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                 processors=[ResizeToFill(345, 345)],
                                 format='JPEG',
                                 options={'quality': 60})
    created = models.DateTimeField(verbose_name= "Creation Date", auto_now_add=True)
    updated = models.DateTimeField(verbose_name= "Updation Date", auto_now_add=True)


    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
        ordering = ['-created']

    def __str__(self):
        return self.name
        