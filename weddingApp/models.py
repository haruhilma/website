from djongo import models

# Create your models here.

class Slider(models.Model):
    slider_id=models.ObjectIdField()
    slider_title=models.CharField(max_length=255)
    slider_description=models.TextField()
    slider_created_by=models.IntegerField()
    slider_created_at=models.DateTimeField()
