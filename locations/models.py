from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
 
    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('neighborhood_details', args=[str(self.pk)])


class Business(models.Model):
    name = models.CharField(max_length=30)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='businesses')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name
