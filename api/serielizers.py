from rest_framework.serializers import Serializer,ModelSerializer
from . import models
from rest_framework import serializers
class LoginSerielizer(Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
class SignUpSerielizer(ModelSerializer):
    class Meta:
        model=models.Profile
        fields="__all__"
   
