# Generated by Django 2.1.5 on 2019-02-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('feature', models.CharField(max_length=200, verbose_name='Feature')),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery', verbose_name='Image')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Updation Date')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
                'ordering': ['-created'],
            },
        ),
    ]
