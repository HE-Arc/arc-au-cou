from arcaucouapp.models import User, Group
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    def create(self, validated_data):
        return User.objects.create(email=validated_data['email'], 
                                   username=validated_data['username'], 
                                   password=make_password(validated_data['password']))
        
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
    def create(self, validated_data):
        user = User.objects.filter(username=validated_data['username'])
        print(user.values()[0]['password'])
        print(validated_data['password'])
        print(check_password(validated_data['password'],user.values()[0]['password']))
        if check_password(validated_data['password'],user.values()[0]['password']):
            return user.values()[0]
        else:
            return None


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']