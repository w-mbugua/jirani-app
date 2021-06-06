from django.test import TestCase
from .models import Profile
from django.contrib.auth import get_user_model
from locations.models import Neighborhood, Admin


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user1 =  get_user_model().objects.create_user(username = 'testuser', email = 'test@email.com', password='secret')
        self.admin1 = Admin(person=self.user1)
        self.admin1.save()
        self.area1 = Neighborhood.objects.create(name='area51', location='nairobi', admin=self.admin1)
        self.area1.save()
        self.new_profile = Profile(user = self.user1, bio='here to test', neighborhood=self.area1)
    
    def test_profile_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))
    
    def test_string_method(self):
        self.assertEqual(str(self.new_profile), self.user1.username)

