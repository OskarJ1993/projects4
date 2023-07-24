from django.contrib.auth.models import AbstractUser
from django.db import models

#CustomUser to Model to Save Register User
class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    first_name = models.CharField(verbose_name='first_name', max_length=255)
    last_name = models.CharField(verbose_name='last_name', max_length=255)

    username = models.CharField(verbose_name='username', max_length=255,unique=True)
     
    USERNAME_FIELD='username'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.email
