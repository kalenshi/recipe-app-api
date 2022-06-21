"""
This module contains the default user model
"""

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """
    The manager object for the user model
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create, save and return a new user
        """
        if not email:
            raise ValueError("Email must be provided for all users.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates the superuser for the application
        """
        user = self.create_user(email=email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Creates the user model for out application/system
    """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
