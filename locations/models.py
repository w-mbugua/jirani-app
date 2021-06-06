from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField


class Admin(models.Model):
    person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.person.username

class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name

    def get_count(self):
        residents = self.profiles.all().count()
        return residents
    
    def count_businesses(self):
        businesses_count = self.businesses.all().count()
        
        return businesses_count
    
    def contact_count(self):
        return self.contacts.all().count()
    
    @classmethod
    def find_business(cls, biz_id):
        business = cls.objects.get(id=biz_id)
        return business

    @classmethod
    def search_business(cls, searchterm):
        business = cls.objects.filter(name__icontains = searchterm)
        return business
    
    # def get_absolute_url(self):
    #     return reverse('neighborhood_details', args=[str(self.pk)])

class Business(models.Model):
    name = models.CharField(max_length=30)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='businesses')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
    @classmethod
    def search_business(cls, searchterm):
        business = cls.objects.filter(name__icontains = searchterm)
        return business
    


CATEGORY_CHOICES = (('Police', 'Police'), ('Health', 'Health'))

class Contact(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=6)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='contacts')

    def get_location(self):
        return self.neighborhood
    
