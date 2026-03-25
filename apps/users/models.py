from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    # We need a custom manager because we removed the 'username' field.
    # Django's default manager expects username to exist.

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)  # lowercase the domain part
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # hashes the password — NEVER store plaintext
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None                    # REMOVE the username field
    email = models.EmailField(unique=True)  # email is now the login field

    jlpt_level = models.CharField(max_length=2, default='N5')
    xp = models.PositiveIntegerField(default=0)
    streak = models.PositiveIntegerField(default=0)
    last_study_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'   # tells Django to use email for login
    REQUIRED_FIELDS = []       # no other required fields for createsuperuser
    objects = UserManager()    # use our custom manager
