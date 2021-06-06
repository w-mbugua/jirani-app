from django.test import TestCase
from .models import Neighborhood, Business, Contact, Admin
from django.contrib.auth import get_user_model

class NeighborhoodModelTest(TestCase):
    def setUp(self):
        self.user1 =  get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password='secret'
        )
        self.admin1 = Admin(person=self.user1)
        self.admin1.save()
        self.area1 = Neighborhood.objects.create(name='area51', location='nairobi', admin=self.admin1)
        self.area1.save()
        self.bizness = Business.objects.create(name='dining place', neighborhood=self.area1, owner=self.user1, email='place@dining.com')
        self.bizness.save()
        
        self.new_contact = Contact(name='area1 Hospital', category='Health', email='area1hospital@gmail.com', phone_number='+254678456', neighborhood=self.area1)
        self.new_contact.save()

    def test_neighborhoodinstance(self):
        self.assertTrue(isinstance(self.area1, Neighborhood))
        self.assertTrue(isinstance(self.bizness, Business))
        self.assertTrue(isinstance(self.new_contact, Contact))

    def test_neighborhoodcountmethods(self):
        self.assertEqual(self.area1.count_businesses(), 1)
        self.assertEqual(self.area1.contact_count(), 1)
    
    def test_locations(self):
        self.assertTrue(self.new_contact.get_location(), self.area1)
