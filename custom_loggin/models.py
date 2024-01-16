from django.db import models
from django.contrib.auth.models import AbstractUser
from custom_loggin.myusermanager import MyUserManager


class MyUser(AbstractUser):
    username = None
    mobile = models.CharField(max_length=11, unique=True)
    otp = models.IntegerField(blank=True, null=True)
    otp_creat_time = models.DateTimeField(auto_now=True)

    #profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    #date_of_birth = models.DateField(null=True, blank=True)


    objects = MyUserManager()

    USERNAME_FIELD = "mobile"

    REQUIRED_FIELDS = []

    backend = 'custom_loggin.backend.ModelBackend'

# class UserProfile(models.Model):
#     user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
#     address = models.CharField(max_length=255, blank=True, null=True)
