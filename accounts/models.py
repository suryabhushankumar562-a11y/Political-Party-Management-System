from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):

    ROLE_CHOICES =(
        ('SUPERADMIN', 'Super Admin'),
        ('ADMIN', 'Admin'),
        ('MEMBER', 'Member'),
        ('VOLUNTEER', 'Volunteer'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='MEMBER'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
