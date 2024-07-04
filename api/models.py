from django.db import models

# Create your models here.
class Profile(models.Model):
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    orgName=models.CharField(max_length=50)
    pic=models.URLField(default=None,null=True)
    location=models.TextField()
    userType=models.CharField(max_length=20)
class Post(models.Model):
    fromUser=models.ForeignKey(Profile,on_delete=models.PROTECT,related_name="fromUser")
    toUser=models.OneToOneField(Profile,on_delete=models.PROTECT,default=None,null=True,related_name="toUser")
    quantity=models.FloatField()
    status=models.IntegerField()#0 - not applied, 1 - delivering, 2 - delivered