from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='site/logo')

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = '1. Site'

    def __str__(self):
        return self.name

# New User
class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='users/avatars/%Y/%m/%d',
        default='users/avatars/default.jpg',
    )
    bio = models.TextField(max_length=500, null=True)
    location = models.CharField(max_length=30, null=True)
    website = models.CharField(max_length=100, null=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = '2. User'

    def __str__(self):
        return self.username
