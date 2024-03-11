from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=64, unique=True)
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    organization = models.ForeignKey(
        'Organization', on_delete=models.PROTECT, null=True,
        blank=True, related_name='users'
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'id{self.id} - {self.username}'


class Organization(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    address = models.CharField(max_length=256)
    postcode = models.CharField(max_length=16)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    organizations = models.ManyToManyField(Organization, through='EventOrganization')
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title


class EventOrganization(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
