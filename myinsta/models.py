from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.models import HTMLField
import datetime as dt

class Profile(models.Model):
  profile_photo = models.ImageField(upload_to='profile_images/', default="")
  bio = models.TextField(max_length = 100)
  userId =models.IntegerField(default = 0)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  
  

  def __str__(self):
        return self.bio


class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField(max_length=100)
    image = models.ImageField(upload_to = 'studio/', default="")
    date_posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    poster_id=models.IntegerField(default=0)
    
    

    def __str__(self):
      return self.image_name


class Comments(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    commented = models.CharField(max_length = 200)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      comments=Comments.objects.filter(image_pk = id)
      return self.commented


