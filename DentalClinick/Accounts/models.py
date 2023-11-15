from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.contrib.auth.hashers import make_password

# Create your models here.

GENDER_CHOICES = (
    ('m', 'male'),
    ('f', 'female')
)


# Create your models here.

class UserAdmin(AbstractUser):
    fname = models.CharField(max_length=18, default='')
    lname = models.CharField(max_length=18, default='')
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthdate = models.DateField(null=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.fname + ' ' + self.lname


class HomeInfo(models.Model):
    admin = models.ForeignKey(UserAdmin, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    title_ar_field = models.CharField(max_length=200)
    description_ar_field = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')
    background = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AddDr(models.Model):
    admin = models.ForeignKey(UserAdmin, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    time = models.CharField(max_length=255)

    name_ar_field = models.CharField(max_length=200)
    job_ar_field = models.CharField(max_length=200)
    description_ar_field = models.CharField(max_length=255)
    time_ar_field = models.CharField(max_length=255)

    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AddWork(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    dr = models.ForeignKey(AddDr, related_name='addwork_dr', on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=255)

    title_ar_field = models.CharField(max_length=200)
    category_ar_field = models.CharField(max_length=200)
    dr_ar_field = models.ForeignKey(AddDr, related_name='addwork_dr_ar_field', on_delete=models.CASCADE, null=True)
    description_ar_field = models.CharField(max_length=255)

    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UserContact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
