from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Title",max_length=200)
    content = RichTextField(verbose_name= "Content")
    created = models.DateField(auto_now_add=True, verbose_name="Created Date")
    updated =models.DateField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        ordering = ['title']
    
    def __str__(self):
        return self.title
