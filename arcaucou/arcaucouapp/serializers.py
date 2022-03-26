from django.contrib.auth.models import User
from arcaucouapp.models import Group
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
    def create(self, validated_data):
        return User.objects.create(email=validated_data['email'], 
                                   username=validated_data['username'], 
                                   password=make_password(validated_data['password']))
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name','password']
    def create(self, validated_data):
        return Group.objects.create(name=validated_data['name'],
                                    password=make_password(validated_data['password']))