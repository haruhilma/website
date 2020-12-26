# Generated by Django 3.1.4 on 2020-12-25 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weddingApp', '0002_categoryevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=255)),
                ('event_description', models.TextField()),
                ('event_location', models.CharField(max_length=255)),
                ('event_shedule', models.DateTimeField()),
                ('event_id_kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weddingApp.categoryevent')),
            ],
        ),
    ]
