from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email',max_length=255,unique=True)
    phone = models.CharField(null=True,max_length=255)
    type = models.CharField(null=True,max_length=255)
    department =  models.CharField(max_length=255,blank=True,null=True)
    REQUIRED_FIELDS = ['username','phone','first_name','last_name','type']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
