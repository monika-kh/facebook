from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




class Facebook(AbstractUser):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='facebook', on_delete=models.CASCADE)
    #facebook_id = models.CharField(max_length=100)
    #facebook_url = models.CharField(max_length=200, default='')
    #first_name = models.CharField(max_length=200, default='')
    #last_name = models.CharField(max_length=200, default='')
    #verified = models.CharField(max_length=200, default='')
    name = models.CharField(max_length=200, default='')
    language = models.CharField(max_length=200, default='')
    hometown = models.CharField(max_length=200, default='')
    #email = models.CharField(max_length=200, default='', db_index=True)
    gender = models.CharField(max_length=200, default='')
    birthdate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, default='')
    #timezone = models.CharField(max_length=200, default='')
    #accesstoken = models.CharField(max_length=2000, default='')
