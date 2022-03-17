from arcaucouapp.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']
        
class UserCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = User.objects.create_user(**validated_data)
        return instance

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']