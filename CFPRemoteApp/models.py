from django.db import models

# Create your models here.
class CFPUsers(models.Model):
    UName = models.CharField(max_length=30, primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
