from django.test import TestCase
from .models import Profile, Image

# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.kevin = Profile(id = 132, profile_photo = " ",bio = "I love traveling", userId = 1)

      # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kevin,Profile))
    
    

        # Testing Save method
    def test_save(self):
        self.kevin.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    # Testing Delete method
    def test_delete(self):
        self.kevin.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)


class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Profile class test
        self.kevin = Profile( bio = "I love traveling", userId = 1)

        # Image class Test
        self.image = Image(image = " ",image_name="nature goodness",image_caption = "", date_posted = "10/2/2019", poster_id = 2)
        self.image.save_image()


    # # Testing  instance
    def test_instance(self):
         self.assertTrue(isinstance(self.image,Image))

    # Testing Save method
    def test_save_method(self):
         self.image.save_image()
         images = Image.objects.all()
         self.assertTrue(len(images)>0)

     # Testing Delete method
    def test_delete_method(self):
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)


     # Testing getting image by id 
    def test_get_image(self):
        images = Image.get_image(self.image.id)
        self.assertTrue(images == self.image)

    # Testing Update method
    def test_update_method(self):
        image = Image.get_image(self.image.id)
        image.update_image_caption("new image")
        image = Image.get_image(self.image.id)
        self.assertFalse(image.image == "new_image")