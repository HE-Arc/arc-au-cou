from django.contrib.auth.models import User
from arcaucouapp.models import Sudoku, Group, Leaderboard, UserToGroup
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create(email=validated_data['email'],
                                   username=validated_data['username'],
                                   password=make_password(validated_data['password']))
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'password']

    def create(self, validated_data):
        return Group.objects.create(name=validated_data['name'],
                                    password=make_password(validated_data['password']))

class SudokuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sudoku
        fields = ['url', 'start_sudoku', 'end_sudoku', 'date']
        
class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = '__all__'
    def create(self, validated_data):
        print(validated_data)
        return Leaderboard.objects.create(time=validated_data['time'],
                                          user=validated_data['user'])
        
class UserToGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToGroup
        fields = '__all__'
    def create(self, validated_data):
        return UserToGroup.objects.create(user=validated_data['user'],
                                          group=validated_data['group'])
