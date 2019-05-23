from django.test import TestCase
from .models import Profile, Image

# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.kevin = Profile(id = 132, profile_photo = "",bio = "I love traveling", userId = 1)

      # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kevin,Profile))
    
    def test_initialization(self):
        self.assertEqual(self.kevin.profile_photo,"")
        self.assertEqual(self.kevin.bio, "I love traveling")
        self.assertEqual(self.kevin.userId, 1)

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


