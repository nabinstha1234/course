from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models

from .managers import CustomUserManager


# Create your models here.


class CustomUser(AbstractUser):
    pass
    # username = None
    # email = models.EmailField(_('email address'), unique=True)
    #
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    #
    # objects = CustomUserManager()
    #
    # def __str__(self):
    #     return self.email
