from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    photo = CloudinaryField('image')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
    # def get_absolute_url(self):
    #     return reverse('user_profile', args=[str(self.user.username)])
