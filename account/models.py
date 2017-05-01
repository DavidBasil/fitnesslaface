from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """User's profile model"""
    user = models.OneToOneField(User)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return 'Profile of  {}'.format(self.user.username)
