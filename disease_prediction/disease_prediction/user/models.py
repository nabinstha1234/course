import os
import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from .manager import UserManager


def get_profile_picture_upload_path(_, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('user/profile-pictures/', filename)


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.UUIDField(
        max_length=150,
        unique=True,
        null=True,
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
        default=uuid.uuid4
    )
    email = models.EmailField(max_length=45, unique=True, error_messages={
        'unique': "A user with that email already exists.",
    }, )
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45, null=True, blank=True)
    last_name = models.CharField(max_length=45)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def display_name(self):
        return f"{self.first_name} {self.last_name}" if not self.middle_name \
            else f"{self.first_name} {self.middle_name} {self.last_name}"

    def __str__(self):
        return f"{self.email}"

    def save(self, *args, **kwargs):
        self.email = self.email.lower()

        instance = super().save(*args, **kwargs)

        return instance

class Country(models.Model):
    name = models.CharField(max_length=100,null=True)
    iso3 = models.CharField(max_length=100,null=True)
    iso2 = models.CharField(max_length=10, null=True)
    phonecode = models.CharField(max_length=100,null=True)
    captial = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"

class State(models.Model):
    name = models.CharField(max_length=100, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    country_code = models.CharField(max_length=100, null=True)
    state_code = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name}"

class UserProfile(models.Model):

    DOCTOR = 0
    PATIENT = 1
    ADMIN = 2
    STATUS_CHOICES = [
        (DOCTOR, 0),
        (PATIENT, 1),
        (ADMIN, 2),
    ]
    b_firstname = models.CharField(max_length=250,null=True)
    b_lastname = models.CharField(max_length=250,null=True)
    b_middlename = models.CharField(max_length=250,null=True)
    address = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250,null=True)
    zip = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=250, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    state_name = models.CharField(max_length=250, null=True)
    apartment = models.CharField(max_length=250, null=True)
    user_status = models.CharField(max_length=2, choices=STATUS_CHOICES, null=True, default=None)


    def __str__(self):
        return f"{self.store_name}"
