from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='site/logo/')

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = '1. Sites'

    def __str__(self):
        return self.name

# New user model
class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='user/avatars/%Y/%m/%d/',
        default='user/avatars/default.jpg',
    )
    bio = models.TextField(max_length=500, null=True)
    location = models.CharField(max_length=30, null=True)
    website = models.CharField(max_length=100, null=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = '2. Users'

    def __str__(self):
        return self.username