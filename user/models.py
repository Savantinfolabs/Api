from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date
class CustomUser(AbstractUser): 
    id=models.IntegerField(auto_created=True, primary_key=True) 
    username = models.CharField(max_length = 50, blank = False, null = False, unique = True)
    email = models.EmailField(('email address'), unique = True)
    # native_name = models.CharField(max_length = 5)
    phone=models.CharField(max_length=10,blank=True,null=True)
    total_fees=models.IntegerField(blank=True,null=True)
    Paid_fees=models.IntegerField(blank=True,null=True)
    remaining_fees=models.IntegerField(blank=True,null=True)
    GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES, default='Other')
    session_token=models.CharField(max_length=10,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.username)