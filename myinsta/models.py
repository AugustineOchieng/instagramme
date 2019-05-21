from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField(max_length=100)
    image = models.ImageField(upload_to = 'studio/', default="")
    date_posted = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
      return self.image_name


