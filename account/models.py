from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', '女')), default='female', verbose_name='性别')


