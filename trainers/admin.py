from django.contrib import admin
from .models import Trainer

# Register your models here.
class TrainerAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Trainer,TrainerAdmin)