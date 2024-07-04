from django.db import models

# Create your models here.
class Profile(models.Model):
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    orgName=models.CharField(max_length=50)
    pic=models.URLField(default=None,null=True)
    location=models.TextField()
    userType=models.CharField(max_length=20)
