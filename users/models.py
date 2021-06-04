from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from cloudinary.models import CloudinaryField


class CustomUser(AbstractUser):
    neighborhood = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50, null=True, blank=True)


class Post(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    body = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.body[:20]
    
    # def get_absolute_url(self):
    #     return reverse('post_detail', args=[str(self.id)])
