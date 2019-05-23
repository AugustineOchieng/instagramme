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


class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'studio/', default="")
    date_posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    poster_id=models.IntegerField(default=0)
    
    @classmethod
    def get_images(cls):
        image = cls.objects.all()
        return image

    @classmethod
    def get_image(cls, image_id):
        single_image = cls.objects.get(id=image_id)
        return single_image

    def save_image(self):
        self.save()

    def delete_image(self):
        Image.objects.filter().delete()

    def update_image_caption(self, update):
        self.image_caption = update
        self.save()

    class Meta:
        ordering = ['-id']

    def __str__(self):
      return self.image_name


class Comments(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    commented = models.CharField(max_length = 200)
    
    @classmethod
    def get_comments(cls):
        comment = cls.objects.all()
        return comment

    def save_comment(self):
        self.save()     

    def delete_comment(self):
        Image.objects.filter().delete()

    def update_comment(self, update):
        self.comment_message = update
        self.save()

    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image_pk = id)
        return comments
    
    def __str__(self):
      comments=Comments.objects.filter(image_pk = id)
      return self.commented


