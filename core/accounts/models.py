from django.db.models import *
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser , PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = EmailField(max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(Model):
    user = ForeignKey('User', on_delete=CASCADE, related_name='user_profile')
    first_name = CharField(max_length=255, blank=False)
    last_name = CharField(max_length=255, blank=False)
    phone_number = BigIntegerField(null=True, blank=True)
    image = ImageField(null=True, blank=True, upload_to="media/profile")
    description = TextField(null=True, blank=True)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)

    def __str__(self):
        return self.user.email 


@receiver(post_save, sender=User)
def add_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
