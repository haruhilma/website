# Generated by Django 3.1.4 on 2020-12-25 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingApp', '0003_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='slider_images',
            field=models.ImageField(default=0, upload_to='upload/slider/'),
            preserve_default=False,
        ),
    ]
