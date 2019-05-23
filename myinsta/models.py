from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
  profile_photo = models.ImageField(upload_to='profile_images/', default="")
  bio = models.TextField(max_length = 100)
  userId =models.IntegerField(default = 0)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  
  def save_profile(self):
        self.save()

  def delete_profile(self):
        self.delete()   

  def update_bio(self,bio):
        self.bio = bio
        self.save()

  @classmethod
  def update_profile(cls,profile,update):
      updated = cls.objects.filter(Image_name=profile).update(name=update)
      return updated

  @classmethod
  def search_by_username(cls,search_term):
      profile = cls.objects.filter(user__username__icontains=search_term)
      return profile

  def __str__(self):
        return self.bio


